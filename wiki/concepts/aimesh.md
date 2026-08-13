---
title: "AiMesh"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-pcmag-review]]"
  - "[[../source-summary/gt-ac5300-firmware-history]]"
  - "https://www.snbforums.com/threads/aimesh-for-tri-band-routers-rt-ac5300-gt-ac5300.44023/"
related:
  - "[[quick-internet-setup]]"
  - "[[rog-gaming-center]]"
created: 2025-07-16
updated: 2026-08-13
confidence: 0.9
---
# AiMesh

## What it does

In AiMesh mode, the GT-AC5300 routes and runs the ROG Gaming Center as usual, but other Asus routers on the LAN can join as **nodes** that extend Wi-Fi coverage seamlessly (single SSID, client roaming between nodes).

Per PCMag:

> "AiMesh mode... lets you use other Asus routers as nodes to create a seamless mesh network."

## Operation modes confirmed for this router

| Mode | Purpose |
|---|---|
| Wireless Router | default, full router mode |
| Repeater | wireless range extension behind existing router |
| AP (Access Point) | bridge to existing router, no NAT/routing |
| Media Bridge | wireless client mode for devices that need ethernet |
| **AiMesh** | mesh controller, other Asus routers as nodes |

(Source: [[quick-internet-setup]] QIS mode selector; AiMesh confirmed in the PCMag review.)

## Notes

- Picking AiMesh in the setup wizard means choosing this unit as the **controller** — peer Asus routers then have to be added as nodes via their own firmware (`Administration → AiMesh Node`).
- Not in the May-2017 manual. Added in firmware `3.0.0.4.384.20287` on 2018-01-26. See "Firmware introduction" below.

## Firmware introduction (per ASUS release notes + forum confirmation)

- **AiMesh v1** (the "an innovative new router feature..." announcement): added in firmware **`3.0.0.4.384.20287` (2018-01-26)**. Confirmed by SNBForums "AiMesh for Tri-band routers: RT-AC5300, GT-AC5300" thread.
- **AiMesh v1.5 / mid-cycle additions** (2018-08-21, firmware **`3.0.0.4.384.32738`**): added three things that ship under "AiMesh v1" but are post-launch improvements — see [v1.5 additions](#aimesh-v15-additions) below.
- **AiMesh v2** (ethernet backhaul, client-binding per AP, guest WiFi on all nodes, USB-from-nodes, blue-cave-into-AC5300 support): added in firmware **`3.0.0.4.386.41793` (2021-01-26)** per the ASUS support page release notes (last fetched 2026-08-13). See [[../source-summary/gt-ac5300-firmware-history]].
- **Lyra-series nodes** can be added to a GT-AC5300 router in firmware **`3.0.0.4.384.45149` (2018-12-05)** per the same release line.

## AiMesh v1.5 additions

Confirmed from the ASUS release note for `3.0.0.4.384.32738` (2018-08-21) per the [2026-08-13 re-fetch of the ASUS support page](../source-summary/gt-ac5300-firmware-history). Three things that are part of the AiMesh v1 era but were added months after launch:

| # | Addition | Practical effect |
|---|----------|-----------------|
| 1 | **BlueCave as a node** | The non-ROG ASUS BlueCave router can be added to a GT-AC5300 mesh as a node. (v1 at launch supported only ASUSWRT-based routers.) |
| 2 | **Roaming block list** (`Advanced Settings → Wireless`) | Add a device MAC to the list and that device will not be roamed between AiMesh nodes. Equivalent to v2's "client device binding to a specific AP" but expressed as a denial rather than a binding — useful for IoT devices that misbehave when handed off. |
| 3 | **Ethernet onboarding** | Connect the AiMesh router's LAN port to the node's WAN port via Ethernet *before* running the add-node process, instead of relying on wireless pairing. Makes initial setup more reliable when the router and node are in the same room, and lets you build a wired backhaul from day one (predates the v2 "ethernet backhaul mode"). |

The same firmware also fixed a Smart-Connect-vs-AiMesh-onboarding bug (where enabling Smart Connect on the controller could prevent node pairing — fixed in `3.0.0.4.384.21140`, 2018-07-10).

## AiMesh v2 vs v1 — what changed

Released in firmware `3.0.0.4.386.41793` (2021-01-26) per the ASUS release note. The concrete improvements over v1 on the GT-AC5300:

| # | Improvement | Practical effect |
|---|-------------|-----------------|
| 1 | **Ethernet backhaul mode** | Nodes can be wired together via Ethernet so every radio on every node is available for client traffic. In v1, one of the radios (typically 5 GHz-2 on tri-band nodes) had to be dedicated to inter-node traffic, halving the per-client throughput available from a node. This is the headline improvement on a tri-band router like the GT-AC5300. |
| 2 | **One-click topology optimization** | A UI button to recompute which node each client connects to, instead of v1's "connect to whoever you heard first" behaviour. |
| 3 | **Client device binding to a specific AP** | Pin a device (e.g. a stationary printer, or a stubborn device with bad roaming logic) to a specific node. |
| 4 | **Client device reconnect** | Forcefully bounce a client (offline → online) to push it to a better node. Useful when a device's own roaming logic is broken. |
| 5 | **Guest WiFi on every mesh node** | The guest SSID broadcasts from every node, not just the router. An IoT device attaching to a back-room node lands on the guest VLAN. |
| 6 | **USB application access from nodes** | USB storage (or other USB apps) attached to the router is reachable when the client is connected to a downstream node. In v1 only wired / router-banded clients could reach the USB share. |
| 7 | **New "Family" interface in the ASUS Router app** | Mobile-app UI rebuild tied to v2 — simplified per-client management across the mesh. |
| 8 | **Blue Cave support as a node** | The (non-ROG) Blue Cave router can join a GT-AC5300 mesh as a node. |

Same release added system factory-default and reboot actions to the AiMesh page.

**Sources**: ASUS release note for `3.0.0.4.386.41793` (verbatim on [https://www.asus.com/supportonly/gt-ac5300/helpdesk_bios/](https://www.asus.com/supportonly/gt-ac5300/helpdesk_bios/)); ASUS FAQ 1044184 ("Connection priority and Ethernet backhaul mode introduction") and FAQ 1044151 ("How to setup ASUS AiMesh or ZenWiFi Mesh Ethernet backhaul under different conditions"), referenced by the same release note.

## Open verification

- Compatible node models (anything ASUSWRT/AiMesh-capable, but specific list undetermined).
- Which exact 3.0.0.4.382.xxxxx beta (pre-AiMesh-official) included AiMesh on the GT-AC5300 — the 3.0.0.4.384.20287 release *was* the first official build, but private betas likely existed.
