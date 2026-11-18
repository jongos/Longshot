"""Development-only checks for evaluation-case fixtures and golden reports."""
import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
CASES_ROOT = Path(__file__).resolve().parent / "evaluation-cases"
REPORT_SCHEMA = json.loads(
    (ROOT / "skills/longshot-human-centered-ui/references/report-schema.json").read_text()
)
EXPECTED_SCHEMA = json.loads((CASES_ROOT / "expected-schema.json").read_text())

Draft202012Validator.check_schema(REPORT_SCHEMA)
Draft202012Validator.check_schema(EXPECTED_SCHEMA)
report_validator = Draft202012Validator(REPORT_SCHEMA)
expected_validator = Draft202012Validator(EXPECTED_SCHEMA)

TIER_RANK = {"blocks": 0, "harms_trust": 1, "friction": 2, "polish": 3}
REACH_RANK = {"widespread": 0, "common": 1, "situational": 2, "rare": 3}
SEVERITY_RANK = {"critical": 0, "high": 1, "medium": 2, "low": 3}
CONFIDENCE_RANK = {"high": 0, "medium": 1, "low": 2}


def sort_key(finding: dict) -> tuple:
    tier = finding.get("consequence_tier")
    if tier not in TIER_RANK:
        tier_rank = SEVERITY_RANK.get(finding["severity"], 9)
        tier_rank = min(tier_rank, 3)
    else:
        tier_rank = TIER_RANK[tier]
    reach = finding.get("reach")
    reach_rank = REACH_RANK.get(reach, 1)
    severity_rank = SEVERITY_RANK[finding["severity"]]
    confidence_rank = CONFIDENCE_RANK[finding["confidence"]]
    return (tier_rank, reach_rank, severity_rank, confidence_rank)


def check_ranking(findings: list) -> None:
    if len(findings) < 2:
        return
    keys = [sort_key(f) for f in findings]
    for prev, cur in zip(keys, keys[1:]):
        assert cur >= prev, "findings must be sorted by consequence tier, reach, severity, confidence"


def check_case(case_dir: Path) -> None:
    for name in ("request.md", "packet.json", "expected.json", "golden-report.json"):
        assert (case_dir / name).is_file(), f"{case_dir.name}: missing {name}"
    expected = json.loads((case_dir / "expected.json").read_text())
    expected_validator.validate(expected)
    assert expected["case_id"] == case_dir.name
    report = json.loads((case_dir / "golden-report.json").read_text())
    report_validator.validate(report)
    findings = report["findings"]
    assert expected["min_findings"] <= len(findings) <= expected["max_findings"], (
        f"{case_dir.name}: finding count"
    )
    if expected["finding_order"]:
        assert [f["id"] for f in findings] == expected["finding_order"], (
            f"{case_dir.name}: finding id order"
        )
    check_ranking(findings)
    for term in expected["forbidden_finding_title_terms"]:
        lower_term = term.lower()
        for finding in findings:
            assert lower_term not in finding["title"].lower(), (
                f"{case_dir.name}: forbidden term {term!r} in finding title"
            )
    if expected["requires_out_of_scope_section"]:
        notes = report.get("out_of_scope_notes") or []
        assert notes, f"{case_dir.name}: out_of_scope_notes required"
    if not expected["skill_should_apply"]:
        assert not findings, f"{case_dir.name}: skill_should_apply=false requires zero findings"


cases = sorted(p for p in CASES_ROOT.iterdir() if p.is_dir() and not p.name.startswith("."))
assert cases, "no evaluation cases found"
for case in cases:
    check_case(case)
print(f"PASS: {len(cases)} evaluation cases — fixtures, golden reports, ranking and scope expectations.")