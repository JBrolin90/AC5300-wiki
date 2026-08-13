---
title: "Asuswrt-Merlin 386.xx — End-of-Life for the RT-AC5300 / GT-AC5300"
type: comparison
sources:
  - "[[../source-summary/gt-ac5300-firmware-history]]"
related:
  - "[[../entities/rog-rapture-gt-ac5300]]"
created: 2025-07-16
updated: 2026-08-13
confidence: 0.9
---
# Asuswrt-Merlin 386.xx — End-of-Life for the RT-AC5300 / GT-AC5300

Comparison of the Asuswrt-Merlin 386.xx branch's EoL timeline for the **RT-AC5300** (Merlin's model name for the ROG Rapture **GT-AC5300**) against the stock ASUS 386.xx branch.

## Summary

| Date | Event | Source |
|------|-------|--------|
| 2022-06-22 | Merlin 386.7 — last ASUS GPL merge specific to RT-AC5300 (`386_49335`) | asuswrt-merlin.net changelog-386 |
| 2024-07-20 | Merlin 386.14 — merged with ASUS GPL `386_52805`; **WiFi Radar removed** (citing ASUS's own security concerns in recent stock releases) | asuswrt-merlin.net changelog-386 |
| 2024-11-17 | Merlin 386.14_2 — **final 386.xx release** for the RT-AC5300; security backports only | asuswrt-merlin.net changelog-386 |
| 2025-03-12 | Stock ASUS `3.0.0.4.386_51582` ships with explicit **End-of-Life** notice: "its firmware, utility, website, and manual will no longer be updated" | [[../source-summary/gt-ac5300-firmware-history]] (ASUS support page) |

## Differences worth noting

- **WiFi Radar removal** (Merlin 386.14, 2024-07-20) predated stock ASUS's own removal of the feature on other models and was attributed by RMerlin to Asus's own security concerns. The wiki's [[../concepts/wifi-radar]] page applies to stock firmware pre-2024 only; on Merlin 386.14+ the GUI entry is gone.
- **No 380.xx branch applies to this router** — the 380.xx branch targets older hardware (RT-AC68U, RT-AC87U, etc.). The RT-AC5300 / GT-AC5300 was always 386.xx.

## Why this is a comparison, not a concept page

The Asuswrt-Merlin firmware is a third-party fork — it shares most of the ASUSWRT feature surface, but its release cadence, EoL behaviour, and a few specific features (e.g. WiFi Radar) diverge from stock ASUS. This page records those divergences specifically as they affect the GT-AC5300.

## Notes / caveats

- All dates and version numbers are taken from asuswrt-merlin.net/changelog-386 and the ASUS support page, as recorded in [[../source-summary/gt-ac5300-firmware-history]].
- No future 386.xx releases are expected; both Merlin and ASUS have stopped updating this branch for the RT-AC5300.
