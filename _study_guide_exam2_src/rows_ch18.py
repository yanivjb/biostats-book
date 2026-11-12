QUIZ_TABLE = """source | df | Sum Sq | Mean Sq | F | p-value
Model | [A] | 5 | [C] | [E] | 0.48
Residuals | [B] | 52 | [D] | |"""
CUCKOO = """To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species."""
CUCKOO_SUM = """host | mean egg length (mm) | variance | n
Hedge Sparrow | 23.12 | 1.142 | 14
Meadow Pipit | 22.30 | 0.848 | 45
Pied Wagtail | 22.90 | 1.140 | 15
Robin | 22.58 | 0.469 | 16
Tree Pipit | 23.09 | 0.813 | 15
Wren | 21.13 | 0.553 | 15"""
CUCKOO_TUKEY = """Tukey post-hoc test (only significant pairs shown, adjusted p < 0.05):
Hedge Sparrow - Meadow Pipit: p = 0.043
Hedge Sparrow - Wren: p < 0.001
Meadow Pipit - Tree Pipit: p = 0.048
Meadow Pipit - Wren: p < 0.001
Pied Wagtail - Wren: p < 0.001
Robin - Wren: p < 0.001
Tree Pipit - Wren: p < 0.001
(All other pairs: p > 0.2)"""
CRABS = """To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed."""
CRAB_SUM = """crabType | mean | variance | n
female | 1.673 | 0.0412 | 19
intact male | 1.317 | 0.0521 | 19
male major removed | 1.456 | 0.0497 | 18
male minor removed | 1.253 | 0.0392 | 20"""
CRAB_ANOVA = """lm(bodyTemperature ~ crabType, data = crabs) |> anova()

          Df Sum Sq Mean Sq F value    Pr(>F)
crabType   3 1.9964 0.66546  14.654 1.521e-07
Residuals 72 3.2696 0.04541"""
CRAB_TUKEY = """aov(bodyTemperature ~ crabType, data = crabs) |> TukeyHSD()

comparison | diff | p adj
intact male - female | -0.355 | < 0.001
male major removed - female | -0.217 | 0.015
male minor removed - female | -0.420 | < 0.001
male major removed - intact male | 0.138 | 0.208
male minor removed - intact male | -0.065 | 0.778
male minor removed - male major removed | -0.203 | 0.023"""
APHID = """Pea aphids can carry the bacterium Rickettsiella, which may change their body color. Researchers compared color among aphids that never had the bacterium (original), aphids born infected to lab-infected mothers (infected), and aphids born uninfected to lab-infected mothers (uninfected).

aov(color ~ infectionStatus, data = rickettsia) |> summary()
                Df Sum Sq Mean Sq F value   Pr(>F)
infectionStatus  2 2379.3  1189.6   65.59 1.73e-11
Residuals       29  525.9    18.1

aov(color ~ infectionStatus, data = rickettsia) |> TukeyHSD()
comparison | diff | lwr | upr | p adj
original - infected | -17.3 | -21.7 | -12.9 | < 0.0001
uninfected - infected | -19.2 | -23.9 | -14.4 | < 0.0001
uninfected - original | -1.9 | -6.5 | 2.8 | 0.58"""

