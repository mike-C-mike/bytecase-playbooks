"""Chained Coaching paths for ByteCase Playbooks.

These are mentoring-style scenario paths used by the Workbench > Coaching lane.
They are intentionally stored in coach_questions/ so future growth can happen as
content packs rather than hard-coded GUI logic.
"""

COACHING_PATHS = [{'id': 'live-bitlocker-order-of-volatility',
  'title': 'Live BitLocker laptop: order of volatility',
  'category': 'Live Acquisition / Encryption',
  'summary': 'A powered-on encrypted Windows laptop may contain volatile state that changes the acquisition plan.',
  'related_playbook_id': 'live_computer_acquisition_ram',
  'related_reference_terms': ['BitLocker', 'RAM capture', 'Order of volatility', 'Live acquisition', 'Volatile data'],
  'opening_context': 'You arrive at a powered-on Windows laptop that may be protected by BitLocker. The investigator '
                     'asks whether it can simply be powered down and imaged later.',
  'steps': [{'id': 'authority-first',
             'prompt': 'What should your first examiner-thinking step be?',
             'choices': ['Start a RAM capture immediately because encryption is possible. even though the source '
                         'artifact has not been corroborated.',
                         'Confirm authority, scope, policy, and safety before changing the live system.',
                         'Power the laptop down so the scene stays simple.',
                         'Ask the investigator to unlock it and browse files.'],
             'best_index': 1,
             'explanation': 'Live response can change the system and may expose data outside scope. The first mindset '
                            'step is to confirm what is authorized and what policy allows before collection decisions '
                            'are made.',
             'coaching_note': 'Good live-response decisions start with boundaries, not tools.'},
            {'id': 'why-ram-before-powerdown',
             'prompt': 'With authority confirmed, why might RAM or live-state documentation matter before shutdown?',
             'choices': ['It proves the suspect personally used the computer. without documenting scope, source, time '
                         'meaning, or limitations.',
                         'It replaces the need for a later forensic image.',
                         'It may preserve volatile encryption, session, process, and mounted-volume context.',
                         'It guarantees the BitLocker recovery key will be found.'],
             'best_index': 2,
             'explanation': 'A live encrypted system may contain volatile state that disappears at shutdown. RAM and '
                            'live-state documentation may preserve mounted volumes, logged-in sessions, processes, '
                            'network connections, and possible encryption-related material. It does not guarantee a '
                            'key will be found.',
             'coaching_note': 'Use possibility and preservation language. Do not promise results before examination.'},
            {'id': 'bitlocker-specific-evidence',
             'prompt': 'What key evidence-acquisition opportunity may be lost if a BitLocker-protected system is '
                       'powered down?',
             'choices': ['Potential encryption context in volatile memory, including material that may help access '
                         'mounted encrypted data.',
                         'The Windows event log, because it only exists while powered on. because the single artifact '
                         'resolves the human-actor question by itself.',
                         'The hard drive serial number, because shutdown changes it.',
                         'The file hashes, because hashes cannot be computed after shutdown.'],
             'best_index': 0,
             'explanation': 'The key issue is volatile encryption context. Depending on system state and tool '
                            'capability, memory may contain information relevant to mounted encrypted volumes. That '
                            'possibility is why live state and RAM are considered before shutdown.',
             'coaching_note': 'Say what RAM may contain; avoid stating that a recovery key is present unless '
                              'examination supports it.'},
            {'id': 'bigger-picture-statement',
             'prompt': 'Which final statement best frames the decision?',
             'choices': ['Encrypted laptops should always be shut down before imaging. even though the source artifact '
                         'has not been corroborated.',
                         'RAM capture is mandatory on every live computer.',
                         'BitLocker automatically makes disk imaging impossible.',
                         'This is a scope, volatility, encryption, and risk decision that should be documented before '
                         'action.'],
             'best_index': 3,
             'explanation': 'The strongest framing is balanced. The examiner is not saying live capture is always '
                            'required; they are documenting why volatile encryption context, scope, risk, and policy '
                            'were considered before power decisions.',
             'coaching_note': 'The proper order is not one universal button click. It is a documented decision path.'}],
  'debrief': 'A powered-on encrypted laptop should trigger order-of-volatility thinking. Confirm authority first, '
             'document live state, consider RAM/live collection when justified, then explain the shutdown/imaging '
             'decision with limitations. Do not claim a BitLocker key exists in RAM unless examination supports it.'},
 {'id': 'command-history-attribution',
  'title': 'Command history and actor attribution',
  'category': 'Use / Access Context',
  'summary': 'A command or tool artifact exists, but the human actor question still needs careful context.',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_reference_terms': ['Actor vs. artifact',
                              'Device-use context',
                              'Command history',
                              'Remote access',
                              'Overclaim'],
  'opening_context': 'A command appears in shell history, console history, or process-related artifacts. Someone asks '
                     'whether that proves the named suspect typed it.',
  'steps': [{'id': 'safe-core-statement',
             'prompt': 'What is the safest starting statement?',
             'choices': ['The named account holder typed it because the account name is present. without documenting '
                         'scope, source, time meaning, or limitations.',
                         'The artifact may support command activity; actor identity needs more context.',
                         'The command proves intent because it appears technical.',
                         'The artifact is useless unless there is video of the keyboard.'],
             'best_index': 1,
             'explanation': 'The artifact can support activity depending on source and reliability, but the human '
                            'actor conclusion requires additional support.',
             'coaching_note': 'Separate the artifact from the person before building attribution language.'},
            {'id': 'context-to-review',
             'prompt': 'Which context would be most useful before strengthening attribution?',
             'choices': ['Only the command text, because commands identify the typist. because the single artifact '
                         'resolves the human-actor question by itself.',
                         'Only the installed software list, because installed tools prove use.',
                         'Logon/session, possession, remote access, password knowledge, and timeline context.',
                         'Only the file size of the history artifact.'],
             'best_index': 2,
             'explanation': 'Attribution may be supported by a combination of session data, possession/control, '
                            'authentication context, remote-access review, admissions, and corroborating timeline '
                            'sources.',
             'coaching_note': 'Look for converging indicators, not a single magic artifact.'},
            {'id': 'alternative-explanations',
             'prompt': 'Which alternative explanation should stay on your radar?',
             'choices': ['Remote access, automation, malware, shared credentials, or another user session.',
                         'No alternative is needed once a command artifact exists. even though the source artifact has '
                         'not been corroborated.',
                         'The command can only be produced by a local keyboard.',
                         'The system clock eliminates all attribution questions.'],
             'best_index': 0,
             'explanation': 'A careful examiner considers plausible alternative explanations. Remote sessions, '
                            'scheduled tasks, scripts, malware, and shared accounts can complicate the actor question.',
             'coaching_note': 'The ability to name alternatives makes the final statement stronger, not weaker.'}],
  'debrief': 'Command artifacts can be important, but they are not automatically human-actor proof. State what the '
             'source shows, describe the context reviewed, discuss limitations, and avoid turning device activity into '
             'a person-specific conclusion without support.'},
 {'id': 'download-viewing-knowledge',
  'title': 'Downloaded file: possession, viewing, and knowledge',
  'category': 'Browser / File Activity',
  'summary': 'A browser/download artifact exists, but viewing and knowledge require more than a download row.',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_reference_terms': ['Browser history', 'Downloads', 'File access', 'Knowledge', 'Timeline'],
  'opening_context': 'Browser data shows that a file was downloaded. The investigator asks whether that proves the '
                     'user opened it and knew what it contained.',
  'steps': [{'id': 'download-baseline',
             'prompt': 'What can the download artifact most safely support by itself?',
             'choices': ['That the user read the file and understood its contents. without documenting scope, source, '
                         'time meaning, or limitations.',
                         'That the file was manually downloaded by the account owner.',
                         'That the file was never deleted or moved.',
                         'That a download event or record appears to exist from the reviewed source.'],
             'best_index': 3,
             'explanation': 'A download artifact may support that a download record exists, subject to source, parser, '
                            'timestamp, and profile context. Viewing, knowledge, and actor identity need more support.',
             'coaching_note': 'Start with the source record. Build stronger claims only after corroboration.'},
            {'id': 'viewing-support',
             'prompt': 'Which group best supports whether the file may have been opened or interacted with later?',
             'choices': ['Only the browser favicon cache. because the single artifact resolves the human-actor '
                         'question by itself.',
                         'LNK, Jump Lists, recent files, application artifacts, shell activity, and file timestamps.',
                         'Only the filename length.',
                         'Only whether the device was plugged in.'],
             'best_index': 1,
             'explanation': 'File-interaction artifacts such as LNK files, Jump Lists, recent-file lists, app-specific '
                            'histories, and shell artifacts may help evaluate later access. Each has limitations and '
                            'timestamp meaning that must be documented.',
             'coaching_note': 'A viewing question is usually an artifact-correlation question.'},
            {'id': 'knowledge-caution',
             'prompt': 'What should you avoid saying from download evidence alone?',
             'choices': ['That a browser source needs documentation. even though the source artifact has not been '
                         'corroborated.',
                         'That timestamps may need time-zone review.',
                         'That the person knew the contents unless supporting context exists.',
                         'That file movement can be relevant.'],
             'best_index': 2,
             'explanation': 'Knowledge and intent are stronger human conclusions. They may require file access, '
                            'content display, admissions, surrounding communications, search terms, repeated '
                            'interactions, or other corroborating context.',
             'coaching_note': 'Possession, viewing, and knowledge are related but not identical.'}],
  'debrief': 'Treat downloads as a starting point. Correlate browser records with file-system and application '
             'artifacts before discussing access, viewing, knowledge, or actor attribution.'},
 {'id': 'usb-file-movement',
  'title': 'USB connection and possible file movement',
  'category': 'External Media',
  'summary': 'A USB device was connected, but transfer and actor questions need more than connection artifacts.',
  'related_playbook_id': 'external_media_hash_copy_refresher',
  'related_reference_terms': ['USB', 'External media', 'File movement', 'Shellbags', 'LNK'],
  'opening_context': 'Windows artifacts show that a removable device was connected. The question is whether files were '
                     'copied to or from it.',
  'steps': [{'id': 'connection-not-transfer',
             'prompt': 'What is the safest starting statement?',
             'choices': ['Connection artifacts can support device connection, not file transfer by themselves.',
                         'The connected USB proves files were copied. without documenting scope, source, time meaning, '
                         'or limitations.',
                         'USB artifacts identify the person who connected it.',
                         'No external media review is needed once a serial number is found.'],
             'best_index': 0,
             'explanation': 'USB connection indicators can help show that a device was connected or recognized. They '
                            'do not automatically prove file transfer or identify the human actor.',
             'coaching_note': 'Connection, transfer, and attribution are separate questions.'},
            {'id': 'movement-indicators',
             'prompt': 'Which artifacts may help evaluate possible file movement?',
             'choices': ['Only the USB device friendly name. because the single artifact resolves the human-actor '
                         'question by itself.',
                         'Only the monitor serial number.',
                         'Only the Windows wallpaper cache.',
                         'LNK, Jump Lists, Shellbags, recent files, file timestamps, and destination/source media '
                         'review.'],
             'best_index': 3,
             'explanation': 'File access and shell artifacts may support user interaction with files/folders on '
                            'removable media. Reviewing both host and media contents can help determine whether '
                            'movement is supported.',
             'coaching_note': 'The host tells part of the story; the removable media may tell another part.'},
            {'id': 'documentation-focus',
             'prompt': 'What should be documented carefully?',
             'choices': ['Only the fact that a USB existed. even though the source artifact has not been corroborated.',
                         'Device identifiers, first/last connection timing, artifact sources, and transfer '
                         'limitations.',
                         'A conclusion that copying occurred before reviewing file artifacts. without documenting '
                         'scope, source, time meaning, or limitations.',
                         "The examiner's guess about who plugged it in."],
             'best_index': 1,
             'explanation': 'Useful documentation includes device identifiers, source artifacts, time interpretation, '
                            'connected account/session context, media review, and limitations on what the artifacts '
                            'prove.',
             'coaching_note': 'Strong documentation is especially important when the request asks for a stronger '
                              'conclusion than the artifacts support.'}],
  'debrief': 'USB connection is not the same as file transfer. Look for file-interaction artifacts, media contents, '
             'timelines, and context before describing movement or actor identity.'},
 {'id': 'mobile-message-actor-context',
  'title': 'Mobile messages and actor context',
  'category': 'Mobile',
  'summary': 'A mobile extraction shows messages, but possession, account, and human-actor context remain important.',
  'related_playbook_id': 'mobile_device_extraction',
  'related_reference_terms': ['Mobile', 'Messages', 'Account context', 'Possession', 'Extraction limitations'],
  'opening_context': 'A mobile extraction shows a message thread. The investigator asks whether the device owner '
                     'definitely authored one message.',
  'steps': [{'id': 'message-source',
             'prompt': 'What should be established first?',
             'choices': ["The owner's identity, because phone ownership proves authorship. without documenting scope, "
                         'source, time meaning, or limitations.',
                         'The contact photo, because it proves who typed the message.',
                         'The source of the message record, account/app context, timestamps, and extraction type.',
                         'The phone color, because it confirms the sender.'],
             'best_index': 2,
             'explanation': 'Start by understanding what the extraction source shows: app, account, local/cloud '
                            'status, timestamps, sender/recipient fields, and extraction limitations.',
             'coaching_note': 'In mobile review, source and extraction type shape what can be said.'},
            {'id': 'actor-context-mobile',
             'prompt': 'Which context may help with the human-actor question?',
             'choices': ['Possession, passcode knowledge, account control, admissions, timing, and corroborating '
                         'communications.',
                         'Only the device model. because the single artifact resolves the human-actor question by '
                         'itself.',
                         'Only the battery percentage. even though the source artifact has not been corroborated.',
                         'Only the wallpaper image.'],
             'best_index': 0,
             'explanation': 'Human attribution may be supported by device possession/control, authentication context, '
                            'account ownership, admissions, communication patterns, and external corroboration.',
             'coaching_note': 'Device/account activity is not automatically physical-user identity.'},
            {'id': 'mobile-limitation',
             'prompt': 'Which limitation should be considered before explaining the result?',
             'choices': ['Mobile extractions always include every cloud message. even though the source artifact has '
                         'not been corroborated.',
                         'A parsed chat view is always complete.',
                         'Deleted status never matters.',
                         'Unsupported apps, cloud sync, deleted/recovered status, and tool parsing limits may affect '
                         'interpretation.'],
             'best_index': 3,
             'explanation': 'Mobile results can depend on extraction method, device state, app support, cloud data, '
                            'deleted/recovered status, and parser behavior. Those limits should be documented.',
             'coaching_note': 'A clean-looking parsed view can still have scope and limitation issues.'}],
  'debrief': 'Mobile messages can be powerful artifacts, but the careful path is source, extraction type, account/app '
             'context, possession/control context, then attribution language with limitations.'},
 {'id': 'memory-suspicious-process',
  'title': 'Memory review and suspicious process mindset',
  'category': 'Memory / RAM',
  'summary': 'A RAM review shows an unusual process or network context, but the conclusion must stay evidence-based.',
  'related_playbook_id': 'memory_ram_analysis_refresher',
  'related_reference_terms': ['Volatility', 'Process list', 'Command line', 'Network connections', 'Malfind'],
  'opening_context': 'A memory image shows an unusual process name and a network connection. Someone asks whether it '
                     'proves malware was running.',
  'steps': [{'id': 'process-name-caution',
             'prompt': 'What is the safest starting response?',
             'choices': ['Any unusual process name proves malware. without documenting scope, source, time meaning, or '
                         'limitations.',
                         'The process and connection are leads that need corroboration, not a malware conclusion '
                         'alone.',
                         'Network activity means data was stolen.',
                         'Memory findings never matter without disk artifacts.'],
             'best_index': 1,
             'explanation': 'Process names and network connections can be important leads, but malware conclusions '
                            'require more support such as path, parent/child process, command line, loaded modules, '
                            'code injection indicators, hashes, disk artifacts, or external intelligence.',
             'coaching_note': 'Treat memory indicators as context to investigate, not final labels by themselves.'},
            {'id': 'memory-followup-artifacts',
             'prompt': 'Which follow-up is most useful?',
             'choices': ['Only rename the process as malware in the notes. because the single artifact resolves the '
                         'human-actor question by itself.',
                         'Only look at the desktop wallpaper.',
                         'Review process tree, command line, path, handles, modules, network details, and related disk '
                         'artifacts.',
                         'Ignore timestamps because RAM has none.'],
             'best_index': 2,
             'explanation': 'A memory finding gains meaning when correlated with process relationships, command lines, '
                            'file paths, network endpoints, loaded modules, and disk or log artifacts.',
             'coaching_note': 'Memory analysis is strongest when it feeds a corroborated timeline.'},
            {'id': 'network-overclaim',
             'prompt': 'What should you avoid from a network artifact alone?',
             'choices': ['Attributing the remote IP to a person or proving data exfiltration without more context.',
                         'Documenting local and remote address details. even though the source artifact has not been '
                         'corroborated.',
                         'Recording the plugin/tool version used.',
                         'Correlating memory findings with disk review.'],
             'best_index': 0,
             'explanation': 'Network artifacts may show connection context, but attribution and data-transfer '
                            'conclusions require additional evidence and context.',
             'coaching_note': 'IP address, process, and timestamp are pieces of a story, not the whole story.'}],
  'debrief': 'Memory findings can be high-value leads. Explain the observed artifact, correlate with other sources, '
             'and avoid malware, actor, or exfiltration conclusions until supported.'},
 {'id': 'cloud-sync-local-boundary',
  'title': 'Cloud sync: local artifact or cloud activity?',
  'category': 'Cloud / Browser / File Activity',
  'summary': 'Cloud client artifacts may blur local activity, sync state, and cloud account context.',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_reference_terms': ['Cloud sync', 'OneDrive', 'Local artifact', 'Account context', 'Timeline'],
  'opening_context': 'A laptop contains cloud-sync artifacts. The investigator asks whether a file found locally '
                     'proves it was created on that laptop.',
  'steps': [{'id': 'cloud-local-boundary',
             'prompt': 'What is the safest first distinction?',
             'choices': ['A local file always means it was created on that laptop. without documenting scope, source, '
                         'time meaning, or limitations.',
                         'Cloud-sync folders never store local files.',
                         'The cloud account name proves who created the file.',
                         'Separate local presence from cloud origin, sync activity, and user interaction.'],
             'best_index': 3,
             'explanation': 'Cloud-sync clients can create local artifacts for files that originated elsewhere. Local '
                            'presence, sync timing, creation origin, and user interaction are separate questions.',
             'coaching_note': 'Cloud sync creates tempting shortcuts. Resist them.'},
            {'id': 'cloud-context',
             'prompt': "Which context helps evaluate the file's story?",
             'choices': ['Only the folder name. because the single artifact resolves the human-actor question by '
                         'itself.',
                         'Sync logs, account details, local metadata, app access artifacts, and cloud source records '
                         'if available.',
                         'Only whether the laptop is expensive. even though the source artifact has not been '
                         'corroborated.',
                         'Only the file icon.'],
             'best_index': 1,
             'explanation': 'Sync logs, account identifiers, local timestamps, app histories, link/jump artifacts, and '
                            'cloud provider records can help separate sync from local creation or interaction.',
             'coaching_note': 'Local and cloud sources may both be needed to explain the artifact fairly.'},
            {'id': 'cloud-final-language',
             'prompt': 'Which conclusion language is most careful before cloud records are reviewed?',
             'choices': ['The device user definitely created the file locally. even though the source artifact has not '
                         'been corroborated.',
                         'The cloud provider uploaded it without any user account.',
                         'The file was present in the local synced path; origin and interaction need more support.',
                         'The sync folder proves intent.'],
             'best_index': 2,
             'explanation': 'This statement describes the artifact without overclaiming origin, knowledge, or actor '
                            'identity.',
             'coaching_note': 'Careful language buys time for better evidence.'}],
  'debrief': 'Cloud sync cases need source boundaries. Distinguish local presence, sync process activity, local '
             'interaction, cloud account context, and origin before making stronger claims.'},
 {'id': 'timeline-conflict',
  'title': 'Conflicting timestamps and parser differences',
  'category': 'Timestamps / Validation',
  'summary': 'Two sources disagree on time or meaning, and the examiner needs disciplined interpretation.',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_reference_terms': ['Timestamps', 'Time zone', 'Parser validation', 'Artifact meaning', 'Correlation'],
  'opening_context': 'Two tools or artifacts show different timestamps for what appears to be related activity.',
  'steps': [{'id': 'timestamp-first',
             'prompt': 'What should you check first?',
             'choices': ['Artifact source, timestamp meaning, time zone handling, and tool/parser behavior.',
                         'Pick the timestamp that helps the case theory. without documenting scope, source, time '
                         'meaning, or limitations.',
                         'Assume the newest tool is always right.',
                         'Ignore one source without documenting why.'],
             'best_index': 0,
             'explanation': 'Different artifacts can record different events, use different time bases, or be parsed '
                            'differently. Understand source meaning before resolving conflicts.',
             'coaching_note': 'Timestamp conflicts are often meaning conflicts.'},
            {'id': 'timestamp-correlation',
             'prompt': 'Which next step is strongest?',
             'choices': ['Delete the weaker timestamp from notes. because the single artifact resolves the human-actor '
                         'question by itself.',
                         'Call both times exact proof of the same event.',
                         'Convert everything to local time without recording the original basis.',
                         'Correlate with independent artifacts and document the meaning of each timestamp.'],
             'best_index': 3,
             'explanation': 'Correlation and documentation let the examiner explain uncertainty, tool behavior, and '
                            'why one interpretation is stronger.',
             'coaching_note': 'A good timeline explains why entries are comparable or not comparable.'},
            {'id': 'parser-difference',
             'prompt': 'What should you avoid when tools disagree?',
             'choices': ['Recording tool name and version. even though the source artifact has not been corroborated.',
                         'Treating parser output as unquestionable without checking source data or documentation.',
                         'Reviewing known limitations.',
                         'Testing or validating with known data when needed.'],
             'best_index': 1,
             'explanation': 'Tool output is interpretation of source data. When results matter and conflict, the '
                            'examiner should review source context, tool documentation, and validation/known data '
                            'where appropriate.',
             'coaching_note': 'A conflict is a cue to slow down, not guess faster.'}],
  'debrief': 'Timestamp disagreements should be treated as interpretation problems. Identify source, meaning, time '
             'basis, tool behavior, and corroboration before resolving the timeline.'}]


def search_coaching_paths(query):
    needle = (query or "").strip().lower()
    if not needle:
        return []
    results = []
    for path in COACHING_PATHS:
        parts = [
            path.get("title", ""),
            path.get("category", ""),
            path.get("summary", ""),
            path.get("opening_context", ""),
            path.get("debrief", ""),
        ]
        parts.extend(path.get("related_reference_terms", []))
        for step in path.get("steps", []):
            parts.extend([
                step.get("prompt", ""),
                step.get("explanation", ""),
                step.get("coaching_note", ""),
            ])
            parts.extend(step.get("choices", []))
        if needle in "\n".join(str(part) for part in parts).lower():
            results.append(path)
    return results
