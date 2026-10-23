# Independent targeted retest: C and L

Re-read the revised skill and finding template and reapplied only synthetic cases C and L from `validation/cases.md`. Original reports are preserved. No real app, service, screenshot or participant was inspected; this is a limited supplied-evidence review.

## C — Action clarity

**C1 — Identify deletion before activation.** In the supplied disposable-fixture trace, the sole control below an editable item has visible and accessible name `Go`; activation immediately deletes the item without explanation, confirmation or undo. For the task of deciding whether to activate this control, meaningful-label and error-prevention conventions support identifying the destructive outcome beforehand; the supplied label fails to identify deletion. This is a **confirmed defect within the fictional fixture**, with **high confidence** in the label/outcome mismatch. **Severity: high**, because the action loses the item without recovery, although item value and reach are unknown. Unintended deletion is a plausible human consequence, not an observed misunderstanding; frequency is unknown. Recommend `Delete item` plus a cancellable confirmation if recovery is unavailable. **Acceptance:** given an existing item, visible and accessible names identify deletion; activating the action opens the proposed confirmation without deleting; cancellation preserves the item; explicit confirmation deletes only that item. Human follow-up: “What do you expect this action to do?” before activation.

## L — Preview validation

The preview does **not** establish AI service reliability or user trust. The supplied trace supports only a timed canned suggestion with editing and dismissal controls; no AI service was called and no participants were observed. Retain the `Suggestion` label and those controls, but do not infer that people understand or trust them.

This is an **evidence gap**, not a demonstrated interface defect; no defect severity is warranted. Resolve reliability claims with separately authorized tests of the actual service across relevant success and failure conditions, using agreed requirements. Resolve human-understanding and reliance questions through actual task observations, for example “Use this suggestion to prepare your draft,” followed by “What would you check before using it?” Report the preview as simulated and keep service-test evidence and participant evidence separate. The packet does not establish that the interface itself conceals its simulated nature.

## Assessment of changes

The revisions resolve the two targeted reporting ambiguities in this retest. C now cleanly distinguishes a confirmed action-label problem from inferred human misunderstanding. L no longer forces an unsupported validation claim into a usability-defect category with artificial severity. Compact formatting is expressly permitted while retaining substantive finding fields; it reduces structural repetition but does not remove the inherent length of a complete finding.

These are two authored cases evaluated by the same independent reviewer after explicit feedback, so they demonstrate a successful targeted correction, not broad generalization or a blinded comparison. Real browser evidence gathering, live asynchronous behavior and human outcomes remain unvalidated.
