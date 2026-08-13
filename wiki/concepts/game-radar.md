---
title: "Game Radar"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
  - "[[../source-summary/gt-ac5300-manual-figures]]"
related:
  - "[[game-profile]]"
  - "[[game-private-network]]"
  - "[[game-boost]]"
created: 2025-07-16
updated: 2026-08-13
confidence: 0.85
---
# Game Radar

![Game Radar world map — manual p. 38 (per-region server ping markers and Flag/Country/IP/Ping Status table)](../../assets/figures/manual-p038-153-game-radar-world-map.png)

*Figure: Game Radar world map — manual p. 38. Shows the per-region server ping markers and the Flag/Country/IP/Ping Status table.*

## How to use

1. `General → Game Radar`
2. Pick a game from the list
3. Read the **Ping Status** column for each server
4. Pick the lowest-ping server and queue there

## Reference latency bands

Per the manual's [[../source-summary/gt-ac5300-manual#Dashboard (§3.2)|Dashboard]] section:

| Ping | Quality |
|---|---|
| < 99 ms | Good |
| < 150 ms | Acceptable |
| > 150 ms | Hard to play smoothly |

Lower **ping deviation** is better — high deviation causes in-game "toggling" (rubber-banding).

## Use it with

- [[game-profile]] — once you know which server you want, set the port-forward profile for that game.
- [[game-private-network]] — if all servers are far/high-ping, GPN can route through WTFast's optimized paths.
