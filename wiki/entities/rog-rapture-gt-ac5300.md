---
title: "ROG Rapture GT-AC5300"
type: entity
sources:
  - "[[../../raw/E12817_GT_AC5300_Manual.pdf]]"
  - "[[../source-summary/gt-ac5300-manual]]"
  - "[[../../raw/Asus ROG Rapture GT-AC5300 Review.md]]"
  - "[[../source-summary/gt-ac5300-pcmag-review]]"
  - "[[../source-summary/gt-ac5300-firmware-history]]"
created: 2025-07-16
updated: 2025-07-16
confidence: 0.95
---
# ROG Rapture GT-AC5300

## Identity

| Field | Value |
|---|---|
| Manufacturer | ASUS (ASUSTeK Computer Inc.) |
| Brand line | ROG (Republic of Gamers) |
| Model | Rapture GT-AC5300 |
| Document | E12817, First Edition, May 2017 |
| FCC ID (referenced) | 3568A-RTGZ00 (per IC filing) |
| Class | Wireless router (default); also supports AP and Media Bridge modes |

## Hardware

- **Radios**: triple-band, simultaneous 2.4 GHz + 5 GHz-1 + 5 GHz-2
- **Antennas**: 8 × external dipole (Whayu C660-510391-A, Reversed-SMA). Gain 2.14 dBi @ 2.4 GHz, 2.98 dBi @ 5 GHz
- **WAN**: 1 × Gigabit WAN
- **LAN**: 8 × Gigabit Ethernet split as:
  - **Gaming ports** (1–2): hardware packet prioritization
  - **Link Aggregation ports** (5–6): for 802.3ad aggregation (manual wording says "802.11ad" — likely a typo; [needs verification])
  - **LAN ports** (3–4, 7–8)
- **USB**: 1 × USB 3.0 + 1 × USB 2.0 (storage up to 4 TB, printer, 3G/4G modem)
- **Power**: 19 V DC, 3.42 A adapter
- **Environment**: 0–40 °C operating, 50–90 % humidity
- **Capacity**: 300,000 concurrent sessions
- **Power-saving**: ASUS Green Network Technology, up to 70 % savings

## Front-panel LEDs and buttons

Power, 2.4 GHz, 5 GHz, WAN, LAN, WPS LEDs. Buttons: Power, LED on/off, WPS, Wi-Fi on/off, Reset (rear).

## Firmware: ASUSWRT with ROG Gaming Center skin

GUI entry: `http://router.asus.com` (default IP `192.168.1.1`). First login is admin / `<QIS password>`; factory reset restores admin / admin.

## Distinctive features

- [[../concepts/game-ips|Game IPS]] — Trend Micro-powered protection
- [[../concepts/game-boost|Game Boost]] — one-click gaming traffic prioritization + QoS
- [[../concepts/game-private-network|Game Private Network]] — WTFast GPN integration
- [[../concepts/game-profile|Game Profile]] — preset port-forwarding per game
- [[../concepts/game-radar|Game Radar]] — per-game server ping tool
- [[../concepts/wifi-radar|WiFi Radar]] — wireless troubleshooting
- Hardware gaming-prioritized LAN ports
- [[../concepts/smart-connect|Smart Connect]] tri-band steering

## Regulatory

- FCC Part 15 Class B, indoor use only, channels 1–11 (US/CA), 31 cm RF exposure minimum.
- IC RSS-102 (Canada). CE Class B. NCC (Taiwan). AEEE (Turkey).
- GPLv2 firmware — source code published by ASUS with each release.

## See also

- [[../source-summary/gt-ac5300-manual]] — structured manual summary
- [[../source-summary/gt-ac5300-manual-text]] — full extracted text
- [[../source-summary/gt-ac5300-pcmag-review]] — PCMag 2018 review (with benchmarks and feature deltas)
- [[../comparison/gt-ac5300-vs-competitors]] — PCMag's 2018 competitor snapshot
- [[../concepts/quick-internet-setup]] — first-time setup flow
- [[../concepts/rog-gaming-center]] — firmware GUI overview
- [[../concepts/vpn-fusion]] — VPN + direct-internet split
- [[../concepts/aimesh]] — mesh-controller operation mode
- [[../concepts/alexa-ifttt]] — voice / IFTTT integration

## PCMag benchmarks (review source, 2018)

| Test | Result |
|---|---|
| SU-MIMO 2.4 GHz close | 128 Mbps |
| SU-MIMO 2.4 GHz @ 30 ft | 75 Mbps |
| SU-MIMO 5 GHz close | **601 Mbps** (first router PCMag had seen break 600) |
| SU-MIMO 5 GHz @ 30 ft | 330 Mbps |
| MU-MIMO 5 GHz close | 225 Mbps |
| MU-MIMO 5 GHz @ 30 ft | 135 Mbps |
| USB read | 42 MB/s |
| USB write | 39 MB/s |

Historical snapshot — replaced by Wi-Fi 6/7 routers by 2026; kept here for reference.

## Awards / recognition

- **PCMag Editors' Choice** (high-end routers), 2018 — John R. Delaney. Rating 4.5/5, "Best of the year 2018."

## End-of-life status

Per ASUS's own firmware page (last entry 2025-03-12, `3.0.0.4.386_51582`), the GT-AC5300 is **end-of-life**: "its firmware, utility, website, and manual will no longer be updated." See [[../source-summary/gt-ac5300-firmware-history]] for the confirmed release slice. Third-party firmware lineage (Asuswrt-Merlin) likewise dropped the 386.xx branch after 2024-11-17.
