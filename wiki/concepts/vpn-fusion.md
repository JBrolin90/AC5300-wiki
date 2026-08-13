---
title: "VPN Fusion"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-pcmag-review]]"
  - "[[../source-summary/gt-ac5300-firmware-history]]"
  - "https://rog-forum.asus.com/t5/gaming-routers/rog-rapture-gt-ac5300-firmware-3-0-0-4-384-20308-with-aimesh-and/td-p/758225"
related:
  - "[[vpn]]"
  - "[[game-private-network]]"
created: 2025-07-16
updated: 2025-07-16
confidence: 0.85
---
# VPN Fusion

## What it does

Without VPN Fusion, when you enable a VPN client on the router, **all** WAN-bound traffic is tunneled — and that often hurts real-time game latency. VPN Fusion lets you route **specific clients** (or specific traffic classes) out the VPN while the rest goes direct.

PCMag's description:

> "For users who run a VPN that may degrade gaming performance, the VPN Fusion feature allows you to use a VPN connection alongside an ordinary internet connection to keep your games running at top speed."

## Where it sits in the GUI

Not in the May-2017 manual. Implied to live under `General → VPN` or `Advanced → WAN`, paired with the existing [[vpn]] tab. [needs verification — exact menu path not documented in the sources ingested so far].

## How it relates to existing concepts

- [[vpn]] — built-in PPTP *server* and NAT-passthrough are different functionality.
- [[game-private-network]] — WTFast GPN is its own system; VPN Fusion is orthogonal (you could use both, but VPN Fusion is generic, GPN is per-game).

## Firmware introduction (confirmed via ROG forum / SNBForums)

- **First appearance**: firmware **`3.0.0.4.382_15984`** (dated 2017-08-25 by a user testing list on the ROG forum). The user's firmware progression notes:
  - `3.0.0.4.382.12184` (2017-06-09) — OpenVPN works, **no VPN Fusion** option in the GUI.
  - `3.0.0.4.382.15984` (2017-08-25) — **VPN Fusion** option now present.
- **Working implementation**: `3.0.0.4.384_20648`. Per a 2024 user report on the ROG forum, "VPN Fusion" was functioning in this build but regressed in the next 4 firmware releases; recovered in newer builds.
- **ROG-only exclusivity**: VPN Fusion was launched as a ROG (GT-xxxx) router feature. SNBForums (2022+ reports) confirms: "VPN Fusion is currently only available on ROG models (GT-*****). However this will be made available to non-ROG models starting with firmware 3.0.0.4.388_2xxxx."

## Open verification

- Exact menu path and supported VPN protocols (OpenVPN? WireGuard? PPTP/L2TP only?).
- Whether VPN Fusion requires WTFast/GPN to be disabled, or whether the three can coexist.
- Which Asuswrt-Merlin / third-party firmware version first made VPN Fusion available to non-ROG ASUS routers.
