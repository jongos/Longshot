# Validation and development checks

## Completed records

- [Initial synthetic report evaluation](RESULTS.md): thirteen authored packets, generated reports and independent assessment.
- [Bounded recommendation cycle](recommendation-cycle-2026-10-24/RESULTS.md): 32 synthetic reports, 44 evaluator judgments, ties, regressions and narrow adopted refinements.
- [Report continuity/schema checks](report-continuity.md): example exports, references and resolution requirements.
- [Rename and independent role](rename-independent-role.md), [walkthrough protocol](walkthrough-protocol.md), and [retest](retest.md): focused historical records.
- [Semantic review cases](semantic-review.md), [task selection](task-selection-review.md), and [workflow friction](workflow-friction.md): authored contract cases; not executed browser benchmarks.
- [Website checks](website-launch.md): historical landing-page checks, not skill reliability evidence.

## Plans — execution paused

- [Observed demonstration, issue #2](observed-demo-plan.md).
- [Human-grounded benchmark research, issue #1](human-grounded-plan.md).

Major tests remain paused. Existing generated reports and sample traces must not be relabeled as human observations or executed application journeys.

## Run the checks

From the repository root, use Python 3.12 or later in an isolated environment:

```sh
python -m venv .venv
# macOS/Linux:
.venv/bin/python -m pip install -r validation/requirements.txt
.venv/bin/python validation/check_report_examples.py
.venv/bin/python validation/check_evaluation_cases.py
```

On Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r validation/requirements.txt
.\.venv\Scripts\python.exe validation/check_report_examples.py
```

Expected output begins `PASS: two examples`, then `PASS: 4 evaluation cases`. The first check validates schema structure, the two sample reports, evidence references and anchors, prior-finding coverage, resolution requirements and invalid exports (including empty reproduction steps). The evaluation-case check validates fixtures, golden reports, consequence-first finding order and narrow-scope expectations under `validation/evaluation-cases/`. See [docs/evaluation-cases.md](../docs/evaluation-cases.md). Neither check establishes evidence truth or usability performance.

[GitHub Actions](../.github/workflows/validate.yml) runs this same check on pushes and pull requests. These dependencies and CI are development-only; skill users need neither Python nor jsonschema. CI does not run browsers, paid evaluations, benchmarks or human studies.
