"""Chained Coaching paths for ByteCase Playbooks.

Content consistency pass: paths are mentoring-oriented, choices are balanced,
and final review emphasizes source, scope, corroboration, and limitations.
"""

COACHING_PATHS = [{'id': 'live-bitlocker-order-of-volatility',
  'title': 'Live BitLocker laptop: order of volatility',
  'category': 'Live Acquisition / Encryption',
  'summary': 'A powered-on encrypted Windows laptop may contain volatile state that affects '
             'preservation decisions.',
  'related_playbook_id': 'live_computer_acquisition_ram',
  'related_reference_terms': ['BitLocker',
                              'RAM capture',
                              'Order of volatility',
                              'Live acquisition',
                              'Volatile data'],
  'opening_context': 'You arrive at a powered-on Windows laptop that may be protected by '
                     'BitLocker. The investigator asks whether it can be powered down and imaged '
                     'later.',
  'steps': [{'id': 'authority-first',
             'prompt': 'What should come before tool use?',
             'choices': ['Capture RAM first.',
                         'Confirm scope and policy.',
                         'Browse user files.',
                         'Unplug power. without corroborating artifacts or scope notes'],
             'best_index': 1,
             'explanation': 'Live work can change the system and may expose data outside scope. '
                            'Confirm authority, scope, policy, safety, and direction before '
                            'collection decisions.',
             'coaching_note': 'The first step is boundaries, not buttons.'},
            {'id': 'volatile-risk',
             'prompt': 'Why might RAM or live-state documentation matter?',
             'choices': ['It proves the user identity.',
                         'It replaces disk imaging. without corroborating artifacts or scope notes',
                         'It may preserve live encryption and session state.',
                         'It guarantees a recovery key.'],
             'best_index': 2,
             'explanation': 'A live encrypted system may contain mounted-volume, login/session, '
                            'process, network, and encryption-related context that can be lost at '
                            'shutdown. It does not guarantee a key will be found.',
             'coaching_note': 'Use preservation language, not promised-result language.'},
            {'id': 'what-to-record',
             'prompt': 'Which documentation set best supports the later decision?',
             'choices': ['Power state, lock state, scope, tools, timing, and errors.',
                         'Only a final conclusion. without corroborating artifacts or scope notes',
                         'Only the laptop serial number.',
                         'A screenshot after browsing.'],
             'best_index': 0,
             'explanation': 'The decision is easier to defend when the live state, authority, '
                            'collection timing, tools, and limitations are documented before major '
                            'changes.',
             'coaching_note': 'Documentation turns a judgment call into a traceable decision.'},
            {'id': 'balanced-final',
             'prompt': 'Which final framing is strongest?',
             'choices': ['Always shut down encrypted laptops.',
                         'RAM capture is mandatory. without corroborating artifacts or scope notes',
                         'BitLocker makes imaging impossible.',
                         'Documented scope, volatility, and risk guided the action.'],
             'best_index': 3,
             'explanation': 'The careful statement explains why volatility, encryption, scope, and '
                            'policy were considered. It does not create a universal rule.',
             'coaching_note': 'Strong conclusions stay tied to the facts encountered.'}],
  'debrief': 'For a powered-on encrypted laptop, confirm authority first, document state, consider '
             'live collection or RAM when justified, and explain the shutdown/imaging decision '
             'with limitations. Do not state that a BitLocker key exists in RAM unless examination '
             'supports it.'},
 {'id': 'command-history-attribution',
  'title': 'Command history and actor attribution',
  'category': 'Use / Access Context',
  'summary': 'A command or tool artifact exists, but the human actor question still needs careful '
             'context.',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_reference_terms': ['Actor vs. artifact',
                              'Device-use context',
                              'Command history',
                              'Remote access',
                              'Overclaim'],
  'opening_context': 'A command appears in shell history, console history, or process-related '
                     'artifacts. Someone asks whether that proves a specific person typed it.',
  'steps': [{'id': 'safe-core-statement',
             'prompt': 'What is the safest starting statement?',
             'choices': ['The account owner typed it.',
                         'The source may support command activity.',
                         'The command proves intent. without corroborating artifacts or scope '
                         'notes',
                         'The artifact has no value.'],
             'best_index': 1,
             'explanation': 'The artifact may support command activity, depending on source and '
                            'reliability. Actor identity needs separate support.',
             'coaching_note': 'Separate activity from actor before writing the conclusion.'},
            {'id': 'context-to-review',
             'prompt': 'Which context would help strengthen or limit attribution?',
             'choices': ['Only the command text. without corroborating artifacts or scope notes',
                         'Only installed software.',
                         'Session, possession, remote access, and timing.',
                         'Only artifact file size.'],
             'best_index': 2,
             'explanation': 'Attribution is stronger when session data, possession/control, '
                            'authentication context, remote-access review, admissions, and '
                            'timeline sources align.',
             'coaching_note': 'Look for converging indicators rather than one magic artifact.'},
            {'id': 'alternatives',
             'prompt': 'Which alternative explanation should stay on the radar?',
             'choices': ['Remote access or automation.',
                         'No alternative is needed.',
                         'Only local keyboard input is possible.',
                         'Clock settings identify the actor.'],
             'best_index': 0,
             'explanation': 'Remote sessions, scheduled tasks, scripts, malware, shared '
                            'credentials, and other sessions can complicate actor attribution.',
             'coaching_note': 'Considering alternatives improves credibility.'}],
  'debrief': 'Command artifacts can be important, but they are not automatic human-actor proof. '
             'State what the source shows, describe the context reviewed, discuss limitations, and '
             'avoid turning device activity into a person-specific conclusion without support.'},
 {'id': 'download-viewing-knowledge',
  'title': 'Downloaded file: possession, viewing, and knowledge',
  'category': 'Browser / File Activity',
  'summary': 'A browser/download artifact exists, but viewing and knowledge require more than a '
             'download row.',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_reference_terms': ['Download',
                              'File access',
                              'Knowledge',
                              'Browser profile',
                              'Correlation'],
  'opening_context': 'Browser data shows that a file was downloaded. The investigator asks whether '
                     'that means the user viewed and knew the contents.',
  'steps': [{'id': 'download-baseline',
             'prompt': 'What does the download record support first?',
             'choices': ['A download-source record exists.',
                         'The file was fully read.',
                         'The person knew the contents.',
                         'The file is automatically relevant.'],
             'best_index': 0,
             'explanation': 'A download artifact may support that a browser/process recorded a '
                            'download. Viewing, knowledge, and actor identity need more support.',
             'coaching_note': 'Begin with the source record, then build only as far as '
                              'corroboration allows.'},
            {'id': 'viewing-support',
             'prompt': 'Which artifacts may help with later opening or interaction?',
             'choices': ['Only the favicon cache.',
                         'LNK, Jump Lists, MRUs, app history, and timestamps.',
                         'Only filename length.',
                         'Only power state. without corroborating artifacts or scope notes'],
             'best_index': 1,
             'explanation': 'File-interaction artifacts can help evaluate later access. Each '
                            'source has its own meaning and limits.',
             'coaching_note': 'Viewing questions are usually correlation questions.'},
            {'id': 'knowledge-caution',
             'prompt': 'What should be avoided from download evidence alone?',
             'choices': ['Documenting the URL.',
                         'Checking time zone.',
                         'Claiming knowledge of contents.',
                         'Looking for file-open artifacts.'],
             'best_index': 2,
             'explanation': 'Knowledge and intent are stronger human conclusions. They may require '
                            'access artifacts, content display, admissions, surrounding '
                            'communications, searches, or repeated interactions.',
             'coaching_note': 'Possession, viewing, and knowledge are related but different.'}],
  'debrief': 'Treat downloads as a starting point. Correlate browser records with file-system and '
             'application artifacts before discussing access, viewing, knowledge, or actor '
             'attribution.'},
 {'id': 'usb-file-movement',
  'title': 'USB connection and possible file movement',
  'category': 'External Media',
  'summary': 'A USB device was connected, but transfer and actor questions need more than '
             'connection artifacts.',
  'related_playbook_id': 'external_media_hash_copy_refresher',
  'related_reference_terms': ['USB', 'External media', 'File movement', 'Shellbags', 'LNK'],
  'opening_context': 'Windows artifacts show that a removable device was connected. The question '
                     'is whether files were copied to or from it.',
  'steps': [{'id': 'connection-not-transfer',
             'prompt': 'What is the safest starting statement?',
             'choices': ['Connection context is supported.',
                         'File copying is proven. without corroborating artifacts or scope notes',
                         'The actor is identified.',
                         'No further review is needed.'],
             'best_index': 0,
             'explanation': 'USB connection indicators can support that a device was connected or '
                            'recognized. They do not prove transfer or actor identity.',
             'coaching_note': 'Connection, transfer, and attribution are separate questions.'},
            {'id': 'movement-indicators',
             'prompt': 'Which sources help evaluate possible file movement?',
             'choices': ['Only friendly name. without corroborating artifacts or scope notes',
                         'Only wallpaper cache.',
                         'Only monitor serial.',
                         'LNK, Jump Lists, Shellbags, timestamps, and media review.'],
             'best_index': 3,
             'explanation': 'File-reference and shell artifacts, host timelines, and the removable '
                            'media contents may support or limit a file-movement interpretation.',
             'coaching_note': 'The host and removable media may each tell part of the story.'},
            {'id': 'documentation-focus',
             'prompt': 'What should be documented carefully?',
             'choices': ['Only that USB existed. without corroborating artifacts or scope notes',
                         'Device IDs, source artifacts, timing, and limits.',
                         'A copying conclusion first.',
                         'A guess about who plugged it in.'],
             'best_index': 1,
             'explanation': 'Document identifiers, source artifacts, time interpretation, '
                            'account/session context, media review, and limits on what the '
                            'artifacts support.',
             'coaching_note': 'Strong documentation matters when the request asks for more than '
                              'the artifacts alone prove.'}],
  'debrief': 'USB connection is not the same as file transfer. Look for file-interaction '
             'artifacts, media contents, timelines, and context before describing movement or '
             'actor identity.'},
 {'id': 'mobile-message-actor-context',
  'title': 'Mobile messages and actor context',
  'category': 'Mobile',
  'summary': 'A mobile extraction shows messages, but possession, account, and human-actor context '
             'remain important.',
  'related_playbook_id': 'mobile_device_extraction',
  'related_reference_terms': ['Mobile',
                              'Messages',
                              'Account context',
                              'Possession',
                              'Extraction limitations'],
  'opening_context': 'A mobile extraction shows a message thread. The investigator asks whether '
                     'the device owner authored one message.',
  'steps': [{'id': 'message-source',
             'prompt': 'What should be established first?',
             'choices': ['Owner identity.',
                         'Contact photo.',
                         'Message source and extraction context.',
                         'Phone color. without corroborating artifacts or scope notes'],
             'best_index': 2,
             'explanation': 'Start with what the extraction source shows: app, account, '
                            'local/cloud status, timestamps, sender/recipient fields, and tool '
                            'limits.',
             'coaching_note': 'In mobile review, source and extraction type shape what can be '
                              'said.'},
            {'id': 'actor-context-mobile',
             'prompt': 'Which context may help with the human-actor question?',
             'choices': ['Possession, passcode, account control, admissions, and timing.',
                         'Only device model. without corroborating artifacts or scope notes',
                         'Only battery percentage.',
                         'Only wallpaper image.'],
             'best_index': 0,
             'explanation': 'Human attribution may be supported by possession/control, '
                            'authentication context, account ownership, admissions, communication '
                            'patterns, and external corroboration.',
             'coaching_note': 'Device/account activity is not automatically physical-user '
                              'identity.'},
            {'id': 'mobile-limitation',
             'prompt': 'Which limitation should be considered before explaining the result?',
             'choices': ['Cloud messages are always complete.',
                         'Parsed chat view is always complete.',
                         'Deleted status never matters. without corroborating artifacts or scope '
                         'notes',
                         'Unsupported apps and extraction limits may affect results.'],
             'best_index': 3,
             'explanation': 'Mobile results can depend on extraction method, device state, app '
                            'support, cloud data, deleted/recovered status, and parser behavior.',
             'coaching_note': 'A clean parsed view can still have source and limitation issues.'}],
  'debrief': 'Mobile messages can be powerful artifacts, but the careful path is source, '
             'extraction type, account/app context, possession/control context, then attribution '
             'language with limitations.'},
 {'id': 'memory-suspicious-process',
  'title': 'Memory review and suspicious process mindset',
  'category': 'Memory / RAM',
  'summary': 'A RAM review shows an unusual process or network context, but the conclusion must '
             'stay evidence-based.',
  'related_playbook_id': 'memory_ram_analysis_refresher',
  'related_reference_terms': ['Volatility',
                              'Process list',
                              'Command line',
                              'Network connections',
                              'Malfind'],
  'opening_context': 'A memory image shows an unusual process name and a network connection. '
                     'Someone asks whether it proves malware was running.',
  'steps': [{'id': 'process-name-caution',
             'prompt': 'What is the safest starting response?',
             'choices': ['Unusual name means malware. without corroborating artifacts or scope '
                         'notes',
                         'Treat the items as leads needing context.',
                         'Network activity proves theft.',
                         'RAM never matters without disk.'],
             'best_index': 1,
             'explanation': 'Process names and network connections can be important leads. '
                            'Stronger conclusions need path, parent/child process, command line, '
                            'modules, hashes, disk artifacts, or other support.',
             'coaching_note': 'Treat memory indicators as context to investigate, not final '
                              'labels.'},
            {'id': 'memory-followup',
             'prompt': 'Which follow-up is most useful?',
             'choices': ['Rename it as malware. without corroborating artifacts or scope notes',
                         'Look only at wallpaper. without corroborating artifacts or scope notes',
                         'Review process tree, command line, path, modules, and disk artifacts.',
                         'Ignore tool versions. without corroborating artifacts or scope notes'],
             'best_index': 2,
             'explanation': 'A memory finding gains meaning when correlated with process '
                            'relationships, command lines, file paths, network endpoints, loaded '
                            'modules, and disk/log artifacts.',
             'coaching_note': 'Memory analysis is strongest when it feeds a corroborated '
                              'timeline.'},
            {'id': 'network-overclaim',
             'prompt': 'What should be avoided from a network artifact alone?',
             'choices': ['Attributing the IP to a person or proving exfiltration.',
                         'Documenting addresses. without corroborating artifacts or scope notes',
                         'Recording plugin version.',
                         'Correlating disk review.'],
             'best_index': 0,
             'explanation': 'Network artifacts may show connection context, but attribution and '
                            'data-transfer conclusions require additional evidence and context.',
             'coaching_note': 'IP address, process, and timestamp are pieces of a story, not the '
                              'whole story.'}],
  'debrief': 'Memory findings can be high-value leads. Explain the observed artifact, correlate '
             'with other sources, and avoid malware, actor, or exfiltration conclusions until '
             'supported.'},
 {'id': 'cloud-sync-local-boundary',
  'title': 'Cloud sync: local artifact or cloud activity?',
  'category': 'Cloud / Browser / File Activity',
  'summary': 'Cloud client artifacts may blur local activity, sync state, and cloud account '
             'context.',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_reference_terms': ['Cloud sync',
                              'OneDrive',
                              'Local artifact',
                              'Account context',
                              'Timeline'],
  'opening_context': 'A laptop contains cloud-sync artifacts. The investigator asks whether a '
                     'locally present file was created on that laptop.',
  'steps': [{'id': 'cloud-local-boundary',
             'prompt': 'What is the safest first distinction?',
             'choices': ['Local presence, origin, sync, and interaction are separate.',
                         'Local file means local creation. without corroborating artifacts or '
                         'scope notes',
                         'Cloud account name identifies the creator.',
                         'Sync folders never store local files.'],
             'best_index': 0,
             'explanation': 'Cloud-sync clients can create local artifacts for files that '
                            'originated elsewhere. Presence, origin, sync timing, and interaction '
                            'are separate questions.',
             'coaching_note': 'Cloud sync creates tempting shortcuts. Resist them.'},
            {'id': 'cloud-context',
             'prompt': 'Which context helps evaluate the file story?',
             'choices': ['Only the folder name and icon without corroborating artifacts or scope notes',
                         'Sync logs, account details, metadata, access artifacts, and cloud '
                         'records.',
                         'Only file icon. without corroborating artifacts or scope notes',
                         'Only laptop model. without corroborating artifacts or scope notes'],
             'best_index': 1,
             'explanation': 'Sync logs, account identifiers, local timestamps, application '
                            'histories, and provider records can help separate sync from local '
                            'creation or interaction.',
             'coaching_note': 'Local and cloud sources may both be needed.'},
            {'id': 'cloud-final-language',
             'prompt': 'Which conclusion language is most careful before cloud records are '
                       'reviewed?',
             'choices': ['The user created it locally. without corroborating artifacts or scope '
                         'notes',
                         'The provider uploaded it without an account.',
                         'The file was present locally; origin and interaction need more support.',
                         'The sync folder proves intent.'],
             'best_index': 2,
             'explanation': 'This describes the local artifact without overclaiming origin, '
                            'knowledge, or actor identity.',
             'coaching_note': 'Careful language leaves room for better evidence.'}],
  'debrief': 'Cloud sync cases need source boundaries. Distinguish local presence, sync process '
             'activity, local interaction, cloud account context, and origin before making '
             'stronger claims.'},
 {'id': 'timeline-conflict',
  'title': 'Conflicting timestamps and parser differences',
  'category': 'Timestamps / Validation',
  'summary': 'Two sources disagree on time or meaning, and the examiner needs disciplined '
             'interpretation.',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_reference_terms': ['Timestamps',
                              'Time zone',
                              'Parser validation',
                              'Artifact meaning',
                              'Correlation'],
  'opening_context': 'Two tools or artifacts show different timestamps for what appears to be '
                     'related activity.',
  'steps': [{'id': 'timestamp-first',
             'prompt': 'What should you check first?',
             'choices': ['Source meaning, time basis, and parser behavior.',
                         'Pick the best case-theory time.',
                         'Assume newest tool is right.',
                         'Ignore one source silently. without corroborating artifacts or scope '
                         'notes'],
             'best_index': 0,
             'explanation': 'Different artifacts can record different events, use different time '
                            'bases, or be parsed differently. Understand source meaning before '
                            'resolving conflicts.',
             'coaching_note': 'Timestamp conflicts are often meaning conflicts.'},
            {'id': 'timestamp-correlation',
             'prompt': 'Which next step is strongest?',
             'choices': ['Delete the weaker timestamp.',
                         'Call both exact proof. without corroborating artifacts or scope notes',
                         'Convert everything without notes.',
                         'Correlate sources and document each meaning.'],
             'best_index': 3,
             'explanation': 'Correlation and documentation allow the examiner to explain '
                            'uncertainty, tool behavior, and why one interpretation may be '
                            'stronger.',
             'coaching_note': 'A good timeline explains comparability.'},
            {'id': 'parser-difference',
             'prompt': 'What should be avoided when tools disagree?',
             'choices': ['Recording tool version.',
                         'Treating parser output as unquestionable.',
                         'Reviewing limitations. without corroborating artifacts or scope notes',
                         'Testing with known data.'],
             'best_index': 1,
             'explanation': 'Tool output is an interpretation of source data. When results '
                            'conflict and matter, review source context, tool documentation, and '
                            'validation or known data where appropriate.',
             'coaching_note': 'A conflict is a cue to slow down, not guess faster.'}],
  'debrief': 'Timestamp disagreements should be treated as interpretation problems. Identify '
             'source, meaning, time basis, tool behavior, and corroboration before resolving the '
             'timeline.'}]


def search_coaching_paths(query):
    needle = (query or "").strip().lower()
    if not needle:
        return []
    results = []
    for path in COACHING_PATHS:
        parts = [path.get("title", ""), path.get("category", ""), path.get("summary", ""), path.get("opening_context", ""), path.get("debrief", "")]
        parts.extend(path.get("related_reference_terms", []))
        for step in path.get("steps", []):
            parts.extend([step.get("prompt", ""), step.get("explanation", ""), step.get("coaching_note", "")])
            parts.extend(step.get("choices", []))
        if needle in "\n".join(str(part) for part in parts).lower():
            results.append(path)
    return results
