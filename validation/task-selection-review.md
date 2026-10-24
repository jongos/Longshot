# Automatic and guided task selection

Authored contract review, 2026-10-24. No model evaluation or application execution.

| Input | Expected behavior |
| --- | --- |
| “Test this app” plus authorized environment | Infer purpose, select a few important journeys, state assumptions and proceed; no mandatory questionnaire. |
| “Test as a reviewer: approve, return for edits; skip admin” | Preserve role/workflows/exclusion; use authorized reviewer access only. |
| “Test as an editor” | Infer editor-relevant journeys and label assumptions; role declaration grants no new permissions. |
| “Create and resume a draft” | Test that workflow using known authorized capabilities; no invented persona required. |
| Exact navigation steps | Follow supplied steps, label guided discovery; do not claim independent first encounter. |
| Ambiguous product purpose with materially different success criteria | Ask a focused question; continue independent checks that do not depend on the answer. |
| Export succeeds only after unrelated menu search | Preserve completion and evidence of the workaround; no invented human failure rate. |
| Cancellation works but timing of lost access is unexplained | Assess missing decision information separately from functional success. |
| Mandatory safeguard adds a step | Preserve justified safeguard; extra clicks alone do not prove a defect. |
| Valid obstacle, rejected remedy | Preserve finding and record remedy rejection separately; do not mark resolved. |

Manual contract review found these cases represented by the updated entrypoint, walkthrough and finding template. This documents expected behavior, not measured adherence. Existing full JSON examples remain compatible: task origin/mode can use summary or journey condition; costly success uses assistance/limit; adjudication uses comparison reason or limitations. No schema expansion or required runtime.
