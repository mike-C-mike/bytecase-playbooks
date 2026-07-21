"""ByteCase Playbooks glossary terms: browser terms."""

TERMS = [{'term': 'Browser history',
  'category': 'Browser',
  'definition': 'Records that may indicate pages, URLs, visits, downloads, searches, or other '
                'browser activity depending on browser and artifact type.',
  'plain_language': 'Records that may indicate pages, URLs, visits, downloads, searches, or other '
                    'browser activity depending on browser and artifact type.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'Browser history does not always prove intent, knowledge, or a specific human '
               'actor.',
  'related': ['Downloads', 'Cache', 'Cookies'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Download artifact',
  'category': 'Browser / File Activity',
  'definition': 'A record suggesting a file was downloaded, saved, or handled by a browser or '
                'application.',
  'plain_language': 'A record suggesting a file was downloaded, saved, or handled by a browser or '
                    'application.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'Download evidence is not the same as viewing, opening, knowledge, or intent.',
  'related': ['Browser history', 'File access', 'Recent files'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Cache artifact',
  'category': 'Browser',
  'definition': 'Browser-stored content or metadata retained for performance or application '
                'behavior.',
  'plain_language': 'Browser-stored content or metadata retained for performance or application '
                    'behavior.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'Cached content may be created automatically and should not be overclaimed as '
               'intentional viewing.',
  'related': ['Browser history', 'Cookies'],
  'related_playbooks': [],
  'aliases': []},
 {'term': 'Cookie',
  'category': 'Browser',
  'definition': 'Browser or app data often used for sessions, preferences, tracking, or site '
                'state.',
  'plain_language': 'Browser or app data often used for sessions, preferences, tracking, or site '
                    'state.',
  'why_it_matters': '',
  'common_examples': [],
  'guardrail': 'A cookie can support account or site context, but does not by itself prove a '
               'specific person used the browser at that moment.',
  'related': ['Browser history', 'Account context'],
  'related_playbooks': [],
  'aliases': []}]
