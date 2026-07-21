"""Coach Mode question-pack loader for ByteCase Playbooks.

This package keeps coach/training questions out of playbook_data.py so new
question packs can be added without bloating the main playbook content file.

Built-in topic packs live as Python modules inside this package.
Downloadable/imported packs use JSON and are stored locally under:

    ByteCase/playbooks/question_packs/

Imported packs are educational content. The loader validates structure and
keeps imported content separate from the built-in ByteCase question set.
"""

import json
import shutil
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

from .browser_file_activity import QUESTIONS as BROWSER_FILE_ACTIVITY_QUESTIONS
from .external_media import QUESTIONS as EXTERNAL_MEDIA_QUESTIONS
from .integrity_hashing import QUESTIONS as INTEGRITY_HASHING_QUESTIONS
from .memory_ram import QUESTIONS as MEMORY_RAM_QUESTIONS
from .mobile import QUESTIONS as MOBILE_QUESTIONS
from .timestamps import QUESTIONS as TIMESTAMPS_QUESTIONS
from .use_access_context import QUESTIONS as USE_ACCESS_CONTEXT_QUESTIONS
from .validation_tool_confidence import QUESTIONS as VALIDATION_TOOL_CONFIDENCE_QUESTIONS
from .windows_file_activity import QUESTIONS as WINDOWS_FILE_ACTIVITY_QUESTIONS

ALLOWED_DIFFICULTIES = ["Novice", "Experienced", "Expert"]
MAX_PACK_BYTES = 2 * 1024 * 1024
MAX_QUESTIONS_PER_PACK = 500
PACK_SETTINGS_FILENAME = "question_pack_settings.json"

BUILT_IN_PACK_ID = "bytecase-built-in"
BUILT_IN_PACK_NAME = "Built-in ByteCase Questions"

BUILT_IN_COACH_QUESTIONS = []
BUILT_IN_COACH_QUESTIONS.extend(BROWSER_FILE_ACTIVITY_QUESTIONS)
BUILT_IN_COACH_QUESTIONS.extend(EXTERNAL_MEDIA_QUESTIONS)
BUILT_IN_COACH_QUESTIONS.extend(INTEGRITY_HASHING_QUESTIONS)
BUILT_IN_COACH_QUESTIONS.extend(MEMORY_RAM_QUESTIONS)
BUILT_IN_COACH_QUESTIONS.extend(MOBILE_QUESTIONS)
BUILT_IN_COACH_QUESTIONS.extend(TIMESTAMPS_QUESTIONS)
BUILT_IN_COACH_QUESTIONS.extend(USE_ACCESS_CONTEXT_QUESTIONS)
BUILT_IN_COACH_QUESTIONS.extend(VALIDATION_TOOL_CONFIDENCE_QUESTIONS)
BUILT_IN_COACH_QUESTIONS.extend(WINDOWS_FILE_ACTIVITY_QUESTIONS)


def _default_bytecase_root() -> Path:
    return Path.home() / "ByteCase"


def question_pack_directory() -> Path:
    """Return the user-local folder for downloaded/imported question packs."""
    return _default_bytecase_root() / "playbooks" / "question_packs"


def question_pack_settings_path() -> Path:
    return question_pack_directory() / PACK_SETTINGS_FILENAME


def bundled_sample_pack_path() -> Path:
    return Path(__file__).resolve().parent.parent / "sample_question_pack.json"


def sanitize_file_part(value: str) -> str:
    cleaned = "".join(ch if ch.isalnum() or ch in ("-", "_", ".") else "-" for ch in str(value).strip().lower())
    cleaned = "-".join(part for part in cleaned.split("-") if part)
    return cleaned or "question-pack"


def load_pack_settings() -> Dict[str, Any]:
    path = question_pack_settings_path()
    if not path.exists():
        return {"disabled_pack_ids": []}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"disabled_pack_ids": []}
    if not isinstance(data, dict):
        return {"disabled_pack_ids": []}
    disabled = data.get("disabled_pack_ids", [])
    if not isinstance(disabled, list):
        disabled = []
    return {"disabled_pack_ids": [str(value) for value in disabled]}


def save_pack_settings(settings: Dict[str, Any]) -> Path:
    folder = question_pack_directory()
    folder.mkdir(parents=True, exist_ok=True)
    path = question_pack_settings_path()
    path.write_text(json.dumps(settings, indent=2), encoding="utf-8")
    return path


