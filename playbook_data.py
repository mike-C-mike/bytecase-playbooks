"""Built-in ByteCase Playbooks content.

The content is intentionally guidance-focused. It does not perform evidence
collection, extraction, parsing, or analysis.
"""

APP_NAME = "ByteCase Playbooks"
APP_SUBTITLE = "Guided Examiner Reference and Learning Companion"
APP_VERSION = "0.10.4"
APP_ATTRIBUTION = "Part of the ByteCase toolset by Forensics Byte."
APP_DOMAIN = "byte-case.com"

PLAYBOOK_BOUNDARY = (
    "ByteCase Playbooks provides reference guidance, learning prompts, and "
    "documentation reminders. It does not replace agency policy, legal authority, "
    "formal training, tool validation, or examiner judgment. It does not perform "
    "acquisition, extraction, parsing, or analysis."
)

PLAYBOOKS = [
    {
        "id": "live_computer_acquisition_ram",
        "title": "Live Computer Acquisition / RAM Capture",
        "category": "Acquisition / Imaging",
        "level": "Intermediate",
        "summary": "Use when a powered-on computer may contain volatile data, encryption context, running processes, or live network activity that could be lost at shutdown.",
        "use_when": [
            "The computer is powered on and live state may matter.",
            "RAM, running processes, network connections, or encryption context may be relevant.",
            "You need a refresher on order of operations before touching a live system.",
        ],
        "avoid_when": [
            "Authority/scope does not permit live collection.",
            "Agency policy requires immediate power removal or seizure only.",
            "Scene safety or legal direction requires a different action.",
        ],
        "steps": [
            {
                "title": "Confirm authority and scope",
                "field_focus": "Confirm what you are allowed to collect before changing a live system.",
                "learning_detail": "Live response can alter the system and may expose information outside the original request. Start by confirming the legal authority, agency policy, case scope, and who approved the action.",
                "why": "This step defines the boundaries for every collection decision that follows. Without scope, it is difficult to justify why volatile data, memory, or targeted files were collected.",
                "tools": ["Warrant/consent/scope paperwork", "Case request", "Agency SOP", "Examiner notes"],
                "artifacts": ["Authority reference", "Scope statement", "Approved collection target", "Known limitations"],
                "cautions": ["Do not expand collection just because the system is accessible.", "Do not treat this playbook as legal advice.", "Record uncertainty instead of guessing."],
                "document": ["Authority type/reference", "Approver/requesting investigator", "Scope limits", "Reason live acquisition was considered"],
            },
            {
                "title": "Document initial system state",
                "field_focus": "Record what is visible and how the machine is connected before taking action.",
                "learning_detail": "Photographs and notes about screen state, power state, network connections, peripherals, open applications, and date/time context help explain what the examiner encountered before collection began.",
                "why": "Live systems change quickly. A clear starting state helps separate examiner actions from the condition encountered at the beginning.",
                "tools": ["Camera", "Notebook", "Screen photographs", "System clock reference"],
                "artifacts": ["Open windows", "Logged-in user context", "Network cables/Wi-Fi", "External devices"],
                "cautions": ["Avoid interacting with the system before documenting visible state.", "Be careful with sensitive on-screen information outside scope."],
                "document": ["Date/time", "Power state", "Visible applications", "Logged-in user if visible", "Network/peripheral status"],
            },
            {
                "title": "Consider network and isolation decisions",
                "field_focus": "Decide whether network connectivity should remain, be isolated, or be documented before changes.",
                "learning_detail": "Network decisions are context-dependent. Disconnecting may stop remote activity but can also destroy active sessions, alter malware behavior, or affect cloud-synced state. Leaving it connected may preserve state but can allow remote changes.",
                "why": "This decision can affect evidence preservation and risk. The reason for the decision matters as much as the decision itself.",
                "tools": ["Network notes", "Photographs", "Faraday/network isolation tools if applicable", "Agency SOP"],
                "artifacts": ["Active connections", "Remote sessions", "Cloud sync state", "Open network shares"],
                "cautions": ["There is not one universal answer.", "Do not disconnect automatically without thinking through impact.", "Document who directed the decision."],
                "document": ["Network state before action", "Decision made", "Reason for decision", "Time of any change"],
            },
            {
                "title": "Prioritize volatile data",
                "field_focus": "Collect the most volatile data before actions that could destroy it.",
                "learning_detail": "Volatile data may include RAM, running processes, active network connections, logged-in sessions, mounted volumes, open files, encryption-related context, and command-line activity. The exact collection order depends on authority, policy, tools, and risk.",
                "why": "Shutdown, reboot, unplugging, or even normal system activity can overwrite or destroy volatile data.",
                "tools": ["RAM capture tool", "Live response scripts", "Built-in OS commands", "Forensic triage tool where approved"],
                "artifacts": ["Memory image", "Process list", "Network connections", "Logged-in users", "Mounted volumes"],
                "cautions": ["Live collection changes the system.", "Malware may react to tools.", "Do not over-collect outside scope."],
                "document": ["Tool names/versions", "Commands/options used", "Output paths", "Start/end times", "Errors"],
            },
            {
                "title": "Capture RAM when justified",
                "field_focus": "Capture memory before shutdown or disk-only imaging when RAM may matter.",
                "learning_detail": "RAM can contain running process data, network connection context, command lines, injected code indicators, encryption-related material, and other volatile artifacts. It should be captured before shutdown when justified and authorized.",
                "why": "Memory is volatile. Once the system powers down, many memory-resident artifacts are lost.",
                "tools": ["Magnet RAM Capture", "FTK Imager memory capture", "WinPmem", "DumpIt", "Belkasoft RAM Capturer"],
                "artifacts": ["Memory image", "Capture log", "Hash value if generated", "Tool output"],
                "cautions": ["Admin privileges may be required.", "Large memory images need adequate destination storage.", "Some endpoint protections may interfere.", "A successful capture still needs later validation/review."],
                "document": ["Capture tool/version", "Output filename", "Destination media", "Hash if available", "Start/end time", "Errors or warnings"],
                "command_examples": [
                    {"label": "Confirm capture output exists", "example": "dir <destination_folder>", "purpose": "Confirm that the expected memory image or tool output was created.", "does_not_prove": "It does not prove the image is complete, valid, or correctly interpreted."},
                    {"label": "Calculate SHA-256 on Windows", "example": "Get-FileHash .\\memory.raw -Algorithm SHA256", "purpose": "Record an integrity value for the captured memory image when appropriate.", "does_not_prove": "A matching hash supports integrity; it does not explain what is in memory."},
                ],
                "does_not_prove": ["A successful capture does not prove that all volatile evidence was collected.", "A hash value does not interpret memory content.", "Tool success does not remove the need to document limitations."],
            },
            {
                "title": "Collect targeted live context if authorized",
                "field_focus": "Capture process, network, user, and system context only when it fits the scope.",
                "learning_detail": "Live context can help explain what was active at the time of acquisition. Common examples include running processes, network connections, logged-in users, mounted volumes, open files, and system time. These are not conclusions by themselves.",
                "why": "Context helps later interpretation of memory and disk artifacts. It also records state that may not exist after shutdown.",
                "tools": ["OS commands", "Live response scripts", "Forensic triage tools", "Screenshots where allowed"],
                "artifacts": ["Process list", "Network connection list", "Logged-in sessions", "Mounted volumes", "System information"],
                "cautions": ["Commands change access times/logs.", "Avoid collecting beyond scope.", "Do not treat live outputs as final findings without corroboration."],
                "document": ["Commands/tools used", "Output locations", "Timestamps", "Known limitations", "Why live context was collected"],
            },
            {
                "title": "Decide next preservation path",
                "field_focus": "Choose whether to image, seize, shut down, or perform targeted collection next.",
                "learning_detail": "After volatile data is addressed, the next decision depends on scope, encryption, device state, available tools, time, and agency policy. Options may include full disk imaging, targeted collection, graceful shutdown, hard power removal, or leaving the system running for another team.",
                "why": "This is where live acquisition transitions into broader preservation. The decision should be explainable later.",
                "tools": ["Write blocker", "Forensic imaging tool", "Targeted collection tool", "Agency SOP"],
                "artifacts": ["Disk image", "Targeted files", "Collection logs", "Hash manifests"],
                "cautions": ["Encryption and mounted volumes can change the best path.", "Do not assume dead-box imaging is always possible after shutdown.", "Document limitations."],
                "document": ["Decision made", "Reason", "Tools/version", "Hash values", "Any deviation from normal process"],
            },
        ],
    },
    {
        "id": "dead_box_computer_imaging",
        "title": "Dead-Box Computer Imaging",
        "category": "Acquisition / Imaging",
        "level": "Foundational",
        "summary": "Use when a powered-off computer or removed storage device is being preserved through a forensic image or documented acquisition process.",
        "use_when": ["The system is powered off.", "Storage media can be imaged with a write blocker or approved process.", "The goal is preservation of storage media."],
        "avoid_when": ["The system is live and volatile data may be critical.", "Encryption risk requires a live-response decision first.", "Authority/scope only allows targeted collection."],
        "steps": [
            {
                "title": "Confirm authority, scope, and target media",
                "field_focus": "Know what storage device or partition you are authorized to image.",
                "learning_detail": "A computer may contain multiple internal drives, removable media, cloud-synced folders, or user profiles. Confirming the target reduces over-collection and helps explain acquisition choices.",
                "why": "Imaging can collect a broad amount of data. Scope controls what should be preserved and how it should be described.",
                "tools": ["Case request", "Warrant/consent", "Asset labels", "Photographs"],
                "artifacts": ["Device identifiers", "Drive serials", "Storage capacity", "Scope notes"],
                "cautions": ["Do not assume every attached storage device is in scope.", "Record uncertainty."],
                "document": ["Authority reference", "Target media", "Make/model/serial", "Capacity", "Condition"],
            },
            {
                "title": "Photograph and document physical condition",
                "field_focus": "Capture the system and storage state before disassembly or connection.",
                "learning_detail": "Physical documentation supports later explanation of how storage media was identified and handled. This includes labels, serial numbers, cables, ports, external damage, and any attached devices.",
                "why": "It creates a record of the device before examiner handling changes the physical configuration.",
                "tools": ["Camera", "Evidence labels", "Notes", "Device inventory form"],
                "artifacts": ["Photos", "Serial numbers", "Connection state", "Condition notes"],
                "cautions": ["Avoid mixing original media and destination media.", "Keep chain-of-custody requirements in mind."],
                "document": ["Photos taken", "Drive identifiers", "Condition", "Any removed components"],
            },
            {
                "title": "Use write protection where applicable",
                "field_focus": "Prevent writes to original media before imaging.",
                "learning_detail": "Hardware or software write protection helps prevent accidental modification of source media. The write-protection method should be appropriate for the media type and validated according to lab process.",
                "why": "Preserving source media integrity is a core acquisition concern.",
                "tools": ["Hardware write blocker", "Software write blocker", "ByteCase Validate record", "Imaging workstation"],
                "artifacts": ["Write blocker model/serial", "Validation record", "Connection method", "Tool logs"],
                "cautions": ["A write blocker should be validated locally.", "Adapters and bridges can affect the setup.", "Some media types need special handling."],
                "document": ["Write blocker/tool used", "Validation reference", "Source/destination identifiers", "Connection path"],
            },
            {
                "title": "Create forensic image or documented acquisition",
                "field_focus": "Acquire the source media using an approved imaging process.",
                "learning_detail": "A forensic image should preserve the selected source media as completely as practical within the tool, format, and scope. Common formats include raw/dd, E01/Ex01, or other lab-approved formats.",
                "why": "A repeatable image allows analysis without repeatedly handling original media.",
                "tools": ["FTK Imager", "Magnet ACQUIRE", "EnCase Imager", "Guymager", "dc3dd/dd where appropriate"],
                "artifacts": ["Image file", "Acquisition log", "Hash values", "Segment files"],
                "cautions": ["Confirm destination capacity.", "Record errors/bad sectors.", "Do not ignore tool warnings."],
                "document": ["Tool/version", "Image format", "Source/destination", "Start/end time", "Errors", "Hash values"],
            },
            {
                "title": "Verify image integrity",
                "field_focus": "Confirm the acquisition hash/verification result before moving forward.",
                "learning_detail": "Hash verification helps show that the acquired output matches what the tool calculated during acquisition. Later rehashing can support continued integrity checks.",
                "why": "Integrity documentation supports repeatability and later review.",
                "tools": ["Acquisition tool verification", "ByteCase Verify", "Hash manifest"],
                "artifacts": ["MD5/SHA-1/SHA-256 values where policy allows", "Verification log", "Manifest"],
                "cautions": ["Hash algorithms and policies vary.", "A matching hash does not prove relevance or meaning; it supports integrity."],
                "document": ["Algorithm", "Hash value", "Verification result", "Tool/version", "Any mismatch or limitation"],
            },
        ],
    },
    {
        "id": "mobile_device_extraction",
        "title": "Mobile Device Extraction Refresher",
        "category": "Extraction / Acquisition",
        "level": "Foundational",
        "summary": "Use when preparing for or reviewing a phone/tablet extraction workflow and related documentation considerations.",
        "use_when": ["A mobile device is within scope.", "The examiner needs a refresher on extraction types and documentation.", "The device state, lock status, or network status may affect handling."],
        "avoid_when": ["Authority/scope does not permit mobile extraction.", "Device handling must be directed by another lab/SOP.", "Safety or urgent conditions require a different process."],
        "steps": [
            {
                "title": "Confirm authority, scope, and device identity",
                "field_focus": "Confirm what device and data categories are authorized before extraction.",
                "learning_detail": "Mobile devices can contain highly personal data across apps, accounts, cloud services, messages, photos, location, and browser activity. Scope should be clear before extraction or review.",
                "why": "Mobile extractions can be broad. Clear scope helps avoid unnecessary collection or review.",
                "tools": ["Case request", "Warrant/consent", "Device intake form", "Photographs"],
                "artifacts": ["Make/model", "Serial/IMEI/MEID", "Phone number", "Carrier", "Lock state"],
                "cautions": ["Do not assume cloud data is included in device authority.", "Do not bypass scope because a tool can parse something."],
                "document": ["Authority reference", "Device identifiers", "Lock state", "Scope limits", "Requested extraction type"],
            },
            {
                "title": "Document condition and connectivity",
                "field_focus": "Record power state, lock state, visible notifications, and network isolation decisions.",
                "learning_detail": "Mobile device handling may require balancing preservation, battery, lock state, remote wipe risk, and network isolation. Device state can affect available extraction methods.",
                "why": "The initial state can explain what extraction options were possible and why handling decisions were made.",
                "tools": ["Camera", "Faraday bag/box if used", "Power source", "Device notes"],
                "artifacts": ["Screen state", "Battery level", "SIM/SD presence", "Network indicators", "Notifications"],
                "cautions": ["Network isolation can alter cloud/app state.", "Power loss can change access options.", "Do not interact more than necessary before documenting."],
                "document": ["Power/lock state", "Battery", "Network status", "Isolation method", "Visible condition"],
            },
            {
                "title": "Choose extraction approach",
                "field_focus": "Identify the most appropriate extraction type supported by authority, device state, and tool capability.",
                "learning_detail": "Common mobile collection types include logical, file system, physical where supported, cloud/account return where authorized, backup-based collection, and manual documentation. Availability depends on platform, OS version, lock state, tool support, and legal scope.",
                "why": "Extraction type affects what data is collected, what may be missing, and how results should be explained.",
                "tools": ["Cellebrite UFED/Physical Analyzer", "Magnet AXIOM", "GrayKey", "MSAB XRY", "Oxygen Forensic Detective", "Vendor backups where appropriate"],
                "artifacts": ["Extraction type", "Tool logs", "Unsupported apps", "Partial extraction notes", "Cloud/account artifacts if authorized"],
                "cautions": ["More advanced extraction does not automatically mean complete truth.", "Unsupported apps and encrypted data must be documented.", "Cloud authority is separate from device capability."],
                "document": ["Tool/version", "Extraction type", "Device OS/version", "Success/failure", "Limitations", "Output location"],
            },
            {
                "title": "Preserve extraction outputs and logs",
                "field_focus": "Save extraction files, reports, logs, and metadata in a structured case folder.",
                "learning_detail": "Mobile tools often produce source extraction containers, parsed databases, reports, logs, and exports. The source extraction and logs are usually more important than a single examiner-facing report.",
                "why": "Preserving outputs supports repeatability and review.",
                "tools": ["Tool export folder", "ByteCase Acquire", "ByteCase Verify", "Case storage"],
                "artifacts": ["Extraction container", "Tool logs", "Reports", "Hash manifests", "Screenshots"],
                "cautions": ["Do not rely only on a PDF report.", "Record output folder paths and tool-generated logs.", "Protect sensitive data."],
                "document": ["Output path", "Generated files", "Hash values if used", "Tool logs", "Known limits"],
            },
            {
                "title": "Plan common artifact review areas",
                "field_focus": "Review only artifact areas that fit the case scope and investigative question.",
                "learning_detail": "Common mobile artifact areas include messages, calls, contacts, photos/videos, app data, downloads, browser activity, location, accounts, cloud sync indicators, and deleted/recovered items where supported. Presence of an artifact does not prove user intent by itself.",
                "why": "A scoped review plan helps avoid unfocused searching and overclaiming.",
                "tools": ["Cellebrite PA", "Magnet AXIOM", "Oxygen", "SQLite viewers", "Manual verification where appropriate"],
                "artifacts": ["Messages", "Calls", "Contacts", "Media", "App data", "Browser", "Location", "Accounts"],
                "cautions": ["Tool parsing can be incomplete or wrong.", "Timestamps/time zones matter.", "Corroborate important artifacts.", "Document unsupported apps."],
                "document": ["Artifact areas reviewed", "Why selected", "Tool/version", "Limitations", "Manual verification steps"],
            },
        ],
    },
    {
        "id": "memory_ram_analysis_volatility",
        "title": "Memory / RAM Analysis Refresher",
        "category": "Analysis",
        "level": "Intermediate",
        "summary": "Use when reviewing a memory image and needing an ordered refresher on common memory-analysis questions, especially with Volatility-style workflows.",
        "use_when": ["A memory image has been captured.", "You need a structured review order for RAM analysis.", "You want reminders about what plugin output can and cannot prove."],
        "avoid_when": ["The memory image source/integrity is unknown and cannot be documented.", "The task is outside scope or training.", "A qualified malware/memory specialist should handle the matter."],
        "steps": [
            {
                "title": "Confirm memory image source and integrity",
                "field_focus": "Know where the memory image came from before interpreting it.",
                "learning_detail": "Document the acquisition tool, version, source machine, output filename, acquisition time, hash values if available, and any errors. Work from a copy when practical.",
                "why": "Memory analysis findings depend on the reliability and context of the image being reviewed.",
                "tools": ["ByteCase Acquire", "ByteCase Verify", "Capture tool logs", "Case notes"],
                "artifacts": ["Memory image", "Hash values", "Acquisition log", "System context"],
                "cautions": ["Do not analyze an undocumented image as though it is fully trusted.", "Hash match supports integrity, not interpretation."],
                "document": ["Image source", "Capture tool/version", "Hash values", "Known errors", "Working copy path"],
            },
            {
                "title": "Identify OS and memory context",
                "field_focus": "Start with basic image information before running deeper plugins.",
                "learning_detail": "Volatility 3 commonly uses symbol-based analysis. Start with basic image info to understand OS/build details and whether the tool can interpret the image correctly.",
                "why": "Wrong OS context or missing symbols can produce incomplete or misleading output.",
                "tools": ["Volatility 3 windows.info", "Volatility Workbench", "Tool documentation"],
                "artifacts": ["OS/build details", "Symbol status", "Image metadata"],
                "cautions": ["Plugin errors may reflect symbol/tool issues rather than evidence facts.", "Record command output and errors."],
                "document": ["Command/tool used", "OS/build output", "Symbol issues", "Tool version"],
                "command_examples": [
                    {"label": "Volatility 3 image information", "example": "vol.py -f memory.raw windows.info", "purpose": "Start by identifying basic Windows memory image context and symbol/tool interpretation status.", "does_not_prove": "It does not prove suspicious activity or user action."},
                ],
                "does_not_prove": ["OS/build output does not prove user activity.", "A plugin error does not automatically prove tampering or corruption.", "Symbol status must be documented before deeper reliance on plugin output."],
            },
            {
                "title": "Review processes and process tree",
                "field_focus": "Look at running process list and parent/child relationships first.",
                "learning_detail": "Process listings and trees help establish what was active and how processes relate. Suspicious names, paths, parent-child relationships, or unexpected user contexts may require follow-up, but are not conclusions by themselves.",
                "why": "Process context gives a map for later network, command-line, DLL, handle, and injection review.",
                "tools": ["Volatility 3 windows.pslist", "Volatility 3 windows.pstree", "Volatility 3 windows.psscan"],
                "artifacts": ["Process names", "PIDs/PPIDs", "Start times", "Parent-child relationships"],
                "cautions": ["A process name alone is not proof of malware.", "Terminated/hidden process views may differ by plugin."],
                "document": ["Commands used", "Processes of interest", "Why selected", "Screenshots/output paths"],
                "command_examples": [
                    {"label": "Process list", "example": "vol.py -f memory.raw windows.pslist", "purpose": "List active processes visible through a standard process walk.", "does_not_prove": "A process name alone does not prove malware or user intent."},
                    {"label": "Process tree", "example": "vol.py -f memory.raw windows.pstree", "purpose": "Review parent/child process relationships.", "does_not_prove": "A strange parent/child relationship is a lead, not a final conclusion."},
                    {"label": "Pool scan process view", "example": "vol.py -f memory.raw windows.psscan", "purpose": "Look for process objects that may not appear in the normal process list.", "does_not_prove": "Differences between plugin views require explanation and corroboration."},
                ],
                "does_not_prove": ["A process name by itself does not prove malicious activity.", "A suspicious process relationship should be treated as a lead.", "Hidden or terminated process indicators need corroboration."],
            },
            {
                "title": "Review command lines and network connections",
                "field_focus": "Connect process context to command-line arguments and network activity.",
                "learning_detail": "Command-line arguments can explain how a process launched. Network connections can show listening ports, remote connections, and process-associated communication. Both require context and corroboration.",
                "why": "This step often turns a process list into a more meaningful lead set.",
                "tools": ["Volatility 3 windows.cmdline", "Volatility 3 windows.netscan", "OS/network logs where available"],
                "artifacts": ["Command lines", "Local/remote addresses", "Ports", "Owning PIDs"],
                "cautions": ["IP presence is not attribution.", "Connections may be stale or normal.", "Time context matters."],
                "document": ["Commands/plugins", "Relevant rows", "Associated PID/process", "Limitations"],
                "command_examples": [
                    {"label": "Command-line arguments", "example": "vol.py -f memory.raw windows.cmdline", "purpose": "Review command-line arguments associated with processes.", "does_not_prove": "Command-line text still needs context and corroboration."},
                    {"label": "Network scan", "example": "vol.py -f memory.raw windows.netscan", "purpose": "Review network endpoints, ports, and process associations visible in memory.", "does_not_prove": "An IP address is not attribution, and a connection row may be stale or benign."},
                ],
                "does_not_prove": ["Network connection output does not prove attribution.", "A command line does not always prove who typed it.", "Time context and corroboration are required."],
            },
            {
                "title": "Review modules, handles, and injection indicators",
                "field_focus": "Use deeper plugins to investigate selected leads, not to generate unsupported conclusions.",
                "learning_detail": "DLL/module listings, handles, and suspicious memory region indicators can help investigate unusual processes. Findings should be corroborated with disk artifacts, logs, threat intel, or additional analysis where appropriate.",
                "why": "Deeper plugins are most useful when driven by specific questions from earlier review.",
                "tools": ["Volatility 3 windows.dlllist", "Volatility 3 windows.handles", "Volatility 3 windows.malfind", "YARA where authorized/trained"],
                "artifacts": ["Loaded modules", "File/registry handles", "Suspicious memory regions", "Dumped memory segments"],
                "cautions": ["malfind-style output is a lead, not a final malware conclusion.", "False positives happen.", "Dumping content may create sensitive derivative artifacts."],
                "document": ["Reason plugin was run", "Output path", "Findings needing corroboration", "Limitations"],
                "command_examples": [
                    {"label": "Loaded modules", "example": "vol.py -f memory.raw windows.dlllist --pid <PID>", "purpose": "Review modules loaded by a process of interest.", "does_not_prove": "A module list by itself does not prove malicious injection."},
                    {"label": "Handles", "example": "vol.py -f memory.raw windows.handles --pid <PID>", "purpose": "Review files, registry keys, events, and other objects referenced by a process.", "does_not_prove": "A handle shows reference context, not necessarily user intent."},
                    {"label": "Injection indicators", "example": "vol.py -f memory.raw windows.malfind --pid <PID>", "purpose": "Look for memory regions that may warrant deeper review.", "does_not_prove": "malfind-style output is a lead; false positives and benign explanations are possible."},
                ],
                "does_not_prove": ["malfind output does not equal a final malware conclusion.", "Loaded modules and handles must be interpreted with process and system context.", "Dumped memory regions may require separate handling and documentation."],
            },
            {
                "title": "Document conclusions carefully",
                "field_focus": "Separate observed tool output from examiner interpretation.",
                "learning_detail": "Memory analysis can produce valuable leads, but report language should distinguish observed output, corroborated findings, limitations, and unresolved questions.",
                "why": "Clear language prevents overclaiming and makes review easier.",
                "tools": ["ByteCase Notes", "Artifact index", "Screenshots/exports", "Peer review where available"],
                "artifacts": ["Referenced output", "Artifact IDs", "Screenshots", "Limitations"],
                "cautions": ["Do not claim user intent from one artifact.", "Do not equate suspicious with malicious without support.", "Record tool limitations."],
                "document": ["What was observed", "How it was observed", "What it may indicate", "What it does not prove", "Supporting artifacts"],
                "does_not_prove": ["A single plugin result rarely proves intent by itself.", "Suspicious does not automatically mean malicious.", "Tool output should be separated from examiner interpretation."],
            },
        ],
    },
    {
        "id": "windows_artifact_review_refresher",
        "title": "Windows Artifact Review Refresher",
        "category": "Analysis",
        "level": "Beginner / Intermediate",
        "summary": "Use when reviewing a Windows computer image or logical collection and needing a refresher on common artifact areas, what they may help answer, and what they do not prove by themselves.",
        "use_when": [
            "A Windows computer image, mounted image, or targeted collection is ready for review.",
            "You need a structured refresher on common Windows artifact areas.",
            "You want reminders about documentation language and common overclaims.",
        ],
        "avoid_when": [
            "The task is outside legal authority, scope, training, or agency policy.",
            "You are being asked to make a conclusion that needs deeper specialist review.",
            "The source image or collection cannot be documented.",
        ],
        "steps": [
            {
                "title": "Confirm source image, scope, and working copy",
                "field_focus": "Start with source context before reviewing artifacts.",
                "learning_detail": "A Windows artifact review should begin with the acquisition source, image/collection type, case scope, and whether you are working from a protected copy. The artifact review is only as strong as its preservation and documentation foundation.",
                "why": "Source context prevents the examiner from treating an incomplete targeted collection like a full-disk image, or reviewing artifacts outside the approved question.",
                "tools": ["ByteCase Acquire", "ByteCase Verify", "Forensic image mounter", "Case request/scope documents"],
                "artifacts": ["Image/collection source", "Hash manifest", "Mount path", "Scope statement", "Known collection limits"],
                "cautions": ["Do not assume a targeted collection contains all expected artifacts.", "Do not skip preservation context just because a forensic suite opens the image."],
                "document": ["Source media/image", "Hash/integrity status", "Collection type", "Scope limits", "Working copy or mount path"],
            },
            {
                "title": "Identify users, profiles, and system context",
                "field_focus": "Establish which user profiles and system areas are relevant before diving into artifacts.",
                "learning_detail": "User profiles help frame browser data, downloads, recent files, desktop files, recycle bin content, and application artifacts. System context helps identify OS version, time zone, installed applications, and available logs.",
                "why": "Most Windows artifacts become more meaningful when tied to a user profile, system timeline, and OS context.",
                "tools": ["Autopsy", "Magnet AXIOM", "EnCase/FTK-style file browser", "Registry viewer", "Timeline tool"],
                "artifacts": ["Users folder", "NTUSER.DAT", "SOFTWARE/SYSTEM hives", "Time zone settings", "Installed programs"],
                "cautions": ["A profile folder does not prove who used the machine at a specific time.", "Time zone and clock issues can affect interpretation."],
                "document": ["Relevant profiles", "OS/build details", "Time zone/clock notes", "Tool version", "Limitations"],
            },
            {
                "title": "Review common user activity artifacts",
                "field_focus": "Look for artifacts that help answer what the user or system interacted with.",
                "learning_detail": "Common user activity areas include LNK files, Jump Lists, RecentDocs, ShellBags, UserAssist, Prefetch, Downloads, Desktop/Documents folders, and Recycle Bin. Each artifact answers a different question and has different limits.",
                "why": "Reviewing artifacts by question helps avoid turning a pile of parsed output into unsupported conclusions.",
                "tools": ["LECmd/JLECmd", "RECmd", "PECmd", "Autopsy", "Magnet AXIOM", "Timeline Explorer"],
                "artifacts": ["LNK files", "Jump Lists", "RecentDocs", "ShellBags", "UserAssist", "Prefetch", "Recycle Bin"],
                "cautions": ["Existence of a file reference does not always prove the user opened the file.", "Prefetch indicates execution context, not necessarily user intent.", "Parser output should be validated when important."],
                "document": ["Artifact source path", "Parser/tool version", "Relevant timestamps", "User/profile association", "Interpretation limits"],
            },
            {
                "title": "Review browser, download, and cloud-sync areas",
                "field_focus": "Review Internet and sync artifacts in context with the case scope.",
                "learning_detail": "Browser history, cache, downloads, cookies, autofill, bookmarks, extensions, and cloud sync folders can help answer access, download, upload, and account-context questions. Browser artifacts often need careful timestamp and profile interpretation.",
                "why": "Internet and cloud activity are common in many cases, but they are easy to overstate without context.",
                "tools": ["Browser History Examiner", "Hindsight", "Autopsy", "Magnet AXIOM", "SQLite viewer"],
                "artifacts": ["Chrome/Edge/Firefox profiles", "History databases", "Downloads tables", "Cache", "OneDrive/Dropbox/Google Drive folders", "Sync logs"],
                "cautions": ["Visited URL does not always prove intentional viewing by a specific person.", "Cloud sync folders may contain remote-synced files.", "Private browsing may reduce local artifacts."],
                "document": ["Browser/profile path", "Artifact type", "Timestamps and time zone", "Account context", "What the artifact does and does not show"],
            },
            {
                "title": "Corroborate and record limitations",
                "field_focus": "Use multiple artifacts where possible and separate observation from interpretation.",
                "learning_detail": "A stronger review ties multiple artifacts together: file system metadata, registry artifacts, browser records, logs, thumbnails, or application data. Limitations should be documented clearly when artifacts are missing, incomplete, unsupported, or outside scope.",
                "why": "Corroboration and limitations make the work more defensible and easier to review later.",
                "tools": ["ByteCase Notes", "ByteCase Verify", "Timeline tools", "Forensic suite reports"],
                "artifacts": ["Artifact index", "Screenshots", "Exported parser output", "Timeline entries", "Hash manifests"],
                "cautions": ["Do not turn one artifact into a broad conclusion.", "Record unsupported parsers or failed ingest modules.", "Missing artifacts may result from scope, collection type, settings, or normal system behavior."],
                "document": ["Corroborating artifacts", "Contradicting/unclear items", "Tool limitations", "Examiner notes", "Artifact references"],
            },
        ],
    },
    {
        "id": "external_media_hash_copy_refresher",
        "title": "External Media Hash / Copy Refresher",
        "category": "Acquisition / Imaging",
        "level": "Beginner",
        "summary": "Use when handling USB drives, SD cards, external drives, or other removable media where the task is to preserve, hash, copy, or document media contents.",
        "use_when": [
            "You are working with removable media or a small external storage device.",
            "The task may be hash-only, targeted copy, or full imaging depending on scope.",
            "You need a reminder about write protection, labels, and output documentation.",
        ],
        "avoid_when": [
            "The media appears damaged and should be handled by a specialist.",
            "The request requires capabilities outside your tools/training.",
            "Agency policy requires a different preservation method.",
        ],
        "steps": [
            {
                "title": "Document media before connection",
                "field_focus": "Record labels, markings, condition, and identifiers before connecting media.",
                "learning_detail": "Photographing and documenting removable media before connection helps preserve the condition encountered and supports later chain/context notes.",
                "why": "Small media can be mislabeled, swapped, or physically altered. Pre-connection documentation reduces ambiguity.",
                "tools": ["Camera", "Evidence label", "ByteCase Intake", "ByteCase Acquire"],
                "artifacts": ["Media photos", "Make/model", "Serial number", "Capacity", "Evidence item number"],
                "cautions": ["Do not rely only on written labels.", "Avoid connecting unknown media to non-forensic systems."],
                "document": ["Item number", "Media type", "Visible identifiers", "Condition", "Photographs taken"],
            },
            {
                "title": "Choose write protection and acquisition approach",
                "field_focus": "Decide whether full imaging, logical copy, or hash-only work fits the request.",
                "learning_detail": "Removable media can often be imaged through a hardware write blocker, software write protection, or tool-specific workflow. A targeted copy may be appropriate when scope is limited, but the limitation should be clear.",
                "why": "The preservation method affects what can be said later about completeness and integrity.",
                "tools": ["Hardware write blocker", "Software write blocker", "FTK Imager", "Guymager", "dc3dd/dd where trained", "ByteCase Validate"],
                "artifacts": ["Full image", "Logical copy", "Hash manifest", "Tool log", "Write blocker validation record"],
                "cautions": ["Do not claim a targeted copy is a full image.", "Validate write-blocking process where appropriate.", "Document why the method was selected."],
                "document": ["Write protection method", "Tool/version", "Acquisition type", "Reason for method", "Validation reference if used"],
            },
            {
                "title": "Hash source and outputs where appropriate",
                "field_focus": "Use hashes to support integrity checks for media, images, copied files, or exported results.",
                "learning_detail": "Hashing helps detect changes to data between preservation, transfer, and later review. Hashes support integrity; they do not explain what a file means or who used it.",
                "why": "Hash documentation makes later rechecks and court/report preparation easier.",
                "tools": ["ByteCase Verify", "FTK Imager", "hashdeep/md5deep", "Forensic suite hashing"],
                "artifacts": ["MD5/SHA-256 hashes", "Hash manifest", "Verification report", "Tool log"],
                "cautions": ["Use agency-approved hash algorithms.", "File-level hashes and image-level hashes answer different questions.", "A matching hash is not an analysis conclusion."],
                "document": ["Algorithm", "Hash tool/version", "Source/output hashed", "Manifest path", "Verification result"],
            },
            {
                "title": "Preserve outputs and record limitations",
                "field_focus": "Keep the copied/imaged output, logs, hashes, and notes together.",
                "learning_detail": "A clean output packet should make it easy to understand what was handled, how it was preserved, where outputs are stored, and what limitations applied.",
                "why": "Small media tasks can look simple, but missing logs or unclear scope can create problems later.",
                "tools": ["ByteCase Acquire", "ByteCase Verify", "ByteCase Notes", "Agency storage location"],
                "artifacts": ["Image/copy output", "Logs", "Hash manifests", "Notes", "Photos"],
                "cautions": ["Do not mix evidence outputs with unrelated working files.", "Do not overwrite prior exports without documenting it."],
                "document": ["Output folder", "Files created", "Any errors", "Limitations", "Next review step"],
            },
        ],
    }
]



