"""Built-in ByteCase Playbooks content.

The content is intentionally guidance-focused. It does not perform evidence
collection, extraction, parsing, or analysis.
"""

APP_NAME = "ByteCase Playbooks"
APP_SUBTITLE = "Guided Examiner Reference and Learning Companion"
APP_VERSION = "0.8.1"
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
        "helps_answer": "May help evaluate whether an application or executable appears to have run or been prepared to run on a Windows system.",
        "where_to_look": ["Prefetch, when enabled and available", "Amcache/ShimCache-style program inventory artifacts", "UserAssist and related user activity artifacts", "Event logs", "LNK and Jump List context", "EDR or endpoint logs, if available"],
        "tools": ["Autopsy", "KAPE", "Eric Zimmerman tools", "Registry Explorer", "Timeline Explorer", "Commercial forensic suites"],
        "cautions": ["Execution indicators do not prove who personally ran the program.", "Some artifacts show presence, inventory, or interaction rather than confirmed execution.", "Time zone, system clock, parser support, and artifact meaning must be checked."],
        "document": ["Artifact source and path", "Tool/parser/version", "Timestamp meaning", "Associated user profile if supported", "Corroborating sources", "Limitations"],
        "related_playbooks": ["Windows Artifact Review Refresher"],
    },
    {
        "id": "windows_file_access",
        "category": "Windows",
        "title": "File access and user activity indicators",
        "helps_answer": "May help evaluate whether files, folders, removable media, or recent items appear to have been opened, viewed, or interacted with.",
        "where_to_look": ["LNK files", "Jump Lists", "RecentDocs / MRU-style artifacts", "Shellbags", "Recycle Bin", "Office recent files", "Cloud sync logs where available"],
        "tools": ["LECmd", "JLECmd", "ShellBags Explorer", "Registry Explorer", "Autopsy", "Commercial forensic suites"],
        "cautions": ["A recent-file artifact does not prove the suspect personally opened the file.", "Preview panes, automated indexing, sync clients, or application behavior can create activity traces.", "File access artifacts should be tied to user/session/device-control context when attribution matters."],
        "document": ["Artifact family", "User profile path", "Timestamp type", "File path referenced", "Whether source file was present", "Corroborating activity"],
        "related_playbooks": ["Windows Artifact Review Refresher"],
    },
    {
        "id": "usb_devices",
        "category": "Windows",
        "title": "USB / external device connection indicators",
        "helps_answer": "May help evaluate whether a removable device appears to have been connected and how it may relate to user activity or copied files.",
        "where_to_look": ["USBSTOR and device registry artifacts", "MountedDevices", "SetupAPI logs", "Event logs", "LNK and Jump Lists pointing to removable paths", "Volume serial numbers"],
        "tools": ["Registry Explorer", "USB-focused parsers", "Timeline tools", "Autopsy", "Commercial forensic suites"],
        "cautions": ["A USB connection does not prove file transfer.", "A connected device does not prove which person connected it.", "Device identifiers can be reused, missing, or interpreted incorrectly without corroboration."],
        "document": ["Device make/model/serial if available", "Volume serial", "First/last connection indicators", "User association indicators", "File access artifacts linked to removable paths", "Limitations"],
        "related_playbooks": ["External Media Hash / Copy Refresher", "Windows Artifact Review Refresher"],
    },
    {
        "id": "browser_activity",
        "category": "Browser",
        "title": "Browser activity indicators",
        "helps_answer": "May help evaluate web activity, searches, downloads, sessions, account use, or web application context.",
        "where_to_look": ["Browser history", "Downloads", "Cookies/session data", "Cache", "Form history/search terms", "Extensions", "Cloud browser sync context"],
        "tools": ["Browser-focused forensic parsers", "SQLite viewers", "Autopsy", "Commercial forensic suites"],
        "cautions": ["A browser record does not always prove intentional visit by a specific person.", "Popups, redirects, sync, previews, and embedded content can create records.", "Downloads do not prove a file was opened or understood."],
        "document": ["Browser/profile", "Artifact table/source", "Timestamp meaning", "URL/download path", "Account/session indicators", "Corroboration"],
        "related_playbooks": ["Windows Artifact Review Refresher"],
    },
    {
        "id": "memory_processes",
        "category": "Memory / RAM",
        "title": "Processes, command lines, and network context",
        "helps_answer": "May help review what was active in memory, including process relationships, command-line arguments, and network connections.",
        "where_to_look": ["Process list", "Process tree", "Command line output", "Network connection plugins", "Loaded DLL/modules", "Handles/files/registry references"],
        "tools": ["Volatility 3", "Volatility Workbench", "Commercial memory analysis support", "Timeline/correlation tools"],
        "cautions": ["A suspicious process name does not prove malware.", "An IP address is not attribution.", "Command-line evidence on a device does not prove which person typed or initiated it without supporting context."],
        "document": ["Memory image hash", "Tool/version", "Plugin/command", "PID/process relationship", "Timestamps if available", "Corroborating disk/log artifacts"],
        "related_playbooks": ["Memory / RAM Analysis Refresher", "Live Computer Acquisition / RAM Capture"],
    },
    {
        "id": "mobile_messages_media",
        "category": "Mobile",
        "title": "Messages, media, app, and account context",
        "helps_answer": "May help review communications, media, app data, account context, and device-use indicators from a mobile extraction.",
        "where_to_look": ["Messages and attachments", "Calls/contacts", "Photos/videos and metadata", "App databases", "Location artifacts", "Accounts and device identifiers", "Extraction logs and unsupported app notes"],
        "tools": ["Cellebrite Physical Analyzer", "Magnet AXIOM", "GrayKey output review", "SQLite viewers", "Manual validation/corroboration"],
        "cautions": ["A message or app artifact does not prove who physically held the phone at that moment.", "Cloud sync and multi-device accounts can complicate attribution.", "Unsupported or partially parsed apps should be documented as limitations."],
        "document": ["Extraction type", "Tool/version", "Device lock/account context", "Artifact source", "Timestamp/time zone", "Limitations and corroboration"],
        "related_playbooks": ["Mobile Device Extraction Refresher"],
    },
]

