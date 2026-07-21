# ByteCase Playbooks Navigation Model

Version: v0.10.3

## Product identity

ByteCase Playbooks is a reference and readiness tool.

It explains examiner workflows, reinforces careful interpretation, and supports practice drills. It does not track case progress, write case notes, perform evidence parsing, or make findings.

## Top-level lanes

### Home

Landing page and command center.

Use Home for:

- selecting a playbook
- opening the current session
- choosing the main path
- starting from a simple user question

### Workbench

Active examiner reference and readiness area.

Workbench contains:

- Guide
- Playbook
- Artifacts
- Coaching
- Drills

Use Workbench when actively learning, refreshing, thinking through an artifact, or practicing examiner judgment.

### Library

Support and administration area.

Library contains:

- Save / Export
- Search
- Question Packs
- Settings

Use Library for saving sessions, searching the reference repository, managing imported question packs, or adjusting app settings.

## v0.10.1 navigation decision

The v0.10.0 quick navigation bar was removed. It repeated the Workbench and Library navigation and made the header feel crowded.

The current model intentionally keeps only:

- top-level lanes
- Workbench subtabs
- Library subtabs

## Workbench focus

Artifacts should begin with the examiner question, not the artifact list.

Coaching should focus on mentoring-style judgment prompts, not tabletop exercises or formal testing.

Drills should remain quick practice and missed-question review.

## Parking-lot boundary

Do not add these to Playbooks:

- Case progress tracking
- Case-specific workflow checklist
- Examiner observation notes
- Evidence findings
- Formal training completion records
- Tool validation records
- Tabletop exercise management

Potential future modules:

- ByteCase Workflow for case progress tracking
- ByteCase Tabletop / ByteCase Scenarios for structured tabletop exercises
- Question Pack Builder for authoring/exporting drill packs


## v0.10.3 artifact-library decision

The Artifacts lane now uses situation-specific question lists. This avoids mismatched prompts such as Windows USB questions appearing during mobile-device review. The intended user path is:

1. Select the closest situation.
2. Select a question that makes sense for that situation.
3. Review mapped artifact areas, where to look, common tools/methods, guardrails, and documentation reminders.

This keeps the artifact library decision-driven instead of forcing the user to start by already knowing which artifact family matters.


## v0.10.3 Coaching path model

The Coaching lane is now a chained mentoring experience rather than a one-question reveal model.

- Coaching content lives in `coach_questions/coaching_paths.py`.
- The GUI records each response without revealing the answer during the path.
- The final review explains the full reasoning chain.
- Coaching stays inside Playbooks because it supports reference and readiness, but tabletop exercises remain parked as a future separate module candidate.
