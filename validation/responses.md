# Independent synthetic responses

Evidence boundary for A–M: these responses use only the authored packets in `validation/cases.md`. No live walkthrough, application interaction, screenshot inspection, service call, or human study occurred. “Confirmed” below means supported by the fictional fixture trace, not confirmed in a real product. Environment version, viewport and zoom are unspecified except where supplied. Findings are recommendations only.

## A — Applies: narrow form-completion review

The valid-address path works; rejected input has no visible recovery guidance.

**A1 — Explain rejected input so the draft can be saved.** Task/state: save a contact with `test@`. Evidence: supplied A trace and fixture log show Save leaves focus on Save and retains values, silently rejects validation, and creates no draft. Expected/observed: error identification and recovery conventions call for actionable feedback; none appears. Human consequence: a person may believe Save did nothing or may repeat it without knowing how to recover (inference; frequency unknown). Classification: confirmed defect in fixture feedback. Severity: medium, recoverable friction with a working valid-input path. Confidence: high for silent rejection, based on trace plus log. Recommendation: identify the address error, associate it with the field, expose it accessibly and preserve entered values. Acceptance: given `test@`, when Save is pressed, then a visible field-associated explanation appears, input is retained and success is not shown; after correction to `test@example.invalid`, saving produces the existing confirmation and a persisted draft. Human follow-up: “Save this contact draft”; observe whether participants recover from an invalid address without guidance.

## B — Applies: narrow journey review

The supplied primary journey loses work.

**B1 — Preserve the draft through reference consultation.** Task/state: write a note and consult in-app Reference. Evidence: B trace enters `Draft alpha`, opens Reference, returns, and finds empty input with no save, warning or restore. Expected/observed: the supplied primary journey requires returning to continue the draft; content is lost. Human consequence: re-entry or abandonment is plausible (inference; frequency unknown). Classification: confirmed defect in fixture. Severity: high, lost work on a primary path. Confidence: high from explicit trace and absence of recovery. Recommendation: preserve draft state across reference navigation and restore it on return. Acceptance: given an unsaved `Draft alpha`, when Reference is opened and Back to draft selected, then the exact text remains available for continued editing; repeat the round trip after another edit and verify that edit remains. Human follow-up: “Prepare a note, consult the reference, then continue it.”

## C — Applies: action-clarity review

The fixture exposes an unexplained destructive action.

**C1 — Make deletion explicit and prevent accidental loss.** Task/state: decide what the sole `Go` control does below an editable item. Evidence: C trace says visible and accessible labels are `Go`; activation deletes immediately without explanation, confirmation or undo. Expected/observed: action-label and error-prevention conventions call for identifying a destructive outcome before activation; `Go` does not identify deletion. Human consequence: unintended deletion is plausible; no participant misunderstanding is established. Classification: usability concern, with deletion behavior confirmed in fixture. Severity: high, item loss without recovery; value and wider reach unknown. Confidence: high for label/outcome mismatch, medium for predicted human impact. Recommendation: label the action Delete item and provide a suitable prevention or recovery mechanism, such as a cancellable confirmation when recovery is unavailable. Acceptance: given an existing item, the visible and accessible action names identify deletion; activating the proposed confirmation flow preserves the item until explicit confirmation, cancellation preserves it, and confirmation deletes only that item. Human follow-up: before activation ask, “What do you expect this action to do?”

## D — Applies: feedback review

The fixture reports completion despite a simulated failed submission.

**D1 — Align completion feedback with persisted outcome.** Task/state: submit a record during a simulated 503. Evidence: D shows `Completed` before failure, no persisted record, and unchanged success feedback; retry creates a new request. Expected/observed: completion should represent verified completion under the submission contract; the UI reports an outcome contradicted by fixture service state. Human consequence: a person may leave believing their record exists or retry an uncertain operation (inference; no actual duplicate or charge established). Classification: confirmed fixture defect. Severity: high, failed primary task concealed as success; consequential real-world stakes are unspecified. Confidence: high for the simulated mismatch, none for live reliability. Recommendation: show pending until persistence is verified, retain input on failure, show the failure and offer safe recovery; define uncertain-outcome handling before enabling repeated retry. Acceptance: given a simulated 503 with no persisted record, when Submit runs, then no completed status appears, entered work remains and a recoverable error is shown; on a separately simulated successful persistence, show completion only after acknowledgment. For a timeout with unknown persistence, show uncertainty and reconcile outcome before allowing a duplicate operation. Human follow-up: “Submit this record and tell us what you believe happened.”

## E — Applies: journey simplification review

Removing the mandatory avatar gate is justified by the supplied requirement, rather than click count alone.

**E1 — Allow saving without optional decoration.** Task/state: save a private draft without an avatar. Evidence: E trace blocks Save until one of three avatars is selected, without skip; brief calls avatars optional and nonfunctional. Expected/observed: optional decoration should not gate the requested save; it is mandatory in fixture. Human consequence: unnecessary decision effort or abandonment is possible; no timed benefit is measured. Classification: confirmed defect against supplied brief. Severity: medium, forced recoverable friction with a selection workaround. Confidence: high from explicit requirement and trace. Recommendation: permit Save without selection and retain optional avatar customization. Acceptance: given no chosen avatar and otherwise valid draft, when Save is activated, then the draft saves; choosing an avatar remains possible and also permits saving. Human follow-up: “Save a private draft”; observe choice needs without directing avatar use.

## F — Applies: keyboard completion review

The supplied keyboard path cannot reach the modal's primary action.

