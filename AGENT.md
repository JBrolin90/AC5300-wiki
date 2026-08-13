# Research Wiki: [Your Topic]

## Project Structure

- `raw/` — Immutable source documents. Never modify files here.
- `assets/` — Derivative image artifacts referenced from wiki pages.
  - `assets/figures/` — Images **extracted** from raw/ sources (e.g. `pdfimages` from a PDF). Each file carries the source it came from in its name.
  - `assets/diagrams/` — **Agent-authored** diagrams (e.g. Excalidraw `.excalidraw` files plus their `.png` renders). Created by the LLM to clarify or contrast with extracted figures.
- `wiki/` — LLM-generated and maintained markdown pages.
- `wiki/index.md` — Master content catalog. Update on every operation.
- `wiki/log.md` — Append-only operation log.
- `outputs/` — Generated reports, presentations, lint results.

## Page Types and Conventions

Every wiki page must have YAML frontmatter:

    ---
    title: Page Title
    type: concept | entity | source-summary | comparison
    sources:
      - "[[../source-summary/source-name]]"        # wikilinks in double quotes
      - "https://example.com/..."                  # bare URLs in double quotes
    related:
      - "[[related-concept]]"                      # bare-name wikilinks resolve from this folder
    created: YYYY-MM-DD
    updated: YYYY-MM-DD
    confidence: 0.0–1.0                            # numeric, e.g. 0.85
    ---

### Field notes

- **`type`**: must match the directory the page lives in (`concepts/`, `entities/`, `source-summary/`, `comparison/`).
- **`sources`**: every claim should be traceable. Prefer wikilinks to other wiki pages or to `raw/` artifacts; use plain URLs when no wiki page exists yet.
- **`related`**: cross-links to other concept/entity pages that this page depends on or contrasts with. Optional — omit the field when there are no related pages.
- **`confidence`**: a single number in `[0.0, 1.0]`. Conventional buckets (for guidance only): ≥ 0.9 high, 0.7–0.9 medium, < 0.7 low. If you have a per-claim breakdown, put it in the body, not in the frontmatter.
- **`created`** vs **`updated`**: `created` is the date the page first existed; bump `updated` on every substantive edit.

### Verbatim clipping exception

Pages in `source-summary/` that are **verbatim clippings** of an external article (e.g. `*-original.md`) keep their original frontmatter from the clipping tool. They do **not** get the wiki schema applied on top — the wiki schema applies only to LLM-authored summaries. Reference them in `sources:` of the matching summary page instead of treating them as siblings.

### Naming

- Filenames: kebab-case matching the concept (e.g., attention-mechanism.md)
- Cross-references: use [[wikilinks]] for all internal links
- Source references: always link back to raw/ file paths

### Images and diagrams

Two kinds of visual assets live under `assets/`:

| Kind | Folder | Filename convention | Created by |
|---|---|---|---|
| **Extracted figure** | `assets/figures/` | `{source-prefix}-p{page}-{index}-{caption}.{ext}` — e.g. `manual-p017-03-router-front.png`, `pcmag-p01-02-router-photo.jpg` | `pdfimages` or equivalent, run from a `raw/` source |
| **Agent-authored diagram** | `assets/diagrams/` | `{caption}.excalidraw` (plus a companion `{caption}.excalidraw.png` for rendering outside Obsidian) — e.g. `aimesh-v1-vs-v2.excalidraw`, `usb-port-layout.excalidraw` | The LLM, via the Excalidraw tools |

Both kinds follow the same overall rules:

- Kebab-case filenames matching the caption.
- The caption part of the filename should be descriptive enough to identify the figure without opening it.
- For extracted figures, `source-prefix` identifies the source document (`manual`, `pcmag`, `firmware-page`, etc.) so a reader knows where it came from.

**Referencing in markdown**:

The wiki uses **standard markdown** with relative paths (not Obsidian wikilinks), so that figures render correctly in any viewer — Obsidian, VS Code preview, GitHub, static-site generators, web exports — without depending on the viewer's file-index or name-based resolver.

- **Standard markdown (preferred)**: `![alt text](../../assets/figures/manual-p017-03-router-front.png)`
- The path is **relative to the wiki page that embeds the image**. From `wiki/concepts/foo.md`, the path is `../../assets/figures/...`. From `wiki/source-summary/foo.md`, the same path applies.
- Obsidian wikilink syntax `![[name]]` is **not** used here. We tried it; the user's Obsidian vault didn't resolve the names despite the files being present, and the syntax doesn't work in non-Obsidian viewers anyway.

**Alt text and captions**: every image in a wiki page should have alt text that describes what's shown. For figures extracted from sources, the alt text should also note the source page (e.g. `Router front panel — ASUS GT-AC5300 manual p.17`). For diagrams, the alt text can be the caption. A longer caption can also appear in italics below the image for richer context.

**When to extract vs when to redraw**: extract figures that carry information not present in the text layer (hardware diagrams, screenshots). Redraw or supplement when the source figure is ambiguous, outdated, or when a clarifying diagram would help. Pair them inline when both exist.

## Workflows

### Ingest

1. Read the source document in raw/
   1a. If the source contains embedded figures, extract them with `pdfimages` (or equivalent) into `assets/figures/` using the naming convention `{source-prefix}-p{page}-{index}-{caption}.{ext}`. Skip purely decorative figures (icons, background art) unless they carry information.
   1b. For raster figures that carry text not present in the source's text layer (e.g. screenshots), optionally run `naps2_ocr` and embed the result in the figure's alt text on the wiki page that references it.
2. Discuss key takeaways with the user (including which figures are wiki-worthy)
3. Create wiki/sources/[source-name].md summary, embedding figures inline at the relevant points
4. Update or create concept/entity pages as needed (with figure references where they add information)
5. Update wiki/index.md with new entries
6. Append to wiki/log.md

### Query

1. Read wiki/index.md to identify relevant pages
2. Read those pages and synthesize an answer
3. Cite sources using [[wikilinks]]
4. If the answer is novel and valuable, offer to save it as a new wiki page

### Lint

1. Scan all wiki pages for contradictions
2. Identify orphan pages (no incoming links)
3. Flag missing concepts referenced but not created
4. Find stale claims superseded by newer sources
5. Save results to outputs/lint-YYYY-MM-DD.md


