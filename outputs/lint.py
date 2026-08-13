#!/usr/bin/env python3
"""Lint pass over the wiki, per AGENT.md workflow:

  1. Scan all wiki pages for contradictions
  2. Identify orphan pages (no incoming links)
  3. Flag missing concepts referenced but not created
  4. Find stale claims superseded by newer sources
  5. Save results to outputs/lint-YYYY-MM-DD.md

Run from the project root:

    python3 outputs/lint.py

Produces `outputs/lint-YYYY-MM-DD.md` and prints a summary.
"""

from __future__ import annotations

import datetime as dt
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

WIKI_ROOT = Path(__file__).resolve().parent.parent / "wiki"
ASSETS_ROOT = Path(__file__).resolve().parent.parent / "assets"
OUTPUTS = Path(__file__).resolve().parent

# Image extensions recognized when resolving wikilinks.
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".excalidraw"}

TYPE_BY_DIR = {
    "concepts": "concept",
    "entities": "entity",
    "source-summary": "source-summary",
    "comparison": "comparison",
}

# Wiki-internal pages that are allowed to have no incoming links:
#   - index.md itself (it IS the catalog)
#   - log.md (append-only audit log)
#   - verbatim clippings (their value is in being reference text, not in being linked)
#   - extracted .txt files (reference text for the manual)
EXEMPT_FROM_ORPHAN_CHECK = {
    "index.md",
    "log.md",
    "gt-ac5300-pcmag-review-original.md",
    "gt-ac5300-manual-text.txt",
}

# Pages that are exempt from frontmatter / type checks (verbatim clippings and
# raw text extracts — they carry their own non-wiki metadata).
EXEMPT_FROM_METADATA_CHECK = {
    "gt-ac5300-pcmag-review-original.md",
    "gt-ac5300-manual-text.txt",
}

# Wikilink regex. Handles `[[target]]`, `[[target|alias]]`, `[[target#frag]]`,
# `[[../relative/path]]`, and markdown-escaped pipes (`\|`).
WIKILINK_RE = re.compile(
    r"\[\["
    r"([^\]|#]+)"          # target
    r"(?:#[^\]|]+)?"        # optional fragment
    r"(?:\\?\|[^\]]+)?"     # optional alias (markdown-escapes | as \|)
    r"\]\]"
)


# ---------- ingestion -----------------------------------------------------

def load_page(path: Path) -> dict:
    """Load a wiki page's frontmatter and body."""
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(WIKI_ROOT.parent).as_posix()
    if text.lstrip().startswith("---"):
        # Has YAML frontmatter.
        end = text.index("---", 3)
        fm = yaml.safe_load(text[3:end]) or {}
        body = text[end + 3:]
    else:
        fm = {}
        body = text
    return {"path": path, "rel": rel, "frontmatter": fm, "body": body}


def load_all_pages() -> list[dict]:
    pages = []
    for sub in TYPE_BY_DIR:
        d = WIKI_ROOT / sub
        if not d.exists():
            continue
        for p in sorted(d.iterdir()):
            if p.suffix in (".md", ".txt"):
                pages.append(load_page(p))
    # Also load index.md and log.md as edges (not subject to lint themselves).
    return pages


# ---------- helpers --------------------------------------------------------

def normalize_target(target: str) -> str:
    """Resolve a wikilink target against the wiki/ root or the assets/ tree.

    Tries (in order):
      1. The path verbatim under wiki/
      2. The path verbatim under assets/
      3. The bare basename under each wiki/ subdir (handles `../concepts/foo` -> `concepts/foo`)
      4. The bare basename under each assets/ subdir
    All lookups are tried with extensions "", ".md", ".txt", and image extensions.
    """
    target = target.rstrip("\\").strip()
    if not target:
        return ""
    name = target.rsplit("/", 1)[-1]
    exts = ("", ".md", ".txt", *IMAGE_EXTS)

    def _rel(cand: Path) -> str:
        return cand.relative_to(WIKI_ROOT.parent).as_posix()

    # 1. verbatim under wiki/
    for ext in exts:
        cand = (WIKI_ROOT / target)
        if ext:
            cand = cand.with_suffix(ext)
        if cand.exists():
            return _rel(cand)
    # 2. verbatim under assets/
    for ext in exts:
        cand = (ASSETS_ROOT / target)
        if ext:
            cand = cand.with_suffix(ext)
        if cand.exists():
            return _rel(cand)
    # 3. bare basename under each wiki/ subdir
    for ext in (".md", ".txt"):
        for sub in TYPE_BY_DIR:
            cand = WIKI_ROOT / sub / name_with_ext(name, ext)
            if cand.exists():
                return _rel(cand)
    # 4. bare basename under each assets/ subdir
    for ext in IMAGE_EXTS:
        for sub in ("figures", "diagrams"):
            cand = ASSETS_ROOT / sub / name_with_ext(name, ext)
            if cand.exists():
                return _rel(cand)
    return target  # unresolved