ARTIFACT_AREAS = [
    {
        "id": "windows_execution",
        "category": "Windows",
        "title": "Program execution indicators",
        "helps_answer": "May help evaluate whether an application, script, command shell, or executable appears to have run, been prepared to run, or been inventoried on a Windows system.",
        "where_to_look": ["Prefetch, when enabled and available", "Amcache and ShimCache-style program inventory artifacts", "UserAssist and related user activity artifacts", "Windows Event Logs", "LNK and Jump List context", "EDR, application, or endpoint logs when available"],
        "tools": ["KAPE", "Eric Zimmerman tools such as PECmd, AppCompatCacheParser, AmcacheParser, RECmd", "Registry Explorer", "Timeline Explorer", "Autopsy", "Commercial forensic suites"],
        "cautions": ["Execution indicators do not prove who personally ran the program.", "Some artifacts show inventory, presence, or interaction rather than confirmed execution.", "Parser support, OS version, artifact meaning, time zone, and system clock must be considered."],
        "document": ["Artifact source and path", "Tool/parser/version", "Timestamp meaning", "Associated user profile if supported", "Corroborating sources", "Limitations or missing artifacts"],
        "related_playbooks": ["Windows Artifact Review Refresher", "Memory / RAM Analysis Refresher"],
    },
    {
        "id": "windows_file_access",
        "category": "Windows",
        "title": "File access and user activity indicators",
        "helps_answer": "May help evaluate whether files, folders, removable paths, recent items, or application documents appear to have been opened, viewed, selected, or interacted with.",
        "where_to_look": ["LNK files", "Jump Lists", "RecentDocs and MRU-style registry artifacts", "Shellbags", "Office recent files", "Thumbnail/preview/cache artifacts where relevant", "Cloud sync client logs and local metadata"],
        "tools": ["LECmd", "JLECmd", "ShellBags Explorer", "Registry Explorer", "Timeline Explorer", "Autopsy", "Commercial forensic suites"],
        "cautions": ["A recent-file artifact does not prove the named person personally opened the file.", "Preview panes, indexing, sync clients, application behavior, and automated processes can create activity traces.", "File access artifacts should be tied to user/session/device-control context when attribution matters."],
        "document": ["Artifact family", "User profile path", "Referenced file path", "Timestamp type", "Whether source file was present", "Corroborating user/session/activity context"],
        "related_playbooks": ["Windows Artifact Review Refresher"],
    },
    {
        "id": "windows_logon_sessions",
        "category": "Windows",
        "title": "Logon, account, and session indicators",
        "helps_answer": "May help evaluate which accounts or sessions appear active, logged on, recently used, or associated with activity on a Windows system.",
        "where_to_look": ["Security Event Log logon/logoff events where available", "User profile folders and NTUSER.DAT", "RDP and Terminal Services event logs", "SRUM and network profile context", "Recent user activity artifacts", "System clock/time zone settings"],
        "tools": ["Event Log Explorer or Windows Event Viewer", "EvtxECmd", "Registry Explorer", "KAPE", "Timeline Explorer", "Commercial forensic suites"],
        "cautions": ["A Windows account name does not automatically identify the human actor.", "Cached, service, network, remote, and automated logons can look different and need context.", "Shared accounts, shared passwords, remote access, and malware/automation can weaken attribution."],
        "document": ["Account/profile identifiers", "Logon type or session context when known", "Event IDs or artifact sources", "Time zone and clock context", "Corroborating possession/access/admission context"],
        "related_playbooks": ["Windows Artifact Review Refresher", "Live Computer Acquisition / RAM Capture"],
    },
    {
        "id": "windows_event_logs",
        "category": "Windows",
        "title": "Windows event and system activity logs",
        "helps_answer": "May help evaluate system startup/shutdown, service activity, logons, device installs, remote access, application events, and other OS-level activity.",
        "where_to_look": ["System, Security, Application, PowerShell, Terminal Services, and Setup event logs", "Windows Defender and security product logs where available", "Task Scheduler logs", "SetupAPI logs", "Windows Update and service logs"],
        "tools": ["EvtxECmd", "Event Log Explorer", "Windows Event Viewer", "KAPE", "Timeline Explorer", "Commercial forensic suites"],
        "cautions": ["Event logs can be absent, rolled over, cleared, incomplete, or disabled.", "Event presence and absence both require careful interpretation.", "Event IDs require OS/version context and should not be overgeneralized."],
        "document": ["Log name and event ID", "Provider/source", "Timestamp and time zone", "Record number if applicable", "Parser/version", "Known gaps or cleared logs"],
        "related_playbooks": ["Windows Artifact Review Refresher"],
    },
    {
        "id": "usb_devices",
        "category": "Windows",
        "title": "USB / external device connection indicators",
        "helps_answer": "May help evaluate whether a removable device appears to have been connected to a Windows system and whether other artifacts may relate that device to file activity.",
        "where_to_look": ["USBSTOR and related device registry artifacts", "MountedDevices", "SetupAPI logs", "Event logs", "LNK and Jump Lists pointing to removable paths", "Volume serial numbers and drive letters", "Device install timestamps"],
        "tools": ["Registry Explorer", "USB-focused parsers", "RECmd", "SetupAPI parsers", "Timeline tools", "Autopsy", "Commercial forensic suites"],
        "cautions": ["A USB connection does not prove file transfer.", "A connected device does not prove which person connected it.", "Device identifiers can be missing, reused, ambiguous, or parsed differently across tools."],
        "document": ["Device make/model/serial if available", "Volume serial", "First/last connection indicators", "Drive letter/path context", "User association indicators", "File access artifacts linked to removable paths"],
        "related_playbooks": ["External Media Hash / Copy Refresher", "Windows Artifact Review Refresher"],
    },
    {
        "id": "external_media_file_movement",
        "category": "External Media",
        "title": "External media file movement indicators",
        "helps_answer": "May help evaluate whether files may have been copied to, copied from, opened from, or staged around removable media.",
        "where_to_look": ["LNK and Jump Lists referencing removable paths", "Recent files and MRUs", "Shellbags for removable folders", "File system timestamps on source/destination", "USB connection artifacts", "Application logs", "Cloud sync or archive tool logs"],
        "tools": ["LECmd", "JLECmd", "ShellBags Explorer", "MFTECmd", "Timeline Explorer", "KAPE", "Commercial forensic suites"],
        "cautions": ["File movement is usually inferred from multiple artifacts; one artifact alone may be insufficient.", "Opening from removable media is not the same as copying to removable media.", "Timestamp changes can result from normal application or filesystem behavior."],
        "document": ["Source and destination paths", "Device identifiers", "Relevant timestamps and meanings", "Corroborating artifacts", "Alternative explanations", "Missing or unavailable artifacts"],
        "related_playbooks": ["External Media Hash / Copy Refresher", "Windows Artifact Review Refresher"],
    },
    {
        "id": "browser_activity",
        "category": "Browser",
        "title": "Browser activity indicators",
        "helps_answer": "May help evaluate web activity, searches, downloads, sessions, account use, browser profiles, or web-application context.",
        "where_to_look": ["Browser history", "Downloads", "Cookies/session artifacts", "Cache", "Form history and search terms", "Extensions", "Browser profile/account sync context", "Web app local storage"],
        "tools": ["Browser-focused forensic parsers", "Hindsight", "SQLite viewers", "KAPE", "Autopsy", "Commercial forensic suites"],
        "cautions": ["A browser record does not always prove intentional visit by a specific person.", "Redirects, popups, embedded content, browser sync, previews, and application webviews can create records.", "A download record does not prove a file was opened, understood, or intentionally used."],
        "document": ["Browser and profile", "Artifact table/source", "URL/download path", "Timestamp meaning", "Account/session indicators", "Corroborating file access or user activity"],
        "related_playbooks": ["Windows Artifact Review Refresher"],
    },
    {
        "id": "cloud_sync",
        "category": "Cloud / Sync",
        "title": "Cloud sync and local cloud-client indicators",
        "helps_answer": "May help distinguish local device activity from cloud-synced, web, multi-device, or account-driven activity.",
        "where_to_look": ["OneDrive, Google Drive, Dropbox, iCloud, or other sync client folders", "Sync client logs and metadata", "Local placeholders/hydration state where available", "Browser cloud-service records", "Account/session artifacts", "File system timestamps and cloud metadata exports where authorized"],
        "tools": ["KAPE", "SQLite viewers", "Log viewers", "Cloud/provider exports where authorized", "Commercial forensic suites", "Manual artifact review"],
        "cautions": ["A synced file on a device does not always prove it was created, opened, or downloaded by that device user.", "Cloud account authority may be separate from device authority.", "Placeholder files, offline files, and sync conflicts can complicate interpretation."],
        "document": ["Provider/client", "Account identifiers", "Local path and sync state", "Source of cloud data", "Authority/scope", "Timestamp meanings and limitations"],
        "related_playbooks": ["Windows Artifact Review Refresher", "Mobile Device Extraction Refresher"],
    },
    {
        "id": "remote_access_automation",
        "category": "Remote Access / Automation",
        "title": "Remote access, automation, and scheduled activity indicators",
        "helps_answer": "May help evaluate whether observed activity could relate to remote access tools, scheduled tasks, scripts, automation, malware, or administrative activity.",
        "where_to_look": ["RDP and Terminal Services logs", "Remote access application logs", "PowerShell logs", "Scheduled Tasks", "Services", "Startup items", "Process command lines", "Network connections", "EDR/security logs if available"],
        "tools": ["Autoruns", "EvtxECmd", "PowerShell log review", "KAPE", "Volatility", "Timeline Explorer", "Commercial forensic suites"],
        "cautions": ["Remote access can create activity that appears local without broader context.", "Automation or scheduled activity can run without a person actively typing at that moment.", "Tool presence is not automatically malicious or unauthorized."],
        "document": ["Remote tool names/versions if known", "Session/account context", "Source/destination IPs where available", "Task/service/script details", "Timeline correlation", "Alternative explanations"],
        "related_playbooks": ["Memory / RAM Analysis Refresher", "Windows Artifact Review Refresher"],
    },
    {
        "id": "memory_processes",
        "category": "Memory / RAM",
        "title": "Processes, command lines, and network context",
        "helps_answer": "May help review what was active in memory, including process relationships, command-line arguments, network connections, handles, loaded modules, and live context.",
        "where_to_look": ["Process list", "Process tree", "Command line output", "Network connection plugins", "Loaded DLL/modules", "Handles/files/registry references", "Memory strings or targeted carving where appropriate"],
        "tools": ["Volatility 3", "Volatility Workbench", "MemProcFS", "Redline-style triage where appropriate", "Timeline/correlation tools", "Commercial memory analysis support"],
        "cautions": ["A suspicious process name does not prove malware.", "An IP address is not attribution.", "Command-line evidence on a device does not prove which person typed or initiated it without supporting context."],
        "document": ["Memory image hash", "Tool/version", "Plugin/command", "PID/process relationship", "Timestamps if available", "Corroborating disk/log artifacts"],
        "related_playbooks": ["Memory / RAM Analysis Refresher", "Live Computer Acquisition / RAM Capture"],
    },
    {
        "id": "encryption_live_state",
        "category": "Encryption / Live State",
        "title": "BitLocker, mounted volumes, and encryption-related volatile context",
        "helps_answer": "May help evaluate whether a powered-on encrypted system has live state that could be lost during shutdown, such as mounted volumes, logged-in sessions, or memory-resident encryption context.",
        "where_to_look": ["Visible lock/power/login state", "Mounted volumes", "BitLocker status and recovery/key protector information where authorized", "RAM capture", "Live process/session/network context", "Tool logs and photographs"],
        "tools": ["RAM capture tools such as Magnet RAM Capture, FTK Imager memory capture, WinPmem, DumpIt, Belkasoft RAM Capturer", "Built-in Windows commands where authorized", "Volatility", "Acquisition notes/photos", "Commercial forensic suites"],
        "cautions": ["Do not claim a BitLocker key or recovery key is present in RAM unless the capture is examined and corroborated.", "Live collection changes the system and must be authorized and documented.", "Powering down may remove access to mounted encrypted volumes or volatile context."],
        "document": ["Power/lock/login state", "Encryption indicators", "Live collection authority", "RAM capture tool/version", "Mounted volumes", "Reason for live collection or shutdown decision"],
        "related_playbooks": ["Live Computer Acquisition / RAM Capture", "Memory / RAM Analysis Refresher", "Dead-Box Computer Imaging"],
    },
    {
        "id": "file_system_metadata",
        "category": "File System",
        "title": "File system metadata, deletion, and recycle context",
        "helps_answer": "May help evaluate file existence, paths, timestamps, deletion/recycle status, naming patterns, and source/destination context.",
        "where_to_look": ["MFT and file system metadata", "$Recycle.Bin", "Directory listings", "File timestamps", "USN Journal where available", "Volume shadow copies where available", "Application metadata"],
        "tools": ["MFTECmd", "RBCmd", "Timeline Explorer", "Autopsy", "Commercial forensic suites", "File system viewers"],
        "cautions": ["Deletion does not automatically prove concealment or intent.", "Timestamps can be affected by copying, extraction, timezone, filesystem, and application behavior.", "Recovered filenames and paths may be incomplete or tool-dependent."],
        "document": ["File path/name", "Timestamp fields and meaning", "Deletion/recycle status", "Source artifact", "Tool/version", "Recovery limitations"],
        "related_playbooks": ["Windows Artifact Review Refresher", "Dead-Box Computer Imaging"],
    },
    {
        "id": "mobile_messages_media",
        "category": "Mobile",
        "title": "Messages, calls, media, app, and account context",
        "helps_answer": "May help review communications, attachments, calls, contacts, media, app data, account context, and device-use indicators from a mobile extraction.",
        "where_to_look": ["Messages and attachments", "Calls and contacts", "Photos/videos and metadata", "App databases", "Account/device identifiers", "Extraction logs and unsupported app notes", "Manual verification where appropriate"],
        "tools": ["Cellebrite Physical Analyzer", "Magnet AXIOM", "GrayKey output review", "MSAB XRY", "Oxygen Forensic Detective", "SQLite viewers", "Manual validation/corroboration"],
        "cautions": ["A message or app artifact does not prove who physically held the phone at that moment.", "Contact names and account labels can be user-entered, synced, stale, or misleading.", "Unsupported or partially parsed apps should be documented as limitations."],
        "document": ["Extraction type", "Tool/version", "Device lock/account context", "Artifact source", "Timestamp/time zone", "Deleted/recovered status", "Limitations and corroboration"],
        "related_playbooks": ["Mobile Device Extraction Refresher"],
    },
    {
        "id": "mobile_location_media",
        "category": "Mobile",
        "title": "Mobile location, media metadata, and movement context",
        "helps_answer": "May help review possible location, movement, camera/media, app-location, or device-state context from mobile data within scope.",
        "where_to_look": ["Photo/video EXIF and file metadata", "Location databases where parsed", "Maps and ride/share app artifacts", "Wi-Fi/cell/network context", "Health/fitness app data where authorized", "Cloud media sync indicators"],
        "tools": ["Cellebrite Physical Analyzer", "Magnet AXIOM", "Oxygen Forensic Detective", "SQLite viewers", "EXIF/media metadata tools", "Manual map/source review"],
        "cautions": ["Location artifacts vary in precision, source, and reliability.", "A device location is not automatically the same as a person's location.", "Cloud sync, shared accounts, and generated metadata can complicate source interpretation."],
        "document": ["Artifact source/database", "Coordinate/source/precision if available", "Timestamp/time zone", "Device/account context", "Sync/source limitations", "Corroboration"],
        "related_playbooks": ["Mobile Device Extraction Refresher"],
    },
    {
        "id": "mobile_extraction_limits",
        "category": "Mobile",
        "title": "Mobile extraction type and limitation indicators",
        "helps_answer": "May help explain what a mobile extraction did or did not collect and why certain apps, deleted items, or artifact categories may be absent.",
        "where_to_look": ["Extraction report metadata", "Tool logs", "Extraction type summary", "Unsupported app notes", "Device OS/version", "Lock state and acquisition method", "Cloud/account scope notes"],
        "tools": ["Cellebrite UFED/Physical Analyzer", "Magnet AXIOM", "GrayKey output review", "MSAB XRY", "Oxygen Forensic Detective", "Tool-generated logs and reports"],
        "cautions": ["A logical extraction is not the same as a file-system or physical extraction.", "Tool support changes by device, OS version, security state, and tool version.", "Absence of parsed data does not always mean absence on the device."],
        "document": ["Tool/version", "Extraction type", "Device model/OS", "Lock state", "Success/failure/partial status", "Unsupported apps or limitations"],
        "related_playbooks": ["Mobile Device Extraction Refresher"],
    },
]

