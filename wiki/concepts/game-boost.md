---
title: "Game Boost"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
  - "[[../source-summary/gt-ac5300-pcmag-review]]"
related:
  - "[[../entities/rog-rapture-gt-ac5300]]"
  - "[[game-private-network]]"
created: 2025-07-16
updated: 2026-08-13
confidence: 0.9
---
# Game Boost

## What it does

When **Game Boost** is enabled, the GT-AC5300 tags gaming packets as top priority at the QoS layer so that bulk traffic (downloads, updates, sync) doesn't crowd out real-time play. Path: `General → Game Boost`.

## Apps Analysis

Per-app traffic identification. Toggle ON under the Game Boost tab → Apps Analysis pane. Required for accurate QoS classification when QoS Type is Adaptive.

## QoS

Path: `General → Game Boost → QoS`.

Steps:
1. Enable QoS: ON
2. Enter **upload** and **download** bandwidth (get values from ISP, or `http://speedtest.net`)
3. Pick QoS Type:
   - **Adaptive** — auto-classifies per app (requires Apps Analysis)
   - **Traditional** — manual priority rules
   - **Bandwidth limiter** — caps total throughput
4. Apply

## Web History

Path: `General → Game Boost → Web History`. Lists URLs visited per client; **Refresh** clears the list. (Pure visibility tool — no blocking. For blocking see [[game-ips#Parental Control — Web & Apps Filters]].)

## Related

- For route-optimized game traffic (latency reduction, not just local prioritization), see [[game-private-network]].
- For per-game server diagnostics before enabling boost, see [[game-radar]].

## Review-side detail (PCMag, 2018)

The reviewer describes GameBoost as prioritizing traffic to **Sony PlayStation**, **Nintendo Wii / 3DS**, and **Microsoft Xbox One** consoles. The manual does not enumerate these consoles explicitly; treat the review's list as independent confirmation. (Console-detection is implicitly part of the [[../concepts/game-profile]] matching mechanism.)

## Mobile Game Mode (later addition)

Added in firmware `3.0.0.4.384.81695` (2020-03-26) per the [ASUS support page release note](../source-summary/gt-ac5300-firmware-history). A one-click toggle that puts a single **mobile device** at the highest QoS priority, separate from the console-level Game Boost rules above.

- Requires the ASUS Router App (Android ≥ 1.0.0.5.44, iOS ≥ 1.0.0.5.41).
- Useful for mobile-game lag control (PUBG Mobile, Call of Duty Mobile, etc.) where the per-console rules of Game Boost don't match the device.
- Co-shipped with the new "work-from-home / streaming / learning" Adaptive QoS categories in the same release.
