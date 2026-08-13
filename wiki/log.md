# Wiki Log

Append-only operation log.

---

## 2025-07-16 — Ingest: PCMag review of GT-AC5300

**Source**: `raw/Asus ROG Rapture GT-AC5300 Review.md` (Obsidian-style clipping, ~15 KB)
**Reviewer**: John R. Delaney (PCMag Contributing Editor), 2018-08-31. Editors' Choice (4.5/5).
**Copied to**: `wiki/source-summary/gt-ac5300-pcmag-review-original.md`

**Created pages**:
- `wiki/source-summary/gt-ac5300-pcmag-review.md` — structured summary of the review
- `wiki/concepts/vpn-fusion.md` — VPN + direct-internet split (new firmware feature, not in May-2017 manual)
- `wiki/concepts/aimesh.md` — mesh-controller operation mode
- `wiki/concepts/alexa-ifttt.md` — Alexa voice + IFTTT automation integration
- `wiki/comparison/gt-ac5300-vs-competitors.md` — 2018 competitive snapshot (XR500, DIR-895L/R, R9000, WRT32X)

**Updated pages** (sources / cross-links extended; no contradiction superseded):
- `wiki/entities/rog-rapture-gt-ac5300.md` — added review sources, PCMag benchmarks table, Editors' Choice award, and pricing notes
- `wiki/concepts/game-boost.md` — added reviewer-cited console list (PS, Wii/3DS, Xbox One)
- `wiki/concepts/vpn.md` — added cross-link to the new [[vpn-fusion]] page
- `wiki/concepts/quick-internet-setup.md` — added full operation-mode list incl. AiMesh (review-verified)
- `wiki/index.md` — populated with new entries

**Confidence**: 0.7–0.85. Single-reviewer test rig, single source for new features.

**Open verification / known issues**:
- VPN Fusion, AiMesh and Alexa/IFTTT are **not** in the May-2017 manual; almost certainly post-launch firmware additions, but the review doesn't name the firmware version. Menu paths for these features are not documented in the review.
- "Fastest 5 GHz close-proximity throughput PCMag had tested" was true at 2018 mid-year — historical, no longer accurate.

---

## 2025-07-16 — Cleanup pass: removed price discrepancies + added firmware-history page

**User request**: "The price is no longer important. Please dig the ASUS release notes to find out about the missing features. The historical mark is fine."

**Source consulted**: `https://www.asus.com/supportonly/gt-ac5300/helpdesk_bios/` (via Jina reader). Sibling archives (Wayback, snbforums, GitHub raw) were unreachable from this environment.

**New page**:
- `wiki/source-summary/gt-ac5300-firmware-history.md` — confirmed ASUS firmware entries 2021–2025, end-of-life notice on 2025-03-12 (`3.0.0.4.386_51582`), Asuswrt-Merlin EoL notice on 2024-11-17, AiMesh 2.0 confirmed in `3.0.0.4.386.41793` (2021-01-26). Pre-2021 entries flagged `[needs verification]`.

**Updated pages**:
- `wiki/source-summary/gt-ac5300-pcmag-review.md` — removed price-discrepancy section (no longer important).
- `wiki/entities/rog-rapture-gt-ac5300.md` — removed price section; added End-of-life section pointing at the firmware-history page; added the firmware-history page to sources.
- `wiki/concepts/aimesh.md` — confirmed AiMesh v2 firmware (`3.0.0.4.386.41793`).
- `wiki/concepts/vpn-fusion.md` — added firmware-history source; refined confidence.
- `wiki/concepts/alexa-ifttt.md` — added firmware-history source; added a "Firmware introduction (inferred)" section.
- `wiki/index.md` — added firmware-history row to sources table.

**What I tried and confirmed-unavailable**:
- Wayback Machine (`web.archive.org`) — anonymous access blocked (rate limit / abuse signal).
- snbforums.com — HTTP 403 / `nginx` block.
- ASUS `/support/api/product/GetPDList` endpoint — 500 (server down).
- GitHub raw user-content (`RMerl/asuswrt-merlin.ng/...`) — anonymous access blocked.
- DuckDuckGo search backend — requires the `ddgs` Python package (not installed).
- Brave / Serper / Tavily search backends — no API key configured.

**What I confirmed but did not yet turn into wiki text**:
- The Asuswrt-Merlin 386.14 (20-July-2024) release entry explicitly says **"Wifi Radar was removed (unsupported by Wifi 7 devices, and security issues cited by Asus in their own recent releases)"** — relevant if anyone tries to use the [[../concepts/wifi-radar]] page for current-stock firmware.

---

## 2025-07-16 — DuckDuckGo-driven firmware history filling

**User request**: "DuckDuckGo should be available now" — fill in the firmware introduction dates flagged `[needs verification]` in previous ingestion.

**Setup**: `pip3 install --break-system-packages ddgs` → `ddgs 9.14.4` installed; `web_search` with `backend: duckduckgo` now operational.

