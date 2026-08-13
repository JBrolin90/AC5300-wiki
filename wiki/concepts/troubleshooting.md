---
title: "Troubleshooting"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
related:
  - "[[administration]]"
  - "[[utilities]]"
created: 2025-07-16
updated: 2025-07-16
confidence: 0.85
---
# Troubleshooting

## Basic Troubleshooting (§6.1)

Try these in order:

### 1. Upgrade firmware to latest
1. Web GUI → `Advanced Settings → Administration → Firmware Upgrade → Check`
2. If newer is available, download from `http://www.asus.com/Networks/Wireless_Routers/RTAC5300/#download`
3. **Browse** → pick the file → **Upload**

### 2. Restart network in this order
1. Modem off
2. Unplug modem
3. Router + computers off
4. Plug in modem
5. Modem on, wait 2 min
6. Router on, wait 2 min
7. Computers on

### 3. Check Ethernet cables
- WAN LED on = cable to modem is good
- LAN LED on = cable to that PC is good

### 4. Check wireless settings on the PC
SSID, encryption method, password — all must match the router.

### 5. Check network settings
- Each client needs a valid IP (use the router's DHCP)
- Some ISPs lock service to the originally registered MAC — find the client MAC via `Network Map → Clients`, hover for status.

## FAQ (§6.2)

### Can't access router GUI via browser
- Check wired connection + LEDs (above)
- Login is **admin / admin** (factory) or **admin / `<QIS password>`**
- Caps Lock off
- Clear cookies + temporary internet files
- Disable proxy server, cancel dial-up, set TCP/IP to obtain IP automatically
- Use **CAT5e or CAT6** cables

### Client can't connect wirelessly
- For 5 GHz issues: confirm the wireless device supports 5 GHz (or is dual-band)
- **Out of range**: move router closer / adjust antennas per [[placement#Antenna orientation]]
- **DHCP disabled**: enable it under `Advanced Settings → LAN → DHCP Server`
- **SSID hidden**: unhide under `Wireless → General`
- **Channel mismatch** (regulatory): adjust channel / bandwidth / wireless mode
- **Last resort**: factory reset (`Administration → Restore/Save/Upload Setting → Restore`)

### Internet not accessible
- Web GUI → `Advanced Settings → Network Map` → check **Internet Status**
- If WAN IP unreachable, restart network (above)
- **Parental Control block**: `General → Parental Control` → remove the device from the list / adjust schedule
- If still nothing: reboot PC, verify IP + gateway
- Check modem + router LEDs

### Forgot SSID / password
- Wired: Web GUI → Network Map → router icon → new SSID + key → Apply
- Or factory reset (`admin/admin`)

### Restore to defaults
- `Administration → Restore/Save/Upload Setting → Restore`

Factory defaults (per §6.2):

| Field | Value |
|---|---|
| User | admin |
| Password | admin |
| DHCP | Yes (if WAN plugged in) |
| IP | http://router.asus.com (or 192.168.1.1) |
| Subnet | 255.255.255.0 |
| DNS 1 | 192.168.1.1 |
| SSID 2.4 GHz | ASUS |
| SSID 5 GHz | ASUS_5G |

### Firmware upgrade failed
- Rescue mode + [[utilities#Firmware Restoration]] (Firmware Restoration utility 1.9.0.4)

## Before configuring (Web GUI prep)

For clients having persistent trouble reaching the GUI:

### A. Disable proxy
- **Windows 7**: IE → Tools → Internet Options → Connections → LAN Settings → uncheck "Use a proxy server"
- **macOS**: Safari → Preferences → Advanced → Change Settings → uncheck FTP / Web Proxy

### B. TCP/IP set to DHCP
- **Windows 7**: Network Sharing Center → Manage network connections → IPv4 / IPv6 Properties → "Obtain an IP address automatically"
- **macOS**: System Preferences → Network → Configure → TCP/IP → "Using DHCP"

### C. Disable dial-up
- **Windows 7**: IE → Tools → Internet Options → Connections → "Never dial a connection"
