---
title: "Wireless Settings"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
  - "[[../source-summary/gt-ac5300-manual-figures]]"
related:
  - "[[wifi-radar]]"
  - "[[guest-network]]"
  - "[[smart-connect]]"
created: 2025-07-16
updated: 2026-08-13
confidence: 0.9
---
# Wireless Settings

![Wireless → Bridge mode — manual p. 55 (2.4 GHz MAC entry, AP Mode selector, Connect to APs in list toggle)](../../assets/figures/manual-p055-193-wireless-bridge-mode.png)

*Figure: Wireless → Bridge mode — manual p. 55. Shows the 2.4 GHz MAC entry, AP Mode selector (AP Only), and the "Connect to APs in list" toggle.*

## General

`Advanced Settings → Wireless → General`

- Frequency: 2.4 GHz or 5 GHz (one setting at a time)
- **Smart Connect** toggle: routes clients across all 3 radios automatically — see [[smart-connect]]
- SSID: up to 32 chars, unique per band
- **Hide SSID**: Yes/No
- Wireless mode: Auto (a/b/g/n/ac) / N only / Legacy (b/g/n, N clients capped at 54 Mbps)
- Control Channel: Auto (recommended) or fixed; channel availability varies by region
- Channel bandwidth: 20 / 40 / 80 MHz
- Authentication method: Open / WPA-Personal / WPA2-Personal / WPA-Enterprise / WPA2-Enterprise / RADIUS with 802.1x

> **Manual warning (§4.1.1)**: 802.11n/ac prohibits HT (High Throughput) with WEP or WPA-TKIP unicast cipher. Your data rate will drop to 802.11g 54 Mbps.

## WPS

`Advanced Settings → Wireless → WPS`

- Default uses 2.4 GHz; switch frequency via the **Switch Frequency** control
- Two methods: **Push Button** (physical WPS button on the router) or **Client PIN**
- WPS supports Open / WPA-Personal / WPA2-Personal only — not WPA-Enterprise, RADIUS, or Shared Key

## Bridge (WDS)

`Advanced Settings → Wireless → Bridge` (WDS = Wireless Distribution System)

| AP Mode | Behavior |
|---|---|
| AP Only | Wireless Bridge disabled |
| WDS Only | Bridge active; no regular clients |
| HYBRID | Bridge + regular clients; clients get half the AP's speed |

Add remote APs by MAC in the Remote AP List. All APs in the bridge must share the same control channel.

## Wireless MAC Filter

`Advanced Settings → Wireless → Wireless MAC Filter`. Modes: **Accept** (allow only listed) / **Reject** (block listed).

## RADIUS Setting

For WPA-Enterprise / WPA2-Enterprise / 802.1x. Configures: server IP, server port, connection secret.

## Professional

`Advanced Settings → Wireless → Professional`. **Manual recommends keeping defaults.** Notable knobs:

| Setting | Effect |
|---|---|
| Enable Radio / Date to Enable Radio / Time of Day to Enable Radio | Schedule radio on/off (per weekday/weekend) |
| Set AP isolated | Block wireless client-to-client traffic (useful for guest-heavy networks) |
| Roaming Assistant | Disconnect clients below a signal threshold so they roam to a stronger AP |
| IGMP Snooping | Optimize multicast over wireless |
| Multicast rate | Fixed Mbps rate for multicast, or Disable |
| Preamble Type | Short (busy networks) vs Long (legacy devices) |
| AMPDU RTS | Group frames; use RTS for each AMPDU between g/b devices |
| RTS Threshold | Lower = better in busy/noisy networks |
| DTIM Interval / Beacon Interval | Sleep-mode delivery timing; default 3 ms / 100 ms |
| Enable TX Bursting | Faster transmit to 802.11g devices |
| Enable WMM APSD | Wi-Fi Multimedia power-save delivery |
| Reducing USB 3.0 interference | Trades USB 3.0 throughput for cleaner 2.4 GHz Wi-Fi |
| Optimize AMPDU aggregation | Max MPDUs per AMPDU on error-prone channels |
| Optimize ack suppression | Max acks to suppress in a row |
| Turbo QAM (256-QAM) | Enable on 2.4 GHz for MCS 8/9 → better range/throughput |
| Airtime Fairness | Allocate equal airtime per client (slowest client no longer bottlenecks) |
| Explicit Beamforming | If both client and router support 802.11ac beamforming |
| Universal Beamforming | Beamforming for legacy clients |
| TX Power adjustment | 0–100 mW |

> **Caveat (§4.2.6)**: "Increasing the TX Power adjustment values may affect the stability of the wireless network."
