# ByteCase Playbooks

**Guided Examiner Reference and Learning Companion**  
Part of the ByteCase toolset by Forensics Byte.  
https://byte-case.com

## Version

v0.6.0

## Purpose

ByteCase Playbooks is a click-based reference and learning tool for digital evidence examiners. It is designed for real-time reference during an investigation or as a refresher/training companion during downtime.

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

## v0.6.0 updates

v0.6.0 adds an artifact-area navigator, question-driven guidance, and stronger use/access attribution guardrails.

Changes include:

- Added **Artifact Areas** tab
- Added artifact guidance for Windows execution, file access, USB devices, browser activity, memory context, and mobile activity
- Added **What are you trying to understand?** helper
- Added question guidance for device control, file access, command execution, USB connection, and browser/download activity
- Added **Use / Access Context** guardrail guidance
- Added reminders that device artifacts, commands, logins, and file activity do not automatically identify the human actor
- Added search coverage for artifact areas and investigative questions
- Added glossary entries for Device-use context and Actor vs. artifact

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

## Dependencies

Runtime:

- Python standard library
- Tkinter
- python-docx, MIT License

No evidence-processing, parsing, acquisition, extraction, or analysis dependency is included.

## Recommended commit message

```text
Add Playbooks artifact navigator and use-context guardrails
```

## Recommended commit description

```text
Adds an Artifact Areas tab, question-driven artifact guidance, and use/access context guardrails to ByteCase Playbooks. The new guidance helps examiners understand common artifact areas, what questions those artifacts may support, what tools may apply, and what not to overclaim, including reminders that device activity, commands, logins, and file access do not automatically identify the human actor without supporting context.