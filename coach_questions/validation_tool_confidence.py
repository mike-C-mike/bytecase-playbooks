"""Coach Mode questions for Validation / Tool Confidence.

Questions are intentionally judgment-focused. They reinforce careful
interpretation, documentation habits, and overclaim guardrails.
"""

QUESTIONS = [{'answer_index': 1,
  'choices': ['Tool output replaces examiner judgment.',
              'The output should be reviewed with source, tool/version, settings, limitations, and '
              'validation awareness.',
              'No documentation is needed if the result looks right.',
              'The tool vendor is responsible for all conclusions.'],
  'difficulty': 'Novice',
  'explanation': 'Tool output is a useful aid, but it needs examiner review. Important results should be '
                 'documented with tool/version, source, settings, and any known limitations or validation '
                 'context.',
  'follow_up': ['What source data was parsed?',
                'What tool and version produced the result?',
                'Is the relevant function validated or corroborated?'],
  'guardrail': 'Tool output is not a substitute for examiner judgment.',
  'id': 'validation_novice_tool_output',
  'question': 'A forensic tool produces a parsed result. What should the examiner remember?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['tool output', 'validation', 'version', 'limitations'],
  'topic': 'Validation / Tool Confidence'},
 {'answer_index': 1,
  'choices': ['A public test or vendor claim means local checking is unnecessary.',
              'Use known test data/processes to document that this tool/version/environment behaves as '
              'expected for the function being relied on.',
              'Only validate tools after a case is challenged.',
              'Validation is only for lab managers.'],
  'difficulty': 'Experienced',
  'explanation': 'Local validation records help document tool/version/environment behavior. Public tests and '
                 'vendor docs can inform the process, but they do not replace local awareness of the exact '
                 'setup being used.',
  'follow_up': ['What function are you relying on?',
                'What known test can demonstrate expected behavior?',
                'Where is the validation record stored?'],
  'guardrail': 'Tool confidence should be tied to the function, version, environment, and record of testing.',
  'id': 'validation_experienced_known_test',
  'question': 'Before relying on a tool feature for an important task, what local validation mindset is '
              'appropriate?',
  'related_playbook_id': 'memory_ram_analysis_volatility',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['validation', 'known test', 'tool version', 'environment'],
  'topic': 'Validation / Tool Confidence'},
 {'answer_index': 1,
  'choices': ['Pick the tool with the nicer report.',
              'Compare source data, tool versions, parser settings, documentation, known limitations, and '
              'manual/alternate validation where practical.',
              'Assume the commercial tool is always right.',
              'Delete the conflicting result.'],
  'difficulty': 'Expert',
  'explanation': 'Parser disagreement should be handled transparently. The examiner should understand source '
                 'data, parser assumptions, version behavior, time conversion, and whether another method '
                 'can clarify the issue.',
  'follow_up': ['Are both tools parsing the same source bytes?',
                'Do they define fields or timestamps differently?',
                'Can the artifact be manually reviewed or checked with a known reference?'],
  'guardrail': 'Parser disagreement is a finding to investigate, not something to hide or simplify.',
  'id': 'validation_expert_parser_disagreement',
  'question': 'Two tools parse the same artifact differently. What is the best next step?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['parser disagreement', 'tool validation', 'manual review', 'limitations'],
  'topic': 'Validation / Tool Confidence'}]
