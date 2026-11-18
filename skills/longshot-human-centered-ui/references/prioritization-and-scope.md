# Prioritize findings and hold scope

Use when ordering findings, writing the improvement plan, or deciding what belongs in the main report versus a brief aside.

## Consequence comes first

Every finding should state what could happen to someone trying the task, not only what looked wrong. Rank findings for readers by **consequence tier**, then by **how often** the situation arises, then by **how many people or journeys** it affects. Confidence and implementation effort stay visible but do not reorder a confirmed blocker below cosmetic polish.

### Consequence tiers (primary sort)

Assign one tier per finding. Use the highest tier the evidenced behavior credibly supports; uncertainty does not automatically lower tier if the stakes are clear.

| Tier | Meaning | Typical severity (not automatic) |
| --- | --- | --- |
| **blocks** | Cannot complete the task, or the interface credibly leads to a wrong irreversible result | critical / high |
| **harms_trust** | Task may appear done while it failed, destructive action is disguised, or saved work is not actually kept | critical / high |
| **friction** | Task can finish with substantial extra steps, memory, waiting or recovery | medium / high |
| **polish** | Minor clarity, layout, wording or preference; task still completes | low / medium |

### Usage and reach (secondary and tertiary sort)

Within the same tier, order findings that hit **more people or more core journeys** earlier. State usage as **measured**, **owner-reported**, or **estimated**; do not treat one walkthrough as measured incidence. Reach counts **distinct tasks or roles affected**, not agent retries.

| Reach label | Meaning |
| --- | --- |
| **widespread** | Primary or daily loop for most intended users |
| **common** | Important branch or secondary role, encountered often |
| **situational** | Edge case, rare role or infrequent path |
| **rare** | Unusual setup; still report when consequence is severe |

### Tie-breaking and forbidden shortcuts

- If tiers match and reach is comparable, prefer higher **severity** and higher **confidence** earlier.
- Do **not** multiply tiers into a single score that can bury a blocker.
- Do **not** rank a hypothesis as **blocks** without evidence that matches that consequence.
- Do **not** downgrade **harms_trust** to **friction** because a workaround exists; note the workaround separately.

### Explicit ranking rule (for skill and reports)

Sort the **findings list**, the **opening “most consequential” summary**, and the **improvement plan** using:

1. Consequence tier: `blocks` → `harms_trust` → `friction` → `polish`
2. Reach: `widespread` → `common` → `situational` → `rare`
3. Severity: `critical` → `high` → `medium` → `low`
4. Confidence: `high` → `medium` → `low` (same consequence and reach)

Record `consequence_tier`, `reach`, and `frequency_basis` on each finding in JSON export when used; in Markdown, state tier and reach in the finding or in a short ranked list at the top.

## Scope discipline

Match the user’s stated boundary: one screen, one flow, one component, one role, or explicit exclusions.

- **In scope:** Test and report only what the request authorizes. Infer missing detail only when it changes safe access or success meaning; label inferences.
- **Stay narrow:** A focused request is not permission to run a full-product audit. Do not add journeys, roles or surfaces the user excluded or did not ask for.
- **Out of scope — brief aside:** When something outside the boundary would likely matter, list it in a short **Out of scope** section (one line per item: what was noticed, why it was not tested). Do not expand the review to cover it without new authorization.
- **Suggested coverage:** Keep user-supplied workflows distinct from optional extra journeys; label suggested coverage and do not silently replace the user’s list.

Reconcile before delivery: requested scope, what was attempted, what was blocked, and what was deliberately not tested.