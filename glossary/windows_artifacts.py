"""ByteCase Playbooks glossary terms: windows artifacts."""

TERMS = [{'term': 'LNK file',
  'category': 'Windows Artifacts',
  'definition': 'A shortcut artifact that may provide context about file paths, volumes, '
                'timestamps, and user interaction patterns.',
  'plain_language': 'A shortcut artifact that may provide context about file paths, volumes, '
                    'timestamps, and user interaction patterns.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'A shortcut can support interaction context but does not prove the named person '
               'opened the file.',
  'related': ['Recent files', 'Jump Lists', 'File access'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Jump List',
  'category': 'Windows Artifacts',
  'definition': 'A Windows artifact that can record recent or frequent file/application '
                'interaction for supported applications.',
  'plain_language': 'A Windows artifact that can record recent or frequent file/application '
                    'interaction for supported applications.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'Jump List entries require context and should be corroborated with other artifacts '
               'when making strong claims.',
  'related': ['LNK file', 'Recent files', 'User activity'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Prefetch',
  'category': 'Windows Artifacts',
  'definition': 'A Windows artifact that can indicate program execution on supported systems.',
  'plain_language': 'A Windows artifact that can indicate program execution on supported systems.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'Program execution does not identify who initiated the program by itself.',
  'related': ['Program execution', 'Windows artifact review'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Registry artifact',
  'category': 'Windows Artifacts',
  'definition': 'Configuration and activity data stored in Windows registry hives that may support '
                'user, device, program, and system context.',
  'plain_language': 'Configuration and activity data stored in Windows registry hives that may '
                    'support user, device, program, and system context.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'Registry artifacts vary by Windows version, configuration, and acquisition scope.',
  'related': ['USB history', 'UserAssist', 'Mounted devices'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Event log',
  'category': 'Windows Artifacts',
  'definition': 'A Windows log source that can provide system, security, application, logon, '
                'service, and device-related records.',
  'plain_language': 'A Windows log source that can provide system, security, application, logon, '
                    'service, and device-related records.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'An event log record should be interpreted based on event ID, source, logging '
               'configuration, and surrounding context.',
  'related': ['Timestamps', 'Logon event', 'USB connection'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'USBSTOR',
  'category': 'Windows Artifacts',
  'definition': 'A Windows registry area commonly associated with USB storage device history.',
  'plain_language': 'A Windows registry area commonly associated with USB storage device history.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'USB connection artifacts do not prove file transfer or identify the human actor by '
               'themselves.',
  'related': ['USB connection', 'SetupAPI', 'External media'],
  'related_playbooks': [],
  'aliases': []}]
