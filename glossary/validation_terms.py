"""ByteCase Playbooks glossary terms: validation terms."""

TERMS = [{'term': 'Hash verification',
  'category': 'Integrity',
  'definition': 'A process for checking whether data matches a previously recorded hash value. '
                'Hashes support integrity checks; they do not interpret content or user intent.',
  'plain_language': 'A process for checking whether data matches a previously recorded hash value. '
                    'Hashes support integrity checks; they do not interpret content or user '
                    'intent.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': '',
  'related': ['ByteCase Verify', 'SHA-256', 'MD5', 'Manifest'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Tool validation',
  'category': 'Validation',
  'definition': 'Local documentation that a tool, device, or process behaved as expected for a '
                'known test in a specific environment.',
  'plain_language': 'Local documentation that a tool, device, or process behaved as expected for a '
                    'known test in a specific environment.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'Validation supports confidence in a process; it does not certify all future '
               'results in all environments.',
  'related': ['ByteCase Validate', 'Limitations', 'Retest'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Reference method',
  'category': 'Validation',
  'definition': 'A second tool, source, known dataset, or expected result used to compare behavior '
                'during validation.',
  'plain_language': 'A second tool, source, known dataset, or expected result used to compare '
                    'behavior during validation.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': '',
  'related': ['Tool validation', 'Known test data', 'Corroboration'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Known test data',
  'category': 'Validation',
  'definition': 'Data with expected properties or results used to test tool behavior.',
  'plain_language': 'Data with expected properties or results used to test tool behavior.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': '',
  'related': ['Reference method', 'Tool validation'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Command example',
  'category': 'Playbooks',
  'definition': 'A sample command or tool action shown as a learning/reference prompt.',
  'plain_language': 'A sample command or tool action shown as a learning/reference prompt.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'Commands must be adapted to the examiner’s tool path, image name, case scope, '
               'agency policy, and operating environment.',
  'related': ['Volatility', 'Documentation', 'Limitations'],
  'related_playbooks': [],
  'aliases': []}]
