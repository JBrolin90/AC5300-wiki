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

### Choosing a page type

Before creating a page, decide which of `concept | entity | source-summary | comparison` fits the content. Apply this decision tree:

1. **Is the content about a single named thing** (a router, a person, a product, a project)? → `entity`
2. **Is the content primarily a verbatim index / list / timeline / changelog from one external source** (e.g. a manufacturer's release notes, a spec sheet, an FAQ page)? → `source-summary` — the source *is* the canonical reference; the wiki's job is to render it consistently and cross-link it from concept pages.
3. **Is the content a side-by-side comparison of two or more things?** → `comparison`
4. **Is the content about a feature, setting, procedure, or cross-cutting theme that the wiki needs to navigate to?** → `concept`

Within `concept`, distinguish four sub-kinds so the structure stays consistent:

| Sub-kind | Example pages | When to use |
|---|---|---|
| **Feature concept** | `vpn-fusion`, `aimesh`, `game-boost`, `game-ips`, `game-private-network`, `game-profile`, `game-radar`, `wifi-radar`, `alexa-ifttt`, `quick-internet-setup` | A single user-facing capability. Owns its own firmware-introduction context, settings, and limitations. |
| **Setting concept** | `wireless-settings`, `lan-wan`, `ipv6`, `smart-connect`, `guest-network`, `port-forwarding-and-trigger`, `vpn` | A category of configurable parameters — the user goes there to set things. |
| **Procedure concept** | `administration`, `utilities`, `troubleshooting`, `quick-internet-setup` | A workflow or set of utilities the user invokes. |
| **Cross-cutting concept** | `firmware` | A theme that touches multiple feature pages (release history, end-of-life status, security CVEs, naming conventions, licensing, etc.). Acts as a **coordinator**: each aspect lives on its own feature or source-summary page; this page ties them together with tables and pointers. |

The **cross-cutting concept** pattern is the one most often missed at ingestion. Symptom: readers searching the index for a high-level topic find nothing because the topic's facts were correctly distributed across feature pages but no coordinator exists. If a source's content spans multiple feature pages and no existing page coordinates them, create one — don't force it, but don't skip it either.

A coordinating cross-cutting page should **not duplicate detail**; it should index it. Tables that point to other pages are usually enough.

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
2. Discuss key takeaways with the user (including which figures are wiki-worthy). **For each takeaway, classify its page type** using the [Choosing a page type](#choosing-a-page-type) decision tree: `entity`, `source-summary`, `comparison`, or `concept` (and within concept: feature / setting / procedure / cross-cutting). Note any cross-cutting themes that may need a coordinator page.
3. Create `wiki/source-summary/[source-name].md`, embedding figures inline at the relevant points.
   3a. **If the source is primarily a release-notes / changelog / index** (e.g. a firmware release history), the source-summary is the right home for the raw timeline. Per-release feature facts, however, often belong on the relevant feature concept page (e.g. "Mobile Game Mode introduced in `3.0.0.4.384.81695`" → `concepts/game-boost`). Push those facts to the feature pages and leave the source-summary as the consolidated catalog.
4. For each topic surfaced in step 2, update or create the corresponding page (entity / source-summary / comparison / concept). Use figure references where they add information. **Cross-cutting themes** (firmware, security, licensing, …) often need a *coordinating concept page* even when each aspect already lives on its own feature page — add one if no such coordinator exists and reference it from `wiki/index.md`. See the firmware creation log entry for a worked example.
5. Update `wiki/index.md` with new entries (under the appropriate section heading).
6. Append to `wiki/log.md` — record what was created/updated, what page-type decisions were made, and what cross-cutting coordinators were added.

### Query

1. Read wiki/index.md to identify relevant pages
2. Read those pages and synthesize an answer
3. Cite sources using [[wikilinks]]
4. **Synthesis-to-concept proposal.** If answering required reading and combining **2 or more wiki pages** because no single page contained the answer (i.e. the topic is not yet its own concept page, or its existing page is incomplete), **propose promoting that topic to a concept page**. The proposal must include:
   - Proposed page title (kebab-case)
   - Page type per the [Choosing a page type](#choosing-a-page-type) decision tree
   - One-paragraph rationale (why this deserves its own page)
   - List of existing wiki pages that fed into the synthesis and that the new page would reference
   - **Confidence** (high / medium / low) — high when the synthesis represents a clearly-coherent topic that several sources converge on; low when it's a one-off look-up that happened to touch 2 pages
   - Whether the new page would **create** (no existing page) or **augment** (existing page is incomplete or scattered)
   
   Present the proposal to the user. **Do not auto-create the page.** Wait for approval. If approved, run the [Promote](#promote) procedure below.
5. If the answer is novel and valuable but doesn't represent a coherent cross-page topic (e.g. it's a one-off look-up or transient debugging info), offer to save it as a chat-history note rather than a wiki page — but only if it would be useful to keep; don't bloat the wiki.

### Lint

1. Scan all wiki pages for contradictions
2. Identify orphan pages (no incoming links)
3. Flag missing concepts referenced but not created
4. Find stale claims superseded by newer sources
5. Save results to outputs/lint-YYYY-MM-DD.md

### Promote

Run this procedure when the user approves a synthesis-to-concept proposal from the [Query](#query) workflow (or asks directly to extract a topic into its own page).

This is the **second way** that pages enter the wiki: not from a source ingest, but from successful multi-page synthesis in a Query session. The trigger is different but the destination (a well-structured wiki page with frontmatter, sources, related, confidence) is the same.

1. Decide the page type per the [Choosing a page type](#choosing-a-page-type) decision tree.
2. Draft the page following the standard wiki schema (YAML frontmatter with `type:`, `sources:`, `related:`, `confidence:`, `created:`, `updated:`; body with sections and [[wikilinks]] back to the pages that fed into the synthesis).
3. **Augment, don't duplicate.** If an existing page covers most of the topic, edit it instead of creating a parallel page. Cross-link the synthesis page from the existing one if the topics genuinely differ.
4. Update `wiki/index.md` with the new entry under the appropriate section heading.
5. Append to `wiki/log.md` — record:
   - That the page was created via promotion (not via initial source ingest)
   - Which wiki pages fed into the synthesis
   - The rationale (what question triggered the synthesis, and why the topic deserves its own page)
   - The confidence level from the proposal
6. Run `python3 outputs/lint.py` to confirm no new orphans / catalog gaps / missing concepts / metadata issues.


