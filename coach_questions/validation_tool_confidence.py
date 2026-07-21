"""Coach Mode questions for validation / tool / confidence.

Content consistency pass: answer choice length is intentionally balanced so
the safest response is not signaled by being longest.
"""

QUESTIONS = [{'id': 'validation_novice_tool_output',
  'topic': 'Validation / Tool Confidence',
  'difficulty': 'Novice',
  'question': 'A forensic tool produces a parsed result. What should the examiner remember?',
  'choices': ['Tool output replaces judgment. without corroborating artifacts or scope notes',
              'Parsed results are aids requiring review.',
              'All parsed fields are final findings.',
              'Screenshots validate the parser.'],
  'answer_index': 1,
  'explanation': 'Tool output is useful, but important results should be reviewed against source '
                 'context, tool documentation, known limitations, and corroborating artifacts '
                 'where needed.',
  'follow_up': ['What artifact was parsed?',
                'What tool and version were used?',
                'Is source-level review needed?'],
  'guardrail': 'Tool output is not a substitute for examiner judgment.',
  'related_scenario_id': 'command_seen_on_device',
  'search_terms': ['tool output', 'parser', 'validation']},
 {'id': 'validation_experienced_local_check',
  'topic': 'Validation / Tool Confidence',
  'difficulty': 'Experienced',
  'question': 'Before relying on an important tool feature, what validation mindset is safest?',
  'choices': ['Vendor claims are enough. without corroborating artifacts or scope notes',
              'Use local records, known data, and limitations.',
              'Skip checks for common tools.',
              'Only public tests matter.'],
  'answer_index': 1,
  'explanation': 'Local validation records help document tool/version/environment behavior for the '
                 'specific function being used. Public tests and vendor documentation can inform '
                 'the review but do not replace local confidence.',
  'follow_up': ['Has this function been tested locally?',
                'Was the same version and environment used?',
                'Are limitations documented?'],
  'guardrail': 'Tool confidence should be tied to function, version, environment, and documented '
               'testing.',
  'related_scenario_id': 'command_seen_on_device',
  'search_terms': ['validation', 'known data', 'tool confidence']},
 {'id': 'validation_expert_parser_disagreement',
  'topic': 'Validation / Tool Confidence',
  'difficulty': 'Expert',
  'question': 'Two tools parse the same artifact differently. What is the best next step?',
  'choices': ['Use the nicer report. without corroborating artifacts or scope notes',
              'Assume the paid tool is correct.',
              'Review source data, docs, versions, and limits.',
              'Ignore the disagreement.'],
  'answer_index': 2,
  'explanation': 'Parser disagreement should be handled transparently. Review source data, '
                 'artifact meaning, tool versions, known limitations, and known-good tests where '
                 'needed.',
  'follow_up': ['Are tools parsing the same source?',
                'Do docs explain the field differently?',
                'Can known-good data reproduce the behavior?'],
  'guardrail': 'Parser disagreement is a finding to investigate, not something to hide or '
               'simplify.',
  'related_scenario_id': 'command_seen_on_device',
  'search_terms': ['parser disagreement', 'tool version', 'validation']}]
