# Applied Biostats: Open-Ended Discussion Bank (Exam 2, Chapters 13–21)

This is a knowledge base for the tutor bot's discussion mode (Mode 4). Each entry has:

- **Prompt**: what to ask the student, with any data or context they need.
- **Key ideas**: what a complete answer contains. This is for the tutor only. Never paste it to the student.
- **Good enough when**: the bar for saying "this is good enough to submit."
- **What could go wrong**: common misconceptions to listen for, and how to redirect.
- **Hints**: escalating nudges, used one at a time and only after the student has tried.
- **Related**: IDs in `question_bank_exam2.csv` that cover the same idea as multiple choice.

Figures are linked to their public copies on the course site; give students the link. Chapter numbers follow the bank: 13 linear models, 14 normal distribution, 15 t distribution, 16 comparing two means, 17 F, 18 ANOVA, 19 regression, 20 multiple regression, 21 interactions.

---

## Tutor rules (apply to every entry)

1. **Attempt first.** Give no help until the student has tried an answer. If they ask for help first, say something like "I'm happy to help once you give it a first shot."
2. **Don't give the answer.** Guide with questions, examples and hints. Never paste the key ideas.
3. **Be encouraging.** Say specifically what is right in their answer before addressing what's missing.
4. **Hints in order.** Give one hint at a time. Move to the next only if the student is still stuck.
5. **Good enough is good enough.** Once the student has tried more than once and has a complete sentence showing they understand, say: "Great job, this is good enough to submit. I'm here if you want to refine it further." Don't keep pushing for a perfect answer.
6. **Correct misconceptions gently but clearly.** If the student says something wrong (e.g., "a p-value is the probability the null is true," or "we controlled for body mass"), don't let it slide. Ask a question that exposes the problem.
7. **No R needed.** Students won't have R on the exam. Don't ask them to run code. Talking about what code or output *means* is fine.
8. **Stay in scope.** If a student asks something outside these chapters, give a short answer and steer back.

---

## Chapter 13: Linear models

### O-13-01 · Dose as a category or as a number?
- **Source:** Linear models group quiz (2026), Q1
- **Prompt:** Orange juice increases tooth growth, so researchers asked whether vitamin C alone does the job. They gave hamsters vitamin C at three doses (0.5, 1 or 2 mg/day), either in water or as orange juice, and modeled tooth length with dose as a categorical variable rather than a number. What is the difference between these two choices, and why might you choose the categorical one?
- **Key ideas:**
  - **Categorical:** each dose gets its own mean (two coefficients, each compared to the reference dose). No assumption about the shape of the dose-response.
  - **Numeric:** dose gets a single slope, which assumes each extra mg changes tooth length by the same amount (a straight line).
  - **Why categorical here:** with only three, unevenly spaced doses, we may not want to assume linearity.
  - **The cost:** an extra parameter, and no way to predict between or beyond the doses tested.
- **Good enough when:** the student explains that categorical gives separate means while numeric gives one slope (assuming linearity), plus one reason to prefer categorical.
- **What could go wrong:**
  - "Numbers must always be numeric." Ask: do we believe going from 1 to 2 mg has exactly twice the effect of going from 0.5 to 1 mg?
  - "It makes no difference." Ask how many coefficients each version has.
- **Hints:**
  1. How many coefficients does dose get each way?
  2. What does a single slope assume about the effect of each extra mg?
- **Related:** ch13-quiz-01, ch13-quiz-02, ch13-quiz-03

### O-13-02 · Summarize the larval fish results
- **Source:** Linear models group quiz (2026), Q9
- **Prompt:** Show [ch13-quiz-fish.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch13-quiz-fish.png). To ask whether fishing makes fish populations more variable, a model of 28 fish species gives: lm(cv ~ exploited + age), with (Intercept) = 1.25, exploitedyes = 0.45, age = -0.04, and residual SD = 0.313 (25 df). Here cv is the year-to-year coefficient of variation in larval abundance, and age is age at maturation (years). Summarize these results in a short paragraph for a biologist.
- **Key ideas:**
  - **Main comparison:** after adjusting for age at maturation, exploited species have more variable larval populations (CV about 0.45 higher).
  - **Covariate:** within each group, later-maturing species are slightly less variable (about 0.04 lower CV per year).
  - **Fit:** species typically deviate from predictions by about 0.3.
  - **Caution:** this is observational, so it shows an association with exploitation, not that fishing caused the variability.
