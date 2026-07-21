"""Coach Mode questions for integrity / hashing.

Content consistency pass: answer choice length is intentionally balanced so
the safest response is not signaled by being longest.
"""

QUESTIONS = [{'id': 'integrity_novice_matching_hash',
  'topic': 'Integrity / Hashing',
  'difficulty': 'Novice',
  'question': 'Two SHA-256 values match for the same file content. What does that support?',
  'choices': ['The compared content has not changed.',
              'The file is relevant evidence.',
              'The user knew the contents. without corroborating artifacts or scope notes',
              'The tool made no mistakes anywhere.'],
  'answer_index': 0,
  'explanation': 'A matching hash supports integrity for the specific object, algorithm, and '
                 'comparison. It does not interpret the file or explain user knowledge.',
  'follow_up': ['What exact source was hashed?',
                'Which algorithm and tool/version were used?',
                'Was the hash file-level, image-level, or export-level?'],
  'guardrail': 'Integrity is not interpretation.',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['hash', 'SHA-256', 'integrity']},
 {'id': 'integrity_experienced_mismatch',
  'topic': 'Integrity / Hashing',
  'difficulty': 'Experienced',
  'question': 'A rehash does not match the original manifest. What is the careful next step?',
  'choices': ['Assume tampering immediately.',
              'Verify source, method, scope, and prior records.',
              'Ignore the mismatch. without corroborating artifacts or scope notes',
              'Change the manifest to match.'],
  'answer_index': 1,
  'explanation': 'A mismatch is important, but possible causes include the wrong file, changed '
                 'content, a different export, different scope, metadata changes, or documentation '
                 'error. Resolve before concluding why it happened.',
  'follow_up': ['Was the same exact object hashed?',
                'Were tool settings and paths the same?',
                'Are prior manifests and logs available?'],
  'guardrail': 'A hash mismatch requires investigation; it is not automatically malicious '
               'alteration.',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['hash mismatch', 'manifest', 'verification']},
 {'id': 'integrity_expert_multiple_hashes',
  'topic': 'Integrity / Hashing',
  'difficulty': 'Expert',
  'question': 'MD5, SHA-1, and SHA-256 values exist from different tools. What should the report '
              'tie each value to?',
  'choices': ['Only the shortest value.',
              'The person who possessed the device.',
              'Exact source, algorithm, tool/version, and time.',
              'The case theory. without corroborating artifacts or scope notes'],
  'answer_index': 2,
  'explanation': 'Hash values are useful only when tied to the exact object hashed, the algorithm, '
                 'tool/version, and collection or verification context.',
  'follow_up': ['Are these source-media, image, file, or export hashes?',
                'Were they generated at acquisition or later verification?',
                'Are the values reproducible?'],
  'guardrail': 'Hash values must be scoped to the exact object hashed.',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['MD5', 'SHA-1', 'SHA-256', 'scope']}]