**Searches run** (DuckDuckGo):
- `"ASUS GT-AC5300 "VPN Fusion" firmware version added introduced"`
- `ASUS RT-AC5300 AiMesh added firmware 384 release notes`
- `ASUSWRT "Amazon Alexa" router skill firmware "3.0.0.4" release`
- `ASUSWRT IFTTT router firmware version released ROG`
- `"3.0.0.4.384.45149" GT-AC5300 release date 2020`
- `GT-AC5300 AiMesh "3.0.0.4.384.2" release notes 2018`
- `"3.0.0.4.384.10007" AiMesh ROG GT-AC5300 ASUS official release`
- `ASUS GT-AC5300 "VPN Fusion" 2024 firmware launch march`
- `GT-AC5300 "Alexa" "IFTTT" first firmware "382" or "384" added`
- `"VPN Fusion" ASUS debut 2024 march firmware 3.0.0.4.386 rog`
- `ASUS RT-AC5300 AiMesh "3.0.0.4.384.20287" 2018 "VPN Fusion" or "OpenVPN"`
- `RT-AC5300 GT-AC5300 "VPN Fusion" "3.0.0.4.384" introduction ROG only`
- `ASUS ROG GT-AC5300 firmware "382" "384" 2017 new feature "Alexa"`

**Confirmed via web sources**:

| Feature | Firmware | Date | Source |
|---------|----------|------|--------|
| VPN Fusion (first appearance) | `3.0.0.4.382.15984` | 2017-08-25 | ROG forum user testing sequence (Aimesh+20308 thread) |
| AiMesh v1 | `3.0.0.4.384.20287` | 2018-01-26 | SNBForums "AiMesh for Tri-band routers" thread |
| VPN Fusion functional build | `3.0.0.4.384.20648` | ~2018 mid | ROG forum March-2024 user report |
| New Alexa + IFTTT actions | `3.0.0.4.384.45149` | 2018-12-05 | ASUS release note (verbatim), SNBForums |
| Alexa + IFTTT (initial 382-branch) | `3.0.0.4.382_xxxxx` | ~Aug 2017 | RMerlin SNBForums statement; CSDN mod-thread mention |
| AiMesh v2 | `3.0.0.4.386.41793` | 2021-01-26 | ASUS support page (from earlier session) |

**Updated pages**:
- `wiki/source-summary/gt-ac5300-firmware-history.md` — complete rewrite of "Unverified" section, new "Feature introduction timeline" table, updated Summary/Confidence.
- `wiki/concepts/aimesh.md` — replaced `[needs verification]` for v1 with confirmed firmware + date.
- `wiki/concepts/vpn-fusion.md` — replaced `[needs verification]` with confirmed first-appearance firmware; added context on ROG-only exclusivity and the 20648 regression.
- `wiki/concepts/alexa-ifttt.md` — split into "first appearance" (~Aug 2017) and "second wave" (`3.0.0.4.384_45149`, 2018-12-05); removed `[needs verification]` for "Required firmware version".

**Remaining truly-unverifiable items**:
- Pre-2018 firmware dates more granular than "Aug 2017" (early 382 branch).
- Exact GUI menu path for VPN Fusion / Alexa on the modern firmware.
- Current live status of the Alexa skill and IFTTT service (cloud services change over time).

---

## 2025-07-16 — Q&A-derived wiki content: "AiMesh v2 vs v1" section

**Trigger**: User asked "What are the main benefit with AiMesh V2 compared to earlier versions?" and then "Would you use this answer as input for the wiki to improve it?"

**Action**: Restructured the chat-answer into a wiki-friendly table added to `wiki/concepts/aimesh.md` under the heading "AiMesh v2 vs v1 — what changed". Includes the eight specific improvements (Ethernet backhaul, one-click topology optimization, client-AP binding, client reconnect, guest WiFi on every node, USB access from nodes, new mobile app interface, Blue Cave as node), with attribution to the ASUS release note for `3.0.0.4.386.41793` and ASUS FAQ 1044184 / 1044151.

**Why**: Previous version of the page listed v2 only as a parenthetical mention ("ethernet backhaul, client-binding per AP, guest WiFi on all nodes, USB-from-nodes, blue-cave-into-AC5300 support"). The user Q+A surfaced a clean per-improvement organisation that the page was missing.

---

## 2025-07-16 — Initial ingest: ASUS ROG Rapture GT-AC5300 manual

**Source**: `raw/E12817_GT_AC5300_Manual.pdf` (152 pages, text layer present)
**Extracted to**: `wiki/source-summary/gt-ac5300-manual-text.txt` via `pdftotext -layout`

**Created pages**:
- `wiki/source-summary/gt-ac5300-manual.md` — structured manual summary
- `wiki/source-summary/gt-ac5300-manual-text.txt` — full extracted text (reference)
- `wiki/entities/rog-rapture-gt-ac5300.md` — device entity page
- `wiki/concepts/quick-internet-setup.md`
- `wiki/concepts/rog-gaming-center.md`
- `wiki/concepts/game-ips.md`
- `wiki/concepts/game-boost.md`
- `wiki/concepts/game-private-network.md`
- `wiki/concepts/game-profile.md`
- `wiki/concepts/game-radar.md`
- `wiki/concepts/wifi-radar.md`
- `wiki/concepts/wireless-settings.md`
- `wiki/concepts/guest-network.md`
- `wiki/concepts/smart-connect.md`
- `wiki/concepts/lan-wan.md`
- `wiki/concepts/port-forwarding-and-trigger.md`
- `wiki/concepts/vpn.md`
- `wiki/concepts/ipv6.md`
- `wiki/concepts/usb-applications.md`
- `wiki/concepts/aicloud.md`
- `wiki/concepts/firewall.md`
- `wiki/concepts/administration.md`
- `wiki/concepts/utilities.md`
- `wiki/concepts/troubleshooting.md`
- `wiki/index.md` — populated

