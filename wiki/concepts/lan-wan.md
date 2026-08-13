---
title: "LAN / WAN"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
  - "[[../source-summary/gt-ac5300-manual-figures]]"
related:
  - "[[port-forwarding-and-trigger]]"
  - "[[firewall]]"
created: 2025-07-16
updated: 2026-08-13
confidence: 0.9
---
# LAN / WAN

![LAN → DHCP Server tab — manual p. 66 (Basic Config, IP Pool, manual-assignment table)](../../assets/figures/manual-p066-220-lan-dhcp-server.png)

*Figure: LAN → DHCP Server tab — manual p. 66. Shows Basic Config (Enable toggle, Domain Name, IP Pool start/end, Lease Time, Default Gateway) and the per-client manual-assignment table.*

## LAN

`Advanced Settings → LAN`

### LAN IP
- Modify IP address and Subnet Mask. **Any change is reflected in DHCP settings.**

### DHCP Server
- Enable: Yes/No
- Domain name
- IP Pool: Starting and Ending addresses (manual range or up to 32 MAC-bound static assignments)
- Lease time (seconds)
- DNS / WINS servers (optional)
- Manual assignment: Yes/No; up to 32 MACs

> Manual recommends `192.168.1.xxx` (xxx in 2–254) for the IP pool. Starting ≤ Ending.

### Route
- Static route table for multi-router networks. Manual says: don't touch defaults unless you know routing.

### IPTV
- IPTV / VoIP / multicast / UDP settings. Specifics from ISP.

## WAN

`Advanced Settings → WAN`

### Internet Connection
- **Type**: Automatic IP / PPPoE / PPTP / L2TP / Static IP
- Enable WAN: Yes/No
- **Enable NAT** (default on): maps private LAN IPs to one public WAN IP
- **Enable UPnP**: auto-port-forwarding for compatible apps/games (vs. manual Port Forwarding)
- **Connect to DNS Server automatically**
- Authentication, Host Name, MAC Address (clone from previous device if ISP locks to MAC), DHCP query frequency

### Dual WAN
Two modes when a second WAN source is attached (e.g. secondary ISP or 3G/4G modem):

| Mode | Behavior |
|---|---|
| Failover | Secondary WAN is backup; takes over when primary fails |
| Load Balance | Both WANs share traffic; optimizes throughput, minimizes response time |

### Port Trigger
Dynamically opens an incoming port for a limited window when a LAN client makes an outgoing connection on a trigger port. Good for one-to-many (e.g. multiple PCs using the same game at different times).

### Virtual Server / Port Forwarding
Statically maps an external port to a LAN client's IP/port. Use the **Famous Server List** / **Famous Game List** for presets. See [[port-forwarding-and-trigger]].

### DMZ
Exposes one LAN client to the Internet; that client receives all inbound packets. Useful for hosting a domain/web/email server. **Security risk** — only one host should be in the DMZ.

### DDNS
Dynamic DNS via ASUS DDNS (host format `xxx.asuscomm.com`) or another DDNS provider. Required for [[aicloud|Smart Access]] and the [[../source-summary/gt-ac5300-manual|FTP link from AiDisk]].

> DDNS won't work when WAN IP is private (192.168.x.x, 10.x.x.x, 172.16.x.x).

### NAT Passthrough
Default ON: PPTP, L2TP, IPsec, RTSP. Toggles on `Advanced Settings → WAN → NAT Passthrough`.