def is_pack_enabled(pack_id: str) -> bool:
    settings = load_pack_settings()
    return str(pack_id) not in set(settings.get("disabled_pack_ids", []))


def set_question_pack_enabled(pack_id: str, enabled: bool) -> Path:
    settings = load_pack_settings()
    disabled = set(settings.get("disabled_pack_ids", []))
    if enabled:
        disabled.discard(str(pack_id))
    else:
        disabled.add(str(pack_id))
    settings["disabled_pack_ids"] = sorted(disabled)
    return save_pack_settings(settings)


def normalize_question(item: Dict[str, Any], pack_meta: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    normalized = dict(item or {})
    normalized.setdefault("id", "custom-question")
    normalized.setdefault("topic", "General")
    normalized.setdefault("difficulty", "Novice")
    normalized.setdefault("question", "")
    normalized.setdefault("choices", [])
    normalized.setdefault("explanation", "")
    normalized.setdefault("follow_up", [])
    normalized.setdefault("guardrail", "")
    normalized.setdefault("related_scenario_id", "")
    normalized.setdefault("search_terms", [])

    choices = normalized.get("choices", [])
    if not isinstance(choices, list):
        choices = []
    normalized["choices"] = [str(value) for value in choices]

    follow_up = normalized.get("follow_up", [])
    if isinstance(follow_up, str):
        follow_up = [follow_up]
    normalized["follow_up"] = [str(value) for value in follow_up] if isinstance(follow_up, list) else []

    search_terms = normalized.get("search_terms", [])
    if isinstance(search_terms, str):
        search_terms = [search_terms]
    normalized["search_terms"] = [str(value) for value in search_terms] if isinstance(search_terms, list) else []

    if "answer_index" not in normalized:
        answer_text = str(normalized.get("answer", ""))
        if answer_text and answer_text in normalized["choices"]:
            normalized["answer_index"] = normalized["choices"].index(answer_text)
        else:
            normalized["answer_index"] = 0

    try:
        normalized["answer_index"] = int(normalized.get("answer_index", 0))
    except (TypeError, ValueError):
        normalized["answer_index"] = 0

    if pack_meta is None:
        pack_meta = {}
    normalized.setdefault("pack_id", pack_meta.get("pack_id", BUILT_IN_PACK_ID))
    normalized.setdefault("pack_name", pack_meta.get("pack_name", BUILT_IN_PACK_NAME))
    normalized.setdefault("pack_version", pack_meta.get("version", "built-in"))
    normalized.setdefault("pack_publisher", pack_meta.get("publisher", "Forensics Byte"))
    normalized.setdefault("pack_source", pack_meta.get("source", "Built-in"))
    normalized.setdefault("pack_path", pack_meta.get("path", ""))
    return normalized


def validate_question(item: Any, existing_ids: set, index: int) -> Tuple[Optional[Dict[str, Any]], List[str], List[str]]:
    errors = []
    warnings = []
    if not isinstance(item, dict):
        return None, [f"Question {index + 1}: question entry must be an object."], []

    normalized = normalize_question(item)
    qid = str(normalized.get("id", "")).strip()
    if not qid:
        errors.append(f"Question {index + 1}: missing id.")
    elif qid in existing_ids:
        errors.append(f"Question {index + 1}: duplicate question id '{qid}'.")
    else:
        existing_ids.add(qid)

    if not str(normalized.get("question", "")).strip():
        errors.append(f"Question {index + 1}: missing question text.")

    choices = normalized.get("choices", [])
    if not isinstance(choices, list) or len(choices) < 2:
        errors.append(f"Question {index + 1}: choices must contain at least two options.")

    answer_index = normalized.get("answer_index", 0)
    if not isinstance(answer_index, int) or answer_index < 0 or answer_index >= len(choices):
        errors.append(f"Question {index + 1}: answer_index must point to one of the choices.")

    difficulty = normalized.get("difficulty", "Novice")
    if difficulty not in ALLOWED_DIFFICULTIES:
        warnings.append(f"Question {index + 1}: difficulty '{difficulty}' is not one of {', '.join(ALLOWED_DIFFICULTIES)}.")

    return normalized, errors, warnings


def validate_question_pack_data(data: Any) -> Dict[str, Any]:
    errors: List[str] = []
    warnings: List[str] = []
    if not isinstance(data, dict):
        return {"ok": False, "errors": ["Question pack must be a JSON object."], "warnings": [], "pack": None, "questions": []}

    pack_name = str(data.get("pack_name", "")).strip()
    pack_id = str(data.get("pack_id", "")).strip()
    version = str(data.get("version", "")).strip()
    publisher = str(data.get("publisher", "")).strip()
    questions = data.get("questions", [])

    if not pack_name:
        errors.append("Missing pack_name.")
    if not pack_id:
        errors.append("Missing pack_id.")
    if not version:
        errors.append("Missing version.")
    if not publisher:
        warnings.append("Missing publisher. The pack will be marked as Unknown Publisher.")
        publisher = "Unknown Publisher"
    if not isinstance(questions, list):
        errors.append("questions must be a list.")
        questions = []
    if len(questions) > MAX_QUESTIONS_PER_PACK:
        errors.append(f"Pack contains {len(questions)} questions. Maximum supported per pack is {MAX_QUESTIONS_PER_PACK}.")

    normalized_questions: List[Dict[str, Any]] = []
    seen_ids = set()
    for idx, item in enumerate(questions):
        normalized, q_errors, q_warnings = validate_question(item, seen_ids, idx)
        errors.extend(q_errors)
        warnings.extend(q_warnings)
        if normalized is not None:
            normalized_questions.append(normalized)

    pack = {
        "pack_name": pack_name,
        "pack_id": pack_id,
        "version": version,
        "publisher": publisher,
        "description": str(data.get("description", "")).strip(),
        "license": str(data.get("license", "")).strip(),
        "questions": normalized_questions,
    }
    return {"ok": not errors, "errors": errors, "warnings": warnings, "pack": pack, "questions": normalized_questions}


def validate_question_pack_file(path: Path) -> Dict[str, Any]:
    path = Path(path)
    if not path.exists():
        return {"ok": False, "errors": ["File does not exist."], "warnings": [], "pack": None, "questions": []}
    try:
        size = path.stat().st_size
    except OSError as exc:
        return {"ok": False, "errors": [f"Could not read file details: {exc}"], "warnings": [], "pack": None, "questions": []}
    if size > MAX_PACK_BYTES:
        return {"ok": False, "errors": [f"Question pack is too large. Maximum supported size is {MAX_PACK_BYTES} bytes."], "warnings": [], "pack": None, "questions": []}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"ok": False, "errors": [f"Could not parse JSON: {exc}"], "warnings": [], "pack": None, "questions": []}
    return validate_question_pack_data(data)


