---
title: "Smart Connect"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
related:
  - "[[wireless-settings]]"
created: 2025-07-16
updated: 2025-07-16
confidence: 0.85
---
# Smart Connect

## Enabling

Two ways:
1. `Advanced Settings → Wireless → General → Enable Smart Connect: ON`
2. `Advanced Settings → Smart Connect`

The single SSID is shared across all three radios; the router steers clients to the best band.

## Smart Connect Rule

`Advanced Settings → Smart Connect → Smart Connect Rule` (or `Network Tools → Smart Connect Rule` per the manual's wording). Four sections of controls:

### 1. Steering Trigger Condition
When does steering kick in?
| Control | What it does |
|---|---|
| **Bandwidth Utilization** | When utilization exceeds this %, steering starts. (How utilization is measured isn't documented.) |
| **Enable Load Balance** | Toggles load balancing across radios (mechanism unspecified in the manual). |
| **RSSI** | When a client's signal strength meets this threshold, steering is triggered. |
| **PHY Rate Less / PHY Rate Greater** | STA link-rate thresholds that trigger steering. |
| **VHT** | `ALL` (any client triggers), `AC only` (only 802.11ac), `Not-allowed` (only non-ac → 802.11a/b/g/n). |

### 2. STA Selection Policy
Once steering triggers, which client (STA) gets steered?

### 3. Interface Select and Qualify Procedures
Where does the steered client land?
- **Target Band** controls specify first and second choice
- Steered client goes to the first target if its Bandwidth Utilization < set value; otherwise to the second target

### 4. Bounce Detect
Prevents clients from being ping-ponged:
- Each client can be steered **N Counts** within a **Window Time**
- After Count is hit, the client is locked to its current band for **Dwell Time**
- Does NOT count disconnects the client initiates on its own

## When to leave defaults

Unless you have a specific Wi-Fi layout problem (e.g. legacy clients on 5 GHz slowing the rest of the band), leave these at defaults. The manual itself notes the controls reference Broadcom's documentation, which isn't included.

## See also

- [[wifi-radar]] for diagnosing wireless issues — useful before/after enabling Smart Connect.
