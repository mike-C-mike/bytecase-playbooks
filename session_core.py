"""Session and export helpers for ByteCase Playbooks."""
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from playbook_data import APP_NAME, APP_VERSION, APP_ATTRIBUTION, APP_DOMAIN, PLAYBOOK_BOUNDARY, get_playbook
from settings_service import playbook_output_dir, sanitize_folder_name


def now_stamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def file_stamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def create_session(playbook_id: str, mode: str = "Field Reference") -> Dict[str, Any]:
    playbook = get_playbook(playbook_id)
    if not playbook:
        raise ValueError("Unknown playbook: " + str(playbook_id))
    return {
        "app": APP_NAME,
        "version": APP_VERSION,
        "created_at": now_stamp(),
        "updated_at": now_stamp(),
        "mode": mode,
        "playbook_id": playbook_id,
        "playbook_title": playbook["title"],
        "current_step_index": 1,
        "step_state": [
            {"index": idx + 1, "title": step["title"], "checked": False, "notes": ""}
            for idx, step in enumerate(playbook.get("steps", []))
        ],
    }


def apply_session_to_playbook(session: Dict[str, Any]) -> Dict[str, Any]:
    session["updated_at"] = now_stamp()
    playbook = get_playbook(session.get("playbook_id", ""))
    if playbook:
        session["playbook_title"] = playbook["title"]
        existing = {int(item.get("index", 0)): item for item in session.get("step_state", [])}
        rebuilt = []
        for idx, step in enumerate(playbook.get("steps", []), start=1):
            current = existing.get(idx, {})
            rebuilt.append({
                "index": idx,
                "title": step["title"],
                "checked": bool(current.get("checked", False)),
                "notes": current.get("notes", ""),
            })
        session["step_state"] = rebuilt
        max_step = max(1, len(rebuilt))
        try:
            current_index = int(session.get("current_step_index", 1))
        except (TypeError, ValueError):
            current_index = 1
        session["current_step_index"] = max(1, min(current_index, max_step))
    # Remove older case-style fields if a prior JSON is opened.
    for old_key in ["case_number", "examiner", "session_notes"]:
        session.pop(old_key, None)
    return session


def session_summary(session: Dict[str, Any]) -> Dict[str, Any]:
    steps = session.get("step_state", [])
    checked = sum(1 for step in steps if step.get("checked"))
    noted = sum(1 for step in steps if (step.get("notes") or "").strip())
    return {
        "total_steps": len(steps),
        "checked_steps": checked,
        "steps_with_notes": noted,
        "mode": session.get("mode", ""),
        "playbook_title": session.get("playbook_title", ""),
        "current_step_index": session.get("current_step_index", 1),
    }


def build_output_folder(settings: Dict[str, Any], session: Dict[str, Any]) -> Path:
    pb = sanitize_folder_name(session.get("playbook_title") or session.get("playbook_id") or "playbook").lower().replace(" ", "_")
    root = playbook_output_dir(settings)
    folder = root / "sessions" / f"{file_stamp()}_{pb}"
    folder.mkdir(parents=True, exist_ok=True)
    (root / "reports").mkdir(parents=True, exist_ok=True)
    return folder


def session_to_text(session: Dict[str, Any]) -> str:
    playbook = get_playbook(session.get("playbook_id", "")) or {}
    state = {item.get("index"): item for item in session.get("step_state", [])}
    lines: List[str] = []
    lines.append(APP_NAME)
    lines.append("Guided Examiner Reference Session")
    lines.append(APP_ATTRIBUTION)
    lines.append(APP_DOMAIN)
    lines.append("")
    lines.append(f"Version: {APP_VERSION}")
    lines.append(f"Created: {session.get('created_at', '')}")
    lines.append(f"Updated: {session.get('updated_at', '')}")
    lines.append(f"Mode: {session.get('mode', '')}")
    lines.append(f"Playbook: {session.get('playbook_title', '')}")
    lines.append(f"Current Step: {session.get('current_step_index', 1)}")
    lines.append("")
    lines.append("Boundary Notice")
    lines.append(PLAYBOOK_BOUNDARY)
    lines.append("")
    if playbook:
        lines.append("Playbook Summary")
        lines.append(playbook.get("summary", ""))
        lines.append("")
        lines.append("Use When")
        for item in playbook.get("use_when", []):
            lines.append(f"- {item}")
        lines.append("")
        lines.append("Avoid / Pause When")
        for item in playbook.get("avoid_when", []):
            lines.append(f"- {item}")
        lines.append("")
        lines.append("Steps")
        for idx, step in enumerate(playbook.get("steps", []), start=1):
            item = state.get(idx, {})
            mark = "x" if item.get("checked") else " "
            pointer = " <-- current step" if idx == session.get("current_step_index", 1) else ""
            lines.append(f"[{mark}] Step {idx}: {step.get('title', '')}{pointer}")
            lines.append(f"Field Focus: {step.get('field_focus', '')}")
            lines.append(f"Learning Detail: {step.get('learning_detail', '')}")
            lines.append(f"Why: {step.get('why', '')}")
            for label, key in [("Possible Tools", "tools"), ("Common Artifacts", "artifacts"), ("Cautions", "cautions"), ("Document", "document")]:
                lines.append(label + ":")
                for value in step.get(key, []):
                    lines.append(f"- {value}")
            notes = (item.get("notes") or "").strip()
            if notes:
                lines.append("Step Reference Notes:")
                lines.append(notes)
            lines.append("")
    summary = session_summary(session)
    lines.append("Session Summary")
    lines.append(f"Current Step: {summary['current_step_index']} of {summary['total_steps']}")
    lines.append(f"Reviewed Steps: {summary['checked_steps']} of {summary['total_steps']}")
    lines.append(f"Steps With Notes: {summary['steps_with_notes']}")
    return "\n".join(lines)


def save_session_outputs(settings: Dict[str, Any], session: Dict[str, Any]) -> Tuple[Path, Path, Optional[Path]]:
    session = apply_session_to_playbook(session)
    folder = build_output_folder(settings, session)
    base_name = f"bytecase_playbook_session_{sanitize_folder_name(session.get('playbook_id', 'playbook'))}_{file_stamp()}"
    json_path = folder / f"{base_name}.json"
    txt_path = folder / f"{base_name}.txt"
    docx_path = folder / f"{base_name}.docx"
    json_path.write_text(json.dumps(session, indent=2), encoding="utf-8")
    txt_path.write_text(session_to_text(session), encoding="utf-8")
    if settings.get("output", {}).get("export_docx", True):
        try:
            from docx_exporter import export_session_docx
            export_session_docx(session, docx_path)
        except Exception as exc:
            error_path = folder / "docx_export_error.txt"
            error_path.write_text(str(exc), encoding="utf-8")
            docx_path = None
    else:
        docx_path = None
    return json_path, txt_path, docx_path


def load_session(path: Any) -> Dict[str, Any]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return apply_session_to_playbook(data)
