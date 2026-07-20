# ByteCase Playbooks

**Guided Examiner Reference and Learning Companion**  
Part of the ByteCase toolset by Forensics Byte.  
https://byte-case.com

## Version

v0.5.0

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
- What sample command or tool action might apply?
- What does this step not prove by itself?

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

## v0.5.0 updates

v0.5.0 adds command/example guidance and stronger overclaim guardrails.

Changes include:

- Added **Commands** button on the Playbook screen
- Added **Does Not Prove** button on the Playbook screen
- Added **Copy Commands** quick action
- Added command examples to RAM capture and Volatility-oriented memory-analysis steps
- Added command/example details to Learning / Refresher mode when available
- Added **Does Not Prove** reminders to relevant steps
- Included command examples and overclaim guardrails in TXT/DOCX session exports
- Added glossary entries for Command example and Does not prove
- Expanded search to include command examples and does-not-prove guardrails

## Command examples

Command examples are learning/reference prompts. They are not one-size-fits-all instructions.

Users must adapt examples to their own:

- Tool path
- Filename
- Image path
- Case scope
- Agency policy
- Training
- Validated local process
- Operating environment

For example, a Volatility command may appear as:

```text
vol.py -f memory.raw windows.pslist
```

The examiner must still confirm the correct tool installation, image filename, plugin availability, permissions, symbols, and output handling.

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
Add Playbooks command guidance and overclaim guardrails
```

## Recommended commit description

```text
Adds command/example guidance and does-not-prove guardrails to ByteCase Playbooks. Includes Commands, Does Not Prove, and Copy Commands actions, adds Volatility-oriented memory-analysis command examples, expands reference search and glossary coverage, and includes command guidance in TXT/DOCX session exports while preserving Playbooks as a non-case reference/refresher tool.
```
