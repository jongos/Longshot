# Validation results

Run date: 2026-10-23.

## Method

An independent agent received the skill, retained references and thirteen authored synthetic evidence packets in [cases.md](cases.md). It produced [responses.md](responses.md) and an [independent assessment](independent-assessment.md). It received no expected answers or implementation suggestions. No application was accessed or modified, no services were invoked and no participants were studied.

This evaluates instruction following, activation decisions and report quality against supplied traces. It is not a test of automatic skill discovery in every host, live browser operation, visual perception, assistive technology or human usability.

## Observed results

| Packet | Tested behavior | Result in initial evaluation |
| --- | --- | --- |
| A | Silent validation rejection | Identified missing feedback; retained valid-path evidence and testable recovery criteria. |
| B | Draft lost after navigation | Identified lost work and a precise retention acceptance test. |
| C | Ambiguous destructive action | Identified label/outcome mismatch and prevention need; classification ambiguity led to clarification. |
| D | False completion after simulated failure | Identified misleading success; kept simulation separate from live service claims. |
| E | Mandatory optional decoration | Used the supplied requirement to justify removing the gate, not click count alone. |
| F | Keyboard and modal focus failure | Identified blocked keyboard completion without inventing screen-reader or conformance results. |
| G | Appealing interface with failed completion | Prioritized lost work and recovery; did not treat supplied appearance as independently inspected. |
| H | Working control flow | No invented findings; preserved coverage limits. |
| I | Single spelling correction | Did not expand into an audit or claim an edit without access. |
| J | One-sentence factual question | Answered directly without audit activation. |
| K | Missing access to private production app | Requested safe evidence/access; no fabricated observations or assumed authorization. |
| L | Canned AI preview and validation claim | Rejected reliability/trust claims; initially forced an evidence gap into a severity-rated finding. Corrected in skill and retested. |
| M | Justified confirmation step | No invented defect; preserved the required safeguard. |

## Refinement

The skill now explicitly separates evidence gaps from interface findings, distinguishes an observed action-label mismatch from an inferred human reaction, suggests sanitized evidence or synthetic access for blocked reviews, and permits compact findings without dropping substantive fields. Original outputs are retained for transparency. See [targeted retest](retest.md) for the subsequent C/L responses.

## Package checks

- The skill-creator `quick_validate.py` passed for the skill and installed copy. The default Python lacked PyYAML; validation used an already available local PyYAML package, without adding a runtime dependency to Longshot.
- UI metadata parsed successfully; automatic invocation is enabled, the description length is valid and the example names the correct skill identifier.
- All three relative links in SKILL.md resolve to bundled references.
- Installed files were hash-compared with repository skill files after refinement and matched.

## Limits

No screenshots exist for these text-only packets, and none were fabricated. No rendered browser walkthrough, real application review, human study or automated accessibility scan was performed. User confusion, satisfaction and success rates remain unmeasured. Longshot's live evidence collection and host-specific discovery remain unvalidated. The Microsoft PDF fetch limitation is documented in [research guidance](../skills/human-centered-ui-review/references/research.md). Further validation should use authorized isolated rendered fixtures and actual human research where needed, not substitute these packet results for either.
