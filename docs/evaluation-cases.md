# Evaluation cases

These cases check Longshot’s **scope discipline** and **consequence-first ranking** using authored fixtures. They are not live browser tests or human research. They require no credentials, paid services or product writes.

## What they cover

| Case | Request | What a useful run shows | Material failures |
| --- | --- | --- | --- |
| [narrow-form-save](../validation/evaluation-cases/narrow-form-save/) | Review form save only | Silent validation failure surfaced; save control ranked by trust impact | Full-app audit; treating failure as success |
| [misleading-complete](../validation/evaluation-cases/misleading-complete/) | Review submission feedback | False “Completed” ranked above polish | Accepting the message as persistence proof |
| [spelling-only](../validation/evaluation-cases/spelling-only/) | Fix one label typo | Skill does not apply; no invented UX findings | Multi-finding audit without access |
| [narrow-checkout-save](../validation/evaluation-cases/narrow-checkout-save/) | Save button only | No in-scope defect required; **Out of scope** notes for other issues | Header/settings defects in main findings |

Fixtures live under `validation/evaluation-cases/<case>/`:

- `request.md` — user prompt
- `packet.json` — facts and boundary
- `expected.json` — machine-checkable expectations (counts, order, scope flags)
- `golden-report.json` — exemplar JSON report that matches the skill’s export schema and ranking rules

## Run the structural checks (from source)

From the repository root, use Python 3.12+ in an isolated environment (same as [validation/README.md](../validation/README.md)):

```sh
python -m venv .venv
.venv/bin/python -m pip install -r validation/requirements.txt
.venv/bin/python validation/check_report_examples.py
.venv/bin/python validation/check_evaluation_cases.py
```

Expected output includes `PASS: 4 evaluation cases — fixtures, golden reports, ranking and scope expectations.`

CI runs both scripts on pushes and pull requests.

## Run a behavioral check (agent)

Use a **fresh** evaluator session with the current `longshot-human-centered-ui` skill. Provide only that case’s `request.md` and `packet.json` — not this rubric, another evaluator’s answer or `golden-report.json`. Write the response outside the repository.

Judge decisions and evidence, not exact wording. Compare against `expected.json` **material_failures** and whether findings stay in scope. Record skill revision, case id and limitations with any test report.

A passing structural check does not prove every agent run will rank correctly; it locks fixture shape, schema compliance and exemplar ordering. Broader synthetic packets remain in [validation/cases.md](../validation/cases.md).

## Attribution

Ranking and scope patterns are aligned with common UX review practice. Comparable open work includes [rinzler1/ux-review-skills](https://github.com/rinzler1/ux-review-skills) (MIT). Longshot’s text and fixtures are original to this repository (Apache-2.0).