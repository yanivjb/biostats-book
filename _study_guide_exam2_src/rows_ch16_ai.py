from ai_helpers import V, r
from scipy.stats import t as T
import importlib.util, os
spec = importlib.util.spec_from_file_location('o16', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rows_ch16.py')); o = importlib.util.module_from_spec(spec); spec.loader.exec_module(o)
BP, TROUT, ATAXIA, FROGS = o.BP, o.TROUT, o.ATAXIA, o.FROGS
BP2 = """Two field studies each found that a nest-box treatment raised fledgling mass by 3 g (null value μ₀ = 0).

Study | n | SD (g)
P | 900 | 30
Q | 9 | 3

Equations: SE = s / √n, t = (x̄ - μ₀) / SE, d = (x̄ - μ₀) / s"""
ROWS = [
V("ch16-quiz-01", 1, question=BP2 + "\n\nMatch each study to its Cohen's d:\n\n1. Study P\n2. Study Q",
options="""A) d = 0.1
B) d = 1
C) d = 3
D) d = 10""", answer="1-A, 2-B", explanation="d = difference / SD. P: 3 / 30 = 0.1. Q: 3 / 3 = 1.", why_wrong="Divide by the SD, not the SE.", hint="d = difference ÷ SD."),
V("ch16-quiz-01", 2, question=BP + "\n\nMatch each study to its standard error:\n\n1. Study X\n2. Study Y",
options="""A) SE = 0.2
B) SE = 0.63
C) SE = 2
D) SE = 20""", answer="1-A, 2-B", explanation="X: 20 / √10,000 = 20 / 100 = 0.2. Y: 2 / √10 = 0.63.", why_wrong="SE = SD / √n.", hint="SD ÷ √n."),

V("ch16-quiz-02", 1, question=BP2 + "\n\nMatch each study to its t value:\n\n1. Study P\n2. Study Q",
options="""A) t = 0.1
B) t = 1
C) t = 3
D) t = 9""", answer="1-C, 2-C", explanation="P: SE = 30 / √900 = 1, t = 3 / 1 = 3. Q: SE = 3 / √9 = 1, t = 3 / 1 = 3. Same t, very different effect sizes.", why_wrong="Find each SE first.", hint="SE = SD / √n, then t = difference / SE."),
V("ch16-quiz-02", 2, question=BP + "\n\nIf Study Y had 40 people instead of 10 (same SD and difference), what would its t value be?",
options="""A) t = 3.16
B) t = 6.32
C) t = 12.6
D) t = 1""", answer="1-B" if False else "B",
explanation="SE = 2 / √40 = 0.316; t = 2 / 0.316 = 6.32. Quadrupling n doubles t.",
why_wrong="""A) That's t with n = 10.
C) That multiplies by 4 instead of √4.
D) That's d.""", hint="Quadrupling n halves the SE."),

V("ch16-quiz-03", 1, question=BP2 + "\n\nBoth studies have t = 3, but Study P has d = 0.1 and Study Q has d = 1. Which statement is correct?",
options="""A) Same t, but Study Q shows a much larger effect
B) Same t, so the effects are the same size
C) Study P has the larger effect because it has more data
D) Neither is significant because their t values are equal""", answer="A",
explanation="t mixes effect size and sample size. Q's effect is a full SD; P's is a tenth of an SD but detected thanks to its huge sample.",
why_wrong="""B) Equal t doesn't mean equal effects.
C) Sample size doesn't change effect size.
D) Equal t says nothing about non-significance.""", hint="What does d measure that t doesn't?"),
V("ch16-quiz-03", 2, question=BP + "\n\nStudy X has a tiny effect (d = 0.1) but the smaller p-value. Why?",
options="""A) Its huge sample makes the SE tiny, so t is large
B) Its large SD makes the difference more convincing
C) Its effect is actually larger than Study Y's effect
D) p-values measure the size of an effect directly""", answer="A",
explanation="SE = 20 / 100 = 0.2, so even a small difference is many SEs from zero.",
why_wrong="""B) A larger SD lowers t.
C) d = 0.1 vs 1.
D) p mixes effect size with sample size.""", hint="What does n do to the SE?"),

V("ch16-quiz-04", 1, question=BP + "\n\nWhich study has the larger effect of the drug on blood pressure, relative to individual variation?",
options="""A) Study X
B) Study Y
C) We can't tell from these numbers""", answer="B",
explanation="Effect size (d) is 1 for Y and 0.1 for X: relative to individual variation, Y's effect is ten times larger.",
why_wrong="""A) X has the smaller p-value, but the smaller d.
C) We can calculate d from these numbers.""", hint="Compare Cohen's d."),
V("ch16-quiz-04", 2, question=BP2 + "\n\nBoth studies give the same p-value (t = 3). Which study's null hypothesis is more likely to be false?",
options="""A) Study P, because its sample is larger
B) Study Q, because its effect is larger
C) We can't tell from these p-values""", answer="C",
explanation="A p-value is the probability of data this extreme if the null were true, not the probability the null is false.",
why_wrong="A) and B) p-values don't give the probability a hypothesis is true or false.", hint="What does a p-value condition on?"),

V("ch16-quiz-05", 1, question="40 lizards had a mean sprint speed of 2.1 m/s, with a 95% CI of 1.9 to 2.3 m/s. Mark each statement as OK or Wrong:\n\n1. If we repeated this study many times, about 95% of intervals built this way would contain the true mean.\n2. 95% of lizards sprint between 1.9 and 2.3 m/s.\n3. A 90% CI from the same data would be narrower.\n4. With 160 lizards (and similar data), the 95% CI would be about half as wide.",
options="""A) OK
B) Wrong""", answer="1-A, 2-B, 3-A, 4-A",
explanation="1) OK: correct interpretation. 2) Wrong: the CI is about the mean, not individuals. 3) OK: less confidence → narrower. 4) OK: 4× n halves the SE.",
why_wrong="CIs describe uncertainty in the mean.", hint="Mean vs individuals; confidence vs width."),
V("ch16-quiz-05", 2, question="25 people had a mean body temperature of 98.52 °F, with a 95% CI of 98.24 to 98.80 °F. Mark each statement as OK or Wrong:\n\n1. Values outside the interval, like 98.0 °F, are implausible for the true mean.\n2. The interval would be wider with only 10 people.\n3. There is a 95% chance the sample mean is between 98.24 and 98.80 °F.\n4. Most people's temperatures are between 98.24 and 98.80 °F.",
options="""A) OK
B) Wrong""", answer="1-A, 2-A, 3-B, 4-B",
explanation="1) OK: values outside a 95% CI would be rejected at α = 0.05. 2) OK: smaller n → bigger SE. 3) Wrong: the sample mean (98.52) is known and is in the interval by construction. 4) Wrong: individuals vary much more than the mean.",
why_wrong="The CI is about the population mean.", hint="What is the interval about?"),

V("ch16-hw-01", 1, image="ch16-hw-trout.png", question=TROUT + "\n\nThe plot shows each stream and the group means with 95% confidence intervals. Which statements are consistent with the plot? (Select all that apply.)",
options="""A) The CI for streams with trout is narrower
B) The CI for streams without trout is narrower
C) Survival varied more among streams without trout
D) Every stream without trout had higher survival than every stream with trout""", answer="A, C",
explanation="Streams with trout cluster tightly (variance 0.00088), giving a narrow CI; streams without trout vary widely (0.01074). The groups overlap, so D is false.",
why_wrong="""B) The no-trout CI is wider.
D) The groups overlap.""", hint="Look at the spread of points in each group."),
V("ch16-hw-01", 2, image="ch16-hw-trout.png", question=TROUT + "\n\nThe plot shows each stream and the group means with 95% confidence intervals. Why is the CI wider for streams without trout, even though both groups have six streams?",
options="""A) Survival varies more among streams without trout
B) The mean survival is higher in streams without trout
C) Streams without trout had fewer salmon in them
D) The CI is always wider for the reference group""", answer="A",
explanation="With equal n, CI width depends on the SD. The no-trout variance is about 12 times larger.",
why_wrong="""B) The mean doesn't set the width.
C) Both have n = 6 streams.
D) No such rule.""", hint="CI width = critical t × SD / √n."),

V("ch16-hw-02", 1, question="Two groups of 8 frogs have jumping-distance variances of 120 and 150 cm². Using the rule of thumb (OK if one variance is less than about 5 times the other), how comfortable are you assuming equal variance?",
options="""A) Comfortable: the ratio is only about 1.25
B) Nervous: the variances are not identical
C) Can't say without running a formal test""", answer="A",
explanation="150 / 120 = 1.25, far below 5.",
why_wrong="""B) Sample variances never match exactly.
C) The rule of thumb is enough here.""", hint="Divide the larger variance by the smaller."),
V("ch16-hw-02", 2, question=TROUT + "\n\nWhat is the ratio of the larger variance to the smaller one?",
options="""A) About 1.2
B) About 5
C) About 12
D) About 120""", answer="C",
explanation="0.01074 / 0.00088 = 12.2.",
why_wrong="""A) Compares the means, not the variances.
B) That's the rule-of-thumb cutoff.
D) Off by a factor of 10.""", hint="Divide 0.01074 by 0.00088."),

V("ch16-hw-03", 1, question=TROUT + "\n\nWhat is the pooled standard deviation? (The pooled variance is the average of the two variances, since n is equal.)",
answer=r(((0.01074+0.00088)/2)**0.5,4), explanation="Pooled variance = (0.01074 + 0.00088) / 2 = 0.00581; pooled SD = √0.00581 = 0.0762.", hint="Average the variances, then take the square root."),
V("ch16-hw-03", 2, question="Two groups of 11 lizards have variances in body temperature of 2.4 and 3.6 °C². What is the pooled variance?",
answer=r((10*2.4+10*3.6)/20,2), explanation="(10 × 2.4 + 10 × 3.6) / 20 = 3.0. With equal n it's the average.", hint="Equal n → average the variances."),

V("ch16-hw-04", 1, question=TROUT + "\n\nThe pooled SD is 0.0762. If the difference in means had been 0.10 instead of 0.041, how big would the effect be?\n\nSize | Cohen's d\nTiny | 0.01 to 0.20\nSmall | 0.20 to 0.50\nMedium | 0.50 to 0.80\nLarge | 0.80 to 1.20\nVery large | 1.20 to 2.00\nHuge | > 2.00",
options="""A) A small effect
B) A medium effect
C) A very large effect
D) A huge effect""", answer="C",
explanation="d = 0.10 / 0.0762 = 1.31, very large.",
why_wrong="""A) and B) Too small.
D) Not above 2.""", hint="Difference ÷ pooled SD."),
V("ch16-hw-04", 2, question=TROUT + "\n\nTo calculate Cohen's d for these data, we divide the difference in means (0.041) by:",
options="""A) The pooled standard deviation, 0.0762
B) The standard error of the difference, 0.044
C) The pooled variance, 0.00581
D) The difference's 95% confidence interval""", answer="A",
explanation="d = 0.041 / 0.0762 = 0.54.",
why_wrong="""B) Dividing by the SE gives t.
C) Variance has squared units.
D) A CI isn't a single scale.""", hint="Effect size uses the SD."),

V("ch16-hw-05", 1, question=TROUT + "\n\nThe pooled variance is 0.00581 and the difference in means is 0.041. The SE of the difference is 0.044. What is t? (Report to two decimals.)",
answer=r(0.041/0.044,2), explanation="t = 0.041 / 0.044 = 0.93.", hint="Difference ÷ SE."),
V("ch16-hw-05", 2, question="Two groups of 8 frogs have a pooled variance of 50. What is the standard error of the difference in means? (Report to two decimals.)",
answer=r((50*(1/8+1/8))**0.5,2), explanation="SE = √[50 × (1/8 + 1/8)] = √12.5 = 3.54.", hint="√[s²ₚ (1/n₁ + 1/n₂)]."),

V("ch16-hw-06", 1, question=TROUT + "\n\ntest | difference (absent - present) | 95% CI | p-value\ntwo-sample t | 0.041 | (-0.057, 0.139) | 0.374\nWelch's t | 0.041 | (-0.068, 0.150) | 0.389\n\nWhy is Welch's CI slightly wider?",
options="""A) It doesn't assume equal variance and uses fewer df
B) It uses a different estimate of the difference in means
C) It assumes the data are not normally distributed
D) It always gives exactly the same CI as the standard test""", answer="A",
explanation="Welch's test estimates each group's variance separately and adjusts the df down, giving a larger critical t.",
why_wrong="""B) The difference is 0.041 in both.
C) Welch's test still assumes normality.
D) They differ here.""", hint="Compare the assumptions."),
V("ch16-hw-06", 2, question=TROUT + "\n\ntest | difference (absent - present) | 95% CI | p-value\ntwo-sample t | 0.041 | (-0.057, 0.139) | 0.374\nWelch's t | 0.041 | (-0.068, 0.150) | 0.389\n\nDo the two tests lead to the same conclusion at α = 0.05?",
options="""A) Yes: both fail to reject the null
B) Yes: both reject the null
C) No: only Welch's test rejects
D) No: only the standard test rejects""", answer="A",
explanation="Both p-values are well above 0.05, and both CIs include 0.",
why_wrong="B), C) and D) Both p > 0.05.", hint="Compare each p-value to 0.05."),

V("ch16-hw-07", 1, question=TROUT + "\n\nTRUE or FALSE: The 95% CI for the difference in survival (-0.057 to 0.139) includes values large enough to matter for salmon conservation.",
options="""A) TRUE
B) FALSE""", answer="A",
explanation="A 14-percentage-point drop in survival would matter, and it's inside the interval. We can't rule out a meaningful effect.",
why_wrong="FALSE: the upper end (0.139) is a big change in survival.", hint="Look at the upper end of the CI."),
V("ch16-hw-07", 2, question=TROUT + "\n\nTRUE or FALSE: With p = 0.37 and only six streams per group, this study had limited power to detect a moderate effect of brook trout.",
options="""A) TRUE
B) FALSE""", answer="A",
explanation="Small samples and high variability give wide CIs and low power, so failing to reject says little.",
why_wrong="FALSE: six streams per group is a small study.", hint="What limits power?"),

V("ch16-chimein-01", 1, question=ATAXIA + "\n\nIf the pooled SD had been 46.8 days (twice as large) with the same difference in means, what would |d| be?",
options="""A) |d| ≈ 0.9, large
B) |d| ≈ 1.8, large
C) |d| ≈ 3.6, huge
D) |d| ≈ 0.45, small""", answer="A",
explanation="|d| = 42.7 / 46.8 = 0.91. Doubling the SD halves d.",
why_wrong="""B) That's with the original SD.
C) Doubles d instead of halving it.
D) Halves it twice.""", hint="d = difference ÷ SD."),
V("ch16-chimein-01", 2, question=ATAXIA + "\n\nTo calculate Cohen's d for the difference in lifespan, which value do we divide 42.7 days by?",
options="""A) 23.4, the pooled SD
B) 549.3, the pooled variance
C) 13.5, the SE of the difference
D) 6, the sample size per group""", answer="A",
explanation="d = 42.7 / 23.4 = 1.82.",
why_wrong="""B) Variance has squared units.
C) Dividing by the SE gives t.
D) n isn't part of d.""", hint="Effect size uses the SD."),

V("ch16-chimein-02", 1, question=ATAXIA + "\n\nThe two-sample t-test gives p = 0.01. Which statement is correct?",
options="""A) If exercise had no effect, a difference this big would be rare
B) There is a 1% chance that exercise has no effect on lifespan
C) There is a 99% chance that exercise increases lifespan
D) The effect of exercise on lifespan must be very large""", answer="A",
explanation="p is the probability of a difference at least this large if the null were true.",
why_wrong="""B) and C) p isn't a probability about hypotheses.
D) p doesn't measure effect size.""", hint="p assumes the null."),
V("ch16-chimein-02", 2, question=ATAXIA + "\n\nA classmate says, \"p = 0.01, so there's a 99% chance exercise extends lifespan.\" What's wrong?",
options="""A) p is computed assuming the null; it isn't P(null)
B) Nothing; 1 - p is the chance the alternative is true
C) The p-value should have been compared with 0.01
D) The classmate should have used the Welch p-value""", answer="A",
explanation="p = P(data this extreme | null), not P(null | data).",
why_wrong="""B) 1 - p isn't the probability of the alternative.
C) and D) Irrelevant to the misinterpretation.""", hint="Prosecutor's fallacy."),

V("ch16-chimein-03", 1, question=ATAXIA + "\n\nThe variances are 224.3 (no exercise) and 874.4 (exercise). Why might a researcher choose Welch's t-test here?",
options="""A) The variances differ by a factor of about 4
B) The means differ by about 43 days
C) The sample sizes are unequal in the two groups
D) Welch's test always gives smaller p-values""", answer="A",
explanation="874.4 / 224.3 = 3.9: near the rule-of-thumb limit, so Welch's test is a reasonable check.",
why_wrong="""B) The difference in means isn't the issue.
C) Both groups have n = 6.
D) Welch's p is usually larger.""", hint="Which assumption does Welch's test drop?"),
V("ch16-chimein-03", 2, question=ATAXIA + "\n\ntest | difference | 95% CI | p-value\nstandard (equal variance) t | -42.7 | (-72.8, -12.5) | 0.010\nWelch's t (unequal variance) | -42.7 | (-74.3, -11.0) | 0.015\n\nDoes dropping the equal-variance assumption change the conclusion at α = 0.05?",
options="""A) No: both tests reject the null
B) Yes: only the standard test rejects
C) Yes: only Welch's test rejects
D) No: neither test rejects the null""", answer="A",
explanation="Both p-values are below 0.05, and neither CI includes 0.",
why_wrong="B), C) and D) Both p < 0.05.", hint="Compare each p to 0.05."),

V("ch16-chimein-05", 1, question=ATAXIA + "\n\nIf the two-sample t-test had given p = 0.08, at α = 0.05 we would ____ the null hypothesis.",
options="""A) reject
B) accept
C) fail to reject
D) fail to accept""", answer="C",
explanation="0.08 > 0.05, so we fail to reject. We never 'accept' or 'prove' the null.",
why_wrong="""A) p > α.
B) and D) We never accept the null.""", hint="Compare p with α."),
V("ch16-chimein-05", 2, question=ATAXIA + "\n\nThe two-sample t-test gives t = -3.15 with 10 df. Where does the 10 come from?",
options="""A) n₁ + n₂ - 2
B) n₁ - 1
C) n₁ + n₂
D) n₁ + n₂ - 1""", answer="A",
explanation="A two-sample t-test has n₁ + n₂ - 2 df.",
why_wrong="""B) That's one group.
C) and D) Subtract one df per group.""", hint="One df lost per group mean."),

V("ch16-chimein-06", 1, question=ATAXIA + "\n\nWhich change to the study design would have made the lifespan p-value trustworthy? (Pick the two best.)",
options="""A) Deciding to compare lifespans before collecting any data
B) Using Welch's t-test instead of the standard t-test
C) Testing lifespan in a new, independent set of mice
D) Reporting the p-value to more decimal places""", answer="A, C",
explanation="The problem is that the hypothesis came from the data. Pre-specifying it, or testing it on new data, fixes that.",
why_wrong="""B) Welch's test doesn't fix data-driven hypotheses.
D) Precision isn't the issue.""", hint="When was the hypothesis formed?"),
V("ch16-chimein-06", 2, question=ATAXIA + "\n\nWhy does testing a hypothesis suggested by the data inflate false positives?",
options="""A) We notice differences that are large by chance, then test them
B) The data become more variable once we look at them
C) The sample size shrinks once we pick a hypothesis
D) It doesn't; p-values are valid whenever we compute them""", answer="A",
explanation="If we only test differences that already look big, many will be flukes, so far more than 5% of tests of true nulls will be 'significant'.",
why_wrong="""B) and C) Looking doesn't change the data.
D) p-values assume a pre-specified test.""", hint="Which differences catch our eye?"),

V("ch16-chimein-08", 1, question=ATAXIA + "\n\nThe 95% CI for the difference (no exercise - exercise) is -72.8 to -12.5 days. TRUE or FALSE: If this study were repeated many times, about 95% of the intervals built this way would contain the true difference.",
options="""A) TRUE
B) FALSE""", answer="A",
explanation="That's the correct interpretation of a 95% CI.", why_wrong="FALSE: this is the correct interpretation.", hint="The 95% is about the procedure."),
V("ch16-chimein-08", 2, question=ATAXIA + "\n\nThe 95% CI for the difference (no exercise - exercise) is -72.8 to -12.5 days. TRUE or FALSE: Because 0 is not in the interval, a two-tailed test at α = 0.05 rejects the null of no difference.",
options="""A) TRUE
B) FALSE""", answer="A",
explanation="A 95% CI excludes the null value exactly when a two-tailed test at α = 0.05 rejects (p = 0.010 here).", why_wrong="FALSE: CIs and tests agree.", hint="Is 0 inside the interval?"),

V("ch16-chimein-09", 1, question="Study A (n = 20) finds p = 0.04; study B (n = 2,000) finds p = 0.0001. Which statement is correct?",
options="""A) Study B's effect isn't necessarily larger; its sample is much larger
B) Study B's effect must be larger because its p-value is smaller
C) Study A's effect must be larger because its sample is smaller
D) Both studies must have found exactly the same effect size""", answer="A",
explanation="p depends on both effect size and sample size, so smaller p doesn't imply a bigger effect.",
why_wrong="""B) and C) p-values don't rank effect sizes.
D) Nothing tells us they're equal.""", hint="What else changes p?"),
V("ch16-chimein-09", 2, question="Which is the best way to communicate how large a difference between two groups is?",
options="""A) Report an effect size such as Cohen's d, with its CI
B) Report the p-value with as many decimal places as possible
C) Report whether the result was significant at α = 0.05
D) Report the t statistic and its degrees of freedom""", answer="A",
explanation="Effect sizes describe magnitude; p-values, significance and t mix magnitude with sample size.",
why_wrong="""B), C) and D) All depend on n.""", hint="Magnitude, not evidence."),

V("ch16-book-01", 1, image="ch16-book-frogs.png", question=FROGS + "\n\nThe plot shows each mated pair and the group means with 95% CIs. What does the spread of points tell you?",
options="""A) Hatched eggs vary hugely among pairs in both treatments
B) Hatched eggs are nearly identical within each treatment
C) Only the preferred treatment shows much variation
D) Only the nonpreferred treatment shows much variation""", answer="A",
explanation="Both groups range from near 0 to around 900 eggs; variation within groups dwarfs the difference between them.",
why_wrong="""B) There's huge variation.
C) and D) Both groups vary similarly (variances 56,118 vs 67,412).""", hint="Look at the range of points in each group."),
V("ch16-book-01", 2, image="ch16-book-frogs.png", question=FROGS + "\n\nThe plot shows each mated pair and the group means with 95% CIs. What do the overlapping CIs suggest?",
options="""A) The data don't clearly show a difference between treatments
B) Preferred females clearly produce more hatched eggs
C) Nonpreferred females clearly produce more hatched eggs
D) The treatments definitely have identical means""", answer="A",
explanation="Broadly overlapping CIs suggest the difference may not be significant (p = 0.30). That's not proof the means are equal.",
why_wrong="""B) and C) The difference is uncertain.
D) Overlap doesn't prove equality.""", hint="Overlap ≠ identical."),

V("ch16-book-02", 1, image="ch16-book-frog-hists.png", question=FROGS + "\n\nThe figure shows histograms of hatched eggs, (A) with both treatments combined and (B) separately for each treatment. Why can the combined histogram be misleading for checking normality?",
options="""A) Mixing groups with different means can create odd shapes
B) Combining groups always makes the data look more normal
C) The combined plot has too many observations to judge
D) It isn't misleading; it's the best plot for this purpose""", answer="A",
explanation="The t-test assumes normal residuals within groups. Two normal groups with different means can make a lumpy or skewed combined histogram.",
why_wrong="""B) It can go either way.
C) More data helps judge shape.
D) Check within groups.""", hint="What does the t-test assume is normal?"),
V("ch16-book-02", 2, image="ch16-book-frog-hists.png", question=FROGS + "\n\nThe figure shows histograms of hatched eggs, (A) with both treatments combined and (B) separately for each treatment. The two-sample t-test assumes that ____ are normally distributed.",
options="""A) The values within each treatment (the residuals)
B) The values with both treatments combined
C) The two treatment means, compared to each other
D) The p-values from many repeated studies""", answer="A",
explanation="The assumption is about residuals: each value minus its group mean.",
why_wrong="""B) Combined data mix two means.
C) and D) Not the assumption.""", hint="Residuals."),

V("ch16-book-03", 1, question="Two groups of 15 tadpoles have growth-rate variances of 4.0 and 26.0. Should you feel comfortable assuming equal variance?",
options="""A) Yes
B) No
C) Maybe""", answer="B",
explanation="26.0 / 4.0 = 6.5, beyond the rule of thumb of about 5. Welch's t-test would be safer.",
why_wrong="A) and C) The ratio exceeds 5.", hint="Ratio of variances."),
V("ch16-book-03", 2, question=FROGS + "\n\nWhat is the ratio of the larger variance to the smaller one?",
options="""A) About 1.2
B) About 5
C) About 12
D) About 68""", answer="A",
explanation="67,412 / 56,118 = 1.20.",
why_wrong="""B) That's the rule-of-thumb cutoff.
C) That's the trout ratio.
D) That's the difference in means.""", hint="Divide the larger variance by the smaller."),

V("ch16-book-04", 1, question=FROGS + "\n\nWhat is the pooled standard deviation? (The pooled variance is 61,556.)",
answer=r(61556**0.5,1), explanation="√61,556 = 248.1 eggs.", hint="Square root of the pooled variance."),
V("ch16-book-04", 2, question="Group 1 has n = 11 and variance 40; group 2 has n = 21 and variance 70. What is the pooled variance?",
answer=r((10*40+20*70)/30,1), explanation="(10 × 40 + 20 × 70) / (11 + 21 - 2) = (400 + 1,400) / 30 = 60.", hint="Weight each variance by n - 1."),

V("ch16-book-05", 1, question=FROGS + "\n\nThe pooled SD is 248. If the difference in means had been 250 eggs instead of 68.8, how would you characterize the effect size?",
options="""A) Small (0.20 to 0.50)
B) Medium (0.50 to 0.80)
C) Large (0.80 to 1.20)
D) Huge (> 2.00)""", answer="C",
explanation="d = 250 / 248 = 1.01, large.",
why_wrong="""A) and B) Too small.
D) Not above 2.""", hint="Difference ÷ pooled SD."),
V("ch16-book-05", 2, question=FROGS + "\n\nThe pooled SD is 248 eggs and the difference in means is 68.8 eggs. What is Cohen's d?",
options="""A) 0.28
B) 1.04
C) 3.6
D) 68.8""", answer="A",
explanation="d = 68.8 / 248 = 0.28.",
why_wrong="""B) That's t (68.8 / SE of 66.4).
C) That's 248 / 68.8, upside down.
D) That's the raw difference.""", hint="Difference ÷ pooled SD."),

V("ch16-book-06", 1, question="A study reports Cohen's d = 1.5 but doesn't give the sample size. What can you conclude?",
options="""A) The effect is large, but we can't tell if p < 0.05
B) The null must be rejected, because the effect is large
C) The null must be true, because no p-value is given
D) The study must have had a large sample size""", answer="A",
explanation="d describes magnitude. Significance also depends on n: with 3 per group, even d = 1.5 may not be significant.",
why_wrong="""B) Small samples can miss large effects.
C) Missing p says nothing.
D) d doesn't reveal n.""", hint="What else does significance depend on?"),
V("ch16-book-06", 2, question=FROGS + "\n\nThe t-test gives p = 0.30 and d = 0.28. Which statement is best?",
options="""A) The estimated effect is small, and there's no clear difference
B) The effect is small, so the null hypothesis must be true
C) The effect is small, so the p-value must be wrong
D) The p-value shows that preferred females lay fewer eggs""", answer="A",
explanation="d describes the estimated size; p says the data are consistent with no difference. Neither proves the null.",
why_wrong="""B) Failing to reject isn't proof.
C) Small d and large p are consistent.
D) p > 0.05; no clear difference.""", hint="Size vs evidence."),

V("ch16-book-07", 1, question=FROGS + "\n\nIf the researchers had predicted in advance that preferred females would produce MORE hatched eggs, match each hypothesis for a one-tailed test:\n\n1. Null hypothesis\n2. Alternative hypothesis",
options="""A) Mean hatched eggs are the same or lower with preferred females
B) Mean hatched eggs are higher with preferred females
C) Mean hatched eggs differ between the treatments
D) Males prefer females that produce more offspring""", answer="1-A, 2-B",
explanation="A one-tailed alternative specifies the direction; the null covers everything else.", why_wrong="C) is two-tailed; D) isn't a statistical hypothesis.", hint="One direction."),
V("ch16-book-07", 2, question=FROGS + "\n\nWhich is a statistical null hypothesis for this study?",
options="""A) Population mean hatched eggs are equal in the two treatments
B) The sample mean hatched eggs are equal in the two treatments
C) Males can't tell preferred and nonpreferred females apart
D) Preferred females produce more hatched eggs than others""", answer="A",
explanation="Hypotheses are about populations. The sample means clearly differ (414 vs 345).",
why_wrong="""B) Sample means are known and differ.
C) That's a biological idea.
D) That's an alternative.""", hint="Population, not sample."),

V("ch16-book-08", 1, question=FROGS + "\n\nA two-sample t-test gives a difference of 68.8 eggs, SE = 66.4, and 54 df (critical t = 2.005). Which of these values ARE in the 95% CI for the difference? (Select all that apply.)",
options="""A) -100
B) 0
C) 150
D) 250""", answer="B, C",
explanation="68.8 ± 2.005 × 66.4 = 68.8 ± 133.1 → (-64.3, 201.9). 0 and 150 are inside.",
why_wrong="A) and D) are outside.", hint="Compute the interval first."),
V("ch16-book-08", 2, question=FROGS + "\n\nA two-sample t-test gives a difference of 68.8 eggs and SE = 66.4. What is t?",
options="""A) About 1.04
B) About 2.00
C) About 0.28
D) About 133""", answer="A",
explanation="t = 68.8 / 66.4 = 1.04.",
why_wrong="""B) That's the critical t.
C) That's d.
D) That's the CI half-width.""", hint="Difference ÷ SE."),

V("ch16-book-09", 1, question="A two-sample t-test gives t = 5.3. If you didn't know the degrees of freedom, could you tell whether to reject the null at α = 0.05?",
options="""A) Yes: reject
B) Yes: fail to reject
C) No: I can't tell""", answer="C",
explanation="Critical t is 2.0 to 2.8 for most studies, but with 1 df it's 12.7, so 5.3 wouldn't be significant. Without df, we can't be sure (though with any realistic df beyond 2, we'd reject).",
why_wrong="""A) With 1 or 2 df the critical t is above 4.3.
B) With 3 or more df, 5.3 is significant.""", hint="How large can the critical t get with very few df?"),
V("ch16-book-09", 2, question="A two-sample t-test gives t = 1.5. Could you reject the null at α = 0.05 with any number of degrees of freedom?",
options="""A) No: the critical t is never below 1.96
B) Yes: with enough df, 1.5 becomes significant
C) Yes: with very few df, 1.5 becomes significant""", answer="A",
explanation="The critical t (two-tailed, α = 0.05) approaches 1.96 from above as df grow, so 1.5 is never significant.",
why_wrong="""B) The critical value never drops below 1.96.
C) Fewer df make the critical value larger.""", hint="What's the smallest the critical t can be?"),

V("ch16-book-10", 1, question="A t-test gives t = 2.4. With which degrees of freedom would you reject the null at α = 0.05? (Critical t: 2.78 for 4 df; 2.09 for 20 df.)",
options="""A) 20 df but not 4 df
B) 4 df but not 20 df
C) Both 4 and 20 df
D) Neither 4 nor 20 df""", answer="A",
explanation="2.4 > 2.09 but 2.4 < 2.78.",
why_wrong="Compare 2.4 with each critical value.", hint="Is |t| above the critical value?"),
V("ch16-book-10", 2, question="Why does the same t value (say 2.2) lead to rejection in a large study but not in a very small one?",
options="""A) Few df mean fatter t tails and a larger critical value
B) Large studies use a smaller α than small studies do
C) Small studies always have larger effect sizes in practice
D) The t value means different things in each study""", answer="A",
explanation="With few df, the t has fatter tails, so the critical value is larger (2.57 for 5 df vs ~1.96 for large df).",
why_wrong="""B) α is the same.
C) Irrelevant.
D) t means the same thing.""", hint="How does the critical t change with df?"),

V("ch16-book-11", 1, question=FROGS + "\n\nThe 95% CI for the difference in hatched eggs is about -64 to 202. What does this tell us?",
options="""A) The data fit no difference and also fairly large effects
B) The true difference is definitely zero
C) The true difference is definitely large
D) Preferred females lay more eggs than nonpreferred""", answer="A",
explanation="The interval includes 0 and also differences of 200 eggs; the data are too imprecise to say much.",
why_wrong="""B) and C) The CI includes both.
D) The estimate is in the other direction, and uncertain.""", hint="What range of values does the CI include?"),
V("ch16-book-11", 2, question=FROGS + "\n\nThe t-test gives p = 0.30. What would be needed to get a clearer answer about whether mate choice affects hatched eggs?",
options="""A) A larger sample, to shrink the SE and narrow the CI
B) A smaller α, such as 0.01, to make the test stricter
C) Switching to Welch's t-test on the same data
D) Nothing more; p = 0.30 proves there is no effect""", answer="A",
explanation="More pairs would reduce the SE, narrowing the CI and increasing power.",
why_wrong="""B) A smaller α makes rejecting harder.
C) The variances are similar; Welch won't help.
D) Failing to reject isn't proof.""", hint="What controls the width of the CI?"),
]
