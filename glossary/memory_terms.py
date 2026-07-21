"""ByteCase Playbooks glossary terms: memory terms."""

TERMS = [{'term': 'RAM capture',
  'category': 'Memory',
  'definition': 'Collection of system memory from a live machine. RAM can contain volatile '
                'process, connection, command-line, session, and encryption-related context.',
  'plain_language': 'Collection of system memory from a live machine. RAM can contain volatile '
                    'process, connection, command-line, session, and encryption-related context.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': '',
  'related': ['Volatility', 'Volatile data', 'Live acquisition'],
  'related_playbooks': ['Live Computer Acquisition / RAM Capture',
                        'Memory / RAM Analysis Refresher'],
  'aliases': []},
 {'term': 'Volatility',
  'category': 'Memory',
  'definition': 'A memory forensics framework commonly used to examine memory images. Plugin '
                'output should be reviewed in context and documented as tool output, not as an '
                'automatic conclusion.',
  'plain_language': 'A memory forensics framework commonly used to examine memory images. Plugin '
                    'output should be reviewed in context and documented as tool output, not as an '
                    'automatic conclusion.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': '',
  'related': ['windows.info',
              'windows.pslist',
              'windows.pstree',
              'windows.netscan',
              'windows.malfind'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Process tree',
  'category': 'Memory',
  'definition': 'A parent-child view of running or recovered processes that can help show '
                'execution relationships.',
  'plain_language': 'A parent-child view of running or recovered processes that can help show '
                    'execution relationships.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'A process relationship is context, not proof of user intent or malware by itself.',
  'related': ['pslist', 'pstree', 'cmdline'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Network connection',
  'category': 'Memory',
  'definition': 'A record or observation of local/remote network activity associated with a '
                'process or system state.',
  'plain_language': 'A record or observation of local/remote network activity associated with a '
                    'process or system state.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'An IP address or connection does not prove attribution, compromise, or intent by '
               'itself.',
  'related': ['netscan', 'Process', 'Timestamp'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Malfind-style output',
  'category': 'Memory',
  'definition': 'Memory analysis output that may flag injected or suspicious memory regions for '
                'review.',
  'plain_language': 'Memory analysis output that may flag injected or suspicious memory regions '
                    'for review.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'Suspicious memory output is a lead. It does not independently prove malware '
               'without additional analysis.',
  'related': ['Volatility', 'malfind', 'Corroboration'],
  'related_playbooks': [],
  'aliases': []}]
