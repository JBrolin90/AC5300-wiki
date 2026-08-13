---
title: "AiCloud 2.0"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
related:
  - "[[usb-applications]]"
  - "[[lan-wan#DDNS]]"
created: 2025-07-16
updated: 2025-07-16
confidence: 0.85
---
# AiCloud 2.0

## Setup

1. Install **ASUS AiCloud** from Google Play / Apple App Store
2. Connect phone to the router's network
3. Follow in-app prompts

## Cloud Disk

- Requires a USB storage device plugged into the router (see [[usb-applications]])
- Toggle **Cloud Disk** ON in the AiCloud panel
- Access at `https://router.asus.com` (use Chrome or Firefox per the manual) → log in with router account
- Note: AiCloud does **not save** device passwords — you re-enter them manually on each new client (security choice)

## Smart Access

HTTPS-by-domain for accessing your home network from outside. Requires an ASUS DDNS hostname (see [[lan-wan#DDNS]]).

`https://<yourASUSDDNSname>.asuscomm.com` → secure Cloud Disk + Smart Access.

## Smart Sync

Bidirectional sync between the router-attached USB and ASUS WebStorage.

1. `AiCloud → Smart Sync → Go`
2. Enable: ON
3. **Add new account** — ASUS WebStorage credentials
4. Pick the directory to sync
5. Apply
