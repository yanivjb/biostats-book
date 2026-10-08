"""Build the tutor bot's knowledge files from question_bank.csv and open_ended_bank.md.
Figures are linked to their published copies on the course site, so the bot can hand students a link."""
import ast, collections, csv, os, re

FIG_BASE = "https://yanivjb.github.io/biostats-book/study_guide/images/"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
src = open(os.path.join(ROOT, "sg", "build_data.py"), encoding="utf-8").read()
tree = ast.parse(src)
CONCEPTS = next(ast.literal_eval(n.value) for n in tree.body
                if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "CONCEPTS")
NAMES = {0: "Types of variables", 1: "Getting started with R", 2: "ggplot", 3: "Reproducible science", 4: "Data in R",
         5: "Univariate summaries", 6: "Associations I", 7: "Associations II", 8: "Sampling", 9: "Uncertainty",
         10: "Null hypothesis significance testing", 11: "Shuffling (permutation)", 12: "Study design"}

rows = [r for r in csv.DictReader(open(os.path.join(ROOT, "question_bank.csv"), encoding="utf-8")) if r["include"] == "yes"]
by_id = {r["id"]: r for r in rows}

def chapters(r): return [int(c) for c in re.findall(r"\d+", r["chapter"])]
def concepts(r):
    tags = {t.strip() for t in r["topics"].split(",")}
    out = []
    for ch in chapters(r):
        out += [name for name, t in CONCEPTS.get(ch, {}).items() if tags & set(t)]
    return out or ["(general)"]

def block(r):
    root = r["variant_of"] or r["id"]
    kind = "AI-written version of " + root if r["variant_of"] else "Course original"
    lines = [f"### {r['id']}", f"- **Kind:** {kind}", f"- **Concepts:** {'; '.join(concepts(r))}",
             f"- **Type:** {r['type']}"]
    figs = [n.strip() for n in r["image"].split(";") if n.strip()]
    if figs:
        lines.append("- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: "
                     + ", ".join(f"[{n}]({FIG_BASE}{n})" for n in figs))
    lines += ["- **Question:**", "", r["question"].strip(), ""]
    if r["options"].strip():
        lines += ["- **Options:**", ""] + ["  " + o for o in r["options"].strip().split("\n")] + [""]
    lines += [f"- **Answer (tutor only):** {r['answer'].strip()}",
              f"- **Explanation (tutor only):** {r['explanation'].strip()}"]
    if r["why_wrong"].strip():
        lines += ["- **Why the wrong options are wrong (tutor only):**"] + ["  " + l for l in r["why_wrong"].strip().split("\n") if l.strip()]
    if r["hint"].strip():
        lines.append(f"- **Hint:** {r['hint'].strip()}")
    return "\n".join(lines) + "\n"

fig = [r for r in rows if r["image"].strip()]
groups = collections.defaultdict(list)
for r in rows:
    groups[chapters(r)[-1] if len(chapters(r)) > 1 else chapters(r)[0]].append(r)

out = ["# Applied Biostats tutor: question bank (Exam 1, chapters 0–12)", "",
       "Knowledge file for the course tutor. Each question has an ID, its concepts, the question, options, the answer, "
       "an explanation, why each wrong option is wrong, and a hint. Fields marked **tutor only** must never be shown "
       "to the student before they have answered.", "",
       "- **Course originals** come from the instructor's homework, quizzes, Chime Ins and book.",
       "- **AI-written versions** test the same idea with a new scenario or numbers. Their ID ends in -v1 or -v2 and names the original.",
       f"- {len(rows)} questions in all. {len(fig)} use a figure and are marked **Figure question (website only)**: students practice those on the "
       "study-guide website, where the figure is shown. Use one only when a student brings it to you; its figure link is included.", "",
       "## Chapters and concepts", ""]
for ch in sorted(NAMES):
    out.append(f"- **Chapter {ch}: {NAMES[ch]}** — " + "; ".join(CONCEPTS.get(ch, {}).keys()))
out.append("")
PARTS = [(0, 3), (4, 6), (7, 9), (10, 12)]
old = os.path.join(HERE, "tutor_question_bank.md")
if os.path.exists(old):
    os.remove(old)
for lo, hi in PARTS:
    part = [out[0].replace("question bank", f"question bank, chapters {lo}–{hi}")] + out[1:]
    for ch in range(lo, hi + 1):
        if ch not in groups:
            continue
        part += [f"## Chapter {ch}: {NAMES[ch]}", ""]
        order = sorted(groups[ch], key=lambda r: (r["variant_of"] or r["id"], r["variant_of"] != "", r["id"]))
        part += [block(r) for r in order]
    path = os.path.join(HERE, f"tutor_bank_ch{lo:02d}-{hi:02d}.md")
    open(path, "w", encoding="utf-8").write("\n".join(part))
    print(os.path.basename(path), os.path.getsize(path) // 1024, "KB")
print(len(rows), "questions,", len(fig), "with figures")

# Open-ended bank: turn figure file names into links to the published images.
ob = open(os.path.join(ROOT, "open_ended_bank.md"), encoding="utf-8").read()
ob = re.sub(r"`([\w.-]+\.png)`", lambda m: f"[{m.group(1)}]({FIG_BASE}{m.group(1)})", ob)
ob = ob.replace("Images are in `bank_images/`.", "Figures are linked to their public copies on the course site; give students the link.")
open(os.path.join(HERE, "open_ended_bank.md"), "w", encoding="utf-8").write(ob)
print("open_ended_bank.md:", len(re.findall(re.escape(FIG_BASE), ob)), "figure links")
print({ch: len(v) for ch, v in sorted(groups.items())})
