"""Coach Mode questions for memory / ram.

Content consistency pass: answer choice length is intentionally balanced so
the safest response is not signaled by being longest.
"""

QUESTIONS = [{'id': 'memory_novice_process_name',
  'topic': 'Memory / RAM',
  'difficulty': 'Novice',
  'question': 'A process name in memory looks suspicious. What is the best first mindset?',
  'choices': ['Call it malware immediately.',
              'Treat it as a lead needing context.',
              'Ignore it because RAM changes.',
              'Attribute it to the user. without corroborating artifacts or scope notes'],
  'answer_index': 1,
  'explanation': 'A process name can be misleading. Review path, parent/child process, command '
                 'line, modules, handles, and related disk/log artifacts before stronger claims.',
  'follow_up': ['What is the process path and parent process?',
                'Are command-line arguments available?',
                'Do disk artifacts support the same activity?'],
  'guardrail': 'A process name alone is not a malware finding.',
  'related_scenario_id': 'command_seen_on_device',
  'search_terms': ['memory', 'process', 'malware', 'Volatility']},
 {'id': 'memory_experienced_malfind',
  'topic': 'Memory / RAM',
  'difficulty': 'Experienced',
  'question': 'A memory plugin flags possible injected code. What is the best next response?',
  'choices': ['The system is confirmed compromised.',
              'Correlate plugin output with process and source context.',
              'Delete the process from the notes.',
              'Skip tool/version documentation. without corroborating artifacts or scope notes'],
  'answer_index': 1,
  'explanation': 'Suspicious plugin output should be evaluated with process tree, path, modules, '
                 'network details, hashes, source context, tool version, and possible false '
                 'positives.',
  'follow_up': ['What did the plugin actually detect?',
                'Can the region be dumped and reviewed?',
                'Do other sources support the same conclusion?'],
  'guardrail': 'Suspicious memory output is not automatic proof of compromise, intent, or actor '
               'identity.',
  'related_scenario_id': 'command_seen_on_device',
  'search_terms': ['malfind', 'injection', 'memory plugin']},
 {'id': 'memory_expert_live_limitations',
  'topic': 'Memory / RAM',
  'difficulty': 'Expert',
  'question': 'A RAM capture was made after several minutes of live interaction. How should '
              'limitations be handled?',
  'choices': ['Omit timing because capture succeeded.',
              'Document actions, elapsed time, tools, and limits.',
              'Describe it as perfect live state.',
              'Assume no volatile data changed. without corroborating artifacts or scope notes'],
  'answer_index': 1,
  'explanation': 'Live collection changes the system, and memory is constantly changing. Document '
                 'timing, interactions, tool behavior, errors, and limitations so later '
                 'interpretation is properly bounded.',
  'follow_up': ['What actions occurred before capture?',
                'Was the system isolated or still networked?',
                'Were tool errors or warnings recorded?'],
  'guardrail': 'A successful live capture is not a perfect record of every prior volatile '
               'condition.',
  'related_scenario_id': 'command_seen_on_device',
  'search_terms': ['RAM capture', 'live response', 'limitations']}]
