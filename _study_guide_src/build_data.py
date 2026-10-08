"""Build study_guide/bank.json and study_guide/open_ended.json from the two banks.

Run from the folder that holds question_bank.csv, open_ended_bank.md and bank_images/:
    python3 build_data.py OUTPUT_DIR
"""
import base64, csv, json, os, re, shutil, sys, textwrap
from parse_wrong import split_why_wrong

OUT = sys.argv[1] if len(sys.argv) > 1 else 'study_guide'
KEY = 'clarkia'

CHAPTERS = {
    0: 'Types of variables', 1: 'Getting started with R', 2: 'Intro to ggplot', 3: 'Reproducible science',
    4: 'Data in R', 5: 'Univariate summaries', 6: 'Associations I', 7: 'Associations II',
    8: 'Sampling', 9: 'Uncertainty', 10: 'Hypothesis testing (NHST)', 11: 'Shuffling (permutation)',
    12: 'Study design',
}

# Topic tags in the bank -> one cleaned list of concepts per chapter.
CONCEPTS = {
    0: {'Variable types': ['variable types'], 'Explanatory & response variables': ['modeling choices']},
    1: {'R basics': ['R basics', 'vectors'], 'Assignment & the environment': ['assignment & environment'],
        'Functions, pipes & packages': ['packages', 'pipes & functions'], 'Errors & debugging': ['errors & debugging'],
        'Scripts & reproducibility': ['scripts', 'scripts & reproducibility'], 'Learning R': ['learning R']},
    2: {'Plot design principles': ['data viz principles', 'honest plots'],
        'Aesthetics & ggplot layers': ['aesthetics', 'ggplot layers', 'ggplot basics'],
        'Visualizing associations': ['associations']},
    3: {'Reproducible workflows': ['reproducibility', 'scripts', 'file paths', 'loading data', 'packages'],
        'Data entry & data dictionaries': ['data dictionaries', 'data entry', 'variable types', 'data in R'],
        'Missing data & bias': ['missing data', 'sampling bias']},
    4: {'Tidy data': ['tidy data'], 'dplyr verbs': ['data in R', 'dplyr verbs', 'pipes', 'cleaning names'],
        'Assignment & the environment': ['assignment & environment'], 'Errors & debugging': ['errors & debugging', 'packages']},
    5: {'Shape of distributions': ['shape of distributions', 'histograms', 'transformations'],
        'Center: mean & median': ['mean & median', 'mean', 'robust summaries', 'missing data (NA)'],
        'Spread: variance & SD': ['variance', 'sums of squares', 'standard deviation', 'sample size'],
        'Range, IQR & boxplots': ['range & IQR', 'boxplots'], 'Coefficient of variation': ['coefficient of variation'],
        'Summaries in R': ['summarize', 'assignment & environment', 'errors & debugging', 'dplyr verbs']},
    6: {'Two categorical variables': ['two categorical variables', 'bar charts', 'conditional proportions', 'joint proportions'],
        "Difference in means & Cohen's d": ['difference in means', "Cohen's d", 'one categorical one continuous', 'confidence intervals'],
        'Visualizing associations': ['visualizing associations', 'boxplots', 'jitter', 'histograms', 'density plots', 'facets'],
        'Association vs causation': ['interpreting associations', 'correlation vs causation']},
    7: {'Covariance': ['covariance', 'variance', 'joint proportions', 'independence', 'multiplication rule', "Bessel's correction"],
        'Correlation': ['correlation', 'scatterplots', 'linear vs nonlinear association', 'outliers'],
        'Association vs causation': ['correlation vs causation', 'interpreting associations', 'causation', 'experimental design', 'confounding']},
    8: {'Samples, populations & estimates': ['estimates vs parameters', 'samples vs populations', 'parameters vs estimates', 'population', 'population distribution'],
        'Sampling distribution': ['sampling distribution', 'uncertainty'],
        'SD vs SE': ['standard deviation', 'standard error', 'sample size'],
        'Sampling error vs bias': ['sampling error', 'sampling bias', 'random sampling'],
        'Non-independence': ['non-independence', 'sampling design'],
        'Shape of distributions': ['shape of distributions', 'histograms']},
    9: {'Sampling distribution & SE': ['sampling distribution', 'standard error', 'sampling error', 'uncertainty', 'standard deviation', 'sample size'],
        'Bootstrap': ['bootstrap', 'shape of distributions', 'histograms'],
        'Confidence intervals': ['confidence intervals', 'interpretation', 'coverage', "Cohen's d"],
        'Visualizing uncertainty': ['visualizing uncertainty', 'variability', 'error bars']},
    10: {'Null & alternative hypotheses': ['null and alternative hypotheses', 'two-tailed tests', 'one- vs two-tailed tests'],
         'What a p-value means': ['p-values', 'interpretation', "prosecutor's fallacy", 'null distribution', 'hypothesis testing decisions', 'confidence intervals', 'hypothesis tests'],
         'Errors, power & sample size': ['type I error', 'type II error', 'alpha', 'power', 'sample size', 'publication bias', 'effect size'],
         'Confounding & non-independence': ['confounding', 'interpreting results', 'non-independence', 'assumptions', 'correlation vs causation']},
    11: {'Bootstrap vs permutation': ['permutation', 'bootstrap', 'null distribution'],
         'Permutation p-values': ['p-values', 'hypothesis testing decisions', 'reporting', 'null and alternative hypotheses'],
         'Bootstrap CIs': ['confidence intervals', 'correlation', 'scatterplots', 'associations', 'interpretation'],
         'Non-independence & blocking': ['non-independence', 'blocking', 'assumptions']},
    12: {'Experiments vs observational studies': ['experimental design', 'random assignment', 'observational studies', 'causation', 'reverse causation', 'causal inference', 'natural experiments', 'predictions', 'counterfactuals', 'correlation vs causation', 'spurious correlation', 'confounding', 'sampling error'],
         'Controls & placebos': ['controls', 'placebo'],
         'Power & precision': ['power', 'power and precision', 'blocking', 'matching', 'non-significant results'],
         'Validity': ['internal validity', 'external validity', 'ecological validity', 'dose', 'sampling bias', 'measurement'],
         'The language of causation': ['effect size', 'response variable', 'scientific vs statistical models']},
}

