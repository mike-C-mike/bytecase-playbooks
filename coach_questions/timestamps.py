"""Coach Mode questions for Timestamps.

Questions are intentionally judgment-focused. They reinforce careful
interpretation, documentation habits, and overclaim guardrails.
"""

QUESTIONS = [{'answer_index': 0,
  'choices': ['Whether the timestamp basis/time zone/source meaning is understood.',
              'Whether the timestamp looks recent.',
              'Whether the timestamp has seconds.',
              'Whether the file name is short.'],
  'difficulty': 'Novice',
  'explanation': 'Timestamps can use local time, UTC, filesystem semantics, database-specific meanings, or '
                 'tool-normalized values. Know what the timestamp represents before building a timeline.',
  'follow_up': ['Is it UTC or local time?',
                'What event does it represent: created, modified, accessed, parsed, sent, received, '
                'connected?',
                'Did the tool normalize it?'],
  'guardrail': 'A timestamp without source meaning can mislead timeline analysis.',
  'id': 'timestamps_novice_timezone',
  'question': 'A timestamp appears in a tool report. What should be checked before comparing it to other '
              'events?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['timestamp', 'timezone', 'timeline', 'UTC'],
  'topic': 'Timestamps'},
 {'answer_index': 1,
  'choices': ['Choose the time that helps the case theory.',
              'Document source meanings, time zones, clock skew, parser behavior, and possible explanations '
              'before forming a timeline statement.',
              'Ignore one artifact.',
              'Average the times.'],
  'difficulty': 'Experienced',
  'explanation': 'Conflicting timestamps require source-aware interpretation. Differences can come from '
                 'artifact semantics, time zones, clock changes, sync behavior, parser normalization, or '
                 'different stages of activity.',
  'follow_up': ['What does each timestamp represent?',
                'Was system time reliable?',
                'Are there independent timeline anchors?'],
  'guardrail': 'Do not force conflicting timestamps into a cleaner story than the data supports.',
  'id': 'timestamps_experienced_sequence',
  'question': 'Two artifacts show close but conflicting times for related activity. What is a careful '
              'response?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['timeline', 'clock skew', 'timestamp conflict', 'parser'],
  'topic': 'Timestamps'},
 {'answer_index': 0,
  'choices': ['Immediately calling it timestomping or anti-forensics.',
              'Checking system clock, artifact semantics, parser behavior, application behavior, and '
              'corroborating sources before naming a cause.',
              'Documenting the inconsistency.',
              'Looking for independent anchors.'],
  'difficulty': 'Expert',
  'explanation': 'Timestamp anomalies can have many causes. Anti-forensics is one possibility, but it should '
                 'not be asserted without supporting context and alternative explanations being considered.',
  'follow_up': ['Could clock drift, time zone conversion, sync, app behavior, or parser limits explain it?',
                'Are there event logs or external anchors?',
                'Is there other evidence of intentional manipulation?'],
  'guardrail': 'An anomalous timestamp is a question, not an automatic anti-forensics conclusion.',
  'id': 'timestamps_expert_anti_forensics',
  'question': 'A timestamp appears inconsistent with surrounding activity. What should an expert-level '
              'examiner avoid?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['timestomping', 'anti-forensics', 'timestamp anomaly', 'clock'],
  'topic': 'Timestamps'}]