INVESTIGATIVE_QUESTIONS = [
    {
        "id": "deadbox_user_control",
        "question": "What may help show who used or controlled this Windows laptop?",
        "situations": ["Dead-box laptop exam", "Shared device or shared account"],
        "look_at": ["User profiles and account names", "Logon/session artifacts", "Recent file and application activity", "Browser profiles and accounts", "Possession/location/admission context", "Remote-access or automation alternatives"],
        "mindset": "Treat user control as a supported interpretation, not a single-artifact conclusion. Look for patterns across profiles, sessions, recent activity, possession, passwords, admissions, and alternative access paths.",
        "guardrails": ["A Windows account name is not automatically the human actor.", "A profile folder can support context but does not prove who was physically present.", "Shared accounts, remote access, and automation should be considered when attribution matters."],
        "related_artifact_ids": ["windows_logon_sessions", "windows_file_access", "browser_activity", "windows_execution", "remote_access_automation"],
        "related_artifacts": ["Windows - Logon, account, and session indicators", "Windows - File access and user activity indicators", "Browser - Browser activity indicators"],
    },
    {
        "id": "deadbox_file_interaction",
        "question": "Was a file opened, viewed, deleted, moved, or otherwise interacted with?",
        "situations": ["Dead-box laptop exam", "File movement question", "Shared device or shared account"],
        "look_at": ["LNK and Jump Lists", "RecentDocs/MRU and application recent lists", "Shellbags and folder interaction", "Recycle Bin and filesystem metadata", "Source file presence or absence", "Cloud sync or removable-media paths"],
        "mindset": "Start by separating file existence from file interaction. Then look for multiple activity traces that may support opening, viewing, moving, deletion, or access from a specific user profile.",
        "guardrails": ["Recent-file artifacts can be created by previews, sync, indexing, or application behavior.", "Deletion is not automatically concealment or intent.", "File movement usually requires correlation across more than one artifact family."],
        "related_artifact_ids": ["windows_file_access", "file_system_metadata", "external_media_file_movement", "cloud_sync"],
        "related_artifacts": ["Windows - File access and user activity indicators", "File System - File system metadata, deletion, and recycle context"],
    },
    {
        "id": "deadbox_program_execution",
        "question": "Was a program, command shell, script, or tool likely executed?",
        "situations": ["Dead-box laptop exam", "Possible remote access or automation", "Shared device or shared account"],
        "look_at": ["Prefetch where available", "Amcache/ShimCache-style artifacts", "UserAssist", "Event logs", "PowerShell/script logs", "LNK/Jump List context", "Remote access or scheduled task artifacts"],
        "mindset": "Look for execution-supporting artifacts, then evaluate whether they show execution, inventory, user interaction, or only presence. Actor attribution needs separate context.",
        "guardrails": ["Program presence is not execution.", "Execution indicators do not prove who ran the program.", "Command/script activity can come from automation, admin activity, malware, or remote access."],
        "related_artifact_ids": ["windows_execution", "windows_event_logs", "remote_access_automation", "windows_logon_sessions"],
        "related_artifacts": ["Windows - Program execution indicators", "Remote Access / Automation - Remote access, automation, and scheduled activity indicators"],
    },
    {
        "id": "live_volatile_priority",
        "question": "What should be considered before changing or powering down the live system?",
        "situations": ["Powered-on computer / live system", "BitLocker-enabled laptop"],
        "look_at": ["Authority and scope for live collection", "Visible power/lock/login state", "Running processes", "Network connections", "Mounted volumes", "Encryption indicators", "RAM capture opportunity", "Risk of remote change or data loss"],
        "mindset": "This is an order-of-volatility and risk decision. Document first, then decide whether live collection is justified and authorized before shutdown or isolation changes destroy state.",
        "guardrails": ["Live collection changes the system and must be documented.", "Order of volatility does not override scope, safety, or agency policy.", "Powering down may lose RAM, mounted encrypted volumes, sessions, and network context."],
        "related_artifact_ids": ["memory_processes", "encryption_live_state", "windows_logon_sessions", "remote_access_automation"],
        "related_artifacts": ["Memory / RAM - Processes, command lines, and network context", "Encryption / Live State - BitLocker, mounted volumes, and encryption-related volatile context"],
    },
    {
        "id": "bitlocker_ram_key_context",
        "question": "Could BitLocker or mounted encryption make RAM/live collection important?",
        "situations": ["BitLocker-enabled laptop", "Powered-on computer / live system", "Memory/RAM review"],
        "look_at": ["Whether volumes are mounted/unlocked", "Logged-in or locked state", "BitLocker status indicators where authorized", "RAM capture feasibility", "Tool/policy support", "Destination storage and hash documentation"],
        "mindset": "A powered-on encrypted system may expose access and context that disappears at shutdown. RAM may contain useful encryption-related material, but that possibility must not be overstated before examination.",
        "guardrails": ["Do not claim a recovery key is in RAM unless observed and corroborated.", "Do not run commands outside authority just because the system is live.", "Document why live collection was or was not attempted."],
        "related_artifact_ids": ["encryption_live_state", "memory_processes", "windows_logon_sessions"],
        "related_artifacts": ["Encryption / Live State - BitLocker, mounted volumes, and encryption-related volatile context", "Memory / RAM - Processes, command lines, and network context"],
    },
    {
        "id": "memory_process_network_question",
        "question": "What was active in RAM, and what context can it support?",
        "situations": ["Memory/RAM review", "Powered-on computer / live system"],
        "look_at": ["Process list/tree", "Command lines", "Network connections", "Handles and loaded modules", "Suspicious process relationships", "Corroborating disk/log artifacts", "Memory image acquisition context"],
        "mindset": "RAM can show live system context, but memory plugin output is a lead that needs careful source, plugin, timestamp, and corroboration notes.",
        "guardrails": ["A process name by itself is not a malware conclusion.", "An IP address is not attribution.", "Command lines in memory do not identify the human actor by themselves."],
        "related_artifact_ids": ["memory_processes", "windows_execution", "remote_access_automation", "encryption_live_state"],
        "related_artifacts": ["Memory / RAM - Processes, command lines, and network context"],
    },
    {
        "id": "mobile_messages_context",
        "question": "What mobile artifacts may support communication, media, or app activity?",
        "situations": ["Mobile device review"],
        "look_at": ["Messages and attachments", "Calls/contacts", "Photos and videos", "App databases", "Account/device identifiers", "Deleted/recovered status", "Extraction limitations"],
        "mindset": "Start from the extraction type and app support, then connect relevant mobile artifacts to the question without jumping from device activity to human actor identity.",
        "guardrails": ["A message artifact does not prove who physically held the phone.", "Contact names and app labels may be user-entered, synced, stale, or misleading.", "Deleted/recovered artifacts require careful source and status explanation."],
        "related_artifact_ids": ["mobile_messages_media", "mobile_extraction_limits"],
        "related_artifacts": ["Mobile - Messages, calls, media, app, and account context", "Mobile - Mobile extraction type and limitation indicators"],
    },
    {
        "id": "mobile_location_media_question",
        "question": "What mobile artifacts may support location, movement, or media-context review?",
        "situations": ["Mobile device review"],
        "look_at": ["Photo/video metadata", "Location databases", "Maps or transportation app artifacts", "Wi-Fi/cell/network context", "Cloud media sync", "Timestamp/time zone and precision"],
        "mindset": "Location and media artifacts can provide context, but source, precision, sync behavior, and device/account control must be documented before drawing stronger conclusions.",
        "guardrails": ["Device location is not automatically a person's location.", "Location precision and source vary widely.", "Cloud sync and shared accounts can complicate origin and possession."],
        "related_artifact_ids": ["mobile_location_media", "mobile_messages_media", "mobile_extraction_limits"],
        "related_artifacts": ["Mobile - Mobile location, media metadata, and movement context"],
    },
    {
        "id": "mobile_extraction_limits_question",
        "question": "What should be checked before explaining what a mobile extraction does or does not show?",
        "situations": ["Mobile device review"],
        "look_at": ["Extraction type", "Tool/version", "Device model and OS", "Lock state", "Unsupported apps", "Cloud/account scope", "Tool logs and partial extraction warnings"],
        "mindset": "Before interpreting absence or presence, understand how the data was acquired and what the tool says it could not collect or parse.",
        "guardrails": ["Absence of a parsed artifact is not always absence from the device.", "Tool support changes by OS, device state, and tool version.", "Cloud data may require separate authority and collection."],
        "related_artifact_ids": ["mobile_extraction_limits", "mobile_messages_media", "cloud_sync"],
        "related_artifacts": ["Mobile - Mobile extraction type and limitation indicators"],
    },
    {
        "id": "external_media_connected",
        "question": "Was a removable device connected to this computer, and what context supports that?",
        "situations": ["External media review", "Dead-box laptop exam", "File movement question"],
        "look_at": ["USBSTOR and mounted device artifacts", "SetupAPI logs", "Event logs", "Volume serial and drive letter context", "User association indicators", "Connection timeline"],
        "mindset": "First establish device connection context, then separately evaluate file movement, user association, and timing.",
        "guardrails": ["Connection does not prove file transfer.", "Connection does not identify the person who connected it.", "Device identifiers and drive letters can be ambiguous without correlation."],
        "related_artifact_ids": ["usb_devices", "external_media_file_movement", "windows_logon_sessions"],
        "related_artifacts": ["Windows - USB / external device connection indicators", "External Media - External media file movement indicators"],
    },
    {
        "id": "external_media_file_transfer",
        "question": "Is there support for files being copied to or from external media?",
        "situations": ["External media review", "File movement question", "Dead-box laptop exam"],
        "look_at": ["Removable-path LNK/Jump Lists", "Shellbags", "Recent files", "File system timestamps", "USB connection context", "Application logs", "Source/destination file presence"],
        "mindset": "Treat file transfer as a correlation question. Build a timeline using device connection, file activity, source/destination paths, and user/session context.",
        "guardrails": ["Opening a file from USB is not the same as copying it.", "Timestamp patterns can be suggestive but may have benign explanations.", "Avoid saying transfer occurred unless supporting artifacts align."],
        "related_artifact_ids": ["external_media_file_movement", "usb_devices", "windows_file_access", "file_system_metadata"],
        "related_artifacts": ["External Media - External media file movement indicators", "Windows - USB / external device connection indicators"],
    },
    {
        "id": "browser_download_activity",
        "question": "Was there browser, search, download, or web-app activity relevant to the question?",
        "situations": ["Browser/download review", "Dead-box laptop exam", "Shared device or shared account"],
        "look_at": ["Browser profile", "History", "Downloads", "Cookies/session artifacts", "Search terms/form history", "Cache/local storage", "Downloaded file path", "File-open artifacts after download"],
        "mindset": "Separate browsing, downloading, opening, account use, and user intent. They are related but not identical conclusions.",
        "guardrails": ["A browser record can come from redirects, embedded content, sync, or previews.", "A download record does not prove the file was opened or understood.", "Browser account/profile context matters for attribution."],
        "related_artifact_ids": ["browser_activity", "windows_file_access", "cloud_sync", "file_system_metadata"],
        "related_artifacts": ["Browser - Browser activity indicators", "Cloud / Sync - Cloud sync and local cloud-client indicators"],
    },
    {
        "id": "cloud_sync_source",
        "question": "Is this local activity, cloud-synced activity, or both?",
        "situations": ["Cloud sync review", "Browser/download review", "Mobile device review", "Dead-box laptop exam"],
        "look_at": ["Cloud client folders", "Sync logs/metadata", "Placeholder or hydration state", "Cloud account identifiers", "Browser web-app activity", "Provider exports where authorized", "Local file-open artifacts"],
        "mindset": "Identify the source of the data before interpreting it. A synced artifact may reflect another device, web account, or cloud service rather than only local user activity.",
        "guardrails": ["Cloud authority may be separate from device authority.", "A synced file does not automatically prove local creation or viewing.", "Multi-device accounts complicate attribution and timing."],
        "related_artifact_ids": ["cloud_sync", "browser_activity", "windows_file_access", "mobile_extraction_limits"],
        "related_artifacts": ["Cloud / Sync - Cloud sync and local cloud-client indicators"],
    },
    {
        "id": "remote_or_automation_context",
        "question": "Could remote access, automation, scripts, or scheduled activity explain what happened?",
        "situations": ["Possible remote access or automation", "Powered-on computer / live system", "Dead-box laptop exam", "Shared device or shared account"],
        "look_at": ["RDP/remote access logs", "Remote access apps", "PowerShell logs", "Scheduled Tasks", "Services and startup entries", "Process command lines", "Network connections", "Security/EDR logs"],
        "mindset": "When actor attribution matters, look for alternative mechanisms that can create activity without the account holder physically typing at the keyboard.",
        "guardrails": ["Remote access can make activity appear local without corroborating context.", "Scheduled tasks and scripts can run without active human input.", "Tool presence alone is not unauthorized use or malware."],
        "related_artifact_ids": ["remote_access_automation", "windows_event_logs", "memory_processes", "windows_execution"],
        "related_artifacts": ["Remote Access / Automation - Remote access, automation, and scheduled activity indicators"],
    },
]

