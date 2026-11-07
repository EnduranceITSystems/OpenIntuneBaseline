# EIT workstation policies

All custom policy exports are additional `Win - EIT - ... - v1.0` policies beside the original OIB files in `WINDOWS/IntuneManagement/SettingsCatalog`. The original 77 OIB exports and `WINDOWS/PolicyManifest.json` are unchanged from source revision `4229858a3bc00d8bfa81809c1d7829eab6313595`.

## Identity and ownership

- Every EIT policy has a new `EITID:<GUID>` marker and a distinct export object GUID. Neither is reused from an OIB policy.
- Reference custom policies with `eit:<lowercase-guid>`; reference original policies with `oib:<lowercase-guid>`.
- `WINDOWS/EITPolicyManifest.json` owns EIT identities, source lineage and phase metadata. Original OIB manifest entries stay active and unchanged.
- A source OIB ID records derivation, not an update or deprecation. Export object GUIDs are provenance placeholders, never customer object identities.
- The OIB manifest updater excludes EIT files, so it cannot relabel or rotate EIT identities. EIT structural/identity validation runs through the tests below.
- All EIT exports are unassigned candidates. Intune schema/import validation and device pilots remain pending.

## New EIT policy exports

| EIT policy | EIT reference | OIB source ID |
| --- | --- | --- |
| [Win - EIT - ES - Defender Antivirus - D - AV Configuration - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20ES%20-%20Defender%20Antivirus%20-%20D%20-%20AV%20Configuration%20-%20v1.0.json) | `eit:534437ec-a7be-512e-a24f-d9679fbb8a3e` | `oib:2064828d-fb90-4a27-b4f9-3ee30f5a4da2` |
| [Win - EIT - ES - Defender Antivirus - D - Security Experience - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20ES%20-%20Defender%20Antivirus%20-%20D%20-%20Security%20Experience%20-%20v1.0.json) | `eit:e94196a8-04f4-5275-8bb2-69d366730e13` | `oib:1bdb3565-26e1-4820-b79f-6afed73c5a67` |
| [Win - EIT - ES - Defender Antivirus - D - Tamper Protection - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20ES%20-%20Defender%20Antivirus%20-%20D%20-%20Tamper%20Protection%20-%20v1.0.json) | `eit:a67bcf50-6ba6-5a22-87f5-7072d7e7db06` | `oib:1bdb3565-26e1-4820-b79f-6afed73c5a67` |
| [Win - EIT - SC - Device Security - U - Session Lock and Wake Authentication - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Device%20Security%20-%20U%20-%20Session%20Lock%20and%20Wake%20Authentication%20-%20v1.0.json) | `eit:f6c3f6cf-e74c-5674-bdc1-6943a4a27c65` | `oib:d4027112-4cf4-4e56-82cd-0fc97d43580f` |
| [Win - EIT - SC - Device Security - U - Workstation Power Management - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Device%20Security%20-%20U%20-%20Workstation%20Power%20Management%20-%20v1.0.json) | `eit:09e16f5d-b8d8-5f3c-8f4d-762b7e99c40f` | `oib:d4027112-4cf4-4e56-82cd-0fc97d43580f` |
| [Win - EIT - SC - Credential Management - D - Passwordless Experience - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Credential%20Management%20-%20D%20-%20Passwordless%20Experience%20-%20v1.0.json) | `eit:92129f67-fa4d-5ecd-9f32-6555bb280df5` | `oib:ac354d32-c6b3-41c2-a2e9-68f89f2efc98` |
| [Win - EIT - SC - Credential Management - D - Web Sign-In - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Credential%20Management%20-%20D%20-%20Web%20Sign-In%20-%20v1.0.json) | `eit:5b05ba52-6b64-571d-a37a-40e935157e4f` | `oib:ac354d32-c6b3-41c2-a2e9-68f89f2efc98` |
| [Win - EIT - SC - Microsoft Edge - U - Management - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Microsoft%20Edge%20-%20U%20-%20Management%20-%20v1.0.json) | `eit:bfc47284-490c-5137-baed-e481aaced7bd` | `oib:88eeb6c0-a110-4473-bf63-79fb1649cd8b` |
| [Win - EIT - SC - Microsoft Edge - U - Extensions - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Microsoft%20Edge%20-%20U%20-%20Extensions%20-%20v1.0.json) | `eit:39da61fb-41a4-5790-882d-7caa7ee98fc8` | `oib:3b1399b4-fc9a-4523-820f-769416d72543` |
| [Win - EIT - SC - Microsoft Edge - U - Approved Extensions - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Microsoft%20Edge%20-%20U%20-%20Approved%20Extensions%20-%20v1.0.json) | `eit:56a75bab-b6b5-5ba8-90a9-0246dfe6fdb7` | `oib:3b1399b4-fc9a-4523-820f-769416d72543` |
| [Win - EIT - SC - Microsoft Edge - U - Required Extensions - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Microsoft%20Edge%20-%20U%20-%20Required%20Extensions%20-%20v1.0.json) | `eit:ff59e197-d050-5509-affe-763958c19fdc` | `oib:3b1399b4-fc9a-4523-820f-769416d72543` |
| [Win - EIT - SC - Microsoft Edge - U - User Experience - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Microsoft%20Edge%20-%20U%20-%20User%20Experience%20-%20v1.0.json) | `eit:c45bde50-7556-5918-8b3b-cfe26346b02f` | `oib:fd09768a-a622-4a0d-a944-2d9cfabc4b8e` |
| [Win - EIT - SC - Microsoft Edge - U - Website Notifications - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Microsoft%20Edge%20-%20U%20-%20Website%20Notifications%20-%20v1.0.json) | `eit:46e80d02-8477-53ee-855d-7ff4b78d6b3a` | `oib:fd09768a-a622-4a0d-a944-2d9cfabc4b8e` |
| [Win - EIT - SC - Microsoft Edge - U - Approved Notification Sites - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Microsoft%20Edge%20-%20U%20-%20Approved%20Notification%20Sites%20-%20v1.0.json) | `eit:038e4a1d-2c1e-5300-ada7-96db5396683b` | `oib:fd09768a-a622-4a0d-a944-2d9cfabc4b8e` |
| [Win - EIT - SC - Microsoft OneDrive - D - Configuration - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Microsoft%20OneDrive%20-%20D%20-%20Configuration%20-%20v1.0.json) | `eit:d5dc74cf-dcc4-5249-9db8-6d9707e6f098` | `oib:6ef9dfea-74b4-485d-aad2-237f7e2ebab2` |
| [Win - EIT - SC - Microsoft OneDrive - D - Allowed Sync Tenants - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Microsoft%20OneDrive%20-%20D%20-%20Allowed%20Sync%20Tenants%20-%20v1.0.json) | `eit:bc32307c-7205-5eab-8d05-24d181ebbe77` | `oib:6ef9dfea-74b4-485d-aad2-237f7e2ebab2` |
| [Win - EIT - SC - Device Security - D - Printing - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Device%20Security%20-%20D%20-%20Printing%20-%20v1.0.json) | `eit:82fc6a20-ffbf-57ce-b40a-93308ca7e678` | `oib:1968c406-b707-4382-ac9e-2fc4ee084eb4` |
| [Win - EIT - SC - Microsoft Store - D - Configuration - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Microsoft%20Store%20-%20D%20-%20Configuration%20-%20v1.0.json) | `eit:453fe1bc-feb8-59b2-8adc-d0a9c6d49b2a` | `oib:d239dfc3-e20a-48c9-a906-09c0af624cb7` |
| [Win - EIT - SC - Microsoft Store - D - Packaged App Installation (Enterprise) - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Microsoft%20Store%20-%20D%20-%20Packaged%20App%20Installation%20(Enterprise)%20-%20v1.0.json) | `eit:edd7cabd-5a61-5536-b6e2-cfa55230b79b` | `oib:d239dfc3-e20a-48c9-a906-09c0af624cb7` |
| [Win - EIT - SC - Microsoft Store - U - Configuration - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Microsoft%20Store%20-%20U%20-%20Configuration%20-%20v1.0.json) | `eit:91139756-b0b3-5481-8aff-798df75175a2` | `oib:2a4518b8-64b5-43c4-ac03-18ce627f1105` |
| [Win - EIT - SC - Microsoft Store - U - Store Access (Enterprise) - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Microsoft%20Store%20-%20U%20-%20Store%20Access%20(Enterprise)%20-%20v1.0.json) | `eit:e3ea9d6b-b344-57cb-b519-df83a090b77b` | `oib:2a4518b8-64b5-43c4-ac03-18ce627f1105` |
| [Win - EIT - ES - Defender Antivirus Updates - D - Test - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20ES%20-%20Defender%20Antivirus%20Updates%20-%20D%20-%20Test%20-%20v1.0.json) | `eit:04db5f11-023f-5271-9ff8-4208faa2ccec` | `oib:c1b1a707-f50c-461a-a811-e8d47fed076c` |
| [Win - EIT - ES - Defender Antivirus Updates - D - Production - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20ES%20-%20Defender%20Antivirus%20Updates%20-%20D%20-%20Production%20-%20v1.0.json) | `eit:01ef94aa-4306-570f-afee-73769b140580` | `oib:f597c79e-dbdb-4419-aa69-3617716658e4` |
| [Win - EIT - SC - Network Security - D - NTLM Enforcement - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Network%20Security%20-%20D%20-%20NTLM%20Enforcement%20-%20v1.0.json) | `eit:3c2ddaa8-b2da-54fe-9a59-f2e9745d745a` | `oib:78a64af6-87dc-4a95-94f8-e967508adee7` |
| [Win - EIT - SC - Network Security - D - NTLM Audit - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Network%20Security%20-%20D%20-%20NTLM%20Audit%20-%20v1.0.json) | `eit:abd3a60a-0c60-5329-9109-bf1ea19c7e62` | `oib:78a64af6-87dc-4a95-94f8-e967508adee7` |
| [Win - EIT - SC - Device Security - D - Remote Desktop Host Access - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Device%20Security%20-%20D%20-%20Remote%20Desktop%20Host%20Access%20-%20v1.0.json) | `eit:f53caec5-b037-5940-8046-0b19203e178e` | `oib:a61ce19f-4615-42ab-abe7-bdcd76d2b203` |
| [Win - EIT - SC - Device Security - D - Workstation File Associations - v1.0](../IntuneManagement/SettingsCatalog/Win%20-%20EIT%20-%20SC%20-%20Device%20Security%20-%20D%20-%20Workstation%20File%20Associations%20-%20v1.0.json) | `eit:52935b3b-6995-57ab-b9ec-39d79f817a5b` | `oib:887cefec-6882-49e0-a237-91f8d02b2cab` |

