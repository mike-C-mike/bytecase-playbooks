"""Coach Mode questions for mobile.

Content consistency pass: answer choice length is intentionally balanced so
the safest response is not signaled by being longest.
"""

QUESTIONS = [{'id': 'mobile_novice_message_actor',
  'topic': 'Mobile',
  'difficulty': 'Novice',
  'question': 'A message exists in a mobile extraction. What should be avoided without more '
              'context?',
  'choices': ['The extraction contains a message record.',
              'The app/source should be documented.',
              'The device owner typed it.',
              'Timestamps need review.'],
  'answer_index': 2,
  'explanation': 'A message artifact may show content and metadata in the extraction, but '
                 'authorship and physical device use need possession, access, account, admission, '
                 'or corroborating context.',
  'follow_up': ['What app/account produced the message?',
                'What extraction type and tool version were used?',
                'Is there possession or authentication context?'],
  'guardrail': 'A mobile artifact does not automatically prove who physically held or used the '
               'device.',
  'related_scenario_id': 'mobile_message_actor',
  'search_terms': ['mobile messages', 'authorship', 'actor']},
 {'id': 'mobile_experienced_extraction_differences',
  'topic': 'Mobile',
  'difficulty': 'Experienced',
  'question': 'Two extractions from the same phone show different artifact coverage. What should '
              'the examiner compare?',
  'choices': ['Extraction type, tool version, device state, and logs.',
              'Only the larger report. without corroborating artifacts or scope notes',
              'Assume one output is altered.',
              'Only screenshots from the tool.'],
  'answer_index': 0,
  'explanation': 'Logical, file system, physical, cloud, and manual workflows can produce '
                 'different coverage. Device lock state, OS version, app support, and tool '
                 'versions matter.',
  'follow_up': ['Were both extractions the same type?',
                'Was the device locked or unlocked?',
                'Do logs show unsupported apps or partial results?'],
  'guardrail': 'Different mobile outputs do not automatically mean one is false or altered.',
  'related_scenario_id': 'mobile_message_actor',
  'search_terms': ['mobile extraction', 'logical', 'filesystem', 'tool limits']},
 {'id': 'mobile_expert_cloud_boundary',
  'topic': 'Mobile',
  'difficulty': 'Expert',
  'question': 'A mobile matter includes device data and possible cloud account data. What boundary '
              'should be documented?',
  'choices': ['Device authority includes all cloud data.',
              'Device source, cloud source, authority, and time range.',
              'Cloud data should always be ignored. without corroborating artifacts or scope notes',
              'Cloud artifacts place the phone at the scene.'],
  'answer_index': 1,
  'explanation': 'Device extractions and cloud/account returns can represent different sources, '
                 'time ranges, authorities, and limitations. Keep them separated before comparing.',
  'follow_up': ['What authority covered each source?',
                'Are cloud records provider returns or synced local artifacts?',
                'Do timestamps use the same basis?'],
  'guardrail': 'Do not blur device evidence and cloud/account evidence without documenting source '
               'and scope.',
  'related_scenario_id': 'mobile_message_actor',
  'search_terms': ['cloud', 'mobile', 'source boundary', 'authority']}]
