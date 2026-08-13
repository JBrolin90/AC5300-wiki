---
title: "Firmware"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
  - "[[../source-summary/gt-ac5300-firmware-history]]"
  - "[[../source-summary/gt-ac5300-pcmag-review]]"
related:
  - "[[administration]]"
  - "[[utilities]]"
  - "[[aimesh]]"
  - "[[vpn-fusion]]"
  - "[[alexa-ifttt]]"
  - "[[game-boost]]"
  - "[[usb-applications]]"
  - "[[../entities/rog-rapture-gt-ac5300]]"
  - "[[../comparison/asuswrt-merlin-386-eol]]"
created: 2026-08-13
updated: 2026-08-13
confidence: 0.9
---
# Firmware

The GT-AC5300 ships with **ASUSWRT** (Merlin-modifiable) carrying a ROG-themed GUI skin ("ROG Gaming Center"). Firmware is a *delivery mechanism* for features rather than a feature itself — most of what is interesting about firmware lives on the relevant feature page. This page is the **canonical index** that pulls those pieces together.

> **End-of-life**: as of 2025-03-12, ASUS has marked the GT-AC5300 EoL; the latest stock firmware `3.0.0.4.386_51582` ships with the verbatim notice *"This model was end of its life, and its firmware, utility, website, and manual will no longer be updated."* See the [[../entities/rog-rapture-gt-ac5300#End-of-life status|entity page]] and [[../source-summary/gt-ac5300-firmware-history|firmware history]] for details.

## Where to find firmware-related content

| Aspect | Where it lives | Notes |
|---|---|---|
| **GUI update procedure** (Browse → Upload, rescue mode trigger) | [[administration#Firmware Upgrade]] | Manual §4.10.3 |
| **Rescue-mode recovery utility** (Firmware Restoration v1.9.0.4) | [[utilities#Firmware Restoration]] | Static IP `192.168.1.x/24`, hold Reset on power-up |
| **Full release history** (2018-07 → 2025-03, all dated entries + release notes) | [[../source-summary/gt-ac5300-firmware-history]] | Primary source: ASUS `supportonly/gt-ac5300/helpdesk_bios/` |
| **End-of-life status + Merlin EoL cross-link** | [[../entities/rog-rapture-gt-ac5300]] | Updated 2026-08-13 |
| **Asuswrt-Merlin vs stock ASUS EoL timeline** | [[../comparison/asuswrt-merlin-386-eol]] | 386.xx branch only |
| **GPLv2 licensing** (firmware includes GPL-licensed third-party code; ASUS publishes source per release) | [[../entities/rog-rapture-gt-ac5300]] (Regulatory section) | Manual appendix |

## Feature introductions (firmware-gated features)

The wiki's convention is to put the firmware-version context on the *feature* page itself. The table below is the consolidated index — click through to each feature page for the per-feature detail.

| Feature | First firmware | Date | Page |
|---|---|---|---|
| **VPN Fusion** | `3.0.0.4.382.15984` | ~2017-08-25 | [[vpn-fusion]] |
| **Alexa + IFTTT** (first wave: code present, China-region disabled) | `3.0.0.4.382.xxxxx` | ~2017-08 | [[alexa-ifttt]] |
| **AiMesh v1** | `3.0.0.4.384.20287` | 2018-01-26 | [[aimesh]] |
| **AiMesh v1.5** — ethernet onboarding, Roaming block list, BlueCave as node | `3.0.0.4.384.32738` | 2018-08-21 | [[aimesh]] |
| **USB 3.0 / 2.0 mode switch** (in Administration → System → USB Settings) | `3.0.0.4.384.32738` | 2018-08-21 | [[usb-applications]] |
| **Alexa + IFTTT** (second wave: "report security status", "devices online", WoL, "check new firmware") | `3.0.0.4.384.45149` | 2018-12-05 | [[alexa-ifttt]] |
| **Adaptive QoS work-from-home categories** (Zoom/Teams, Khan Academy/Udemy, Netflix/Disney+, Peloton/Zwift, etc.) | `3.0.0.4.384.81695` | 2020-03-26 | (mentioned in [[game-boost]]) |
| **Mobile Game Mode** (one-click mobile-device prioritization) | `3.0.0.4.384.81695` | 2020-03-26 | [[game-boost]] |
| **AiMesh v2** — ethernet backhaul, client-binding per AP, guest WiFi on every node, USB access from nodes, BlueCave as node | `3.0.0.4.386.41793` | 2021-01-26 | [[aimesh]] |

## Security CVEs (firmware-fixed)

Selected high-impact CVEs that were fixed in stock firmware for this model. The full list lives in [[../source-summary/gt-ac5300-firmware-history]].

| CVE | Description | Firmware | Date |
|---|---|---|---|
| CVE-2018-14710..14714, -17020/-21/-22 | Multiple security issues | `3.0.0.4.384.45149` | 2018-12-05 |
| CVE-2018-20334, CVE-2018-20336 | (per ASUS release notes) | `3.0.0.4.384.45713` | 2019-04-18 |
| **CVE-2019-15126 (Kr00k)** | Wi-Fi encryption flaw | `3.0.0.4.384.81686` | 2020-03-10 |
| **CVE-2020-12695 (CallStranger)** | UPnP flaw | `3.0.0.4.384.81974` | 2020-07-13 |
| CVE-2021-3450, CVE-2021-3449 | OpenSSL | `3.0.0.4.386.42643` | 2021-05-07 |
| FragAttacks | Wi-Fi aggregation flaws | `3.0.0.4.386.42643` | 2021-05-07 |
| CVE-2021-34174, 2022-23970/1/2/3, 2022-23973, 2022-25595/6 | Multiple | `3.0.0.4.386.46092` | 2022-03-17 |
| CVE-2022-0778 | OpenSSL | `3.0.0.4.386.48377` | 2022-03-30 |
| CVE-2023-28702, CVE-2023-28703 | DoS / httpd | `3.0.0.4.386.51529` | 2023-11-27 |

> **Note**: the GT-AC5300 is **no longer receiving security updates** (EoL 2025-03-12). The CVE list is historical. Anyone operating this router in 2026+ should treat it as unmaintained and consider isolating it from untrusted networks.

## Update procedure (summary)

Two paths. See [[administration#Firmware Upgrade]] for full detail.

- **Normal update** (web GUI): `Advanced Settings → Administration → Firmware Upgrade` → **Check** (auto-fetch) or **Browse** → upload a downloaded `.zip` → router reboots.
- **Manual update from a too-old baseline**: if the running firmware is much older than what you want to install (e.g. upgrading across many branches), ASUS's `FAQ/1008000` "Method 2: Update Manually" is referenced by the firmware page release notes.

If a normal update fails (Power LED flashes slowly) → **rescue mode** → use the **Firmware Restoration** utility from a PC with static IP `192.168.1.x/24` (full steps on [[utilities#Firmware Restoration]]).

## Naming conventions

ASUS firmware version strings for this model follow `MAJOR.MAJOR.MAJOR.MAJOR.BRANCH.BUILD`:

- `3.0.0.4.382.xxxxx` — launch-era (2017) — base for VPN Fusion / first Alexa code
- `3.0.0.4.384.xxxxx` — mid-cycle (2018–2020) — introduced AiMesh v1 → v1.5
- `3.0.0.4.386.xxxxx` — current branch (2021 → 2025) — AiMesh v2, CVE fixes, EoL
- `9.0.0.4.386.xxxxx` — **beta** quick-fix builds (e.g. CVE-2020-25681..25687 DNSmasq quick-fix)
- `_CNonly` suffix — China-region variant (e.g. `.384.45708_CNonly`)

## Open verification

- Pre-2018 firmware dates more granular than "Aug 2017" (early 382 branch). The ASUS support page does not currently extend back into the 382 branch; per-release notes live on the ROG forum and SNBForums (sources cited in [[../source-summary/gt-ac5300-firmware-history]]).
- Whether the next re-fetch of the ASUS support page extends the historical index further into the 382 branch.
