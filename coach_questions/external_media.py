"""Coach Mode questions for external / media.

Content consistency pass: answer choice length is intentionally balanced so
the safest response is not signaled by being longest.
"""

QUESTIONS = [{'id': 'external_media_novice_connection',
  'topic': 'External Media',
  'difficulty': 'Novice',
  'question': 'Windows artifacts show a removable device was connected. What does that support '
              'first?',
  'choices': ['Device connection or recognition context.',
              'Confirmed file copying. without corroborating artifacts or scope notes',
              'The human who connected it.',
              'The contents of the device.'],
  'answer_index': 0,
  'explanation': 'Connection artifacts can support that a device was recognized or installed. File '
                 'movement and actor identity require separate evidence.',
  'follow_up': ['Can the device be identified by serial or volume information?',
                'Do file-access artifacts reference removable paths?',
                'What user/session context overlaps the connection?'],
  'guardrail': 'Connection is not transfer, and transfer is not human attribution.',
  'related_scenario_id': 'usb_connected_question',
  'search_terms': ['USB', 'external media', 'connection']},
 {'id': 'external_media_experienced_transfer',
  'topic': 'External Media',
  'difficulty': 'Experienced',
  'question': 'Which artifacts are useful when asking whether files moved to or from removable '
              'media?',
  'choices': ['Only the device friendly name. without corroborating artifacts or scope notes',
              'LNK, Jump Lists, paths, timestamps, and media contents.',
              'Only the monitor serial number.',
              'Only the drive letter by itself.'],
  'answer_index': 1,
  'explanation': 'Possible transfer is a correlation question. The stronger review combines '
                 'connection data, file-reference artifacts, source/destination paths, timestamps, '
                 'and media contents when available.',
  'follow_up': ['Are the same files present on source and destination?',
                'Do shell artifacts reference removable paths?',
                'Do connection times overlap file activity?'],
  'guardrail': 'Do not describe copying unless supporting artifacts align.',
  'related_scenario_id': 'usb_connected_question',
  'search_terms': ['file transfer', 'Shellbags', 'LNK', 'Jump Lists']},
 {'id': 'external_media_expert_actor',
  'topic': 'External Media',
  'difficulty': 'Expert',
  'question': 'A USB device was connected during a user logon session. What should be considered '
              'before attributing the action?',
  'choices': ['Logon context, possession, remote access, and timing.',
              'The drive letter alone identifies the actor.',
              'Connection time proves keyboard use.',
              'No further context can help. without corroborating artifacts or scope notes'],
  'answer_index': 0,
  'explanation': 'User/session context can support attribution, but shared accounts, remote '
                 'access, unattended systems, and automation can complicate who connected or used '
                 'the device.',
  'follow_up': ['Was the system physically controlled by one person?',
                'Were remote sessions active?',
                'Do other artifacts show activity from the same profile?'],
  'guardrail': 'A connection timestamp plus account context is still not automatic human-actor '
               'proof.',
  'related_scenario_id': 'usb_connected_question',
  'search_terms': ['USB attribution', 'session', 'possession']}]
