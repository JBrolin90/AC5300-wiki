---
title: "ASUS ROG Rapture GT-AC5300 — User Manual"
type: source-summary
sources:
  - "[[../../raw/E12817_GT_AC5300_Manual.pdf]]"
  - "[[gt-ac5300-manual-text.txt]]"
related:
  - "[[../entities/rog-rapture-gt-ac5300]]"
created: 2025-07-16
updated: 2025-07-16
confidence: 0.95
---
# ASUS ROG Rapture GT-AC5300 — User Manual

## Document Metadata

- **Document ID**: E12817, First Edition, May 2017
- **Producer**: Adobe InDesign CS6 / Adobe PDF Library 10.0.1 (PDF version 1.6)
- **Pages**: 152
- **Text layer**: Present (PDF is searchable; no OCR required for ingest)
- **Extracted via**: `pdftotext -layout` to `gt-ac5300-manual-text.txt`

## Manual Structure

| Ch. | Title | Notes |
|---|---|---|
| 1 | Getting to know your wireless router | Hardware, ports, LEDs, setup requirements |
| 2 | Getting started | Wired/wireless setup, QIS, Wi-Fi connection |
| 3 | Configuring General Settings (ROG Gaming Center) | Gaming features, dashboard, traffic analyzer |
| 4 | Configuring the Advanced Settings | Wireless, LAN, WAN, USB, AiCloud, IPv6, firewall, smart connect |
| 5 | Utilities | Device Discovery, Firmware Restoration, Printer Server, Download Master |
| 6 | Troubleshooting | Basic steps and FAQs |
| App. | Notices, GPLv2, hotline numbers | Regulatory + global support contacts |

## Curated Notes

### Hardware highlights (§1.3)
- 8 external antennas (Whayu C660-510391-A dipole, Reversed-SMA, 2.14 dBi @ 2.4 GHz / 2.98 dBi @ 5 GHz) — per the IC filing table.
- Dedicated "Gaming ports" 1–2 with packet prioritization.
- Link Aggregation ports 5–6 (802.11ad/WDS style pairing — actually 802.3ad-style aggregation per wording "use link aggregation").
- USB 3.0 + USB 2.0 ports for storage / printer / 3G-4G modem.
- Triple-band: 2.4 GHz + 5 GHz-1 + 5 GHz-2, concurrent.
- Power: 19 V / 3.42 A.

### Quick Internet Setup (QIS) (§2.2)
- Web GUI auto-launches at `http://router.asus.com`; first login prompts for password.
- QIS auto-detects connection type. Default LAN: 192.168.1.1 / 255.255.255.0, DHCP on.

### ROG Gaming Center features (§3)
The headline differentiator. Six dedicated features:
- **[[../concepts/game-ips|Game IPS]]** — Trend Micro-powered network protection, malicious-site blocking, two-way IPS, infected-device prevention, parental controls (web/apps filter + time scheduling).
- **[[../concepts/game-boost|Game Boost]]** — One-click prioritization of gaming packets. Includes QoS (Adaptive / Traditional / Bandwidth limiter) and Web History.
- **[[../concepts/game-private-network|Game Private Network (GPN)]]** — WTFast integration to route game traffic through optimized GPN servers (free tier = 1 device).
- **[[../concepts/game-profile|Game Profile]]** — Curated port-forwarding presets for popular games; avoids NAT/port-block issues.
- **[[../concepts/game-radar|Game Radar]]** — Ping diagnostic against per-game server lists to pick the lowest-latency server.
- **[[../concepts/wifi-radar|WiFi Radar]]** — Wireless troubleshooting tool: site survey, channel statistics, advanced troubleshooting.

### Dashboard (§3.2)
- Real-time traffic chart and **worldwide game-server ping** view. Manual defines: ping < 99 ms = good, < 150 ms = acceptable, > 150 ms = hard to play smoothly. Lower ping deviation = better.

### Wireless (§4.2)
- Three radios configurable independently. Authentication options: Open / WPA-Personal / WPA2-Personal / WPA-Enterprise / WPA2-Enterprise / RADIUS/802.1x.
- **Important caveat**: 802.11n/ac prohibits HT with WEP or WPA-TKIP unicast cipher — throughput drops to 54 Mbps (802.11g).
- Guest network: up to **9 SSIDs** (3 × 2.4 GHz + 3 × 5 GHz-1 + 3 × 5 GHz-2).
- Bridge mode (WDS): AP Only / WDS Only / HYBRID. Hybrid mode caps clients at half the AP's speed.
- Professional settings include: AMPDU RTS, RTS threshold, DTIM, Beacon interval, TX Bursting, WMM APSD, USB 3.0 interference reduction, Turbo QAM (256-QAM on 2.4 GHz), Airtime Fairness, Explicit/Universal Beamforming, TX power (0–100).
- **Smart Connect** — automatic band steering across the 3 radios.

