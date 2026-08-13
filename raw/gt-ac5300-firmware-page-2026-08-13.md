# GT-AC5300 firmware entries — extracted from ASUS support page

Source: <https://www.asus.com/supportonly/gt-ac5300/helpdesk_bios/>
Retrieved: 2026-08-13

Total entries: **23** (newest first).

## 3.0.0.4.386_51582  (2025/03/12)

- **Title**: (not given)
- **Size**: 69.65 MB
- **Release notes**:

  This model was end of its life, and its firmware, utility, website, and manual will no longer be updated. For more details, please refer to https://www.asus.com/event/network/eol-product/
  1.Fixed the UI issue in Chrome.
  2.Enhanced input parameter handling techniques to improve data processing stability and system security.
  3.Enhance system access control mechanisms.

## 3.0.0.4.386_51569  (2024/11/12)

- **Title**: (not given)
- **Size**: 69.74 MB
- **Release notes**:

  Please unzip the firmware file, and then verify the checksum.
  SHA256: 06f4be976520a833c05bcaa569602f615ca05d50cceed71059ed7893c3bb8c0b
  1. Strengthened input validation and data processing workflows to further protect information security.
  2. Enhanced AiCloud password protection mechanisms, safeguarding against unauthorized access attempts.
  3. Enhanced device security through improved buffer handling in connection features.
  4. Refined data handling processes, ensuring secure and accurate information management.
  5. Enhanced file access control mechanisms, promoting a more secure operating environment.
  6. Strengthened certificate protection, providing enhanced data security.

## 3.0.0.4.386_51529  (2023/11/27)

- **Title**: (not given)
- **Size**: 69.2 MB
- **Release notes**:

  Security updates:
  -Fixed DoS vulnerabilities in firewall configuration pages.
  -Fixed DoS vulerabilities in httpd.
  -Fixed information disclosure vulnerability.
  -Fixed CVE-2023-28702 and CVE-2023-28703.
  -Fixed null pointer dereference vulnerabilities.
  Please unzip the firmware file, and then verify the checksum.
  SHA256: bbb0e96c4d62e26992b41eafb6c490e0a72225a41f3997ffb72c3e5dc23c22ae

## 3.0.0.4.386.48377  (2022/03/30)

- **Title**: (not given)
- **Size**: 66.16 MB
- **Release notes**:

  1. Fixed OpenSSL CVE-2022-0778
  2. Added more security measures to block malware.
  3. Fixed Stored XSS vulnerability. Thanks to Milan Kyselica of IstroSec.
  4. Fixed CVE-2022-23970, CVE-2022-23971, CVE-2022-23972, CVE-2022-23973, CVE-2022-CVE-2022-25595, CVE-2022-25596
  5. Added 3rd party DNS server list in WAN --> DNS to help users enhance the connection security.
  We suggest manually resetting the router after upgrading from 3.0.0.4.384 or earlier version to this version.
  https://www.asus.com/support/FAQ/1039078
  Please unzip the firmware file first then check the MD5 code.
  MD5: d5693fe7c0ed6c0546f0f12f1b43f1c1

## 3.0.0.4.386.46092  (2022/03/17)

- **Title**: (not given)
- **Size**: 66.09 MB
- **Release notes**:

  Security
  - Fixed string format stacks vulnerability
  - Fixed cross-site-scripting vulnerability
  - Fixed informational vulnerability.
  Thanks to Howard McGreehan.
  -Fixed SQL injection vulnerability
  -Fixed json file traversal vulnerability
  -Fixed plc/port file traversal vulnerability
  -Fixed stack overflow vulnerability
  Thanks to HP of Cyber Kunlun Lab
  -Fixed authenticated stored XSS vulnerability
  Thanks to Luke Walker – SmartDCC
  -Fixed LPD denial of service vulnerability
  -Fixed cfgserver heap overflow vulnerability
  -Fixed cfgserver denial of service vulnerability
  Thanks to TianHe from BeFun Cyber Security Lab.
  -Fixed CVE-2021-34174, CVE-2022-23972, CVE-2022-23970, CVE-2022-23971, CVE-2022-23973
  Added more ISP profile
  Digi 1 - TM
  Digi 2 - TIME
  Digi 3 - Digi
  Digi 4 - CTS
  Digi 5 - ALLO
  Digi 6 - SACOFA
  Maxis - CTS
  Maxis - SACOFA
  Maxis - TNB/ALLO
  Fixed AiMesh guest network issues.
  Fixed DDNS issues where the WAN IP is IPv6
  Fixed UI bugs in Administration --> feedback.
  Fixed time zone error.
  Improved the connection stability.
  Fixed IPSecVPN issues.
  Please unzip the firmware file first then check the MD5 code.
  MD5:5ab1affddaa0d90f757154cc8d3dae54