ROWS = [
# ---------------- Quiz: ANOVA (Nov 2) ----------------
dict(id="ch18-quiz-01", source="ANOVA quiz (2026), Q1", topics="ANOVA table, degrees of freedom, mean squares", type="matching",
question="A study has 30 samples spread across 4 groups. Complete its ANOVA table:\n\n" + QUIZ_TABLE + "\n\nMatch each missing entry to its value:\n\n1. [A] model df\n2. [B] residual df\n3. [C] model mean square\n4. [D] residual mean square\n5. [E] F",
options="""A) 3
B) 26
C) 1.67
D) 2
E) 0.83""",
answer="1-A, 2-B, 3-C, 4-D, 5-E",
explanation="df model = groups - 1 = 3. df residual = n - groups = 30 - 4 = 26. MS model = 5 / 3 = 1.67. MS residual = 52 / 26 = 2. F = 1.67 / 2 = 0.83.",
why_wrong="Common mistakes: residual df = n - 1 (29), or F = SS model / SS residual (0.096).",
hint="Mean square = sum of squares / df; F = MS model / MS residual."),

dict(id="ch18-quiz-02", source="ANOVA quiz (2026), Q2", topics="NHST", type="MC",
question="A study of 30 samples in 4 groups gives F = 0.83 (3 and 26 df), p = 0.48. What do you do to the null hypothesis at α = 0.05?",
options="""A) Reject it
B) Fail to reject it
C) Accept it""",
answer="B",
explanation="p = 0.48 > 0.05. An F below 1 means the groups differ less than we'd expect by chance alone.",
why_wrong="""A) p is far above α.
C) We never accept the null.""",
hint="Compare p with α."),

dict(id="ch18-quiz-03", source="ANOVA quiz (2026), Q3", topics="R squared", type="numeric",
question="In an ANOVA, SS model = 5 and SS residual = 52. What proportion of the variance in the response does the model explain in this study (R²)?",
answer="0.088", explanation="R² = SS model / SS total = 5 / (5 + 52) = 5 / 57 = 0.088.",
why_wrong="Common mistake: SS model / SS residual (5 / 52 = 0.096). The denominator is the total.",
hint="SS total = SS model + SS residual."),

dict(id="ch18-quiz-04", source="ANOVA quiz (2026), Q4", topics="R squared, generalizing", type="TF",
question="An ANOVA in one study gives R² = 0.088. TRUE or FALSE: the explanatory variable explains 8.8% of the variation in the response in nature.",
options="""A) TRUE
B) FALSE""",
answer="B",
explanation="R² describes this study only. It depends on which groups were included, how many samples were in each, and the conditions of the study, so it doesn't carry over to nature.",
why_wrong="TRUE: R² can't be extrapolated beyond the study that produced it.",
hint="Would R² change if the study had sampled different groups, or different numbers per group?"),

dict(id="ch18-quiz-05", source="ANOVA quiz (2026), Q5", topics="ANOVA assumptions", type="select-all",
question="Which of the following are assumptions of an ANOVA? (Select all that apply.)",
options="""A) Random and independent values of the response variable (conditional on the explanatory variable)
B) Normal distributions (of residuals) for each population
C) Equal variances for all groups
D) The frequency of each group in the study is proportional to its frequency in nature""",
answer="A, B, C",
explanation="ANOVA assumes independent, unbiased data, normally distributed residuals, and equal variance among groups. Group sizes don't need to match nature.",
why_wrong="D) Sample sizes per group are a design choice, not an assumption (though they do affect R²).",
hint="Which option is about study design rather than the data-generating process?"),

dict(id="ch18-quiz-06", source="ANOVA quiz (2026), Q6", topics="post-hoc tests", type="MC",
question="After you reject the null hypothesis in an ANOVA, you:",
options="""A) Assume all group means differ, while acknowledging this could be a false positive
B) Conduct standard t-tests between all pairs to find out which groups differ
C) Conduct post-hoc tests to see which means differ""",
answer="C",
explanation="Rejecting the ANOVA null says not all means are equal, not that all differ. Post-hoc tests (e.g. Tukey) find which pairs differ while controlling the overall false positive rate.",
why_wrong="""A) Rejecting doesn't mean every mean differs.
B) Uncorrected pairwise t-tests bring back the multiple testing problem.""",
hint="What does the ANOVA's alternative hypothesis actually say?"),

dict(id="ch18-quiz-07", source="ANOVA quiz (2026), Q7", topics="multiple testing", type="open", include="no",
question="Explain the multiple testing problem, and how an ANOVA followed by post-hoc tests addresses it.",
answer="Model answer: Every test has a chance (α) of a false positive when the null is true, so running many tests makes it likely that at least one is 'significant' by chance. With 4 groups there are 6 pairwise tests, and the chance of at least one false positive is about 26%, not 5%. An ANOVA tests a single null (all means are equal) at α = 0.05. Only if it's rejected do we do post-hoc tests, which adjust their p-values so the overall false positive rate across all comparisons stays near 5%.",
explanation="The key ideas: many tests inflate the false positive rate, an ANOVA does one test, and post-hoc tests correct for multiple comparisons.",
hint="What happens to the chance of at least one false positive as you run more tests?"),

dict(id="ch18-quiz-08", source="ANOVA quiz (2026), Q8", topics="ANOVA calculations, R", type="MC",
question="""A student wrote this code to calculate an ANOVA by hand (on PLP1 gene expression across groups of patients):

summarise(n_group = n_distinct(group), n_total = n(),
          df_group = n_group - 1,
          df_error = n_total - n_group,
          ss_group = sum(group_sqrd_dev),
          ss_error = sum(error_sqrd_dev),
          ms_group = ss_group / df_group,
          ms_error = ss_error / df_error,
          f_val = ss_group / ss_error,
          p_val = pf(q = f_val, df1 = df_group, df2 = df_error, lower.tail = FALSE))

Which line has a mistake?""",
options="""A) df_error = n_total - n_group
B) ms_group = ss_group / df_group
C) f_val = ss_group / ss_error
D) p_val = pf(q = f_val, df1 = df_group, df2 = df_error, lower.tail = FALSE)""",
answer="C",
explanation="F is a ratio of mean squares, not sums of squares: f_val = ms_group / ms_error.",
why_wrong="""A) Correct: error df = n - number of groups.
B) Correct.
D) Correct: F tests use the upper tail.""",
hint="Is F a ratio of sums of squares or of mean squares?"),

dict(id="ch18-quiz-09", source="ANOVA quiz (2026), Q9", topics="post-hoc tests, writing results", type="MC",
question=APHID + "\n\nWhich summary is correct?",
options="""A) Infection status didn't affect color (p = 0.58)
B) All three groups differ significantly from each other in color
C) Infected differ from the other two, which don't differ from each other
D) Original aphids differ in color from the other two groups""",
answer="C",
explanation="The ANOVA rejects equal means (F = 65.6, df = 2 and 29, p = 1.7 × 10⁻¹¹). The Tukey tests show infected aphids differ from both other groups, which don't differ from each other.",
why_wrong="""A) 0.58 is the p-value for just one pair; the overall ANOVA is highly significant.
B) Original vs uninfected isn't significant.
D) The odd group out is infected, not original.""",
hint="Look at the Tukey table: which comparisons have small p-values?"),

dict(id="ch18-quiz-10", source="ANOVA quiz (2026), Q9", topics="post-hoc tests, writing results", type="open", include="no",
question=APHID + "\n\nWrite a brief paragraph about these results, including significance groups.",
answer="Model answer: Aphid color differed among infection groups (one-way ANOVA: F = 65.6, df = 2 and 29, p = 1.7 × 10⁻¹¹). A Tukey post-hoc test showed that aphids born infected differed from both aphids that never carried Rickettsiella (difference = 17.3 color units, 95% CI 12.9 to 21.7) and aphids born uninfected to infected mothers (19.2, 95% CI 14.4 to 23.9; both p < 0.0001), while those two groups didn't differ (1.9, p = 0.58). In significance groups: infected = a; original and uninfected = b. So it's carrying the bacterium, not having an infected mother, that is associated with color change.",
explanation="A good summary reports the overall test, the post-hoc result with effect sizes and CIs, significance groups, and the biological meaning.",
hint="Start with the ANOVA, then use the Tukey table to say which groups differ."),

# ---------------- Homework (cuckoo eggs) ----------------
dict(id="ch18-hw-01", source="ANOVA homework, Q1", topics="multiple testing, pairwise comparisons", type="numeric",
question=CUCKOO + "\n\nWith six groups, how many possible pairwise comparisons are there?",
answer="15", explanation="k(k - 1) / 2 = 6 × 5 / 2 = 15.",
why_wrong="Common mistake: 6 × 5 = 30, counting each pair twice.",
hint="Each pair counts once: A vs B is the same as B vs A."),

dict(id="ch18-hw-02", source="ANOVA homework, Q2", topics="multiple testing", type="numeric",
question=CUCKOO + "\n\nIf we conducted all 15 pairwise comparisons and every null hypothesis were true, what is the probability of rejecting at least one true null at α = 0.05? (Treat the tests as independent.)",
answer="0.537", explanation="P(no false positives) = 0.95¹⁵ = 0.463, so P(at least one) = 1 - 0.463 = 0.537.",
why_wrong="Common mistake: 15 × 0.05 = 0.75. Adding probabilities overcounts.",
hint="Find the chance of no false positives in all 15 tests first."),

dict(id="ch18-hw-03", source="ANOVA homework, Q3", topics="sums of squares, deviations", type="matching",
question=CUCKOO + "\n\nEach plot shows cuckoo egg lengths by host (colored points), the group means (colored lines) and the grand mean (black line). Match each kind of deviation to the plot that shows it:\n\n1. Error deviations\n2. Model deviations\n3. Total deviations",
image="ch18-hw-cuckoo-deviations.png",
options="""A) Plot A
B) Plot B
C) Plot C""",
answer="1-B, 2-A, 3-C",
explanation="A: group means to the grand mean (model). B: each egg to its group mean (error). C: each egg to the grand mean (total).",
why_wrong="Check where each vertical line starts and ends.",
hint="In which plot do the lines never reach the points?"),

dict(id="ch18-hw-04", source="ANOVA homework, Q4-5", topics="equal variance assumption", type="MC",
question=CUCKOO + "\n\n" + CUCKOO_SUM + "\n\nWhat is the largest fold difference in variance between host species, and how worried should we be about the equal variance assumption?",
options="""A) Less than two-fold; not a concern
B) Between two- and five-fold; probably not a major concern
C) Between five- and ten-fold; somewhat worrisome
D) More than ten-fold; a big concern, so we should transform or use Welch's ANOVA""",
answer="B",
explanation="Largest / smallest = 1.142 / 0.469 = 2.4-fold, within the rule of thumb (less than about 5), so the equal variance assumption is probably fine.",
why_wrong="""A) 2.4 is more than two-fold.
C) and D) Overstate the difference.""",
hint="Divide the largest variance by the smallest."),

dict(id="ch18-hw-05", source="ANOVA homework, Q6-7", topics="ANOVA, NHST", type="MC",
question=CUCKOO + """

lm(egg_length ~ host_species, data = cuckoo) |> anova()

              Df Sum Sq Mean Sq F value    Pr(>F)
host_species   5 42.940  8.5879  10.388 3.152e-08
Residuals    114 94.248  0.8267

What is the p-value, and what do we do with the null hypothesis at α = 0.05?""",
options="""A) Less than 10⁻¹⁰; reject
B) Between 10⁻¹⁰ and 10⁻³; reject
C) Between 10⁻³ and 0.05; reject
D) Greater than 0.05; fail to reject""",
answer="B",
explanation="p = 3.2 × 10⁻⁸ is between 10⁻¹⁰ and 10⁻³, far below 0.05, so we reject the null that all hosts have the same mean egg length.",
why_wrong="Common mistake: misreading scientific notation. 3.2e-08 means 0.000000032.",
hint="e-08 means ×10⁻⁸."),

dict(id="ch18-hw-06", source="ANOVA homework, Q8", topics="post-hoc tests, significance groups", type="select-all",
question=CUCKOO + "\n\n" + CUCKOO_TUKEY + "\n\nWhich host species (if any) is significantly different from all the others? (Select all that apply.)",
options="""A) Wren
B) Meadow Pipit
C) Robin
D) Hedge Sparrow
E) Pied Wagtail
F) Tree Pipit
G) None""",
answer="A",
explanation="Wren differs from all five other hosts (cuckoo eggs in wren nests are much smaller). Meadow Pipit differs from only three of the five.",
why_wrong="B) Meadow Pipit doesn't differ significantly from Pied Wagtail or Robin.",
hint="Which host appears in a significant comparison with every other host?"),

dict(id="ch18-hw-07", source="ANOVA homework, Q9", topics="summary() output, intercept", type="MC",
question=CUCKOO + "\n\nPiping lm(egg_length ~ host_species) into summary() shows a p-value for the (Intercept) of < 2e-16. Why don't we care?",
options="""A) Because it's just a p-value, not an effect size
B) Because it tests the silly null that mean cuckoo egg length is zero
C) Because it tests the silly null that mean Hedge Sparrow-nest egg length is 0
D) We should care: it shows host species matters""",
answer="C",
explanation="Hedge Sparrow comes first alphabetically, so it's the reference level and the intercept is its mean. The intercept's p-value tests whether that mean is zero, which no one doubts for an egg.",
why_wrong="""A) Not the reason.
B) The intercept is the reference group's mean, not the overall mean.
D) It tests a null we already know is false.""",
hint="Which group does the intercept describe?"),

# ---------------- ChimeIn ----------------
dict(id="ch18-chimein-01", source="Chime In (ANOVA), Q1-2", topics="multiple testing", type="matching",
question="Match each question to its answer:\n\n1. Why is it a bad idea to conduct all pairwise t-tests when you have more than two groups?\n2. How does an ANOVA overcome the multiple testing problem?",
options="""A) Because the false positive rate is no longer what we advertise (α)
B) By testing one hypothesis, not many
C) Because it's more work
D) By lowering α for each test""",
answer="1-A, 2-B",
explanation="Many tests each with α = 0.05 give a much higher chance of at least one false positive. ANOVA tests a single null (all means equal).",
why_wrong="C) Effort isn't the issue. D) ANOVA doesn't adjust α; post-hoc corrections do something like that.",
hint="What happens to the chance of a false positive as you run more tests?"),

dict(id="ch18-chimein-02", source="Chime In (ANOVA), Q4", topics="sampling distribution", type="MC",
question="Which of the following is true about sampling distributions?",
options="""A) The sampling distribution shows how values in your data are spread
B) The sampling distribution shows the distribution of samples in your data
C) The sampling distribution shows the distribution of estimates from many samples (or bootstraps)""",
answer="C",
explanation="A sampling distribution is the distribution of an estimate (like a mean) across many hypothetical samples, which we approximate by bootstrapping or theory.",
why_wrong="""A) That's the distribution of the data.
B) Not a meaningful description.""",
hint="It's a distribution of estimates, not of data points."),

dict(id="ch18-chimein-03", source="Chime In (ANOVA), Q5", topics="standard error, standard deviation", type="MC",
question="What is the distinction between the standard error and the standard deviation?",
options="""A) The standard error is always greater than the standard deviation
B) The standard deviation reflects variability in your data, while the standard error reflects uncertainty in an estimate
C) The standard error reflects variability in your data, while the standard deviation reflects uncertainty in an estimate""",
answer="B",
explanation="SD describes spread among individuals; SE (= SD / √n) describes how much an estimate would vary across samples.",
why_wrong="""A) The SE is smaller than the SD for any n > 1.
C) Backwards.""",
hint="Which one shrinks as sample size grows?"),

# ---------------- Book: ANOVA summary (crabs) ----------------
dict(id="ch18-book-01", source="Book: ANOVA summary (Q1a)", topics="multiple testing, pairwise comparisons", type="numeric",
question=CRABS + "\n\nThere are four groups. How many possible pairwise comparisons are there?",
answer="6", explanation="4 × 3 / 2 = 6.",
why_wrong="Common mistake: 4 × 3 = 12, counting each pair twice.",
hint="k(k - 1) / 2."),

dict(id="ch18-book-02", source="Book: ANOVA summary (Q1b)", topics="multiple testing", type="numeric",
question=CRABS + "\n\nIf all four groups came from the same population (the null is true) and we did all 6 pairwise tests at α = 0.05, what is the probability of rejecting at least one true null? (Treat the tests as independent.)",
answer="0.265", explanation="1 - 0.95⁶ = 1 - 0.735 = 0.265.",
why_wrong="Common mistake: 6 × 0.05 = 0.30.",
hint="Find the chance of no false positives first."),

dict(id="ch18-book-03", source="Book: ANOVA summary (Q2)", topics="visualizing groups", type="MC",
question=CRABS + "\n\nLooking at the plot (individual crabs, with means and 95% CIs), which comparison is most likely to be significantly different?",
image="ch18-book-crabs.png",
options="""A) female vs male major removed
B) female vs male minor removed
C) intact male vs male major removed
D) intact male vs male minor removed
E) male major removed vs male minor removed""",
answer="B",
explanation="Females have the highest mean and males with the minor claw removed the lowest; their CIs are far apart.",
why_wrong="The other pairs have closer means and more overlapping CIs.",
hint="Which two means are farthest apart?"),

dict(id="ch18-book-04", source="Book: ANOVA summary (Q3-4)", topics="equal variance assumption", type="MC",
question=CRABS + "\n\n" + CRAB_SUM + "\n\nWhat is the largest fold difference in variance between treatments, and how concerned should we be about the equal variance assumption?",
options="""A) Less than two-fold; probably not a major concern
B) Between two- and five-fold; somewhat worrisome, but we can plow ahead
C) Between five- and ten-fold; a big concern
D) More than ten-fold; we must transform or use Welch's ANOVA""",
answer="A",
explanation="0.0521 / 0.0392 = 1.33-fold, so the variances are very similar.",
why_wrong="B), C) and D) Overstate the difference.",
hint="Divide the largest variance by the smallest."),

dict(id="ch18-book-05", source="Book: ANOVA summary (Q5)", topics="sums of squares, deviations", type="matching",
question=CRABS + "\n\nEach panel shows individual crabs, the group means (colored lines) and the grand mean (black line). Match each kind of deviation to its panel:\n\n1. Total deviations\n2. Model deviations\n3. Error deviations",
image="ch18-book-crab-deviations.png",
options="""A) Panel a
B) Panel b
C) Panel c""",
answer="1-B, 2-C, 3-A",
explanation="a: crabs to their group mean (error). b: crabs to the grand mean (total). c: group means to the grand mean (model).",
why_wrong="Check where each vertical line starts and ends.",
hint="Which panel's lines never touch the points?"),

dict(id="ch18-book-06", source="Book: ANOVA summary (Q6)", topics="sums of squares", type="MC",
question=CRABS + """

crabs |>
  mutate(grand_mean = mean(bodyTemperature)) |>
  group_by(crabType) |>
  mutate(group_mean = mean(bodyTemperature)) |>
  ungroup() |>
  summarise(this_partition = sum((group_mean - grand_mean)^2))

What is the best name for this_partition?""",
options="""A) MS_total
B) MS_model
C) MS_error
D) SS_total
E) SS_model
F) SS_error""",
answer="E",
explanation="It sums squared deviations of group means from the grand mean (one per crab): the model sum of squares. It isn't divided by df, so it's not a mean square.",
why_wrong="A), B) and C) Nothing is divided by df. D) and F) Those use the individual observations.",
hint="What is compared to what, and is anything divided by df?"),

dict(id="ch18-book-07", source="Book: ANOVA summary (Q7a)", topics="QQ plots, R errors", type="MC",
question="""This code was meant to make QQ plots of residuals from an ANOVA but didn't work:

augmented_crab <- lm(bodyTemperature ~ crabType, data = crabs) |> augment()
augmented_crab |>
  ggplot(aes(x = .resid)) +
  geom_qq() +
  geom_qq_line() +
  facet_wrap(~crabType)

Why not?""",
options="""A) We did not load the broom package
B) We never generated augmented_crab
C) You must use the original tibble, not augment() output, to make a plot
D) geom_qq() expects the aesthetic to be called sample, not x""",
answer="D",
explanation="geom_qq() and geom_qq_line() need aes(sample = .resid).",
why_wrong="""A) augment() comes from broom, but that isn't the problem here.
B) It's created in the first line.
C) augment() output works fine with ggplot.""",
hint="Which aesthetic does a QQ plot need?"),

dict(id="ch18-book-08", source="Book: ANOVA summary (Q7b-c)", topics="QQ plots, normality assumption", type="MC",
question="""Four QQ plots were proposed for an ANOVA of crab heat gain by crabType:

Plot 1: raw bodyTemperature, faceted by crabType
Plot 2: raw bodyTemperature, all groups together
Plot 3: fitted values (.fitted), faceted by crabType
Plot 4: residuals (.resid), faceted by crabType

These plots evaluate the assumption of normally distributed residuals. Which two are reasonable ways to do so?""",
options="""A) Plot 1 and Plot 2
B) Plot 1 and Plot 4
C) Plot 2 and Plot 4
D) Plot 3 and Plot 4""",
answer="B",
explanation="Within a group, raw values and residuals differ only by the group mean, so Plot 1 and Plot 4 show the same shape. Plot 2 mixes groups with different means. Plot 3: every fitted value in a group is the same number.",
why_wrong="""A) and C) Plot 2 pools groups with different means, which can look non-normal even when residuals are fine.
D) Fitted values carry no information about residual shape.""",
hint="Residuals are the data minus their group mean."),

dict(id="ch18-book-09", source="Book: ANOVA summary (Q8)", topics="R output, ANOVA workflow", type="matching",
question="""In the context of an ANOVA, which R code gives you each of the following?

1. Estimates of model coefficients only
2. An ANOVA table
3. Results of a post-hoc test
4. Coefficients and standard errors, plus many potentially misleading t- and p-values""",
options="""A) lm(y ~ x) |> anova()  OR  aov(y ~ x) |> summary()
B) aov(y ~ x) |> TukeyHSD()
C) lm(y ~ x) |> summary()
D) lm(y ~ x)""",
answer="1-D, 2-A, 3-B, 4-C",
explanation="lm() alone prints coefficients. anova() (or summary() of aov()) gives the ANOVA table. TukeyHSD() runs a post-hoc test. summary() of an lm gives coefficient t-tests, which mostly test comparisons with the reference group and aren't the tests we want.",
why_wrong="Common mix-up: summary() of an lm vs summary() of an aov. They give different output.",
hint="Which one prints a table with Sum Sq and F?"),

dict(id="ch18-book-10", source="Book: ANOVA summary (Q9)", topics="ANOVA, NHST", type="MC",
question=CRABS + "\n\n" + CRAB_ANOVA + "\n\nWhat do we do to the null hypothesis?",
options="""A) Reject it
B) Fail to reject it
C) Accept it
D) Fail to accept it""",
answer="A",
explanation="F = 14.7 on 3 and 72 df gives p = 1.5 × 10⁻⁷, far below 0.05: rates of heat gain differ among crab groups.",
why_wrong="B) p is tiny. C) and D) We don't accept nulls.",
hint="Compare p with α."),

dict(id="ch18-book-11", source="Book: ANOVA summary (Q10)", topics="post-hoc tests, significance groups", type="MC",
question=CRABS + "\n\n" + CRAB_TUKEY + "\n\nIf female is in significance group 'a', which group(s) is intact male in?",
options="""A) a only
B) b only
C) c only
D) a, b
E) b, c
F) a, b, c""",
answer="E",
explanation="Female differs from all males: a. Male major removed and male minor removed differ (p = 0.023), so they get different letters, b and c. Intact male doesn't differ from either of them (p = 0.21 and 0.78), so it shares both letters: b, c.",
why_wrong="""A) and D) Intact male differs from female.
B) and C) Intact male doesn't differ from either 'major removed' (b) or 'minor removed' (c).""",
hint="Groups that don't differ share a letter. Assign letters to the two claw-removed groups first."),
]
