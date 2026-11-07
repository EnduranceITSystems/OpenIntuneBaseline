"""Local structural/intent checks; no Graph calls or package-removal execution."""
import base64
import hashlib
import json
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

WINDOWS = Path(__file__).resolve().parents[1]
ROOT = WINDOWS.parent


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


class EITWorkstationPolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads((WINDOWS / 'Standards/EITWorkstationPolicies.json').read_text(encoding='utf-8'))
        cls.manifest = json.loads((WINDOWS / 'EITPolicyManifest.json').read_text(encoding='utf-8'))
        cls.exports = [json.loads(p.read_text(encoding='utf-8-sig')) for p in (WINDOWS / 'IntuneManagement/SettingsCatalog').glob('Win - EIT - *.json')]

    def policy(self, part):
        found = [p for p in self.exports if part in p['name']]
        self.assertEqual(1, len(found), part)
        return found[0]

    def setting(self, policy, suffix):
        nodes = [n for n in walk(policy['settings']) if n.get('settingDefinitionId', '').endswith(suffix)]
        self.assertEqual(1, len(nodes), suffix)
        return nodes[0]

    def choice(self, part, suffix):
        return self.setting(self.policy(part), suffix)['choiceSettingValue']['value']

    def test_changed_exports_have_manifest_identity_and_no_assignments(self):
        manifest = {p['eitId'].upper(): p for p in self.manifest['policies']}
        self.assertEqual(len(manifest), len(self.manifest['policies']))
        for row in self.index['policyChanges']:
            p = json.loads((ROOT / row['path']).read_text(encoding='utf-8'))
            self.assertEqual(row['name'], p['name'])
            self.assertEqual(row['name'] + '.json', Path(row['path']).name)
            self.assertTrue(row['name'].startswith('Win - EIT - '))
            self.assertTrue(row['name'].endswith(' - v1.0'))
            self.assertNotIn('OIBID:', p['description'])
            self.assertEqual(p['settingCount'], len(p['settings']))
            self.assertEqual([], p['assignments'])
            ids = re.findall(r'EITID:([0-9A-Fa-f-]{36})', p['description'])
            self.assertEqual([row['eitId']], [i.upper() for i in ids])
            self.assertEqual(row['name'], manifest[row['eitId']]['name'])
            self.assertEqual([str(i) for i in range(len(p['settings']))], [s['id'] for s in p['settings']])

    def test_no_duplicate_active_policy_export_identity(self):
        ids = [re.search(r'EITID:([0-9A-Fa-f-]{36})', p['description'])[1].upper() for p in self.exports]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(self.exports), len({p['id'] for p in self.exports}))

    def test_parameters_bind_real_export_settings(self):
        exports = {}
        for path in (WINDOWS / 'IntuneManagement').rglob('*.json'):
            p = json.loads(path.read_text(encoding='utf-8-sig'))
            match = re.search(r'(EITID|OIBID):([0-9A-Fa-f-]{36})', p['description'])
            ref = ('eit:' if match[1] == 'EITID' else 'oib:') + match[2].lower()
            exports[ref] = p
        for b in self.index['customerParameterBindings']:
            p = exports[b['policyRef']]
            self.assertIn(b['settingId'], {n.get('settingDefinitionId') for n in walk(p)})
            self.assertIn(b['token'], json.dumps(p))

    def test_safe_samples_and_separate_tamper(self):
        self.assertTrue(self.choice('Defender Antivirus - D - AV Configuration', 'submitsamplesconsent').endswith('_1'))
        self.assertTrue(self.choice('Defender Antivirus - D - Tamper Protection', 'tamperprotection_options').endswith('_1'))
        self.assertNotIn('tamperprotection_options', json.dumps(self.policy('Defender Antivirus - D - Security Experience')))

    def test_power_and_lock_are_separate(self):
        p = self.policy('Workstation Power Management')
        self.assertEqual(0, self.setting(p, 'standbytimeoutpluggedin_enteracstandbytimeout')['simpleSettingValue']['value'])
        self.assertEqual(0, self.setting(p, 'unattendedsleeptimeoutpluggedin')['simpleSettingValue']['value'])
        self.assertNotIn('machineinactivitylimit', json.dumps(p))
        lock = self.policy('Session Lock and Wake Authentication')
        self.assertEqual(900, self.setting(lock, 'machineinactivitylimit_v2')['simpleSettingValue']['value'])
        self.assertNotIn('standbytimeout', json.dumps(lock))

    def test_web_signin_does_not_leak_into_passwordless(self):
        self.assertNotIn('enablewebsignin', json.dumps(self.policy('Passwordless Experience')))
        self.assertEqual(1, self.policy('Web Sign-In')['settingCount'])

    def test_enterprise_store_controls_are_separate(self):
        self.assertNotIn('blocknonadminuserinstall', json.dumps(self.policy('Store - D - Configuration')))
        self.assertNotIn('removewindowsstore_1', json.dumps(self.policy('Store - U - Configuration')))
        self.assertEqual(1, self.policy('Packaged App Installation (Enterprise)')['settingCount'])
        self.assertEqual(1, self.policy('Store Access (Enterprise)')['settingCount'])

    def test_default_extensions_do_not_force_copilot(self):
        text = json.dumps(self.policy('Edge - U - Extensions'))
        self.assertNotIn('extensioninstallforcelist', text)
        self.assertNotIn('ofefcgjbeghpigppfmkologfjadafddi', text)
        self.assertNotIn('nkbndigcebkoaejohleckhekfmcecfja', text)

    def test_one_drive_kfm_and_partner_list_are_separate(self):
        self.assertNotIn('allowtenantlist', json.dumps(self.policy('OneDrive - D - Configuration')))
        self.assertNotIn('kfmoptinnowizard', json.dumps(self.policy('Allowed Sync Tenants')))
        allow = next(b for b in self.index['customerParameterBindings'] if b['parameter'] == 'onedrive-allowed-tenants')
        self.assertEqual('customer-tenant-id', allow['mustInclude'])
        self.assertEqual('reject', allow['emptyBehavior'])

    def test_ntlm_audit_is_not_enforcement(self):
        self.assertTrue(self.choice('NTLM Audit', 'restrictntlm_incomingntlmtraffic').endswith('_0'))
        self.assertTrue(self.choice('NTLM Audit', 'restrictntlm_outgoingntlmtraffictoremoteservers').endswith('_1'))
        self.assertTrue(self.choice('NTLM Audit', 'restrictntlm_auditincomingntlmtraffic').endswith('_2'))
        self.assertTrue(self.choice('NTLM Enforcement', 'restrictntlm_incomingntlmtraffic').endswith('_2'))

    def test_defender_test_channels(self):
        self.assertTrue(self.choice('Defender Antivirus Updates - D - Test', 'engineupdateschannel').endswith('_4'))
        self.assertTrue(self.choice('Defender Antivirus Updates - D - Test', 'platformupdateschannel').endswith('_4'))
        self.assertTrue(self.choice('Defender Antivirus Updates - D - Test', 'securityintelligenceupdateschannel').endswith('_5'))

    def test_native_rdp_is_explicitly_disabled(self):
        self.assertTrue(self.choice('Remote Desktop Host Access', 'allowuserstoconnectremotely').endswith('_0'))

    def test_single_merged_association_payload(self):
        owners = [p for p in self.exports if any(n.get('settingDefinitionId', '').endswith('defaultassociationsconfiguration') for n in walk(p))]
        self.assertEqual(1, len(owners))
        node = self.setting(owners[0], 'defaultassociationsconfiguration')
        xml = ET.fromstring(base64.b64decode(node['simpleSettingValue']['value']))
        entries = {n.attrib['Identifier']: n.attrib for n in xml}
        self.assertEqual(len(entries), len(xml))
        for key in ['.htm', '.html', 'http', 'https']:
            self.assertEqual('MSEdgeHTM', entries[key]['ProgId'])
        for key in ['.appx', '.cab', '.com', '.shb', '.shs', '.pdf']:
            self.assertNotIn(key, entries)
        self.assertEqual('Applications\\notepad.exe', entries['.ps1']['ProgId'])

    def test_every_proposed_path_exists(self):
        for row in self.index['requirements']:
            for path in row['proposedPolicyPaths']:
                self.assertTrue((ROOT / path).is_file(), path)

    def test_original_oib_exports_and_manifest_are_unchanged(self):
        expected = self.manifest['baselinePolicySha256']
        originals = {p.relative_to(ROOT).as_posix() for p in (WINDOWS / 'IntuneManagement').rglob('Win - OIB - *.json')}
        self.assertEqual(77, len(expected))
        self.assertEqual(set(expected), originals)
        for path, digest in expected.items():
            self.assertEqual(digest, hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), path)
        self.assertEqual(self.manifest['oibManifestSha256'], hashlib.sha256((WINDOWS / 'PolicyManifest.json').read_bytes()).hexdigest())

    def test_eit_ids_and_export_ids_cannot_collide_with_oib(self):
        original_ids, original_export_ids = set(), set()
        for path in self.manifest['baselinePolicySha256']:
            p = json.loads((ROOT / path).read_text(encoding='utf-8-sig'))
            original_ids.add(re.search(r'OIBID:([0-9A-Fa-f-]{36})', p['description'])[1].upper())
            original_export_ids.add(p['id'])
        eit_ids = {r['eitId'] for r in self.index['policyChanges']}
        self.assertEqual(27, len(eit_ids))
        self.assertTrue(eit_ids.isdisjoint(original_ids))
        self.assertTrue({p['id'] for p in self.exports}.isdisjoint(original_export_ids))
        for row in self.index['policyChanges']:
            self.assertIn(row['sourceOibId'], original_ids)
            self.assertEqual('eit:' + row['eitId'].lower(), row['reference'])

    def test_selection_sets_reference_eit_policies_without_retiring_oib(self):
        known = {r['reference'] for r in self.index['policyChanges']}
        for row in self.index['selectionSets']:
            self.assertTrue(set(row['eitPolicyRefs']) <= known)
        oib = json.loads((WINDOWS / 'PolicyManifest.json').read_text(encoding='utf-8'))
        identities = {r['oibId'].lower(): r for r in oib['policies']}
        for row in self.index['selectionSets']:
            self.assertEqual('active', identities[row['sourcePolicyId'][4:]]['status'])


    def test_enterprise_controls_are_not_selected_for_pro(self):
        excluded = {r['reference'] for r in self.manifest['policies'] if '(Enterprise)' in r['name']}
        self.assertEqual(2, len(excluded))
        selected = {ref for row in self.index['selectionSets'] for ref in row['eitPolicyRefs']}
        self.assertTrue(excluded.isdisjoint(selected))
        for row in self.manifest['policies']:
            if row['reference'] in excluded:
                self.assertEqual('excluded', row['standardSelection'])
                self.assertNotIn('pro', row['targetEditions'])



if __name__ == '__main__':
    unittest.main()