# Accepted ranges for numeric questions: (label, low, high, shown answer).
NUMERIC = {
    'ch04-book-05': [('', 7, 7, '7')],
    'ch05-quiz-04': [('', 401, 403, '402')],
    'ch05-quiz-05': [('', 200, 202, '201')],
    'ch05-gquiz-05': [('', 0.06, 0.08, '≈ 0.07')],
    'ch05-book-08': [('', 0.0197, 0.0237, '0.0217')],
    'ch05-book-09': [('variance', 0.0066, 0.0078, '≈ 0.0072'), ('SD', 0.075, 0.095, '≈ 0.085')],
    'ch06-hw-04': [('a) difference (kg/capita)', 0.90, 1.10, '≈ 0.97'), ("b) Cohen's d", 0.28, 0.36, '≈ 0.32')],
    'ch07-gquiz-04': [('', 0.078, 0.088, '1/12 ≈ 0.083')],
    'ch07-hw-01': [('', 0.255, 0.265, '≈ 0.260')],
    'ch07-hw-02': [('', -0.0125, -0.0085, '≈ −0.0104')],
    'ch07-hw-03': [('', 0.34, 0.38, '≈ 0.36')],
    'ch07-book-03': [('a) expected', 0.160, 0.166, '≈ 0.163'), ('b) observed − expected', 0.208, 0.214, '≈ 0.211')],
    'ch07-book-04': [('', 0.2122, 0.2140, '≈ 0.213')],
    'ch10-hw-05': [('', 0.17, 0.19, '≈ 0.18')],
    'ch10-book-04': [('', 0.037, 0.043, '≈ 0.04')],
}