CONTROL_CONTEXT_PROMPTS = [
    {
        "title": "Access and control context",
        "prompt": "What facts support that a person had access to or control over the device, account, or session?",
        "examples": ["Admitted knowing the password/PIN", "Exclusive possession or custody", "Account/profile tied to the person", "Biometric/passcode setup context", "Recent use consistent with their schedule/location", "Witness/camera/physical evidence support"],
        "caution": "Access and control indicators support context. They do not automatically prove that the person performed every action found on the device.",
    },
    {
        "title": "Actor vs. artifact separation",
        "prompt": "What does the artifact show, and what extra evidence would be needed to connect it to a specific person?",
        "examples": ["Artifact: command line existed", "Extra context: logged-in user, session timing, possession, admissions, remote-access review", "Artifact: browser history record", "Extra context: account/session, activity pattern, file access, corroborating source"],
        "caution": "Avoid wording that turns tool output into a human-action conclusion unless the supporting context is documented.",
    },
    {
        "title": "Alternative explanations",
        "prompt": "What reasonable alternatives need to be ruled out or documented?",
        "examples": ["Shared device", "Shared password", "Remote access", "Malware or automation", "Cloud sync", "Scheduled task/script", "Application preview/indexing behavior"],
        "caution": "The point is not to invent doubt. The point is to document what the evidence supports, what it does not support, and what was considered.",
    },
]