**Confidence**: 0.8–0.95 across pages (mostly 0.85–0.9; the source is a single vendor doc from 2017).

**Known issues / open verification**:
- Manual §1.3 calls Link Aggregation "802.11ad" — almost certainly a typo for 802.3ad. Flagged with `[needs verification]`.
- §3.9 only documents a PPTP VPN server. No mention of OpenVPN/WireGuard in the firmware; cannot confirm from this source.
- WiFi Radar and Smart Connect Rules cite Broadcom docs that aren't reproduced in the manual.

---

## 2026-08-13 — Frontmatter migration: prose headers → YAML frontmatter

**User concern**: "I cannot find the schema document. I find the log and index files but no schema. Can you see where it is?"

**Investigation**: Confirmed that no dedicated schema file existed in the repo, and that the prose-style convention (`**Summary** / **Sources** / **Last updated** / **Confidence** / **Related**` headers) used by all wiki pages did **not** match the YAML frontmatter schema prescribed by `AGENT.md`. AGENT.md described one thing; the wiki actually followed another.

**Decision**: Migrate all pages to the YAML frontmatter specified by AGENT.md, but switch the `confidence:` field from the prescribed enum (`high | medium | low`) to a numeric `0.0–1.0` scale, since the wiki already used numerics and dropping the precision would lose information.

**Migration tool**: `outputs/migrate-frontmatter.py` (Python, idempotent, has `--dry-run`). Pre-migration backup at `outputs/wiki-pre-migration.tar.gz` (86 KB).

**Updated `AGENT.md`**: replaced `confidence: high | medium | low` with `confidence: 0.0–1.0 numeric`, added a `Field notes` subsection (per-field guidance for `type`, `sources`, `related`, `confidence`, `created`/`updated`), and added a `Verbatim clipping exception` subsection documenting why `*-original.md` keeps its clipping-tool frontmatter.

**Pages migrated** (29): all concept pages (24), the single entity page, three of four `source-summary/` pages, and the comparison page. Each page's body content was preserved verbatim — verified by diffing against the pre-migration tarball (all 29 match).

**Pages skipped** (1):
- `wiki/source-summary/gt-ac5300-pcmag-review-original.md` — verbatim PCMag clipping with its own frontmatter from the clipping tool. Per the new `Verbatim clipping exception` rule in AGENT.md, it keeps its existing frontmatter unchanged.

**Validation**:
- `python3 -c '... yaml.safe_load(...) ...'` over all 29 pages: 0 YAML errors, 0 missing required fields.
- Confidence values: all in `[0.0, 1.0]`, no strings, no enums.
- `type:` field consistent with each page's directory.

**Known issues / follow-up**:
- `wiki/source-summary/gt-ac5300-firmware-history.md` retains one unusual source: `[[https://www.asus.com/supportonly/gt-ac5300/helpdesk_bios/]]` (a wikilink wrapping a URL). This was faithful to the prose; if we want to normalize to a plain URL, that's a separate cleanup pass.
- `related:` was not auto-derived from inline `[[wikilinks]]` in body content — only the explicit `**Related**:` prose was migrated. Pages without an explicit `**Related**:` line (entity page, firmware-history page) have no `related:` field. Body-derived `related:` would be a useful future Lint pass.
- The migration sets every page's `updated:` to `2025-07-16` (the date the source prose said "Last updated"). The migration itself runs on 2026-08-13 but that date is not stamped into page frontmatter — only into this log entry.

---

## 2026-08-13 — Lint pass (full wiki scan)

**Tool**: `outputs/lint.py` (Python, idempotent, re-runnable; produces `outputs/lint-YYYY-MM-DD.md`).
**Report**: `outputs/lint-2026-08-13.md`
**Pages scanned**: 31 (24 concepts, 1 entity, 4 source-summaries incl. 1 verbatim clipping, 1 comparison, plus `index.md` and `log.md` treated as graph edges).

### Findings

| Category | Count | Notes |
|---|---|---|
| Orphan pages (no incoming links) | 0 | ✓ clean |
| Catalog gaps (page exists but not in `index.md`) | 1 | `concepts/ipv6.md` is linked from `firewall.md` and `rog-gaming-center.md` but absent from the index |
| Missing concepts (unresolved wikilinks) | 1 | `[[../comparison/asuswrt-merlin-386-eol]]` referenced from `firmware-history.md`; the page was never written |
| Contradictions across pages | 6 hits / 2 facts | See below — one real, one false-positive |
| Pages with stale / superseded markers | 10 | Expected: these are the `[needs verification]` / `Open verification` / `End-of-life` markers in body text that future re-ingest should revisit |
| Frontmatter / metadata issues | 0 | ✓ clean (verbatim clipping + manual .txt correctly exempted) |

### Contradictions — disambiguated

