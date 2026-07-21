"""Coach Mode questions for Integrity / Hashing.

Questions are intentionally judgment-focused. They reinforce careful
interpretation, documentation habits, and overclaim guardrails.
"""

QUESTIONS = [{'answer_index': 0,
  'choices': ['The file content being compared has not changed between those hash calculations.',
              'The file is relevant evidence.',
              'The file proves user intent.',
              'The file is safe to execute.'],
  'difficulty': 'Novice',
  'explanation': 'Matching hash values support file integrity for the compared content and algorithm. They '
                 'do not explain what the file means, whether it is relevant, or who used it.',
  'follow_up': ['What exactly was hashed?',
                'When and by what tool?',
                'Was the source or output path documented?'],
  'guardrail': 'Integrity is not interpretation.',
  'id': 'hashing_novice_integrity',
  'question': 'Two SHA-256 hash values match for a file. What does that support?',
  'related_playbook_id': 'external_media_hash_copy_refresher',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['hash', 'integrity', 'SHA-256', 'verify'],
  'topic': 'Integrity / Hashing'},
 {'answer_index': 1,
  'choices': ['Assume evidence tampering immediately.',
              'Document the mismatch, verify the exact file/source/algorithm, check paths and versions, '
              'preserve both results, and investigate the cause.',
              'Delete the newer hash record.',
              'Ignore the mismatch if filenames match.'],
  'difficulty': 'Experienced',
  'explanation': 'A mismatch is important, but the cause may include wrong file, changed metadata/content, '
                 'different algorithm, path confusion, export transformation, or actual alteration. Document '
                 'before concluding.',
  'follow_up': ['Was the same file and algorithm used?',
                'Were outputs transformed or regenerated?',
                'Can the original source or manifest be verified?'],
  'guardrail': 'A hash mismatch needs investigation; it is not automatically proof of malicious alteration.',
  'id': 'hashing_experienced_mismatch',
  'question': 'A rehash does not match the original manifest. What should happen next?',
  'related_playbook_id': 'external_media_hash_copy_refresher',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['hash mismatch', 'manifest', 'integrity', 'algorithm'],
  'topic': 'Integrity / Hashing'},
 {'answer_index': 1,
  'choices': ['Report only the shortest hash because it is easier to read.',
              'Clearly state each algorithm, source, tool/version, calculation time, and what each hash '
              'applies to.',
              'Mix values if filenames match.',
              'Use hashes to conclude who created the file.'],
  'difficulty': 'Expert',
  'explanation': 'Hash values are only meaningful when tied to an exact source, algorithm, tool/version, and '
                 'time. Different tools may hash different objects, containers, exports, or normalized '
                 'outputs.',
  'follow_up': ['Were the same bytes hashed by each tool?',
                'Are hashes for original media, image, exported file, report, or container?',
                'Does policy prefer a specific algorithm?'],
  'guardrail': 'Hash values must be scoped to the exact object hashed.',
  'id': 'hashing_expert_algorithm_scope',
  'question': 'An examiner has MD5, SHA-1, and SHA-256 values from different tools. What is the careful '
              'reporting approach?',
  'related_playbook_id': 'external_media_hash_copy_refresher',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['MD5', 'SHA-1', 'SHA-256', 'algorithm', 'scope'],
  'topic': 'Integrity / Hashing'}]