def search_artifact_areas(query):
    needle = (query or "").strip().lower()
    if not needle:
        return []
    results = []
    for item in ARTIFACT_AREAS:
        haystack_parts = [item.get("title", ""), item.get("category", ""), item.get("helps_answer", "")]
        for key in ("where_to_look", "tools", "cautions", "document", "related_playbooks"):
            haystack_parts.extend(item.get(key, []))
        if needle in "\n".join(str(part) for part in haystack_parts).lower():
            results.append(item)
    return results


def search_investigative_questions(query):
    needle = (query or "").strip().lower()
    if not needle:
        return []
    results = []
    for item in INVESTIGATIVE_QUESTIONS:
        haystack_parts = [item.get("question", ""), item.get("mindset", "")]
        for key in ("look_at", "guardrails", "related_artifacts"):
            haystack_parts.extend(item.get(key, []))
        if needle in "\n".join(str(part) for part in haystack_parts).lower():
            results.append(item)
    return results


SCENARIO_CARDS = [
    {
        "id": "command_seen_on_device",
        "title": "Command or tool activity appears on a device",
        "category": "Use / Access Context",
        "situation": "A command, script, executable, or tool artifact appears in process, shell, event, memory, or application history and someone wants to know who ran it.",
        "what_to_think": [
            "First separate the technical activity from the human actor.",
            "Ask what the artifact actually shows: execution, possible execution, history, presence, or a parser interpretation.",
            "Then look for user/session/control context that may support who had access at the relevant time.",
        ],
        "supporting_context": [
            "Logged-in user and active session context",
            "Local account, domain account, or cloud account association",
            "Possession or custody of the device at the relevant time",
            "Admission about device use, account use, or exclusive password/PIN knowledge",
            "Remote access indicators, scheduled tasks, scripts, malware, or automation review",
            "Corroborating timestamps from logs, files, memory, browser, messaging, or external records",
        ],
        "guardrails": [
            "A command appearing on a device does not prove which person typed or initiated it.",
            "A named account does not automatically prove the account holder was physically present.",
            "Shared credentials, remote access, automation, malware, and scheduled tasks can affect interpretation.",
            "An admission of exclusive password knowledge can support device control context, but should be documented precisely and weighed with the rest of the evidence.",
        ],
        "plain_language": "The artifact can support that activity occurred on the system. Connecting that activity to a person usually requires additional access, account, possession, timing, or admission context.",
        "related_playbook_id": "windows_artifact_review_refresher",
        "related_playbook_title": "Windows Artifact Review Refresher",
        "related_reference_terms": ["Actor vs. artifact", "Device-use context", "Overclaim", "Corroboration"],
    },
    {
        "id": "downloaded_file_question",
        "title": "Downloaded file needs interpretation",
        "category": "Browser / File Activity",
        "situation": "A download record, file path, browser artifact, or recovered file suggests something was downloaded and the examiner needs to explain what can and cannot be said.",
        "what_to_think": [
            "Separate download evidence from file-open evidence.",
            "Review browser download records, file system metadata, recent-file artifacts, shortcut artifacts, and application history when available.",
            "Consider whether sync, preview, cache, automated download, or another user/session could explain the artifact.",
        ],
        "supporting_context": [
            "Browser download database and source URL",
            "File path, MAC times, Zone.Identifier, and file metadata",
            "LNK, Jump List, MRU, recent files, or application-specific open history",
            "User profile and browser account context",
            "Corroborating messages, searches, or external records",
        ],
        "guardrails": [
            "A download record does not prove the file was opened or understood.",
            "A file existing on a device does not prove knowledge by a specific person.",
            "Browser sync, redirects, cached content, and automated activity can complicate interpretation.",
        ],
        "plain_language": "A download artifact may support that a browser or process obtained a file. Stronger claims about viewing, knowledge, intent, or actor identity require additional context.",
        "related_playbook_id": "windows_artifact_review_refresher",
        "related_playbook_title": "Windows Artifact Review Refresher",
        "related_reference_terms": ["Browser activity", "File access", "Corroboration", "Does not prove"],
    },
    {
        "id": "usb_connected_question",
        "title": "USB or external media connection question",
        "category": "External Media",
        "situation": "Artifacts suggest a USB drive or external device connected to a computer and the examiner needs to understand what that supports.",
        "what_to_think": [
            "Identify the device and connection history first.",
            "Then ask whether any file access, copy, shortcut, shell, or application artifacts connect that device to relevant activity.",
            "Finally evaluate user/session/control context around the connection time.",
        ],
        "supporting_context": [
            "USBSTOR, MountedDevices, device class, volume serial, and SetupAPI context",
            "Event logs or device install timestamps",
            "LNK/Jump List references to removable paths",
            "File copy, recent file, or application activity related to removable media",
            "User logon/session evidence around connection times",
        ],
        "guardrails": [
            "USB connection does not prove file transfer.",
            "USB connection does not prove who connected the device.",
            "Timestamp interpretation can be complicated by install time, first connection, last connection, time zones, and parser behavior.",
        ],
        "plain_language": "USB artifacts can help show that a device was connected or recognized. Showing transfer, access, or actor identity usually requires additional artifacts and context.",
        "related_playbook_id": "external_media_hash_copy_refresher",
        "related_playbook_title": "External Media Hash / Copy Refresher",
        "related_reference_terms": ["USB", "External media", "File access", "Device-use context"],
    },
    {
        "id": "mobile_message_actor",
        "title": "Mobile message or app activity needs actor context",
        "category": "Mobile",
        "situation": "A mobile extraction shows messages, app activity, media, or account artifacts and someone wants to know who physically used the device or account.",
        "what_to_think": [
            "Start with what the extraction and parsed artifact show.",
            "Review account/device ownership, lock state, passcode context, message thread context, app account context, and possession/control indicators.",
            "Be careful when moving from device/account activity to a specific human actor.",
        ],
        "supporting_context": [
            "Device identifiers, phone number, account names, SIM/eSIM, and cloud account association",
            "Lock state, passcode/PIN/biometric context, and admissions about password knowledge",
            "Possession/custody, witness, camera, location, or communication context",
            "Message content, timing, writing style, attachments, contact names, and surrounding conversation",
            "Tool limitations, unsupported apps, deleted/recovered status, and time zone handling",
        ],
        "guardrails": [
            "A message or app artifact does not automatically prove who held the phone at that moment.",
            "An account name or contact label may be user-entered, synced, stale, or misleading.",
            "Deleted or recovered artifacts need careful explanation of source, status, and tool interpretation.",
        ],
        "plain_language": "Mobile artifacts can show activity tied to a device, account, app, or extraction source. Human attribution should be supported by possession, access, account, admission, timing, and corroborating context.",
        "related_playbook_id": "mobile_device_extraction",
        "related_playbook_title": "Mobile Device Extraction Refresher",
        "related_reference_terms": ["Mobile", "Device-use context", "Actor vs. artifact", "Limitations"],
    },
]


