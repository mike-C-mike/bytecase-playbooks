"""ByteCase Playbooks glossary terms: legal scope terms."""

TERMS = [{'term': 'Scope',
  'category': 'Authority / Scope',
  'definition': 'The boundary of what is authorized, requested, or appropriate to collect, '
                'examine, or report.',
  'plain_language': 'The boundary of what is authorized, requested, or appropriate to collect, '
                    'examine, or report.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'Scope should be confirmed before collection or analysis decisions.',
  'related': ['Legal authority', 'Targeted collection', 'Limitations'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Legal authority',
  'category': 'Authority / Scope',
  'definition': 'The warrant, consent, subpoena, court order, policy, or other authority under '
                'which a digital evidence action is taken.',
  'plain_language': 'The warrant, consent, subpoena, court order, policy, or other authority under '
                    'which a digital evidence action is taken.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'ByteCase Playbooks is not legal advice and does not determine whether authority is '
               'sufficient.',
  'related': ['Scope', 'Documentation', 'Limitations'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Possession context',
  'category': 'Attribution',
  'definition': 'Information about who possessed, carried, controlled, or had practical access to '
                'a device or account.',
  'plain_language': 'Information about who possessed, carried, controlled, or had practical access '
                    'to a device or account.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'Possession can support access context, but it does not automatically prove every '
               'action on the device.',
  'related': ['Device-use context', 'Actor vs. artifact'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Password knowledge',
  'category': 'Attribution',
  'definition': 'Information that a person knows, uses, controls, or admits knowing a password or '
                'unlock method.',
  'plain_language': 'Information that a person knows, uses, controls, or admits knowing a password '
                    'or unlock method.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'Password knowledge can support control/access context, especially if unique, but '
               'should still be weighed with other evidence.',
  'related': ['Device-use context', 'Possession context'],
  'related_playbooks': [],
  'aliases': []}]
