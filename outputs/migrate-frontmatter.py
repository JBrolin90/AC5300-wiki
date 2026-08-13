#!/usr/bin/env python3
"""One-off migration: convert the wiki's prose-header convention into proper
YAML frontmatter on every wiki page.

Run from the project root:

    python3 outputs/migrate-frontmatter.py [--dry-run]

Skips verbatim clippings (pages that already start with their own YAML
frontmatter, e.g. `*-original.md`). For all other pages it:

  1. parses the H1 title, the `**Summary** / **Sources** / **Related** /
     **Last updated** / **Confidence**` block, and the body (everything
     after the first `---` divider),
  2. emits the wiki schema YAML frontmatter,
  3. writes back with frontmatter + H1 + body (prose headers are removed
     since their info is now in the YAML).

Idempotent: re-running on already-migrated pages is a no-op (they will
already have frontmatter and will be skipped).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent / "wiki"

TYPE_BY_DIR = {
    "concepts": "concept",
    "entities": "entity",
    "source-summary": "source-summary",
    "comparison": "comparison",
}

# Pages to skip (verbatim clippings with their own non-wiki frontmatter).
SKIP_PAGES = {
    "source-summary/gt-ac5300-pcmag-review-original.md",
}

# Default created/updated dates for this migration. The log shows every page
# was created on 2025-07-16; the migration itself runs on 2026-08-13.
DEFAULT_CREATED = "2025-07-16"
MIGRATION_DATE = "2026-08-13"


# ---------- parsing -------------------------------------------------------

H1_RE = re.compile(r"^# (.+?)\s*$", re.MULTILINE)
DIVIDER_RE = re.compile(r"^---\s*$", re.MULTILINE)

SUMMARY_RE = re.compile(r"\*\*Summary\*\*:\s*(.+?)(?=\n\*\*[A-Z]|\n---|\Z)",
                        re.DOTALL)
SOURCES_RE = re.compile(r"\*\*Sources\*\*:(.*?)(?=\n\*\*[A-Za-z]|\n---|\Z)",
                        re.DOTALL)
RELATED_RE = re.compile(r"\*\*Related\*\*:\s*(.+?)(?=\n\*\*[A-Za-z]|\n---|\Z)",
                        re.DOTALL)
UPDATED_RE = re.compile(r"\*\*Last updated\*\*:\s*(\d{4}-\d{2}-\d{2})")
CONFIDENCE_RE = re.compile(r"\*\*Confidence\*\*:\s*([0-9]+(?:\.[0-9]+)?)")

WIKILINK_RE = re.compile(r"\[\[([^\]\n]+?)\]\]")
MDLINK_RE = re.compile(r"\[([^\]\n]+?)\]\(([^\)\n]+?)\)")
BARE_URL_RE = re.compile(r"https?://[^\s\)\,\]]+")
TRAILING_PAREN_RE = re.compile(r"\s*\([^)]*\)\s*$")


def parse_sources(text: str) -> list[str]:
    """Extract a list of sources from a `**Sources**: ...` block.

    Each item is returned as the form that should appear in YAML:
      - wikilinks as  "[[link]]"
      - URLs as "https://..."
    """
    items: list[str] = []
    seen: set[str] = set()

    # 1. Wikilinks (highest fidelity — preserve path/target verbatim).
    for m in WIKILINK_RE.finditer(text):
        target = m.group(1).strip()
        # Strip trailing parenthetical like "(ASUS support page, ...)".
        target = TRAILING_PAREN_RE.sub("", target).strip()
        key = f"[[{target}]]"
        if key not in seen:
            seen.add(key)
            items.append(key)

    # 2. Markdown links [text](url) — extract url, ignore display text.
    for m in MDLINK_RE.finditer(text):
        url = m.group(2).strip()
        if url not in seen:
            seen.add(url)
            items.append(url)

    # 3. Bare URLs not already captured.
    for m in BARE_URL_RE.finditer(text):
        url = m.group(0).rstrip(".,)")
        if url not in seen and f"[[{url}]]" not in seen:
            seen.add(url)
            items.append(url)

    return items


def parse_pipe_list(text: str) -> list[str]:
    """Parse the comma-separated list after `**Related**:`."""
    items: list[str] = []
    for raw in text.split(","):
        item = raw.strip()
        item = TRAILING_PAREN_RE.sub("", item).strip()
        if not item:
            continue
        # Normalize to a [[wikilink]] form. The prose already uses
        # [[wikilinks]] in some pages and bare names in others; we wrap
        # bare names so YAML is unambiguous.
        if item.startswith("[[") and item.endswith("]]"):
            items.append(item)
        else:
            items.append(f"[[{item}]]")
    return items


def split_header_block(text: str) -> tuple[str, str]:
    """Split the prose-header block from the body using the first `---`.

    Returns (header_block, body). header_block includes the H1 and the
    Summary/Sources/... lines; body is everything from after the divider.
    """
    divider = DIVIDER_RE.search(text)
    if not divider:
        return text, ""
    return text[: divider.start()], text[divider.end():]


# ---------- per-file migration --------------------------------------------

def migrate(path: Path, dry_run: bool) -> str:
    rel = path.relative_to(WIKI_ROOT.parent).as_posix()
    if rel in SKIP_PAGES:
        return f"SKIP    {rel}  (verbatim clipping)"

    text = path.read_text(encoding="utf-8")

    # Already-migrated check: page starts with `---`.
    if text.lstrip().startswith("---"):
        return f"SKIP    {rel}  (already has YAML frontmatter)"

    header, body = split_header_block(text)

    h1 = H1_RE.search(header)
    if not h1:
        return f"WARN    {rel}  (no H1 found)"
    title = h1.group(1).strip()

    sources = []
    sm = SOURCES_RE.search(header)
    if sm:
        sources = parse_sources(sm.group(1))
    related: list[str] = []
    rm = RELATED_RE.search(header)
    if rm:
        related = parse_pipe_list(rm.group(1))
    um = UPDATED_RE.search(header)
    updated = um.group(1) if um else MIGRATION_DATE
    cm = CONFIDENCE_RE.search(header)
    confidence = float(cm.group(1)) if cm else None

    page_type = TYPE_BY_DIR.get(path.parent.name)
    if page_type is None:
        return f"WARN    {rel}  (unrecognized directory {path.parent.name!r})"

    # Build YAML frontmatter.
    lines: list[str] = ["---"]
    lines.append(f"title: {_yaml_str(title)}")
    lines.append(f"type: {page_type}")
    if sources:
        lines.append("sources:")
        for s in sources:
            lines.append(f"  - {_yaml_str(s)}")
    else:
        lines.append("sources: []")
    if related:
        lines.append("related:")
        for r in related:
            lines.append(f"  - {_yaml_str(r)}")
    lines.append(f"created: {DEFAULT_CREATED}")
    lines.append(f"updated: {updated}")
    if confidence is not None:
        lines.append(f"confidence: {confidence}")
    lines.append("---")
    lines.append("")  # blank line after frontmatter close

    # Body: H1 + body content. The H1 was inside `header`, so put it back.
    body = body.lstrip("\n")
    new_text = "\n".join(lines) + f"# {title}\n\n" + body

    if dry_run:
        return f"DRY-RUN {rel}  sources={len(sources)} related={len(related)} conf={confidence}"

    path.write_text(new_text, encoding="utf-8")
    return f"OK      {rel}  sources={len(sources)} related={len(related)} conf={confidence}"


def _yaml_str(s: str) -> str:
    """Quote a YAML string. Use double quotes; escape any embedded " or \\."""
    escaped = s.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


# ---------- main ----------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="show what would change without writing files")
    args = ap.parse_args()

    rc = 0
    for sub in TYPE_BY_DIR:
        for path in sorted((WIKI_ROOT / sub).glob("*.md")):
            line = migrate(path, args.dry_run)
            print(line)
            if line.startswith("WARN"):
                rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
