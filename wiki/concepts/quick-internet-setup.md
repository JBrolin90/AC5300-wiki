---
title: "Quick Internet Setup (QIS)"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
  - "[[../source-summary/gt-ac5300-pcmag-review]]"
related:
  - "[[rog-gaming-center]]"
  - "[[lan-wan]]"
created: 2025-07-16
updated: 2025-07-16
confidence: 0.95
---
# Quick Internet Setup (QIS)

## When it runs

- First browser visit to `http://router.asus.com` after a fresh setup or factory reset
- Subsequent logins go straight to the [[rog-gaming-center]] GUI (admin / `<QIS-set-password>`)

## Workflow

1. Plug in power; connect WAN cable from modem to the GT-AC5300's WAN port
2. (Wired) connect PC to a LAN port, or (Wireless) connect to the default SSID (`ASUS` / `ASUS_5G`)
3. Open a browser — auto-redirects to QIS
4. If no redirect, manually enter `http://router.asus.com`
5. QIS auto-detects connection type (DHCP, PPPoE, PPTP, L2TP, Static IP)
6. Set a **router admin password** (this becomes the GUI login — factory default after reset is `admin` / `admin`)
7. Configure SSID names + wireless security

## Factory defaults (per §6.2 of the manual)

| Field | Value |
|---|---|
| Login | admin / admin |
| LAN IP | 192.168.1.1 (a.k.a. router.asus.com) |
| Subnet | 255.255.255.0 |
| DHCP | Enabled (when WAN plugged in) |
| DNS 1 | 192.168.1.1 |
| SSID 2.4 GHz | ASUS |
| SSID 5 GHz | ASUS_5G |

## Notes

- Use a wired connection during setup to avoid Wi-Fi hiccups.
- If replacing an existing router, disconnect the old one first; reboot the cable modem.
- After QIS, the [[rog-gaming-center]] features (Game IPS, Game Boost, etc.) are accessible from `General` in the navigation panel.

## Operation-mode selector (PCMag review confirms)

The QIS first screen offers five modes (review-verified, set mid-2018 firmware):

- **Wireless Router** (default)
- **Repeater**
- **Access Point (AP)**
- **Media Bridge**
- **AiMesh** — see [[aimesh]]

Setup can take < 5 minutes on a fresh install (per reviewer's experience).
