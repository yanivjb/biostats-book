from ai_helpers import V, r
from scipy.stats import f as F
S22 = """To ask whether pink flowers carry more genes from the sister subspecies xantiana, we compared the admixture proportion (the share of the genome from xantiana) of pink- and white-flowered parviflora plants at Site 22:

lm(admix_proportion ~ petal_color, data = clarkia_s22_hz) |> anova()

            Df    Sum Sq    Mean Sq F value   Pr(>F)
petal_color  1 0.0025843 0.00258430  8.1871 0.008049
Residuals   27 0.0085224 0.00031564"""
DEV_HW = "Each plot shows the admixture proportion of individual pink and white parviflora plants, the grand mean (black line) and the group means (dashed lines). The vertical lines show deviations."
DEV_BK = "The plots show admixture proportions of individual pink and white parviflora plants at Site 22, the grand mean (black line) and the group means (dashed lines)."
pval = lambda f, d1, d2: F.sf(f, d1, d2)
ROWS = [
V("ch17-hw-01", 1, question="Consider this code:\n\nSS <- data |>\n  mutate(grand = mean(y)) |>\n  group_by(group) |>\n  mutate(fit = mean(y)) |>\n  ungroup() |>\n  summarise(SS_1 = sum((y - grand)^2),\n            SS_2 = sum((fit - grand)^2),\n            SS_3 = sum((y - fit)^2))\n\nMatch each label to the sum of squares it calculates:\n\n1. SS_1\n2. SS_2\n3. SS_3",
options="""A) Sum of squares error
B) Sum of squares total
C) Sum of squares model""", answer="1-B, 2-C, 3-A",
explanation="Total: observation - grand mean. Model: group mean (fit) - grand mean. Error: observation - group mean.", why_wrong="Look at what is subtracted from what.", hint="Which pair of values does each line compare?"),
V("ch17-hw-01", 2, question="In an ANOVA, which deviations are squared and summed to get each sum of squares?\n\n1. SS error\n2. SS model\n3. SS total",
options="""A) Each observation minus the grand mean
B) Each group's mean minus the grand mean, once per observation
C) Each observation minus its own group's mean""", answer="1-C, 2-B, 3-A",
explanation="Error: within groups. Model: between group means and the grand mean. Total: everything around the grand mean.", why_wrong="SS total = SS model + SS error.", hint="Error is within groups."),

V("ch17-hw-02", 1, image="ch17-hw-deviations.png", question=DEV_HW + " Which plot's squared and summed lines give the sum of squares that the model leaves unexplained?",
options="""A) plot 1
B) plot 2
C) plot 3""", answer="C",
explanation="The unexplained part is SS error: each point to its group mean (plot 3).", why_wrong="""A) Total deviations.
B) Model deviations.""", hint="What's left after fitting group means?"),
V("ch17-hw-02", 2, image="ch17-hw-deviations.png", question=DEV_HW + " In plot 2, all points in the same group have the same length of line. Why?",
options="""A) Each line goes from the group mean to the grand mean
B) Each line goes from a point to its group mean
C) Each line goes from a point to the grand mean""", answer="A",
explanation="Model deviations depend only on the group, so every member of a group has the same one.", why_wrong="""B) Those vary point to point (error).
C) Those vary point to point (total).""", hint="Which deviation ignores the individual values?"),

V("ch17-hw-03", 1, question="Complete this ANOVA table:\n\nsource | df | Sum Sq | Mean Sq | F | p-value\nmodel | 2 | 12.0 | [A] | [C] | [D]\nerror | 27 | 54.0 | [B] | |\n\nMatch each missing entry to its value:\n\n1. [A] (mean square model)\n2. [B] (mean square error)\n3. [C] (F)\n4. [D] (p-value)",
options="""A) 6.0
B) 2.0
C) 3.0
D) """ + r(pval(3,2,27),3) + """
E) 0.22
F) 0.5""", answer="1-A, 2-B, 3-C, 4-D",
explanation="MS model = 12 / 2 = 6. MS error = 54 / 27 = 2. F = 6 / 2 = 3. With 2 and 27 df, p = " + r(pval(3,2,27),3) + ".",
why_wrong="Mean square = SS / df; F = MS model / MS error.", hint="Divide each SS by its df first."),
V("ch17-hw-03", 2, question="Complete this ANOVA table:\n\nsource | df | Sum Sq | Mean Sq | F\nmodel | 1 | [A] | 3.0 | 6.0\nerror | 20 | [B] | [C] |\n\nMatch each missing entry to its value:\n\n1. [A] (SS model)\n2. [B] (SS error)\n3. [C] (MS error)",
options="""A) 3.0
B) 10.0
C) 0.5
D) 60.0""", answer="1-A, 2-B, 3-C",
explanation="SS model = 3.0 × 1 = 3.0. MS error = MS model / F = 3.0 / 6.0 = 0.5. SS error = 0.5 × 20 = 10.0.",
why_wrong="Work backwards: F = MS model / MS error and MS = SS / df.", hint="Start from F to get MS error."),

V("ch17-hw-04", 1, question="An ANOVA comparing two groups of tadpoles gives a mean square error of 0.25. The difference in group means is 0.3 g. With only two groups, the mean square error equals the pooled variance. How big is the effect?\n\nSize | Cohen's d\nTiny | 0.01 to 0.20\nSmall | 0.20 to 0.50\nMedium | 0.50 to 0.80\nLarge | 0.80 to 1.20\nVery large | 1.20 to 2.00\nHuge | > 2.00",
options="""A) Tiny
B) Small
C) Medium
D) Large
E) Huge""", answer="C",
explanation="Pooled SD = √0.25 = 0.5. d = 0.3 / 0.5 = 0.6, medium.",
why_wrong="""A), B) Too small. D), E) Too large. (Dividing by the variance, 0.25, would wrongly give 1.2.)""", hint="Take the square root of MS error first."),
V("ch17-hw-04", 2, question="An ANOVA comparing two groups gives:\n\nsource | df | Sum Sq | Mean Sq\nmodel | 1 | 2.8475 | 2.8475\nerror | 47 | 1.9789 | 0.0421\n\nWith only two groups, the mean square error equals the pooled variance. What is the pooled standard deviation?",
options="""A) 0.205
B) 0.0421
C) 1.41
D) 0.0018""", answer="A",
explanation="Pooled SD = √0.0421 = 0.205.",
why_wrong="""B) That's the variance.
C) That's √1.9789.
D) That's 0.0421².""", hint="Square root of MS error."),

V("ch17-hw-05", 1, question="An ANOVA gives SS model = 12.0 and SS error = 54.0. What is R²? Report it to three decimals.",
answer=r(12/66,3), explanation="R² = 12 / (12 + 54) = 12 / 66 = 0.182.", hint="SS model / SS total."),
V("ch17-hw-05", 2, question="An ANOVA gives SS total = 4.8264 and R² = 0.590. What is SS error? Report it to two decimals.",
answer=r(4.8264*(1-0.59),2), explanation="SS error = SS total × (1 - R²) = 4.8264 × 0.41 = 1.98.", hint="R² is the share explained; the rest is error."),

V("ch17-hw-06", 1, question="An ANOVA gives p = 0.0000001. Technically, this means that:",
options="""A) Data this extreme would be very rare if the null were true
B) There is a 0.00001% chance that the null hypothesis is true
C) The group means are definitely different from one another
D) The differences among the group means must be very large""", answer="A",
explanation="p is the probability of data at least this extreme under the null.",
why_wrong="""B) p isn't P(null).
C) Rejection isn't proof.
D) A tiny p can come from a small effect in a large sample.""", hint="p assumes the null."),
V("ch17-hw-06", 2, question="An ANOVA gives p = 0.62. Technically, this means that:",
options="""A) The null would often generate data at least this extreme
B) There is a 62% chance that the null hypothesis is true
C) The group means are definitely equal to one another
D) There is a 38% chance that the alternative is true""", answer="A",
explanation="62% of datasets generated under the null would be at least this extreme, so ours isn't surprising.",
why_wrong="""B) and D) p isn't a probability about hypotheses.
C) Failing to reject isn't proof.""", hint="p assumes the null."),

V("ch17-hw-07", 1, question="A two-sample t-test comparing two groups gives t = 3. What F would an ANOVA on the same data give?",
options="""A) F = 9
B) F = 3
C) F = 1.73
D) F = 6""", answer="A",
explanation="With two groups, F = t² = 9, and the p-values are identical.",
why_wrong="""B) F isn't equal to t.
C) That's √3.
D) That's 2t.""", hint="F = t² for two groups."),
V("ch17-hw-07", 2, question="With two groups, a two-sample t-test and an ANOVA give the same p-value. What does the t-test report that the F does not?",
options="""A) The direction of the difference, through t's sign
B) Whether the difference is statistically significant
C) A separate p-value for each group being compared
D) The amount of variance explained by the model""", answer="A",
explanation="F = t² is always positive, so it loses the sign; t tells you which group is larger.",
why_wrong="""B) Both give the same p.
C) Neither does.
D) That's R², from the ANOVA table.""", hint="What does squaring remove?"),

V("ch17-chimein-01", 1, question="Match each scenario to the quantity it describes:\n\n1. How much the mean height of 20 seedlings would vary if we repeated the experiment\n2. How much the heights of the 20 seedlings vary from one another",
options="""A) Standard error
B) Standard deviation""", answer="1-A, 2-B",
explanation="Variation of an estimate across samples is the SE; variation among individuals is the SD.", why_wrong="Estimates vs individuals.", hint="Is it about the mean or the plants?"),
V("ch17-chimein-01", 2, question="Match each quantity to how it changes as sample size increases:\n\n1. Standard error\n2. Standard deviation",
options="""A) Shrinks, since estimates get more precise
B) Stays about the same, since individuals vary just as much""", answer="1-A, 2-B",
explanation="SE = SD / √n shrinks with n. The SD estimates population variability, which doesn't depend on n.", why_wrong="Uncertainty shrinks; variability doesn't.", hint="Which one has √n in it?"),

V("ch17-chimein-02", 1, question="In an ANOVA, which sum of squares measures:\n\n1. Variation among individuals within the same group\n2. Variation among the group means\n3. All the variation in the response",
options="""A) Total
B) Error (aka residual)
C) Model (aka group)""", answer="1-B, 2-C, 3-A",
explanation="Within-group variation is error; between-group variation is model; all of it is total.", why_wrong="SS total = SS model + SS error.", hint="Within vs between."),
V("ch17-chimein-02", 2, question="An ANOVA has SS model = 30 and SS error = 70. Match each quantity to its value:\n\n1. SS total\n2. R²\n3. The share of variation left unexplained",
options="""A) 100
B) 0.3
C) 0.7""", answer="1-A, 2-B, 3-C",
explanation="SS total = 30 + 70 = 100. R² = 30 / 100 = 0.3. Unexplained = 70 / 100 = 0.7.", why_wrong="SS total = SS model + SS error.", hint="Add first, then divide."),

V("ch17-chimein-03", 1, question="An ANOVA gives F = 0.95. What does this suggest?",
options="""A) The groups differ about as much as chance predicts
B) The groups differ much more than chance predicts
C) The group means are all exactly equal
D) The ANOVA must have been calculated incorrectly""", answer="A",
explanation="Under the null F ≈ 1, so 0.95 is just what we'd expect from sampling error alone.",
why_wrong="""B) That would give a large F.
C) Sample means are never exactly equal.
D) F near 1 is common.""", hint="What is F's expected value under the null?"),
V("ch17-chimein-03", 2, question="Under the null hypothesis, why is F expected to be about 1?",
options="""A) MS model and MS error both estimate the same variance
B) The group means are always exactly equal under the null
C) The sum of squares model is always zero under the null
D) F is defined so that it can never be greater than 1""", answer="A",
explanation="If all groups share one mean, between-group variation reflects only sampling error, just like within-group variation, so their ratio is about 1.",
why_wrong="""B) and C) Sample means differ by chance, so SS model isn't zero.
D) F can be large.""", hint="What does each mean square estimate under the null?"),

V("ch17-chimein-04", 1, question="The null hypothesis for an ANOVA comparing four diets is:",
options="""A) All four diets have the same population mean
B) At least one diet has a different population mean
C) All four diets have different population means
D) The sample means of the four diets are equal""", answer="A",
explanation="H₀: μ₁ = μ₂ = μ₃ = μ₄.",
why_wrong="""B) That's the alternative.
C) Too strong for either.
D) Hypotheses are about populations.""", hint="No difference at all."),
V("ch17-chimein-04", 2, question="An ANOVA comparing three fertilizers rejects the null. What can we conclude?",
options="""A) At least one fertilizer's mean differs from another's
B) All three fertilizers have different means
C) The first fertilizer differs from the other two
D) The fertilizer with the highest mean is best""", answer="A",
explanation="Rejecting H₀ means not all means are equal. Which ones differ needs post-hoc comparisons.",
why_wrong="""B) and C) The ANOVA doesn't say which differ.
D) That's not what the test tells us.""", hint="What's the alternative hypothesis?"),

V("ch17-chimein-05", 1, question="An ANOVA compares three groups. One group's mean is much LOWER than the other two. What happens to F?",
options="""A) F gets larger, just as if the mean were much higher
B) F gets smaller, possibly falling below 1
C) F becomes negative, in the lower tail
D) F doesn't change, since F ignores direction""", answer="A",
explanation="F is built from squared deviations, so a mean far below the others increases SS model just as one far above does.",
why_wrong="""B) and C) Squaring removes direction; F can't be negative.
D) F ignores direction but still grows.""", hint="What does squaring do to a negative deviation?"),
V("ch17-chimein-05", 2, question="Why don't we double the p-value from an ANOVA's F test, the way we'd account for two tails in a t-test?",
options="""A) Large F covers differences in any direction
B) ANOVAs always use a smaller α of 0.025
C) F tests are always one-sided by assumption
D) We should double it, but software forgets""", answer="A",
explanation="Because F uses squared deviations, any difference among means pushes F into the upper tail. Small F isn't evidence against the null.",
why_wrong="""B) α is unchanged.
C) It's not an assumption; it's how F is built.
D) Doubling would be wrong.""", hint="What does a small F mean?"),

V("ch17-chimein-06", 1, question="Pretend we have 3 groups and 33 samples, with SS groups = 8 and SS error = 60. What is F?",
answer=r((8/2)/(60/30),2), explanation="df groups = 3 - 1 = 2; df error = 33 - 3 = 30. MS groups = 8 / 2 = 4; MS error = 60 / 30 = 2. F = 4 / 2 = 2.", hint="Find the df, then the mean squares."),
V("ch17-chimein-06", 2, question="Pretend we have 4 groups and 24 samples, with SS groups = 15 and SS error = 40. What is F?",
answer=r((15/3)/(40/20),2), explanation="df groups = 4 - 1 = 3; df error = 24 - 4 = 20. MS groups = 15 / 3 = 5; MS error = 40 / 20 = 2. F = 5 / 2 = 2.5.", hint="Find the df, then the mean squares."),

V("ch17-chimein-07", 1, question="Pretend we have 3 groups and 33 samples: F = 2.0 on 2 and 30 degrees of freedom. In R:\n\npf(2.0, df1 = 2, df2 = 30, lower.tail = FALSE)\n[1] " + r(pval(2,2,30),3) + "\n\nWhat do we conclude at α = 0.05?",
options="""A) The null is correct
B) The alternative is correct
C) We reject the null
D) We fail to reject the null
E) We accept the null""", answer="D",
explanation="p = " + r(pval(2,2,30),3) + " > 0.05, so we fail to reject. That doesn't mean the null is correct.",
why_wrong="""A) and E) We never accept or prove the null.
B) and C) p > α.""", hint="Compare p with 0.05."),
V("ch17-chimein-07", 2, question="Which R code gives the p-value for F = 14.7 on 1 and 21 degrees of freedom?",
options="""A) pf(14.7, df1 = 1, df2 = 21, lower.tail = FALSE)
B) pf(14.7, df1 = 1, df2 = 21)
C) 2 * pf(14.7, df1 = 1, df2 = 21, lower.tail = FALSE)
D) qf(14.7, df1 = 1, df2 = 21)""", answer="A",
explanation="The F test uses the upper tail only: the area above the observed F.",
why_wrong="""B) That's the lower tail.
C) F tests aren't doubled.
D) qf() takes a probability.""", hint="Upper tail, not doubled."),

V("ch17-book-01", 1, question="Five groups of plants are all drawn from the same population. An ANOVA is run many times on new samples. Around what value should the F statistics cluster?",
options="""A) 1
B) 0
C) 5
D) 1.96""", answer="A",
explanation="Under the null, F ≈ 1, since both mean squares estimate the same variance.",
why_wrong="""B) F is about 1, not 0.
C) Not the number of groups.
D) That's a z critical value.""", hint="Ratio of two estimates of the same variance."),
V("ch17-book-01", 2, question="If the null hypothesis of an ANOVA is FALSE, F tends to be:",
options="""A) Larger than 1
B) Smaller than 1
C) Exactly 1
D) Negative""", answer="A",
explanation="Real differences add to MS model but not MS error, so F grows.",
why_wrong="""B) and C) Those are typical under the null.
D) F can't be negative.""", hint="What do real differences add to?"),

V("ch17-book-02", 1, question="An ANOVA gives F = 3.5 on 2 and 6 df (critical F = 5.14), and another gives F = 3.5 on 2 and 60 df (critical F = 3.15). Which reject the null at α = 0.05? (Select all that apply.)",
options="""A) The test with 2 and 6 df
B) The test with 2 and 60 df
C) Neither test rejects the null
D) Both tests reject the null""", answer="B",
explanation="3.5 < 5.14 (fail to reject) but 3.5 > 3.15 (reject). The same F can lead to different decisions depending on df.",
why_wrong="""A) 3.5 is below 5.14.
C) and D) Only one rejects.""", hint="Compare F with each critical value."),
V("ch17-book-02", 2, question="An ANOVA gives F = 1.3. Which of these could be true? (Select all that apply.)",
options="""A) The null hypothesis is true
B) The null hypothesis is false
C) We reject the null at α = 0.05 for most df
D) We fail to reject the null at α = 0.05 for most df""", answer="A, B, D",
explanation="F = 1.3 is usually not significant, but the null might be true or false (we may lack power).",
why_wrong="C) Critical F values are almost always above 1.3 (except with huge df for many groups).", hint="F near 1 is common under the null."),

V("ch17-book-03", 1, question="An ANOVA gives F = 0.4 with 3 and 40 df. Which of these is correct? (Select all that apply.)",
options="""A) The group means vary less than expected by chance
B) We reject the null hypothesis
C) We fail to reject the null hypothesis
D) The null hypothesis must be true""", answer="A, C",
explanation="F < 1 means the group means are closer together than sampling error alone usually produces. We fail to reject, but that doesn't prove the null.",
why_wrong="""B) Small F is never in the rejection region.
D) Failing to reject isn't proof.""", hint="Where is the rejection region?"),
V("ch17-book-03", 2, question="Can an F statistic below 1 ever lead to rejecting the null at α = 0.05? (Select all that apply.)",
options="""A) No: we only reject for large F (upper tail)
B) Yes: with enough degrees of freedom
C) Yes: if the groups are very unequal in size
D) No: F below 1 means less variation among means than expected""", answer="A, D",
explanation="Critical F values are always above 1, and small F values reflect less between-group variation than expected by chance.",
why_wrong="""B) and C) Critical F stays above 1.""", hint="Where is the rejection region?"),

V("ch17-book-04", 1, question="We used an ANOVA to test whether pink and white parviflora flowers at Squirrel Mountain have the same admixture proportion (the share of their genome from the sister subspecies xantiana). The p-value was 0.40. This means: (Select all that apply.)",
options="""A) Data like ours would be common if the null hypothesis were true
B) Petal color has no relationship with admixture
C) There's a 40% chance pink and white flowers have equal admixture""", answer="A",
explanation="p = 0.40 means data this extreme are common under the null. It doesn't prove there's no relationship, and it isn't the probability the null is true.",
why_wrong="""B) Failing to reject isn't proof of no effect.
C) p isn't P(null).""", hint="p assumes the null."),
V("ch17-book-04", 2, question="An ANOVA finds that pink parviflora plants have significantly higher admixture (more genome from xantiana) than white ones (p < 0.001). Which explanations does this result make unlikely? (Select all that apply.)",
options="""A) The difference is due to sampling error alone
B) Pink color itself was introgressed from xantiana
C) Pollinators carry xantiana pollen to pink flowers""", answer="A",
explanation="A small p makes chance an unlikely explanation (though not impossible). It can't tell apart the biological explanations B and C.",
why_wrong="B) and C) are both consistent with the result; the test doesn't distinguish them.", hint="What does a p-value address?"),

V("ch17-book-05", 1, question="Consider this code:\n\ndata |>\n  mutate(gm = mean(y)) |>\n  group_by(trt) |>\n  mutate(trt_mean = mean(y)) |>\n  ungroup() |>\n  summarise(X = sum((y - gm)^2),\n            Y = sum((y - trt_mean)^2),\n            Z = sum((trt_mean - gm)^2))\n\nWhich equation must be true?",
options="""A) X = Y + Z
B) Y = X + Z
C) Z = X + Y
D) X = Y × Z""", answer="A",
explanation="X is SS total, Y is SS error and Z is SS model, and SS total = SS error + SS model.",
why_wrong="Identify which is total first.", hint="Which one is SS total?"),
V("ch17-book-05", 2, question="In R, the code\n\nsummarise(SS = sum((y - mean(y))^2))\n\nrun on ungrouped data calculates which sum of squares?",
options="""A) SS total
B) SS model
C) SS error
D) None of these""", answer="A",
explanation="Each observation minus the grand mean, squared and summed: SS total.",
why_wrong="""B) Model uses group means.
C) Error uses group means.""", hint="No grouping, so mean(y) is the grand mean."),

V("ch17-book-06", 1, question="At Site 22, the mean admixture proportion of pink-flowered parviflora plants is 0.0330. A pink-flowered plant has an admixture proportion of 0.0410. What is this plant's error (residual) deviation?",
answer=r(0.0410-0.0330,4), explanation="Observation minus its group mean: 0.0410 - 0.0330 = 0.0080.", hint="Observation minus group mean."),
V("ch17-book-06", 2, question="At Site 22, a white-flowered parviflora plant has an admixture proportion of 0.0250, and the white group mean is 0.0132. What is this plant's error (residual) deviation?",
answer=r(0.0250-0.0132,4), explanation="Observation minus its group mean: 0.0250 - 0.0132 = 0.0118.", hint="Observation minus group mean."),

V("ch17-book-07", 1, image="ch17-book-deviations.png", question=DEV_BK + " Which plot's deviations, squared and summed, give the sum of squares used in the numerator of F (before dividing by df)?",
options="""A) Plot A
B) Plot B
C) Plot C""", answer="C",
explanation="F's numerator is MS model, from SS model: group means to the grand mean (Plot C).",
why_wrong="""A) Error (denominator).
B) Total.""", hint="F = MS model / MS error."),
V("ch17-book-07", 2, image="ch17-book-deviations.png", question=DEV_BK + " If petal color explained nothing (both group means equal the grand mean), which plot's lines would all have length zero?",
options="""A) Plot A
B) Plot B
C) Plot C""", answer="C",
explanation="Model deviations are group mean minus grand mean, so they vanish when the group means equal the grand mean.",
why_wrong="""A) Points still vary around their group means.
B) Points still vary around the grand mean.""", hint="Which lines connect group means to the grand mean?"),

V("ch17-book-08", 1, question=S22 + "\n\nWhat would we conclude at α = 0.01?",
options="""A) Reject the null, because p < 0.01
B) Fail to reject, because p > 0.01
C) Reject, and the null is proven false
D) It depends on R², not on the p-value""", answer="A",
explanation="p = 0.008 < 0.01, so we reject even at this stricter level (without proving anything).",
why_wrong="""B) 0.008 < 0.01.
C) Rejection isn't proof.
D) The decision uses p and α.""", hint="Compare 0.008 with 0.01."),
V("ch17-book-08", 2, question=S22 + "\n\nWhat is the mean square error (the pooled variance)?",
options="""A) 0.00031564
B) 0.0085224
C) 8.1871
D) 0.0025843""", answer="A",
explanation="MS error = 0.0085224 / 27 = 0.00031564.",
why_wrong="""B) That's SS error.
C) That's F.
D) That's SS model (and MS model).""", hint="SS error / df error."),

V("ch17-book-09", 1, question=S22 + "\n\nWhat proportion of the variation in admixture proportion is NOT explained by petal color?",
answer=r(0.0085224/(0.0025843+0.0085224),3), explanation="SS error / SS total = 0.0085224 / 0.0111067 = 0.767 (1 - R²).", hint="SS error / SS total."),
V("ch17-book-09", 2, question=S22 + "\n\nHow many plants were in this study?",
answer="29", explanation="df total = 1 + 27 = 28 = n - 1, so n = 29.", hint="Total df = n - 1."),

V("ch17-book-10", 1, question=S22 + "\n\nThe pooled SD is 0.0178. If the difference in means had been 0.0089 instead of 0.0199, how big would the effect be?",
options="""A) Small (0.20 to 0.50)
B) Medium (0.50 to 0.80)
C) Large (0.80 to 1.20)
D) Huge (> 2.00)""", answer="B",
explanation="d = 0.0089 / 0.0178 = 0.5, medium (at the boundary).",
why_wrong="""A) 0.5 is at the medium boundary.
C) and D) Too large.""", hint="Difference ÷ pooled SD."),
V("ch17-book-10", 2, question=S22 + "\n\nTo get Cohen's d, we divide the difference in means (0.0199) by:",
options="""A) √0.00031564, the pooled SD
B) 0.00031564, the mean square error
C) √8.1871, the square root of F
D) 0.0085224, the sum of squares error""", answer="A",
explanation="d = 0.0199 / 0.0178 = 1.12. The pooled SD is the square root of MS error.",
why_wrong="""B) That's a variance.
C) √F = |t|, not an SD.
D) Not divided by df.""", hint="Effect size uses an SD."),
]
