"""Coach Mode questions for windows / file / activity.

Content consistency pass: answer choice length is intentionally balanced so
the safest response is not signaled by being longest.
"""

QUESTIONS = [{'id': 'windows_novice_execution_artifact',
  'topic': 'Windows / File Activity',
  'difficulty': 'Novice',
  'question': 'A program-execution artifact is present. What is the safest starting '
              'interpretation?',
  'choices': ['The program activity may be supported by that artifact.',
              'The named person ran the program.',
              'The program was malicious.',
              'Intent is established. without corroborating artifacts or scope notes'],
  'answer_index': 0,
  'explanation': 'Program-execution artifacts can support application activity, but interpretation '
                 'depends on the artifact family, source meaning, OS version, and corroboration.',
  'follow_up': ['Which artifact family is it?',
                'Does it show execution, inventory, or user interaction?',
                'Are session/account artifacts aligned?'],
  'guardrail': 'Execution indicators do not automatically identify the human actor or intent.',
  'related_scenario_id': 'command_seen_on_device',
  'search_terms': ['Prefetch', 'Amcache', 'execution']},
 {'id': 'windows_experienced_deleted_file',
  'topic': 'Windows / File Activity',
  'difficulty': 'Experienced',
  'question': 'A deleted-file artifact is found. What should be avoided without more support?',
  'choices': ['Documenting source and path.',
              'Reviewing recycle context.',
              'Calling it intentional concealment.',
              'Checking timestamps. without corroborating artifacts or scope notes'],
  'answer_index': 2,
  'explanation': 'Deletion artifacts may support that a file was deleted, moved to recycle, or no '
                 'longer exists in a location. Motive and intent require additional context.',
  'follow_up': ['Was it deleted, recycled, moved, or overwritten?',
                'What account/session context exists?',
                'Are there related searches, messages, or tool activity?'],
  'guardrail': 'Deletion is not automatically concealment.',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['deleted file', 'recycle bin', 'intent']},
 {'id': 'windows_expert_absence_conflict',
  'topic': 'Windows / File Activity',
  'difficulty': 'Expert',
  'question': 'One artifact suggests execution, while an expected artifact is absent. What is the '
              'careful approach?',
  'choices': ['Execution did not happen.',
              'The present artifact wins.',
              'Evaluate artifact creation rules and limitations.',
              'Pick the simpler story. without corroborating artifacts or scope notes'],
  'answer_index': 2,
  'explanation': 'Artifact presence and absence both require context. Some artifacts are not '
                 'created under all OS versions, configurations, execution paths, or retention '
                 'conditions.',
  'follow_up': ['Should the expected artifact exist on this system?',
                'Could cleaning, rollover, policy, or configuration explain absence?',
                'Do other sources support or weaken execution?'],
  'guardrail': 'Absence of an expected artifact is not automatically proof that activity did not '
               'occur.',
  'related_scenario_id': 'command_seen_on_device',
  'search_terms': ['artifact absence', 'execution', 'Prefetch']}]
