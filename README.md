# ByteCase Playbooks

**Guided Examiner Reference and Readiness Companion**  
Part of the ByteCase toolset by Forensics Byte.  
https://byte-case.com

## Version

v0.10.7

## Purpose

ByteCase Playbooks is a click-based reference and readiness tool for digital evidence examiners. It is designed for real-time reference during a task, quick refresher learning, and judgment-focused practice.

It helps answer questions such as:

- What workflow am I dealing with?
- What should I understand before I act?
- Why does this step matter?
- What artifact areas may commonly matter?
- What should I document?
- What should I avoid overclaiming?
- What does this artifact or step not prove by itself?
- What extra context may help connect device activity to a person?

## What ByteCase Playbooks is not

ByteCase Playbooks does not perform acquisition, extraction, parsing, analysis, or reporting conclusions. It does not replace legal authority, agency policy, formal training, tool validation, or examiner judgment.

It is not the same as ByteCase Workflow.

- **ByteCase Playbooks explains and reinforces the work.**
- **ByteCase Workflow tracks the work.**

## Current structure

### Home

Landing page and command center.

### Workbench

Active reference and readiness tools:

- Guide
- Playbook
- Artifacts
- Coaching
- Drills

### Library

Support and administration tools:

- Save / Export
- Search
- Question Packs
- Settings

## v0.10.7 updates

v0.10.7 is a content consistency sprint focused on credibility.

### Content audit areas

This sprint reviewed and tightened:

- Artifact questions
- Coaching paths
- Coach drill questions
- Glossary/search wording
- Tool and method examples
- Guardrails and explanations

### Artifact guidance cleanup

The Artifact section now has tighter, situation-specific wording around common examiner questions. The content was reviewed to reduce mismatched situation/question pairings and keep artifact guidance connected to the selected device or workflow.

Artifact guidance continues to use tool names only as examples of commonly used industry tools or methods. They are not endorsements, recommendations, validation statements, or substitutes for agency-approved tools and local validation.

### Coaching path cleanup

Chained Coaching paths were reviewed for:

- source-first thinking
- scope and authority reminders
- attribution caution
- proper use of “may support” language
- avoiding claims not supported by the artifact alone
- useful final debriefs

Coaching content remains stored in:

```text
coach_questions/coaching_paths.py
```

### Drill question cleanup

Built-in Coach Mode drill questions were rewritten for cleaner wording and better answer-choice balance.

The goal is to test examiner judgment, not pattern recognition. Correct answers are no longer consistently the longest option, and explanations now focus more consistently on source, scope, corroboration, and limitations.

## Recent milestones

### v0.10.5

Fixed mouse-wheel behavior for both outer scrollable pages and nested Text/Listbox/Treeview widgets.

### v0.10.3

Expanded Coaching into chained mentoring paths. The user answers each step first, then receives the full review and debrief at the end.

### v0.10.2

Expanded the Artifact library and made artifact questions situation-specific.

### v0.10.1

Removed the repetitive quick navigation bar, renamed Scenarios to Coaching, and reworked the Artifacts section around “What are you trying to understand?”

## Parking lot

Still parked for later:

- ByteCase Workflow for case progress tracking
- ByteCase Tabletop / ByteCase Scenarios as a future separate scenario exercise module
- Question Pack Builder for authoring/exporting drill packs
- persistent drill history and spaced refresher mode
- release packaging for Playbooks


## v0.10.7 UI Polish

This sprint tightened the interface without adding new forensic functionality. It shortened navigation labels, reduced repeated header text, increased the default window size, simplified panel names, tightened spacing, and reduced oversized text areas so the Workbench feels more professional and less crowded.

Top-level navigation remains:

```text
Home
Workbench
Library
```

Workbench subtabs are now concise:

```text
Guide
Steps
Artifacts
Coach
Drills
```

Library subtabs are now concise:

```text
Export
Search
Packs
Settings
```
