#!/usr/bin/env python3
"""Scoped consumer verification; never discovers or executes the full corpus."""
import argparse, hashlib, json, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def read(rel):
    return json.loads((ROOT / rel).read_text())
def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--law', default='law')
    args = ap.parse_args()
    for manifest in ['source-pin.json', 'CANON-MANIFEST.json']:
        for row in read(manifest)['files']:
            raw = (ROOT / row['path']).read_bytes()
            assert len(raw) == row['size'], row['path']
            assert 'sha256:' + hashlib.sha256(raw).hexdigest() == row['sha256'], row['path']
    for model in read('source-pin.json')['models']:
        for flavor, expected in model['hashes'].items():
            path = f"registry/{flavor}/{model['name']}.lawir.json"
            raw = (ROOT / path).read_bytes()
            assert 'sha256:' + hashlib.sha256(raw).hexdigest() == expected, path
            ir = json.loads(raw)
            assert ir['package']['name'] == model['name'], path
            assert ir['package']['version'] == model['version'], path
        own = read(f"registry/package/{model['name']}.lawir.json")
        assert all(n['package'] == model['namespace'] for n in own['nodes']), model['name']
    for row in read('examples/index.json'):
        folder = ROOT / 'examples' / row['name']
        expected = json.loads((folder / 'result.json').read_text())
        for _ in range(2):
            actual = json.loads(subprocess.check_output([args.law, 'eval', str(folder)], text=True))
            assert actual == expected, row['name'] + ': canonical replay differs'
        ex = row['expected']
        q = expected['results'][0]
        if 'truth' in ex: assert q['truthStatus'] == ex['truth'], row['name']
        if 'evaluation' in ex: assert q['evaluationStatus'] == ex['evaluation'], row['name']
        if 'rule' in ex:
            assert any(n.get('rule') == ex['rule'] for n in expected['proofGraph']['nodes']), row['name']
            node = next(n for n in json.loads((folder / 'request.json').read_text())['ir']['nodes'] if n['id'] == ex['rule'])
            assert ex['anchor'] in node.get('anchors', []), row['name']
        print('REPLAY PASS', row['name'], expected['resultHash'])
    folder = ROOT / 'collections/imprevision-force-majeure'
    actual = json.loads(subprocess.check_output([args.law, 'ask', str(folder), '--case', 'PrixEnHausse', '--query-json', str(folder/'queries/renegociation-ouverte.json'), '--format', 'json'], text=True))
    assert actual == read('examples/renegociation-ouverte/result.json'), 'native ask differs'
    inspect = json.loads(subprocess.check_output([args.law, 'inspect', str(ROOT/'examples/renegociation-ouverte/result.json'), 'summary'], text=True))
    assert inspect['ok'], 'inspection failed'
    print('PASS: 21 model identities/hashes; 17 examples twice; native ask and inspect; no corpus run')
if __name__ == '__main__': main()
