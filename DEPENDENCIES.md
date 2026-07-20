# ByteCase Playbooks Dependencies

## Runtime dependencies

| Dependency | Purpose | License posture |
|---|---|---|
| Python standard library | Core application logic, JSON, paths, timestamps | Python Software Foundation License |
| Tkinter / Tcl-Tk | Desktop GUI | Included with most Python Windows installs; Tcl/Tk is permissive-style open source |
| python-docx | Optional DOCX export | MIT License |

## Build dependencies

None in v0.1.0.

PyInstaller can be added later for release packaging. PyInstaller is GPL 2.0 with a commercial-use exception. That has been acceptable for the other ByteCase tools when documented.

## Dependency policy

ByteCase Playbooks should avoid unnecessary dependencies. Prefer Python standard library, MIT, BSD, Apache-2.0, PSF, or similarly permissive licenses. Flag GPL, AGPL, noncommercial, unknown, or commercial-use-restricted dependencies before adding them.

## Evidence-processing boundary

ByteCase Playbooks does not include evidence parsing, acquisition, extraction, malware analysis, memory analysis automation, or forensic conclusions. It is a guided reference and learning companion.
