---
title: "Administration"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
related:
  - "[[quick-internet-setup]]"
  - "[[utilities#Firmware Restoration]]"
created: 2025-07-16
updated: 2025-07-16
confidence: 0.9
---
# Administration

## Operation Mode

`Advanced Settings → Administration → Operation Mode`

| Mode | Behavior |
|---|---|
| **Wireless Router** (default) | Standard NAT router with its own LAN; provides Internet to clients |
| **Access Point** | Creates a new wireless network on top of an existing wired network — note: in this mode you need [[utilities#Device Discovery]] to find the router's IP |
| **Media Bridge** | Two-router setup; this router bridges multiple ethernet devices (Smart TVs, consoles) onto the wireless network |

> Router **reboots** on mode change.

## System

`Advanced Settings → Administration → System`

- Change router login password (and optionally login name)
- Time Zone
- NTP Server (syncs system time — required by [[game-ips#Parental Control — Time Scheduling]])
- Enable Telnet: Yes/No
- Authentication Method: HTTP / HTTPS / both
- **Enable Web Access from WAN**: Yes/No
- **Allow only specified IP address**: Yes/No (locks WAN-side GUI to a Client List)

## Firmware Upgrade

`Advanced Settings → Administration → Firmware Upgrade`

- Download latest firmware from `http://www.asus.com`
- Click **Browse** → select the file → **Upload**
- Router reboots when done
- On upgrade failure, the router enters rescue mode (Power LED flashes slowly) — use [[utilities#Firmware Restoration]]

## Restore / Save / Upload Setting

`Advanced Settings → Administration → Restore/Save/Upload Setting`

- **Restore**: factory defaults (admin/admin, ASUS/ASUS_5G SSIDs)
- **Save**: download current settings to a file
- **Upload**: restore from a saved file

> If issues occur after a partial restore, the manual recommends uploading the latest firmware and reconfiguring — **do not** restore factory defaults as a first step.
