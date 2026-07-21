# ByteCase Playbooks

**Guided Examiner Reference and Learning Companion**  
Part of the ByteCase toolset by Forensics Byte.  
https://byte-case.com

## Version

v0.9.0

## Purpose

ByteCase Playbooks is a click-based reference, refresher, and learning tool for digital evidence examiners. It is designed for real-time reference during an investigation or as a downtime learning companion for new or occasional examiners.

It helps answer questions such as:

- What kind of workflow am I dealing with?
- Why does this step matter?
- Why does this step come before another step?
- What artifact areas may commonly matter?
- What tools may be used for this area?
- What should I document?
- What should I avoid overclaiming?
- What does this step not prove by itself?
- What extra context may help connect device activity to a person?

## What ByteCase Playbooks is not

ByteCase Playbooks does not perform acquisition, extraction, parsing, analysis, or reporting conclusions. It does not replace legal authority, agency policy, formal training, tool validation, or examiner judgment.

It is not the same as ByteCase Workflow.

- **ByteCase Playbooks explains the work.**
- **ByteCase Workflow tracks the work.**

## Included playbooks

This release includes six built-in playbooks:

1. Live Computer Acquisition / RAM Capture
2. Dead-Box Computer Imaging
3. Mobile Device Extraction Refresher
4. Memory / RAM Analysis Refresher
5. Windows Artifact Review Refresher
6. External Media Hash / Copy Refresher

## v0.9.0 updates

v0.9.0 expands Coach Mode into a more useful drill workflow.

Coach Mode is a question-and-answer practice area that helps reinforce examiner thinking, attribution caution, documentation habits, and overclaim guardrails.

Changes include:

- Added selectable drill size: All, 5, 10, 15, or 20 questions
- Added drill order control: In order or Shuffle
- Added missed-question tracking
- Added Review Missed mode
- Added Coach Drill Summary popup
- Added Copy Missed / Summary action
- Preserved topic and difficulty filtering
- Preserved answer checking, explanations, follow-up questions, and guardrails
- Preserved shortcuts to related Scenario Coach cards and reference terms
- Preserved Playbooks as a non-case reference/refresher module

## Coach Mode topics

Starter question topics include:

- Use / Access Context
- Browser / File Activity
- External Media
- Memory / RAM
- Integrity / Hashing
- Mobile
- Timestamps
- Windows / File Activity
- Validation / Tool Confidence


## Coach drills and missed-question review

Coach Mode can now be used as a short practice drill instead of only a linear question list. The examiner can choose a topic, difficulty, question count, and order. After checking answers, missed questions can be loaded into a focused review set.

Drill controls include:

- Topic
- Difficulty
- Count
- Order
- Start / Reset
- Review Missed
- Summary
- Copy Missed

The drill score and missed-question review are local to the current app session. Coach Mode remains a refresher and learning tool. It does not score case work and does not write case notes.

## Attribution / use-context mindset

ByteCase Playbooks intentionally separates:

```text
What the artifact shows
```

from:

```text
Who performed the human action
```

For example, a command appearing on a device can support that the command existed or was executed in a certain environment, but it does not automatically prove which person typed or initiated it. The examiner should look for supporting context such as device possession, account/session information, password knowledge, admissions, remote-access indicators, cloud sync behavior, automation, malware, and corroborating physical or witness context when attribution matters.

An admission such as being the only person who knows a device password can support access/control context, but it should still be documented accurately and weighed with the rest of the evidence.

## Main modes

### Field Reference

A concise real-time reference mode for when the examiner needs the immediate order of thinking, cautions, and documentation reminders.

### Learning / Refresher

A deeper mode for training, downtime review, or examiners who do not perform a task often.

## Step card design

Each playbook step can include:

- Field focus
- Learning detail
- Why this matters
- Possible tools
- Common artifacts / outputs
- Cautions
- Does-not-prove reminders
- What to document
- Command examples, where useful
- Optional step reference notes

Each step has quick explanation buttons:

- Why?
- Tools
- Artifacts
- Cautions
- Document
- Commands
- Does Not Prove
- Use Context

## Output structure

Default output root:

```text
C:\Users\<user>\ByteCase\
```

Session exports are stored as:

```text
ByteCase\
  playbooks\
    sessions\
      <timestamp>_<playbook_name>\
        bytecase_playbook_session_<playbook>_<timestamp>.json
        bytecase_playbook_session_<playbook>_<timestamp>.txt
        bytecase_playbook_session_<playbook>_<timestamp>.docx
```

Saved playbook sessions are not case notes and are not written under a case folder. They are intended to reopen the same playbook, mode, current step, reviewed steps, and step reference notes.

Coach Mode practice progress is currently in-memory only and is not written to case output.

## Dependencies

Runtime:

- Python standard library
- Tkinter
- python-docx, MIT License

No evidence-processing, parsing, acquisition, extraction, or analysis dependency is included.

## Recommended commit message

```text
Add Playbooks coach drills and missed review
```

## Recommended commit description

```text
Adds Coach Mode drill controls for question count and order, missed-question tracking, Review Missed mode, a drill summary popup, and Copy Missed/Summary support while preserving topic/difficulty filtering, Scenario Coach shortcuts, and Playbooks as a non-case reference and refresher tool.
```

## Coach difficulty levels

Coach Mode now supports three examiner experience levels for each major realm:

- **Novice** - baseline safety, vocabulary, and overclaim prevention.
- **Experienced** - context-building, source comparison, and documentation judgment.
- **Expert** - ambiguity handling, conflicting artifacts, source limitations, and stronger corroboration questions.

The intent is to let a new examiner start safely while giving a more practiced examiner deeper scenario questions without turning Playbooks into a certification exam or case-tracking tool.


## v0.9.0 question-pack organization

v0.9.0 reorganizes Coach Mode questions into modular question packs. Coach questions now live in the `coach_questions/` folder instead of being embedded directly in `playbook_data.py`. This keeps the main playbook content easier to maintain and leaves room for fast expansion into larger topic packs, agency-specific packs, lightning rounds, missed-question review, and future drill modes.

Question pack foundation:

```text
coach_questions/
  __init__.py
  browser_file_activity.py
  external_media.py
  integrity_hashing.py
  memory_ram.py
  mobile.py
  timestamps.py
  use_access_context.py
  validation_tool_confidence.py
  windows_file_activity.py
```

Each pack exposes a `QUESTIONS` list. The package loader combines them into `COACH_QUESTIONS` for the existing Coach Mode interface.