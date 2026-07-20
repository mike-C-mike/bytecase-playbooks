# ByteCase Playbooks

**Guided Examiner Reference and Learning Companion**  
Part of the ByteCase toolset by Forensics Byte.  
https://byte-case.com

## Version

v0.4.0

## Purpose

ByteCase Playbooks is a click-based reference and learning tool for digital evidence examiners. It is designed for real-time reference during an investigation or as a refresher/training companion during downtime.

It helps answer questions such as:

- What kind of workflow am I dealing with?
- Why does this step matter?
- Why does this step come before another step?
- What should I document?
- What artifact areas may commonly matter?
- What tools may be used for this area?
- What should I avoid overclaiming?

## Guide Me decision helper

The **Guide Me** tab is a shortcut for new examiners or occasional examiners who know the situation but are not sure which playbook to open. It recommends a playbook based on common scenarios such as powered-on computer, dead-box imaging, mobile extraction, memory analysis, Windows artifact review, or external media hash/copy work.

The recommendation screen explains why the path fits, what questions should be asked before continuing, and what first steps the playbook will emphasize.

## What ByteCase Playbooks is not

ByteCase Playbooks does not perform acquisition, extraction, parsing, analysis, or reporting conclusions. It does not replace legal authority, agency policy, formal training, tool validation, or examiner judgment.

It is not the same as ByteCase Workflow.

- **ByteCase Playbooks explains the work.**
- **ByteCase Workflow tracks the work.**

## v0.4.0 included playbooks

This release includes six built-in playbooks:

1. Live Computer Acquisition / RAM Capture
2. Dead-Box Computer Imaging
3. Mobile Device Extraction Refresher
4. Memory / RAM Analysis Refresher
5. Windows Artifact Review Refresher
6. External Media Hash / Copy Refresher

## v0.4.0 updates

v0.4.0 fixes Python 3.7/3.9 compatibility issues, hardens mouse-wheel scrolling around Tkinter combobox popdowns, and simplifies session saving so Playbooks does not behave like a case-notes tool.

Changes include:

- Replaced Python 3.10+ type annotations with older-compatible typing
- Fixed a Tkinter mouse-wheel callback error caused by combobox popup widgets
- Removed case number, examiner, and overall case/session notes fields
- Session save now records only the current playbook, mode, current step, reviewed steps, and step reference notes
- Session exports now save under `ByteCase\playbooks\sessions\` instead of a case folder
- Preserved the Reference tab, glossary search, Windows artifact review playbook, and external media hash/copy playbook

## Main modes

### Field Reference

A concise real-time reference mode for when the examiner needs the immediate order of thinking, cautions, and documentation reminders.

### Learning / Refresher

A deeper mode for training, downtime review, or examiners who do not perform a task often.

## Step card design

Each playbook step includes:

- Field focus
- Learning detail
- Why this matters
- Possible tools
- Common artifacts / outputs
- Cautions
- What to document
- Optional step reference notes

Each step has quick explanation buttons:

- Why?
- Tools
- Artifacts
- Cautions
- Document

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

## Dependencies

Runtime:

- Python standard library
- Tkinter
- python-docx, MIT License

No evidence-processing, parsing, acquisition, extraction, or analysis dependency is included.

## Recommended commit message

```text
Fix Playbooks session scope and Python compatibility
```

## Recommended commit description

```text
Fixes Python compatibility and Tkinter mouse-wheel handling, then simplifies Playbooks session saving so it records only the current playbook state instead of case details or case notes. Session output now saves under ByteCase/playbooks/sessions, preserving Playbooks as a reference/refresher tool rather than a case workflow tracker.
```


## v0.4.0

- Reordered the Playbook step screen so the reading/explanation section appears before user notes.
- Renamed the explanation panel to **Read this first**.
- Renamed step notes to **Your notes for this step** and clarified that these are optional session/reference notes, not case notes.


## v0.4.0 highlights

- Added step context text showing where the selected step sits in the playbook.
- Added Pop Out Reading for real-time reference use.
- Added Deep Dive so users can open the full learning layer without changing modes.
- Added Copy Summary and Copy Document List actions for quick reference/session notes.
- Expanded the built-in glossary with corroboration, limitations, volatile data, and forensic image entries.