"""Settings helpers for ByteCase Playbooks."""
import json
from pathlib import Path
from typing import Any, Dict

from playbook_data import APP_VERSION

SETTINGS_FILENAME = "settings.json"
DEFAULT_OUTPUT_ROOT = Path.home() / "ByteCase"

DEFAULT_SETTINGS: Dict[str, Any] = {
    "app": {
        "name": "ByteCase Playbooks",
        "version": APP_VERSION,
    },
    "appearance": {
        "theme": "system",
    },
    "output": {
        "output_root": "",
        "export_txt": True,
        "export_docx": True,
    },
    "defaults": {
        "mode": "Field Reference",
    },
}


def settings_path() -> Path:
    return Path.cwd() / SETTINGS_FILENAME


def deep_merge(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    result = dict(base)
    for key, value in (override or {}).items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def load_settings() -> Dict[str, Any]:
    path = settings_path()
    if not path.exists():
        return json.loads(json.dumps(DEFAULT_SETTINGS))
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return json.loads(json.dumps(DEFAULT_SETTINGS))
    return deep_merge(DEFAULT_SETTINGS, data)


def save_settings(settings: Dict[str, Any]) -> Path:
    path = settings_path()
    path.write_text(json.dumps(settings, indent=2), encoding="utf-8")
    return path


def get_output_root(settings: Dict[str, Any]) -> Path:
    raw = (settings.get("output", {}).get("output_root") or "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_OUTPUT_ROOT


def playbook_output_dir(settings: Dict[str, Any]) -> Path:
    return get_output_root(settings) / "playbooks"


def sanitize_folder_name(value: str) -> str:
    cleaned = "".join(ch if ch not in '<>:"/\\|?*' else "_" for ch in str(value).strip())
    return cleaned or "playbook"
