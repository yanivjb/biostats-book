"""Collect rows_chNN.py files into question_bank_exam2.csv (same columns as the Exam 1 bank)."""
import csv, glob, importlib.util, re, sys
COLS = ['id','source','chapter','topics','type','question','options','answer','explanation','why_wrong','hint','image','include','near_duplicate_of','flags','drafted_by_claude','reveals_answer_to','variant_of']
rows = []
import sys; sys.path.insert(0, '.')
files = sorted(glob.glob('rows_ch*.py'))
files = [f for f in files if not f.endswith('_ai.py')] + [f for f in files if f.endswith('_ai.py')]
orig = {}
for f in files:
    spec = importlib.util.spec_from_file_location(f[:-3], f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for r in m.ROWS:
        r = dict(r)
        if r.get('variant_of'):
            o = orig[r['variant_of']]
            for k in ('topics', 'chapter'): r.setdefault(k, o[k])
            if 'type' not in r:
                a = r['answer'].strip()
                if re.match(r'^\d+-[A-H]', a): r['type'] = 'matching'
                elif not r.get('options'): r['type'] = 'numeric'
                elif r['options'].startswith('A) TRUE'): r['type'] = 'TF'
                elif ',' in a: r['type'] = 'select-all'
                elif o['type'] == 'select-all': r['type'] = 'select-all'
                else: r['type'] = 'MC'
        else:
            orig[r['id']] = r
        r['chapter'] = r.get('chapter') or str(int(re.match(r'ch(\d+)', r['id']).group(1)))
        r.setdefault('include', 'yes')
        r.pop('flags', None)
        if not r.get('variant_of'): r.pop('drafted_by_claude', None)
        bad = set(r) - set(COLS)
        assert not bad, (r['id'], bad)
        if r['type'] in ('MC','select-all','matching','TF'): assert r.get('options'), r['id']
        rows.append(r)
from shuffle_options import shuffle_row
rows = [shuffle_row(r) for r in rows]
ids = [r['id'] for r in rows]; assert len(ids) == len(set(ids)), 'duplicate ids'
with open('question_bank_exam2.csv', 'w', newline='') as fh:
    w = csv.DictWriter(fh, COLS); w.writeheader(); [w.writerow(r) for r in rows]
from collections import Counter
print(len(rows), 'rows'); print(Counter((r['chapter'], r['type']) for r in rows))
