# ByteCase Playbooks

**Guided Examiner Reference and Readiness Companion**  
Part of the ByteCase toolset by Forensics Byte.  
https://byte-case.com

## Version

v0.9.4

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

## v0.9.4 updates

v0.9.4 is a navigation simplification sprint. It keeps the v0.9.3 grouping but tightens the top-level menu further.

Top-level navigation is now organized as:

- **Home**
- **Reference**
- **Practice**
- **Library**

### Reference

Reference contains the active workbench areas:

- Guide
- Playbook
- Artifacts
- Scenarios

### Practice

Practice contains the readiness and training areas:

- Drills
- Packs

### Library

Library contains supporting areas that should not compete with the main workflow:

- Save / Export
- Search
- Settings

Session saving/export is no longer a top-level lane. It now lives under Library as **Save / Export**, which keeps Playbooks focused around three primary user paths: reference, practice, and library/support.

Scope remains unchanged: Playbooks is a non-case reference and readiness tool. It does not create case notes, track case progress, perform forensic analysis, or produce investigative findings.

## Current built-in playbooks

This release includes six built-in playbooks:

1. Live Computer Acquisition / RAM Capture
2. Dead-Box Computer Imaging
3. Mobile Device Extraction Refresher
4. Memory / RAM Analysis Refresher
5. Windows Artifact Review Refresher
6. External Media Hash / Copy Refresher

## Major capability areas

### Field Reference

A concise real-time reference mode for when the examiner needs the immediate order of thinking, cautions, and documentation reminders.

### Learning / Refresher

A deeper mode for training, downtime review, or examiners who do not perform a task often.

### Scenario Coach

Short scenario guidance for careful interpretation. Scenario Coach focuses on what an artifact may support, what it does not prove, what supporting context may help, and what to document.

### Coach Mode

Question-and-answer practice for examiner judgment. Coach Mode supports topic filtering, difficulty levels, drill count, shuffle/in-order mode, answer explanations, missed-question review, and summary/copy support.

### Question Packs

Downloadable/importable Coach Mode question packs can be validated, imported, enabled, disabled, and selected from Coach Mode. Imported packs are stored locally under:

```text
ByteCase\playbooks\question_packs\
```

Built-in ByteCase questions remain separate from imported/custom question packs.

### Reference Library

The Reference Library searches across glossary terms, playbooks, artifact areas, scenario cards, investigative questions, and Coach Mode content.

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
- Tkinter / Tcl-Tk
- python-docx for DOCX export

Packaging:

- PyInstaller, optional for building a Windows EXE

See `DEPENDENCIES.md` for license notes.

## Suggested next work

After this navigation cleanup, the next polish direction is to keep simplifying the Start page and reduce visual clutter inside each lane before adding another major capability.