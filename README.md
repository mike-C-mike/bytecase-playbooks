# ByteCase Playbooks

**Guided Examiner Reference and Readiness Companion**  
Part of the ByteCase toolset by Forensics Byte.  
https://byte-case.com

## Version

v0.10.4

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

## v0.10.2 updates

v0.10.1 is a navigation and workbench focus sprint.

### Quick navigation removed

The persistent quick navigation bar from v0.10.0 was removed because it repeated the same navigation already available in the tab model.

The top-level navigation is now intentionally simpler:

- **Home**
- **Workbench**
- **Library**

### Scenarios renamed to Coaching

The former **Scenarios** subtab is now **Coaching**.

Coaching is designed to feel like a mentoring examiner asking judgment-focused questions. It presents:

- a broad examiner-thinking prompt
- multiple-choice best-response options
- an explanation of why the selected response is safer or weaker
- follow-up questions a mentoring examiner might ask
- a bigger-picture takeaway

This is not a tabletop exercise. Tabletop exercises remain parked as a future separate module candidate.

### Artifact section reworked

The Artifact section now starts with **What are you trying to understand?** instead of starting with an artifact list.

The user selects:

- a situation, such as a dead-box laptop exam or powered-on computer
- the examiner question they are trying to answer

The app then fills in:

- decision factors
- artifact areas that may apply
- where those artifacts may be found
- common tools or methods used to collect or examine them
- guardrails and documentation reminders

Tool names are examples of commonly used industry tools or methods. They are not endorsements, recommendations, or validation statements.

### New starter coaching prompts

v0.10.1 adds starter coaching prompts for:

- powered-on BitLocker laptop decisions
- command history and actor attribution
- order of volatility thinking

These are focused on examiner mindset rather than pure trivia.


## v0.10.2 updates

v0.10.2 expands and tightens the Artifact section. Each situation now has its own targeted question list instead of reusing generic questions across unrelated device types.

### Situation-specific artifact questions

The Question dropdown is now filtered by the selected Situation. For example, Mobile Device Review now focuses on mobile communications, app/account context, location/media, extraction limitations, and cloud/sync source issues. It no longer shows Windows-only questions such as USB connection review unless the selected situation is a computer or external-media workflow.

### Expanded artifact library

The built-in artifact areas now cover more connected examiner questions, including Windows execution, file access, logons/sessions, event logs, USB/external media, browser activity, cloud sync, remote access/automation, memory/RAM, BitLocker/live encryption context, file system metadata, and mobile extraction limitations.

Tool names remain examples of commonly used industry tools or methods. They are not endorsements, recommendations, validation statements, or a substitute for agency-approved tools and local validation.

## v0.10.3 updates

v0.10.3 expands the Coaching lane into chained mentoring paths.

### Chained Coaching

Coaching now asks a series of related questions instead of revealing the answer immediately after a single prompt. The user records each answer, moves through the path, and then clicks **Finish & Review** to see the full coaching review.

The final review shows:

- each question in the path
- the selected response
- the safer/best response
- why the response is safer or weaker
- mentor notes
- an overall path score
- a bigger-picture debrief

### Coaching content moved into question-pack structure

Coaching paths now live in:

```text
coach_questions/coaching_paths.py
```

This keeps mentoring scenario content out of the GUI and main playbook data file, leaving room for future expansion and possible downloadable coaching-path packs later.

### Answer choices improved

Coaching answer positions and option lengths are now varied so the best answer is not visually obvious. The intent is to test examiner judgment instead of pattern recognition.

### Built-in chained paths

Starter paths now include:

- Live BitLocker laptop: order of volatility
- Command history and actor attribution
- Downloaded file: possession, viewing, and knowledge
- USB connection and possible file movement
- Mobile messages and actor context
- Memory review and suspicious process mindset
- Cloud sync: local artifact or cloud activity?
- Conflicting timestamps and parser differences

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

## Parking lot

Still parked for later:

- ByteCase Workflow for case progress tracking
- ByteCase Tabletop / ByteCase Scenarios as a future separate scenario exercise module
- Question Pack Builder for authoring/exporting drill packs
- persistent drill history and spaced refresher mode
- release packaging for Playbooks


## v0.10.4 updates

v0.10.4 fixes mouse-wheel scrolling across the consolidated Playbooks navigation. Earlier builds could allow the last-created scrollable page to replace the global wheel binding for other pages. The ScrollableFrame now registers wheel handlers additively and supports Windows/macOS MouseWheel plus Linux Button-4/Button-5 events.