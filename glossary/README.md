# ByteCase Playbooks Glossary Packs

Glossary terms are organized by topic so the reference library can grow without crowding the main playbook file.

## Built-in pack files

- `core_terms.py`
- `acquisition_terms.py`
- `memory_terms.py`
- `windows_artifacts.py`
- `mobile_terms.py`
- `browser_terms.py`
- `validation_terms.py`
- `legal_scope_terms.py`

Each pack exposes a `TERMS` list.

## Term fields

Recommended fields:

```python
{
    "term": "Volatile Data",
    "category": "Acquisition",
    "definition": "Short definition.",
    "plain_language": "Plain-language explanation.",
    "why_it_matters": "Why the term matters for examiner decision-making.",
    "common_examples": ["Example 1", "Example 2"],
    "guardrail": "What not to overclaim.",
    "related": ["Related term"],
    "related_playbooks": ["Related playbook title"],
    "aliases": ["search alias"],
}
```

## Future editable/custom terms

The loader already checks for optional custom JSON files:

- `custom_glossary_terms.json` in the application folder
- `ByteCase/playbooks/custom/glossary_terms.json` in the user profile

Those files can contain either a list of term dictionaries or an object with a `terms` list. This leaves room for a future Add/Edit/Remove Glossary Terms screen without another major refactor.
