---
title: "GT-AC5300 — ASUS firmware history (last retrieved 2026-08-13)"
type: source-summary
sources:
  - "[[../raw/gt-ac5300-firmware-page-2026-08-13.html]]"
  - "[[../raw/gt-ac5300-firmware-page-2026-08-13.md]]"
  - "[[https://www.asus.com/supportonly/gt-ac5300/helpdesk_bios/]]"
  - "https://rog-forum.asus.com/t5/gaming-routers/rog-rapture-gt-ac5300-firmware-3-0-0-4-384-20308-with-aimesh-and/td-p/758225"
  - "https://www.snbforums.com/threads/aimesh-for-tri-band-routers-rt-ac5300-gt-ac5300.44023/"
  - "https://www.snbforums.com/threads/is-there-any-news-of-ifttt-compliance-in-asus-merlin-firmware-for-rt-68u.40525/"
created: 2025-07-16
updated: 2026-08-13
confidence: 0.9
---
# GT-AC5300 — ASUS firmware history (last retrieved 2026-08-13)

## Status: End-of-life

The latest published firmware (3.0.0.4.386_51582, 2025-03-12) ships with the following notice verbatim from ASUS:

> "This model was end of its life, and its firmware, utility, website, and manual will no longer be updated."

Reference link cited on the firmware page: https://www.asus.com/event/network/eol-product/

Implication for this wiki: no further ASUS-provided versions will appear. Third-party firmware (Asuswrt-Merlin) likewise dropped the 386.xx branch after 386.14_2 (17-Nov-2024, see [[../comparison/asuswrt-merlin-386-eol]] note below).

## Re-fetch 2026-08-13 — notable findings

A re-fetch of the ASUS support page on 2026-08-13 (raw HTML at `raw/gt-ac5300-firmware-page-2026-08-13.html`, ~573 KB) revealed **14 additional 384-branch firmware entries** that were not on the page on 2025-07-16. The page now lists entries back to `3.0.0.4.384.21140` (2018-07-10). Confirmed: the latest stock firmware is unchanged from the prior fetch — still `3.0.0.4.386_51582` (2025-03-12) with EoL notice.

### New entries from the re-fetch (newest → oldest)

