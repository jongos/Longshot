"""Development-only schema/example checks. Requires jsonschema, not a skill runtime."""
import copy
import json
from pathlib import Path
from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / 'skills/longshot-human-centered-ui/references/report-schema.json').read_text())
Draft202012Validator.check_schema(SCHEMA)
validator = Draft202012Validator(SCHEMA)
bundle = ROOT / 'examples/synthetic-evidence-bundle'
runs = [json.loads((bundle / f'run-00{i}.json').read_text()) for i in (1, 2)]

def references(report):
    evidence_ids = [e['id'] for e in report['evidence']]
    assert len(set(evidence_ids)) == len(evidence_ids), 'duplicate evidence IDs'
    finding_ids = [f['id'] for f in report['findings']]
    assert len(set(finding_ids)) == len(finding_ids), 'duplicate finding IDs'
    def walk(value):
        if isinstance(value, dict):
            for key, child in value.items():
                if key == 'evidence_ids':
                    assert set(child) <= set(evidence_ids), 'dangling evidence reference'
                walk(child)
        elif isinstance(value, list):
            for child in value: walk(child)
    walk(report)
    for item in report['evidence']:
        path, _, fragment = item['locator'].partition('#')
        artifact = bundle / path
        assert artifact.is_file(), 'missing artifact'
        if fragment:
            headings = [line[3:].lower().replace(':', '').replace(' ', '-') for line in artifact.read_text().splitlines() if line.startswith('## ')]
            assert fragment in headings, 'missing artifact anchor'

for run in runs:
    validator.validate(run)
    references(run)
assert {c['finding_id'] for c in runs[1]['comparisons']} == {f['id'] for f in runs[0]['findings']}
assert all(c['prior_run_id'] == runs[0]['run_id'] for c in runs[1]['comparisons'])

def rejected(report):
    try: validator.validate(report)
    except ValidationError: return
    raise AssertionError('invalid export accepted')

bad = copy.deepcopy(runs[1]); bad['comparisons'][0]['status'] = 'verified_resolved'; rejected(bad)
good = copy.deepcopy(runs[1]); c = good['comparisons'][0]; c['status'] = 'verified_resolved'; c['comparable'] = True
for name in ('acceptance_check', 'original_obstacle_check', 'preserved_behavior_check'):
    c[name] = {'result': 'passed', 'evidence_ids': ['E-003'], 'detail': 'Structural test only; not an actual resolved finding.'}
validator.validate(good)  # Schema cannot prove evidence relevance; this is not published as a result.
bad = copy.deepcopy(good); bad['comparisons'][0]['preserved_behavior_check']['evidence_ids'] = []; rejected(bad)
bad = copy.deepcopy(runs[0]); bad['schema_version'] = '2.0.0'; rejected(bad)
bad = copy.deepcopy(runs[0]); bad['capabilities'][0]['coverage'] = 'available'; rejected(bad)
bad = copy.deepcopy(runs[0]); bad['findings'][0]['evidence_ids'] = ['missing']
try: references(bad)
except AssertionError: pass
else: raise AssertionError('dangling reference accepted')
print('PASS: two examples, artifact/reference integrity, prior-finding coverage, resolution evidence gates, version and coverage negatives.')
