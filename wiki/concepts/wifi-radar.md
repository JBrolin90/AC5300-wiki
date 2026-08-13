---
title: "WiFi Radar"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
related:
  - "[[wireless-settings]]"
created: 2025-07-16
updated: 2025-07-16
confidence: 0.85
---
# WiFi Radar

## Caveat

> **Manual note (§3.8)**: Enabling WiFi Radar may result in a drop in wireless performance. Only enable Wi-Fi Radar when needed.

It's an active measurement tool — leave it off in production.

## Setup

1. `General → WiFi Radar`
2. **Settings** tab: configure WiFi Radar parameters (bands, scan interval)
3. Set the schedule for data recording
4. Click **Start Data Collection**
5. Click **Submit**

## Sub-views

| Sub-feature | What it shows |
|---|---|
| WiFi Site Survey | All wireless networks in range, with signal/channel info |
| Wireless Channel Statistics | Channel usage across all bands + channel distribution |
| Advanced Troubleshooting | WiFi glitch statistics (interference, drops, retries) |

## When to use

- Picking the cleanest 2.4 GHz or 5 GHz channel when [[wireless-settings#General|General → Wireless]] is set to Auto.
- Diagnosing intermittent dropouts vs. interference from neighbors.
- Verifying changes after enabling/disabling USB 3.0 interference reduction in [[wireless-settings#Professional|Professional settings]].
