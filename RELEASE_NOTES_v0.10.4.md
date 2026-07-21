# ByteCase Playbooks v0.10.4 Release Notes

## Mouse-wheel scrolling fix

This sprint fixes mouse-wheel scrolling across scrollable pages in ByteCase Playbooks.

Earlier builds registered each scrollable page using Tkinter's process-wide wheel binding without preserving earlier bindings. As more pages were created, the most recently created page could replace the binding used by earlier pages, leaving users able to drag the scrollbar manually but unable to scroll with the mouse wheel on many screens.

## Changes

- Updated `ScrollableFrame` to register mouse-wheel bindings additively.
- Added support for Windows/macOS `<MouseWheel>` events.
- Added support for Linux/X11 `<Button-4>` and `<Button-5>` wheel events.
- Added defensive pointer checks so only the scrollable frame under the mouse responds.
- Preserved the v0.10.x navigation model and Coaching/Artifacts functionality.

## Scope

No new dependencies were added.

Playbooks remains a reference and readiness tool. It does not track case progress, write case notes, perform forensic analysis, or produce investigative findings.