def installed_question_pack_files() -> List[Path]:
    folder = question_pack_directory()
    if not folder.exists():
        return []
    files = []
    for path in sorted(folder.glob("*.json")):
        if path.name == PACK_SETTINGS_FILENAME:
            continue
        files.append(path)
    return files


def import_question_pack(source_path: Path) -> Dict[str, Any]:
    source_path = Path(source_path)
    validation = validate_question_pack_file(source_path)
    if not validation.get("ok"):
        return validation
    pack = validation.get("pack") or {}
    folder = question_pack_directory()
    folder.mkdir(parents=True, exist_ok=True)
    filename = f"{sanitize_file_part(pack.get('pack_id', 'question-pack'))}-{sanitize_file_part(pack.get('version', '1.0.0'))}.json"
    destination = folder / filename

    # Treat pack_id as the stable identity for a downloadable pack. When a new
    # version is imported, remove older local files with the same pack_id so the
    # user does not accidentally drill against duplicate versions of the same pack.
    for existing in installed_question_pack_files():
        existing_validation = validate_question_pack_file(existing)
        existing_pack = existing_validation.get("pack") or {}
        if existing_pack.get("pack_id") == pack.get("pack_id") and existing.resolve() != destination.resolve():
            try:
                existing.unlink()
            except OSError:
                pass

    if source_path.resolve() != destination.resolve():
        shutil.copy2(str(source_path), str(destination))
    set_question_pack_enabled(pack.get("pack_id", ""), True)
    validation["destination"] = str(destination)
    return validation


