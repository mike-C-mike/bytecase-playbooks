"""ByteCase Playbooks glossary terms: mobile terms."""

TERMS = [{'term': 'Logical extraction',
  'category': 'Mobile',
  'definition': 'A mobile extraction that generally collects data available through normal device '
                'APIs, backups, or logical access methods.',
  'plain_language': 'A mobile extraction that generally collects data available through normal '
                    'device APIs, backups, or logical access methods.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'Logical extraction may omit app data, deleted data, or protected content depending '
               'on platform and tool support.',
  'related': ['File system extraction', 'Physical extraction', 'Extraction limitations'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'File system extraction',
  'category': 'Mobile',
  'definition': 'A mobile extraction that collects broader file system content when supported by '
                'the device, OS version, lock state, and tool.',
  'plain_language': 'A mobile extraction that collects broader file system content when supported '
                    'by the device, OS version, lock state, and tool.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': '',
  'related': ['Logical extraction', 'Mobile artifacts', 'Unsupported app'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'App artifact',
  'category': 'Mobile',
  'definition': 'Data associated with a mobile application, such as messages, media, settings, '
                'caches, databases, or logs.',
  'plain_language': 'Data associated with a mobile application, such as messages, media, settings, '
                    'caches, databases, or logs.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'A parsed app artifact should be reviewed with extraction type, app version, parser '
               'support, and context.',
  'related': ['Unsupported app', 'Parser output', 'Corroboration'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Cloud return',
  'category': 'Cloud / Mobile',
  'definition': 'Data returned from a cloud provider or account source under appropriate legal '
                'authority.',
  'plain_language': 'Data returned from a cloud provider or account source under appropriate legal '
                    'authority.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'Cloud data may differ from device-resident data and should be labeled by source.',
  'related': ['Scope', 'Account context', 'Source boundary'],
  'related_playbooks': [],
  'aliases': []}]
