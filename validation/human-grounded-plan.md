# Human-Grounded Evaluation Plan

Status: research and design only. No major benchmark, recruitment or human study is authorized or reported as completed by this plan.

## Evidence to Seek

Consented, sanitized human usability sessions, stable authorized application snapshots and independently adjudicated issue records. Verify licenses, redistribution rights, consent scope, access requirements, recording redaction and whether the tasks can actually be reproduced. Do not infer permission from a public paper or repository.

Starting research leads: [UXAgent](https://arxiv.org/abs/2502.12561), which supports study-design iteration before human testing, and [Avenir UX](https://onflow-ai.github.io/Avenir-UX/), which describes human-agent comparisons and preliminary results. Neither is assumed to supply an immediately usable licensed dataset. Generated satisfaction ratings and simulated think-aloud transcripts are not human measurements.

## Proposed Comparison

### Qualification shortlist and decision gate

Retain the public-source leads from [issue #1](https://github.com/jongos/Longshot/issues/1); this planning update does not claim new access or source verification:

| Lead | Potential use | Unresolved qualification |
| --- | --- | --- |
| [OPeRA](https://huggingface.co/datasets/NEU-HAI/OPeRA/blob/main/README.md) | Human web behavior and archival task evidence | Reuse/processing scope, independent issue annotations and executable historical states |
| [GUIDE](https://huggingface.co/datasets/kixlab/GuideBench) | Novice difficulty/help evidence | Gated access, permitted processing and defect adjudication; recordings are not runnable interfaces |
| [MultiUX](https://yaoyashen.github.io/MultiUX.pdf) | Independent issue review and consensus method | Accessible session artifacts, reuse rights and matching app states |

For each candidate, record exact version, available artifacts, task, consent/reuse/processing scope, sanitization, access conditions, app-state fidelity, issue labels and unresolved questions. Choose archival interpretation only when recordings support it; choose independent browser discovery only when authorized frozen interfaces exist. No candidate is selected as ready to run yet. The next research deliverable is a completed qualification sheet and a justified select/defer decision.

Before execution, freeze matching/adjudication rules, acceptable consequential misses and false positives, reviewer time/cost limits, model/tool budget and stop conditions. Start with two development tasks and four held-out cases, including two consequential defects and two narrowly reviewed controls; three fresh runs per condition would give 24 held-out runs against a plain-agent baseline. This is a proposed feasibility pilot, not a reliability estimate. Keep paired variants and related task/interface families within one split. Execution needs separate approval.

### Separate questions and measures

- Task selection: are the important user goals and consequential states covered? Compare automatic selection with a reviewed priority list; evaluate guided adherence separately.
- Detection: supported distinct findings, consequential misses, clean-control false positives and evidence quality on identical tasks.
- Stability: recurrence and severity/confidence changes across fresh runs; classify tool failures separately. More runs of one model do not represent more human participants.
- Recommendations: causal relevance, proportionate scope, preserved behavior and falsifiable acceptance criteria. Measure actual benefit only after an authorized change-and-retest.

Record supported disagreements, unknowns and zero-yield runs. Do not average away a severe miss or substitute report length for usefulness. Source/privacy or reproducible-state failures stop dependent work.

Compare Longshot with a plain task-testing prompt using the same model, tools, access, budgets and app states. Keep development cases separate from held-out tasks and hide human findings from testers. Include good controls, justified safeguards, uncertain outcomes, tool failures and genuinely consequential defects. Record prior solution exposure and evidence modality. Use separate resettable sessions and independent contexts where available; disclose limitations.

Have blinded reviewers adjudicate issue-level evidence and recommendation quality. Match findings by underlying obstacle rather than wording, deduplicate repeated symptoms and preserve disagreement. Human-observed issues are a reference, not an exhaustive oracle: review valid new findings independently. Report denominators and uncertainty; do not label every unmatched issue a false positive or every agent success human success.

Measure supported-finding precision; consequential-issue recall against the adjudicated reference; reproducibility; recommendation relevance, preservation of safeguards and regression risk; confidence calibration; false positives on clean controls; and time/cost per verified useful finding. Separate execution failure from product failure. Do not optimize number of criticisms, report length or a single aggregate score.

Recommendation benefit requires a separately authorized change-and-retest comparison; human benefit requires human outcome evidence. A report judged plausible is not evidence a fix helped. Determine a feasible pilot and sampling plan after assessing data availability; do not invent a statistically sufficient participant count.
