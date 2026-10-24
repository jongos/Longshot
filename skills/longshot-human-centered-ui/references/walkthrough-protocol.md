# Walkthrough Protocol

Use for interactive task testing. Keep a narrow review small: one journey can use a short ledger instead of a formal report. No new browser framework, service, account or paid model is required.

## Set Up a Fair First Encounter

In automatic mode, identify the product's apparent purpose from authorized visible context and select a few journeys by user importance, consequence of failure and unresolved uncertainty. Consider the core job, a consequential choice, returning to unfinished work and recovery from a plausible mistake; select only relevant paths. Use supplied or authorized support reports, failed searches and prior research when available; do not fetch private analytics by default. Mark each selected task as user-defined, evidence-derived or inferred. Unknown usage frequency stays unknown.

In guided mode, carry the user's roles, workflows and acceptance criteria into the journey map. Partial guidance is enough: a role without workflows allows task inference within that role; workflows without roles can use the authorized account's known capabilities. Preserve priorities and exclusions. If a specified workflow conflicts with the visible interface, record the mismatch and test within scope rather than silently substituting another task. Necessary missing credentials or risky actions block only dependent steps.

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

### Examine Workflow Friction

Use these four lenses where the task calls for them, in either automatic or guided mode. They are prompts for observation, not four mandatory audits or finding quotas. Preserve the first attempt before deliberately searching for alternatives.

- **Choice visibility:** check whether a dominant editor, preview or default path obscures useful alternatives such as selecting existing work. Record the actual viewport, visible cues and route needed to find the choice. Compare relevant empty/populated states when authorized. An option below the fold is not inherently a defect; explain why its placement interferes with this goal and check whether a clear shortcut already exists.
- **Action scope:** check whether labels and nearby context explain what an action affects: this item, a shared template, the current project or an external result. Compare similarly named controls and their actual outcomes. A label such as “Photos” may imply browsing while opening creation; establish the expectation from context, not the word alone. Do not trigger destructive or paid actions merely to discover their scope; use authorized synthetic records or report the untested outcome. Recommend clearer scope without weakening confirmation or replacement safeguards.
- **Context continuity:** check whether exploring or comparing alternatives requires applying one, losing the prior selection, or backtracking through unrelated steps. Look for workflows that assume a prerequisite the user has not created. Record what is preserved, what changes and whether a usable return/cancel path exists. Distinguish a necessary dependency from an unexplained or unnecessary gate. Preserve meaningful selection, draft and ownership context; do not remove a justified prerequisite just to shorten the flow.
- **Translation burden:** check whether users must convert internal units, decode provider terms or reconcile shifting labels to complete the task. Show the exact terms/units and the decision they affect; establish whether they refer to the same object before calling them inconsistent. Preserve useful expert precision: pair familiar units or names with technical detail when appropriate rather than hiding it. Do not replace truthful service status with a simpler but misleading label.

For each supported concern, connect the observed cue or state to the task consequence, offer a bounded recommendation and an acceptance test. Capture working alternatives and safeguards. Unsupported human confusion or frequency remains an inference; functional success alone does not dismiss evidenced friction.

Before diagnosis, capture costly success where it matters: the available cue, the extra inference/search/backtracking/workaround that enabled progress, and any remaining uncertainty. Completion does not erase these observations. Do not treat every extra step as friction or impose artificial click limits. For example, finding an export option by searching unrelated menus supports a discoverability concern; it does not establish a human failure rate.

At consequential decisions, check whether the interface supplies the information needed to act: prerequisites, likely outcome, cost or commitment, reversibility, current state, completion evidence and where to resume. Use only applicable questions. Record the missing or conflicting information and why it affects this task. A cancellation control that omits when access ends can warrant a concern even if cancellation works; do not invent feelings or requirements.

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

Evaluate detection and remedy separately. Explain the causal link between the proposed change and the evidenced obstacle, proportionate effort/scope, useful behavior to retain and an observable result that would disprove the benefit. If competing causes imply different remedies, recommend the smallest authorized diagnostic check that distinguishes them. Compare alternatives only when the choice matters. A correct finding does not make every suggested fix correct.

Choose the smallest change addressing the observed obstacle. State useful behavior to preserve, a tradeoff and a falsifiable acceptance test. Compare a plausible alternative when the choice is consequential; do not produce alternatives just to fill space. A required safeguard is not needless friction merely because it adds a step. A proposed simplification must be assessed separately from whether the existing implementation meets its contract.

When a later fix-and-retest is authorized, repeat comparable task conditions and check an adjacent preserved behavior. Report whether the observed obstacle disappeared and whether a regression appeared. This supports a finding about the tested behavior, not a claim that humans became faster or more satisfied.

## Learn From Reviewed Findings

When prior adjudications are supplied or saving feedback is authorized, append the finding ID, reviewer/source, disposition, reason and evidence: reproduced/accepted, valid but tolerated, expectation rejected, environment-caused or unresolved. Keep this judgment separate from retest status. Rejection of a remedy does not invalidate the obstacle, and acceptance is not proof a fix helped. Preserve disagreements and original observations. Use reviewed evidence to prioritize later tasks; do not silently modify the skill, create persistent profiles, upload reports or overwrite history. In JSON 1.0.0, place concise adjudication context in comparison `reason` or `limitations` rather than inventing new required fields.