## Selection without changing OIB

Use the source register's `selectionSets` and each EIT policy's phase and `standardSelection` metadata. The two EIT `(Enterprise)` Store controls are excluded from Pro/Business selection. Approved extension/notification policies are parameter-dependent and omitted for empty approved lists; Web Sign-In remains optional. `targetEditions` records intended targeting, while `supportStatus: validation-required` preserves the pending technical review. For a replacement set, select its EIT policies for the relevant populations/phases and omit the corresponding original OIB policy from those targets. This does not modify, retire or delete that OIB policy. The original remains available to other environments.

The EIT native RDP host-access control is additive: retain the original OIB RDP/RPC hardening alongside it. NTLM Audit and NTLM Enforcement are exclusive phases. Passwordless Experience follows Hello enrollment; Web Sign-In is optional. Defender Test and Production have separate memberships. Do not coassign conflicting OIB and EIT implementations.

## Customer parameter contract

Source parameter bindings live in `EITWorkstationPolicies.json` and identify the exact `policyRef` and setting. EIT parameter templates must be rendered before import; unresolved tokens are not deployable settings. Empty approved extension/notification lists omit those optional policies. OneDrive allowed sync tenants must include the customer plus approved partners, while KFM/custom-root bindings remain customer-only. Approved print-server input serializes as a semicolon-separated list. These are customer values, not local automation variants.

