"""Coach Mode questions for Mobile.

Questions are intentionally judgment-focused. They reinforce careful
interpretation, documentation habits, and overclaim guardrails.
"""

QUESTIONS = [{'answer_index': 2,
  'choices': ['The extraction contains a message record.',
              'The message content, direction, app, timestamp, and source should be documented.',
              'A specific person physically typed or read the message.',
              'Related account/device context may matter.'],
  'difficulty': 'Novice',
  'explanation': 'A message artifact may show content and metadata in the extraction, but the human actor '
                 'may require device possession, account control, lock state, app/session context, '
                 'admissions, or corroboration.',
  'follow_up': ['Was the device in the person’s possession?',
                'Who knew the passcode or controlled the account?',
                'Does app/account data support who used it?'],
  'guardrail': 'A mobile artifact does not automatically prove who physically held or used the device.',
  'id': 'mobile_novice_message_actor',
  'question': 'A message exists in a mobile extraction. What should be avoided without more context?',
  'related_playbook_id': 'mobile_device_extraction',
  'related_scenario_id': 'mobile_message_actor',
  'search_terms': ['mobile', 'message', 'actor', 'possession', 'passcode'],
  'topic': 'Mobile'},
 {'answer_index': 1,
  'choices': ['Only the larger extraction matters.',
              'Extraction type, tool/version, device state, supported apps, limitations, and why outputs may '
              'differ.',
              'The smaller extraction is wrong.',
              'Different outputs prove tampering.'],
  'difficulty': 'Experienced',
  'explanation': 'Logical, file system, physical, cloud, and manual workflows can produce different artifact '
                 'coverage. Document extraction type and limitations before comparing outputs.',
  'follow_up': ['What extraction types were performed?',
                'What tool/version and device OS were involved?',
                'Which apps or databases were unsupported or partially parsed?'],
  'guardrail': 'Different mobile extraction outputs do not automatically mean one is false or altered.',
  'id': 'mobile_experienced_extraction_type',
  'question': 'Two mobile extractions from the same device show different artifact coverage. What should the '
              'examiner document?',
  'related_playbook_id': 'mobile_device_extraction',
  'related_scenario_id': 'mobile_message_actor',
  'search_terms': ['mobile extraction', 'logical', 'file system', 'limitations'],
  'topic': 'Mobile'},
 {'answer_index': 1,
  'choices': ['Device authority always includes all cloud data.',
              'Separate device extraction scope from cloud/account-return authority, source, timing, and '
              'limitations.',
              'Cloud data should be treated as live device data.',
              'Cloud artifacts prove the phone was present.'],
  'difficulty': 'Expert',
  'explanation': 'Cloud/account returns and device extractions can represent different sources, time ranges, '
                 'sync states, and legal authorities. Keep source and authority boundaries clear.',
  'follow_up': ['What authority covered the device vs account/cloud source?',
                'What time range did each source cover?',
                'Were records synced, server-side, cached, or locally stored?'],
  'guardrail': 'Do not blur device evidence and cloud/account evidence without documenting source and '
               'authority.',
  'id': 'mobile_expert_cloud_device_boundary',
  'question': 'A mobile investigation includes device data and possible cloud account data. What boundary '
              'should be kept clear?',
  'related_playbook_id': 'mobile_device_extraction',
  'related_scenario_id': 'mobile_message_actor',
  'search_terms': ['cloud', 'mobile', 'authority', 'sync', 'account'],
  'topic': 'Mobile'}]
