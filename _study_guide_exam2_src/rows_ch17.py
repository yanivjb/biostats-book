HW_TABLE = """source | df | Sum Sq | Mean Sq | F | p-value
model | 1 | 2.8475 | 2.8475 | [B] | [C]
error | 47 | 1.9789 | [A] | |"""
S22 = """To ask whether pink flowers carry more genes from the sister subspecies xantiana, we compared the admixture proportion (the share of the genome from xantiana) of pink- and white-flowered parviflora plants at Site 22:

lm(admix_proportion ~ petal_color, data = clarkia_s22_hz) |> anova()

            Df    Sum Sq    Mean Sq F value   Pr(>F)
petal_color  1 0.0025843 0.00258430  8.1871 0.008049
Residuals   27 0.0085224 0.00031564"""
SS_CODE = """SS <- data |>
  mutate(grand_mean = mean(response)) |>
  group_by(explanatory) |>
  mutate(yhat = mean(response)) |>
  ungroup() |>
  summarise(SS_A = sum((yhat - grand_mean)^2),
            SS_B = sum((response - yhat)^2),
            SS_C = sum((response - grand_mean)^2))"""
ROWS = [
# ---------------- Homework ----------------
dict(id="ch17-hw-01", source="F homework, Q1", topics="sums of squares", type="matching",
question="""Consider this code:

SS <- data |>
  mutate(mean_y = mean(y)) |>
  group_by(explanatory) |>
  mutate(y_predicted = mean(y)) |>
  ungroup() |>
  mutate(resid = y - y_predicted) |>
  summarise(SS_A = sum(resid^2),
            SS_B = sum((y - mean_y)^2),
            SS_C = sum((y_predicted - mean_y)^2))

Match each label to the sum of squares it calculates:

1. SS_A
2. SS_B
3. SS_C""",
options="""A) Sum of squares error
B) Sum of squares total
C) Sum of squares model""",
answer="1-A, 2-B, 3-C",
explanation="Error: observations minus their group's prediction. Total: observations minus the grand mean. Model: group predictions minus the grand mean.",
why_wrong="Common mix-up: model vs total. Total starts from each observation; model starts from each group's mean.",
hint="For each line, ask: what is being compared to what?"),

dict(id="ch17-hw-02", source="F homework, Q2", topics="sums of squares, deviations", type="matching",
question="Each plot shows the admixture proportion of individual pink and white parviflora plants, the grand mean (black line) and the group means (dashed lines). The vertical lines show deviations. Match each plot to the deviations it shows:\n\n1. plot 1\n2. plot 2\n3. plot 3",
image="ch17-hw-deviations.png",
options="""A) Total deviations
B) Model deviations
C) Error deviations""",
answer="1-A, 2-B, 3-C",
explanation="Plot 1: each point to the grand mean (total). Plot 2: each group mean to the grand mean (model). Plot 3: each point to its group mean (error).",
why_wrong="Look at where each line starts and ends: a point, a group mean (dashed), or the grand mean (black).",
hint="Where does each vertical line start, and where does it end?"),

dict(id="ch17-hw-03", source="F homework, Q3", topics="ANOVA table, mean squares, F", type="matching",
question="Complete this ANOVA table:\n\n" + HW_TABLE + "\n\nMatch each missing entry to its value:\n\n1. [A] (mean square error)\n2. [B] (F)\n3. [C] (p-value)",
options="""A) 0.0421
B) 0.98
C) 67.6
D) 1.4
E) 1.19 × 10⁻¹⁰
F) 0.05""",
answer="1-A, 2-C, 3-E",
explanation="MS error = 1.9789 / 47 = 0.0421. F = MS model / MS error = 2.8475 / 0.0421 = 67.6. An F of 67.6 on 1 and 47 df is extremely unlikely under the null: p = 1.19 × 10⁻¹⁰.",
why_wrong="Common mistakes: dividing SS error by the total df, or computing F as MS error / MS model (0.015).",
hint="Mean square = sum of squares / df; F = MS model / MS error."),

dict(id="ch17-hw-04", source="F homework, Q4", topics="effect size, Cohen's d, pooled variance", type="MC",
question="""An ANOVA comparing two groups gives:

source | df | Sum Sq | Mean Sq
model | 1 | 2.8475 | 2.8475
error | 47 | 1.9789 | 0.0421

The difference in group means is 0.51. With only two groups, the mean square error equals the pooled variance. How big is the effect?

Size | Cohen's d
Tiny | 0.01 to 0.20
Small | 0.20 to 0.50
Medium | 0.50 to 0.80
Large | 0.80 to 1.20
Very large | 1.20 to 2.00
Huge | > 2.00""",
options="""A) Tiny
B) Small
C) Medium
D) Large
E) Very large
F) Huge""",
answer="F",
explanation="Pooled SD = √0.0421 = 0.205. Cohen's d = 0.51 / 0.205 = 2.49, a huge effect (> 2).",
why_wrong="Common mistake: dividing by the variance (0.0421) instead of the SD, or by MS model.",
hint="Turn the mean square error into a standard deviation first."),

dict(id="ch17-hw-05", source="F homework, Q5", topics="R squared", type="numeric",
question="An ANOVA comparing two groups gives SS model = 2.8475 (1 df) and SS error = 1.9789 (47 df). What is R², the proportion of variance in Y attributable to the model? Report it to three decimals.",
answer="0.590", explanation="R² = SS model / SS total = 2.8475 / (2.8475 + 1.9789) = 2.8475 / 4.8264 = 0.590.",
why_wrong="Common mistake: SS model / SS error (1.44).",
hint="SS total = SS model + SS error."),

dict(id="ch17-hw-06", source="F homework, Q6", topics="p-values", type="MC",
question="Our p-value equaled the probability of being struck by lightning and bitten by a shark on the same day. Technically, this means that:",
options="""A) The null would rarely generate data this extreme
B) There is a very small chance that the null is true
C) The null is false""",
answer="A",
explanation="A p-value is the probability of data at least this extreme if the null were true. It isn't the probability the null is true, and it doesn't prove the null false.",
why_wrong="""B) Treats p as the probability of the null.
C) Even a tiny p doesn't prove anything for certain.""",
hint="What does a p-value assume?"),

dict(id="ch17-hw-07", source="F homework, Q8", topics="t-test vs ANOVA", type="MC",
question="With two groups, we can use a two-sample t-test or an ANOVA. When is a two-sample t-test preferred over an ANOVA?",
options="""A) Never: an ANOVA is always the better choice
B) When data are non-independent within groups
C) Either: they agree (F = t²); t also gives direction""",
answer="C",
explanation="With two groups, F = t² and the p-values are identical. The choice is about presentation; the t also gives the direction of the difference.",
why_wrong="""A) Both are fine with two groups.
B) Non-independence is a problem for both.""",
hint="What is t² for two groups?"),

# ---------------- ChimeIn ----------------
dict(id="ch17-chimein-01", source="Chime In (F), Q1-3", topics="standard error, standard deviation, uncertainty vs variability", type="matching",
question="Match each quantity to what it describes:\n\n1. Standard error (SE)\n2. Standard deviation (SD)",
options="""A) Uncertainty: variability in an estimate across repeated samples
B) Variability: how much individuals in the sample differ""",
answer="1-A, 2-B",
explanation="Both measure spread, but of different things. The SD describes spread among individuals; the SE describes spread of an estimate (like a mean) across hypothetical repeated samples.",
why_wrong="Common mix-up: they're both 'variability', but the SE is the variability of an estimate, which is what we mean by uncertainty.",
hint="Which one shrinks as you collect more data?"),

dict(id="ch17-chimein-02", source="Chime In (F), Q4-6", topics="sums of squares, deviations", type="matching",
question="Imagine drawing vertical lines on a plot of data from several groups, then squaring the length of every line and summing them. Which sum of squares would we get for each kind of line?\n\n1. Lines connecting each observation to its group mean\n2. Lines connecting each group mean to the grand mean (one per data point)\n3. Lines connecting each observation to the grand mean",
options="""A) Total
B) Error (aka residual)
C) Model (aka group)""",
answer="1-B, 2-C, 3-A",
explanation="Observation to group mean: error. Group mean to grand mean: model. Observation to grand mean: total. And SS total = SS model + SS error.",
why_wrong="Common mix-up: model vs total.",
hint="Which deviations would be zero if every observation equaled its group mean?"),

dict(id="ch17-chimein-03", source="Chime In (F), Q8", topics="F statistic, null hypothesis", type="MC",
question="What is the expected value of F under the null hypothesis?",
options="""A) 0
B) 1
C) 1.96
D) It depends""",
answer="B",
explanation="Under the null, the mean square for groups and the mean square error both estimate the same variance (sampling error), so their ratio is about 1.",
why_wrong="""A) Even with no true differences, group means vary by chance, so MS model isn't zero.
C) 1.96 is a critical value for z.
D) Its exact distribution depends on the df, but its expectation is about 1.""",
hint="Under the null, what do MS model and MS error both estimate?"),

dict(id="ch17-chimein-04", source="Chime In (F), Q9", topics="ANOVA hypotheses", type="MC",
question="The alternative hypothesis for an ANOVA is:",
options="""A) All means differ
B) Not all means differ
C) Not all means are equal""",
answer="C",
explanation="The null is that all groups have the same mean. The alternative is that at least one differs, i.e. not all means are equal.",
why_wrong="""A) Too strong: just one group differing makes the null false.
B) Says something different: 'not all differ' allows all to be equal.""",
hint="What's the opposite of 'all means are equal'?"),

dict(id="ch17-chimein-05", source="Chime In (F), Q10-11", topics="F distribution, one vs two tails", type="MC",
question="When conducting an ANOVA we look only at the upper tail of the F distribution. Why is that fine, even though we usually do two-tailed tests?",
options="""A) It isn't fine: we should double the ANOVA p-value, as for a two-tailed t-test
B) ANOVA is an exception: with three or more groups, one-tailed tests are allowed
C) Because the upper tail of F already covers differences in both directions
D) Because we already know which group should have the larger mean""",
answer="C",
explanation="F is built from squared deviations, so a group mean far above or far below the others both make F bigger. Any kind of difference among means pushes F into the upper tail.",
why_wrong="""A) Doubling would be wrong: small F values aren't evidence of differences.
B) It's not an exception; it's how F is built.
D) ANOVA doesn't specify a direction.""",
hint="What happens to a squared deviation when a mean is unusually low?"),

dict(id="ch17-chimein-06", source="Chime In (F), Q13", topics="F statistic, mean squares", type="numeric",
question="Pretend we have 2 groups and 23 samples, with SS groups = 7 and SS error = 10. What is F?",
answer="14.7", explanation="df groups = 2 - 1 = 1; df error = 23 - 2 = 21. MS groups = 7 / 1 = 7; MS error = 10 / 21 = 0.476. F = 7 / 0.476 = 14.7.",
why_wrong="Common mistake: F = SS groups / SS error (0.7), skipping the degrees of freedom.",
hint="Turn each sum of squares into a mean square first."),

dict(id="ch17-chimein-07", source="Chime In (F), Q14-16", topics="F statistic, p-values, NHST", type="MC",
question="""Pretend we have 2 groups and 23 samples: F = 14.7 on 1 and 21 degrees of freedom. In R:

pf(14.7, df1 = 1, df2 = 21, lower.tail = FALSE)
[1] 0.00097

What do we conclude at α = 0.05?""",
options="""A) The null is correct
B) The alternative is correct
C) We reject the null
D) We fail to reject the null
E) We accept the null""",
answer="C",
explanation="F = 14.7 is far above its expected value of about 1, and p = 0.001 < 0.05, so we reject the null. (We still haven't proved the alternative.)",
why_wrong="""A) and E) p is tiny, and we never accept the null.
B) Rejecting the null isn't proof of the alternative.
D) p is far below α.""",
hint="Compare p with α."),

# ---------------- Book: F (ANOVA) summary ----------------
dict(id="ch17-book-01", source="Book: F (ANOVA) summary (Q1)", topics="F statistic, null hypothesis", type="MC",
question="Under the null hypothesis that all groups come from the same population, the expected value of F is:",
options="""A) 0
B) 1
C) It depends on the degrees of freedom""",
answer="B", near_duplicate_of="ch17-chimein-03",
explanation="Under the null, MS model and MS error both estimate the same variance, so F ≈ 1.",
why_wrong="""A) Group means vary by chance even under the null.
C) Its distribution depends on df, but it's centered near 1.""",
hint="F is a ratio of two estimates of what, under the null?"),

dict(id="ch17-book-02", source="Book: F (ANOVA) summary (Q2)", topics="F statistic, critical values", type="select-all",
question="If F is greater than its expected value under the null (about 1), then: (Select all that apply.)",
options="""A) The null is false
B) The null is true
C) We reject the null
D) We fail to reject the null
E) We may or may not reject the null, depending on the degrees of freedom""",
answer="E",
explanation="An F a bit above 1 is common by chance. Whether F is big enough to reject depends on its critical value, which depends on the degrees of freedom.",
why_wrong="""A) and B) F alone never proves anything about the null.
C) and D) It depends how much bigger than 1, and on the df.""",
hint="Is F = 1.2 significant? It depends on what?"),

dict(id="ch17-book-03", source="Book: F (ANOVA) summary (Q3)", topics="F statistic, critical values", type="select-all",
question="If F is less than its expected value under the null (about 1), then: (Select all that apply.)",
options="""A) The null is false
B) The null is true
C) We reject the null
D) We fail to reject the null
E) We may or may not reject the null, depending on the degrees of freedom""",
answer="D",
explanation="An F below 1 means groups differ less than we'd expect from chance alone, so it's never in the rejection region (the upper tail). We fail to reject.",
why_wrong="""B) Failing to reject doesn't prove the null true.
E) Critical values are always above 1, so the df don't matter here.""",
hint="Where is the rejection region of an F test?"),

dict(id="ch17-book-04", source="Book: F (ANOVA) summary (Q4)", topics="p-values, interpreting results", type="select-all",
question="We used an ANOVA to test whether pink and white parviflora flowers at Squirrel Mountain have the same admixture proportion (the share of their genome from the sister subspecies xantiana). The p-value was very small (much less than 0.05). This means: (Select all that apply.)",
options="""A) Such an extreme F would be unlikely if the null were true
B) Pollinators avoid visiting white-flowered parviflora plants
C) The pink petal color has introgressed from xantiana""",
answer="A",
explanation="A small p-value tells us the data would be surprising under the null. It doesn't identify a biological cause; B and C are possible explanations that the test can't distinguish.",
why_wrong="""B) and C) These are biological hypotheses; an association alone doesn't show either one.""",
hint="What does a p-value tell you, and what doesn't it?"),

dict(id="ch17-book-05", source="Book: F (ANOVA) summary (Q5-7)", topics="sums of squares", type="matching",
question="Consider this code:\n\n" + SS_CODE + "\n\nMatch each sum of squares to the label that calculates it:\n\n1. SS error\n2. SS model\n3. SS total",
options="""A) SS_A
B) SS_B
C) SS_C""",
answer="1-B, 2-A, 3-C", near_duplicate_of="ch17-hw-01",
explanation="SS_A: group means vs grand mean (model). SS_B: observations vs group means (error). SS_C: observations vs grand mean (total).",
why_wrong="Common mix-up between SS_A and SS_C: one starts from yhat, the other from the response.",
hint="yhat is each observation's group mean."),

dict(id="ch17-book-06", source="Book: F (ANOVA) summary (Q8)", topics="linear models, group means", type="numeric",
question="""At Site 22, the mean admixture proportion of pink-flowered parviflora plants is 0.0330 and of white-flowered plants is 0.0132. What is the difference (pink minus white)?""",
answer="0.0199", explanation="0.0330 - 0.0132 = 0.0199 (0.0198 with these rounded means).",
why_wrong="Common mistake: white minus pink (negative).",
hint="Pink minus white.",
),

dict(id="ch17-book-07", source="Book: F (ANOVA) summary (Q9-11)", topics="sums of squares, deviations", type="matching",
question="The plots show admixture proportions of individual pink and white parviflora plants at Site 22, the grand mean (black line) and the group means (dashed lines). Match each kind of deviation to the plot that shows it:\n\n1. Error deviations\n2. Model deviations\n3. Total deviations",
image="ch17-book-deviations.png",
options="""A) Plot A
B) Plot B
C) Plot C""",
answer="1-A, 2-C, 3-B", near_duplicate_of="ch17-hw-02",
explanation="A: points to their group mean (error). B: points to the grand mean (total). C: group means to the grand mean (model).",
why_wrong="Check where each line starts and ends.",
hint="Which plot's lines never touch the points?"),

dict(id="ch17-book-08", source="Book: F (ANOVA) summary (Q12-13)", topics="NHST, interpreting results", type="MC",
question=S22 + "\n\nWhat do we do with the null hypothesis, and what does that mean?",
options="""A) Reject it; the null is false
B) Reject it; we can't say for sure whether the null is true
C) Fail to reject it; the null is true
D) Reject it; the null has a 0.008 chance of being true""",
answer="B",
explanation="p = 0.008 < 0.05, so we reject. But rejecting doesn't prove the null false, and p isn't the probability the null is true.",
why_wrong="""A) Rejecting isn't proof.
C) p is below α.
D) p is not the probability the null is true.""",
hint="Compare p with α, then think about what p does and doesn't mean."),

dict(id="ch17-book-09", source="Book: F (ANOVA) summary (Q14)", topics="R squared", type="numeric",
question=S22 + "\n\nWhat is R² for this model?",
answer="0.233", explanation="R² = SS model / SS total = 0.0025843 / (0.0025843 + 0.0085224) = 0.0025843 / 0.0111067 = 0.233. Petal color explains about 23% of the variation in admixture proportion at this site.",
why_wrong="Common mistake: SS model / SS error (0.30).",
hint="SS total = SS model + SS error."),

dict(id="ch17-book-10", source="Book: F (ANOVA) summary (Q15)", topics="effect size, Cohen's d", type="MC",
question=S22 + "\n\nThe difference in mean admixture proportion (pink minus white) is 0.0199. How big is the effect (Cohen's d)?",
options="""A) Not worth reporting (< 0.01)
B) Tiny (0.01 to 0.20)
C) Small (0.20 to 0.50)
D) Medium (0.50 to 0.80)
E) Large (0.80 to 1.20)
F) Very large (1.20 to 2.00)
G) Huge (> 2.00)""",
answer="E",
explanation="With two groups, MS error is the pooled variance: pooled SD = √0.00031564 = 0.0178. d = 0.0199 / 0.0178 = 1.12, a large effect.",
why_wrong="Common mistake: dividing by the mean square itself (gives about 63) or by the SE.",
hint="Which entry in the table is the pooled variance? Take its square root."),
]
