# ByteCase Playbooks

**Guided Examiner Reference and Learning Companion**  
Part of the ByteCase toolset by Forensics Byte.  
https://byte-case.com

## Version

v0.7.0

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

## v0.7.0 updates

v0.7.0 adds a **Scenario Coach** layer for common interpretation questions where newer or occasional examiners need help separating technical artifacts from stronger human-action claims.

Changes include:

- Added **Scenario Coach** tab
- Added scenario cards for command/tool activity, downloads, USB/external media, and mobile message/app actor context
- Added scenario guidance for how to think through the issue, what supporting context may help, and what not to overclaim
- Added related playbook shortcuts from scenario cards
- Added related reference search shortcuts from scenario cards
- Expanded reference search to include scenario cards
- Preserved Playbooks as a reference/refresher tool, not a case notes or case workflow module

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
Add Playbooks scenario coach guidance
```

## Recommended commit description

```text
Adds a Scenario Coach tab with common interpretation scenarios for command/tool activity, downloads, USB/external media, and mobile message/app actor context. Scenario cards explain how to think through the issue, what supporting context may help, what not to overclaim, and which related playbook or reference terms may help.
```