def search_scenario_cards(query):
    needle = (query or "").strip().lower()
    if not needle:
        return []
    results = []
    for item in SCENARIO_CARDS:
        haystack_parts = [item.get("title", ""), item.get("category", ""), item.get("situation", ""), item.get("plain_language", ""), item.get("related_playbook_title", "")]
        for key in ("what_to_think", "supporting_context", "guardrails", "related_reference_terms"):
            haystack_parts.extend(item.get(key, []))
        if needle in "\n".join(str(part) for part in haystack_parts).lower():
            results.append(item)
    return results


# Coaching paths are maintained in coach_questions/coaching_paths.py so the
# mentoring/coaching content can grow without hard-coding scenario paths in this
# main data module. The alias preserves older UI/search references.
from coach_questions import COACHING_PATHS, search_coaching_paths

SCENARIO_COACHING_QUESTIONS = COACHING_PATHS


def search_scenario_coaching_questions(query):
    return search_coaching_paths(query)


DECISION_PATHS = [
    {
        "id": "live_computer",
        "label": "Powered-on computer / live system",
        "playbook_id": "live_computer_acquisition_ram",
        "recommended_mode": "Field Reference",
        "why": "A powered-on system may contain volatile data that can be lost during shutdown, including RAM, active processes, network connections, mounted volumes, and encryption context.",
        "questions": [
            "Is live collection authorized and within scope?",
            "Could shutdown lose data that matters?",
            "Do agency SOPs allow RAM capture or live response?",
        ],
        "first_steps": ["Confirm authority and scope", "Document initial state", "Think through network/isolation decisions", "Prioritize volatile data"],
    },
    {
        "id": "dead_box_computer",
        "label": "Powered-off computer / removed drive",
        "playbook_id": "dead_box_computer_imaging",
        "recommended_mode": "Field Reference",
        "why": "A powered-off system is usually approached as a preservation/imaging workflow, with attention to physical documentation, write protection, imaging, and verification.",
        "questions": [
            "What storage media is actually in scope?",
            "Is write protection available and validated?",
            "Do you have destination capacity and an approved imaging format?",
        ],
        "first_steps": ["Confirm target media and scope", "Photograph and document condition", "Use write protection where applicable", "Create and verify the image"],
    },
    {
        "id": "mobile_device",
        "label": "Mobile phone / tablet extraction",
        "playbook_id": "mobile_device_extraction",
        "recommended_mode": "Field Reference",
        "why": "Mobile workflows depend heavily on scope, device state, lock status, network condition, tool support, extraction type, and documented limitations.",
        "questions": [
            "Is the device and data category clearly within scope?",
            "What is the power, lock, and network state?",
            "Which extraction types are available for this device and tool version?",
        ],
        "first_steps": ["Confirm authority, scope, and device identity", "Document condition and connectivity", "Choose extraction approach", "Preserve outputs and logs"],
    },
    {
        "id": "memory_analysis",
        "label": "Memory image / RAM analysis",
        "playbook_id": "memory_ram_analysis",
        "recommended_mode": "Learning / Refresher",
        "why": "Memory analysis often benefits from a structured review order so the examiner understands OS context, processes, process trees, command lines, connections, and suspicious indicators without overclaiming.",
        "questions": [
            "What system produced the memory image?",
            "Has the image been preserved and hashed?",
            "What question are you trying to answer before running plugins?",
        ],
        "first_steps": ["Confirm image source and integrity", "Identify OS details", "Review processes and process tree", "Review network and command-line context"],
    },
    {
        "id": "windows_artifacts",
        "label": "Windows artifact review",
        "playbook_id": "windows_artifact_review",
        "recommended_mode": "Learning / Refresher",
        "why": "Windows artifact review is strongest when the examiner starts with the question being asked, then reviews user activity, execution, file access, browser, USB, and log sources while documenting limits.",
        "questions": [
            "What user or activity question are you trying to answer?",
            "Which artifact families are most relevant?",
            "What corroboration is available?",
        ],
        "first_steps": ["Define the question", "Identify user profiles and time zone context", "Review common activity artifacts", "Document limitations and corroboration"],
    },
    {
        "id": "external_media",
        "label": "External media hash / copy",
        "playbook_id": "external_media_hash_copy",
        "recommended_mode": "Field Reference",
        "why": "External media work can look simple, but still needs scope, device identification, copy/imaging method, hash documentation, and clean output preservation.",
        "questions": [
            "Is the entire media or only selected files in scope?",
            "Will you image it, copy selected data, or generate a hash-only record?",
            "How will integrity and output location be documented?",
        ],
        "first_steps": ["Confirm scope and media identity", "Choose copy/imaging/hash approach", "Record hashes and logs", "Preserve outputs and limitations"],
    },
]


