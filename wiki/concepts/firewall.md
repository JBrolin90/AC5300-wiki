---
title: "Firewall"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
related:
  - "[[game-ips]]"
  - "[[lan-wan]]"
created: 2025-07-16
updated: 2025-07-16
confidence: 0.9
---
# Firewall

> Firewall is **enabled by default** (§4.9 intro).

`Advanced Settings → Firewall`

## General

- **Enable Firewall**: Yes
- **Enable DoS protection**: Yes (may affect performance)
- **Logged packets type**: Dropped / Accepted / Both

## URL Filter

Block specific URLs.

- Enable: ON
- Enter URL, click add, Apply

> **Important caveat**: URL Filter is **DNS-query-based**. If a client already visited a URL, the DNS cache holds it and the filter doesn't trigger. **Clear the DNS cache before enabling.**

## Keyword Filter

Block URLs containing specific words/phrases.

- Enable: ON
- Enter word/phrase, click add, Apply

> Same DNS-cache caveat as URL Filter. Additionally: HTTP-compressed pages can't be filtered, and **HTTPS pages cannot be blocked** by keyword.

## Network Services Filter

Block LAN → WAN packet exchanges on specific services (Telnet, FTP, etc.). Modes:

- **Black List**: block listed services, allow everything else
- **White List**: allow only listed services, block everything else

Per-entry fields: Source IP, Destination IP, Port Range, Protocol. Plus a day/time schedule.

## IPv6 Firewall

Default behavior: block all unsolicited inbound IPv6 traffic. This page lets you allow inbound traffic from specified services.

See also [[ipv6]].

## Differences from Game IPS

[[game-ips|Game IPS]] is the Trend Micro cloud-powered protection (URL reputation, malware, infected-device prevention). The Firewall is the router's own stateful packet filter (DoS, port filters). They're complementary — leave both on.