NUMERIC.update({
    'ch10-hw-05-v1': [('', 0.17, 0.19, '≈ 0.18')],
    'ch10-hw-05-v2': [('', 0.10, 0.12, '≈ 0.11')],
    'ch10-book-04-v1': [('', 0.020, 0.024, '≈ 0.022')],
    'ch10-book-04-v2': [('', 0.037, 0.043, '≈ 0.04')],
    'ch06-hw-04-v1': [('a) difference (mm)', 3.8, 4.0, '≈ 3.91'), ("b) Cohen's d", 1.55, 1.69, '≈ 1.62')],
    'ch06-hw-04-v2': [('', 0.74, 0.76, '0.75')],
    'ch07-gquiz-04-v1': [('', 0.085, 0.095, '0.09')],
    'ch07-gquiz-04-v2': [('', -0.001, 0.001, '0')],
    'ch07-hw-01-v1': [('', 0.195, 0.205, '0.20')],
    'ch07-hw-01-v2': [('', 0.135, 0.145, '0.14')],
    'ch07-hw-02-v1': [('', 0.095, 0.105, '0.10')],
    'ch07-hw-02-v2': [('', 0.155, 0.165, '0.16')],
    'ch07-hw-03-v1': [('', 0.59, 0.61, '0.6')],
    'ch07-hw-03-v2': [('', -0.61, -0.59, '−0.6')],
    'ch07-book-03-v1': [('a) expected', 0.135, 0.145, '0.14'), ('b) observed − expected', 0.155, 0.165, '0.16')],
    'ch07-book-03-v2': [('', 0.073, 0.077, '0.075')],
    'ch07-book-04-v1': [('', 0.1612, 0.1620, '≈ 0.162')],
    'ch07-book-04-v2': [('', 0.0752, 0.0756, '≈ 0.0754')],
    'ch05-quiz-04-v1': [('', 61.5, 62.5, '62')],
    'ch05-quiz-04-v2': [('', 25.5, 26.5, '26')],
    'ch05-quiz-05-v1': [('', 30.5, 31.5, '31')],
    'ch05-quiz-05-v2': [('', 2.95, 3.05, '3')],
    'ch05-gquiz-05-v1': [('', 24.0, 24.7, '≈ 24.33')],
    'ch05-gquiz-05-v2': [('', 3.75, 3.87, '≈ 3.81')],
    'ch05-book-08-v1': [('', 0.0245, 0.0255, '0.025')],
    'ch05-book-08-v2': [('', 7.9, 8.1, '8')],
    'ch05-book-09-v1': [('variance', 0.0080, 0.0087, '≈ 0.0083'), ('SD', 0.088, 0.094, '≈ 0.091')],
    'ch05-book-09-v2': [('variance', 3.95, 4.05, '4'), ('SD', 1.98, 2.02, '2')],
    'ch04-book-05-v1': [('', 22.1, 22.1, '22.1')],
    'ch04-book-05-v2': [('', 5, 5, '5')],
})

