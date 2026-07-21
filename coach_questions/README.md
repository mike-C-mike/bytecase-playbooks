# Coach Question Packs

Coach Mode questions are organized by topic. Each module exposes a `QUESTIONS` list containing question dictionaries.

Required fields for each question:

```python
{
    "id": "unique_question_id",
    "topic": "Use / Access Context",
    "difficulty": "Novice",
    "question": "Question text",
    "choices": ["A", "B", "C", "D"],
    "answer_index": 1,
    "explanation": "Why the answer is best",
    "follow_up": ["Follow-up prompt"],
    "guardrail": "Does-not-prove reminder",
    "related_playbook_id": "windows_artifact_review_refresher",
    "related_scenario_id": "command_activity_actor",
    "search_terms": ["actor", "attribution"]
}
```

To add a new pack, create a module in this folder, define `QUESTIONS`, then import and extend it in `__init__.py`.
