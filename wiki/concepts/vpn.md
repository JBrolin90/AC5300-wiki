---
title: "VPN"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-manual]]"
  - "[[../source-summary/gt-ac5300-manual-figures]]"
  - "[[../source-summary/gt-ac5300-pcmag-review]]"
related:
  - "[[lan-wan#NAT Passthrough]]"
  - "[[vpn-fusion]]"
created: 2025-07-16
updated: 2026-08-13
confidence: 0.85
---
# VPN

![PPTP VPN Server config — manual p. 43 (Enable toggle, Advanced Settings, Network Place support, client setup guide, Username/Password table)](../../assets/figures/manual-p043-166-vpn-server-pptp.png)

*Figure: PPTP VPN Server config — manual p. 43. Shows the Enable toggle, Advanced Settings dropdown, Network Place (Samba) support toggle, the 7-step client setup guide, and the Username / Password table editor.*

## Server mode

`General → VPN`

1. **Enable PPTP VPN Server**: ON
2. (Optional) **Advanced Settings** dropdown to configure:
   - Broadcast support
   - Authentication
   - MPPE Encryption
   - Client IP address range
3. **Network Place (Samba) Support**: Yes → VPN clients can also access Samba shares
4. Add username + password; click add
5. Apply

## Client mode (pass-through)

[[lan-wan#NAT Passthrough|NAT Passthrough]] handles inbound VPN sessions from LAN clients to an external VPN server:
- **PPTP Passthrough** — default ON
- **L2TP Passthrough** — default ON
- **IPsec Passthrough** — default ON
- **RTSP Passthrough** — default ON

Toggle under `Advanced Settings → WAN → NAT Passthrough`.

## Caveats

- Only PPTP is supported as a server (per the manual). For OpenVPN/WireGuard you'd need newer firmware or different firmware (e.g. Merlin) — [needs verification].
- MPPE encryption requires clients that support it.

## Related firmware feature

- [[vpn-fusion]] — newer firmware feature that lets the router run a VPN **client** alongside the normal WAN, so game traffic can bypass the VPN. Distinct from the PPTP **server** covered above.
