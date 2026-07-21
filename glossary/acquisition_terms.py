"""ByteCase Playbooks glossary terms: acquisition terms."""

TERMS = [{'term': 'Live acquisition',
  'category': 'Acquisition',
  'definition': 'Collection from a powered-on system. It may preserve volatile state but also '
                'changes the system and requires careful documentation and scope control.',
  'plain_language': 'Collection from a powered-on system. It may preserve volatile state but also '
                    'changes the system and requires careful documentation and scope control.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': '',
  'related': ['RAM capture', 'Volatile data', 'Network isolation', 'Encryption context'],
  'related_playbooks': ['Live Computer Acquisition / RAM Capture'],
  'aliases': []},
 {'term': 'Dead-box imaging',
  'category': 'Imaging',
  'definition': 'Preservation of storage media when the device is powered off or the storage media '
                'is removed and handled through a controlled imaging process.',
  'plain_language': 'Preservation of storage media when the device is powered off or the storage '
                    'media is removed and handled through a controlled imaging process.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': '',
  'related': ['Write blocker', 'Forensic image', 'Hash verification'],
  'related_playbooks': ['Dead-Box Computer Imaging'],
  'aliases': []},
 {'term': 'Forensic image',
  'category': 'Acquisition',
  'definition': 'A documented acquisition of storage media or selected data created for later '
                'examination.',
  'plain_language': 'A documented acquisition of storage media or selected data created for later '
                    'examination.',
  'why_it_matters': '',
  'common_examples': ['E01 image', 'RAW/dd image', 'Logical container export'],
  'guardrail': 'Image format and scope matter; an image is not automatically complete for every '
               'possible evidence question.',
  'related': ['Dead-box imaging', 'Hash verification', 'Write blocker'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Write blocker',
  'category': 'Preservation',
  'definition': 'A hardware, software, or process control used to reduce or prevent writes to '
                'source media during acquisition.',
  'plain_language': 'A hardware, software, or process control used to reduce or prevent writes to '
                    'source media during acquisition.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'A write blocker should be locally validated and documented.',
  'related': ['ByteCase Validate', 'Dead-box imaging', 'External media'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Targeted collection',
  'category': 'Acquisition',
  'definition': 'Collection of selected files, folders, logs, or exports instead of a full '
                'physical or logical image.',
  'plain_language': 'Collection of selected files, folders, logs, or exports instead of a full '
                    'physical or logical image.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'Targeted collection can be valid when scoped, but it may omit artifacts outside '
               'the target.',
  'related': ['Scope', 'Logical collection', 'Limitations'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Volatile data',
  'category': 'Memory',
  'definition': 'Data that can change or disappear quickly, especially on a powered-on system.',
  'plain_language': 'Data that can change or disappear quickly, especially on a powered-on system.',
  'why_it_matters': '',
  'common_examples': ['RAM',
                      'Running processes',
                      'Network connections',
                      'Logged-in users',
                      'Mounted volumes'],
  'guardrail': '',
  'related': ['Live acquisition', 'RAM capture', 'Memory analysis'],
  'related_playbooks': [],
  'aliases': []}]
