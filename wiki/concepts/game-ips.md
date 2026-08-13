---
title: "Game IPS"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
  - "[[../source-summary/gt-ac5300-manual-figures]]"
related:
  - "[[../entities/rog-rapture-gt-ac5300]]"
  - "[[rog-gaming-center]]"
created: 2025-07-16
updated: 2026-08-13
confidence: 0.9
---
# Game IPS

![Game IPS overview — manual p. 23 (Router Security Assessment, Malicious Sites Blocking, Two-Way IPS, Infected Device Prevention, Parental Controls)](../../assets/figures/manual-p023-128-game-ips-overview.png)

*Figure: Game IPS overview — manual p. 23. Shows Router Security Assessment (Scan), Malicious Sites Blocking, Two-Way IPS, Infected Device Prevention, and Parental Controls tabs.*

## What it covers

Game IPS is the GT-AC5300's branded name for the security suite that combines Trend Micro's network protection engine with the router's own outbound/inbound filter. Five sub-features, all in **General → Game IPS**:

| Sub-feature | What it does |
|---|---|
| Network Protection (Router Weakness Scan) | One-click audit of router config; click "Secure Your Router" to fix weak items |
| Blocking Malicious Sites | Block known-bad URLs from a cloud database (auto-on after scan) |
| Two-Way IPS | Blocks common exploits in router config (auto-on after scan) |
| Infected Device Prevention and Blocking | Prevents compromised LAN clients from phoning home with PII/infection status; optional e-mail alerts |
| Parental Control | Web & Apps Filter + Time Scheduling per client |

## Network Protection workflow

1. `General → Game IPS → Network Protection → Scan`
2. Router Security Assessment page lists items as Yes / No / Weak / Very Weak
3. Either click individual items to fix manually, or click **Secure Your Router** to auto-configure
4. Confirm with OK

> **Manual quote (§3.3.1)**: "Items marked with Yes on the Router Security Assessment page are considered to be safe."

## Parental Control — Web & Apps Filters

Categories: Adult, Instant Message and Communication, P2P and File Transfer, Streaming and Entertainment. Accepts EULA on first activation; per-client profile; device identified by name or MAC.

## Parental Control — Time Scheduling

Day/time grid per client. Requires NTP-synced system time (set under [[administration]] → System). Client name cannot contain special characters or spaces.

## Caveats

- Most sub-features are **auto-enabled** after running the Router Weakness Scan — flipping them manually off may undo auto-protection.
- Infected-Device alerts require e-mail account configuration (provider, address, password) under Alert Preference.
