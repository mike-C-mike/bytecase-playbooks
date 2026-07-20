"""Validation helpers for ByteCase Playbooks."""
from typing import Dict, List


def validate_session(session: Dict) -> List[str]:
    warnings: List[str] = []
    if not (session.get("case_number") or "").strip():
        warnings.append("Case number is blank. Export will use NO_CASE.")
    if not (session.get("playbook_id") or "").strip():
        warnings.append("No playbook selected.")
    if not session.get("step_state"):
        warnings.append("No playbook steps are loaded.")
    return warnings
