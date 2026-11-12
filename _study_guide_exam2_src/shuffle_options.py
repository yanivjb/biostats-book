"""Reorder answer options so correct letters don't follow a pattern.
- AI variants (MC, select-all): random order, seeded by question id.
- All matching questions: random order, avoiding answers in straight A, B, C order.
- Skipped: original MC/select-all (instructor's order), TF, and option sets with a natural order.
Letter references like 'B)' in the explanation, why_wrong and hint are relabelled to match."""
import random, re

KEEP = re.compile(r"^(none of|all of|all four|all three|all of them|both of|both [a-z]+ and|neither|it depends|we can.t|can.t tell|"
                  r"not enough|cannot tell|only model|they.re the same)", re.I)
ORDINAL_WORDS = {'tiny', 'small', 'medium', 'large', 'very large', 'huge', 'not worth reporting'}

def parse(opts):
    return re.findall(r'^([A-H])\) (.*)$', opts, re.M)

def num(t):
    m = re.match(r'^[\s(≈~]*(?:About |Around )?(-?[\d.]+)', t.replace('−', '-'))
    return float(m.group(1)) if m else None

def ordered(items):
    texts = [t for _, t in items]
    if any(KEEP.search(t) for t in texts): return True
    nums = [num(t) for t in texts]
    if all(n is not None for n in nums) and len(set(nums)) == len(nums) and (nums == sorted(nums) or nums == sorted(nums, reverse=True)): return True
    if all(t.split('(')[0].strip().lower().replace('a ', '', 1).replace(' effect', '').strip() in ORDINAL_WORDS for t in texts): return True
    if len(texts) <= 2 and all(re.match(r'^(Yes|No)\b', t) for t in texts): return True
    return False

def relabel(text, m):
    return re.sub(r'(?<![A-Za-z0-9])([A-H])\)', lambda g: m.get(g.group(1), g.group(1)) + ')', text)

def shuffle_row(r):
    t = r['type']
    is_ai = bool(r.get('variant_of'))
    if t not in ('MC', 'select-all', 'matching'): return r
    if t in ('MC', 'select-all') and not is_ai: return r
    items = parse(r.get('options', ''))
    if len(items) < (2 if t == 'matching' else 3) or len(items) != len(r['options'].strip().split('\n')): return r
    if t != 'matching' and ordered(items): return r
    rng = random.Random(r['id'])
    letters = [k for k, _ in items]
    for _ in range(50):
        perm = letters[:]; rng.shuffle(perm)
        m = dict(zip(letters, perm))           # old letter -> new letter
        if t == 'matching':
            pairs = re.findall(r'(\d+)-([A-H])', r['answer'])
            new = [m[L] for _, L in pairs]
            if new != sorted(new) or len(set(new)) == 1: break
        else:
            break
    new_items = sorted(((m[k], txt) for k, txt in items))
    r = dict(r)
    r['options'] = '\n'.join(f'{k}) {txt}' for k, txt in new_items)
    if t == 'matching':
        r['answer'] = re.sub(r'(\d+)-([A-H])', lambda g: f'{g.group(1)}-{m[g.group(2)]}', r['answer'])
    else:
        r['answer'] = ', '.join(sorted(m[L] for L in re.findall(r'[A-H]', r['answer'])))
    for f in ('explanation', 'why_wrong', 'hint'):
        if r.get(f): r[f] = relabel(r[f], m)
    if t != 'matching' and r.get('why_wrong'):   # keep why-wrong lines in A, B, C order
        lines = r['why_wrong'].split('\n')
        if all(re.match(r'^[A-H]\)', l) for l in lines if l.strip()):
            r['why_wrong'] = '\n'.join(sorted(lines, key=lambda l: l[:1]))
    return r
