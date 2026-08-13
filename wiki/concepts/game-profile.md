---
title: "Game Profile"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
  - "[[../source-summary/gt-ac5300-manual-figures]]"
related:
  - "[[game-radar]]"
  - "[[game-boost]]"
created: 2025-07-16
updated: 2026-08-13
confidence: 0.85
---
# Game Profile

![Game Profile curated list — manual p. 36 (StarCraft, Assassin's Creed, Diablo, World of Warcraft, League of Legends, etc.)](../../assets/figures/manual-p036-149-game-profile-curated-list.png)

*Figure: Game Profile curated list — manual p. 36. Shows the Famous Game List (StarCraft, Assassin's Creed, Diablo, World of Warcraft, League of Legends, Uncharted, FIFA 17, Halo, etc.) and the per-game Port Forwarding List editor.*

## Problem it solves

Some games fail to establish peer connections because the router or ISP is blocking the required ports or the device is behind a strict NAT. Manually finding and opening the right ports per game is tedious and per-game-version specific.

## How Game Profile works

`General → Game Profile`:

1. Toggle **Yes** to enable port forwarding
2. Pick a game from the **Famous Game List** (the list is updated over time by firmware updates)
3. Click add → click Apply

The router then applies the right port-forwarding rules for that title.

## Limits

- The list depends on what's bundled in the current firmware — older games or newly released titles may not be present.
- Each title adds port-forwarding entries to the WAN → Virtual Server list; if you no longer play a game, consider removing its profile.
- Pair with [[game-radar]] to verify the chosen server responds well.