# Open-ended prompt -> concepts (must match CONCEPTS of its chapter).
OPEN_CONCEPTS = {
    'O-00-01': ['Variable types', 'Explanatory & response variables'],
    'O-01-01': ['R basics', 'Functions, pipes & packages'], 'O-01-02': ['Assignment & the environment', 'Scripts & reproducibility'],
    'O-01-03': ['Errors & debugging', 'Functions, pipes & packages'],
    'O-04-01': ['dplyr verbs', 'Assignment & the environment'], 'O-04-02': ['Tidy data'],
    'O-02-01': ['Plot design principles'], 'O-02-02': ['Plot design principles'], 'O-02-03': ['Plot design principles', 'Visualizing associations'],
    'O-02-04': ['Plot design principles'],
    'O-03-01': ['Reproducible workflows'], 'O-03-02': ['Missing data & bias', 'Data entry & data dictionaries'],
    'O-05-01': ['Range, IQR & boxplots', 'Center: mean & median'], 'O-05-02': ['Coefficient of variation'],
    'O-05-03': ['Summaries in R'], 'O-05-04': ['Spread: variance & SD'], 'O-05-05': ['Shape of distributions', 'Center: mean & median'],
    'O-05-06': ['Spread: variance & SD'],
    'O-06-01': ["Difference in means & Cohen's d"], 'O-06-02': ['Two categorical variables'],
    'O-07-01': ['Covariance'], 'O-07-02': ['Covariance'], 'O-07-03': ['Correlation'], 'O-07-04': ['Covariance', 'Correlation'],
    'O-07-05': ['Covariance'], 'O-07-06': ['Association vs causation', 'Correlation'], 'O-07-07': ['Correlation'],
    'O-08-01': ['SD vs SE', 'Sampling distribution'], 'O-08-02': ['Sampling error vs bias'], 'O-08-03': ['Sampling error vs bias'],
    'O-08-04': ['Non-independence', 'Sampling error vs bias'], 'O-08-05': ['Sampling error vs bias', 'Non-independence'],
    'O-08-06': ['Sampling error vs bias'], 'O-08-07': ['SD vs SE'], 'O-08-08': ['Non-independence'],
    'O-09-01': ['Sampling distribution & SE'], 'O-09-02': ['Bootstrap'], 'O-09-03': ['Bootstrap'], 'O-09-04': ['Confidence intervals'],
    'O-09-05': ['Bootstrap'], 'O-09-06': ['Visualizing uncertainty'], 'O-09-07': ['Confidence intervals'],
    'O-09-08': ['Visualizing uncertainty', 'Confidence intervals'], 'O-09-09': ['Confidence intervals'],
    'O-10-01': ['Errors, power & sample size'], 'O-10-02': ['Errors, power & sample size'],
    'O-10-03': ['What a p-value means', 'Errors, power & sample size'], 'O-10-04': ['What a p-value means'],
    'O-10-05': ['What a p-value means'], 'O-10-06': ['Errors, power & sample size'], 'O-10-07': ['Null & alternative hypotheses'],
    'O-11-01': ['Bootstrap vs permutation'], 'O-11-02': ['Permutation p-values'], 'O-11-03': ['Non-independence & blocking'],
    'O-12-01': ['Experiments vs observational studies'], 'O-12-02': ['Power & precision'], 'O-12-03': ['Validity'],
    'O-12-04': ['Controls & placebos'], 'O-12-05': ['Power & precision'], 'O-12-06': ['Experiments vs observational studies'],
}
OPEN_CHAPTER_OVERRIDE = {'O-06-01': 6, 'O-06-02': 6}
# The open-ended bank is written for the tutor bot ("Show `plot.png` ..."). On the website the
# image appears under the prompt, so these prompts are reworded to address the student directly.
STUDENT_PROMPT = {
    'O-02-02': ("The figure below shows the same data as small multiples in two layouts, A and B. "
                "Which layout do you prefer for comparing the groups, and why?", ['ch02-chimein-02.png']),
    'O-05-01': ("Look at the boxplot below. Can you estimate the mean from a boxplot? "
                "What can and can't a boxplot tell you?", ['ch05-quiz-boxplot.png']),
    'O-07-06': ("Across 27 countries, chocolate consumption and number of Nobel laureates have r ≈ 0.36 (scatterplot below). "
                "Without the USA, UK and Germany, r ≈ −0.06. Does chocolate make people smarter? "
                "What else could explain this pattern?", ['ch07-hw-choc-nobel-scatter.png']),
    'O-07-07': ("Look at the four scatterplots below. In panel b, y is a perfect wave-shaped function of x, yet r ≈ 0. "
                "Explain how that's possible. What does a correlation coefficient tell you, and what doesn't it tell you?",
                ['ch07-hw-fourpanels.png']),
    'O-08-02': ("I estimated mean human gene length by picking random nucleotides from the genome and recording the length "
                "of the gene each one landed in, until I had 50 genes. I repeated this 1000 times. The plot below shows my "
                "1000 estimates: every one is far above the true mean (2.62 kb). Explain why, and how you would fix it.",
                ['ch08-book-biased-sampdist.png']),
    'O-09-06': ("The two plots below show the same data. Plot A shows means with error bars over the raw points; "
                "Plot B shows boxplots over the raw points. Which do you prefer, and why?", ['ch09-gquiz-astrology-plots.png']),
    'O-09-07': ("People often say a 95% CI has \"a 95% chance of capturing the true parameter.\" Statisticians prefer: "
                "\"95% of confidence intervals from samples of a population will include the true parameter.\" "
                "The cartoon below (by Ellie Murray, @epiellie) compares archery with ring toss. What's the difference "
                "between the two statements? Does it matter? Is it worth policing?", ['ch09-gquiz-ringtoss.png']),
    'O-10-05': ("The plot below shows the probability of each number of correct guesses (out of 9) if mothers were just guessing. "
                "In the real study, 8 of 9 mothers picked their own child's shirt (p ≈ 0.04). In the homework version, 7 of 9 did "
                "(p ≈ 0.18). For each version: what do you conclude about the null, and what can't you conclude? "
                "If 7 of 9 is \"not significant,\" does that mean mothers can't identify their children by smell?",
                ['ch10-smell-null-dist.png']),
    'O-11-02': ("In the line-up below, one panel is the real data and the other 19 were made by shuffling the labels. "
                "If you can reliably pick out the real one, what does that say about the p-value? "
                "What would it mean if you couldn't?", ['ch11-chime-lineup.png']),
}