INVESTIGATIVE_QUESTIONS = [
    {
        "id": "who_used_device",
        "question": "Who may have used or controlled the device?",
        "look_at": ["Known passwords/PINs/passphrases", "Account logins and profile names", "Biometric/passcode setup context", "Logged-in sessions", "Device possession/location context", "Statements/admissions", "Exclusive-use indicators", "Corroborating camera/witness/physical evidence when available"],
        "mindset": "Treat device control as a conclusion that needs support from several sources. A password admission, exclusive possession, account ownership, and user-specific artifacts can strengthen context, but no single item should be overclaimed by itself.",
        "guardrails": ["A device artifact does not automatically identify the human actor.", "Knowing a password can support control/access, but it should be documented carefully and corroborated when important.", "Shared devices, shared passwords, remote access, cloud sync, and malware/automation can complicate attribution."],
        "related_artifacts": ["Windows - Program execution indicators", "Windows - File access and user activity indicators", "Mobile - Messages, media, app, and account context", "Memory / RAM - Processes, command lines, and network context"],
    },
    {
        "id": "file_accessed",
        "question": "Was a file opened, viewed, or interacted with?",
        "look_at": ["LNK files", "Jump Lists", "Recent files/MRU artifacts", "Application recent lists", "File metadata", "Shellbags", "Cloud sync context"],
        "mindset": "Start with the artifact meaning. Some artifacts suggest interaction, some suggest presence, and some are created by applications or previews. Then ask what ties that activity to a user session or account.",
        "guardrails": ["A file reference does not always prove intentional viewing.", "A file existing on a device does not prove the suspect knew about it.", "Tie file activity to user/session/device-control context before making stronger statements."],
        "related_artifacts": ["Windows - File access and user activity indicators", "Browser - Browser activity indicators"],
    },
    {
        "id": "command_executed",
        "question": "Was a command or tool executed?",
        "look_at": ["Command-line artifacts", "Console history where available", "Process execution artifacts", "Scripts/batch files", "Event logs", "EDR/tool logs", "Memory process and cmdline output"],
        "mindset": "Separate execution evidence from actor attribution. First determine what the artifact supports about process or command activity. Then look for account, session, possession, password, remote-access, and corroborating context.",
        "guardrails": ["A command appearing on a device does not prove which person executed it.", "A named account does not automatically prove the account holder was the person at the keyboard.", "Remote access, automation, malware, scripts, shared credentials, and scheduled tasks must be considered when relevant."],
        "related_artifacts": ["Memory / RAM - Processes, command lines, and network context", "Windows - Program execution indicators"],
    },
    {
        "id": "usb_connected",
        "question": "Was a USB or external device connected?",
        "look_at": ["USBSTOR/device registry artifacts", "SetupAPI logs", "MountedDevices", "Event logs", "LNK/Jump Lists referencing removable paths", "Volume serial numbers"],
        "mindset": "Identify the device, connection context, and any user/file activity that supports why the device matters. Then avoid jumping from connection to transfer without evidence of file movement or access.",
        "guardrails": ["USB connection does not prove file transfer.", "USB connection does not prove who connected the device.", "A path to removable media should be corroborated with file activity when possible."],
        "related_artifacts": ["Windows - USB / external device connection indicators", "External Media Hash / Copy Refresher"],
    },
    {
        "id": "browser_activity",
        "question": "Was there browser or download activity?",
        "look_at": ["Browser history", "Downloads database", "Cache", "Cookies/session artifacts", "Search terms/form history", "Downloaded file metadata", "User profile/account context"],
        "mindset": "Treat browser artifacts as activity indicators that need context. Separate URL existence, visit records, download records, and opened-file evidence.",
        "guardrails": ["A browser record does not always prove intent or knowledge.", "A download record does not prove the file was opened.", "Account sync, redirects, embedded content, and multiple users can complicate conclusions."],
        "related_artifacts": ["Browser - Browser activity indicators", "Windows - File access and user activity indicators"],
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



COACH_QUESTIONS = [{'answer_index': 1,
  'choices': ['The suspect typed the command.',
              'The command appears in the reviewed artifact and needs user/session context.',
              'The account owner definitely ran it.',
              'The command proves intent.'],
  'difficulty': 'Novice',
  'explanation': 'The artifact may support that command activity was present in the source you reviewed. It does not, '
                 'by itself, identify the human actor. Start with what the artifact shows, then look for access, '
                 'possession, session, credential, admission, or corroborating context.',
  'follow_up': ['Which account/session was active?',
                'Could remote access, automation, malware, or another person explain it?',
                'Is there possession, password, admission, camera, witness, or timeline context?'],
  'guardrail': 'Activity on a device is not the same as proof of the person who performed it.',
  'id': 'use_context_novice_command_actor',
  'question': 'A command appears in an artifact on a computer. What is the safest first conclusion?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['command', 'actor', 'attribution', 'session', 'password'],
  'topic': 'Use / Access Context'},
 {'answer_index': 1,
  'choices': ['As proof they performed every action on the device.',
              'As useful access/control context that still needs to be weighed with other evidence.',
              'As irrelevant because only artifacts matter.',
              'As proof all device contents belong to them.'],
  'difficulty': 'Experienced',
  'explanation': 'Exclusive password knowledge may support access or control over a device, especially when paired '
                 'with possession and account/session artifacts. It does not prove every action, file, message, or '
                 'command was performed by that person.',
  'follow_up': ['Who had physical possession?',
                'Was the device locked, unlocked, or actively logged in?',
                'Do timestamps, accounts, communications, or witnesses support control at relevant times?'],
  'guardrail': 'Control evidence can support attribution analysis, but it does not replace corroboration.',
  'id': 'use_context_experienced_password_control',
  'question': 'A person says they are the only one who knows the device password. How should that statement be used?',
  'related_playbook_id': 'mobile_device_extraction',
  'related_scenario_id': 'mobile_message_actor',
  'search_terms': ['password', 'control', 'admission', 'access', 'possession'],
  'topic': 'Use / Access Context'},
 {'answer_index': 2,
  'choices': ['Attribute the action to the account owner because the account name appears.',
              'Ignore the account artifact because shared devices are impossible to analyze.',
              'Separate account activity from human attribution and build a timeline using session, possession, remote '
              'access, credential, and corroborating evidence.',
              'State that malware must have performed the action.'],
  'difficulty': 'Expert',
  'explanation': 'On shared, family, workplace, or remotely accessible systems, attribution needs layered context. '
                 'Account artifacts matter, but they should be evaluated with logon type, remote sessions, physical '
                 'possession, credential knowledge, device location, other user activity, witness/camera context, and '
                 'possible automation or malware.',
  'follow_up': ['Was the logon local, remote, cached, service-based, or automated?',
                'Who had access to the device and credentials?',
                'Do unrelated artifacts place a specific person at the device near the relevant time?'],
  'guardrail': 'A named account is an attribution lead, not human-actor proof by itself.',
  'id': 'use_context_expert_remote_shared_device',
  'question': 'A suspicious action occurred under a named account on a shared or remotely accessible device. What is '
              'the strongest careful approach?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['account', 'remote access', 'shared device', 'attribution', 'logon'],
  'topic': 'Use / Access Context'},
 {'answer_index': 2,
  'choices': ['The browser/process appears to have downloaded the file.',
              'The file path and timestamp should be documented.',
              'A specific person definitely opened, viewed, and understood the file.',
              'Related file-open artifacts may be worth checking.'],
  'difficulty': 'Novice',
  'explanation': 'A download artifact can support that a download occurred, but viewing, knowledge, intent, and actor '
                 'identity need additional support such as file-open records, application history, thumbnails, '
                 'communications, admissions, or possession context.',
  'follow_up': ['Are there LNK, Jump List, recent-file, thumbnail, or app history artifacts?',
                'Was the file automatically downloaded or synced?',
                'Does user/session context line up with the timestamp?'],
  'guardrail': 'Downloaded is not the same as opened, viewed, understood, or personally selected.',
  'id': 'browser_file_novice_download',
  'question': 'A browser record shows a file was downloaded. What should the examiner avoid saying without more '
              'support?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['download', 'browser', 'file access', 'viewed', 'knowledge'],
  'topic': 'Browser / File Activity'},
 {'answer_index': 0,
  'choices': ['The file may have been accessed or presented to the user/application context reflected by those '
              'artifacts.',
              'The user fully read and understood the file.',
              'The file was created by the suspect.',
              'The file is contraband because it appears in recent files.'],
  'difficulty': 'Experienced',
  'explanation': 'Recent-file and shortcut artifacts may support interaction or application/user context, but the '
                 'strength depends on the artifact source, timestamp meaning, path, user profile, and corroborating '
                 'records.',
  'follow_up': ['Which artifact created the record and what timestamp does it represent?',
                'Does the path point to local, removable, network, or cloud storage?',
                'Are there app logs, thumbnails, or content artifacts that support interaction?'],
  'guardrail': 'File-access indicators need source-specific timestamp interpretation and do not automatically prove '
               'knowledge or intent.',
  'id': 'browser_file_experienced_file_open',
  'question': 'A file appears in recent-file and shortcut artifacts. What is a careful interpretation?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['recent files', 'LNK', 'Jump List', 'opened', 'artifact'],
  'topic': 'Browser / File Activity'},
 {'answer_index': 1,
  'choices': ['Cache or sync presence always proves the user intentionally saved the file.',
              'The file location, source mechanism, sync/cache behavior, timestamps, and user interaction artifacts '
              'should be evaluated before stronger claims.',
              'Cloud sync folders should be ignored.',
              'Browser cache always proves manual viewing.'],
  'difficulty': 'Expert',
  'explanation': 'Cache and sync artifacts can be generated by automatic processes, previews, redirects, sync clients, '
                 'or background application behavior. Stronger knowledge or actor claims need corroborating '
                 'interaction artifacts and context.',
  'follow_up': ['Was the file manually downloaded, cached, synced, previewed, or generated automatically?',
                'Are there access/open/viewing artifacts outside the cache or sync folder?',
                'Does the user profile and device usage support human interaction at the relevant time?'],
  'guardrail': 'File presence from cache/sync mechanisms does not automatically prove intentional possession, viewing, '
               'or knowledge.',
  'id': 'browser_file_expert_cloud_sync_cache',
  'question': 'A file exists in a browser cache or cloud-sync folder. What should the examiner consider before '
              'describing user knowledge?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['cache', 'cloud sync', 'browser', 'knowledge', 'automatic'],
  'topic': 'Browser / File Activity'},
 {'answer_index': 0,
  'choices': ['A USB/external device was connected or recognized, depending on the artifact.',
              'Files were definitely copied.',
              'The suspect connected it.',
              'The drive contents were viewed.'],
  'difficulty': 'Novice',
  'explanation': 'Connection artifacts can help document that a device was connected or recognized. File transfer, '
                 'viewing, or human actor identity require other supporting artifacts and context.',
  'follow_up': ['What device identifiers were recorded?',
                'What user/session was active?',
                'Are there file access/copy artifacts tied to that device?'],
  'guardrail': 'Connection is not transfer, and transfer is not actor identity.',
  'id': 'external_media_novice_connected',
  'question': 'USB artifacts show a drive was connected. What does that support most directly?',
  'related_playbook_id': 'external_media_hash_copy_refresher',
  'related_scenario_id': 'usb_connected_question',
  'search_terms': ['USB', 'external media', 'connection', 'transfer'],
  'topic': 'External Media'},
 {'answer_index': 1,
  'choices': ['Only the USB vendor name.',
              'USB connection data plus LNK/Jump Lists, shellbags, file paths, timestamps, copy tool logs, and '
              'user/session context.',
              'Only the capacity of the drive.',
              'Only whether the drive letter is common.'],
  'difficulty': 'Experienced',
  'explanation': 'Transfer questions usually require more than connection artifacts. Look for path-based file '
                 'activity, shell/application artifacts, timestamps, and context tying activity to the device and '
                 'session.',
  'follow_up': ['Do file paths reference removable drive letters or volume identifiers?',
                'Do access artifacts occur near the connection window?',
                'What user profile or session produced the artifacts?'],
  'guardrail': 'Do not claim file transfer based only on device connection records.',
  'id': 'external_media_experienced_transfer',
  'question': 'You need to evaluate whether files may have moved to or from USB media. Which set of artifacts is more '
              'helpful?',
  'related_playbook_id': 'external_media_hash_copy_refresher',
  'related_scenario_id': 'usb_connected_question',
  'search_terms': ['USB transfer', 'LNK', 'Jump List', 'shellbags', 'copy'],
  'topic': 'External Media'},
 {'answer_index': 1,
  'choices': ['Treat all removable-drive artifacts as one device.',
              'Map identifiers, volume serials, friendly names, drive letters, connection windows, and file-path '
              'artifacts to avoid mixing devices.',
              'Use the largest drive as the likely source.',
              'Ignore timestamps because drive letters change.'],
  'difficulty': 'Expert',
  'explanation': 'Drive letters can change and multiple devices can have similar names. Use identifiers and time '
                 'windows to connect specific media to specific activity while documenting uncertainty.',
  'follow_up': ['Which identifiers uniquely distinguish each device?',
                'Did drive letters change over time?',
                'Are file paths tied to a specific volume or only a temporary drive letter?'],
  'guardrail': 'Do not merge multiple removable devices into one narrative without mapping identifiers and time '
               'context.',
  'id': 'external_media_expert_multiple_devices',
  'question': 'Multiple external drives were connected over time. What is the safest analysis strategy?',
  'related_playbook_id': 'external_media_hash_copy_refresher',
  'related_scenario_id': 'usb_connected_question',
  'search_terms': ['volume serial', 'drive letter', 'USBSTOR', 'multiple devices'],
  'topic': 'External Media'},
 {'answer_index': 1,
  'choices': ['Conclude malware immediately.',
              'Treat it as a lead and review path, parent process, command line, network connections, modules, and '
              'corroboration.',
              'Delete it from the evidence.',
              'Ignore memory process data.'],
  'difficulty': 'Novice',
  'explanation': 'A process name can be misleading. Process path, parent/child relationship, command line, network '
                 'activity, DLLs/modules, hashes, and supporting artifacts help determine whether it is meaningful.',
  'follow_up': ['What is the full process path?', 'What launched it?', 'Is there network or injected-code context?'],
  'guardrail': 'A process name alone is not a malware finding.',
  'id': 'memory_novice_process_name',
  'question': 'A process name in memory looks suspicious. What should you do first?',
  'related_playbook_id': 'memory_ram_analysis_volatility',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['process', 'RAM', 'Volatility', 'pslist', 'pstree'],
  'topic': 'Memory / RAM'},
 {'answer_index': 1,
  'choices': ['The machine is confirmed compromised.',
              'The plugin output is a lead requiring process context, validation awareness, possible dumped content '
              'review, and corroboration.',
              'The user intentionally installed malware.',
              'No other artifacts matter.'],
  'difficulty': 'Experienced',
  'explanation': 'Suspicious memory output should be evaluated with process tree, path, modules, network connections, '
                 'tool documentation, dumps when justified, and other artifacts. It can guide analysis but should not '
                 'be overclaimed.',
  'follow_up': ['Which process/PID is involved?',
                'Can the output be corroborated with disk or network artifacts?',
                'Is specialized malware analysis needed?'],
  'guardrail': 'Suspicious memory output is not automatic proof of compromise, intent, or actor identity.',
  'id': 'memory_experienced_malfind',
  'question': 'A memory plugin flags possible injected code. What is the best next mindset?',
  'related_playbook_id': 'memory_ram_analysis_volatility',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['malfind', 'injection', 'memory', 'malware'],
  'topic': 'Memory / RAM'},
 {'answer_index': 1,
  'choices': ['Ignore them if the capture succeeded.',
              'Document tool/version, timing, examiner actions, system changes, possible volatility loss, and any '
              'errors or environmental constraints.',
              'State the memory image is a perfect snapshot of original state.',
              'Avoid hashing the output because memory changes.'],
  'difficulty': 'Expert',
  'explanation': 'Live collection changes the system, and memory is constantly changing. Documentation should explain '
                 'what was captured, when, with what tool, and what actions/limitations may affect interpretation.',
  'follow_up': ['What actions occurred before capture?',
                'What tool/version and destination were used?',
                'Were hashes, logs, or errors recorded?'],
  'guardrail': 'A successful live capture is not a perfect record of every prior volatile condition.',
  'id': 'memory_expert_live_capture_limitations',
  'question': 'A RAM capture was performed on a live system after several minutes of interaction. How should '
              'limitations be handled?',
  'related_playbook_id': 'live_computer_acquisition_ram',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['RAM capture', 'volatile data', 'limitations', 'live acquisition'],
  'topic': 'Memory / RAM'},
 {'answer_index': 0,
  'choices': ['The file content being compared has not changed between those hash calculations.',
              'The file is relevant evidence.',
              'The file proves user intent.',
              'The file is safe to execute.'],
  'difficulty': 'Novice',
  'explanation': 'Matching hash values support file integrity for the compared content and algorithm. They do not '
                 'explain what the file means, whether it is relevant, or who used it.',
  'follow_up': ['What exactly was hashed?', 'When and by what tool?', 'Was the source or output path documented?'],
  'guardrail': 'Integrity is not interpretation.',
  'id': 'hashing_novice_integrity',
  'question': 'Two SHA-256 hash values match for a file. What does that support?',
  'related_playbook_id': 'external_media_hash_copy_refresher',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['hash', 'integrity', 'SHA-256', 'verify'],
  'topic': 'Integrity / Hashing'},
 {'answer_index': 1,
  'choices': ['Assume evidence tampering immediately.',
              'Document the mismatch, verify the exact file/source/algorithm, check paths and versions, preserve both '
              'results, and investigate the cause.',
              'Delete the newer hash record.',
              'Ignore the mismatch if filenames match.'],
  'difficulty': 'Experienced',
  'explanation': 'A mismatch is important, but the cause may include wrong file, changed metadata/content, different '
                 'algorithm, path confusion, export transformation, or actual alteration. Document before concluding.',
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
              'Clearly state each algorithm, source, tool/version, calculation time, and what each hash applies to.',
              'Mix values if filenames match.',
              'Use hashes to conclude who created the file.'],
  'difficulty': 'Expert',
  'explanation': 'Hash values are only meaningful when tied to an exact source, algorithm, tool/version, and time. '
                 'Different tools may hash different objects, containers, exports, or normalized outputs.',
  'follow_up': ['Were the same bytes hashed by each tool?',
                'Are hashes for original media, image, exported file, report, or container?',
                'Does policy prefer a specific algorithm?'],
  'guardrail': 'Hash values must be scoped to the exact object hashed.',
  'id': 'hashing_expert_algorithm_scope',
  'question': 'An examiner has MD5, SHA-1, and SHA-256 values from different tools. What is the careful reporting '
              'approach?',
  'related_playbook_id': 'external_media_hash_copy_refresher',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['MD5', 'SHA-1', 'SHA-256', 'algorithm', 'scope'],
  'topic': 'Integrity / Hashing'},
 {'answer_index': 2,
  'choices': ['The extraction contains a message record.',
              'The message content, direction, app, timestamp, and source should be documented.',
              'A specific person physically typed or read the message.',
              'Related account/device context may matter.'],
  'difficulty': 'Novice',
  'explanation': 'A message artifact may show content and metadata in the extraction, but the human actor may require '
                 'device possession, account control, lock state, app/session context, admissions, or corroboration.',
  'follow_up': ['Was the device in the person’s possession?',
                'Who knew the passcode or controlled the account?',
                'Does app/account data support who used it?'],
  'guardrail': 'A mobile artifact does not automatically prove who physically held or used the device.',
  'id': 'mobile_novice_message_actor',
  'question': 'A message exists in a mobile extraction. What should be avoided without more context?',
  'related_playbook_id': 'mobile_device_extraction',
  'related_scenario_id': 'mobile_message_actor',
  'search_terms': ['mobile', 'message', 'actor', 'possession', 'passcode'],
  'topic': 'Mobile'},
 {'answer_index': 1,
  'choices': ['Only the larger extraction matters.',
              'Extraction type, tool/version, device state, supported apps, limitations, and why outputs may differ.',
              'The smaller extraction is wrong.',
              'Different outputs prove tampering.'],
  'difficulty': 'Experienced',
  'explanation': 'Logical, file system, physical, cloud, and manual workflows can produce different artifact coverage. '
                 'Document extraction type and limitations before comparing outputs.',
  'follow_up': ['What extraction types were performed?',
                'What tool/version and device OS were involved?',
                'Which apps or databases were unsupported or partially parsed?'],
  'guardrail': 'Different mobile extraction outputs do not automatically mean one is false or altered.',
  'id': 'mobile_experienced_extraction_type',
  'question': 'Two mobile extractions from the same device show different artifact coverage. What should the examiner '
              'document?',
  'related_playbook_id': 'mobile_device_extraction',
  'related_scenario_id': 'mobile_message_actor',
  'search_terms': ['mobile extraction', 'logical', 'file system', 'limitations'],
  'topic': 'Mobile'},
 {'answer_index': 1,
  'choices': ['Device authority always includes all cloud data.',
              'Separate device extraction scope from cloud/account-return authority, source, timing, and limitations.',
              'Cloud data should be treated as live device data.',
              'Cloud artifacts prove the phone was present.'],
  'difficulty': 'Expert',
  'explanation': 'Cloud/account returns and device extractions can represent different sources, time ranges, sync '
                 'states, and legal authorities. Keep source and authority boundaries clear.',
  'follow_up': ['What authority covered the device vs account/cloud source?',
                'What time range did each source cover?',
                'Were records synced, server-side, cached, or locally stored?'],
  'guardrail': 'Do not blur device evidence and cloud/account evidence without documenting source and authority.',
  'id': 'mobile_expert_cloud_device_boundary',
  'question': 'A mobile investigation includes device data and possible cloud account data. What boundary should be '
              'kept clear?',
  'related_playbook_id': 'mobile_device_extraction',
  'related_scenario_id': 'mobile_message_actor',
  'search_terms': ['cloud', 'mobile', 'authority', 'sync', 'account'],
  'topic': 'Mobile'},
 {'answer_index': 0,
  'choices': ['Whether the timestamp basis/time zone/source meaning is understood.',
              'Whether the timestamp looks recent.',
              'Whether the timestamp has seconds.',
              'Whether the file name is short.'],
  'difficulty': 'Novice',
  'explanation': 'Timestamps can use local time, UTC, filesystem semantics, database-specific meanings, or '
                 'tool-normalized values. Know what the timestamp represents before building a timeline.',
  'follow_up': ['Is it UTC or local time?',
                'What event does it represent: created, modified, accessed, parsed, sent, received, connected?',
                'Did the tool normalize it?'],
  'guardrail': 'A timestamp without source meaning can mislead timeline analysis.',
  'id': 'timestamps_novice_timezone',
  'question': 'A timestamp appears in a tool report. What should be checked before comparing it to other events?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['timestamp', 'timezone', 'timeline', 'UTC'],
  'topic': 'Timestamps'},
 {'answer_index': 1,
  'choices': ['Choose the time that helps the case theory.',
              'Document source meanings, time zones, clock skew, parser behavior, and possible explanations before '
              'forming a timeline statement.',
              'Ignore one artifact.',
              'Average the times.'],
  'difficulty': 'Experienced',
  'explanation': 'Conflicting timestamps require source-aware interpretation. Differences can come from artifact '
                 'semantics, time zones, clock changes, sync behavior, parser normalization, or different stages of '
                 'activity.',
  'follow_up': ['What does each timestamp represent?',
                'Was system time reliable?',
                'Are there independent timeline anchors?'],
  'guardrail': 'Do not force conflicting timestamps into a cleaner story than the data supports.',
  'id': 'timestamps_experienced_sequence',
  'question': 'Two artifacts show close but conflicting times for related activity. What is a careful response?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'downloaded_file_question',
  'search_terms': ['timeline', 'clock skew', 'timestamp conflict', 'parser'],
  'topic': 'Timestamps'},
 {'answer_index': 0,
  'choices': ['Immediately calling it timestomping or anti-forensics.',
              'Checking system clock, artifact semantics, parser behavior, application behavior, and corroborating '
              'sources before naming a cause.',
              'Documenting the inconsistency.',
              'Looking for independent anchors.'],
  'difficulty': 'Expert',
  'explanation': 'Timestamp anomalies can have many causes. Anti-forensics is one possibility, but it should not be '
                 'asserted without supporting context and alternative explanations being considered.',
  'follow_up': ['Could clock drift, time zone conversion, sync, app behavior, or parser limits explain it?',
                'Are there event logs or external anchors?',
                'Is there other evidence of intentional manipulation?'],
  'guardrail': 'An anomalous timestamp is a question, not an automatic anti-forensics conclusion.',
  'id': 'timestamps_expert_anti_forensics',
  'question': 'A timestamp appears inconsistent with surrounding activity. What should an expert-level examiner avoid?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['timestomping', 'anti-forensics', 'timestamp anomaly', 'clock'],
  'topic': 'Timestamps'},
 {'answer_index': 0,
  'choices': ['The program appears in an artifact commonly associated with execution or application activity, '
              'depending on the source.',
              'The suspect definitely ran the program.',
              'The program was malicious.',
              'The program was installed by the user.'],
  'difficulty': 'Novice',
  'explanation': 'Program-execution artifacts can support application activity, but interpretation depends on artifact '
                 'type, source, timestamp meaning, account/session context, and corroboration.',
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
  'explanation': 'Deletion artifacts may support that a file was deleted or no longer exists in a location. Intent to '
                 'conceal requires additional context and should not be assumed.',
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
  'explanation': 'Artifact presence and absence both require context. Some artifacts are not created under every '
                 'condition, can be cleared, can be disabled, or may not apply to that OS/version/application '
                 'behavior.',
  'follow_up': ['Should the missing artifact have been created under these conditions?',
                'Is the tool parsing the right OS version and source?',
                'Are there alternative supporting or refuting artifacts?'],
  'guardrail': 'Absence of an expected artifact is not automatically proof that activity did not occur.',
  'id': 'windows_expert_artifact_disagreement',
  'question': 'One Windows artifact suggests execution, while another expected artifact is absent. What is the best '
              'expert response?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['artifact absence', 'program execution', 'parser limits', 'corroboration'],
  'topic': 'Windows / File Activity'},
 {'answer_index': 1,
  'choices': ['Tool output replaces examiner judgment.',
              'The output should be reviewed with source, tool/version, settings, limitations, and validation '
              'awareness.',
              'No documentation is needed if the result looks right.',
              'The tool vendor is responsible for all conclusions.'],
  'difficulty': 'Novice',
  'explanation': 'Tool output is a useful aid, but it needs examiner review. Important results should be documented '
                 'with tool/version, source, settings, and any known limitations or validation context.',
  'follow_up': ['What source data was parsed?',
                'What tool and version produced the result?',
                'Is the relevant function validated or corroborated?'],
  'guardrail': 'Tool output is not a substitute for examiner judgment.',
  'id': 'validation_novice_tool_output',
  'question': 'A forensic tool produces a parsed result. What should the examiner remember?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['tool output', 'validation', 'version', 'limitations'],
  'topic': 'Validation / Tool Confidence'},
 {'answer_index': 1,
  'choices': ['A public test or vendor claim means local checking is unnecessary.',
              'Use known test data/processes to document that this tool/version/environment behaves as expected for '
              'the function being relied on.',
              'Only validate tools after a case is challenged.',
              'Validation is only for lab managers.'],
  'difficulty': 'Experienced',
  'explanation': 'Local validation records help document tool/version/environment behavior. Public tests and vendor '
                 'docs can inform the process, but they do not replace local awareness of the exact setup being used.',
  'follow_up': ['What function are you relying on?',
                'What known test can demonstrate expected behavior?',
                'Where is the validation record stored?'],
  'guardrail': 'Tool confidence should be tied to the function, version, environment, and record of testing.',
  'id': 'validation_experienced_known_test',
  'question': 'Before relying on a tool feature for an important task, what local validation mindset is appropriate?',
  'related_playbook_id': 'memory_ram_analysis_volatility',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['validation', 'known test', 'tool version', 'environment'],
  'topic': 'Validation / Tool Confidence'},
 {'answer_index': 1,
  'choices': ['Pick the tool with the nicer report.',
              'Compare source data, tool versions, parser settings, documentation, known limitations, and '
              'manual/alternate validation where practical.',
              'Assume the commercial tool is always right.',
              'Delete the conflicting result.'],
  'difficulty': 'Expert',
  'explanation': 'Parser disagreement should be handled transparently. The examiner should understand source data, '
                 'parser assumptions, version behavior, time conversion, and whether another method can clarify the '
                 'issue.',
  'follow_up': ['Are both tools parsing the same source bytes?',
                'Do they define fields or timestamps differently?',
                'Can the artifact be manually reviewed or checked with a known reference?'],
  'guardrail': 'Parser disagreement is a finding to investigate, not something to hide or simplify.',
  'id': 'validation_expert_parser_disagreement',
  'question': 'Two tools parse the same artifact differently. What is the best next step?',
  'related_playbook_id': 'windows_artifact_review_refresher',
  'related_scenario_id': 'command_activity_actor',
  'search_terms': ['parser disagreement', 'tool validation', 'manual review', 'limitations'],
  'topic': 'Validation / Tool Confidence'}]


def search_coach_questions(query):
    needle = (query or "").strip().lower()
    if not needle:
        return []
    results = []
    for item in COACH_QUESTIONS:
        haystack_parts = [
            item.get("id", ""), item.get("topic", ""), item.get("difficulty", ""),
            item.get("question", ""), item.get("explanation", ""), item.get("guardrail", ""),
        ]
        haystack_parts.extend(item.get("choices", []))
        haystack_parts.extend(item.get("follow_up", []))
        haystack_parts.extend(item.get("search_terms", []))
        if needle in "\n".join(str(part) for part in haystack_parts).lower():
            results.append(item)
    return results


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

    {
        "term": "Device-use context",
        "category": "Attribution",
        "definition": "Information that helps evaluate who may have had access to or control over a device, account, session, or action. Examples can include password knowledge, possession, account ownership, logged-in sessions, admissions, and corroborating physical or witness context.",
        "related": ["Actor vs. artifact", "Corroboration", "Overclaim"],
    },
    {
        "term": "Actor vs. artifact",
        "category": "Attribution",
        "definition": "A reminder to separate what a digital artifact shows from who performed the related human action. A command, file access trace, or login artifact may support activity, but the human actor usually requires additional context.",
        "related": ["Device-use context", "Does not prove", "Limitations"],
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