- **Good enough when:** the student states the exploited vs unexploited difference with its size and direction, and mentions that age was adjusted for.
- **What could go wrong:**
  - "Fishing causes higher variability." Ask whether exploitation was assigned at random.
  - Interpreting the intercept as meaningful (an unexploited species maturing at age 0).
  - "Controlled for age." Prefer "adjusted for."
- **Hints:**
  1. Start with the comparison the study was about. Which group is more variable, and by how much?
  2. What else is in the model, and what does including it do?
- **Related:** ch13-quiz-05, ch13-quiz-08, ch13-quiz-09

---

## Chapter 14: The normal distribution

### O-14-01 · Are birth weights really normal?
- **Source:** Book: Normal summary (Q8)
- **Prompt:** Birth weight is a key predictor of infant health. The weights of singleton babies born in the U.S. are roughly normal (mean 3.339 kg, SD 0.573 kg). Do you think birth weights are actually perfectly normal? If not, how might they deviate?
- **Key ideas:**
  - Real traits are never perfectly normal; the normal is a model.
  - Birth weight can't be negative, but a normal distribution has infinite tails.
  - Premature births create a longer left tail (more very light babies than a normal predicts). There may also be a slight right skew from very large babies.
  - The normal works well in the middle but can misjudge the tails, which is where many health questions (e.g. low birth weight) live.
- **Good enough when:** the student says no and gives at least one specific, biologically sensible way the distribution departs from normal.
- **What could go wrong:**
  - "Yes, because the textbook said so." Ask what processes could produce very light babies.
  - Vague answers ("it might be skewed") without a reason. Ask which direction, and why.
- **Hints:**
  1. Think about the tails. What could produce unusually light babies?
  2. Can a baby weigh less than 0 kg? What does a normal distribution say?
- **Related:** ch14-book-01, ch14-hw-08

---

## Chapter 15: The t distribution

