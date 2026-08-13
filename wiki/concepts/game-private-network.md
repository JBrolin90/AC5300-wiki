---
title: "Game Private Network (GPN)"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
related:
  - "[[game-boost]]"
  - "[[game-radar]]"
created: 2025-07-16
updated: 2025-07-16
confidence: 0.85
---
# Game Private Network (GPN)

## Provider

WTFast (https://www.wtfast.com/). The router UI embeds WTFast account login and GPN rule management.

## Setup workflow

1. `General → Game Boost → WTFast` (path per §3.5)
2. Create a free WTFast account at wtfast.com (free tier = 1 device)
3. Log in inside the router UI
4. Under WTFast Rules, create a profile for the device you want GPN'd
5. Pick a GPN server (Auto or specific) and click **Apply**
6. **Enable the GPN profile BEFORE launching the game**

## Free vs paid

- **Free**: 1 device
- **Paid**: Multiple devices, subscription via the **Upgrade** button in the WTFast panel

## When to use vs. Game Boost

| Tool | Best for |
|---|---|
| [[game-boost\|Game Boost]] (local QoS) | Resolving local contention — downloads, streaming, updates crowding out game traffic on your own network |
| **GPN** | Resolving ISP routing issues — game server is far away or routed through bad hops |

You can use both together: GPN at the route layer, Game Boost at the LAN-priority layer.