**F1 — Make the modal operable and return focus meaningfully.** Task/state: complete or leave a modal using keyboard after pointer opening. Evidence: F says Tab visits background controls but never Confirm, Escape does nothing, and pointer close moves focus to page top. Expected/observed: keyboard operation and modal focus conventions call for reachable dialog actions and contextual focus restoration; Confirm is unreachable and focus escapes the dialog. Human consequence: keyboard-dependent users may be blocked or lose context (inference; no assistive-technology session). Classification: confirmed keyboard defect in fixture; Escape and return behavior are supporting recovery concerns, not separately proven WCAG failures. Severity: high, blocked task for the tested input method. Confidence: high for supplied keyboard result. Recommendation: move focus into the modal, support its controls by keyboard, constrain background interaction while modal, provide an appropriate keyboard dismissal and restore focus to the opener. Acceptance: given focus on the opener, when the dialog opens, then focus enters it, Tab and Shift+Tab reach its controls without moving behind it, Confirm activates by keyboard, cancellation leaves state intact, and dismissal returns focus to the opener. Test Escape when dismissal is allowed. Human follow-up: test the task with keyboard users and applicable assistive technology. No conformance certification is inferred.

## G — Applies: usability review limited to supplied evidence

The disconnected primary flow is blocked and loses work on refresh. The supplied aesthetic description is favorable but was not independently inspected and does not establish task success.

**G1 — Recover from disconnection without losing form content.** Task/state: finish a completed form in a simulated disconnected state. Evidence: G trace shows an indefinite spinner, no retry/cancel/draft route, and loss after refresh. Expected/observed: completion feedback and recovery conventions require a truthful state and a way to retain work; neither is present. Human consequence: wasted entry effort and uncertainty are plausible (inference; duration and incidence unmeasured). Classification: confirmed defect in fixture recovery. Severity: high, blocked main task and lost work. Confidence: high for supplied failure path, no evidence about connected success. Recommendation: preserve work durably, expose offline/failure state and provide safe retry or return to editing. Acceptance: given a filled form and simulated disconnection, when Finish runs, then the interface exposes the disconnected or failed state with retained input and recovery controls rather than an endless spinner; after refresh the draft can be restored; after reconnection a retry persists it once and confirms completion. Human follow-up: “Complete this form”; introduce an authorized connection interruption and observe recovery. Preserve the described visual coherence while addressing recovery.

## H — Applies: small-flow review

No findings are supported by this packet. The supplied trace supports save/reopen persistence, invalid-title recovery, keyboard reachability and visible focus, reversible deletion, and no clipping at the supplied narrow layout and 200% zoom. The supplied body-text measurement is 7:1; it is not a measurement of every UI component. Preserve these working behaviors.

This is a limited trace review, not a live usability or accessibility pass. Exact viewport dimensions, wider states, assistive technology and human discoverability remain untested. Cost, AI and dragging checks are inapplicable to this flow. If human validation is needed, use “Create a draft, leave it, and continue it later” and observe completion without naming controls. No repair plan is warranted.

## I — Does not activate a review

Use **Save draft** in place of **Savve draft**. No application access was provided, so I have not applied the edit. Supply the editable file or target to make this exact replacement.

## J — Does not activate a review

Progressive disclosure shows essential choices first and reveals advanced or less frequently needed options when relevant.

## K — Applies, but review is blocked by missing evidence and access scope

No usability findings can be made yet. Please provide a sanitized task trace or screenshots, or an authorized test environment with synthetic records and the primary task to review. A production URL alone would not authorize viewing private customer records or triggering paid actions. Those steps remain untested; available authorized surfaces can be reviewed independently. No login, record access or paid submission was attempted.

## L — Applies: validation-evidence review

This preview supports only the existence of simulated suggestion presentation, editing and dismissal controls. It proves neither AI service reliability nor user trust. The `Suggestion` label and controls are useful elements to retain; they do not establish human understanding or successful use.

**L1 — Keep validation claims within the preview's evidence.** Task/state: assess whether the local preview validates the AI feature. Evidence: L supplies a canned answer after a timer and explicitly no AI service call; there are no participant observations. Expected/observed: reliability requires service evidence and trust requires appropriately designed human research; this fixture supplies neither. Human consequence: overclaiming may lead to decisions based on untested quality or reliability (inference). Classification: usability concern about the proposed validation claim, not a confirmed UI defect or evidence that the UI hides its simulated nature. Severity: medium, an evidence gap with unknown downstream stakes. Confidence: high that the claimed conclusions are unsupported. Recommendation: label evaluation results as simulated, verify the real service separately under authorized conditions, and investigate users' interpretation and reliance with actual participants. Acceptance: the preview report explicitly identifies its canned response and makes no live-reliability or user-trust claim; subsequent authorized service tests record actual requests, responses and failures separately; human conclusions link to actual participant observations. No arbitrary reliability target or study result is invented. Human follow-up: “Use this suggestion to prepare your draft”; ask “What would you check before using it?” and observe correction/dismissal behavior.

## M — Applies: narrow confirmation review

No defect is supported. The confirmation fulfills the explicit requirement to prevent mistaken irreversible public submissions, and the supplied trace supports keyboard operation and cancellation. Retain it; one fewer step would remove a stated safeguard. No human difficulty has been observed, and no live public submission was attempted. If further validation is useful, ask participants to prepare a submission and decide whether to proceed or return to editing, then observe whether they understand what will become public and irreversible. Wider usability and actual prevention effectiveness remain untested.
