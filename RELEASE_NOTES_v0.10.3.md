# ByteCase Playbooks v0.10.3 Release Notes

## Chained Coaching Sprint

v0.10.3 expands the Workbench > Coaching lane from single-answer prompts into chained mentoring paths.

## Highlights

- Adds multi-question Coaching paths.
- Records each response without revealing the best answer during the path.
- Adds final review with selected response, best response, explanation, mentor note, score, and bigger-picture debrief.
- Moves Coaching path content into `coach_questions/coaching_paths.py` so it can grow like the Coach question packs.
- Expands built-in Coaching paths from 3 single prompts to 8 chained paths with 25 total mentoring questions.
- Varies answer position and option length so the safest response is not visually obvious.

## Built-in Coaching paths

- Live BitLocker laptop: order of volatility
- Command history and actor attribution
- Downloaded file: possession, viewing, and knowledge
- USB connection and possible file movement
- Mobile messages and actor context
- Memory review and suspicious process mindset
- Cloud sync: local artifact or cloud activity?
- Conflicting timestamps and parser differences

## Boundary

Coaching paths are readiness prompts. They do not produce investigative findings, replace agency policy, validate tools, or determine legal conclusions.