def name_with_ext(name: str, ext: str) -> str:
    return name if name.endswith(ext) else name + ext


def all_wikilinks(page: dict) -> list[str]:
    """Return all wikilink targets referenced by a page (resolved)."""
    targets = []
    for m in WIKILINK_RE.finditer(page["body"]):
        targets.append(normalize_target(m.group(1)))
    return targets


# ---------- checks ---------------------------------------------------------

def find_orphans(pages: list[dict]) -> list[dict]:
    """Pages with no incoming links from any other wiki page or the index."""
    # Edges: every wiki page (incl. index.md) -> all pages it links to.
    incoming: dict[str, set[str]] = defaultdict(set)
    extras = [load_page(p) for p in (WIKI_ROOT / "index.md",) if (WIKI_ROOT / "index.md").exists()]
    extras += [load_page(p) for p in (WIKI_ROOT / "log.md",) if (WIKI_ROOT / "log.md").exists()]
    for page in pages + extras:
        for target in all_wikilinks(page):
            incoming[target].add(page["rel"])
    orphans = []
    for page in pages:
        if page["path"].name in EXEMPT_FROM_ORPHAN_CHECK:
            continue
        if incoming.get(page["rel"], set()) == set():
            orphans.append(page)
    return orphans


def find_missing_concepts(pages: list[dict]) -> list[tuple[str, str]]:
    """Wikilinks whose target does not resolve to an existing file."""
    missing = []
    seen = set()
    for page in pages + [load_page(WIKI_ROOT / "index.md")]:
        for m in WIKILINK_RE.finditer(page["body"]):
            raw = m.group(1).rstrip("\\").strip()
            if not raw or raw.startswith("http"):
                continue
            resolved = normalize_target(raw)
            # Distinguish "didn't resolve" vs "raw looks unresolved".
            if resolved == raw:
                # normalize_target only returns the raw input on miss.
                key = (page["rel"], raw)
                if key not in seen:
                    seen.add(key)
                    missing.append((page["rel"], raw))
    return missing


# Specific facts to cross-check for contradictions.
# Each value is a (label, regex) pair — we collect all matches across pages.
FACT_PATTERNS = [
    ("LAN ports (number)", re.compile(r"\b(\d+)\s*(?:×|x)?\s*(?:Gigabit|GbE)?\s*(?:LAN|Ethernet)\s*ports?\b", re.IGNORECASE)),
    ("USB ports (number)", re.compile(r"\b(\d+)\s*×?\s*USB\b", re.IGNORECASE)),
    ("Antennas (number)", re.compile(r"\b(\d+)\s*(?:×|x)?\s*(?:external|removable|adjustable)?\s*antennas?\b", re.IGNORECASE)),
    ("RAM amount", re.compile(r"\b(\d+)\s*(?:GB|MB)\s*(?:of\s*)?(?:RAM|memory)\b", re.IGNORECASE)),
    ("Flash storage", re.compile(r"\b(\d+)\s*(?:GB|MB)\s*(?:of\s*)?flash\b", re.IGNORECASE)),
    ("Guest SSIDs", re.compile(r"\b(?:up\s+to\s+)?(\d+)\s*(?:isolated\s+)?SSIDs?\b", re.IGNORECASE)),
]


def find_contradictions(pages: list[dict]) -> dict[str, list[dict]]:
    """Collect (page, value, snippet) triples per fact; flag facts where
    values disagree.

    Snippet = ~80 chars of surrounding text so a human can tell whether a
    value is about the subject (GT-AC5300) or about a mentioned-but-different
    entity (e.g. a competitor in a comparison page).
    """
    fact_values: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    for page in pages:
        body = page["body"]
        for label, regex in FACT_PATTERNS:
            for m in regex.finditer(body):
                start = max(0, m.start() - 50)
                end = min(len(body), m.end() + 50)
                snippet = body[start:end].replace("\n", " ").strip()
                fact_values[label][m.group(1)].append({
                    "page": page["rel"],
                    "snippet": snippet,
                })
    contradictions = {}
    for label, value_to_hits in fact_values.items():
        if len(value_to_hits) > 1:
            contradictions[label] = [
                {"value": value, "hits": hits}
                for value, hits in value_to_hits.items()
            ]
    return contradictions


