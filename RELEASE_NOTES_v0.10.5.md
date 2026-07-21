# ByteCase Playbooks v0.10.5 Release Notes

## Nested Scroll Fix

This sprint fixes mouse-wheel behavior for inner scrollable widgets inside scrollable pages.

Previously, page-level scrolling could override multi-line text boxes, list boxes, and tree views. Users could see an inner scrollbar but had to drag it manually because the mouse wheel moved the outer page instead.

## Changes

- Added a shared cross-platform wheel-unit helper.
- Added inner-widget mouse-wheel handling for Text, Listbox, and Treeview widgets.
- Inner widgets now consume wheel events while they can scroll.
- At the top or bottom edge, wheel events can pass back to the outer page so scrolling still feels natural.
- Updated the outer ScrollableFrame handler to use the shared wheel helper.
- Preserved Windows/macOS `<MouseWheel>` support and Linux/X11 `<Button-4>` / `<Button-5>` support.

## Scope

This is a usability fix only. It does not change Playbooks content, session scope, exports, question packs, or case-output behavior.
