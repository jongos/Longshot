# Report Continuity Validation

## Issue #3 follow-up — 2026-10-24

Added [14 authored semantic decision cases](semantic-review.md) covering identity, retest relevance, channel-specific coverage and Markdown/JSON meaning. Updated the guide and report template to require evidence-content review, preserve uncertain matches and split/merge history, and reconcile both formats. Kept schema 1.0.0 and consumer requirements unchanged. These are specification examples, not independent behavioral evaluation. Major tests remain paused.

Focused checks rerun successfully: both full JSON examples and existing negative/reference checks; skill frontmatter/scaffold validation; whitespace diff check. Manual contract review covered all 14 cases and their paired representation excerpts. The saved-draft evidence remains insufficient for resolution even though a deliberately altered candidate passes schema structure. No model trial, browser walkthrough, human study or landing-page visual/accessibility evaluation was performed. The examples document expected decisions, not measured agent adherence.

Date: 2026-10-23. Major tests remain paused. No real application, human study, competitor trial or large benchmark was run.

Added optional schema 1.0.0, report-continuity guidance, capability/coverage distinctions and a complete authored synthetic evidence bundle. The sample includes a working control and an intentionally incomparable follow-up; LS-001 remains untested, not resolved. No screenshots or participant results were fabricated.

Focused development checks in `check_report_examples.py` passed: both exports conform to Draft 2020-12 schema; evidence IDs and local artifact anchors resolve; the follow-up covers the prior finding; unsupported versions, invalid coverage values, missing resolution evidence and dangling references are rejected. A structurally valid resolution candidate is checked only in memory to exercise the positive schema branch; it is not a real test result or published example of a repaired defect.

The schema cannot establish evidence truth, comparability, privacy, semantic finding identity or recommendation benefit. Human/agent review must verify those. The script requires the standard `jsonschema` package for development validation; consumers of the skill do not need it. No new runtime dependency or service is introduced.

Skill structural validation passed. README and landing-page heading audits passed (13 and 29 headings). Whitespace checks passed. The landing-page change adds explanatory copy and a link using existing styles; no new visual system or interaction is introduced. This update was not a full browser/accessibility evaluation.
