# ByteCase Playbooks

**Guided Examiner Reference and Learning Companion**  
Part of the ByteCase toolset by Forensics Byte.  
https://byte-case.com

## Version

v0.1.0

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

## What ByteCase Playbooks is not

ByteCase Playbooks does not perform acquisition, extraction, parsing, analysis, or reporting conclusions. It does not replace legal authority, agency policy, formal training, tool validation, or examiner judgment.

It is not the same as ByteCase Workflow.

- **ByteCase Playbooks explains the work.**
- **ByteCase Workflow tracks the work.**

## v0.1.0 included playbooks

This first sprint includes four starter playbooks:

1. Live Computer Acquisition / RAM Capture
2. Dead-Box Computer Imaging
3. Mobile Device Extraction Refresher
4. Memory / RAM Analysis Refresher

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
- Optional examiner notes

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
  <case_number>\
    playbooks\
      sessions\
        <timestamp>_<playbook_name>\
          bytecase_playbook_session_<playbook>_<timestamp>.json
          bytecase_playbook_session_<playbook>_<timestamp>.txt
          bytecase_playbook_session_<playbook>_<timestamp>.docx
```

## Dependencies

Runtime:

- Python standard library
- Tkinter
- python-docx, MIT License

No evidence-processing, parsing, acquisition, extraction, or analysis dependency is included.

## Recommended commit message

```text
Create ByteCase Playbooks v0.1.0
```

## Recommended commit description

```text
Adds the initial ByteCase Playbooks guided examiner reference tool with click-based playbook selection, Field Reference and Learning/Refresher modes, step cards, explanation panels, session notes, save/load support, and JSON/TXT/DOCX exports for starter live acquisition, dead-box imaging, mobile extraction, and memory analysis playbooks.
```
