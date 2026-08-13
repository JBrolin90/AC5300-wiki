---
title: "Utilities"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
related:
  - "[[administration]]"
  - "[[usb-applications]]"
created: 2025-07-16
updated: 2025-07-16
confidence: 0.9
---
# Utilities

> **All utilities are Windows-only.** macOS is not supported.

## Downloads (per the manual)

| Utility | Version | URL |
|---|---|---|
| Device Discovery | 1.4.7.1 | `http://dlcdnet.asus.com/pub/ASUS/LiveUpdate/Release/Wireless/Discovery.zip` |
| Firmware Restoration | 1.9.0.4 | `http://dlcdnet.asus.com/pub/ASUS/LiveUpdate/Release/Wireless/Rescue.zip` |
| Windows Printer Utility | 1.0.5.5 | `http://dlcdnet.asus.com/pub/ASUS/LiveUpdate/Release/Wireless/Printer.zip` |

## Device Discovery

Detects ASUS wireless routers on the local network and lets you configure wireless settings. **Required when the router is in [[administration#Operation Mode|Access Point mode]]** — since in AP mode you can't assume `router.asus.com` resolves.

Launch: `Start → All Programs → ASUS Utility → GT-AC5300 Wireless Router → Device Discovery`.

## Firmware Restoration

Used after a failed firmware upgrade. **Launch rescue mode on the router first:**

1. Unplug the router from power
2. Hold the **Reset** button (rear panel)
3. Replug the router **while still holding Reset**
4. Release Reset when the **Power LED flashes slowly** → rescue mode

Then on the PC:
1. Set static IP: `192.168.1.x` / `255.255.255.0`
2. Run Firmware Restoration
3. Pick the firmware file → **Upload** (takes ~3–4 minutes)

> This is **not** a normal firmware upgrade. Do not run on a working router — use the web UI's [[administration#Firmware Upgrade]].

## Printer Server

Two modes:

### EZ Printer Sharing (Windows XP / Vista / 7 only)

1. `Advanced Settings → USB Application → Network Printer Server`
2. Click **Download Now!** → unzip → run the Printer icon
3. Follow wizard (hardware setup → wait for initial setup → finish)
4. Install printer driver via Windows UI
5. Network clients can now print

### LPR (cross-platform: Windows + macOS)

LPR/LPD = Line Printer Remote / Line Printer Daemon.

On Windows:
1. `Start → Devices and Printers → Add a printer`
2. **Add a local printer**
3. **Create a new port** → Type: **Standard TCP/IP Port**
4. Hostname/IP: the **router's IP**
5. **Custom** → **Settings** → Protocol: **LPR** → Queue Name: **`LPRServer`**
6. Install driver from vendor list (or Have Disk)
7. Finish

On macOS, use the LPR option in System Preferences → Printers.

## Download Master

`General → USB application → Download Master`. Downloads continue even when client PCs are off.

- Install utility (auto via the menu item)
- Pick the USB drive if multiple
- **Add** → choose type: BitTorrent / HTTP / FTP / NZB
- Provide a `.torrent` file or URL
- BitTorrent settings: dedicated port, speed limits (up/down), peer limits, encryption toggle
- NZB: enter USENET server settings → Apply
