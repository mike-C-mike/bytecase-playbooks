"""Coach Mode questions for External Media.

Questions are intentionally judgment-focused. They reinforce careful
interpretation, documentation habits, and overclaim guardrails.
"""

QUESTIONS = [{'answer_index': 0,
  'choices': ['A USB/external device was connected or recognized, depending on the artifact.',
              'Files were definitely copied.',
              'The suspect connected it.',
              'The drive contents were viewed.'],
  'difficulty': 'Novice',
  'explanation': 'Connection artifacts can help document that a device was connected or recognized. File '
                 'transfer, viewing, or human actor identity require other supporting artifacts and context.',
  'follow_up': ['What device identifiers were recorded?',
                'What user/session was active?',
                'Are there file access/copy artifacts tied to that device?'],
  'guardrail': 'Connection is not transfer, and transfer is not actor identity.',
  'id': 'external_media_novice_connected',
  'question': 'USB artifacts show a drive was connected. What does that support most directly?',
  'related_playbook_id': 'external_media_hash_copy_refresher',
  'related_scenario_id': 'usb_connected_question',
  'search_terms': ['USB', 'external media', 'connection', 'transfer'],
  'topic': 'External Media'},
 {'answer_index': 1,
  'choices': ['Only the USB vendor name.',
              'USB connection data plus LNK/Jump Lists, shellbags, file paths, timestamps, copy tool logs, '
              'and user/session context.',
              'Only the capacity of the drive.',
              'Only whether the drive letter is common.'],
  'difficulty': 'Experienced',
  'explanation': 'Transfer questions usually require more than connection artifacts. Look for path-based '
                 'file activity, shell/application artifacts, timestamps, and context tying activity to the '
                 'device and session.',
  'follow_up': ['Do file paths reference removable drive letters or volume identifiers?',
                'Do access artifacts occur near the connection window?',
                'What user profile or session produced the artifacts?'],
  'guardrail': 'Do not claim file transfer based only on device connection records.',
  'id': 'external_media_experienced_transfer',
  'question': 'You need to evaluate whether files may have moved to or from USB media. Which set of '
              'artifacts is more helpful?',
  'related_playbook_id': 'external_media_hash_copy_refresher',
  'related_scenario_id': 'usb_connected_question',
  'search_terms': ['USB transfer', 'LNK', 'Jump List', 'shellbags', 'copy'],
  'topic': 'External Media'},
 {'answer_index': 1,
  'choices': ['Treat all removable-drive artifacts as one device.',
              'Map identifiers, volume serials, friendly names, drive letters, connection windows, and '
              'file-path artifacts to avoid mixing devices.',
              'Use the largest drive as the likely source.',
              'Ignore timestamps because drive letters change.'],
  'difficulty': 'Expert',
  'explanation': 'Drive letters can change and multiple devices can have similar names. Use identifiers and '
                 'time windows to connect specific media to specific activity while documenting uncertainty.',
  'follow_up': ['Which identifiers uniquely distinguish each device?',
                'Did drive letters change over time?',
                'Are file paths tied to a specific volume or only a temporary drive letter?'],
  'guardrail': 'Do not merge multiple removable devices into one narrative without mapping identifiers and '
               'time context.',
  'id': 'external_media_expert_multiple_devices',
  'question': 'Multiple external drives were connected over time. What is the safest analysis strategy?',
  'related_playbook_id': 'external_media_hash_copy_refresher',
  'related_scenario_id': 'usb_connected_question',
  'search_terms': ['volume serial', 'drive letter', 'USBSTOR', 'multiple devices'],
  'topic': 'External Media'}]
