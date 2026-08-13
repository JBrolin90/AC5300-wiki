---
title: "USB Applications"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
related:
  - "[[aicloud]]"
  - "[[lan-wan]]"
created: 2025-07-16
updated: 2026-08-13
confidence: 0.9
---
# USB Applications

## Supported devices

- USB HDDs / flash drives up to **4 TB**
- Filesystems: **FAT16, FAT32, NTFS, HFS+** (read-write)
- USB printer (one printer + one drive, OR two drives)
- 3G/4G USB modem (verify support at `http://event.asus.com/2009/networks/3gsupport/`)

## AiDisk

`Advanced Settings → USB application → AiDisk`

1. Click **Go** in the AiDisk wizard
2. Pick access rights (admin / user / limited)
3. Configure ASUS DDNS (`xxx.asuscomm.com`) — or **Skip**
4. Finish
5. Access via `ftp://<domain>.asuscomm.com`

## Servers Center

`Advanced Settings → USB application → Media Services and Servers`

### Media Server
- iTunes Server toggle
- DLNA Media Server toggle
- Status display
- Path: All Disks Shared **or** Manual path

### Samba (Network Place) Share
Default-enabled. Add accounts (name + password), add folders, set per-folder permission: **R/W / R / No**.

### FTP Share
- Assumes AiDisk already created the FTP server
- Per-folder rights: **R/W / W / R / No**
- Optional anonymous login (ON/OFF)
- **Max concurrent connections** field

## Safely removing the USB disk

`General → Network Map` → upper-right `>` → **Eject USB disk**. Status becomes "Unmounted" when safe. **Don't just unplug** — risk of data corruption.

## USB 3.0 / 2.0 mode switch (later addition)

Added in firmware `3.0.0.4.384.32738` (2018-08-21) per the [ASUS support page release note](../source-summary/gt-ac5300-firmware-history). A toggle in `Administration → System → USB Settings` that lets you force the USB-3.0 port into USB-2.0 mode.

- Useful if a USB-3.0 device or cable is causing 2.4 GHz Wi-Fi interference (a known issue with USB 3.0's 2.4 GHz noise spectrum).
- Also documented in the manual under Professional settings for wireless: "USB 3.0 interference reduction".

## 3G/4G

`Advanced Settings → USB application → 3G/4G`

| Field | Value |
|---|---|
| Enable USB Modem | Yes |
| Location | ISP's country |
| ISP | Provider name |
| APN | (optional, from provider) |
| Dial Number | Access number |
| PIN code | From provider |
| Username / Password | From provider |
| USB Adapter | Specific model or **Auto** |

> After Apply, **the router reboots**.

## Printer Server

See [[utilities#Printer Server (EZ + LPR)]].
