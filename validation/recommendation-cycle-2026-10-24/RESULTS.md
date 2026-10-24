# Bounded recommendation improvement cycle — 24 October 2026

**Result:** the baseline was already strong. This cycle supports two narrow reporting clarifications, not a broad quality-score gain: concrete preservation acceptance checks, and separating a displayed shortcut from exercised behavior. No complete candidate instruction was adopted.

## What ran

- Frozen baseline: `0dddcf915f861d34c3afba71c82fafb4e5897300`; seven-file [committed skill](https://github.com/jongos/Longshot/tree/0dddcf915f861d34c3afba71c82fafb4e5897300/skills/longshot-human-centered-ui).
- Six authored synthetic development packets × four independent report conditions = **24 reports**. Conditions: baseline, scope before remedy, cause before prescription, preservation before simplification.
- Four frozen fresh packets × baseline and the unchanged selected preservation condition = **eight reports**. All 32 reports stayed within the predeclared 160-word limit (128–154 words).
- **Four Jev playground submissions, 44 pair judgments**, resolved model `jev-1.14.0`: 18 development comparisons in each order, then four fresh comparisons in each order. No retries, image tests or additional semantic batches.
- Independent agent adjudication of evidence support, remedy fit, preservation and testability. It saw the packets and reports, not Jev judgments or selection rationale. The generating and adjudicating agents were not human participants.

The [protocol](protocol.md), [generation record](generation.md), [candidate instructions](variants.json), [development packets](cases.json), [fresh packets](fresh.json), raw reports, anonymized requests, response JSON and answer keys are retained here. Jev was a development evaluator; it is not a consumer dependency. Official interface documentation: [TypeSafe primitives](https://docs.typesafe.ai/primitives).

## What the comparisons actually showed

| Candidate | Development comparisons after reversing report order | Decision |
|---|---|---|
| Scope | Five stable ties; one candidate preference became a tie | Do not adopt. Mostly redundant, sometimes unrelated scope inventory. |
| Cause | Four stable ties; one stable candidate preference (D6); one stable baseline preference (D5) | Do not adopt. More diagnostic detail was not consistently better. |
| Preservation | Four stable ties; one stable candidate preference (D3); one candidate preference became a tie (D4) | Advance unchanged to fresh cases, then retain only narrow supported elements. |
| Preservation on fresh cases | Three stable ties; F1 candidate preference became a tie | No stable fresh-case preference. No broad superiority claim. |

Confidence values are retained as evaluator output, not correctness probabilities or human measures. The [development adjudication](adjudication-dev.md) judged D3 materially equivalent despite Jev's preference; it found useful D4/D6 details despite ties or order sensitivity. The [fresh adjudication](adjudication-fresh.md) found modest F1 role-check and F3 authorization clarity gains, but weaker F2 diagnostic wording and a missing forward-focus acceptance check in F4. All four fresh cases correctly avoided inventing a current product defect; neither condition violated the authorized test boundary.

## Concrete gains retained

| Before in the baseline report | Useful detail in the candidate | Narrow instruction now retained |
|---|---|---|
| D6 acceptance checks one example: 192 frames, 24/30 fps, correct seconds and unchanged count. | Checks that arbitrary valid integer counts remain directly editable without rounding or silent conversion. | When a recommendation can affect evidenced working behavior, include a task-relevant preservation check rather than only the motivating example. |
| D4 checks the visible template button and focus return; it does not explicitly separate the displayed Ctrl+T label from shortcut execution. | Says “Shortcut execution itself is not established by its label” and proposes testing it separately. | A visible promise is not executed coverage. Preserve the verified button/focus check while marking shortcut execution proposed or untested. |

The final walkthrough/template edit is deliberately narrower than the tested preservation condition. It adds an explicit boundary against invented requirements and against replacing known checks with speculative coverage. This responds to the independent review: broad preservation wording introduced a populated-note policy outside D4's task, implied an explicit-choice requirement in D6, and omitted F4's supplied forward-focus check. Those expansions were **not** adopted. Scope and cause additions were **not** added to the skill.

The final narrowed wording received structural and documentation checks; it did not receive another generative evaluation. The fresh comparison tested the unchanged broader candidate, not this final editorial subset. The bounded budget was not expanded to retune against the fresh set.

## What this does not establish

These were supplied synthetic evidence packets, not executed interface journeys. No app, production data, real notification, payment, participant or human-grounded benchmark was used. One generation per case/condition cannot separate instruction effects from ordinary generation variation. Cases within each condition shared a context; four fresh cases are a small transfer check, not statistical validation. Neither the pair judge nor independent adjudicator is ground truth for human usability.

The tested broader preservation condition did not outperform the baseline across all dimensions. The useful outcome is a small, evidence-linked clarification and rejection of unnecessary instruction growth. No best-in-market or human-equivalence claim follows. Only this bounded cycle was unpaused; broader tests remain paused.

## Verification

Report counts, IDs, JSON parsing and word budgets were checked deterministically. Repository skill/schema checks and landing-page smoke checks are recorded in the delivery verification below. No application changes were made.

### Delivery verification

- Skill frontmatter/scaffold validation passed.
- Existing report-schema/example checks passed, including artifact/reference integrity, prior-finding coverage and resolution evidence gates.
- All 32 report objects parsed, IDs matched their packets, and word counts stayed within 160. All four evaluator response objects contained the expected question IDs.
- Landing page: desktop 1440 px and mobile 390 px had no horizontal page overflow; the guidance disclosure opened by keyboard.
- Final narrowed skill wording was not subjected to another report-generation round.
- Local installation synchronized; all seven source/installed file hashes matched.
