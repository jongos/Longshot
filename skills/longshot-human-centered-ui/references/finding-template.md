# Report and finding template

Use only the detail the requested review needs. Empty sections are unnecessary.

For a narrow review, combine the finding fields into one short paragraph rather than repeating headings. Preserve their substance. Keep evidence gaps and unsupported validation claims in coverage limits, with the evidence needed to resolve them; they do not need a defect classification or severity unless a separate interface problem is supported.

## Opening

- Disposition: what can/cannot be concluded about the tested journey; mention blockers directly.
- Scope and coverage: intended users/goals, environment/version, authorized data/actions, paths and states attempted, viewport/input method where known.
- Execution and cause: completed, blocked or untested branches; distinguish product behavior from tool/environment limitations or unknown causes. A blocked review can coexist with correct product behavior.
- Assistance and first encounter: record backtracking, ordinary UI help and privileged information separately from outcome (including uncertain). Disclose prior solution knowledge; distinguish first-pass attempts from diagnostic completion.
- Evidence limits: live agent observations versus supplied traces/screenshots versus simulations; inaccessible or untested behavior; no human participant research unless actually supplied/performed.
- Most consequential findings, followed by working behavior worth preserving.

## Finding

**ID and outcome-focused title**

- **Task/state:** goal, preconditions, route and relevant input.
- **Evidence:** reproducible action sequence and actual result, with an artifact locator or screenshot caption when available. Identify supplied versus directly observed evidence and simulation.
- **Replay context:** sanitized inputs, application/build when known, starting state, viewport/zoom/input method, action and artifact references, terminal verification and safe reset instructions where relevant. Missing details remain explicit.
- **Expectation check, when recorded:** cue and predicted outcome captured before the action, then actual outcome. Identify its basis; do not backfill a prediction or present it as human testimony.
- **Validation and alternatives:** reproduction or countercheck actually performed, competing explanations, and remaining proposed checks. Identify the evidence channel; do not call an intended test executed.
- **Expected / observed:** state both; give the requirement, contract, convention or goal supporting the expectation.
- **Human consequence:** concrete potential impact; label inference and unknown frequency.
- **Classification:** confirmed defect, usability concern or aesthetic preference.
- **Severity:** critical / high / medium / low, with rationale. Use critical for credible severe loss, unintended charges or misleading consequential outcomes; high for blocked important tasks or lost work; medium for substantial recoverable friction; low for minor issues. Adjust for impact, reach and workarounds rather than using labels mechanically. Uncertainty does not erase possible severity.
- **Confidence:** high / medium / low, justified by reproducibility, coverage and competing explanations. Confidence is separate from severity.
- **Recommendation:** smallest change addressing the evidenced obstacle while preserving useful functionality; identify tradeoffs and a result that would contradict the expected benefit. Distinguish a proposed challenge to a requirement from violating that requirement. Keep unknown implementation causes explicit. No implementation is authorized by this field.
- **Acceptance test:** given preconditions, when an action occurs, then an observable result should hold; include relevant recovery or negative paths. Avoid "make it intuitive" or invented performance thresholds.

## Improvement plan

Group findings by the user's outcome, such as complete the primary task, retain work or recover safely. Sequence blockers and consequential risks first, identify dependencies and link acceptance tests. Avoid a composite score hiding a severe finding. Record unresolved product constraints before recommending removal of mandatory steps.

## Human follow-up

Offer neutral tasks and questions targeted at unresolved concerns. Example: "Prepare a draft, consult the reference screen, then continue preparing it." Ask "What do you expect to happen next?" rather than "Was the button confusing?" Human findings remain pending until actual participants are observed.