## Source-owned change register

`EITWorkstationPolicies.json` links all requests to EIT or unchanged OIB policy references. Prepared is authored, not deployed. Compatibility/design entries without an export remain explicit gaps.

| Request | Status | Policy references / source artifacts |
| --- | --- | --- |
| `safe-samples` | prepared | `eit:534437ec-a7be-512e-a24f-d9679fbb8a3e`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - ES - Defender Antivirus - D - AV Configuration - v1.0.json` |
| `require-tamper` | prepared | `eit:a67bcf50-6ba6-5a22-87f5-7072d7e7db06`<br>`eit:e94196a8-04f4-5275-8bb2-69d366730e13`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - ES - Defender Antivirus - D - Tamper Protection - v1.0.json`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - ES - Defender Antivirus - D - Security Experience - v1.0.json` |
| `no-ac-idle-sleep` | prepared | `eit:09e16f5d-b8d8-5f3c-8f4d-762b7e99c40f`<br>`eit:f6c3f6cf-e74c-5674-bdc1-6943a4a27c65`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Device Security - U - Workstation Power Management - v1.0.json`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Device Security - U - Session Lock and Wake Authentication - v1.0.json` |
| `split-passwordless-web-signin` | prepared | `eit:92129f67-fa4d-5ecd-9f32-6555bb280df5`<br>`eit:5b05ba52-6b64-571d-a37a-40e935157e4f`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Credential Management - D - Passwordless Experience - v1.0.json`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Credential Management - D - Web Sign-In - v1.0.json` |
| `intune-edge-owner` | prepared | `eit:bfc47284-490c-5137-baed-e481aaced7bd`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Microsoft Edge - U - Management - v1.0.json` |
| `customer-edge-extensions` | parameter-template | `eit:39da61fb-41a4-5790-882d-7caa7ee98fc8`<br>`eit:56a75bab-b6b5-5ba8-90a9-0246dfe6fdb7`<br>`eit:ff59e197-d050-5509-affe-763958c19fdc`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Microsoft Edge - U - Extensions - v1.0.json`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Microsoft Edge - U - Approved Extensions - v1.0.json`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Microsoft Edge - U - Required Extensions - v1.0.json` |
| `customer-edge-notifications` | parameter-template | `eit:c45bde50-7556-5918-8b3b-cfe26346b02f`<br>`eit:46e80d02-8477-53ee-855d-7ff4b78d6b3a`<br>`eit:038e4a1d-2c1e-5300-ada7-96db5396683b`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Microsoft Edge - U - User Experience - v1.0.json`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Microsoft Edge - U - Website Notifications - v1.0.json`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Microsoft Edge - U - Approved Notification Sites - v1.0.json` |
| `onedrive-tenant-scope` | parameter-template | `eit:bc32307c-7205-5eab-8d05-24d181ebbe77`<br>`eit:d5dc74cf-dcc4-5249-9db8-6d9707e6f098`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Microsoft OneDrive - D - Allowed Sync Tenants - v1.0.json`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Microsoft OneDrive - D - Configuration - v1.0.json` |
| `onedrive-user-tenant` | parameter-binding | `oib:5cd97975-5495-4da4-a402-89817d130cf4`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - OIB - SC - Microsoft OneDrive - U - Configuration - v3.8.json` |
| `customer-printing` | parameter-template | `eit:82fc6a20-ffbf-57ce-b40a-93308ca7e678`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Device Security - D - Printing - v1.0.json` |
| `store-device-pro` | prepared | `eit:453fe1bc-feb8-59b2-8adc-d0a9c6d49b2a`<br>`eit:edd7cabd-5a61-5536-b6e2-cfa55230b79b`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Microsoft Store - D - Configuration - v1.0.json`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Microsoft Store - D - Packaged App Installation (Enterprise) - v1.0.json` |
| `store-user-pro` | prepared | `eit:91139756-b0b3-5481-8aff-798df75175a2`<br>`eit:e3ea9d6b-b344-57cb-b519-df83a090b77b`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Microsoft Store - U - Configuration - v1.0.json`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Microsoft Store - U - Store Access (Enterprise) - v1.0.json` |
| `defender-test-channels` | prepared | `eit:04db5f11-023f-5271-9ff8-4208faa2ccec`<br>`eit:01ef94aa-4306-570f-afee-73769b140580`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - ES - Defender Antivirus Updates - D - Test - v1.0.json`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - ES - Defender Antivirus Updates - D - Production - v1.0.json` |
| `script-associations` | prepared | `eit:52935b3b-6995-57ab-b9ec-39d79f817a5b`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Device Security - D - Workstation File Associations - v1.0.json` |
| `ntlm-audit-transition` | prepared | `eit:abd3a60a-0c60-5329-9109-bf1ea19c7e62`<br>`eit:3c2ddaa8-b2da-54fe-9a59-f2e9745d745a`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Network Security - D - NTLM Audit - v1.0.json`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Network Security - D - NTLM Enforcement - v1.0.json` |
| `pro-cleanup` | design-required |  |
| `pro-copilot-removal` | prepared-script | `WINDOWS/Scripts/EIT-Remove-ConsumerCopilot.ps1` |
| `explicit-rdp-host` | prepared | `eit:f53caec5-b037-5940-8046-0b19203e178e`<br>`oib:a61ce19f-4615-42ab-abe7-bdcd76d2b203`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - EIT - SC - Device Security - D - Remote Desktop Host Access - v1.0.json`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - OIB - SC - Device Security - D - Remote Desktop Services and RPC - v3.0.json` |
| `mobile-site-timezones` | assignment-design | `WINDOWS/Scripts/Enable-AutoTimezone.ps1` |
| `entra-bitlocker-escrow` | compatibility-review | `oib:c53f0da8-45d9-4e38-ab62-d3c359ed91f6`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - OIB - ES - Encryption - D - BitLocker (OS Disk) - v3.7.json` |
| `local-admin-identity` | no-policy-change | `oib:05b9a828-db19-4769-b112-62ea1f5367d6`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - OIB - ES - Local Group Membership - D - Local Administrators - v3.7.json` |
| `business-account-preservation` | compatibility-review | `oib:7afcf2fb-6037-49e5-a22f-5e14676eff69`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - OIB - SC - Microsoft Accounts - D - Configuration - v3.2.json` |
| `site-peering` | assignment-design | `oib:743720b0-ddc7-4c5a-a50a-de89476aef10`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - OIB - SC - Windows Update for Business - D - Delivery Optimisation - v3.0.json` |
| `pro-core-support` | compatibility-review | `oib:d35fd54a-f74f-4f61-969f-6e96d3986b41`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - OIB - SC - Device Security - D - Security Hardening - v4.0.json` |
| `supported-windows-features` | compatibility-review | `oib:3ea33ae4-1f7a-43cd-a82e-ee319470f857`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - OIB - SC - Windows User Experience - D - Feature Configuration - v4.0.json` |
| `supported-settings-backup` | compatibility-review | `oib:604fd048-ca7d-4918-aa55-66a4878e0f52`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - OIB - SC - Windows User Experience - D - Settings Sync - v3.7.json` |
| `supported-spotlight` | compatibility-review | `oib:457cad52-5b2e-4ac6-9451-6d56c05dc4cb`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - OIB - SC - Device Security - U - Windows Spotlight and Org Messages - v3.0.json` |
| `office-supported-controls` | compatibility-review | `oib:a182db08-2f64-4535-8a7e-c0277d88152b`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - OIB - SC - Microsoft Office - D - Security - v3.6.json` |
| `office-user-supported-controls` | compatibility-review | `oib:b549dfd9-5049-4813-a2fb-c860d00290ba`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - OIB - SC - Microsoft Office - U - Security - v4.0.json` |
| `office-supported-preferences` | compatibility-review | `oib:2993c83d-2b5c-4258-bb6e-9392b45eb401`<br>`WINDOWS/IntuneManagement/SettingsCatalog/Win - OIB - SC - Microsoft Office - U - Config and Experience - v3.6.json` |

## Review requirements

Validate new incoming-NTLM-audit, RDP-host and extension-allowlist Settings Catalog definitions during Intune import. Validate current tamper/controlled-configuration semantics, licensing and onboarding. Preserve the baseline Administrator Protection v4.0.1/LAPS fix; it is not changed by this work.

`WINDOWS/Scripts/EIT-Remove-ConsumerCopilot.ps1` targets only the consumer `Microsoft.Copilot` package and defaults to audit. It is not a broad approved cleanup list. Review local-data impact and pilot results before requesting remediation. Office product support, Entra BitLocker escrow, automatic timezone targeting and broad Pro cleanup remain technical gates.

## Local checks

```powershell
./Scripts/Update-OIBManifest.ps1 -Mode Validate -Platform Windows
python -m unittest discover -s WINDOWS/Tests -v
```

Tests verify original OIB file hashes, unchanged OIB manifest, distinct EIT and export IDs, source links, phase metadata, policy structure and intended EIT settings. No live tenant or device application is implied.

Microsoft references: [NTLM auditing](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-localpoliciessecurityoptions#networksecurity_restrictntlm_auditincomingntlmtraffic), [RDP host control](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-remotedesktopservices#allowuserstoconnectremotely), [Edge associations](https://learn.microsoft.com/en-us/deployedge/edge-default-browser).