## 3.0.0.4.386.42643  (2021/05/07)

- **Title**: (not given)
- **Size**: 65.22 MB
- **Release notes**:

  -Fixed CVE-2021-3450, CVE2021-3449 OpenSSL related vulnerability.
  - Fixed the fragattacks vulnerability.
  Please unzip the firmware file first then check the MD5 code.
  MD5: e2ff2cb9647884f9822dc8d6a63ffa90

## 9.0.0.4.386.41994  (2021/02/03)

- **Title**: (not given)
- **Size**: 65.05 MB
- **Beta version**
- **Release notes**:

  Security Fixed:
  Fixed CVE-2020-25681, CVE-2020-25682, CVE-2020-25683, CVE-2020-25687, CVE-2020-25684, CVE-2020-25685, CVE-2020-25686
  Please be noted this is a quick fix beta version for DNSmasq vulnerabilities. Refer to "Method 2: Update Manually" in https://www.asus.com/support/FAQ/1008000 to update this firmware.
  Please unzip the firmware file first then check the MD5 code.
  MD5: e97a0b79671d2d2d1d66be2ace7e3efc

## 3.0.0.4.386.41793  (2021/01/26)

- **Title**: (not given)
- **Size**: 65.08 MB
- **Release notes**:

  1. AiMesh 2.0
  - System optimization: one click in AiMesh to optimize the topology
  - System Ethernet backhaul mode, all nodes will only connect by ethernet, and all bands can release for wireless clients.
  - System factory default and reboot.
  - Client device reconnect, make the device offline and online again.
  - Client device binding to specific AP.
  - Guest WiFi on all Mesh nodes (all node need to upgrade to 3.0.0.4.386 firmware)
  - Access nodes USB application.
  Connection priority and Ethernet backhaul mode introduction
  https://www.asus.com/support/FAQ/1044184
  How to setup ASUS AiMesh or ZenWiFi Mesh Ethernet backhaul under different conditions
  https://www.asus.com/support/FAQ/1044151/
  2. New Family interface in ASUS router App.
  ASUS Router App for iOS must greater than iOS v1.0.0.5.75
  Android version greater than v1.0.0.5.74
  3. The unit of the WiFi time scheduler goes to 1 minute.
  4. Support IPSec IKE v1 and IKE v2, and you can use the Windows 10 native VPN client program to connect to the router's IPSec VPN server. The Windows 10 new FAQ is in https://www.asus.com/support/FAQ/1033576
  5. 2.4 and 5G settings on the network map could modify in the same tab.
  6. Captcha for login can be disabled in the administration -> system.
  7. Printer server port can be disabled on the USB app page.
  8. Clients who connect to the guest network can be viewed in the network map -->view list --> interface
  9. Fixed Let's Encrypt issue.
  10. Added IPTV supports for a specific region.
  Please unzip the firmware file first then check the MD5 code.
  MD5: ee65d41542ebce9947a261ef4405d812

## 3.0.0.4.384.82037  (2020/08/03)

- **Title**: (not given)
- **Size**: 59.49 MB
- **Release notes**:

  Fixed item:
  - Fixed 5GHz connection speed issues.
  Please unzip the firmware file first then check the MD5 code.
  MD5: 27e994544e94baf96e51174e924392c7

## 3.0.0.4.384.81974  (2020/07/13)

- **Title**: (not given)
- **Size**: 59.43 MB
- **Release notes**:

  Security update
  - Fixed CVE-2020-12695 (CallStranger)
  - Fixed Reflected XSS vulnerability.
  - Fixed Directory traversal vulnerability.
  - Fixed CVE-2017-15653.
  The update server transport layer security was upgraded and the old protocol was removed.
  If your router firmware version is lower than 3.0.0.4.384_81686, please refer to the "Update Manually" section in https://www.asus.com/support/FAQ/1008000 to update the firmware.
  Please unzip the firmware file first then check the MD5 code.
  MD5: 4c878dd389f624f930c8b909089a9478

## 3.0.0.4.384.81695  (2020/03/26)

- **Title**: (not given)
- **Size**: 59.29 MB
- **Release notes**:

  1. Update Adaptive QoS categories: Help you to prioritize the mission-critical applications
  Those people who work-from-home & learn-from-home will greatly benefit from this new feature with optimized streaming experiences.
  New Supported Categories & Apps:
  - Video conferencing, including Microsoft Teams®, ZOOM®, Skype®, Google Hangouts®, BlueJeans®
  - Online learning, including Khan academy®, Udemy®, Coursera®, TED®, VIPKiD®, 51Talk®, XDF®, Xueersi®
  - Streaming, including YouTube®, Netflix®, HBO NOW®, Amazon Prime Video®, Disney+®, ESPN®, MLB.com®, iQIY®
  - Indoor training, including Zwift®, Peloton®, Onelap®
  Stay tuned and more apps are coming to the list soon!
  2. Support Mobile Game Mode
  - One-click prioritizing your mobile device to the highest and ensure you the best mobile gaming experiences.
  - Install/Update ASUS Router App (Android supports later than 1.0.0.5.44; iOS supports later than 1.0.0.5.41)
  Please unzip the firmware file first and then check the MD5 code.
  MD5: de0b887a2b75115f47729ada966106b1