### LAN / WAN (§4.4–4.5)
- LAN IP, DHCP server (manual MAC-binding up to 32 addresses), static route, IPTV passthrough.
- WAN types: Automatic IP, PPPoE, PPTP, L2TP, Static IP. NAT, UPnP, DNS auto, MAC clone, DHCP query frequency.
- **Dual WAN**: Failover mode OR Load Balance mode.
- Port Trigger, Virtual Server/Port Forwarding (with famous game/server lists), DMZ, DDNS (`xxx.asuscomm.com`), NAT Passthrough (PPTP/L2TP/IPsec/RTSP — all enabled by default).
- Note: DDNS won't work on private WAN IPs (192.168.x.x, 10.x.x.x, 172.16.x.x).

### VPN (§3.9)
- Built-in **PPTP VPN server** with broadcast support, MPPE encryption, optional Samba support for clients.
- See [[../concepts/vpn]].

### USB Applications (§4.6)
- **AiDisk** — wizard for setting up FTP server + ASUS DDNS.
- **Servers Center** — DLNA Media Server, iTunes Server, Samba Share, FTP Share (anonymous login optional, max concurrent connections configurable).
- **3G/4G** — failover/dedicated WAN via USB modem (verify support at `http://event.asus.com/2009/networks/3gsupport/`).
- Filesystem support: FAT16, FAT32, NTFS, HFS+. Up to 4 TB.

### AiCloud 2.0 (§4.7)
- Mobile app (iOS/Android) for **Cloud Disk**, **Smart Access** (HTTPS via DDNS), and **Smart Sync** (sync to ASUS WebStorage).

### IPv6 (§4.8) and Firewall (§4.9)
- IPv6 connection types vary; ISP-provided.
- Firewall: General (DoS protection), URL filter, Keyword filter (DNS-query-based, doesn't catch already-cached sites or HTTPS), Network Services Filter (black/white list with schedule), IPv6 firewall.

### Smart Connect (§4.12)
- Automatic steering among 2.4 GHz / low-band 5 GHz / high-band 5 GHz. Tunables: Bandwidth Utilization threshold, Load Balance, RSSI trigger, PHY rate thresholds, VHT preference (All / AC only / Not-allowed), Target Band priority, Bounce Detect (Count / Window Time / Dwell Time).

### Administration (§4.10)
- **Operation modes**: Wireless Router (default) / Access Point / Media Bridge. Reboot required on change.
- System: change login password, time zone, NTP, Telnet toggle, HTTP/HTTPS auth, WAN-side web access (IP allowlist).
- Firmware upgrade (web); rescue mode + Firmware Restoration utility on failure.
- Restore/Save/Upload settings (factory restore via GUI).

### Utilities (§5)
- **Device Discovery** v1.4.7.1 — Windows utility to find router IP (needed when in AP mode).
- **Firmware Restoration** v1.9.0.4 — Rescue-mode firmware recovery. Set static IP `192.168.1.x / 255.255.255.0`, hold reset while powering on, Power LED flashes slowly.
- **Printer sharing**: EZ Printer Sharing (Windows XP/Vista/7 only) or LPR/LPD (cross-platform via Standard TCP/IP Port → queue name `LPRServer`).
- **Download Master** — BitTorrent / HTTP / FTP / NZB downloads to attached USB. Speed limits, peer limits, encryption toggles.

### Troubleshooting (§6)
- Factory defaults: user `admin` / pass `admin`, SSID `ASUS` (2.4 GHz) / `ASUS_5G` (5 GHz).
- Common fixes: upgrade firmware, restart network in order (modem → router → PCs), check Ethernet LEDs, clear DNS cache, disable proxy, set TCP/IP to DHCP.

### Regulatory / Notices (Appendix)
- FCC Part 15 Class B; FCC RF exposure: min 31 cm from radiator; **indoor use only**; US/CA: channels 1–11 only.
- IC RSS-102 (Canada), CE Mark Class B, NCC (Taiwan), AEEE (Turkey).
- GPLv2 — firmware includes GPL-licensed third-party code; ASUS publishes source with firmware updates.

## Caveats / Verification Notes

- **Wording oddity** (§1.3): Link Aggregation ports labelled "(5~6)" but the parenthetical says "use link aggregation (802.11ad)" — 802.11ad is 60 GHz WiGig (wrong here). The intended reference is 802.3ad link aggregation. [needs verification against ASUS specs page]
- **Firmware version**: Manual doesn't quote a firmware version. Features may vary by firmware, per §3.1 note.
- All sub-features reference QIS-set admin password; default `admin/admin` is also documented in §6.2 (factory reset).