# Markers that flag stale / superseded / unverified claims.
STALE_MARKERS = [
    "[needs verification]",
    "[stale]",
    "[superseded]",
    "[historical]",
    "(historical",
    "(superseded",
    "Open verification",
    "Open verifications",
    "Known issues",
    "## Caveats",
    "End-of-life",
    "end of life",
    "end-of-life",
    "no longer be updated",
]


def find_stale_claims(pages: list[dict]) -> dict[str, list[str]]:
    """For each page, list the stale markers it contains."""
    stale = {}
    for page in pages:
        hits = []
        for marker in STALE_MARKERS:
            if marker in page["body"]:
                hits.append(marker)
        if hits:
            stale[page["rel"]] = sorted(set(hits))
    return stale


def find_metadata_issues(pages: list[dict]) -> list[str]:
    """Cross-check frontmatter consistency."""
    issues = []
    for page in pages:
        rel = page["rel"]
        if page["path"].name in EXEMPT_FROM_METADATA_CHECK:
            continue
        fm = page["frontmatter"]
        if not fm:
            issues.append(f"{rel}: no frontmatter")
            continue
        # type must match directory.
        expected_type = TYPE_BY_DIR.get(page["path"].parent.name)
        if expected_type and fm.get("type") != expected_type:
            issues.append(f"{rel}: type={fm.get('type')!r}, expected {expected_type!r}")
        # confidence must be numeric and in [0, 1].
        c = fm.get("confidence")
        if c is None:
            issues.append(f"{rel}: missing confidence")
        elif not isinstance(c, (int, float)) or not (0 <= c <= 1):
            issues.append(f"{rel}: bad confidence {c!r}")
        # sources must be a list (possibly empty).
        s = fm.get("sources")
        if s is None:
            issues.append(f"{rel}: missing sources")
        elif not isinstance(s, list):
            issues.append(f"{rel}: sources is not a list")
    return issues


def find_catalog_gaps(pages: list[dict]) -> list[dict]:
    """Pages that should appear in index.md but don't.

    The catalog is the master index; anything in concepts/, entities/,
    source-summary/, or comparison/ that's not listed there is a gap.
    """
    index_text = (WIKI_ROOT / "index.md").read_text(encoding="utf-8")
    gaps = []
    for page in pages:
        rel = page["rel"]
        # Only check wiki pages that ought to be catalogued.
        if page["path"].name in EXEMPT_FROM_METADATA_CHECK:
            continue
        if page["path"].suffix != ".md":
            continue  # skip .txt files
        # Look for the bare-name reference in index.md (e.g. `[[concepts/foo]]`).
        bare = page["path"].relative_to(WIKI_ROOT).as_posix()  # "concepts/foo.md"
        bare_link = bare[:-3]  # "concepts/foo"
        if f"[[{bare_link}]]" not in index_text:
            gaps.append(page)
    return gaps


# ---------- report ---------------------------------------------------------

