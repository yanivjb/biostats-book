import re
LEAD = re.compile(r'^((?:[A-H]\)(?:\s*(?:,|and|–|-|to)\s*)?)+)\s*(.*)$')

def split_why_wrong(text):
    """Return ({letter: [explanations]}, [general notes])."""
    per, general = {}, []
    for line in [l.strip() for l in text.split('\n') if l.strip()]:
        m = LEAD.match(line)
        if not m:
            general.append(line); continue
        head, body = m.group(1), m.group(2)
        letters = re.findall(r'[A-H]', head)
        if re.search(r'[A-H]\)\s*(–|-|to)\s*[A-H]\)', head):
            a, b = re.findall(r'([A-H])\)\s*(?:–|-|to)\s*([A-H])\)', head)[0]
            letters = [chr(c) for c in range(ord(a), ord(b) + 1)] + letters
        for L in dict.fromkeys(letters):
            per.setdefault(L, []).append(body)
    return per, general
