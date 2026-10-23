# Sample Report and Follow-Up

**Synthetic evidence review only.** No real application, participant or browser session was tested.

## Run example-001

Disposition: the authored primary journey loses input on a required navigation path. The cancellation control preserves input. Storage behavior is unknown. Outcome is blocked under the stipulated task; no agent assistance or human behavior was measured.

Scope: fictional draft editor, fixture v1; prepare a draft using a required reference. Input is `Sample draft` / `Blue lantern`. No live accounts or mutations are authorized by this example. Build names are scenario identifiers; viewport, zoom and input modality are unknown. First-encounter testing is not applicable to an authored packet.

| Capability | Host Availability | Coverage | Limit |
| --- | --- | --- | --- |
| Visual interaction | Unknown | Untested | No browser session occurred. |
| Persistence verification | Unknown | Untested | Visible input only; no stored-state evidence. |
| Screenshots | Unknown | Untested | No images were captured. |

| Journey | Scenario Outcome | Evidence |
| --- | --- | --- |
| Enter draft → reference → return | Blocked by cleared input | [E-001](trace.md#e-001-draft-loss) |
| Begin navigation → cancel | Completed with values preserved | [E-002](trace.md#e-002-working-control) |

### LS-001: Required Reference Navigation Clears Working Input

**Expected / observed:** the fixture contract preserves both fields across the required reference trip; E-001 stipulates that both return empty. Reproduction steps and safe hypothetical starting state are in E-001. No live reproduction or contemporaneous expectation annotation was recorded.

**Classification:** confirmed defect within the fictional contract. **Severity:** high, because the required journey loses working input. **Confidence:** high in interpreting the stipulated mismatch, not in a real application's behavior. Cause is assigned to product behavior within the scenario; implementation root cause is unknown.

**Potential consequence:** the user may need to re-enter work. This is an inference; frequency and human impact are unmeasured. Permanent stored-record deletion is not established.

**Recommendation:** retain working title/body across the reference trip. Preserve the reference requirement and working cancellation. Define draft lifetime and account isolation rather than retaining every draft indefinitely.

**Acceptance test:** given distinct title/body values, open the required reference and return; both remain. In a separate control, cancel navigation and verify both remain. If a comparable authorized replay already restores these values, the loss claim does not reproduce. Do not infer a fix from an unrelated success.

**Plan:** prioritize retention; verify the original path and cancellation after an authorized change. No implementation or retest was performed. No other findings are invented from missing keyboard or storage evidence.

**Human follow-up:** “Prepare a draft using the reference and continue editing.” Ask what the participant expects to remain on returning. This is a proposed task, not participant testimony.

## Run example-002

The authored follow-up opens an existing saved draft in fixture v2. Both fields appear ([E-003](trace.md#e-003-incomparable-follow-up)); no new findings arise from that limited packet. This is useful working behavior, but it does not exercise the original reference trip or cancellation.

| Finding | Prior Run | Current Status | Comparable? | Reason |
| --- | --- | --- | --- | --- |
| LS-001 | example-001 | untested | No | Different build and starting state; original navigation and acceptance test absent. |

The original observation remains in example-001. LS-001 is **not marked fixed**. Next step, if authorized: exercise its original acceptance path and preserved cancellation behavior. Capability limits and lack of human evidence remain unchanged.
