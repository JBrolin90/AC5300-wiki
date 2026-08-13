---
title: "ROG Gaming Center"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
related:
  - "[[quick-internet-setup]]"
  - "[[../entities/rog-rapture-gt-ac5300]]"
created: 2025-07-16
updated: 2025-07-16
confidence: 0.9
---
# ROG Gaming Center

## Login

`http://router.asus.com` → login page. First visit redirects to [[quick-internet-setup]]. Default login is `admin` / `<password set during QIS>`; factory-reset login is `admin` / `admin`.

## Panel structure

| Panel | Contains |
|---|---|
| **General** | Network Map, [[game-ips\|Game IPS]], [[game-boost\|Game Boost]], [[game-private-network\|Game Private Network]], [[game-profile\|Game Profile]], [[game-radar\|Game Radar]], [[wifi-radar\|WiFi Radar]], [[vpn\|VPN]], Traffic Analyzer |
| **Advanced Settings** | [[wireless-settings\|Wireless]], Guest Network, [[lan-wan\|LAN]], [[lan-wan\|WAN]], USB Application, AiCloud, [[ipv6\|IPv6]], [[firewall\|Firewall]], [[administration\|Administration]], System Log, [[smart-connect\|Smart Connect]] |

## Top command buttons

The login page surfaces a **Top command buttons** bar plus an **Information banner** with live network status, connected devices, and worldwide game-server ping values.

## Dashboard

`General → Dash Board`. Two real-time views:
- **Network traffic** — live RX/TX per interface
- **Network ping + ping deviation** — per the manual:
  - < 99 ms ping = good
  - < 150 ms ping = acceptable
  - > 150 ms ping = hard to play smoothly
  - Lower ping deviation = better (high deviation causes rubber-banding)

## Versioning

Features may vary across firmware versions (per §3.1). Always check `Administration → Firmware Upgrade` after setting up.