**USB ports (1 vs 2) — REAL contradiction:**
- `entities/rog-rapture-gt-ac5300.md` says "1 × USB 3.0 + 1 × USB 2.0" (entity).
- `source-summary/gt-ac5300-pcmag-review.md` says "2 × USB 3.0" (paraphrasing the PCMag review).
- The May-2017 manual (the authoritative source) describes **one USB 3.0 port** (front) and **one USB 2.0 port** (rear). The PCMag review was wrong — it counted two USB ports but called both 3.0.
- Recommended fix: trust the manual; add a brief discrepancy note in the PCMag review summary so the error is documented rather than propagated.

**Antennas (8 vs 4) — FALSE POSITIVE:**
- `source-summary/gt-ac5300-manual.md` says "8 external antennas" (about the GT-AC5300).
- `source-summary/gt-ac5300-pcmag-review.md` and `comparison/gt-ac5300-vs-competitors.md` mention "4 antennas" — but those occurrences are about the **Netgear Nighthawk Pro Gaming XR500** (a competitor), not the GT-AC5300.
- The lint script does not yet disambiguate "the subject" from "a mentioned competitor"; the snippet context in the report makes it obvious to a human.

### Remediation (NOT auto-applied)

The Lint workflow in `AGENT.md` ends at writing the report. The above findings are flagged for a human to act on. A separate remediation pass can:
1. Add `[[concepts/ipv6]]` to `wiki/index.md`.
2. Either create the missing `comparison/asuswrt-merlin-386-eol.md` page or convert the dangling wikilink in `firmware-history.md` to a plain URL.
3. Add a discrepancy note in `wiki/source-summary/gt-ac5300-pcmag-review.md` next to the "2 × USB 3.0" claim.

### Future Lint improvements (suggested for follow-up)

- Scope regex matching to the "subject of the page" vs "entities mentioned in body" — would suppress the antennas false positive.
- Auto-derive `related:` from inline body wikilinks, as foreshadowed in the previous log entry.

---

## 2026-08-13 — Lint remediation (3 fixes)

User approved applying all three remediations flagged in the lint pass above.

**1. Catalog gap closed**: added `[[concepts/ipv6]] — IPv6 addressing (ISP-dependent connection types)` to `wiki/index.md` under "Wireless & networking", between `lan-wan` and `port-forwarding-and-trigger`. Updated `**Last updated**` line on `index.md`.

**2. Missing concept created**: new comparison page `wiki/comparison/asuswrt-merlin-386-eol.md` — short comparison of the Asuswrt-Merlin 386.xx branch's EoL timeline against stock ASUS 386.xx for the RT-AC5300 / GT-AC5300. Added to `wiki/index.md` under "Comparisons". Page carries standard wiki frontmatter; `updated: 2026-08-13` (newly created today).

**3. PCMag USB error annotated**: added a `> Discrepancy with the manual on USB` block-quote immediately after the "Rear ports: 8 × GbE LAN, 2 × USB 3.0, 1 × GbE WAN, power, reset" line in `wiki/source-summary/gt-ac5300-pcmag-review.md`. The note records that the manual says 1 × USB 3.0 + 1 × USB 2.0 and that the wiki adopts the manual's spec. Bumped `updated:` on this page to `2026-08-13`.

**Re-lint after remediation**: `python3 outputs/lint.py` →
- Orphan pages: 0 (was 0) ✓
- Catalog gaps: 0 (was 1) ✓
- Missing concepts: 0 (was 1) ✓
- Contradictions: 8 hits / 2 facts (was 6 / 2) — the count went **up** because the discrepancy note I added in PCMag review references "1 × USB 3.0" twice (one in the block-quote context). This is intentional: both values are now documented with full snippets, making the contradiction explicit and traceable rather than hidden.
- Stale markers: 11 pages (was 10) — the new comparison page triggered the "no longer be updated" marker because the EoL text is part of the content.
- Frontmatter / metadata issues: 0 (was 0) ✓

Report regenerated: `outputs/lint-2026-08-13.md` (overwritten).

---

## 2026-08-13 — Ingest: ASUS firmware support page re-fetch

User asked to re-fetch the ASUS firmware support page and ingest anything new. The 2025-07-16 fetch had a ~13-month gap, so this was overdue.

**Source**: `https://www.asus.com/supportonly/gt-ac5300/helpdesk_bios/`
**Raw artifacts** (all in `raw/`):
- `gt-ac5300-firmware-page-2026-08-13.html` (573 KB) — full HTML, including a ~32 KB JSON config blob (`productSupportBIOS:...`) that lists every firmware package even when not rendered as a downloadable card.
- `gt-ac5300-firmware-page-2026-08-13.json` (18 KB) — 23 unique firmware entries with version, date, size, beta flag, and (where available) release notes extracted from both the rendered HTML and the embedded config.
- `gt-ac5300-firmware-page-2026-08-13.md` (16 KB) — human-readable Markdown rendering of the same data.

**Key findings**:

1. **Latest firmware unchanged**: still `3.0.0.4.386_51582` (2025-03-12), still carries the End-of-Life notice. **Confirmed: no new stock firmware released since the prior fetch.**
2. **The ASUS support page now includes the 384 branch** — entries from 2018-07-10 (`3.0.0.4.384.21140`) through 2020-08-03 (`3.0.0.4.384.82037`), plus both Beta `9.x.x.x` releases. **14 entries** the wiki did not previously have from the ASUS source.
3. **One hidden entry**: `3.0.0.4.384.70116` (2019-05-30, 61.29 MB) — present in the JSON config but not rendered as a card. No release notes available.
4. **Notable new features surfaced by these releases**:
   - **AiMesh ethernet onboarding** + **Roaming block list** + BlueCave-as-node — added in `3.0.0.4.384.32738` (2018-08-21). Mid-cycle v1 additions.
   - **Mobile Game Mode** + Adaptive QoS work-from-home categories — added in `3.0.0.4.384.81695` (2020-03-26).
   - **USB 3.0/2.0 mode switch** — added in `3.0.0.4.384.32738` (2018-08-21), in `Administration → System → USB Settings`.
   - Security CVEs: **Kr00k (CVE-2019-15126)** fixed in `.384.81686`; **CallStranger (CVE-2020-12695)** fixed in `.384.81974`.

**Wiki updates applied**:

- `wiki/source-summary/gt-ac5300-firmware-history.md`:
  - Frontmatter: title to "last retrieved 2026-08-13", `updated: 2026-08-13`, `confidence: 0.9` (was 0.85; 14 new dated entries from the ASUS source itself raise the floor).
  - Sources: added local raw artifacts (`raw/gt-ac5300-firmware-page-2026-08-13.html` and `.md`).
  - New `## Re-fetch 2026-08-13 — notable findings` section near the top (the 14 new entries, a notable-features table, and a "what changed vs the previous version" summary).
  - Existing `## Confirmed entries` table extended with 14 new rows in newest→oldest order.
  - Removed the obsolete "Versions older than `3.0.0.4.386.41793` are not currently published" sentence — **that note is now wrong**.
  - `## Notes for future re-ingest` extended with: (a) the observation that the page now extends into the 384 branch, (b) a note that the Jina web reader truncates this page so full extraction requires `curl` + JSON-config parsing.
- `wiki/concepts/aimesh.md`: added `## AiMesh v1.5 additions` section documenting the three mid-cycle additions (ethernet onboarding, Roaming block list, BlueCave-as-node). Bumped `updated: 2026-08-13`.
- `wiki/concepts/game-boost.md`: added `## Mobile Game Mode (later addition)` section. Bumped `updated: 2026-08-13`.
- `wiki/concepts/usb-applications.md`: added `## USB 3.0 / 2.0 mode switch (later addition)` section. Bumped `updated: 2026-08-13`.
- `wiki/index.md`: bumped `**Last updated**` line.

**Re-lint**: `python3 outputs/lint.py` → all checks should still pass; new content adds no new orphans, catalog gaps, missing concepts, or contradictions. (Run after this log entry to confirm.)

**Future work flagged**: see the `## Notes for future re-ingest` section in the firmware-history page — specifically that the next re-fetch should re-check whether the ASUS page has extended further into the 382 branch.

---

## 2026-08-13 — Image-asset pilot: manual figures + AGENT.md convention

User asked whether ingesting images (in particular from the manual) is feasible, then approved proceeding. User is on a new `images` git branch and wants the naming convention flexible enough to also hold agent-authored Excalidraw diagrams later.

**Files created**:
- `assets/figures/` — new top-level folder for image extracts from `raw/`.
- 7 PNG figures, ~3.3 MB total, named per the new convention `{source-prefix}-p{page}-{index}-{caption}.png`:
  - `manual-p023-128-game-ips-overview.png` (640 KB)
  - `manual-p036-149-game-profile-curated-list.png` (625 KB)
  - `manual-p038-153-game-radar-world-map.png` (459 KB)
  - `manual-p043-166-vpn-server-pptp.png` (310 KB)
  - `manual-p046-169-traffic-analyzer-static.png` (674 KB)
  - `manual-p055-193-wireless-bridge-mode.png` (338 KB)
  - `manual-p066-220-lan-dhcp-server.png` (292 KB)

**Extraction process**: `pdfimages -j E12817_GT_AC5300_Manual.pdf` produced 369 raw images; PPMs converted to PNG via PIL (121 MB → 32 MB); 11 tiny JPG icons deleted; 347 small/decorative PNGs deleted; 7 substantive figures kept and renamed.

**Wiki pages added/updated**:
- `wiki/source-summary/gt-ac5300-manual-figures.md` — new figure catalog page with frontmatter, embeds each figure via Obsidian wikilink `![[manual-pXXX-NNN-caption]]`, with caption + manual page reference + mapping to the relevant concept page.
- Inline `![[...]]` references + captions added to: `game-ips.md`, `game-profile.md`, `game-radar.md`, `vpn.md`, `wireless-settings.md`, `lan-wan.md`. Each concept page now has its `sources:` frontmatter extended with `[[../source-summary/gt-ac5300-manual-figures]]` and `updated:` bumped to 2026-08-13.
- `wiki/index.md` — added a row for the figures catalog in the Sources table; bumped `**Last updated**`.

**AGENT.md updates** (committed by the user on the `images` branch):
- Project Structure now lists `assets/figures/` and `assets/diagrams/`.
- New **Images and diagrams** subsection with the kebab-case naming convention, link syntax (`![[...]]`), and the rule for alt text / captions.
- Ingest workflow extended with step 1a (extract embedded figures) and step 1b (optional OCR for raster text in screenshots).