| Date | Firmware | Notable change (verbatim or summarized from ASUS) |
|------|----------|---------------------------------------------------|
| 2020-08-03 | `3.0.0.4.384.82037` | "Fixed 5GHz connection speed issues." |
| 2020-07-13 | `3.0.0.4.384.81974` | CVE-2020-12695 (**CallStranger**); reflected XSS; directory traversal; CVE-2017-15653; upgrade-server transport-layer security upgrade. |
| 2020-03-26 | `3.0.0.4.384.81695` | **Adaptive QoS work-from-home categories**: video conferencing (Teams, Zoom, Skype, Hangouts, BlueJeans), online learning (Khan Academy, Udemy, Coursera, TED, VIPKid, 51Talk, XDF, Xueersi), streaming (YouTube, Netflix, HBO NOW, Amazon Prime Video, Disney+, ESPN, MLB.com, iQIY), indoor training (Zwift, Peloton, Onelap). **Mobile Game Mode**: one-click prioritization of a mobile device for best mobile gaming (requires updated ASUS Router App). |
| 2020-03-10 | `3.0.0.4.384.81686` | **CVE-2019-15126 (Kr00k)** vulnerability fix. |
| 2020-03-06 | `3.0.0.4.384.81685` | Firmware-update problem (some conditions); UI bugs; Let's Encrypt bugs; Samba folder-creating bug. |
| 2020-02-03 | `9.0.0.4.384.81551` (Beta) | DDoS fix; Let's Encrypt; **VPN Fusion fixes**; Samba; dual-WAN failover when primary WAN is L2TP. |
| 2019-09-23 | `3.0.0.4.384.81099` | DDoS fix (Altin Thartori); web-control login; Network map list; VPN Fusion bugs; AiMesh node internet-block; Samba compat; OpenVPN; schedule reboot; AiMesh compat; stability. |
| 2019-05-30 | `3.0.0.4.384.70116` | Not rendered as a downloadable card on the support page; only present in the page's embedded config blob. **No release notes available**. |
| 2019-05-22 | `3.0.0.4.384.45717` | DDoS; AiCloud (Matt Cundari); command injection (S1mba Lu); buffer overflow (Javier Aguinaga). |
| 2019-04-18 | `3.0.0.4.384.45713` | CVE-2018-20334; CVE-2018-20336; null-pointer (CodeBreaker/STARLabs); AiCloud buffer overflow (Resecurity Intl); AiMesh LAN-IP-on-IPv6-WAN; AiMesh connect; Network Map; Download Master icon; LAN LED; Traffic-analyzer browser hang; wireless MAC-filter input. |
| 2019-04-03 | `3.0.0.4.384.45708` | Same security fixes as `.45713` plus a "LAN PC cannot find router name in My Network Places when enabling Samba" fix. **`_CNonly` build** (China-region variant). |
| 2018-12-05 | `3.0.0.4.384.45149` | (Already known from prior snbforums research.) Now confirmed verbatim from ASUS: improved tri-band AiMesh backhaul; Lyra/Lyra Mini/Lyra Trio as AiMesh nodes; CVE-2018-14710..14714, -17020/-21/-22; AiCloud/Samba account; DoS (Ruikai Liu); stored XSS (Duda Przemyslaw); OpenSSL update. **New Alexa + IFTTT actions**: "ask ASUS ROUTER to report security status", "ask ASUS ROUTER how many devices are online", IFTTT Wake-on-LAN, IFTTT check-new-firmware-and-upgrade. UI fixes for Dual WAN, Port Forwarding, Restore, VPN Fusion, Adaptive QoS. |
| 2018-09-19 | `3.0.0.4.384.32799` | "Fixed WIFI stability issue." |
| 2018-08-21 | `3.0.0.4.384.32738` | **AiMesh new features**: BlueCave as node; **Roaming block list** in Advanced Settings → Wireless (prevent specific devices from roaming between nodes); **ethernet onboarding** (connect AiMesh router LAN ↔ node WAN via Ethernet before running add-node). Reflected XSS, CSRF, command injection, stack buffer overflow (Rick Ramgattie). Adaptive QoS upload-bandwidth; 4-wire Ethernet compat; USB drives > 2 TB; Samba/FTP folder perms; **USB 3.0/2.0 mode switch** in Administration → System → USB Settings. |
| 2018-07-10 | `3.0.0.4.384.21140` | DDNS-register procedure under dual-WAN load-balance; WAN detect logic; AiMesh onboarding failure when Smart Connect was enabled; AiMesh node notification procedure; AiProtection GUI bugs; OpenVPN-server FAQ URL update. |

### Notable new features confirmed by this re-fetch

