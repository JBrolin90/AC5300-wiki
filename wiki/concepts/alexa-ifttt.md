---
title: "Alexa + IFTTT integration"
type: concept
sources:
  - "[[../source-summary/gt-ac5300-pcmag-review]]"
  - "[[../source-summary/gt-ac5300-firmware-history]]"
  - "https://www.snbforums.com/threads/is-there-any-news-of-ifttt-compliance-in-asus-merlin-firmware-for-rt-68u.40525/"
  - "https://rog-forum.asus.com/t5/gaming-routers/rog-rapture-gt-ac5300-firmware-3-0-0-4-384-20308-with-aimesh-and/td-p/758225"
  - "https://www.amazon.com/ASUS-ROUTER/dp/B07285G1RK"
related:
  - "[[rog-gaming-center]]"
created: 2025-07-16
updated: 2025-07-16
confidence: 0.85
---
# Alexa + IFTTT integration

## Alexa voice commands (per PCMag review)

| Trigger | Effect |
|---|---|
| "Alexa, turn on the guest network" | enables guest SSID |
| Update the firmware | runs an OTA firmware check/update |
| Pause the internet | blocks WAN traffic — useful for dinner / bedtime |

## IFTTT applets (per PCMag review)

Examples given in the review:

- Turn off Wi-Fi at sunset / at bedtime.
- Turn on Wi-Fi when arriving home.
- Send an email when a child logs in to the network.
- React to events from other IFTTT devices (door locks, cameras).

## Where it sits in the GUI

Lives under Advanced settings per the review (not the General tab). [needs verification — exact path not in the review or manual]

## Notes

- Requires the Alexa skill "**Asus Router**" or "**Router**" to be enabled in the Alexa app, and an ASUS account linked to the router.
- Requires an IFTTT account and the "**ASUS Router**" service enabled in IFTTT.
- These services route voice/IFTTT commands through Asus cloud (and through Amazon/IFTTT respectively) — not direct LAN control.

## Firmware introduction (confirmed)

- **First appearance (original Alexa skill + IFTTT service)**: introduced on the `3.0.0.4.382` code branch in **2017**. Per RMerlin (Merlin-developer) on SNBForums, "Alexa and IFTTT is currently only available on the 382 code branch, used by the GT-AC5300 and RT-AC86U" — meaning it was added to the 382 branch and not backported to 380/384 of other models. A Chinese CSDN modding-thread note for `3.0.0.4.382.15984` refers to disabling the Alexa part ("Alexa features unavailable to China users") in that build, narrowing the first-appearance window to between June and late August 2017.
- **New Alexa skills + IFTTT actions** ("Ask ASUS ROUTER to report security status"; "how many devices are online"; IFTTT: Wake on LAN, "check new firmware available and upgrade"): added in firmware **`3.0.0.4.384_45149` (2018-12-05)**. Verbatim release note: "You have to upgrade the firmware version up to 3.0.0.4.384_45149 if you want to use these new Alexa skills and IFTTT actions."

## Open verification

- Exact GUI path (under Advanced Settings per the review).
- The current live status of the Alexa skill and IFTTT service — the user's data and the Alexa/IFTTT websites change over time, so an end-of-2025 or later re-check is warranted.
