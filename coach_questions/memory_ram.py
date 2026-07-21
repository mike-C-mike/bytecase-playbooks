"""Coach Mode questions for Memory / RAM.

Questions are intentionally judgment-focused. They reinforce careful
interpretation, documentation habits, and overclaim guardrails.
"""

QUESTIONS = [{'answer_index': 1,
  'choices': ['Conclude malware immediately.',
              'Treat it as a lead and review path, parent process, command line, network connections, '
              'modules, and corroboration.',
              'Delete it from the evidence.',
              'Ignore memory process data.'],
  'difficulty': 'Novice',
  'explanation': 'A process name can be misleading. Process path, parent/child relationship, command line, '
                 'network activity, DLLs/modules, hashes, and supporting artifacts help determine whether it '
                 'is meaningful.',
  'follow_up': ['What is the full process path?',
                'What launched it?',
                'Is there network or injected-code context?'],
  'guardrail': 'A process name alone is not a malware finding.',
  'id': 'memory_novice_process_name',
  'question': 'A process name in memory looks suspicious. What should you do first?',
  'related_playbook_id': 'memory_ram_analysis_volatility',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['process', 'RAM', 'Volatility', 'pslist', 'pstree'],
  'topic': 'Memory / RAM'},
 {'answer_index': 1,
  'choices': ['The machine is confirmed compromised.',
              'The plugin output is a lead requiring process context, validation awareness, possible dumped '
              'content review, and corroboration.',
              'The user intentionally installed malware.',
              'No other artifacts matter.'],
  'difficulty': 'Experienced',
  'explanation': 'Suspicious memory output should be evaluated with process tree, path, modules, network '
                 'connections, tool documentation, dumps when justified, and other artifacts. It can guide '
                 'analysis but should not be overclaimed.',
  'follow_up': ['Which process/PID is involved?',
                'Can the output be corroborated with disk or network artifacts?',
                'Is specialized malware analysis needed?'],
  'guardrail': 'Suspicious memory output is not automatic proof of compromise, intent, or actor identity.',
  'id': 'memory_experienced_malfind',
  'question': 'A memory plugin flags possible injected code. What is the best next mindset?',
  'related_playbook_id': 'memory_ram_analysis_volatility',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['malfind', 'injection', 'memory', 'malware'],
  'topic': 'Memory / RAM'},
 {'answer_index': 1,
  'choices': ['Ignore them if the capture succeeded.',
              'Document tool/version, timing, examiner actions, system changes, possible volatility loss, '
              'and any errors or environmental constraints.',
              'State the memory image is a perfect snapshot of original state.',
              'Avoid hashing the output because memory changes.'],
  'difficulty': 'Expert',
  'explanation': 'Live collection changes the system, and memory is constantly changing. Documentation '
                 'should explain what was captured, when, with what tool, and what actions/limitations may '
                 'affect interpretation.',
  'follow_up': ['What actions occurred before capture?',
                'What tool/version and destination were used?',
                'Were hashes, logs, or errors recorded?'],
  'guardrail': 'A successful live capture is not a perfect record of every prior volatile condition.',
  'id': 'memory_expert_live_capture_limitations',
  'question': 'A RAM capture was performed on a live system after several minutes of interaction. How should '
              'limitations be handled?',
  'related_playbook_id': 'live_computer_acquisition_ram',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['RAM capture', 'volatile data', 'limitations', 'live acquisition'],
  'topic': 'Memory / RAM'}]