MIN_WORDS = {'O-07-01': 25, 'O-07-02': 25, 'O-07-03': 25, 'O-10-07': 30, 'O-02-01': 25}


def scramble(s):
    b = s.encode('utf-8')
    k = KEY.encode()
    return base64.b64encode(bytes(c ^ k[i % len(k)] for i, c in enumerate(b))).decode()


def parse_options(text):
    opts = []
    for line in text.split('\n'):
        m = re.match(r'^([A-H])\) (.*)$', line.strip())
        if m:
            opts.append({'key': m.group(1), 'text': m.group(2)})
        elif opts and line.strip():
            opts[-1]['text'] += ' ' + line.strip()
    return opts


def concepts_for(chapter, topics):
    cmap = CONCEPTS[chapter]
    found = []
    for t in [t.strip() for t in topics.split(',') if t.strip()]:
        for c, tags in cmap.items():
            if t in tags and c not in found:
                found.append(c)
    return found


def build_bank():
    rows = [x for x in csv.DictReader(open('question_bank.csv', encoding='utf-8')) if x['include'] == 'yes']
    out, problems = [], []
    for x in rows:
        chapters = [int(c) for c in x['chapter'].split(',')]
        concepts = []
        for ch in chapters:
            concepts += [c for c in concepts_for(ch, x['topics']) if c not in concepts]
        if not concepts:
            problems.append(('no concept', x['id'], x['topics']))
        t = x['type']
        q = {'id': x['id'], 'source': x['source'], 'chapters': chapters, 'concepts': concepts,
             'type': {'MC': 'mc', 'TF': 'tf', 'select-all': 'multi', 'matching': 'match',
                      'numeric': 'numeric', 'short answer': 'short'}[t],
             'question': x['question'], 'hint': x['hint'],
             'images': [i.strip() for i in x['image'].split(';') if i.strip()],
             'reveals': x['reveals_answer_to'] or None, 'variant_of': x.get('variant_of') or None}
        secret = {'explanation': x['explanation']}
        if t in ('MC', 'TF', 'select-all', 'matching'):
            q['options'] = parse_options(x['options'])
            if not q['options']:
                problems.append(('no options', x['id']))
        if t in ('MC', 'TF', 'select-all'):
            secret['answer'] = re.findall(r'[A-H]', x['answer'])
            per, general = split_why_wrong(x['why_wrong'])
            secret['why'] = per
            secret['general'] = general
        elif t == 'matching':
            pairs = re.findall(r'(\d+)-([A-H])', x['answer'])
            secret['answer'] = {n: L for n, L in pairs}
            q['items'] = [n for n, _ in pairs]
            secret['general'] = [l for l in x['why_wrong'].split('\n') if l.strip()]
        elif t == 'numeric':
            spec = NUMERIC.get(x['id'])
            if not spec:
                problems.append(('no numeric spec', x['id']))
                spec = []
            q['parts'] = [s[0] for s in spec]
            secret['ranges'] = [[s[1], s[2]] for s in spec]
            secret['shown'] = x['answer']
            secret['general'] = [l for l in x['why_wrong'].split('\n') if l.strip()]
        else:
            secret['shown'] = x['answer']
            secret['general'] = [l for l in x['why_wrong'].split('\n') if l.strip()]
        q['secret'] = scramble(json.dumps(secret, ensure_ascii=False))
        out.append(q)
    return out, problems