## 3.0.0.4.384.81686  (2020/03/10)

- **Title**: (not given)
- **Size**: 59.49 MB
- **Release notes**:

  - Fixed CVE-2019-15126 (Kr00k) vulnerability.
  Please unzip the firmware file first then check the MD5 code.
  MD5: 4b3943cceb619fd5e923b66e62474448

## 3.0.0.4.384.81685  (2020/03/06)

- **Title**: (not given)
- **Size**: 59.05 MB
- **Release notes**:

  - Fixed the firmware update problem in some special conditions.
  - Fixed UI bugs.
  - Fixed Let's Encrypt related bugs.
  - Fixed folder creating bugs in Samba.
  Please unzip the firmware file first then check the MD5 code.
  MD5: e881f3caa2ac6066f5ee76454df653ee

## 9.0.0.4.384.81551  (2020/02/03)

- **Title**: (not given)
- **Size**: 59.34 MB
- **Beta version**
- **Release notes**:

  Please be noted this is a beta version, if you want to roll back to the official version, you will need to process manual firmware update in web GUI.
  - Fixed a DDoS vulnerability.
  - Fixed Let's Encrypt related bugs.
  - Fixed VPN Fusion issues.
  - Fixed folder creating bugs in Samba.
  - Fixed dual wan failover bugs while the primary wan type is L2TP.
  Please unzip the firmware file first then check the MD5 code.
  MD5: 5ca64a4ad70e344bda542161cc2d86a4

## 3.0.0.4.384.81099  (2019/09/23)

- **Title**: (not given)
- **Size**: 63.12 MB
- **Release notes**:

  Security fix
  - Fixed a DDoS vulnerability. Thanks for Altin Thartori's contribution.
  Bug fix
  - Fixed web control interface login problem.
  - Fixed Network map clist list issues.
  - Fixed VPN fusion related bugs.
  - Fixed block internet access problem when clients connected to AiMesh node
  - Fixed Samba server compatibility issue.
  - Fixed OpenVPN related bugs.
  - Fixed schedule reboot bugs.
  - Improved AiMesh compatibility.
  - Improved system stability.
  - Fixed User interface related bugs.
  Please unzip the firmware file first then check the MD5 code.
  MD5: fe3c48f2b9a3767a89b36e58bf942a7f

## 3.0.0.4.384.70116  (2019/05/30)

- **Title**: (not given)
- **Size**: 61.29 MB
- **Release notes**: *(none / not rendered)*

## 3.0.0.4.384.45717  (2019/05/22)

- **Title**: (not given)
- **Size**: 62.31 MB
- **Release notes**:

  - Fixed DDoS vulnerability.
  - Fixed AiCloud vulnerability. Thanks for Matt Cundari's contribution.
  - Fixed command injection vulnerability. Thanks for S1mba Lu's contribution.
  - Fixed buffer overflow vulnerability. Thanks for Javier Aguinaga's contribution.
  Please unzip the firmware file first then check the MD5 code.
  MD5: 641b0a8a03ad080f25981ecc96a72abe

## 3.0.0.4.384.45713  (2019/04/18)

- **Title**: (not given)
- **Size**: 62.31 MB
- **Release notes**:

  Security Fix
  - Fixed CVE-2018-20334
  - Fixed CVE-2018-20336
  - Fixed null pointer issue. Thanks for CodeBreaker of STARLabs’ contribution.
  - Fixed AiCloud buffer overflow vulnerability. Thanks for Resecurity International's contribution.
  Bug Fix
  - Fixed AiMesh LAN IP issue when router using IPv6 WAN.
  - Fixed AiMesh connection issues.
  - Fixed Network Map related issues.
  - Fixed Download Master icon disappear issue.
  - Fixed LAN LED not blinking problem.
  - Fixed browser no response problem when enabled Traffic analyzer.
  - Fixed wireless mac filter input issue.
  Please unzip the firmware file first then check the MD5 code.
  MD5: 9558196da53500a2a8cbf43684c8b8d4

## 3.0.0.4.384.45708  (2019/04/03)

