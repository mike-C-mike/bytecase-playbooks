"""Coach Mode questions for use / access / context.

Content consistency pass: answer choice length is intentionally balanced so
the safest response is not signaled by being longest.
"""

QUESTIONS = [{'id': 'use_context_novice_command_activity',
  'topic': 'Use / Access Context',
  'difficulty': 'Novice',
  'question': 'A command appears in an artifact on a computer. What is the safest first statement?',
  'choices': ['The account owner ran it. without corroborating artifacts or scope notes',
              'Command activity is supported by this source.',
              'The command proves intent.',
              'A single artifact is enough.'],
  'answer_index': 1,
  'explanation': 'The source may support that command activity existed, depending on artifact '
                 'meaning and reliability. Human actor identity requires additional context.',
  'follow_up': ['What account/session was active?',
                'Was remote access, automation, malware, or a shared account possible?',
                'What other artifacts align with the same time period?'],
  'guardrail': 'Device activity and human actor attribution are separate conclusions.',
  'related_scenario_id': 'command_seen_on_device',
  'search_terms': ['actor', 'command', 'attribution', 'user context']},
 {'id': 'use_context_experienced_password_control',
  'topic': 'Use / Access Context',
  'difficulty': 'Experienced',
  'question': 'A person says they are the only one who knows the device password. How should that '
              'be used?',
  'choices': ['As access/control context to weigh with other facts.',
              'As proof of every device action. without corroborating artifacts or scope notes',
              'As a reason to skip timeline work.',
              'As a substitute for source review.'],
  'answer_index': 0,
  'explanation': 'Exclusive password knowledge can support access or control context, especially '
                 'when combined with possession, session, and activity evidence. It does not '
                 'assign every artifact to that person.',
  'follow_up': ['Was the statement documented accurately?',
                'Who else had physical access or remote access?',
                'Do timestamps align with possession or use?'],
  'guardrail': 'Control indicators can strengthen attribution but do not replace corroboration.',
  'related_scenario_id': 'command_seen_on_device',
  'search_terms': ['password', 'control', 'possession', 'admission']},
 {'id': 'use_context_expert_shared_remote',
  'topic': 'Use / Access Context',
  'difficulty': 'Expert',
  'question': 'A suspicious action occurred under a named account on a shared or remotely '
              'accessible system. What is the best framing?',
  'choices': ['Name the account and separate actor identity from activity.',
              'Attribute the act to the account owner.',
              'Ignore the activity unless video exists.',
              'Treat remote access as impossible. without corroborating artifacts or scope notes'],
  'answer_index': 0,
  'explanation': 'On shared or remotely accessible systems, the account is an important lead but '
                 'not a complete human-actor conclusion. The better framing describes the '
                 'account/session evidence and the limits.',
  'follow_up': ['Were there RDP, remote support, scheduled task, or malware indicators?',
                'Was the device shared or unattended?',
                'Are there possession, camera, witness, or admission facts?'],
  'guardrail': 'A named account is attribution context, not human identity proof by itself.',
  'related_scenario_id': 'command_seen_on_device',
  'search_terms': ['shared account', 'remote access', 'actor', 'session']}]