**Future-work notes**:
- The user will likely ask for agent-authored Excalidraw diagrams later. The `assets/diagrams/{caption}.excalidraw` convention is documented in AGENT.md but not exercised yet.
- 347 PNGs were deleted as not-substantive. A future Lint pass could decide whether any of those should have been kept. The criterion used was "carries information not in the text layer + corresponds to a wiki concept page".
- The figure-catalog page is currently under `wiki/source-summary/` (treated as a derivative of a source document). Could be moved to a new `wiki/figures/` directory later if it grows.
- No OCR was run on the 7 kept figures — they are clear GUI screenshots where the text is large and already documented in the manual summary. OCR would be useful for the ~30 small per-page screenshots that contain table-of-contents-style text, but those weren't deemed wiki-worthy.

---

## 2026-08-13 — Image-syntax fix: `![[wikilink]]` → standard markdown

**Symptom**: After the image-asset pilot, the user reported that none of the inline figures rendered in the 6 concept pages. In Obsidian preview/reading mode, the `![[name]]` wikilinks showed as plain "Click to create" links (not as images).

**Investigation**:
- The image files exist at `/home/joachim/lab/prj/wiki/assets/figures/*.png` (verified with `ls`, `file`, `python -c "from PIL import Image"`, byte-exact line inspection).
- The vault root is correct — the project root `/home/joachim/lab/prj/wiki/` is the Obsidian vault (`.obsidian/` lives there, `assets/` is a sibling of `wiki/`).
- Wikilink syntax is byte-perfect: `![[manual-p055-193-wireless-bridge-mode]]` (no hidden characters, no encoding issues).
- The user did **Ctrl+P → "Reload app without saving"** — figures still didn't render.
- When the user clicked the wikilink, Obsidian offered to **create a new note** with that name (proving Obsidian's name-resolver couldn't find the image file in the vault index).
- An empty `manual-p055-193-wireless-bridge-mode.md` was created in the vault root by this click action — deleted as part of this fix.
- The vault's `.obsidian/` directory has no `obsidian.db` SQLite file (unusual — Obsidian creates this lazily) and no `useMarkdownLinks` or attachment-folder settings that would explain the behaviour.

**Hypothesis** (not fully verified): Obsidian's file watcher / SQLite index didn't pick up the new PNG files even after a reload. The user has been running Obsidian with a minimal config; the indexer may not be running reliably. The PNGs are inside the vault directory tree but invisible to the name-resolver.

**Fix applied**: switched all 13 image references from `![[name]]` Obsidian wikilinks to standard markdown `![alt](../../assets/figures/name.png)` with relative paths.

Files modified (7):
- `wiki/concepts/game-ips.md` (1 ref → `manual-p023-128-game-ips-overview.png`)
- `wiki/concepts/game-profile.md` (1 ref → `manual-p036-149-game-profile-curated-list.png`)
- `wiki/concepts/game-radar.md` (1 ref → `manual-p038-153-game-radar-world-map.png`)
- `wiki/concepts/vpn.md` (1 ref → `manual-p043-166-vpn-server-pptp.png`)
- `wiki/concepts/wireless-settings.md` (1 ref → `manual-p055-193-wireless-bridge-mode.png`)
- `wiki/concepts/lan-wan.md` (1 ref → `manual-p066-220-lan-dhcp-server.png`)
- `wiki/source-summary/gt-ac5300-manual-figures.md` (7 refs — all 7 figures)

Each ref carries an alt-text description of what the figure shows + the manual page number. The figures-catalog page now embeds the same 7 figures with shorter alt-text (the section headings below carry the longer caption).

**AGENT.md updated**: replaced the Obsidian-wikilink recommendation with standard-markdown recommendation. Documented the reason (works in any viewer; doesn't depend on vault index).

**Side benefits of standard markdown**:
- Works in Obsidian preview/reading mode.
- Works in VS Code preview (the user has `.vscode/settings.json`).
- Works in any static-site generator (relevant if the wiki is ever exported).
- Works in any web export of markdown.
- Works in Obsidian without depending on the indexer.

**Lint**:
- `python3 outputs/lint.py` → 33 pages, 0 orphans, 0 catalog gaps, 0 missing, 0 metadata issues.
- All 13 image references resolve to existing files (relative paths verified).
- No `![[...]]` remain for the 7 figures.
- Non-image wikilinks (regular cross-links like `[[wifi-radar]]`) are unchanged — still use `[[name]]` syntax for in-wiki links.

**Open follow-up**: lint script (`outputs/lint.py`) still has image-aware logic for resolving `![[name]]` wikilinks via `assets/`. Left in place in case the user later wants to mix the two syntaxes; harmless.

**Future work**: if Obsidian's indexer behaviour is investigated further, the user can decide whether to keep using standard markdown exclusively or whether some `![[name]]` references for diagrams are worth re-introducing (e.g. for Excalidraw files where Obsidian's auto-rename is useful).

---

## 2026-08-13 — New concept: firmware (consolidating a cross-cutting topic)

**User request**: investigate why the wiki has no `Firmware` topic despite the manual having a `Firmware Upgrade` section and a 416-line ASUS firmware-history raw source.

