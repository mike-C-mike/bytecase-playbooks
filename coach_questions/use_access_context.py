"""Coach Mode questions for Use / Access Context.

Questions are intentionally judgment-focused. They reinforce careful
interpretation, documentation habits, and overclaim guardrails.
"""

QUESTIONS = [{'answer_index': 1,
  'choices': ['The suspect typed the command.',
              'The command appears in the reviewed artifact and needs user/session context.',
              'The account owner definitely ran it.',
              'The command proves intent.'],
  'difficulty': 'Novice',
  'explanation': 'The artifact may support that command activity was present in the source you reviewed. It '
                 'does not, by itself, identify the human actor. Start with what the artifact shows, then '
                 'look for access, possession, session, credential, admission, or corroborating context.',
  'follow_up': ['Which account/session was active?',
                'Could remote access, automation, malware, or another person explain it?',
                'Is there possession, password, admission, camera, witness, or timeline context?'],
  'guardrail': 'Activity on a device is not the same as proof of the person who performed it.',
  'id': 'use_context_novice_command_actor',
  'question': 'A command appears in an artifact on a computer. What is the safest first conclusion?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['command', 'actor', 'attribution', 'session', 'password'],
  'topic': 'Use / Access Context'},
 {'answer_index': 1,
  'choices': ['As proof they performed every action on the device.',
              'As useful access/control context that still needs to be weighed with other evidence.',
              'As irrelevant because only artifacts matter.',
              'As proof all device contents belong to them.'],
  'difficulty': 'Experienced',
  'explanation': 'Exclusive password knowledge may support access or control over a device, especially when '
                 'paired with possession and account/session artifacts. It does not prove every action, '
                 'file, message, or command was performed by that person.',
  'follow_up': ['Who had physical possession?',
                'Was the device locked, unlocked, or actively logged in?',
                'Do timestamps, accounts, communications, or witnesses support control at relevant times?'],
  'guardrail': 'Control evidence can support attribution analysis, but it does not replace corroboration.',
  'id': 'use_context_experienced_password_control',
  'question': 'A person says they are the only one who knows the device password. How should that statement '
              'be used?',
  'related_playbook_id': 'mobile_device_extraction',
  'related_scenario_id': 'mobile_message_actor',
  'search_terms': ['password', 'control', 'admission', 'access', 'possession'],
  'topic': 'Use / Access Context'},
 {'answer_index': 2,
  'choices': ['Attribute the action to the account owner because the account name appears.',
              'Ignore the account artifact because shared devices are impossible to analyze.',
              'Separate account activity from human attribution and build a timeline using session, '
              'possession, remote access, credential, and corroborating evidence.',
              'State that malware must have performed the action.'],
  'difficulty': 'Expert',
  'explanation': 'On shared, family, workplace, or remotely accessible systems, attribution needs layered '
                 'context. Account artifacts matter, but they should be evaluated with logon type, remote '
                 'sessions, physical possession, credential knowledge, device location, other user activity, '
                 'witness/camera context, and possible automation or malware.',
  'follow_up': ['Was the logon local, remote, cached, service-based, or automated?',
                'Who had access to the device and credentials?',
                'Do unrelated artifacts place a specific person at the device near the relevant time?'],
  'guardrail': 'A named account is an attribution lead, not human-actor proof by itself.',
  'id': 'use_context_expert_remote_shared_device',
  'question': 'A suspicious action occurred under a named account on a shared or remotely accessible device. '
              'What is the strongest careful approach?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['account', 'remote access', 'shared device', 'attribution', 'logon'],
  'topic': 'Use / Access Context'}]
