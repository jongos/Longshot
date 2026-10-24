# Semantic continuity review

Issue: https://github.com/jongos/Longshot/issues/3

These are authored decision cases, not executed application sessions or a model benchmark. Markdown and JSON excerpts below describe intended representations in schema 1.0.0; fragments are not standalone exports. The existing full exports remain the structural examples. No human outcomes, screenshots or independent reviewer results are claimed.

## Cases and contract decisions

| Authored evidence packet | Readable representation | JSON representation / review decision |
| --- | --- | --- |
| Prior LS-001: unsaved text disappears on reference return. Same conditions and disappearance after Reference is renamed Guide. | LS-001 reproduced; only the label changed. | `finding_id: LS-001`, `status: reproduced`; record label change in `changed_conditions`. Keep ID; wording is not identity. |
| Prior LS-001 as above. New observation: Guide cannot open because access is denied; draft is retained. | Separate obstacle, new ID LS-002; original loss route blocked, not resolved. | LS-002 in `findings`; LS-001 comparison `status: blocked`, with access boundary in `reason`. Do not merge by shared control name. |
| Prior report omitted starting state; new draft loss could match LS-001 but evidence cannot establish it. | Match uncertain; preserve LS-001, provisional LS-002, explain candidate relationship. | Candidate relationship in `reason`/`limitations`; `comparable: null`; no claimed resolution. Missing baseline conditions remain missing. |
| Later diagnosis splits LS-001 into navigation loss LS-002 and refresh loss LS-003. Only navigation was attempted. | Preserve original history and explain both successors; refresh remains untested. | Retain LS-001 comparison with supported status and successor IDs in `reason`; do not imply LS-003 was tested. Same rule preserves all predecessor rows when merging. |
| Changed build, same original unsaved-input route: text retained; acceptance condition and cancel-preservation check also pass in authored evidence E-A/E-B. | LS-001 resolved only for these conditions; build changed, relevant conditions comparable. | `verified_resolved`, `comparable: true`; all three checks `passed` with relevant E-A/E-B references. Keep synthetic provenance; this is a hypothetical valid resolution, not a repair result. |
| Relevant route attempted once without loss; preservation check omitted. | LS-001 not reproduced on this attempt; repair not established. | `status: not_reproduced`; omitted check `result: untested`. Do not convert absence into resolution. |
| Existing saved draft opens; original unsaved-input route never attempted. | LS-001 untested despite successful other journey. | Existing run-002 represents this: `status: untested`, `comparable: false`, three checks untested. Empty `findings` does not erase comparison. |
| Same packet, but export claims all checks passed and points to saved-draft evidence E-003. | Reject resolution claim; evidence never exercised the original route. | Structurally valid references still fail semantic review. Restore the preceding representation; schema success cannot override evidence content. |
| Supplied screenshot shows a clipped label; no interaction evidence. | Visible clipping supported in supplied image; keyboard/focus and persistence untested. | Provenance `supplied`; current host availability `unknown`; relevant interaction coverage `untested`. Do not promote visible-state review into an executed journey. |
| Accessibility-tree-only host exposes a button name; no pixels or screen-reader session. | Exposed name supported; appearance and actual assistive-technology behavior unknown. | Scope capability to tree inspection; do not mark visual or screen-reader coverage verified. Preserve channel in evidence. |
| Interactive host shows Saved toast; authorized storage verification is unavailable. | Acknowledgment observed; persistence uncertain. | Journey `outcome: uncertain` if persistent save is completion condition; persistence row `coverage: blocked` with boundary in `limit`. Tool availability does not prove service completion. |
| Supported loss finding was diagnosed using source; human impact is inferred and implementation cause unknown. | Keep high impact separate from confidence; disclose privileged assistance and speculative consequence. | Preserve `assistance`, `cause: unknown`, `consequence_is_inference: true`, severity/confidence reasons, and recommendation preserve/tradeoff/disconfirmation fields. No stronger claim in export. |
| Narrow working control completes; no supported defect. | No findings for this route; other states untested. | `findings: []`; retain journey evidence, scoped strengths and limitations. No invented criticism or universal usability claim. |
| Access blocked before task starts, no interface evidence. | Review blocked; product quality unknown, no defect inferred. | `findings: []`; blocked journey and boundary limit remain. Do not invent an evidence item or severity to fill the report. |

## Keep / change / defer

- **Keep:** schema 1.0.0, optional JSON, Markdown default, existing examples and explicit synthetic provenance. No consumer dependency or new required field.
- **Change:** distinguish relevant attempt from unrelated success; assess evidence relevance for each resolution check; explain uncertain identity and split/merge history; reconcile meaning across formats; scope modality claims.
- **Defer:** automated semantic matching, model performance evaluation, live demonstration (#2), and human-grounded benchmark execution (#1). A manual decision set is not evidence of model reliability. No major tests ran.

Maintenance cost is one focused guide and this bounded case set. Expand only for a demonstrated ambiguity. Recommendation validity remains separate from detection: preserve useful behavior, state tradeoffs, and give a result that could contradict the proposed benefit. Actual human benefit is not established here.