- **Title**: (not given)
- **Size**: 62.31 MB
- **Release notes**:

  Security Fix
  - Fixed CVE-2018-20334
  - Fixed CVE-2018-20336
  - Fixed null pointer issue. Thanks for CodeBreaker of STARLabs’ contribution.
  - Fixed AiCloud buffer overflow vulnerability. Thanks for Resecurity International's contribution.
  Bug Fix
  - Fixed AiMesh LAN IP issue when router using IPv6 WAN.
  - Fixed AiMesh connection issues.
  - Fixed Network Map related issues.
  - Fixed Download Master icon disappear issue.
  - Fixed LAN PC cannot find router name in My Network Places when enabling Samba service.
  - Fixed LAN LED not blinking problem.
  Please unzip the firmware file first then check the MD5 code.
  MD5: f59c82a740cf6486d6060d52475b6a21

## 3.0.0.4.384.45149  (2018/12/05)

- **Title**: (not given)
- **Size**: 66.22 MB
- **Release notes**:

  AiMesh
  - Improved AiMesh dedicated backhaul mechanism for tri-band to tri-band AiMesh modes.
  - Lyra, Lyra Mini, and Lyra Trio can be added as AiMesh node into GT-AC5300 network.
  Please refer to https://www.asus.com/support/FAQ/1038071 for more detail.
  Security
  - Fixed CVE-2018-14710, CVE-2018-14711, CVE-2018-14712, CVE-2018-14713, CVE-2018-14714. Thanks for Rick Ramgattie's contribution.
  - Fixed AiCloud/ Samba account vulnerability. Thanks for Matthew Cundari's contribution.
  - Fixed DoS vulnerability. Thanks for Ruikai Liu's contribution.
  - Fixed CVE-2018-17020, CVE-2018-17021, CVE-2018-17022.
  - Fixed stored XSS vulnerability. Thanks for Duda Przemyslaw's contribution.
  - Updated OpenSSL library.
  New Alexa skill and IFTTT actions
  - Add Alexa skill “ ask ASUS ROUTER to report security status”
  - Add Alexa skill “ ask ASUS ROUTER how many devices are online”
  - Add IFTTT actions : Wake on LAN
  - Add IFTTT actions : check new firmware available and upgrade
  [Note] You have to upgrade the firmware version up to 3.0.0.4.384_45149 if you want to use these new Alexa skills and IFTTT actions.
  Bug fixes and improvement
  - Improved wireless stability.
  - Modified “Dual Wan” user interface.
  - Modified “Port Forwarding” user interface.
  - Modified “Restore” user interface.
  - Fixed “VPN Fusion” bugs.
  - Fixed GUI bugs on user feedback page.
  - Fixed “Adaptive QoS” bugs.
  Please unzip the firmware file first then check the MD5 code.
  MD5: 0b201e7ff22b117deb66642a7bc4f0bf

## 3.0.0.4.384.32799  (2018/09/19)

- **Title**: (not given)
- **Size**: 65.37 MB
- **Release notes**:

  Fixed WIFI stability issue.
  Please unzip the firmware file first then check the MD5 code.
  MD5: fdf31cb397cb52baf84c2b45579bf3a7

## 3.0.0.4.384.32738  (2018/08/21)

- **Title**: (not given)
- **Size**: 65.36 MB
- **Release notes**:

  AiMesh new features
  - Supported creating mesh system with new router, BlueCave.
  - Added Roaming block list in Advanced Settings --> Wireless.
  You can add devices into block list and this device will not be roamed between AiMesh nodes.
  - Supported ethernet onboarding. User can use ethernet cable.
  You can use ethernet cable to connect AiMesh router LAN port and AiMesh node WAN port first and run the adding node process to build the mesh system.
  Security fixes.
  - Fixed Reflected XSS vulnerability.
  - Fixed CSRF vulnerability.
  - Fixed command injection vulnerability.
  - Fixed stack buffer overflow vulnerability.
  Thanks for Rick Ramgattie contribution.
  Fixed Adaptive QoS upload bandwidth setting issue.
  Fixed 4-wire ethernet cable compatibility issues.
  Fixed USB hard drive over 2TB compatibility issues.
  Fixed Samba/FTP folder permission issues.
  Added USB3.0/2.0 mode switch setting in Administration --> System --> USB Settings.
  Please unzip the firmware file first then check the MD5 code.
  MD5: b5993113cb163272605bc48a097875f3

## 3.0.0.4.384.21140  (2018/07/10)

- **Title**: (not given)
- **Size**: 65.81 MB
- **Release notes**:

  - [DDNS] Modified the procedure of DDNS service register under dual wan load balance mode
  - [WAN] Modified detect logic of internet connection
  - [AiMesh] Fixed AiMesh onboarding unsuccessfully once smart connect is enabled
  - [AiMesh] Modified AiMesh nodes notification procedure
  - [GUI] Fixed AiProtection GUI bugs.
  - [GUI] Updated OpenVPN server FAQ URL.
  Please unzip the firmware file first then check the MD5 code.
  MD5: cb5adc0097f052453e2cf54c64501b0f
