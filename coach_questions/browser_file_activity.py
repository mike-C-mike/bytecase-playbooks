"""Coach Mode questions for browser / file / activity.

Content consistency pass: answer choice length is intentionally balanced so
the safest response is not signaled by being longest.
"""

QUESTIONS = [{'id': 'browser_file_novice_download',
  'topic': 'Browser / File Activity',
  'difficulty': 'Novice',
  'question': 'A browser record shows a file download. What should the examiner avoid saying from '
              'that record alone?',
  'choices': ['The file was downloaded by that browser/profile.',
              'The download source should be documented.',
              'Someone definitely read the file contents.',
              'File-open artifacts may be checked next.'],
  'answer_index': 2,
  'explanation': 'A download record can support a download event, but it does not by itself '
                 'establish viewing, knowledge, intent, or the human actor.',
  'follow_up': ['Is the downloaded file still present?',
                'Are there LNK, Jump List, MRU, or application-open records?',
                'What profile, account, and timestamp context exists?'],
  'guardrail': 'Downloaded is not the same as opened, viewed, understood, or personally selected.',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['download', 'browser', 'knowledge', 'file access']},
 {'id': 'browser_file_experienced_file_open',
  'topic': 'Browser / File Activity',
  'difficulty': 'Experienced',
  'question': 'A file appears in recent-file and shortcut artifacts. What is a careful '
              'interpretation?',
  'choices': ['The artifact may support access or presentation context.',
              'The person fully read the file. without corroborating artifacts or scope notes',
              'The file was created by that user.',
              'The file meaning is already known.'],
  'answer_index': 0,
  'explanation': 'Recent-file and shortcut artifacts can support interaction or application '
                 'context, but the source and artifact family determine exactly what can be said.',
  'follow_up': ['Which profile produced the artifact?',
                'Does the source file still exist?',
                'Are timestamps consistent across sources?'],
  'guardrail': 'File-access indicators require source-specific meaning and attribution context.',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['recent files', 'LNK', 'jump list', 'viewed']},
 {'id': 'browser_file_expert_cloud_sync_cache',
  'topic': 'Browser / File Activity',
  'difficulty': 'Expert',
  'question': 'A file exists in cache or a cloud-sync folder. What should be evaluated before '
              'discussing user knowledge?',
  'choices': ['Only whether the filename is suspicious.',
              'Source mechanism, sync state, and interaction artifacts.',
              'Assume manual saving by the user. without corroborating artifacts or scope notes',
              'Ignore cached and synced data entirely.'],
  'answer_index': 1,
  'explanation': 'Cache and sync mechanisms can create local files through automatic processes, '
                 'previews, redirects, cloud activity, or activity from another device. User '
                 'knowledge requires more context.',
  'follow_up': ['Was the file hydrated, opened, previewed, or synced?',
                'Is there a cloud account or provider record?',
                'Are there local open artifacts after the sync/cache event?'],
  'guardrail': 'Local file presence from cache or sync does not automatically prove intentional '
               'viewing or knowledge.',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['cache', 'cloud sync', 'OneDrive', 'knowledge']}]
