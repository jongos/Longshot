# Longshot bounded recommendation-quality cycle

Predeclared before report generation. Baseline: commit 0dddcf915f861d34c3afba71c82fafb4e5897300; complete seven-file skill snapshot retained in the local experiment directory; the baseline commit preserves the public source.

## Scope and budget

This is a synthetic evidence-packet reasoning experiment, not a rendered-interface test, human study, or market benchmark. No real app, production data, human participants, deployment, or broad benchmark is authorized by this protocol. The general major-test pause remains active outside this cycle.

- Six development packets in cases.json. Four independent conditions: baseline and one of three appended instructions. Exactly 24 development reports, at most 160 words per case per condition, same model and task prompt.
- Select at most one candidate or a justified combination after development adjudication. Four fresh packets in fresh.json are frozen now and excluded from development report contexts. Baseline and selected candidate each produce four reports, at most 160 words each. Maximum eight fresh reports.
- Maximum four Jev submissions: development comparison, development with response order reversed, fresh comparison, fresh with response order reversed. Batch independent typed questions; no image experiments, repeated retries to improve a score, or adaptive evidence rewriting. A failed transport may be retried identically and recorded, without increasing semantic comparisons.
- Stop if access fails, comparable outputs cannot be obtained, or the bounded budget is exhausted. Record incomplete coverage; do not enlarge scope.

## Neutral generation task

Use the provided Longshot skill and evidence packet to write a concise recommendation-quality review of that packet only. Identify supported findings or working behavior, evidence limits, recommendation if warranted, and a falsifiable acceptance check. Maximum 160 words per case. No desired finding count. Do not claim to have operated the interface or observed humans. Do not read other conditions, expected answers, judge results, or fresh packets during development.

## Evaluation and selection

Anonymize condition identity before Jev review. Give Jev identical evidence packets and reports. Evaluate separately: factual support, appropriateness of remedy to established scope/cause, retention of useful behavior, and testability. Allow tie and neither-supported outcomes. Reverse report order independently of content. Record model version, request and returned response. Probability/confidence is not correctness or a human measure.

Independently adjudicate report claims against packet facts. Score each dimension pass/partial/fail with cited report text and packet facts; no finding earns credit for verbosity or invented problems. Count critical unsupported prescriptions separately, never average them away. Useful change requires a specific observable gain over baseline without a new material regression; ties do not justify shipping instructions. Disagreement or order sensitivity remains unresolved evidence, not a reason to rerun until favorable.

Fresh validation is a one-time generalization check, not a reusable development set. Freeze the selected instruction before generating fresh reports. If fresh results regress materially, reject or defer that change; do not revise and re-test on these same cases while calling them fresh. Report exact counts and limitations. Preserve all raw reports, adjudications, prompts and Jev results. Local skill/repo edits happen only after this evaluation supports them.
