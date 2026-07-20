"""Built-in ByteCase Playbooks content.

The content is intentionally guidance-focused. It does not perform evidence
collection, extraction, parsing, or analysis.
"""

APP_NAME = "ByteCase Playbooks"
APP_SUBTITLE = "Guided Examiner Reference and Learning Companion"
APP_VERSION = "0.1.0"
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
            },
        ],
    },
]


def get_playbook(playbook_id):
    for playbook in PLAYBOOKS:
        if playbook["id"] == playbook_id:
            return playbook
    return None


def categories():
    return sorted({pb["category"] for pb in PLAYBOOKS})
