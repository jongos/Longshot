# Observed demonstration plan — issue #2

Planning only. Major tests and fixture execution remain paused. No fixture was implemented or run for this document.

## Bounded demonstration

Use a disposable draft editor with a required reference view, cancellation, return and a visible saved-record view. Define the contract before execution: unfinished input survives the reference round trip; cancellation leaves the draft intact. Provide two visually equivalent resettable variants: one violates retention and one meets the contract. Use ordinary synthetic text and no external service.

Tester prompt: “Prepare a draft using the reference, then return and finish it. Use only this disposable environment. Report the outcome, supporting evidence and any obstacles.” Do not reveal variant labels, defect locations, expected finding counts or source. Record misses and zero-finding reports. Author familiarity must be disclosed; use a fresh independent tester context when available. Keep diagnosis separate.

Freeze fixture and skill revisions, task, starting data, input/viewport, action budget and terminal condition before the attempt. Reset variants independently; do not let a first variant teach the second without recording that exposure. This demonstration proves capture/replay on these cases, not comparative performance.

Capture numbered actions and actual before/action/after artifacts using existing host tools. Verify retained values on return and cancellation behavior; distinguish visible state from storage. Include the original unsuccessful attempt, assistance, diagnosis and any missing evidence. Sanitize before sharing. Produce readable findings and optional schema 1.0.0 JSON from the same evidence.

## Acceptance and stop conditions

A reviewer given only the bundle can locate the original observation, reconstruct starting state and actions, distinguish discovery from diagnosis, and assess each recommendation. Record replay failures and review effort. A working control may have no findings. No required finding quota, reconstructed screenshots or cherry-picked successful attempts.

Stop dependent work if reset is unreliable, evidence capture exposes private data, the terminal outcome cannot be verified, or execution exceeds approved scope/budget. Ask for authorization before fixture execution; approval of this plan alone does not run it.

## Optional later extensions

Separately evaluate automatic task selection and user-guided workflows. Do not mix task-selection quality with detection accuracy: compare detection on the same fixed tasks; assess automatic selection against a separately reviewed task-priority list. Add an unclear consequence and a costly-but-successful route only after the compact demonstration is reviewable.
