# Coach Questions

Built-in Coach Mode questions live in this package as topic-based Python modules.

Runtime imported question packs are loaded from:

```text
ByteCase/playbooks/question_packs/
```

Imported packs are JSON files. They are validated before import and can be enabled or disabled from the Question Packs tab.

## Built-in topic modules

- `use_access_context.py`
- `memory_ram.py`
- `windows_file_activity.py`
- `browser_file_activity.py`
- `external_media.py`
- `integrity_hashing.py`
- `mobile.py`
- `timestamps.py`
- `validation_tool_confidence.py`

Each built-in module exposes a `QUESTIONS` list. The package loader combines built-in questions with enabled imported JSON packs.

## Runtime question pack folder

```text
ByteCase/playbooks/question_packs/
```

Settings for enabling or disabling packs are stored in:

```text
ByteCase/playbooks/question_packs/question_pack_settings.json
```

## Guidance

Built-in questions should stay conservative, generally useful, and Forensics Byte curated.

Imported packs are a good path for downloadable training material, agency-specific refreshers, and future topic releases from the website.