def question_pack_records(include_disabled: bool = True) -> List[Dict[str, Any]]:
    records = [
        {
            "pack_name": BUILT_IN_PACK_NAME,
            "pack_id": BUILT_IN_PACK_ID,
            "version": "built-in",
            "publisher": "Forensics Byte",
            "description": "Core ByteCase Playbooks Coach Mode questions included with the app.",
            "license": "ByteCase built-in educational content",
            "enabled": True,
            "built_in": True,
            "path": "",
            "question_count": len(BUILT_IN_COACH_QUESTIONS),
            "errors": [],
            "warnings": [],
        }
    ]

    disabled = set(load_pack_settings().get("disabled_pack_ids", []))
    for path in installed_question_pack_files():
        validation = validate_question_pack_file(path)
        pack = validation.get("pack") or {}
        pack_id = pack.get("pack_id") or path.stem
        enabled = pack_id not in disabled
        if include_disabled or enabled:
            records.append(
                {
                    "pack_name": pack.get("pack_name", path.stem),
                    "pack_id": pack_id,
                    "version": pack.get("version", ""),
                    "publisher": pack.get("publisher", ""),
                    "description": pack.get("description", ""),
                    "license": pack.get("license", ""),
                    "enabled": enabled,
                    "built_in": False,
                    "path": str(path),
                    "question_count": len(pack.get("questions", [])) if validation.get("ok") else 0,
                    "errors": validation.get("errors", []),
                    "warnings": validation.get("warnings", []),
                }
            )
    return records


def load_external_coach_questions() -> List[Dict[str, Any]]:
    questions: List[Dict[str, Any]] = []
    disabled = set(load_pack_settings().get("disabled_pack_ids", []))
    seen_ids = {str(item.get("id", "")) for item in BUILT_IN_COACH_QUESTIONS}
    for path in installed_question_pack_files():
        validation = validate_question_pack_file(path)
        if not validation.get("ok"):
            continue
        pack = validation.get("pack") or {}
        pack_id = pack.get("pack_id", "")
        if pack_id in disabled:
            continue
        meta = dict(pack)
        meta["source"] = "Imported"
        meta["path"] = str(path)
        for item in validation.get("questions", []):
            question_id = str(item.get("id", ""))
            if question_id in seen_ids:
                continue
            seen_ids.add(question_id)
            questions.append(normalize_question(item, meta))
    return questions


def load_coach_questions() -> List[Dict[str, Any]]:
    built_in_meta = {
        "pack_id": BUILT_IN_PACK_ID,
        "pack_name": BUILT_IN_PACK_NAME,
        "version": "built-in",
        "publisher": "Forensics Byte",
        "source": "Built-in",
        "path": "",
    }
    questions = [normalize_question(item, built_in_meta) for item in BUILT_IN_COACH_QUESTIONS]
    questions.extend(load_external_coach_questions())
    return questions


COACH_QUESTIONS = load_coach_questions()


def get_coach_topics(questions: Optional[Iterable[Dict[str, Any]]] = None) -> List[str]:
    items = list(questions) if questions is not None else COACH_QUESTIONS
    return sorted({item.get("topic", "General") for item in items})


def get_coach_difficulties(questions: Optional[Iterable[Dict[str, Any]]] = None) -> List[str]:
    items = list(questions) if questions is not None else COACH_QUESTIONS
    present = set(item.get("difficulty", "Novice") for item in items)
    ordered = [value for value in ALLOWED_DIFFICULTIES if value in present]
    ordered.extend(sorted(present.difference(ALLOWED_DIFFICULTIES)))
    return ordered


def get_coach_pack_names(questions: Optional[Iterable[Dict[str, Any]]] = None) -> List[str]:
    items = list(questions) if questions is not None else COACH_QUESTIONS
    return sorted({item.get("pack_name", BUILT_IN_PACK_NAME) for item in items})


def search_coach_questions(query: str, questions: Optional[Iterable[Dict[str, Any]]] = None) -> List[Dict[str, Any]]:
    needle = (query or "").strip().lower()
    if not needle:
        return []
    results = []
    items = list(questions) if questions is not None else COACH_QUESTIONS
    for item in items:
        haystack_parts = [
            item.get("id", ""), item.get("topic", ""), item.get("difficulty", ""),
            item.get("question", ""), item.get("explanation", ""), item.get("guardrail", ""),
            item.get("pack_name", ""), item.get("pack_publisher", ""), item.get("pack_id", ""),
        ]
        haystack_parts.extend(item.get("choices", []))
        haystack_parts.extend(item.get("follow_up", []))
        haystack_parts.extend(item.get("search_terms", []))
        if needle in "\n".join(str(part) for part in haystack_parts).lower():
            results.append(item)
    return results
