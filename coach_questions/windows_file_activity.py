"""Coach Mode questions for Windows / File Activity.

Questions are intentionally judgment-focused. They reinforce careful
interpretation, documentation habits, and overclaim guardrails.
"""

QUESTIONS = [{'answer_index': 0,
  'choices': ['The program appears in an artifact commonly associated with execution or application '
              'activity, depending on the source.',
              'The suspect definitely ran the program.',
              'The program was malicious.',
              'The program was installed by the user.'],
  'difficulty': 'Novice',
  'explanation': 'Program-execution artifacts can support application activity, but interpretation depends '
                 'on artifact type, source, timestamp meaning, account/session context, and corroboration.',
  'follow_up': ['Which artifact source is it?',
                'What timestamp does that source record?',
                'Is there user/session or file-path context?'],
  'guardrail': 'Execution indicators do not automatically identify the human actor or intent.',
  'id': 'windows_novice_program_execution',
  'question': 'A program-execution artifact is present. What is the safest starting interpretation?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['program execution', 'prefetch', 'shimcache', 'amcache', 'userassist'],
  'topic': 'Windows / File Activity'},
 {'answer_index': 2,
  'choices': ['Documenting the deletion-related artifact and source.',
              'Considering Recycle Bin, filesystem, application, and timeline context.',
              'Claiming the user intentionally deleted it to hide evidence.',
              'Looking for corroborating activity.'],
  'difficulty': 'Experienced',
  'explanation': 'Deletion artifacts may support that a file was deleted or no longer exists in a location. '
                 'Intent to conceal requires additional context and should not be assumed.',
  'follow_up': ['Was it deleted by user action, app behavior, cleanup, sync, or system process?',
                'Are there Recycle Bin records or logs?',
                'Does surrounding activity support intent?'],
  'guardrail': 'Deletion is not automatically concealment.',
  'id': 'windows_experienced_deleted_file',
  'question': 'A deleted-file artifact is found. What should be avoided without more support?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['deleted file', 'Recycle Bin', 'intent', 'cleanup'],
  'topic': 'Windows / File Activity'},
 {'answer_index': 2,
  'choices': ['The execution did not happen because one artifact is missing.',
              'The execution definitely happened because one artifact is present.',
              'Evaluate artifact creation conditions, OS/app behavior, parser limits, cleanup, timing, and '
              'corroboration before stating strength.',
              'Ignore absence entirely.'],
  'difficulty': 'Expert',
  'explanation': 'Artifact presence and absence both require context. Some artifacts are not created under '
                 'every condition, can be cleared, can be disabled, or may not apply to that '
                 'OS/version/application behavior.',
  'follow_up': ['Should the missing artifact have been created under these conditions?',
                'Is the tool parsing the right OS version and source?',
                'Are there alternative supporting or refuting artifacts?'],
  'guardrail': 'Absence of an expected artifact is not automatically proof that activity did not occur.',
  'id': 'windows_expert_artifact_disagreement',
  'question': 'One Windows artifact suggests execution, while another expected artifact is absent. What is '
              'the best expert response?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['artifact absence', 'program execution', 'parser limits', 'corroboration'],
  'topic': 'Windows / File Activity'}]
