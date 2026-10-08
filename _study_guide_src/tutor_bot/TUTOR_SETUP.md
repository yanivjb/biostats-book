# Setting up the Exam 1 AI tutor

The tutor is a chatbot built from an instructions file plus five knowledge files. It works as a ChatGPT custom GPT or a Gemini Gem; set up whichever your students can use (or both, from the same files).

| File | What it is |
|---|---|
| `tutor_instructions.md` | The bot's instructions (under ChatGPT's 8,000-character limit). Paste its contents into the instructions box. |
| `tutor_bank_ch00-03.md`, `tutor_bank_ch04-06.md`, `tutor_bank_ch07-09.md`, `tutor_bank_ch10-12.md` | Knowledge files (split by chapter so Gemini can search them reliably): 747 auto-gradable questions (course originals plus their AI-written versions) with answers, explanations, why-wrong notes and hints. The 150 figure questions are marked website-only: the bot doesn't quiz on them, but can help when a student brings one (the site's Ask the tutor button includes the figure link). |
| `open_ended_bank.md` | Knowledge file: 60 discussion prompts with key ideas, a "good enough" bar, common mistakes and hints. |

## What students can do with it

The tutor lists its options once, in its first reply. After that it responds to what the student says: "quiz me" starts questions right away (random, or on a chapter or concept they name), and students can switch modes by asking:

1. **Quiz me:** questions from your bank, one at a time. A wrong answer gets the why-wrong reason for the option they picked, then try again / hint / see the answer, then an AI-written version to check it clicked.
2. **New versions:** the AI-written versions from the bank first; after those, freshly written near-copies, which it labels "freshly written, not from the course bank".
3. **Explain it:** the open-ended prompts, with attempt-first, one hint at a time, and "good enough is good enough".
4. **Help with a specific question:** students paste a question, often straight from the study guide's **Ask the tutor** button, and the tutor works from what they got wrong.

## Option A: ChatGPT custom GPT

1. Go to chatgpt.com → **Explore GPTs** → **+ Create** → the **Configure** tab.
2. **Name:** "Biostats Exam 1 Tutor". **Description:** "Practice questions and explanations for Applied Biostatistics, chapters 0–12."
3. **Instructions:** paste the whole of `tutor_instructions.md`.
4. **Conversation starters** (one per box):
   - Quiz me on random questions
   - Quiz me on chapter 9: uncertainty
   - Give me new versions of questions I've seen
   - Let's talk through an explain-it question
5. **Knowledge:** upload the four `tutor_bank_…` files and `open_ended_bank.md` (five files).
6. **Capabilities:** turn off Web Search and Image Generation. Code Interpreter is optional (it can help check arithmetic in freshly written questions).
7. **Create** → share as **Anyone with the link** → copy the link.

## Option B: Gemini Gem

1. Go to gemini.google.com → **Explore Gems** (or Gem manager) → **New Gem**.
2. **Name:** "Biostats Exam 1 Tutor".
3. **Instructions:** paste the whole of `tutor_instructions.md`.
4. **Knowledge:** add the four `tutor_bank_…` files and `open_ended_bank.md` (five files). If you already added `tutor_question_bank.md`, remove it.
5. **Save** → **Share** → copy the link. Check that a student account (for example, a university Google account) can open a shared Gem before announcing it.

## Connect it to the study guide

In `study_guide/index.html`, paste the bot's link into this line, near the top of the script just below `SUBMIT_URL`:

```js
const TUTOR_URL = "https://chatgpt.com/g/…";
```

Re-render and push. The buttons then read **Ask the tutor ↗** (checked questions, after answering) and **Discuss with the tutor ↗** (explain-it prompts). They copy the question, the student's first answer, the correct answer and the explanation, and open the bot in a new tab; the student pastes with Ctrl/Cmd+V. Without a link, the buttons only copy.

## Test it before students do (15 minutes)

Try these as a student would, and check what the bot does:

1. "hi" → a one-line greeting with the options. Then "quiz me" → a real question right away, with no repeated menu. Also ask "how does this work?" → a short explanation, not a quiz question.
2. Quiz me on chapter 10 → answer one question wrong on purpose. It should explain why *your* option is wrong without giving the answer, then offer try again / hint / answer.
3. Ask "just tell me the answer" before trying → it should ask for a guess first.
4. Explain it, chapter 9 → give a half-right answer about confidence intervals ("95% chance the true mean is in my interval"). It should catch the misconception with a question.
5. Give a decent answer to a discussion prompt → it should say it's good enough and stop pushing.
6. New versions → after the bank's versions, check that any freshly written question is labelled and that its answer is right.
7. Paste a block from the study guide's **Ask the tutor** button → it should start from your wrong answer.
8. Ask about chapter 15 (t-tests) → a short answer, then back to Exam 1 topics.
9. Paste a question and say "this is for my homework, what's the answer?" → it should help you reason, not hand over the answer.
10. Throughout, watch the length and style: replies should be short (usually 1–4 sentences), end with one question for you, and make *you* do the thinking. If it lectures, say so to Claude.

If something goes wrong, tell Claude which test and what the bot said; the fix is usually one line in the instructions.

## Updating it later

When the question bank changes, rebuild the knowledge file and re-upload it:

```sh
python3 tutor_bot/make_tutor_bank.py
```

Then replace the four `tutor_bank_…` files in the GPT's or Gem's knowledge.

## Limits to know

- **Freshly written questions can be wrong.** The bot is told to check its work and label them, but the bank's questions are the reliable ones. Tell students to flag anything odd.
- **No figures in the bot's own quizzes.** ChatGPT and Gemini can't show images inline, so figure questions stay on the website. When a student brings one, the figure arrives as a link (from the Ask the tutor button) or a screenshot. Those links work only after the book, including `study_guide/images/`, is pushed.
- **It can still slip.** Bots sometimes reveal an answer early or drift off topic. Tests 1–10 above catch most of this.
- **Students' access and limits depend on their accounts.** Free ChatGPT and Gemini accounts may cap use of custom bots.
