"""Glossary term-pack loader for ByteCase Playbooks.

Built-in glossary terms are organized by topic so the reference repository can grow
without bloating playbook_data.py.

Future GUI editing can write optional custom terms to one of these JSON files:
- custom_glossary_terms.json in the application folder
- ByteCase/playbooks/custom/glossary_terms.json in the user profile

A custom glossary JSON file should contain a list of dictionaries using the same
field names as the built-in entries. At minimum, provide term, category, and
definition.
"""
import json
from pathlib import Path

from .acquisition_terms import TERMS as ACQUISITION_TERMS
from .browser_terms import TERMS as BROWSER_TERMS
from .core_terms import TERMS as CORE_TERMS
from .legal_scope_terms import TERMS as LEGAL_SCOPE_TERMS
from .memory_terms import TERMS as MEMORY_TERMS
from .mobile_terms import TERMS as MOBILE_TERMS
from .validation_terms import TERMS as VALIDATION_TERMS
from .windows_artifacts import TERMS as WINDOWS_ARTIFACT_TERMS

BUILT_IN_GLOSSARY_TERMS = []
BUILT_IN_GLOSSARY_TERMS.extend(CORE_TERMS)
BUILT_IN_GLOSSARY_TERMS.extend(ACQUISITION_TERMS)
BUILT_IN_GLOSSARY_TERMS.extend(MEMORY_TERMS)
BUILT_IN_GLOSSARY_TERMS.extend(WINDOWS_ARTIFACT_TERMS)
BUILT_IN_GLOSSARY_TERMS.extend(MOBILE_TERMS)
BUILT_IN_GLOSSARY_TERMS.extend(BROWSER_TERMS)
BUILT_IN_GLOSSARY_TERMS.extend(VALIDATION_TERMS)
BUILT_IN_GLOSSARY_TERMS.extend(LEGAL_SCOPE_TERMS)


def normalize_term(item):
    normalized = dict(item or {})
    normalized.setdefault("term", "")
    normalized.setdefault("category", "General")
    normalized.setdefault("definition", "")
    normalized.setdefault("plain_language", normalized.get("definition", ""))
    normalized.setdefault("why_it_matters", "")
    normalized.setdefault("common_examples", [])
    normalized.setdefault("guardrail", "")
    normalized.setdefault("related", [])
    normalized.setdefault("related_playbooks", [])
    normalized.setdefault("aliases", [])
    return normalized


def custom_glossary_paths():
    return [
        Path.cwd() / "custom_glossary_terms.json",
        Path.home() / "ByteCase" / "playbooks" / "custom" / "glossary_terms.json",
    ]


def load_custom_glossary_terms():
    terms = []
    for path in custom_glossary_paths():
        if not path.exists():
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(data, dict):
            data = data.get("terms", [])
        if not isinstance(data, list):
            continue
        for item in data:
            if isinstance(item, dict) and item.get("term"):
                terms.append(normalize_term(item))
    return terms


def load_glossary_terms():
    terms = [normalize_term(item) for item in BUILT_IN_GLOSSARY_TERMS]
    terms.extend(load_custom_glossary_terms())
    return terms


GLOSSARY_TERMS = load_glossary_terms()


def get_glossary_categories():
    return sorted({item.get("category", "General") for item in GLOSSARY_TERMS})


def search_glossary(query):
    needle = (query or "").strip().lower()
    if not needle:
        return []
    results = []
    for item in GLOSSARY_TERMS:
        haystack_parts = [
            item.get("term", ""),
            item.get("category", ""),
            item.get("definition", ""),
            item.get("plain_language", ""),
            item.get("why_it_matters", ""),
            item.get("guardrail", ""),
        ]
        for key in ("common_examples", "related", "related_playbooks", "aliases"):
            haystack_parts.extend(item.get(key, []))
        if needle in "\n".join(str(part) for part in haystack_parts).lower():
            results.append(item)
    return results