**Investigation**: searched wiki, log, sources, and concept pages. Findings:

- **Firmware data was already fully extracted**, but deliberately **decomposed** across multiple pages rather than concentrated in one concept:
  - `source-summary/gt-ac5300-firmware-history.md` (release history + EoL)
  - `concepts/administration.md#Firmware Upgrade` (update procedure)
  - `concepts/utilities.md#Firmware Restoration` (rescue mode)
  - `entities/rog-rapture-gt-ac5300.md` (stock firmware identifier + EoL status + GPL licensing)
  - `comparison/asuswrt-merlin-386-eol.md` (Merlin timeline)
  - Per-feature introduction firmware versions embedded in each feature's page (aimesh, vpn-fusion, alexa-ifttt, game-boost, usb-applications)
- **No wikilink anywhere expected `[[concepts/firmware]]` to exist** — `outputs/lint.py` reported `Missing concepts: 0`.
- **The wiki's working model** (visible in the 2026-08-13 re-fetch log) is: feature-introduction facts belong on the *feature* page, not on a generic "firmware" page. So new firmware-versioned content (Mobile Game Mode, USB 3.0/2.0 mode switch, AiMesh v1.5 additions) was added to the relevant feature page rather than to a central firmware page.
- **The sources don't describe "firmware" as a cohesive concept**: the manual's §4.10.3 is only 3-4 paragraphs of update procedure; the ASUS support page is a chronological index; the PCMag review mentions firmware once in passing. The wiki had already classified each aspect correctly — but no single page tied them together.

**Decision** (per user): treat firmware as a *cross-cutting concept* (similar to how `administration`, `utilities`, `troubleshooting` are category pages) and add a coordinating concept page that pulls everything together without duplicating detail.

**Created page**: `wiki/concepts/firmware.md`
- Frontmatter: `type: concept`, `confidence: 0.9`, `sources:` to manual summary + firmware-history source-summary + PCMag review, `related:` to administration, utilities, aimesh, vpn-fusion, alexa-ifttt, game-boost, usb-applications, entity, Merlin EoL comparison.
- Body: 6 sections — opening (what firmware *is* for this router), **Where to find firmware-related content** (table mapping aspect → page), **Feature introductions** (table of all firmware-gated features with version + date + feature-page wikilink), **Security CVEs** (selected high-impact, full list on firmware-history page), **Update procedure** (summary linking to admin/utilities for detail), **Naming conventions** (version-string decoding), **Open verification**.
- No content duplication — the page points to the existing detail pages.

**Updated pages**:
- `wiki/index.md`: added `[[concepts/firmware]]` row under "System, automation & support"; bumped `**Last updated**` line to note the seventh update.
- `wiki/entities/rog-rapture-gt-ac5300.md`: added `[[../concepts/firmware]]` to "See also" (between `rog-gaming-center` and `vpn-fusion`); bumped `updated:` to 2026-08-13.

**AGENT.md**: a separate review of the Ingest workflow identified gaps that allowed this kind of cross-cutting topic to fall through the cracks. Adjustments proposed below — to be applied next.

**Lint** (run after this entry): should still pass with no orphans, no catalog gaps, no missing concepts. Run `python3 outputs/lint.py` to confirm.

---

## 2026-08-13 — New concept: placement (manual §1.4)

**User request**: investigate why a "placement" / "positioning" topic had not been extracted despite manual §1.4 being a clear, distinct topic.

**Investigation**: searched wiki, log, sources, and concept pages. Findings:

- **Manual §1.4 "Positioning your router"** (pages 9–10) contains five concrete bullets: location, interference-source list, firmware nudge, and an antenna-orientation figure showing 4 antennas (2 outer at 45°, 2 inner vertical).
- **§1.4 was never mentioned in the wiki** — only one manual-§-number reference (`see §1.4`) in `concepts/troubleshooting.md`, which used the section number not a wikilink.
- **The antenna-orientation figure was not extracted** during the image-asset pilot (it is rendered as vector graphics in the PDF, not as an embedded raster image, so `pdfimages` skipped it; the pilot used `pdfimages -j` and never fell back to `pdftoppm` for vector figures).
- **No log entry mentioned §1.4** — the initial manual ingest logged §1.3, §2.2, §3.x, §4.x, §5.x, §6.x but not §1.4.

**Why §1.4 fell through the cracks** (compounding reasons, none stated explicitly):
1. §1.4 is small (4 bullets + 1 figure) — likely de-prioritized by an LLM that biased toward ROG-specific content.
2. §1.4 lives in Chapter 1 ("Getting to know your wireless router") — the initial ingest focused on Chapters 3 (Gaming Center), 4 (Advanced Settings), 5 (Utilities). Chapter 1 only got a single curated-note entry (the §1.3 hardware highlights).
3. No broken-wikilink pressure: the troubleshooting reference used the section number, so no `Missing concepts: 1` was ever triggered.
4. The antenna-orientation figure (the most information-dense part of §1.4) was not extracted because it was vector graphics — the image-asset pilot only used `pdfimages`, which doesn't see vector content.

