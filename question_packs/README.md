# ByteCase Playbooks Question Packs

This folder is a development reference for downloadable Coach Mode question packs.

Runtime imported packs are copied to the user's local ByteCase folder:

```text
ByteCase/playbooks/question_packs/
```

Question packs are JSON files with pack metadata and a `questions` list. Use `sample_question_pack.json` as the starter template.

## Required pack fields

- `pack_name`
- `pack_id`
- `version`
- `publisher`
- `questions`

## Required question fields

- `id`
- `topic`
- `difficulty`
- `question`
- `choices`
- `answer_index`
- `explanation`
- `follow_up`
- `guardrail`
- `search_terms`

## Design note

Built-in questions remain part of the app. Imported packs are separate educational content and can be enabled or disabled from the Question Packs tab.