def build_open():
    md = open('open_ended_bank.md', encoding='utf-8').read()
    body = md.split('## Notes for the instructor')[0]
    entries = re.split(r'\n(?=### O-)', body)
    out, problems = [], []
    for e in entries:
        m = re.match(r'### (O-(\d\d)-\d\d) · (.+)', e)
        if not m:
            continue
        oid, ch, title = m.group(1), int(m.group(2)), m.group(3).strip()
        ch = OPEN_CHAPTER_OVERRIDE.get(oid, ch)
        fields = {}
        for fm in re.finditer(r'^- \*\*(.+?):\*\*(.*?)(?=^- \*\*|\Z)', e, re.M | re.S):
            first, _, rest = fm.group(2).partition('\n')
            rest = textwrap.dedent(rest).strip('\n')
            fields[fm.group(1)] = ((first.strip() + '\n' + rest) if first.strip() else rest).strip()
        prompt = fields.get('Prompt', '')
        imgs = re.findall(r'`([\w\-]+\.png)`', prompt)
        hints = [re.sub(r'^\s*\d+\.\s*', '', h).strip() for h in fields.get('Hints', '').split('\n') if h.strip()]
        if oid in STUDENT_PROMPT:
            prompt, imgs = STUDENT_PROMPT[oid]
        elif '.png`' in prompt:
            problems.append(('prompt mentions an image file but has no student wording', oid))
        item = {'id': oid, 'chapters': [ch], 'title': title,
                'concepts': OPEN_CONCEPTS.get(oid, []),
                'source': fields.get('Source', ''), 'prompt': prompt, 'images': imgs,
                'hints': hints, 'min_words': MIN_WORDS.get(oid, 40)}
        secret = {'key': fields.get('Key ideas', ''), 'good': fields.get('Good enough when', ''),
                  'pitfalls': fields.get('What could go wrong', '')}
        item['secret'] = scramble(json.dumps(secret, ensure_ascii=False))
        for c in item['concepts']:
            if c not in CONCEPTS[ch]:
                problems.append(('bad open concept', oid, c))
        if not item['concepts']:
            problems.append(('no open concept', oid))
        out.append(item)
    return out, problems


if __name__ == '__main__':
    os.makedirs(os.path.join(OUT, 'images'), exist_ok=True)
    bank, p1 = build_bank()
    opens, p2 = build_open()
    meta = {'chapters': {str(k): {'name': v, 'concepts': list(CONCEPTS[k])} for k, v in CHAPTERS.items()}}
    used = set()
    for q in bank + opens:
        used.update(q['images'])
    for img in sorted(used):
        shutil.copy(os.path.join('bank_images', img), os.path.join(OUT, 'images', img))
    with open(os.path.join(OUT, 'data.js'), 'w', encoding='utf-8') as f:
        f.write('window.STUDY_DATA = ')
        json.dump({'meta': meta, 'bank': bank, 'open': opens}, f, ensure_ascii=False)
        f.write(';\n')
    print(f'{len(bank)} questions, {len(opens)} open-ended prompts, {len(used)} images')
    for p in p1 + p2:
        print('PROBLEM', p)
