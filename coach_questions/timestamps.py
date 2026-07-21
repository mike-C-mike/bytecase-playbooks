"""Coach Mode questions for timestamps.

Content consistency pass: answer choice length is intentionally balanced so
the safest response is not signaled by being longest.
"""

QUESTIONS = [{'id': 'timestamps_novice_source_meaning',
  'topic': 'Timestamps',
  'difficulty': 'Novice',
  'question': 'A timestamp appears in a tool report. What should be checked before comparing it to '
              'other times?',
  'choices': ['Timestamp basis, source meaning, and time zone.',
              'Whether it supports the case theory.',
              'Only the displayed local time. without corroborating artifacts or scope notes',
              'Whether it is the newest timestamp.'],
  'answer_index': 0,
  'explanation': 'Timestamps can use UTC, local time, filesystem semantics, database-specific '
                 'meanings, or tool conversions. Source meaning should be understood before '
                 'timeline comparison.',
  'follow_up': ['What artifact produced the timestamp?',
                'Does the tool convert time zones?',
                'What was the system clock/time zone?'],
  'guardrail': 'A timestamp without source meaning can mislead timeline analysis.',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['timestamp', 'time zone', 'timeline']},
 {'id': 'timestamps_experienced_conflict',
  'topic': 'Timestamps',
  'difficulty': 'Experienced',
  'question': 'Two sources show close but conflicting times. What is the careful response?',
  'choices': ['Choose the time that fits best.',
              'Document source meaning and possible causes.',
              'Hide the weaker timestamp. without corroborating artifacts or scope notes',
              'Treat both as the same event.'],
  'answer_index': 1,
  'explanation': 'Conflicts can come from different event meanings, time bases, clock skew, parser '
                 'behavior, sync, extraction, or copy activity. Document the basis before '
                 'resolving.',
  'follow_up': ['Are the timestamps measuring the same event?',
                'Are time zones or clock drift involved?',
                'Do independent sources support one interpretation?'],
  'guardrail': 'Do not force conflicting timestamps into a cleaner story than the data supports.',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['timeline conflict', 'clock skew', 'parser']},
 {'id': 'timestamps_expert_anomaly',
  'topic': 'Timestamps',
  'difficulty': 'Expert',
  'question': 'A timestamp appears inconsistent with surrounding activity. What should an '
              'expert-level review avoid?',
  'choices': ['Calling it anti-forensics without support.',
              'Checking copy or sync behavior.',
              'Reviewing parser documentation.',
              'Documenting uncertainty. without corroborating artifacts or scope notes'],
  'answer_index': 0,
  'explanation': 'Timestamp anomalies can have many causes. Anti-forensics is one possible '
                 'explanation, but it should not be asserted without supporting context and '
                 'alternatives being considered.',
  'follow_up': ['Could copying, extraction, sync, or filesystem behavior explain it?',
                'Do other artifacts show the same anomaly?',
                'Is known-good testing needed?'],
  'guardrail': 'An anomalous timestamp is a question, not an automatic anti-forensics conclusion.',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['timestomp', 'anti-forensics', 'timestamp anomaly']}]