| Feature / change | Firmware | Date | Wiki page to update |
|---|---|---|---|
| **Mobile Game Mode** (one-click mobile-device prioritization for gaming) | `3.0.0.4.384.81695` | 2020-03-26 | [[../concepts/game-boost]] |
| **AiMesh ethernet onboarding** (wire the LAN↔WAN before adding node) | `3.0.0.4.384.32738` | 2018-08-21 | [[../concepts/aimesh]] |
| **AiMesh Roaming block list** (pin device to one AP) | `3.0.0.4.384.32738` | 2018-08-21 | [[../concepts/aimesh]] |
| **Adaptive QoS work-from-home / streaming / learning categories** | `3.0.0.4.384.81695` | 2020-03-26 | (no dedicated page; mention in [[../concepts/game-boost]] or [[../concepts/smart-connect]]) |
| **USB 3.0 / 2.0 mode switch** in Administration → System → USB Settings | `3.0.0.4.384.32738` | 2018-08-21 | [[../concepts/usb-applications]] |
| **Kr00k fix (CVE-2019-15126)** | `3.0.0.4.384.81686` | 2020-03-10 | (security; mention in this page's CVE summary) |
| **CallStranger fix (CVE-2020-12695)** | `3.0.0.4.384.81974` | 2020-07-13 | (security) |
| **Adaptive QoS upload-bandwidth fix** | `3.0.0.4.384.32738` | 2018-08-21 | [[../concepts/smart-connect]] (mentions Adaptive QoS) |

### What this changes vs the previous version of this page

- The 2025-07-16 note that the ASUS support page stops at `3.0.0.4.386.41793` is **no longer true**. As of 2026-08-13, the page includes 384-branch entries back to 2018-07-10.
- Several dates that the wiki previously marked `[needs verification]` for older firmware are now confirmed.
- The wiki's pre-2018 firmware notes (from ROG forum / snbforums) are still useful — the ASUS page does not extend back to the 2017-era `.382.xxxxx` builds.

## Feature introduction timeline (compiled from ROG forum + SNBForums)

| Date | Firmware | Event | Confidence |
|------|----------|-------|-----------|
| 2017-06-09 | `3.0.0.4.382.12184` | Launch-era firmware: OpenVPN works, **no VPN Fusion** option. | direct user testing |
| 2017-08-25 | `3.0.0.4.382.15984` | **VPN Fusion** option added to GUI; Alexa code base present (disabled in China region). | direct user testing |
| 2018-01-26 | `3.0.0.4.384.20287` | **AiMesh v1** introduced ("an innovative new router feature that connects multiple ASUS routers to create a whole-home Wi-Fi network"). | direct forum notes |
| ~2018 mid | `3.0.0.4.384.20648` | VPN Fusion functional in this build (regressed in later versions; recovered eventually). | single user report |
| 2018-12-05 | `3.0.0.4.384.45149` | **New Alexa skills + new IFTTT actions** added: "ask ASUS ROUTER to report security status", "how many devices online"; IFTTT: Wake on LAN, "check new firmware and upgrade". Same firmware also adds Lyra-series support as AiMesh nodes for GT-AC5300. | ASUS release note verbatim |
| 2021-01-26 | `3.0.0.4.386.41793` | **AiMesh v2**: ethernet backhaul, client-binding per AP, guest WiFi on all nodes, USB access from nodes, support for adding BlueCave as a mesh node. New Family interface in ASUS Router mobile app. | direct ASUS release note |
| 2021-05-07 | `3.0.0.4.386.42643` | CVE fixes; FragAttacks fix. | direct |
| 2022-03-17 | `3.0.0.4.386.46092` | Multiple CVE fixes; AiMesh guest network fix; IPSec VPN fix; DDNS IPv6 fix. | direct |
| 2022-03-30 | `3.0.0.4.386.48377` | OpenSSL CVE-2022-0778; Stored XSS fix; 3rd-party DNS server list in WAN → DNS. | direct |
| 2023-11-27 | `3.0.0.4.386.51529` | DoS + httpd fixes; null-pointer-deref fixes; CVE-2023-28702/28703. | direct |
| 2024-11-12 | `3.0.0.4.386.51569` | Input validation, AiCloud password protection, cert/buffer hardening. | direct |
| 2025-03-12 | `3.0.0.4.386.51582` | **End-of-life** notice alongside UI/Chrome fix and input-validation hardening. | direct |

## Confirmed entries (ASUS, supportonly/gt-ac5300/helpdesk_bios, last retrieved 2026-08-13)

Listed newest → oldest in the order ASUS serves them. SHA-256/MD5 checksums and download URLs are on the original ASUS page; this wiki does not duplicate them. The 386-branch entries are official releases; the 384-branch entries (newly visible as of 2026-08-13) are also official releases — the ASUS support page now includes them. The two `9.x.x.x` entries are beta builds.

| Date | Version (file name suffix) | Notable change |
|------|---------------------------|----------------|
| 2025-03-12 | `3.0.0.4.386_51582` | EoL notice; UI/Chrome fix; input validation hardening |
| 2024-11-12 | `3.0.0.4.386_51569` | Input validation hardening; AiCloud password protection; cert/buffer/file-access hardening |
| 2023-11-27 | `3.0.0.4.386_51529` | DoS fixes (firewall + httpd); null-pointer-dereference fixes; CVE-2023-28702, CVE-2023-28703 |
| 2022-03-30 | `3.0.0.4.386.48377` | OpenSSL CVE-2022-0778; stored XSS fix (CVE Milan Kyselica of IstroSec); 3rd-party DNS server list in WAN → DNS |
| 2022-03-17 | `3.0.0.4.386.46092` | Multiple CVE fixes (CVE-2021-34174, 2022-23970/1/2/3, 2022-23973, 2022-25595/6); AiMesh guest network fix; IPSec VPN fix; DDNS IPv6 fix; UI bugfixes |
| 2021-05-07 | `3.0.0.4.386.42643` | CVE-2021-3450 / CVE-2021-3449 (OpenSSL); FragAttacks |
| 2021-02-03 | `9.0.0.4.386.41994` (beta) | DNSmasq CVE-2020-25681..25687 quick-fix beta |
| 2021-01-26 | `3.0.0.4.386.41793` | **AiMesh 2.0**: ethernet backhaul, client-binding per AP, guest WiFi on all nodes, USB access from nodes; new ASUS Router Family interface in mobile app |
| 2020-08-03 | `3.0.0.4.384.82037` | "Fixed 5GHz connection speed issues." |
| 2020-07-13 | `3.0.0.4.384.81974` | CVE-2020-12695 (**CallStranger**); reflected XSS; directory traversal; CVE-2017-15653; TLS upgrade on update server. |
| 2020-03-26 | `3.0.0.4.384.81695` | **Adaptive QoS work-from-home categories** (Teams, Zoom, Skype, Hangouts, BlueJeans; Khan Academy, Udemy, Coursera, TED, VIPKid, 51Talk, XDF, Xueersi; YouTube, Netflix, HBO NOW, Amazon Prime Video, Disney+, ESPN, MLB.com, iQIY; Zwift, Peloton, Onelap); **Mobile Game Mode**. |
| 2020-03-10 | `3.0.0.4.384.81686` | **CVE-2019-15126 (Kr00k)** vulnerability fix. |
| 2020-03-06 | `3.0.0.4.384.81685` | Firmware-update fix (some conditions); UI bugs; Let's Encrypt bugs; Samba folder-creating bug. |
| 2020-02-03 | `9.0.0.4.384.81551` (beta) | DDoS fix; Let's Encrypt; **VPN Fusion fixes**; Samba; dual-WAN failover when primary WAN is L2TP. |
| 2019-09-23 | `3.0.0.4.384.81099` | DDoS fix (Altin Thartori); web-control login; Network map list; VPN Fusion bugs; AiMesh node internet-block; Samba compat; OpenVPN; schedule reboot; AiMesh compat; stability. |
| 2019-05-30 | `3.0.0.4.384.70116` | Not rendered as a downloadable card on the support page; only present in the page's embedded config blob. No release notes available. |
| 2019-05-22 | `3.0.0.4.384.45717` | DDoS; AiCloud (Matt Cundari); command injection (S1mba Lu); buffer overflow (Javier Aguinaga). |
| 2019-04-18 | `3.0.0.4.384.45713` | CVE-2018-20334; CVE-2018-20336; null-pointer (CodeBreaker/STARLabs); AiCloud buffer overflow (Resecurity Intl); AiMesh LAN-IP-on-IPv6-WAN; AiMesh connect; Network Map; Download Master icon; LAN LED; Traffic-analyzer browser hang; wireless MAC-filter input. |
| 2019-04-03 | `3.0.0.4.384.45708` | Same security fixes as `.45713` plus "LAN PC cannot find router name in My Network Places when enabling Samba" fix. **`_CNonly` build** (China-region variant). |
| 2018-12-05 | `3.0.0.4.384.45149` | Improved tri-band AiMesh backhaul; Lyra/Lyra Mini/Lyra Trio as AiMesh nodes; CVE-2018-14710..14714, -17020/-21/-22; AiCloud/Samba account; DoS (Ruikai Liu); stored XSS (Duda Przemyslaw); OpenSSL update. **New Alexa + IFTTT actions**. UI fixes for Dual WAN, Port Forwarding, Restore, VPN Fusion, Adaptive QoS. |
| 2018-09-19 | `3.0.0.4.384.32799` | "Fixed WIFI stability issue." |
| 2018-08-21 | `3.0.0.4.384.32738` | **AiMesh new features**: BlueCave as node; **Roaming block list**; **ethernet onboarding**. Reflected XSS, CSRF, command injection, stack buffer overflow (Rick Ramgattie). Adaptive QoS upload-bandwidth; 4-wire Ethernet compat; USB drives > 2 TB; Samba/FTP folder perms; **USB 3.0/2.0 mode switch** in Administration → System → USB Settings. |
| 2018-07-10 | `3.0.0.4.384.21140` | DDNS-register procedure under dual-WAN load-balance; WAN detect logic; AiMesh onboarding failure when Smart Connect was enabled; AiMesh node notification procedure; AiProtection GUI bugs; OpenVPN-server FAQ URL update. |


The ASUS support page also references **two pre-2018 entries** in its embedded config blob (filenames `FW_GT_AC5300_3004384xxxxx.zip` from before 2018-07-10), but those are not currently rendered as downloadable cards and have no release notes on the page. The ROG forum and SNBForums threads referenced in the frontmatter sources remain the best source for those.

## Confirmed via Asuswrt-Merlin changelog (not ASUS)

From `asuswrt-merlin.net/changelog-386` and `changelog-380`, the GT-AC5300 (Merlin models it as "RT-AC5300") lifecycle:

- **Merlin 386.14_2** (17-Nov-2024) — final 386.xx release. Security backports only.
- **Merlin 386.14** (20-July-2024) — merged with ASUS GPL `386_52805`. **Wifi Radar was removed** (citing Asus's own security concerns). **Reminder**: all 386.xx models stopped at the end of 2024.
- **Merlin 386.7** (22-June-2022) — merged with ASUS GPL `386_49335` specifically for the RT-AC5300.

(Only the 386.xx branch applies to the GT-AC5300; the 380.xx branch is for older hardware.)

## Resolved open verifications (as of this session)

| Feature | Page | Confirmed |
|---|---|---|
| VPN Fusion (stock-ASUS) | [[../concepts/vpn-fusion]] | First appearance in GUI: firmware **`3.0.0.4.382.15984`** (~Aug 2017). ROG-only until 388_2xxxx. |
| AiMesh v1 | [[../concepts/aimesh]] | Firmware **`3.0.0.4.384.20287`** (2018-01-26). v2 in `3.0.0.4.386.41793` (2021-01-26). |
| Alexa + IFTTT (initial) | [[../concepts/alexa-ifttt]] | 382 branch (~Aug 2017). (RMerlin statement.) |
| Alexa + IFTTT (second wave) | [[../concepts/alexa-ifttt]] | Firmware **`3.0.0.4.384_45149`** (2018-12-05): added "report security status", "how many devices online", Wake on LAN, "check new firmware". |

## Notes for future re-ingest

- The Wayback Machine (`web.archive.org`) was blocked from this environment on 2025-07-16 — unblocked in that session only on DuckDuckGo via the `ddgs` Python package.
- The Merlin-incompatibility statements (RMerlin himself on SNBForums) are useful corroboration for stock-firmware feature boundary dates.
- For pre-2018 firmware (`3.0.0.4.382.xxxxx` and very early `3.0.0.4.384.xxxxx` releases), the ROG forum (rog-forum.asus.com) houses per-release discussion threads with verbatim release notes. The ASUS support page does not currently extend back into the 382 branch.
- As of the 2026-08-13 re-fetch, the ASUS support page **does** include 384-branch entries back to 2018-07-10, contradicting the 2025-07-16 note that "versions older than `3.0.0.4.386.41793` are not currently published". A future re-fetch should re-check whether the page has extended further into the 382 branch.
- The Jina web reader truncates this page to ~8 KB; full extraction requires `curl` of the raw HTML (saved to `raw/gt-ac5300-firmware-page-YYYY-MM-DD.html`) and parsing the embedded `productSupportBIOS` JSON config for entries that are not rendered as downloadable cards (e.g. `3.0.0.4.384.70116`, 2019-05-30).
