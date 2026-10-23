# Authored Evidence Trace

All entries are synthetic scenario facts, not executed actions. No timestamps, participant quotations or screenshots are supplied.

## E-001: Draft Loss

Fixture v1 contract: working title and body survive navigation to a required reference and back. Starting state: empty draft editor, no prior stored record. Viewport and input modality unspecified.

1. Set title to `Sample draft` and body to `Blue lantern`.
2. Activate `Open reference`. The reference screen appears.
3. Activate `Return to draft`. The editor appears with both fields empty.
4. Stored-record state is unknown. No refresh, backend query or repeated submission was performed, even within the fictional narrative.

The expectation is derived from the supplied contract. There is no contemporaneously recorded tester prediction; do not invent one. For a future authorized replay, start with an isolated empty draft and repeat steps 1–3; no live reset or deletion is prescribed here.

## E-002: Working Control

Separate fixture v1 scenario with the same title/body values:

1. Begin reference navigation, then select `Cancel` before leaving.
2. Both values remain in the editor.

This supports preserving cancellation behavior. It says nothing about keyboard operation, screen readers, actual people or service persistence.

## E-003: Incomparable Follow-Up

Fixture v2 scenario: a previously saved record contains title `Sample draft` and body `Blue lantern`.

1. Open the saved record.
2. Both fields display their stored values.
3. Do not navigate to the reference. Do not test cancellation.

This demonstrates only the stipulated open-record behavior. It cannot establish that the original unsaved-input navigation defect was repaired.