def write_report(orphans, missing, contradictions, stale, meta_issues, catalog_gaps, today):
    lines = []
    lines.append(f"# Wiki Lint — {today}")
    lines.append("")
    lines.append("Generated by `outputs/lint.py` per the Lint workflow in `AGENT.md`.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Orphan pages (no incoming links): **{len(orphans)}**")
    lines.append(f"- Catalog gaps (pages not in `index.md`): **{len(catalog_gaps)}**")
    lines.append(f"- Missing concepts (unresolved wikilinks): **{len(missing)}**")
    total_hits = sum(len(vb['hits']) for vs in contradictions.values() for vb in vs)
    lines.append(f"- Contradictions across pages: **{total_hits}** hits across **{len(contradictions)}** facts")
    lines.append(f"- Pages with stale / superseded markers: **{len(stale)}**")
    lines.append(f"- Frontmatter / metadata issues: **{len(meta_issues)}**")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Orphans
    lines.append("## 1. Orphan pages (no incoming links)")
    lines.append("")
    if orphans:
        lines.append("These pages exist on disk but are not referenced from `index.md` or any other wiki page. Either they are not catalogued, or nothing links to them.")
        lines.append("")
        for p in orphans:
            fm = p["frontmatter"]
            title = fm.get("title", "(no title)")
            ttype = fm.get("type", "?")
            conf = fm.get("confidence", "?")
            lines.append(f"- `{p['rel']}` — **{title}** (`type={ttype}`, `confidence={conf}`)")
    else:
        lines.append("✓ None found.")
    lines.append("")

    # Catalog gaps
    lines.append("## 2. Catalog gaps (page not in `index.md`)")
    lines.append("")
    if catalog_gaps:
        lines.append("Pages that should appear in `wiki/index.md` but do not. The catalog is the master entry point, so missing entries mean the page is invisible to humans browsing the index.")
        lines.append("")
        for p in catalog_gaps:
            fm = p["frontmatter"]
            title = fm.get("title", "(no title)")
            ttype = fm.get("type", "?")
            lines.append(f"- `{p['rel']}` — **{title}** (`type={ttype}`)")
    else:
        lines.append("✓ None found.")
    lines.append("")

    # Missing concepts
    lines.append("## 3. Missing concepts (unresolved wikilinks)")
    lines.append("")
    if missing:
        lines.append("Wikilinks that do not resolve to any existing wiki page or `raw/` artifact. Either create the page, or fix the link.")
        lines.append("")
        # Group by missing target.
        by_target: dict[str, list[str]] = defaultdict(list)
        for src, target in missing:
            by_target[target].append(src)
        for target in sorted(by_target):
            lines.append(f"- `[[{target}]]` referenced from:")
            for src in sorted(set(by_target[target])):
                lines.append(f"    - `{src}`")
    else:
        lines.append("✓ None found.")
    lines.append("")

    # Contradictions
    lines.append("## 4. Contradictions across pages")
    lines.append("")
    if contradictions:
        lines.append("Facts where different pages state different values. These may be intentional (different aspects of the same fact), false positives from cross-page regex matching, or genuine conflicts needing investigation. **Read the snippets** to disambiguate.")
        lines.append("")
        for label, value_blocks in contradictions.items():
            lines.append(f"### {label}")
            lines.append("")
            for vb in value_blocks:
                lines.append(f"**Value `{vb['value']}`** appears in {len(vb['hits'])} place(s):")
                for hit in vb["hits"]:
                    lines.append(f"  - `{hit['page']}` — *...{hit['snippet']}...*")
                lines.append("")
    else:
        lines.append("✓ No contradictions found among the scanned fact patterns.")
    lines.append("")

    # Stale claims
    lines.append("## 5. Stale / superseded / unverified claims")
    lines.append("")
    if stale:
        lines.append('Pages containing markers like `[needs verification]`, "historical", or "End-of-life". These are not necessarily bugs — they are candidates for re-verification on the next ingest.')
        lines.append("")
        for src, markers in sorted(stale.items()):
            lines.append(f"- `{src}` — markers: {', '.join(markers)}")
    else:
        lines.append("✓ None found.")
    lines.append("")

    # Metadata issues
    lines.append("## 6. Frontmatter / metadata issues")
    lines.append("")
    if meta_issues:
        for issue in meta_issues:
            lines.append(f"- {issue}")
    else:
        lines.append("✓ None found.")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"Generated by `outputs/lint.py` on {today}.")

    out_path = OUTPUTS / f"lint-{today}.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


def main() -> int:
    today = dt.date.today().isoformat()
    pages = load_all_pages()
    orphans = find_orphans(pages)
    catalog_gaps = find_catalog_gaps(pages)
    missing = find_missing_concepts(pages)
    contradictions = find_contradictions(pages)
    stale = find_stale_claims(pages)
    meta_issues = find_metadata_issues(pages)
    total_hits = sum(len(vb['hits']) for vs in contradictions.values() for vb in vs)
    out = write_report(orphans, missing, contradictions, stale, meta_issues, catalog_gaps, today)
    print(f"Pages scanned: {len(pages)}")
    print(f"Orphans:        {len(orphans)}")
    print(f"Catalog gaps:   {len(catalog_gaps)}")
    print(f"Missing:        {len(missing)}")
    print(f"Contradictions: {total_hits}")
    print(f"Stale markers:  {len(stale)}")
    print(f"Meta issues:    {len(meta_issues)}")
    print(f"Report:         {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
