"""Coach Mode question-pack loader for ByteCase Playbooks.

This package keeps coach/training questions out of playbook_data.py so new
question packs can be added without bloating the main playbook content file.

To add a future pack:
1. Create a new module in this folder.
2. Define QUESTIONS as a list of question dictionaries.
3. Import and extend it below.
"""

from .browser_file_activity import QUESTIONS as BROWSER_FILE_ACTIVITY_QUESTIONS
from .external_media import QUESTIONS as EXTERNAL_MEDIA_QUESTIONS
from .integrity_hashing import QUESTIONS as INTEGRITY_HASHING_QUESTIONS
from .memory_ram import QUESTIONS as MEMORY_RAM_QUESTIONS
from .mobile import QUESTIONS as MOBILE_QUESTIONS
from .timestamps import QUESTIONS as TIMESTAMPS_QUESTIONS
from .use_access_context import QUESTIONS as USE_ACCESS_CONTEXT_QUESTIONS
from .validation_tool_confidence import QUESTIONS as VALIDATION_TOOL_CONFIDENCE_QUESTIONS
from .windows_file_activity import QUESTIONS as WINDOWS_FILE_ACTIVITY_QUESTIONS

COACH_QUESTIONS = []
COACH_QUESTIONS.extend(BROWSER_FILE_ACTIVITY_QUESTIONS)
COACH_QUESTIONS.extend(EXTERNAL_MEDIA_QUESTIONS)
COACH_QUESTIONS.extend(INTEGRITY_HASHING_QUESTIONS)
COACH_QUESTIONS.extend(MEMORY_RAM_QUESTIONS)
COACH_QUESTIONS.extend(MOBILE_QUESTIONS)
COACH_QUESTIONS.extend(TIMESTAMPS_QUESTIONS)
COACH_QUESTIONS.extend(USE_ACCESS_CONTEXT_QUESTIONS)
COACH_QUESTIONS.extend(VALIDATION_TOOL_CONFIDENCE_QUESTIONS)
COACH_QUESTIONS.extend(WINDOWS_FILE_ACTIVITY_QUESTIONS)


def get_coach_topics():
    return sorted({item.get("topic", "General") for item in COACH_QUESTIONS})


def get_coach_difficulties():
    preferred = ["Novice", "Experienced", "Expert"]
    present = set(item.get("difficulty", "Novice") for item in COACH_QUESTIONS)
    ordered = [value for value in preferred if value in present]
    ordered.extend(sorted(present.difference(preferred)))
    return ordered


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
