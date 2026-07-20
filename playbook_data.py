"""Built-in ByteCase Playbooks content.

The content is intentionally guidance-focused. It does not perform evidence
collection, extraction, parsing, or analysis.
"""

APP_NAME = "ByteCase Playbooks"
APP_SUBTITLE = "Guided Examiner Reference and Learning Companion"
APP_VERSION = "0.5.0"
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


GLOSSARY = [
    {
        "term": "Field Reference Mode",
        "category": "Playbooks",
        "definition": "A shorter view meant for real-time reference during a task. It emphasizes order, documentation, cautions, and quick reminders.",
        "related": ["Learning / Refresher Mode", "Step card", "Boundary notice"],
    },
    {
        "term": "Learning / Refresher Mode",
        "category": "Playbooks",
        "definition": "A deeper view meant for downtime learning or refreshers before performing less-common work. It expands the why, tools, artifacts, cautions, and documentation reminders.",
        "related": ["Field Reference Mode", "Step card", "Examiner judgment"],
    },
    {
        "term": "Live acquisition",
        "category": "Acquisition",
        "definition": "Collection from a powered-on system. It may preserve volatile state but also changes the system and requires careful documentation and scope control.",
        "related": ["RAM capture", "Volatile data", "Network isolation", "Encryption context"],
    },
    {
        "term": "Dead-box imaging",
        "category": "Imaging",
        "definition": "Preservation of storage media when the device is powered off or the storage media is removed and handled through a controlled imaging process.",
        "related": ["Write blocker", "Forensic image", "Hash verification"],
    },
    {
        "term": "RAM capture",
        "category": "Memory",
        "definition": "Collection of system memory from a live machine. RAM can contain volatile process, connection, command-line, session, and encryption-related context.",
        "related": ["Volatility", "Volatile data", "Live acquisition"],
    },
    {
        "term": "Volatility",
        "category": "Memory",
        "definition": "A memory forensics framework commonly used to examine memory images. Plugin output should be reviewed in context and documented as tool output, not as an automatic conclusion.",
        "related": ["windows.info", "windows.pslist", "windows.pstree", "windows.netscan", "windows.malfind"],
    },
    {
        "term": "Write blocker",
        "category": "Preservation",
        "definition": "A hardware, software, or process control used to reduce or prevent writes to source media during acquisition. Local validation and documentation matter.",
        "related": ["ByteCase Validate", "Dead-box imaging", "External media"],
    },
    {
        "term": "Hash verification",
        "category": "Integrity",
        "definition": "A process for checking whether data matches a previously recorded hash value. Hashes support integrity checks; they do not interpret content or user intent.",
        "related": ["ByteCase Verify", "SHA-256", "MD5", "Manifest"],
    },
    {
        "term": "Artifact",
        "category": "Analysis",
        "definition": "A data item or record that may help answer a forensic question. Artifact presence, absence, or parser output must be interpreted in context.",
        "related": ["ByteCase Notes", "Artifact index", "Corroboration"],
    },
    {
        "term": "Overclaim",
        "category": "Reporting",
        "definition": "A statement that goes beyond what the artifact, tool output, or available context supports. Playbooks should help examiners document observations without overstating conclusions.",
        "related": ["Limitations", "Corroboration", "Examiner judgment"],
    },

    {
        "term": "Corroboration",
        "category": "Analysis",
        "definition": "The practice of checking whether an observation is supported by another artifact, source, timestamp, log, tool output, or case context before relying on it heavily.",
        "related": ["Overclaim", "Limitations", "Artifact"],
    },
    {
        "term": "Limitations",
        "category": "Reporting",
        "definition": "Known boundaries of the tool, data source, extraction type, parser support, authority, or examiner process. Limitations should be documented instead of hidden.",
        "related": ["Overclaim", "Tool validation", "Unsupported app"],
    },
    {
        "term": "Volatile data",
        "category": "Memory",
        "definition": "Data that can change or disappear quickly, especially on a powered-on system. Examples may include RAM, running processes, active network connections, logged-in users, and mounted volumes.",
        "related": ["Live acquisition", "RAM capture", "Memory analysis"],
    },
    {
        "term": "Forensic image",
        "category": "Acquisition",
        "definition": "A documented acquisition of storage media or selected data created for later examination. The image format, tool, verification result, and limitations should be recorded.",
        "related": ["Dead-box imaging", "Hash verification", "Write blocker"],
    },
    {
        "term": "Command example",
        "category": "Playbooks",
        "definition": "A sample command or tool action shown as a learning/reference prompt. Commands must be adapted to the examiner's tool path, image name, case scope, agency policy, and operating environment.",
        "related": ["Volatility", "Documentation", "Limitations"],
    },
    {
        "term": "Does not prove",
        "category": "Reporting",
        "definition": "A guardrail reminder that a tool result or artifact can support a lead without proving attribution, intent, or a final conclusion by itself.",
        "related": ["Overclaim", "Corroboration", "Limitations"],
    },
]

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


def search_glossary(query):
    needle = (query or "").strip().lower()
    if not needle:
        return []
    results = []
    for item in GLOSSARY:
        haystack = "\n".join([item.get("term", ""), item.get("category", ""), item.get("definition", ""), "\n".join(item.get("related", []))]).lower()
        if needle in haystack:
            results.append(item)
    return results


def get_playbook(playbook_id):
    for playbook in PLAYBOOKS:
        if playbook["id"] == playbook_id:
            return playbook
    return None


def categories():
    return sorted({pb["category"] for pb in PLAYBOOKS})
