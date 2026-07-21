"""ByteCase Playbooks glossary terms: core terms."""

TERMS = [{'term': 'Field Reference Mode',
  'category': 'Playbooks',
  'definition': 'A shorter view meant for real-time reference during a task. It emphasizes order, '
                'documentation, cautions, and quick reminders.',
  'plain_language': 'A shorter view meant for real-time reference during a task. It emphasizes '
                    'order, documentation, cautions, and quick reminders.',
  'why_it_matters': 'This mode keeps the examiner focused on what to consider now without turning '
                    'the screen into a training course.',
  'common_examples': [],
  'guardrail': '',
  'related': ['Learning / Refresher Mode', 'Step card', 'Boundary notice'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Learning / Refresher Mode',
  'category': 'Playbooks',
  'definition': 'A deeper view meant for downtime learning or refreshers before performing '
                'less-common work. It expands the why, tools, artifacts, cautions, and '
                'documentation reminders.',
  'plain_language': 'A deeper view meant for downtime learning or refreshers before performing '
                    'less-common work. It expands the why, tools, artifacts, cautions, and '
                    'documentation reminders.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': '',
  'related': ['Field Reference Mode', 'Step card', 'Examiner judgment'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Artifact',
  'category': 'Analysis',
  'definition': 'A data item or record that may help answer a forensic question. Artifact '
                'presence, absence, or parser output must be interpreted in context.',
  'plain_language': 'A data item or record that may help answer a forensic question. Artifact '
                    'presence, absence, or parser output must be interpreted in context.',
  'why_it_matters': '',
  'common_examples': ['Browser history record',
                      'LNK file',
                      'Message database record',
                      'Event log entry',
                      'Memory plugin output'],
  'guardrail': 'Artifact presence does not automatically prove intent, identity, knowledge, or '
               'relevance.',
  'related': ['ByteCase Notes', 'Artifact index', 'Corroboration'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Overclaim',
  'category': 'Reporting',
  'definition': 'A statement that goes beyond what the artifact, tool output, or available context '
                'supports.',
  'plain_language': 'A statement that goes beyond what the artifact, tool output, or available '
                    'context supports.',
  'why_it_matters': 'Avoiding overclaim keeps reports defensible and clearer.',
  'common_examples': ['Saying a suspect typed a command based only on command history',
                      'Saying a file was viewed based only on download evidence'],
  'guardrail': '',
  'related': ['Limitations', 'Corroboration', 'Examiner judgment'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Corroboration',
  'category': 'Analysis',
  'definition': 'The practice of checking whether an observation is supported by another artifact, '
                'source, timestamp, log, tool output, or case context before relying on it '
                'heavily.',
  'plain_language': 'The practice of checking whether an observation is supported by another '
                    'artifact, source, timestamp, log, tool output, or case context before relying '
                    'on it heavily.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': '',
  'related': ['Overclaim', 'Limitations', 'Artifact'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Limitations',
  'category': 'Reporting',
  'definition': 'Known boundaries of the tool, data source, extraction type, parser support, '
                'authority, or examiner process.',
  'plain_language': 'Known boundaries of the tool, data source, extraction type, parser support, '
                    'authority, or examiner process.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'Limitations should be documented instead of hidden.',
  'related': ['Overclaim', 'Tool validation', 'Unsupported app'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Does not prove',
  'category': 'Reporting',
  'definition': 'A guardrail reminder that a tool result or artifact can support a lead without '
                'proving attribution, intent, or a final conclusion by itself.',
  'plain_language': 'A guardrail reminder that a tool result or artifact can support a lead '
                    'without proving attribution, intent, or a final conclusion by itself.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': '',
  'related': ['Overclaim', 'Corroboration', 'Limitations'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Device-use context',
  'category': 'Attribution',
  'definition': 'Information that helps evaluate who may have had access to or control over a '
                'device, account, session, or action.',
  'plain_language': 'Information that helps evaluate who may have had access to or control over a '
                    'device, account, session, or action.',
  'why_it_matters': '',
  'common_examples': ['Password knowledge',
                      'Possession',
                      'Account ownership',
                      'Logged-in sessions',
                      'Admissions',
                      'Witness/camera context'],
  'guardrail': 'Control context supports interpretation, but should still be documented accurately '
               'and weighed with other evidence.',
  'related': ['Actor vs. artifact', 'Corroboration', 'Overclaim'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Actor vs. artifact',
  'category': 'Attribution',
  'definition': 'A reminder to separate what a digital artifact shows from who performed the '
                'related human action.',
  'plain_language': 'A reminder to separate what a digital artifact shows from who performed the '
                    'related human action.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'A command, file access trace, login artifact, or app record may support activity, '
               'but the human actor usually requires additional context.',
  'related': ['Device-use context', 'Does not prove', 'Limitations'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Examiner judgment',
  'category': 'Playbooks',
  'definition': 'The trained human evaluation of scope, artifacts, tool limits, context, and '
                'corroboration.',
  'plain_language': 'The trained human evaluation of scope, artifacts, tool limits, context, and '
                    'corroboration.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'ByteCase Playbooks supports judgment; it does not replace it.',
  'related': ['Overclaim', 'Limitations', 'Corroboration'],
  'related_playbooks': [],
  'aliases': []}]
