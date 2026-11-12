BP = """Two clinical studies each found that a drug lowers blood pressure by 2 mmHg (null value μ₀ = 0).

Study | n | SD (mmHg)
X | 10,000 | 20
Y | 10 | 2

Equations: SE = s / √n, t = (x̄ - μ₀) / SE, d = (x̄ - μ₀) / s"""
TEMPCI = "25 people had a mean body temperature of 98.52 °F, with a 95% CI of 98.24 to 98.80 °F."
TROUT = """To see whether introduced brook trout harm native Chinook salmon, Levin et al. measured the proportion of juvenile salmon surviving in six streams with and six without brook trout.

trout | mean survival | variance | n
absent | 0.235 | 0.01074 | 6
present | 0.194 | 0.00088 | 6"""
ATAXIA = """Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise to see if it improved motor skills; finding no effect, they later decided to compare lifespans instead.

treatment | mean lifespan (days) | variance | n
no exercise | 267.3 | 224.3 | 6
exercise | 310.0 | 874.4 | 6

Pooled variance = 549.3 (pooled SD = 23.4). Difference in means (no exercise - exercise) = -42.7 days."""
FROGS = """To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27"""

ROWS = [
# ---------------- Quiz: two-sample group quiz (Oct 28) ----------------
dict(id="ch16-quiz-01", source="Comparing two means group quiz (2026), Q1a", topics="effect size, Cohen's d", type="matching",
question=BP + "\n\nMatch each study to its Cohen's d:\n\n1. Study X\n2. Study Y",
options="""A) d = 0.1
B) d = 1
C) d = 10
D) d = 3.16""",
answer="1-A, 2-B",
explanation="d = difference / SD. Study X: 2 / 20 = 0.1 (tiny). Study Y: 2 / 2 = 1 (large).",
why_wrong="C) and D) are the t values (difference / SE), not Cohen's d.",
hint="Cohen's d uses the SD, not the SE."),

dict(id="ch16-quiz-02", source="Comparing two means group quiz (2026), Q1b", topics="t statistic, standard error, sample size", type="matching",
question=BP + "\n\nMatch each study to its t value:\n\n1. Study X\n2. Study Y",
options="""A) t = 0.1
B) t = 1
C) t = 10
D) t = 3.16""",
answer="1-C, 2-D",
explanation="Study X: SE = 20 / √10,000 = 0.2, so t = 2 / 0.2 = 10. Study Y: SE = 2 / √10 = 0.63, so t = 2 / 0.63 = 3.16.",
why_wrong="A) and B) are Cohen's d values (difference / SD).",
hint="First find each SE = SD / √n."),

dict(id="ch16-quiz-03", source="Comparing two means group quiz (2026), Q1c-d", topics="NHST, sample size, effect size", type="MC",
question=BP + "\n\nStudy X has t = 10 (d = 0.1); Study Y has t = 3.16 (d = 1). At α = 0.05, what do we do with H₀ in each study, and which has the smaller p-value?",
options="""A) Reject H₀ in both; Study X has the smaller p-value
B) Reject H₀ in both; Study Y has the smaller p-value
C) Reject H₀ only in Study Y; Study Y has the smaller p-value
D) Reject H₀ only in Study X; Study X has the smaller p-value""",
answer="A",
explanation="Both t values exceed their critical values (about 1.96 for X; 2.26 for Y with 9 df), so we reject in both. Study X's t is much larger, so its p-value is much smaller, even though its effect is tiny. Huge samples make tiny effects 'significant'.",
why_wrong="""B) Y has the bigger effect, but X has the bigger t (and smaller p) because of its huge sample.
C) X's t of 10 is far beyond the critical value.
D) Y's t of 3.16 also exceeds its critical value (2.26).""",
hint="Compare t values, not effect sizes, to decide about H₀."),

dict(id="ch16-quiz-04", source="Comparing two means group quiz (2026), Q1e", topics="p-values, interpreting results", type="MC",
question=BP + "\n\nStudy X has the smaller p-value. Which study has the higher chance that the null hypothesis is false?",
options="""A) Study X, because its p-value is smaller
B) Study Y, because its effect size is larger
C) We can't tell from these numbers""",
answer="C",
explanation="A p-value is the probability of data this extreme if the null were true. It isn't the probability that the null is false, so comparing p-values doesn't tell us which null is more likely to be false.",
why_wrong="""A) A smaller p-value isn't a higher probability that the null is false.
B) A bigger effect size isn't either.""",
hint="What is a p-value the probability of?"),

dict(id="ch16-quiz-05", source="Comparing two means group quiz (2026), Q2", topics="confidence intervals, interpreting CIs", type="matching",
question=TEMPCI + """ Mark each statement as OK or Wrong:

1. 95% of people have a body temperature between 98.24 and 98.80 °F.
2. If we repeated this study many times, about 95% of intervals built this way would contain the true mean.
3. 98.6 °F is inside the interval, so the true mean is 98.6 °F.
4. A 99% CI from the same data would be narrower.""",
options="""A) OK
B) Wrong""",
answer="1-B, 2-A, 3-B, 4-B",
explanation="""1) Wrong: the CI describes uncertainty in the mean, not where individual people fall (that's much wider).
2) OK: this is the correct interpretation of a 95% CI.
3) Wrong: 98.6 is plausible, but so is every other value in the interval.
4) Wrong: more confidence requires a wider interval.""",
why_wrong="The most common mistake is reading a CI as a range for individuals rather than for the mean.",
hint="Is a CI about individuals or about the mean? What happens to the interval if you want more confidence?"),

# ---------------- Homework (brook trout and salmon) ----------------
dict(id="ch16-hw-01", source="Comparing two means homework, Q1", topics="visualizing two groups, confidence intervals", type="select-all",
question=TROUT + "\n\nThe plot shows each stream and the group means with 95% confidence intervals. Which statements are consistent with the plot? (Select all that apply.)",
image="ch16-hw-trout.png",
options="""A) Mean survival was higher when trout were absent than when they were present
B) Mean survival was lower when trout were absent than when they were present
C) There was no overlap between the 95% confidence intervals for the two treatments
D) The 95% confidence intervals for the two groups overlap
E) There appears to be less variation in survival when trout were present""",
answer="A, D, E",
explanation="The mean is a bit higher without trout (0.235 vs 0.194), the CIs overlap broadly, and survival is much less variable among streams with trout.",
why_wrong="""B) The absent mean is higher.
C) The intervals overlap a lot.""",
hint="Look at where the black points sit, whether the bars overlap, and how spread out each group's points are."),

dict(id="ch16-hw-02", source="Comparing two means homework, Q2", topics="equal variance assumption", type="MC",
question=TROUT + "\n\nThe standard two-sample t-test assumes equal variance. A common rule of thumb is that we're probably OK if one group's variance is less than about five times the other's. How comfortable are you assuming equal variance?",
options="""A) Totally cool: the variances are nearly identical
B) OK, I think: the variance with brook trout is about 5 times larger than without
C) Pretty nervous: the variances are WAY different""",
answer="C",
explanation="0.01074 / 0.00088 = 12: the variance without trout is about 12 times the variance with trout, well beyond the rule of thumb.",
why_wrong="""A) They differ by more than tenfold.
B) Gets both the ratio and the direction wrong: the larger variance is where trout are absent.""",
hint="Divide the bigger variance by the smaller one."),

dict(id="ch16-hw-03", source="Comparing two means homework, Q3", topics="pooled variance", type="numeric",
question=TROUT + "\n\nWhat is the pooled variance? (Hint: with equal sample sizes, it is the average of the two variances.)",
answer="0.00581", explanation="Pooled variance = [(n₁ - 1)s₁² + (n₂ - 1)s₂²] / (n₁ + n₂ - 2) = (5 × 0.01074 + 5 × 0.00088) / 10 = 0.00581.",
why_wrong="Common mistake: averaging the standard deviations instead of the variances.",
hint="Weight each variance by its degrees of freedom."),

dict(id="ch16-hw-04", source="Comparing two means homework, Q4", topics="effect size, Cohen's d", type="MC",
question=TROUT + """

The pooled variance is 0.00581 and the difference in means is 0.041. How big is this effect?

Size | Cohen's d
Not worth reporting | < 0.01
Tiny | 0.01 to 0.20
Small | 0.20 to 0.50
Medium | 0.50 to 0.80
Large | 0.80 to 1.20
Very large | 1.20 to 2.00
Huge | > 2.00""",
options="""A) Not worth reporting to tiny
B) Small to medium
C) Large to very large
D) Huge""",
answer="B",
explanation="Pooled SD = √0.00581 = 0.0762. d = 0.041 / 0.0762 = 0.54, a medium effect (near the small/medium boundary).",
why_wrong="""A) Comes from dividing by the variance, or forgetting to take the square root.
C) and D) Too big: the difference is about half a standard deviation.""",
hint="Cohen's d needs the pooled SD, which is the square root of the pooled variance."),

dict(id="ch16-hw-05", source="Comparing two means homework, Q5", topics="standard error, two-sample t-test", type="numeric",
question=TROUT + "\n\nThe pooled variance is 0.00581. What is the standard error of the difference in means? (Report to three decimals.)",
answer="0.044", explanation="SE = √[s²ₚ (1/n₁ + 1/n₂)] = √[0.00581 × (1/6 + 1/6)] = √0.001937 = 0.044.",
why_wrong="Common mistakes: forgetting the square root (0.0019), or using only one 1/n term (0.031).",
hint="SE = √(pooled variance × (1/n₁ + 1/n₂))."),

dict(id="ch16-hw-06", source="Comparing two means homework, Q6", topics="Welch's t-test, equal variance assumption", type="MC",
question=TROUT + """

Here are results from a standard two-sample t-test and from Welch's t-test (which doesn't assume equal variance):

test | difference (absent - present) | 95% CI | p-value
two-sample t | 0.041 | (-0.057, 0.139) | 0.374
Welch's t | 0.041 | (-0.068, 0.150) | 0.389

In this case, breaking the assumption of equal variance had:""",
options="""A) A very strong effect on our conclusion
B) A moderate effect on our conclusion
C) An effect on our analysis small enough to safely ignore""",
answer="C",
explanation="Welch's test gives a slightly wider CI and a slightly larger p-value, but the conclusion is the same: no evidence of a difference. With equal sample sizes, the standard t-test is fairly robust to unequal variances.",
why_wrong="""A) and B) Both tests fail to reject the null by a wide margin.""",
hint="Would the two tests lead you to different conclusions?"),

dict(id="ch16-hw-07", source="Comparing two means homework, Q7", topics="interpreting non-significant results", type="TF",
question=TROUT + "\n\nTRUE or FALSE: Because we failed to reject the null hypothesis (p = 0.37), we can confidently conclude that introduced brook trout do not influence the survival of juvenile Chinook salmon.",
options="""A) TRUE
B) FALSE""",
answer="B",
explanation="Failing to reject is not evidence of no effect. With only six streams per group, the 95% CI runs from about -0.06 to 0.14, which includes effects large enough to matter for salmon.",
why_wrong="TRUE: absence of evidence isn't evidence of absence, especially with small samples.",
hint="What range of effects is consistent with these data?"),

# ---------------- ChimeIn (ataxia mice) ----------------
dict(id="ch16-chimein-01", source="Chime In (two-sample t), Q1-2", topics="effect size, Cohen's d", type="MC",
question=ATAXIA + "\n\nWhat is the absolute value of Cohen's d, and how big an effect is this? (Small ≈ 0.2, medium ≈ 0.5, large ≥ 0.8.)",
options="""A) |d| ≈ 0.08, small
B) |d| ≈ 0.5, medium
C) |d| ≈ 1.8, large
D) |d| ≈ 3.2, large""",
answer="C",
explanation="|d| = 42.7 / 23.4 = 1.82, a large effect: the groups differ by almost two pooled standard deviations.",
why_wrong="""A) Divides by the variance instead of the SD.
D) 3.15 is the t value (difference / SE), not d.""",
hint="Divide the difference in means by the pooled SD."),

dict(id="ch16-chimein-02", source="Chime In (two-sample t), Q3", topics="p-values, interpreting results", type="MC",
question=ATAXIA + "\n\nThe two-sample t-test gives p = 0.01. What is the probability that the true difference in lifespan between treatments is zero?",
options="""A) 0.01, the p-value from the test
B) 0.05, the significance threshold
C) We can't know this from a p-value""",
answer="C",
explanation="p = 0.01 is the probability of a difference at least this large if the true difference were zero. It isn't the probability that the true difference is zero.",
why_wrong="""A) Confuses P(data | null) with P(null | data).
B) 0.05 is the α threshold, not a probability about the null.""",
hint="What does a p-value assume?"),

dict(id="ch16-chimein-03", source="Chime In (two-sample t), Q4", topics="Welch's t-test, equal variance assumption", type="MC",
question=ATAXIA + """

test | difference | 95% CI | p-value
standard (equal variance) t | -42.7 | (-72.8, -12.5) | 0.010
Welch's t (unequal variance) | -42.7 | (-74.3, -11.0) | 0.015

In this case, compared to the standard t-test, are the p-value and 95% confidence interval from Welch's t-test (which doesn't assume equal variance) smaller, larger, or unchanged?""",
options="""A) Smaller
B) Larger
C) Unchanged""",
answer="B",
explanation="Welch's test gives p = 0.015 (vs 0.010) and a CI of (-74.3, -11.0) (vs -72.8 to -12.5). Not assuming equal variance costs some degrees of freedom, so it's a bit more conservative here.",
why_wrong="""A) Welch's test is usually a little more conservative.
C) The estimate is the same, but the uncertainty changes.""",
hint="Welch's test uses fewer degrees of freedom."),

dict(id="ch16-chimein-04", source="Chime In (two-sample t), Q5", topics="equal variance assumption", type="open", include="no",
question=ATAXIA + "\n\nDo you feel comfortable assuming equal variance? Explain why or why not.",
answer="Model answer: Mostly yes. The exercise group's variance (874) is about 3.9 times the no-exercise variance (224). That's a noticeable difference, but it's under the common rule of thumb of about 5, and the sample sizes are equal, which makes the t-test fairly robust. A Welch's t-test is a good check; here it gives a similar answer (p = 0.015 vs 0.010).",
explanation="Judge by the ratio of variances, the rule of thumb, sample sizes, and whether Welch's test changes the conclusion.",
hint="Divide the larger variance by the smaller one. Is it under about 5?"),

dict(id="ch16-chimein-05", source="Chime In (two-sample t), Q6", topics="NHST", type="MC",
question=ATAXIA + "\n\nThe two-sample t-test gives t = -3.15 (10 df) and p = 0.010. At α = 0.05, we ____ the null hypothesis.",
options="""A) reject
B) accept
C) fail to reject
D) fail to accept""",
answer="A",
explanation="0.010 < 0.05, so we reject the null.",
why_wrong="""B) and D) We never 'accept' a null.
C) p is below α.""",
hint="Compare p with α."),

dict(id="ch16-chimein-06", source="Chime In (two-sample t), Q7", topics="study design, p-hacking, HARKing", type="select-all",
question=ATAXIA + "\n\nThe researchers ran a two-sample t-test assuming equal variance. Which parts of the study make this p-value most suspect? (Pick the two best.)",
options="""A) Lifespan wasn't the question that motivated the study
B) The sample size is too small
C) They should not assume equal variance
D) They should not assume a normal distribution
E) The question may have been inspired by the data""",
answer="A, E",
explanation="The lifespan comparison was decided after the original experiment found nothing, possibly after seeing that lifespans differed. p-values assume the hypothesis was set before looking at the data; testing hypotheses suggested by the data inflates false positives.",
why_wrong="""B) Small samples reduce power, but they don't make a significant p-value suspect in the same way.
C) The variance ratio (about 3.9) is acceptable, and Welch's test agrees.
D) Nothing suggests a strong departure from normality.""",
hint="When, and why, did the researchers decide to compare lifespans?"),

dict(id="ch16-chimein-07", source="Chime In (two-sample t), Q8", topics="study design, p-hacking, HARKing", type="open", include="no",
question=ATAXIA + "\n\nWhy does the way this lifespan question arose make the p-value (0.01) suspect?",
answer="Model answer: The study was designed to test exercise and gait; lifespan was examined only later, after the main result was null, and perhaps because the researchers noticed a difference. A p-value assumes the hypothesis was specified in advance. When we pick which comparison to test after seeing the data (or test many things and report the one that worked), the chance of a false positive is much higher than 5%. This result should be treated as exploratory and tested again in a new experiment.",
explanation="This is the 'garden of forking paths': data-inspired hypotheses make p-values look stronger than they are.",
hint="Would you trust a p-value for a question you chose because the data looked interesting?"),

dict(id="ch16-chimein-08", source="Chime In (two-sample t), Q9", topics="confidence intervals, interpreting CIs", type="TF",
question=ATAXIA + "\n\nThe 95% CI for the difference (no exercise - exercise) is -72.8 to -12.5 days. TRUE or FALSE: Assuming all assumptions are valid, there is a 95% chance that the true mean is between -72.8 and -12.5.",
options="""A) TRUE
B) FALSE""",
answer="B",
explanation="Two problems. The interval is for the difference in means, not 'the true mean'. And a 95% CI means that 95% of intervals built this way would capture the true value; once we've calculated one interval, it either contains the true difference or it doesn't.",
why_wrong="TRUE: a very common way to misread a confidence interval.",
hint="What is the interval about? What does '95%' refer to?"),

dict(id="ch16-chimein-09", source="Chime In (two-sample t), Q10", topics="p-values, effect size", type="MC",
question="Why do p-values fail to communicate effect size?",
options="""A) They involve too much stats jargon for most people
B) They mix the size of a difference with sample size
C) They are great descriptions of effect size""",
answer="B",
explanation="The same small effect can give a tiny p-value with a huge sample, and a large effect can give a big p-value with a small sample. Effect sizes (like Cohen's d) describe how big a difference is.",
why_wrong="""A) Jargon isn't the issue.
C) They aren't: see the blood pressure studies, where the tiny effect had the smaller p-value.""",
hint="What happens to a p-value if you collect much more data, but the effect stays the same?"),

# ---------------- Book: Two t summary (frogs) ----------------
dict(id="ch16-book-01", source="Book: Two t summary (Q1)", topics="visualizing two groups", type="MC",
question=FROGS + "\n\nThe plot shows each mated pair and the group means with 95% CIs. What pattern do you see?",
image="ch16-book-frogs.png",
options="""A) Similar numbers (or slight differences) of hatched eggs in the preferred and nonpreferred treatments
B) Way more hatched eggs in the preferred treatment
C) Way more hatched eggs in the nonpreferred treatment""",
answer="A",
explanation="The means differ a bit (414 vs 345), but there's huge variation within each group and the CIs overlap broadly.",
why_wrong="""B) The preferred mean is actually slightly lower.
C) The nonpreferred mean is higher, but not by much compared to the spread.""",
hint="Compare the difference in means to the spread of points within each group."),

dict(id="ch16-book-02", source="Book: Two t summary (Q2)", topics="assessing normality, two-sample t-test", type="MC",
question="To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs. The figure shows histograms of hatched eggs, (A) with both treatments combined and (B) separately for each treatment. Which is more useful for evaluating the normality assumption of the two-sample t-test?",
image="ch16-book-frog-hists.png",
options="""A) Both treatments combined
B) Data separated by treatment
C) It depends: integrate information from both
D) Neither plot is appropriate""",
answer="B",
explanation="The t-test assumes the residuals (values minus their group mean) are normal, so we look within each group. A combined histogram can look odd just because the groups have different means.",
why_wrong="""A) Mixing two groups with different means can create shapes that aren't a problem.
C) The combined plot adds nothing for this assumption.
D) Within-group histograms are appropriate (a QQ plot of residuals is another good option).""",
hint="The normality assumption is about variation around each group's mean."),

dict(id="ch16-book-03", source="Book: Two t summary (Q3)", topics="equal variance assumption", type="MC",
question=FROGS + "\n\nShould you feel comfortable assuming equal variance?",
options="""A) Yes
B) No
C) Maybe
D) I don't know (I need to run a statistical test to evaluate this assumption)""",
answer="A",
explanation="67,412 / 56,118 = 1.2: the variances are very similar, well within the rule of thumb (less than about 5).",
why_wrong="""B) and C) The variances differ by only about 20%.
D) A rule of thumb (and a look at the data) is enough; formal tests of equal variance aren't needed.""",
hint="Divide the bigger variance by the smaller one."),

dict(id="ch16-book-04", source="Book: Two t summary (Q4)", topics="pooled variance", type="numeric",
question=FROGS + "\n\nWhat is the pooled variance?",
answer="61556", explanation="s²ₚ = [(29 - 1) × 56,118 + (27 - 1) × 67,412] / (29 + 27 - 2) = (1,571,304 + 1,752,712) / 54 = 61,556.",
why_wrong="Common mistake: a simple average of the two variances (61,765). The groups differ in size, so weight by degrees of freedom.",
hint="Weight each variance by its degrees of freedom (n - 1)."),

dict(id="ch16-book-05", source="Book: Two t summary (Q5)", topics="effect size, Cohen's d", type="MC",
question=FROGS + "\n\nThe pooled variance is 61,556. How would you characterize the effect size?",
options="""A) Not worth reporting (d < 0.01)
B) Tiny (0.01 to 0.20)
C) Small (0.20 to 0.50)
D) Medium (0.50 to 0.80)
E) Large (0.80 to 1.20)
F) Very large (1.20 to 2.00)
G) Huge (> 2.00)""",
answer="C",
explanation="Pooled SD = √61,556 = 248. d = (413.9 - 345.1) / 248 = 68.8 / 248 = 0.28, a small effect.",
why_wrong="Common mistake: dividing by the variance (gives about 0.001, 'not worth reporting').",
hint="Use the pooled SD, not the pooled variance."),

dict(id="ch16-book-06", source="Book: Two t summary (Q6)", topics="effect size, NHST", type="MC",
question=FROGS + "\n\nCohen's d is 0.28. From this value alone, we can conclude that:",
options="""A) We should reject the null hypothesis
B) We should fail to reject the null hypothesis
C) The null is false
D) The null is true
E) None of these: d describes size, not evidence""",
answer="E",
explanation="Whether we reject depends on the effect size and the sample size together (through the SE and t). A small effect can be significant in a big study, and a large one non-significant in a small study.",
why_wrong="""A) and B) To decide, we need t (or p), which depends on sample size.
C) and D) No single number proves the null true or false.""",
hint="Does Cohen's d depend on sample size?"),

dict(id="ch16-book-07", source="Book: Two t summary (Q7-8)", topics="null and alternative hypotheses", type="matching",
question=FROGS + "\n\nMatch each hypothesis to its statement:\n\n1. Null hypothesis\n2. Alternative hypothesis (two-tailed)",
options="""A) Mean hatched eggs are the same with preferred and nonpreferred females
B) Mean hatched eggs differ between preferred and nonpreferred females
C) Mean hatched eggs are higher with preferred females
D) Males prefer females that produce more offspring""",
answer="1-A, 2-B",
explanation="The null is no difference in population means. A two-tailed alternative allows a difference in either direction.",
why_wrong="""C) That's a one-tailed alternative.
D) That's a biological hypothesis, not a statistical one.""",
hint="Two-tailed: a difference in either direction counts."),

dict(id="ch16-book-08", source="Book: Two t summary (Q9)", topics="confidence intervals", type="select-all",
question=FROGS + "\n\nA two-sample t-test (equal variance) gives a difference (nonpreferred - preferred) of 68.8 eggs, SE = 66.4, and 54 df (critical t = 2.005). Which of these values are NOT in the 95% confidence interval for the difference? (Select all that apply.)",
options="""A) -92
B) -42
C) 2
D) 52
E) 102
F) 152
G) 202
H) 252""",
answer="A, G, H",
explanation="95% CI = 68.8 ± 2.005 × 66.4 = 68.8 ± 133.0, or about (-64.2, 201.8). -92, 202 and 252 fall outside.",
why_wrong="202 is just outside: the upper limit is 201.8.",
hint="CI = estimate ± critical t × SE."),

dict(id="ch16-book-09", source="Book: Two t summary (Q10A)", topics="t statistic, critical values", type="MC",
question="A two-sample t-test gives t = 1.04. If you didn't know the degrees of freedom, could you tell whether to reject the null at α = 0.05?",
options="""A) Yes: reject the null at α = 0.05
B) Yes: fail to reject the null at α = 0.05
C) No: I can't tell without the df""",
answer="B",
explanation="The critical t at α = 0.05 is never below 1.96 (that's its limit with infinite df), so a t of about 1 is never significant, whatever the df.",
why_wrong="""A) t = 1.04 is far too small.
C) For |t| below 1.96 the df don't matter.""",
hint="What's the smallest critical t can ever be?"),

dict(id="ch16-book-10", source="Book: Two t summary (Q10B)", topics="t statistic, critical values", type="MC",
question="For a different dataset, a t-test gives t = 2.2. If you didn't know the degrees of freedom, could you tell whether to reject the null at α = 0.05?",
options="""A) Yes: reject the null at α = 0.05
B) Yes: fail to reject the null at α = 0.05
C) No: I can't tell without the df""",
answer="C",
explanation="With many df the critical t is near 1.96, so 2.2 would be significant. With few df (e.g. 5 df, critical t = 2.57) it wouldn't.",
why_wrong="""A) and B) Values between about 2 and 4 depend on the df.""",
hint="How does the critical t change with sample size?"),

dict(id="ch16-book-11", source="Book: Two t summary (Q11-12)", topics="interpreting non-significant results", type="MC",
question=FROGS + "\n\nThe t-test gives p = 0.30, so we fail to reject the null. What does this mean?",
options="""A) The null is true: there's no effect of mate choice
B) The null is false: mate choice affects hatching
C) We don't know; we act as if it's true, but could be wrong""",
answer="C",
explanation="Failing to reject means the data are consistent with no difference, not that we've shown there is none. The CI (about -64 to 202 eggs) includes both no effect and fairly large effects.",
why_wrong="""A) Not rejecting doesn't prove the null.
B) There's no evidence against the null here.""",
hint="Does failing to reject prove anything?"),
]