### O-15-01 · Write up the body temperature results
- **Source:** t distribution quiz (2026), Q14
- **Prompt:** To check the folk value of 98.6 °F for human body temperature, researchers measured 25 random people: mean 98.524 °F, SD 0.678 °F (Cohen's d = 0.11), t = -0.56 with 24 df, p = 0.58, 95% CI (98.24, 98.80). Write up these results in a brief paragraph.
- **Key ideas:**
  - Report the estimate with uncertainty: mean 98.52 °F, 95% CI 98.24 to 98.80.
  - Report the test: t = -0.56, df = 24, p = 0.58: not significantly different from 98.6.
  - Report the effect size: tiny (d = 0.11).
  - Conclude without overclaiming: the data are consistent with 98.6, but don't prove it; values from about 98.2 to 98.8 are also plausible.
- **Good enough when:** the paragraph includes the estimate, the test result, and a conclusion that doesn't claim the null is proven.
- **What could go wrong:**
  - "This proves body temperature is 98.6 °F." Ask what failing to reject means.
  - Reporting only the p-value. Ask what a reader would want to know about the size and precision of the estimate.
- **Hints:**
  1. Start with the estimate and its CI.
  2. Then the test (t, df, p). What does a non-significant result allow you to say?
- **Related:** ch15-quiz-07, ch15-quiz-09, ch15-quiz-03

### O-15-02 · Which matters more: t vs z, or the standard error?
- **Source:** Chime In (t), Q9
- **Prompt:** Sample size plays two roles when we use the t: (A) accounting for uncertainty in our estimate of the SD (the t approaches the z as n grows), and (B) setting the size of the standard error. Explain which matters more, and why.
- **Key ideas:**
  - **B matters more for most studies.** SE = SD / √n keeps shrinking as n grows: quadrupling the sample halves the SE, narrowing CIs and increasing power.
  - **A matters mainly for small samples.** Once n is around 20 to 30, the critical t is close to 1.96, so more data barely changes it.
  - Both push toward narrower intervals with larger n, but the √n in the SE is the big effect.
- **Good enough when:** the student picks B and explains that the SE keeps shrinking with n, while the t/z difference fades quickly.
- **What could go wrong:**
  - "A, because t has fat tails." Ask how different the critical values are at n = 30 vs n = 300 (about 2.05 vs 1.97).
  - Confusing the SD (doesn't shrink with n) with the SE (does).
- **Hints:**
  1. How much does the critical t change between n = 30 and n = 300?
  2. How much does the SE change between n = 30 and n = 300?
- **Related:** ch15-chimein-05, ch15-hw-03, ch15-book-03

---

## Chapter 16: Comparing two means

### O-16-01 · Is equal variance OK for the ataxia mice?
- **Source:** Chime In (two-sample t), Q5
- **Prompt:** Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise. Lifespan variance was 224 days² without exercise and 874 days² with exercise (n = 6 per group). Welch's t-test gives p = 0.015; the standard t-test gives p = 0.010. Do you feel comfortable assuming equal variance? Explain why or why not.
- **Key ideas:**
  - The variance ratio is 874 / 224 ≈ 3.9: a real difference, but under the common rule of thumb (less than about 5).
  - Equal sample sizes make the t-test more robust to unequal variances.
  - Welch's test, which doesn't assume equal variance, gives a similar answer, so the conclusion doesn't depend on the assumption.
- **Good enough when:** the student computes or estimates the ratio, compares it to a rule of thumb, and mentions either equal sample sizes or the Welch check.
- **What could go wrong:**
  - "No, because the variances aren't identical." They never are; ask what rule of thumb we use.
  - Comparing SDs to a variance rule of thumb (or vice versa).
- **Hints:**
  1. Divide the larger variance by the smaller one.
  2. Does Welch's test change the conclusion?
- **Related:** ch16-chimein-03, ch16-hw-02, ch16-book-03

### O-16-02 · Why is the ataxia lifespan p-value suspect?
- **Source:** Chime In (two-sample t), Q8
- **Prompt:** Researchers had 6 of 12 mice with spinocerebellar ataxia exercise to see if it improved motor skills. Finding no effect, they later decided to compare lifespans, and found a significant difference (p = 0.01). Why does the way this question arose make the p-value suspect?
- **Key ideas:**
  - Lifespan wasn't the planned question; it was examined after the main result was null, possibly because the researchers noticed a difference.
  - A p-value assumes the hypothesis was specified before seeing the data.
  - Choosing what to test after seeing the data (or testing many things and reporting the one that 'worked') makes false positives much more likely than 5%.
  - The result should be treated as exploratory and tested in a new experiment.
- **Good enough when:** the student explains that the hypothesis was chosen after looking at the data, and that this inflates the chance of a false positive.
- **What could go wrong:**
  - "The sample is too small." Small samples reduce power, but that doesn't explain why a significant p-value is suspect.
  - "They violated equal variance." The variances are acceptable; that's not the main problem.
- **Hints:**
  1. When did the researchers decide to test lifespan?
  2. If you tested ten different traits, how likely is it that one gives p < 0.05 by chance?
- **Related:** ch16-chimein-06

---

## Chapter 18: ANOVA

### O-18-01 · The multiple testing problem
- **Source:** ANOVA quiz (2026), Q7
- **Prompt:** Explain the multiple testing problem, and how an ANOVA followed by post-hoc tests addresses it.
- **Key ideas:**
  - Each test has a chance α of a false positive when the null is true, so running many tests makes it likely at least one is 'significant' by chance.
  - With 4 groups there are 6 pairwise tests: P(at least one false positive) = 1 - 0.95⁶ ≈ 0.26, not 0.05.
  - An ANOVA tests one null (all means equal) at α = 0.05.
  - Only if it's rejected do we do post-hoc tests (e.g. Tukey), which adjust p-values so the overall false positive rate stays near 5%.
- **Good enough when:** the student explains that many tests inflate false positives, and that ANOVA does one test with post-hoc tests correcting for the rest.
- **What could go wrong:**
  - "Multiple testing is a problem because it's more work." Ask what happens to the false positive rate.
  - "ANOVA tells you which groups differ." It doesn't; that's the post-hoc test's job.
- **Hints:**
  1. If each test has a 5% false positive rate, what happens when you run 15 of them?
  2. How many hypotheses does a single ANOVA test?
- **Related:** ch18-chimein-01, ch18-hw-02, ch18-book-02, ch18-quiz-06

### O-18-02 · Write up the Rickettsiella aphid results
- **Source:** ANOVA quiz (2026), Q9
- **Prompt:** Pea aphids can carry the bacterium Rickettsiella, which may change their body color. Researchers compared color among aphids that never had the bacterium (original), aphids born infected to lab-infected mothers (infected), and aphids born uninfected to lab-infected mothers (uninfected).
  ```
  aov(color ~ infectionStatus) |> summary()
                  Df Sum Sq Mean Sq F value   Pr(>F)
  infectionStatus  2 2379.3  1189.6   65.59 1.73e-11
  Residuals       29  525.9    18.1

  TukeyHSD:
  original - infected    diff -17.3 (-21.7, -12.9)  p < 0.0001
  uninfected - infected  diff -19.2 (-23.9, -14.4)  p < 0.0001
  uninfected - original  diff  -1.9  (-6.5,   2.8)  p = 0.58
  ```
  Write a brief paragraph about these results, including significance groups.
- **Key ideas:**
  - The ANOVA rejects equal means: F = 65.6, df = 2 and 29, p = 1.7 × 10⁻¹¹.
  - Tukey: infected aphids differ from both other groups (by about 17 to 19 color units, p < 0.0001); original and uninfected don't differ (p = 0.58).
  - Significance groups: infected = a; original and uninfected = b.
  - Biological meaning: carrying the bacterium, not having an infected mother, is associated with the color change.
- **Good enough when:** the paragraph reports the ANOVA, says which groups differ (with significance groups), and gives a biological interpretation.
- **What could go wrong:**
  - Reporting only the ANOVA. Ask which groups actually differ.
  - Reading p = 0.58 as "infection doesn't matter." Ask which comparison that p-value belongs to.
- **Hints:**
  1. Start with the overall test. Then: which pairs in the Tukey table are significant?
  2. Groups that don't differ share a letter.
- **Related:** ch18-quiz-09, ch18-hw-06, ch18-book-11

---

## Chapter 19: Regression

### O-19-01 · Assumptions for the lizard bite force regression
- **Source:** Regression quiz (2026), Q7
- **Prompt:** Show [ch19-quiz-lizard-diag.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-quiz-lizard-diag.png). Male collared lizards use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite forces 4.3 to 5.4 N). Looking at the diagnostic plots for lm(territory ~ bite), which assumptions of the linear model (if any) concern you? Point to features of the study design and/or the plots. What, if anything, can you do about it?
- **Key ideas:**
  - With only 11 lizards, diagnostic plots can't tell us much: patterns could be noise, and one lizard can strongly influence the slope.
  - The narrow range of bite forces makes it hard to check linearity.
  - Independence could be an issue if neighbouring lizards' territories constrain each other.
  - Unbiased sampling: were these random lizards, or the easiest to catch?
  - Options: interpret cautiously, refit without the most influential point, use a permutation test or bootstrap, and collect more data over a wider range.
- **Good enough when:** the student names at least one concern tied to the study (small n, narrow range, possible non-independence) and one sensible response.
- **What could go wrong:**
  - "The plots look fine, so there's no problem." Ask how many points the plots are based on.
  - "Delete the outliers." Ask how that would change what the results mean.
- **Hints:**
  1. How many lizards are there? How sure can you be about patterns in 11 points?
  2. Could one lizard's territory affect another's?
- **Related:** ch19-quiz-04, ch19-book-07, ch19-book-09

### O-19-02 · Does bite force win territories, or do territories build bite force?
- **Source:** Regression quiz (2026), Q13
- **Prompt:** Male collared lizards with stronger bites have bigger territories. Two explanations: (1) males with stronger bites win bigger territories; (2) males with bigger territories get stronger bites (e.g. by eating better). Which do you prefer and why? Describe an experiment to tease these apart. Can you think of other explanations?
- **Key ideas:**
  - Either explanation fits; this observational regression shows an association but not its direction.
  - A third variable (e.g. body size or age) could drive both.
  - **Experiments:**
    - For (1), reduce some males' bite force, or compare matched males, and see whether they lose territory.
    - For (2), give some males larger or richer territories and measure bite force later.
  - Measuring and adjusting for body size addresses the third-variable explanation.
- **Good enough when:** the student recognizes that the data can't distinguish the directions and proposes a manipulation that could.
- **What could go wrong:**
  - "The regression proves (1) because bite force is on the x-axis." Ask whether putting a variable on the x-axis makes it a cause.
  - Proposing more observational data as the fix. Ask what you would need to manipulate.
- **Hints:**
  1. Which variable could you change experimentally?
  2. Could something else make a lizard both strong-biting and territorial?
- **Related:** ch19-quiz-09, ch20-hw-11

---

## Chapter 20: Multiple regression

### O-20-01 · Is multicollinearity a big problem for the penguin model?
- **Source:** Multiple regression quiz (2026), Q8 (explain)
- **Prompt:** Palmer penguins: bill length was modeled as a function of bill depth and body mass. The two explanatory variables are significantly associated (r² = 0.22, F₁,₃₄₀ = 97.4, p < 2.2 × 10⁻¹⁶). Is multicollinearity likely a big problem? Explain.
- **Key ideas:**
  - A significant association isn't a strong one: with 342 penguins even a modest correlation gives a tiny p-value.
  - Multicollinearity depends on how strongly predictors are related: r² = 0.22 means they share only about a fifth of their variation.
  - VIF = 1 / (1 - r²) ≈ 1.3, well below the 5 to 10 range where we'd worry.
  - Correlated predictors are expected; adjusting for them is the point of multiple regression.
- **Good enough when:** the student says no, separating significance from strength, and uses r² or VIF.
- **What could go wrong:**
  - "Yes, because p is tiny." Ask what the p-value would be with 10 penguins and the same r.
  - "Any correlation between predictors is a problem." Ask why we'd use multiple regression at all, then.
- **Hints:**
  1. Does a small p-value mean a strong correlation?
  2. How much of their variation do the two predictors share (r²)?
- **Related:** ch20-quiz-08, ch20-quiz-12, ch20-hw-06

### O-20-02 · Why one model instead of several?
- **Source:** Chime In (multiple regression), Q1
- **Prompt:** Why use one model with more than one predictor, rather than a separate model for each explanatory variable?
- **Key ideas:**
  - **Variables travel together:** explanatory variables are often associated, so a one-predictor model can credit one variable with an effect that belongs to another. Multiple regression estimates each association adjusting for the others (the estimate can change).
  - **Precision:** accounting for a variable that explains a lot of the response reduces unexplained variation, making other effects easier to detect (the uncertainty shrinks).
  - Example: lazy mole rats are bigger, so comparing castes without accounting for body mass hides the caste difference.
- **Good enough when:** the student gives at least one of the two reasons, clearly explained.
- **What could go wrong:**
  - "It accounts for multiple testing." Each term still gets its own test.
  - "It's just more efficient." Ask what goes wrong if two predictors are correlated and you model each alone.
- **Hints:**
  1. What if two predictors are correlated and you only include one?
  2. What happens to unexplained variation when you add a predictor that matters?
- **Related:** ch20-quiz-13, ch20-chimein-03

### O-20-03 · Why not include every variable?
- **Source:** Chime In (multiple regression), Q2
- **Prompt:** Why not include every possible explanatory variable in a model?
- **Key ideas:**
  - Each term costs a degree of freedom, reducing power.
  - Many terms risk overfitting: describing noise that won't hold for new data.
  - Highly correlated predictors make coefficients unstable (multicollinearity).
  - Some variables shouldn't be adjusted for at all: a consequence of the focal predictor can hide its effect.
  - Very large models are hard to interpret.
  - Include variables for biological reasons tied to the question.
- **Good enough when:** the student gives at least two distinct reasons.
- **What could go wrong:**
  - "More variables always make a better model." Ask what R² does when you add pure noise, and whether that means the model improved.
- **Hints:**
  1. What does each extra term cost?
  2. Could adjusting for the wrong variable hide a real effect?
- **Related:** ch20-hw-03, ch20-quiz-12

---

## Notes for the instructor

- These 14 entries come from the open questions in your quizzes, ChimeIns and book summaries (they are marked `include = no` in `question_bank_exam2.csv`).
- **Images:** O-13-02 and O-19-01 mention a figure in the prompt. `build_data.py` needs a student-facing wording for these in its `STUDENT_PROMPT` dictionary, as for Exam 1.
- **Not included:** reflection and opinion prompts ("what are you still confused about?", "how willing are you to say the null is false?") and "build your own model" tasks.
- **Olympic 200 m write-up:** not included until we have the dataset.
