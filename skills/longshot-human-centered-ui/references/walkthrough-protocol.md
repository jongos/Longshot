# Walkthrough Protocol

Use for interactive task testing. Keep a narrow review small: one journey can use a short ledger instead of a formal report. No new browser framework, service, account or paid model is required.

## Set Up a Fair First Encounter

Start with a neutral goal, necessary user/domain context, authorized data/actions, starting state and observable completion condition. Ask only for missing facts that change the test or boundary. A task such as “compare suitable plans and determine the total cost” should not reveal which navigation item to select.

Separate sources before starting: user-visible information, task facts, known implementation details and supplied solution hints. Do not discard necessary domain knowledge to manufacture a novice failure. If the reviewer already knows the solution, mark the first encounter as informed; a new browser session clears app state, not model knowledge. Do not claim a clean first encounter merely because cookies were reset.

Choose conditions tied to the task: first visit, returning draft, comparing choices, keyboard use, viewport/zoom, interruption or missing information. Do not mechanically run every combination. Device or input constraints are test conditions, not proxies for a disability or demographic group. Only claim assistive-technology behavior when that technology was actually exercised.

## Pass One: Discover and Attempt

Use rendered information in the selected modality. A tool locator can target a visibly discovered control; inspecting hidden labels, source, network responses or backend state to find the answer crosses into diagnosis. If the host only exposes an accessibility tree, name that evidence channel and limit visual-discovery conclusions. Do not use inaccessible information to rescue the first-pass score.

For a consequential or ambiguous decision, record one short action annotation before acting:

> Cue: “Continue.” Expected outcome: another review step, based on the nearby “Review before submission” text. Observed outcome: the application is submitted immediately.

This is an agent expectation, not a participant quotation. Do not reconstruct an unrecorded prediction after seeing the outcome. A mismatch without a supported expectation is a concern to investigate, not a confirmed defect.

Record meaningful backtracking, ordinary help and boundaries encountered. Set a task-appropriate exploration budget; distinguish stopping because the budget or tool failed from evidence that the product blocks completion. Do not invent universal time or click thresholds. Stop immediately before an unauthorized action, even if it would finish the task.

## Pass Two: Diagnose and Countercheck

Preserve the first-pass observations before consulting authorized source, DOM, service or designer evidence. Identify what new information enabled progress. Reproduce consequential issues from a recorded state, compare a working route or test a competing explanation. Use bounded attempts; do not retry uncertain consequential submissions.

Verify meaningful terminal states where authorized. A success toast can coexist with missing persistence; a pending export can be correct while completion remains unverified. Check relevant aftermath such as locating the result, returning later, refreshing, correction, cancellation and resumption. Identify simulated service behavior explicitly.

## Keep a Journey and State Map

Use only applicable rows; unknown is preferable to invented coverage.

| Goal / State | Condition and Starting State | Outcome | Assistance | Evidence / Limit |
| --- | --- | --- | --- | --- |
| Primary task | Record actual account role and fixture | Completed / blocked / uncertain / untested | Unassisted / backtracking / ordinary UI help / privileged information; combine as needed | Action and artifact references; why stopped |
| Return or recovery | Record the interruption actually exercised | Same outcome vocabulary | Record assistance separately | State preserved or lost; persistence not checked if unavailable |

Record app/build version when available, route, viewport, zoom, input method and evidence channel. Do not treat an unknown version as a reason to stop a useful review. Keep cause attribution (product/tool/environment/unknown) distinct from outcome and finding classification. No finding is required for a correctly working row.

## Make Findings Replayable

For each consequential finding, retain: sanitized starting state and inputs → numbered actions → expected and observed result → screenshot/trace locators → terminal verification → bounded reproduction/countercheck → acceptance test. Prefer existing host screenshots and traces. If unavailable, report that limit and provide steps; never fabricate an artifact or expose credentials/session tokens. Record fixture reset instructions only when safe and relevant, without executing an unauthorized reset.

## Challenge the Recommendation

Choose the smallest change addressing the observed obstacle. State useful behavior to preserve, a tradeoff and a falsifiable acceptance test. Compare a plausible alternative when the choice is consequential; do not produce alternatives just to fill space. A required safeguard is not needless friction merely because it adds a step. A proposed simplification must be assessed separately from whether the existing implementation meets its contract.

When a later fix-and-retest is authorized, repeat comparable task conditions and check an adjacent preserved behavior. Report whether the observed obstacle disappeared and whether a regression appeared. This supports a finding about the tested behavior, not a claim that humans became faster or more satisfied.
