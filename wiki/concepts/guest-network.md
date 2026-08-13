---
title: "Guest Network"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
related:
  - "[[wireless-settings]]"
created: 2025-07-16
updated: 2025-07-16
confidence: 0.9
---
# Guest Network

## Capacity

| Band | Guest SSIDs |
|---|---|
| 2.4 GHz | 3 |
| 5 GHz-1 | 3 |
| 5 GHz-2 | 3 |
| **Total** | **9** |

## Setup

`Advanced Settings → Guest Network`

1. Pick the frequency band (2.4 GHz or 5 GHz)
2. Click **Enable**
3. Configure each guest profile:
   - Network Name (SSID)
   - Authentication Method (Open / WPA-Personal / WPA2-Personal)
   - WPA Encryption (TKIP / AES) — when WPA is selected
   - **Access time**: Limitless or a scheduled window
   - **Access Intranet**: Enable / Disable (Disable = Internet only)
4. **Apply**

## Behavior

- **Disable** on Access Intranet is the standard guest setup: clients reach the Internet but cannot see or reach the private LAN.
- Limit Access time to e.g. "9am–6pm" for short-term visitors.
- Use [[wireless-settings#Professional|Professional → Set AP isolated]] in addition if you want guest SSIDs on the same radio to be isolated from each other.