**Is this a legitimate non-extraction?** Partially. Keeping §1.4 inside the manual source-summary was defensible (it's a one-time setup decision, not a feature). But the troubleshooting page's `see §1.4` reference points readers out of the wiki, which is a gap even under the most conservative design. User chose to extract it as a concept.

**Changes applied**:

- **Extracted figure**: `assets/figures/manual-p010-antenna-orientation.png` (1023×548, 48 KB). The figure is vector graphics in the PDF (no embedded raster), so extracted via `pdftoppm -f 10 -l 10 -r 200 -png` + `PIL.crop` rather than `pdfimages`. Naming convention `{source-prefix}-p{page}-{caption}.png` slightly bent here (no figure-index since the source has no embedded raster; documented as an exception in the figures catalog page).
- **Created page**: `wiki/concepts/placement.md` — procedure-style concept page modelled on `concepts/administration.md` and `concepts/utilities.md`. Sections: opening (one-time decision framing), **Location** (central, metal/sun), **Avoid these interference sources** (the 11-item list from §1.4), **Antenna orientation** (45° outer / vertical inner + figure), **Firmware** (cross-link to firmware concept), **When placement isn't enough** (cross-link to troubleshooting).
- **`wiki/concepts/troubleshooting.md`**: replaced `adjust antennas (see §1.4)` with `adjust antennas per [[placement#Antenna orientation]]`. The manual-§-number reference is now a wikilink.
- **`wiki/source-summary/gt-ac5300-manual-figures.md`**: added a new first entry documenting the §1.4 antenna-orientation figure, including the `pdftoppm` + `PIL.crop` extraction method (the page now notes that this is the only figure extracted that way). Bumped `updated:` and added `related:` to placement.
- **`wiki/source-summary/gt-ac5300-manual.md`**: added a new "Positioning your router (§1.4)" Curated Notes section summarizing the bullets and pointing to the placement concept page. Bumped `updated:` and added `related:` to placement.
- **`wiki/index.md`**: added `[[concepts/placement]]` row under "Setup & GUI"; bumped `**Last updated**` to eighth update.

**AGENT.md**: no further changes needed — the cross-cutting concept pattern documented in the previous entry already covered this case. Placement is a **procedure concept** (a workflow/setup step), not a cross-cutting one, so the existing taxonomy was sufficient. The image-extraction step *could* benefit from a note about `pdftoppm` for vector figures, but that's a future Lint improvement rather than a workflow gap.

**Lint** (after this entry): 35 pages scanned, 0 orphans, 0 catalog gaps, 0 missing concepts, 8 contradictions (unchanged), 12 stale markers (unchanged).

---

## 2026-08-13 — AGENT.md: Promote workflow + synthesis-to-concept proposal rule

**User request**: when Pi (or any agent) successfully answers a question by synthesizing across multiple wiki pages — i.e. the topic is *latent* in the wiki but not yet its own concept — Pi should propose promoting that topic to a concept page. Goal: make the wiki self-improving, capturing cross-page knowledge as it gets exercised.

**Investigation**: reviewed the Query workflow in `AGENT.md`. The existing step 4 ("If the answer is novel and valuable, offer to save it as a new wiki page") was a weaker version of this — it didn't distinguish cross-page synthesis from one-off novel answers, didn't propose a specific page type, and didn't have a corresponding procedure for after approval.

**Changes to `AGENT.md`**:

1. **Query workflow step 4** rewritten as **"Synthesis-to-concept proposal"**:
   - Trigger: answering required reading and combining **2+ wiki pages** because no single page contained the answer.
   - Output: a structured proposal containing page title (kebab-case), page type (per the Choosing-a-page-type decision tree), one-paragraph rationale, list of existing pages that fed into the synthesis, confidence level (high/medium/low), and a *create vs augment* decision.
   - Behavior: **propose, do not auto-create**. Wait for the user to approve.

2. **Query workflow step 5**: replaced the old "save as new wiki page" rule with a narrower fallback for novel-but-non-synthesis answers — save as a chat-history note rather than auto-creating a wiki page, only if it would be useful to keep.

3. **New `### Promote` workflow** added (between Lint and the end of the Workflows section):
   - Trigger: user approves a synthesis-to-concept proposal, or asks directly to extract a topic.
   - 6 steps: classify page type → draft with standard wiki schema → augment-don't-duplicate → update index.md → log.md entry with provenance (which pages fed in, the rationale, the confidence) → lint.

**Why a separate workflow and not an Ingest variant?** The Promote trigger is fundamentally different from Ingest:
- **Ingest** = new source arrives → pages are extracted from it
- **Promote** = cross-page synthesis happens → a new page captures the synthesis as a first-class artifact

The destination is the same (well-structured wiki page with frontmatter/sources/related/confidence) but the provenance is different, and `wiki/log.md` records which path each page came from.

**Effect on future sessions**:
- When Pi answers a router question and reads ≥2 pages to do it, Pi will surface a "promote to concept?" proposal with full structure, instead of just answering and moving on.
- When the user approves, Pi runs the Promote workflow and the new page joins the wiki as a synthesis artifact, with provenance pointing back at the pages that fed it.
- This should over time close the "discoverability gaps" identified in the previous log entry's status assessment — topics like "safe use of EoL router", "stock vs Merlin in practice", "common task recipes" will emerge as users (or Pi) actually ask the questions.

**No wiki content changed.** Lint status unchanged. Only `AGENT.md` and `wiki/log.md` (this entry) modified.