def get_decision_path(path_id):
    for path in DECISION_PATHS:
        if path["id"] == path_id:
            return path
    return None



from coach_questions import COACH_QUESTIONS, load_coach_questions, search_coach_questions
from glossary import GLOSSARY_TERMS as GLOSSARY, search_glossary

def search_playbooks(query):
    needle = (query or "").strip().lower()
    if not needle:
        return []
    results = []
    for playbook in PLAYBOOKS:
        haystack_parts = [playbook.get("title", ""), playbook.get("category", ""), playbook.get("summary", "")]
        for step in playbook.get("steps", []):
            haystack_parts.extend([step.get("title", ""), step.get("field_focus", ""), step.get("learning_detail", ""), step.get("why", "")])
            for key in ("tools", "artifacts", "cautions", "document", "does_not_prove"):
                haystack_parts.extend(step.get(key, []))
            for command in step.get("command_examples", []):
                haystack_parts.extend([command.get("label", ""), command.get("example", ""), command.get("purpose", ""), command.get("does_not_prove", "")])
        haystack = "\n".join(str(part) for part in haystack_parts).lower()
        if needle in haystack:
            results.append(playbook)
    return results


def get_playbook(playbook_id):
    for playbook in PLAYBOOKS:
        if playbook["id"] == playbook_id:
            return playbook
    return None


def categories():
    return sorted({pb["category"] for pb in PLAYBOOKS})