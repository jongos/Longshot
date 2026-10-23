# Human-Grounded Evaluation Plan

Status: research and design only. No major benchmark, recruitment or human study is authorized or reported as completed by this plan.

## Evidence to Seek

Consented, sanitized human usability sessions, stable authorized application snapshots and independently adjudicated issue records. Verify licenses, redistribution rights, consent scope, access requirements, recording redaction and whether the tasks can actually be reproduced. Do not infer permission from a public paper or repository.

Starting research leads: [UXAgent](https://arxiv.org/abs/2502.12561), which supports study-design iteration before human testing, and [Avenir UX](https://onflow-ai.github.io/Avenir-UX/), which describes human-agent comparisons and preliminary results. Neither is assumed to supply an immediately usable licensed dataset. Generated satisfaction ratings and simulated think-aloud transcripts are not human measurements.

## Proposed Comparison

Compare Longshot with a plain task-testing prompt using the same model, tools, access, budgets and app states. Keep development cases separate from held-out tasks and hide human findings from testers. Include good controls, justified safeguards, uncertain outcomes, tool failures and genuinely consequential defects. Record prior solution exposure and evidence modality. Use separate resettable sessions and independent contexts where available; disclose limitations.

Have blinded reviewers adjudicate issue-level evidence and recommendation quality. Match findings by underlying obstacle rather than wording, deduplicate repeated symptoms and preserve disagreement. Human-observed issues are a reference, not an exhaustive oracle: review valid new findings independently. Report denominators and uncertainty; do not label every unmatched issue a false positive or every agent success human success.

Measure supported-finding precision; consequential-issue recall against the adjudicated reference; reproducibility; recommendation relevance, preservation of safeguards and regression risk; confidence calibration; false positives on clean controls; and time/cost per verified useful finding. Separate execution failure from product failure. Do not optimize number of criticisms, report length or a single aggregate score.

Recommendation benefit requires a separately authorized change-and-retest comparison; human benefit requires human outcome evidence. A report judged plausible is not evidence a fix helped. Determine a feasible pilot and sampling plan after assessing data availability; do not invent a statistically sufficient participant count.
