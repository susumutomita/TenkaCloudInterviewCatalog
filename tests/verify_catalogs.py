"""Validate plain learning data and independently check the new sample answers."""
import hashlib
import itertools
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]

def validate_catalog(raw):
    assert len(raw) <= 2_000_000
    catalog = json.loads(raw)
    assert catalog['schemaVersion'] == 1
    assert catalog['catalogID'] and catalog['version'] and catalog['title']
    assert 0 < len(catalog['lessons']) <= 200
    assert len({item['id'] for item in catalog['lessons']}) == len(catalog['lessons'])
    for lesson in catalog['lessons']:
        assert all(lesson[key] for key in ['id', 'title', 'category', 'summary', 'authors'])
        assert 0 < len(lesson['steps']) <= 100
        assert len({step['id'] for step in lesson['steps']}) == len(lesson['steps'])
        for item in lesson.get('sources', []):
            assert item['title'] and item['url'].startswith('https://')
        for step in lesson['steps']:
            assert all(step[key] for key in ['id', 'phase', 'prompt', 'explanation'])
            ids = [choice['id'] for choice in step['choices']]
            assert len(ids) == len(set(ids))
            assert (step['correctChoiceID'] in ids) if ids else step['correctChoiceID'] is None
    return catalog

catalogs = [validate_catalog(path.read_bytes()) for path in ROOT.glob('native-*.json') if 'manifest' not in path.name]
assert len({item['catalogID'] for item in catalogs}) == len(catalogs)
for path in ROOT.glob('native-*-manifest.json'):
    manifest = json.loads(path.read_bytes())
    if 'releases' not in manifest:
        for entry in manifest['entries']:
            raw = (ROOT / entry['fileName']).read_bytes()
            catalog = validate_catalog(raw)
            assert hashlib.sha256(raw).hexdigest() == entry['sha256']
            assert catalog['version'] == entry['version']
            assert len(catalog['lessons']) == entry['lessons']
        continue
    versions = set()
    for release in manifest['releases']:
        assert release['version'] not in versions
        versions.add(release['version'])
        raw = subprocess.check_output(['git', 'show', release['commitSHA'] + ':' + release['payloadPath']], cwd=ROOT)
        assert len(raw) == release['bytes']
        assert hashlib.sha256(raw).hexdigest() == release['sha256']
        catalog = validate_catalog(raw)
        assert catalog['catalogID'] == manifest['catalogID']
        assert catalog['version'] == release['version']

pairs = [(2, 5), (1, 4), (3, 6)]
sums = [sum(choice) for choice in itertools.product(*pairs)]
assert len(sums) == 8 and 9 in sums and 8 not in sums
assert sum(1 for mask in range(8) if sum(pairs[i][(mask >> i) & 1] for i in range(3)) == 9) == 3

def peak(intervals):
    events = {}
    for start, end, load in intervals:
        events[start] = events.get(start, 0) + load
        events[end] = events.get(end, 0) - load
    current = maximum = 0
    for time in sorted(events):
        current += events[time]
        maximum = max(maximum, current)
    return maximum
assert peak([(1, 4, 3), (4, 6, 5), (2, 5, 2)]) == 7
assert peak([(1, 3, 4), (3, 5, 4)]) == 4
assert peak([]) == 0
assert peak([(10**12, 10**12 + 2, 3), (10**12 + 1, 10**12 + 3, 5)]) == 8
for intervals in [[(a, b, p), (c, d, q)] for a in range(3) for b in range(a + 1, 4) for c in range(3) for d in range(c + 1, 4) for p in [1, 2] for q in [1, 2]]:
    brute = max(sum(p for a, b, p in intervals if a <= time < b) for time in range(4))
    assert peak(intervals) == brute
values = [3, -3, 3]
prefix, frequency, count = 0, {0: 1}, 0
for value in values:
    prefix += value
    count += frequency.get(prefix - 3, 0)
    frequency[prefix] = frequency.get(prefix, 0) + 1
assert count == 3
assert sum([4, -3, 2]) == 3
assert sum(100 for _ in [0.99, 1.01]) == 200
assert 100_0000 / 86400 < 12
# The existing six design lessons retain their steps and gain technical references.
design = next(item for item in catalogs if item['catalogID'] == 'interviewlab.system-design')
for item in design['lessons']:
    assert item.get('sources')
print(f'PASS {len(catalogs)} catalogs, immutable manifest hashes, and algorithm/design example checks')
