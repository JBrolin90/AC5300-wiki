---
title: "Port Forwarding & Port Trigger"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
related:
  - "[[lan-wan]]"
  - "[[game-profile]]"
created: 2025-07-16
updated: 2025-07-16
confidence: 0.9
---
# Port Forwarding & Port Trigger

## Port Forwarding (Virtual Server)

`Advanced Settings → WAN → Virtual Server / Port Forwarding`

- **Enable**: Yes
- Pick a service type from the **Famous Server List** (HTTP, FTP, etc.)
- Optionally pick from the **Famous Game List** — same data [[game-profile]] uses
- For custom entries, the **Port Forwarding List** needs:

| Field | Notes |
|---|---|
| Service Name | Free-form |
| Port Range | Single port (`80`), range (`10200:10300`), or mixed (`1015:1024,3021`) |
| Local IP | LAN IP of the host (use a static IP!) |
| Local Port | Optional; leave blank to forward to the same Port Range |
| Protocol | TCP / UDP / BOTH (when unsure) |

- Click **Add**, then **Apply**

### Port range conflicts
> Port 80 in the WAN forward + router's own web UI = conflict. Same port can only be used by one service.

### Verifying it works
- Service running on the LAN host
- From a client **outside** the LAN (not behind this router), browse to the router's WAN IP. Success → you can access the service.

## Port Trigger

`Advanced Settings → WAN → Port Trigger`

Use when:
- Multiple LAN clients need port forwarding for the same application at different times
- The app uses different incoming vs. outgoing ports (e.g. IRC)

| Field | Value |
|---|---|
| Description | Short name |
| Trigger Port | Outgoing port that arms the rule |
| Protocol | TCP / UDP |
| Incoming Port | Port to open when triggered |
| Protocol | TCP / UDP |

> Manual caveat: Port triggering only allows one client on the network to use a particular service and incoming port at the same time. The router forwards to the **last** PC to send the trigger.

## Port Forwarding vs. Port Trigger

| Feature | Static? | LAN IP required? | Open always? | Multi-client safe? |
|---|---|---|---|---|
| Port Forwarding | Yes (until removed) | Yes (static) | Yes | Only with distinct ports per client |
| Port Trigger | No (transient) | No (dynamic) | No (only while trigger is active) | One at a time |

**Security**: Port Trigger is more secure because ports are closed when not in use.

## See also

- [[game-profile]] — built-in game presets that create port-forwarding entries.
- [[lan-wan#DMZ]] — full-host exposure (use with caution).
