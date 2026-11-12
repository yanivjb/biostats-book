from ai_helpers import V, r
from scipy.stats import f as F
import importlib.util, os
spec = importlib.util.spec_from_file_location('o18', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rows_ch18.py')); o = importlib.util.module_from_spec(spec); spec.loader.exec_module(o)
CUCKOO, CUCKOO_SUM, CUCKOO_TUKEY, CRABS, CRAB_SUM, CRAB_ANOVA, CRAB_TUKEY, APHID = o.CUCKOO, o.CUCKOO_SUM, o.CUCKOO_TUKEY, o.CRABS, o.CRAB_SUM, o.CRAB_ANOVA, o.CRAB_TUKEY, o.APHID
CUCKOO_ANOVA = """lm(egg_length ~ host_species, data = cuckoo) |> anova()

              Df Sum Sq Mean Sq F value    Pr(>F)
host_species   5 42.940  8.5879  10.388 3.152e-08
Residuals    114 94.248  0.8267"""
ROWS = [
V("ch18-quiz-01", 1, question="A study has 25 samples spread across 5 groups. Complete its ANOVA table:\n\nsource | df | Sum Sq | Mean Sq | F\nModel | [A] | 20 | [C] | [E]\nResiduals | [B] | 40 | [D] |\n\nMatch each missing entry to its value:\n\n1. [A] model df\n2. [B] residual df\n3. [C] model mean square\n4. [D] residual mean square\n5. [E] F",
options="""A) 4
B) 20
C) 5
D) 2
E) 2.5""", answer="1-A, 2-B, 3-C, 4-D, 5-E",
explanation="df model = 5 - 1 = 4. df residual = 25 - 5 = 20. MS model = 20 / 4 = 5. MS residual = 40 / 20 = 2. F = 5 / 2 = 2.5.",
why_wrong="Mean square = SS / df.", hint="Start with the degrees of freedom."),
V("ch18-quiz-01", 2, question=CRABS + "\n\n" + CRAB_ANOVA + "\n\nMatch each quantity to how it was calculated:\n\n1. 3 (crabType df)\n2. 72 (Residuals df)\n3. 0.66546 (crabType Mean Sq)\n4. 14.654 (F value)",
options="""A) Number of groups - 1
B) Number of crabs - number of groups
C) Sum Sq / Df for crabType
D) Mean Sq crabType / Mean Sq Residuals""", answer="1-A, 2-B, 3-C, 4-D",
explanation="df model = 4 - 1 = 3; df residual = 76 - 4 = 72; MS = 1.9964 / 3; F = 0.66546 / 0.04541.", why_wrong="Follow the ANOVA table's logic left to right.", hint="df, then SS / df, then the ratio."),

V("ch18-quiz-02", 1, question="A study of 25 samples in 5 groups gives F = 2.5 (4 and 20 df). In R:\n\npf(2.5, df1 = 4, df2 = 20, lower.tail = FALSE)\n[1] " + r(F.sf(2.5,4,20),3) + "\n\nWhat do you do to the null hypothesis at α = 0.05?",
options="""A) Reject it
B) Fail to reject it
C) Accept it
D) Fail to accept it""", answer="B",
explanation="p = " + r(F.sf(2.5,4,20),3) + " > 0.05, so we fail to reject. (We never 'accept' the null.)",
why_wrong="""A) p > α.
C) and D) We never accept the null.""", hint="Compare p with 0.05."),
V("ch18-quiz-02", 2, question=CRABS + "\n\n" + CRAB_ANOVA + "\n\nWhat do you do to the null hypothesis at α = 0.01?",
options="""A) Reject it
B) Fail to reject it
C) Accept it""", answer="A",
explanation="p = 1.5 × 10⁻⁷ is far below 0.01.",
why_wrong="""B) p < α.
C) We never accept the null.""", hint="Compare p with 0.01."),

V("ch18-quiz-03", 1, question=CRABS + "\n\n" + CRAB_ANOVA + "\n\nWhat proportion of the variance in heat gain does crab type explain in this study (R²)? Report it to three decimals.",
answer=r(1.9964/(1.9964+3.2696),3), explanation="R² = 1.9964 / (1.9964 + 3.2696) = 1.9964 / 5.266 = 0.379.", hint="SS model / SS total."),
V("ch18-quiz-03", 2, question=CUCKOO + "\n\n" + CUCKOO_ANOVA + "\n\nWhat proportion of the variance in cuckoo egg length does host species explain in this study (R²)? Report it to three decimals.",
answer=r(42.940/(42.940+94.248),3), explanation="R² = 42.940 / (42.940 + 94.248) = 42.940 / 137.188 = 0.313.", hint="SS model / SS total."),

V("ch18-quiz-04", 1, question=CRABS + " An ANOVA gives R² = 0.38. TRUE or FALSE: If the researchers had included only females and intact males, R² would necessarily stay 0.38.",
options="""A) TRUE
B) FALSE""", answer="B",
explanation="R² depends on which groups are in the study. Changing the groups changes how much variation they explain.", why_wrong="TRUE: R² is study-specific.", hint="Does R² depend on the design?"),
V("ch18-quiz-04", 2, question="An ANOVA in one greenhouse study gives R² = 0.65 for fertilizer treatment. TRUE or FALSE: fertilizer explains 65% of the variation in plant growth among wild plants.",
options="""A) TRUE
B) FALSE""", answer="B",
explanation="R² describes this study's treatments and conditions, not variation in nature.", why_wrong="TRUE: R² doesn't transfer to nature.", hint="Is the greenhouse nature?"),

V("ch18-quiz-05", 1, question="Which of the following are NOT assumptions of an ANOVA? (Select all that apply.)",
options="""A) Each group has the same number of samples
B) The response variable itself is normally distributed overall
C) Residuals are normally distributed within groups
D) Groups have roughly equal variances""", answer="A, B",
explanation="ANOVA doesn't need equal sample sizes (though they help), and it's the residuals, not the overall response, that should be normal.",
why_wrong="C) and D) are assumptions.", hint="Residuals vs raw data."),
V("ch18-quiz-05", 2, question="A researcher measures 10 leaves from each of 3 trees per treatment, and runs an ANOVA treating all 30 leaves per treatment as independent. Which ANOVA assumption is violated? (Select all that apply.)",
options="""A) Independence of observations
B) Equal variance among groups
C) Normality of residuals
D) Equal sample sizes""", answer="A",
explanation="Leaves from the same tree are not independent; the real replicates are trees.",
why_wrong="""B) and C) Nothing suggests these are violated.
D) Not an ANOVA assumption.""", hint="Are leaves on the same tree independent?"),

V("ch18-quiz-06", 1, question="After an ANOVA comparing five diets rejects the null, a student runs 10 standard t-tests between all pairs at α = 0.05. What's the problem?",
options="""A) The chance of at least one false positive is well above 5%
B) Standard t-tests can't be used with five groups of data
C) The ANOVA already shows that all five diets differ
D) Nothing; this is the standard post-hoc procedure""", answer="A",
explanation="Ten tests at α = 0.05 inflate the family-wise false positive rate. Post-hoc tests like Tukey's control it.",
why_wrong="""B) They can be run; that's the problem.
C) ANOVA shows not all are equal.
D) Use a post-hoc test.""", hint="Multiple testing."),
V("ch18-quiz-06", 2, question="What does a post-hoc test (like Tukey's) do after an ANOVA?",
options="""A) Compares pairs of groups while controlling overall false positives
B) Tests whether the ANOVA's assumptions are met by the data
C) Recalculates the ANOVA's F using only the largest groups
D) Tells us whether all group means differ from one another""", answer="A",
explanation="Post-hoc tests identify which pairs differ, adjusting for the number of comparisons.",
why_wrong="""B) That's diagnostics.
C) Not what it does.
D) It identifies which pairs differ.""", hint="Which groups differ?"),

V("ch18-quiz-08", 1, question="A student wrote this code to calculate an ANOVA by hand:\n\nsummarise(n_group = n_distinct(group), n_total = n(),\n          df_group = n_group - 1,\n          df_error = n_total - 1,\n          ss_group = sum(group_sqrd_dev),\n          ss_error = sum(error_sqrd_dev),\n          ms_group = ss_group / df_group,\n          ms_error = ss_error / df_error,\n          f_val = ms_group / ms_error)\n\nWhich line has a mistake?",
options="""A) df_group = n_group - 1
B) df_error = n_total - 1
C) ms_group = ss_group / df_group
D) f_val = ms_group / ms_error""", answer="B",
explanation="Error df = n_total - n_group (one df lost per group mean), not n_total - 1.",
why_wrong="A), C) and D) are correct.", hint="How many means are estimated?"),
V("ch18-quiz-08", 2, question="A student wrote this code to calculate an ANOVA p-value:\n\np_val = pf(q = f_val, df1 = df_group, df2 = df_error)\n\nWhat's wrong?",
options="""A) It returns the lower tail; it needs lower.tail = FALSE
B) df1 and df2 are swapped; df1 should be df_error
C) pf() should be pt(), since this is a t-test
D) Nothing; this gives the correct p-value""", answer="A",
explanation="By default pf() returns the area below F. The p-value is the area above.",
why_wrong="""B) df1 = model df is right.
C) It's an F test.
D) It gives 1 - p.""", hint="Which tail is the p-value?"),

V("ch18-quiz-09", 1, question=APHID.split("\n\n")[0] + "\n\nTukey HSD:\ncomparison | diff | lwr | upr | p adj\noriginal - infected | -17.3 | -21.7 | -12.9 | < 0.0001\nuninfected - infected | -19.2 | -23.9 | -14.4 | < 0.0001\nuninfected - original | -1.9 | -6.5 | 2.8 | 0.58\n\nIf infected aphids are in significance group 'a', which group letters do original and uninfected aphids get?",
options="""A) Both are 'b'
B) Original is 'b'; uninfected is 'c'
C) Both are 'a'
D) Original is 'a'; uninfected is 'b'""", answer="A",
explanation="Both differ from infected, but not from each other, so they share a letter.",
why_wrong="""B) They don't differ from each other.
C) They differ from infected.
D) Original differs from infected.""", hint="Same letter = not significantly different."),
V("ch18-quiz-09", 2, question=APHID.split("\n\n")[0] + "\n\nTukey HSD:\ncomparison | diff | lwr | upr | p adj\noriginal - infected | -17.3 | -21.7 | -12.9 | < 0.0001\nuninfected - infected | -19.2 | -23.9 | -14.4 | < 0.0001\nuninfected - original | -1.9 | -6.5 | 2.8 | 0.58\n\nWhich comparison's confidence interval includes zero?",
options="""A) uninfected - original
B) original - infected
C) uninfected - infected
D) None of the three""", answer="A",
explanation="(-6.5, 2.8) includes 0, matching its non-significant p of 0.58.",
why_wrong="B) and C) are entirely below 0.", hint="Look at lwr and upr."),

V("ch18-hw-01", 1, question=CUCKOO + " If researchers had studied only four host species, how many possible pairwise comparisons would there be?",
answer="6", explanation="4 × 3 / 2 = 6.", hint="k(k - 1) / 2."),
V("ch18-hw-01", 2, question="A study compares eight populations of lizards. How many possible pairwise comparisons are there?",
answer="28", explanation="8 × 7 / 2 = 28.", hint="k(k - 1) / 2."),

V("ch18-hw-02", 1, question=CUCKOO + " If we conducted 10 pairwise comparisons and every null hypothesis were true, what is the probability of rejecting at least one true null at α = 0.05? (Treat the tests as independent.)",
answer=r(1-0.95**10,3), explanation="1 - 0.95¹⁰ = 1 - 0.599 = 0.401.", hint="1 - P(no false positives)."),
V("ch18-hw-02", 2, question="If we conducted 15 pairwise comparisons at α = 0.01 and every null hypothesis were true, what is the probability of rejecting at least one true null? (Treat the tests as independent.)",
answer=r(1-0.99**15,3), explanation="1 - 0.99¹⁵ = 1 - 0.860 = 0.140.", hint="1 - (1 - α)^tests."),

V("ch18-hw-03", 1, image="ch18-hw-cuckoo-deviations.png", question=CUCKOO + "\n\nEach plot shows cuckoo egg lengths by host (colored points), the group means (colored lines) and the grand mean (black line). Which plot shows the deviations whose sum of squares goes in the DENOMINATOR of F (after dividing by df)?",
options="""A) Plot A
B) Plot B
C) Plot C""", answer="B",
explanation="F = MS model / MS error. MS error comes from error deviations: each egg to its group mean (Plot B).",
why_wrong="""A) Model (numerator).
C) Total.""", hint="Denominator = error."),
V("ch18-hw-03", 2, image="ch18-hw-cuckoo-deviations.png", question=CUCKOO + "\n\nEach plot shows cuckoo egg lengths by host (colored points), the group means (colored lines) and the grand mean (black line). Which plot shows the deviations that would be large if host species had a big effect on egg length?",
options="""A) Plot A
B) Plot B
C) Plot C""", answer="A",
explanation="Model deviations (group means to the grand mean) are large when groups differ a lot.",
why_wrong="""B) Error deviations reflect within-group spread.
C) Total deviations include both.""", hint="Between-group differences."),

V("ch18-hw-04", 1, question=CUCKOO + "\n\n" + CUCKOO_SUM + "\n\nWhich two host species have the most different variances?",
options="""A) Hedge Sparrow and Robin
B) Meadow Pipit and Wren
C) Pied Wagtail and Tree Pipit
D) Hedge Sparrow and Pied Wagtail""", answer="A",
explanation="Largest variance: Hedge Sparrow (1.142); smallest: Robin (0.469).",
why_wrong="Find the largest and smallest variances.", hint="Look at the variance column."),
V("ch18-hw-04", 2, question="Five groups of snails have variances in shell length of 2.1, 2.8, 3.0, 4.2 and 25.0 mm². How worried should we be about the equal variance assumption?",
options="""A) Less than two-fold; not a concern
B) Two- to five-fold; probably fine
C) Five- to ten-fold; somewhat worrisome
D) Over ten-fold; a big concern""", answer="D",
explanation="25.0 / 2.1 = 11.9-fold: transform or use Welch's ANOVA.",
why_wrong="A), B) and C) The ratio is about 12.", hint="Largest / smallest."),

V("ch18-hw-05", 1, question=CUCKOO + "\n\n" + CUCKOO_ANOVA + "\n\nHow many cuckoo eggs were measured?",
options="""A) 120
B) 114
C) 119
D) 6""", answer="A",
explanation="df residual = n - groups, so n = 114 + 6 = 120.",
why_wrong="""B) That's the residual df.
C) That's df total (n - 1).
D) That's the number of hosts.""", hint="Residual df = n - number of groups."),
V("ch18-hw-05", 2, question=CUCKOO + "\n\n" + CUCKOO_ANOVA + "\n\nHow was the F value of 10.388 calculated?",
options="""A) 8.5879 / 0.8267
B) 42.940 / 94.248
C) 42.940 / 5
D) 5 / 114""", answer="A",
explanation="F = MS model / MS residual = 8.5879 / 0.8267.",
why_wrong="""B) Ratio of SS, not MS.
C) That's MS model.
D) Ratio of df.""", hint="Ratio of mean squares."),

V("ch18-hw-06", 1, question=CUCKOO + "\n\n" + CUCKOO_TUKEY + "\n\nWhich host species does NOT differ significantly from Robin?",
options="""A) Hedge Sparrow
B) Wren
C) Both of these differ from Robin
D) Neither of these differs from Robin""", answer="A",
explanation="Robin - Wren is significant (p < 0.001), but Robin - Hedge Sparrow isn't listed, so p > 0.2.",
why_wrong="""B) Robin - Wren is significant.
C) and D) Only one differs.""", hint="Is the pair listed?"),
V("ch18-hw-06", 2, question=CUCKOO + "\n\n" + CUCKOO_TUKEY + "\n\nHow many hosts does Meadow Pipit differ from significantly?",
options="""A) 3
B) 1
C) 5
D) 0""", answer="A",
explanation="Meadow Pipit differs from Hedge Sparrow, Tree Pipit and Wren.",
why_wrong="Count the pairs that include Meadow Pipit.", hint="Count the lines with Meadow Pipit."),

V("ch18-hw-07", 1, question=CUCKOO + " Piping lm(egg_length ~ host_species) into summary() shows a coefficient for host_speciesWren of -1.99 with p < 0.001. What does this test?",
options="""A) Whether Wren eggs differ from Hedge Sparrow eggs
B) Whether Wren eggs differ from all other hosts' eggs
C) Whether the mean Wren egg length is zero
D) Whether host species affects egg length overall""", answer="A",
explanation="Hedge Sparrow is the reference level, so each coefficient is a difference from it.",
why_wrong="""B) Only versus the reference.
C) That's what the intercept tests (for Hedge Sparrow).
D) That's the ANOVA F test.""", hint="Which host is the reference level?"),
V("ch18-hw-07", 2, question=CUCKOO + " Why is the ANOVA F test, rather than the coefficient p-values from summary(), the right first test of whether host species matters?",
options="""A) It tests one null (all hosts equal), avoiding multiple tests
B) It always gives smaller p-values than the coefficient tests
C) The coefficients' p-values can't be calculated for factors
D) summary() ignores the host species variable entirely""", answer="A",
explanation="The coefficient tests compare each host only with the reference, and there are many of them. The F test asks one question about all groups.",
why_wrong="""B) Not always.
C) They are calculated.
D) summary() includes it.""", hint="One test vs many."),

V("ch18-chimein-01", 1, question="Match each scenario to its consequence:\n\n1. Running 20 t-tests on groups that all come from the same population, each at α = 0.05\n2. Running one ANOVA on those same groups at α = 0.05",
options="""A) About a 64% chance of at least one false positive
B) A 5% chance of a false positive
C) A 0% chance of a false positive
D) A 100% chance of a false positive""", answer="1-A, 2-B",
explanation="1 - 0.95²⁰ = 0.64. One ANOVA keeps the false positive rate at α.", why_wrong="Multiple tests multiply chances.", hint="1 - 0.95²⁰."),
V("ch18-chimein-01", 2, question="Match each approach to what it does about multiple testing:\n\n1. ANOVA\n2. Tukey's post-hoc test",
options="""A) Tests a single null hypothesis that all means are equal
B) Compares pairs while controlling the overall false positive rate
C) Runs each pairwise t-test at α = 0.05 with no adjustment
D) Ignores the problem entirely""", answer="1-A, 2-B",
explanation="ANOVA avoids many tests; Tukey adjusts for them.", why_wrong="Neither ignores the problem.", hint="One test vs adjusted tests."),

V("ch18-chimein-02", 1, question="A researcher bootstraps the mean egg length of cuckoos 1,000 times and plots a histogram of the 1,000 bootstrap means. What does this histogram approximate?",
options="""A) The sampling distribution of the mean
B) The distribution of egg lengths in the population
C) The distribution of egg lengths in the sample
D) The null distribution of the egg-length difference""", answer="A",
explanation="Bootstrapping approximates the distribution of an estimate across many samples.",
why_wrong="""B) and C) Those are about individual eggs.
D) Null distributions come from permutation or theory under the null.""", hint="Distribution of estimates."),
V("ch18-chimein-02", 2, question="The spread (standard deviation) of a sampling distribution is called:",
options="""A) The standard error
B) The standard deviation of the data
C) The residual variance
D) The sum of squares""", answer="A",
explanation="The SE is the SD of a sampling distribution.",
why_wrong="""B) That's spread among individuals.
C) and D) Those are ANOVA quantities.""", hint="SD of estimates."),

V("ch18-chimein-03", 1, question="A sample of 100 crabs has an SD of 0.2 for heat gain. What is the standard error of the mean, and what does it describe?",
options="""A) 0.02; uncertainty in the mean
B) 0.02; variability among crabs
C) 0.2; uncertainty in the mean
D) 2.0; variability among crabs""", answer="A",
explanation="SE = 0.2 / √100 = 0.02, describing uncertainty in the estimated mean.",
why_wrong="""B) The SD (0.2) describes variability.
C) That's the SD.
D) Multiplies instead of divides.""", hint="SD / √n."),
V("ch18-chimein-03", 2, question="Which quantity would you report to describe how much individual cuckoo eggs vary in length?",
options="""A) The standard deviation
B) The standard error
C) The 95% confidence interval
D) The p-value""", answer="A",
explanation="The SD describes variability among individuals; SE and CI describe uncertainty in an estimate.",
why_wrong="""B) and C) describe uncertainty in the mean.
D) p is about a hypothesis test.""", hint="Variability vs uncertainty."),

V("ch18-book-01", 1, question=CRABS + "\n\nIf the researchers had added a fifth group (males with both claws removed), how many possible pairwise comparisons would there be?",
answer="10", explanation="5 × 4 / 2 = 10.", hint="k(k - 1) / 2."),
V("ch18-book-01", 2, question="A study compares three diets. How many possible pairwise comparisons are there?",
answer="3", explanation="3 × 2 / 2 = 3.", hint="k(k - 1) / 2."),

V("ch18-book-02", 1, question=CRABS + "\n\nIf all four groups came from the same population and we did all 6 pairwise tests at α = 0.01, what is the probability of rejecting at least one true null? (Treat the tests as independent.)",
answer=r(1-0.99**6,3), explanation="1 - 0.99⁶ = 1 - 0.941 = 0.059.", hint="1 - (1 - α)^tests."),
V("ch18-book-02", 2, question="If three groups all came from the same population and we did all 3 pairwise tests at α = 0.05, what is the probability of rejecting at least one true null? (Treat the tests as independent.)",
answer=r(1-0.95**3,3), explanation="1 - 0.95³ = 1 - 0.857 = 0.143.", hint="1 - (1 - α)^tests."),

V("ch18-book-03", 1, image="ch18-book-crabs.png", question=CRABS + "\n\nLooking at the plot (individual crabs, with means and 95% CIs), which comparison is LEAST likely to be significantly different?",
options="""A) intact male vs male minor removed
B) female vs male minor removed
C) female vs intact male
D) female vs male major removed""", answer="A",
explanation="Intact males and males with the minor claw removed have similar means and overlapping CIs (Tukey p = 0.78).",
why_wrong="B), C) and D) all involve females, whose mean is well above the males'.", hint="Which two means are closest?"),
V("ch18-book-03", 2, image="ch18-book-crabs.png", question=CRABS + "\n\nLooking at the plot (individual crabs, with means and 95% CIs), which group has the highest mean rate of heat gain?",
options="""A) female
B) intact male
C) male major removed
D) male minor removed""", answer="A",
explanation="Females have the highest mean (1.67), consistent with males' claws helping shed heat.",
why_wrong="B), C) and D) are lower.", hint="Find the highest mean."),

V("ch18-book-04", 1, question=CRABS + "\n\n" + CRAB_SUM + "\n\nWhich two groups have the most different variances?",
options="""A) intact male and male minor removed
B) female and intact male
C) female and male major removed
D) male major removed and male minor removed""", answer="A",
explanation="Largest: intact male (0.0521); smallest: male minor removed (0.0392).",
why_wrong="Find the largest and smallest.", hint="Look at the variance column."),
V("ch18-book-04", 2, question=CRABS + "\n\n" + CRAB_SUM + "\n\nHow many crabs were in the study?",
options="""A) 76
B) 72
C) 4
D) 19""", answer="A",
explanation="19 + 19 + 18 + 20 = 76.",
why_wrong="""B) That's the residual df.
C) That's the number of groups.
D) That's one group.""", hint="Add the n column."),

V("ch18-book-05", 1, image="ch18-book-crab-deviations.png", question=CRABS + "\n\nEach panel shows individual crabs, the group means (colored lines) and the grand mean (black line). In which panel do all crabs in the same group have the same length of line?",
options="""A) Panel a
B) Panel b
C) Panel c""", answer="C",
explanation="Panel c shows model deviations: each group mean minus the grand mean, the same for every crab in a group.",
why_wrong="""A) Error deviations vary crab to crab.
B) Total deviations vary crab to crab.""", hint="Which deviation ignores individual values?"),
V("ch18-book-05", 2, image="ch18-book-crab-deviations.png", question=CRABS + "\n\nEach panel shows individual crabs, the group means (colored lines) and the grand mean (black line). Squaring and summing the lines in which two panels gives SS model + SS error = SS total?",
options="""A) Panels c and a add to panel b
B) Panels a and b add to panel c
C) Panels b and c add to panel a""", answer="A",
explanation="c is model, a is error, b is total.",
why_wrong="Identify which panel is total first.", hint="Which panel is total?"),

V("ch18-book-06", 1, question=CRABS + "\n\ncrabs |>\n  group_by(crabType) |>\n  mutate(group_mean = mean(bodyTemperature)) |>\n  ungroup() |>\n  summarise(this_partition = sum((bodyTemperature - group_mean)^2))\n\nWhat is the best name for this_partition?",
options="""A) SS_total
B) SS_model
C) SS_error
D) MS_error""", answer="C",
explanation="Each crab minus its group mean, squared and summed: SS error. Not divided by df.",
why_wrong="""A) Uses the grand mean.
B) Uses group means minus the grand mean.
D) Would divide by df.""", hint="What is subtracted?"),
V("ch18-book-06", 2, question=CRABS + "\n\nThe model sum of squares is 1.9964 with 3 df. What is the model mean square?",
options="""A) 0.66546
B) 1.9964
C) 5.9892
D) 0.04541""", answer="A",
explanation="MS = SS / df = 1.9964 / 3 = 0.665.",
why_wrong="""B) That's SS.
C) Multiplies by df.
D) That's MS residual.""", hint="SS / df."),

V("ch18-book-07", 1, question="This code was meant to make a QQ plot of ANOVA residuals:\n\nlm(bodyTemperature ~ crabType, data = crabs) |>\n  augment() |>\n  ggplot(aes(sample = .fitted)) +\n  geom_qq() +\n  geom_qq_line()\n\nWhat's wrong?",
options="""A) It plots fitted values instead of residuals
B) geom_qq() needs aes(x = ...) instead of sample
C) augment() can't be used with lm() output
D) Nothing; this plots the residuals""", answer="A",
explanation="Use aes(sample = .resid). Fitted values are just the group means.",
why_wrong="""B) sample is correct.
C) augment() works with lm().
D) .fitted isn't the residuals.""", hint="Which column holds the residuals?"),
V("ch18-book-07", 2, question="Which line correctly sets up a QQ plot of residuals from augment() output?",
options="""A) ggplot(aes(sample = .resid))
B) ggplot(aes(x = .resid))
C) ggplot(aes(sample = .fitted))
D) ggplot(aes(y = .resid))""", answer="A",
explanation="geom_qq() needs the sample aesthetic, and the residuals are in .resid.",
why_wrong="""B) and D) Wrong aesthetic.
C) Wrong column.""", hint="geom_qq() expects sample."),

V("ch18-book-08", 1, question="Why is a QQ plot of raw bodyTemperature with all four crab groups pooled a poor check of the ANOVA's normality assumption?",
options="""A) Pooling groups with different means distorts the shape
B) Raw data can never be used to check normality at all
C) QQ plots only work for data with a single group
D) Pooled data always look perfectly normal""", answer="A",
explanation="The assumption is about residuals within groups. Mixing groups with different means can make normal residuals look non-normal.",
why_wrong="""B) Raw values within a group work.
C) You can facet.
D) Pooling can look odd.""", hint="What does the assumption concern?"),
V("ch18-book-08", 2, question="Why is a QQ plot of fitted values (.fitted), faceted by crabType, useless for checking normality?",
options="""A) Every fitted value within a group is the same number
B) Fitted values are always perfectly normally distributed
C) Fitted values exist only for the reference group
D) Faceting by group removes all of the information""", answer="A",
explanation="In a one-way ANOVA the fitted value is the group mean, so each panel is a single repeated value.",
why_wrong="""B) They're constant within a group.
C) Every crab has a fitted value.
D) Faceting is fine for residuals.""", hint="What's the fitted value in an ANOVA?"),

V("ch18-book-09", 1, question="You want to know which pairs of crab groups differ after a significant ANOVA. Which code should you use?",
options="""A) aov(y ~ x) |> TukeyHSD()
B) lm(y ~ x) |> summary()
C) lm(y ~ x) |> anova()
D) lm(y ~ x)""", answer="A",
explanation="TukeyHSD() runs the post-hoc comparisons.",
why_wrong="""B) Compares each group only with the reference.
C) Gives the overall F test.
D) Prints coefficients.""", hint="Post-hoc test."),
V("ch18-book-09", 2, question="Match each code to what it reports:\n\n1. lm(y ~ x) |> anova()\n2. lm(y ~ x)",
options="""A) An ANOVA table with SS, MS, F and p
B) Model coefficients only
C) Pairwise post-hoc comparisons
D) Coefficients with t- and p-values""", answer="1-A, 2-B",
explanation="anova() gives the ANOVA table; lm() alone prints coefficients.", why_wrong="TukeyHSD() and summary() do the others.", hint="What does each function add?"),

V("ch18-book-10", 1, question=CRABS + "\n\n" + CRAB_ANOVA + "\n\nWhat does this result tell us?",
options="""A) Not all crab groups have the same mean heat gain
B) All four crab groups differ in mean heat gain
C) Females gain heat faster than every male group
D) The major claw definitely works as a heat sink""", answer="A",
explanation="Rejecting the ANOVA null means not all means are equal. Which differ needs post-hoc tests; causes need biology.",
why_wrong="""B) and C) Need post-hoc tests.
D) A p-value doesn't prove a mechanism.""", hint="What's the ANOVA's alternative?"),
V("ch18-book-10", 2, question=CRABS + "\n\n" + CRAB_ANOVA + "\n\nIf the null hypothesis were true, about what value would we expect F to be?",
options="""A) About 1
B) About 0
C) About 14.7
D) About 72""", answer="A",
explanation="Under the null, both mean squares estimate the same variance, so F ≈ 1.",
why_wrong="""B) F near 0 is unusual.
C) That's the observed F.
D) That's a df.""", hint="Ratio of two estimates of the same variance."),

V("ch18-book-11", 1, question=CRABS + "\n\n" + CRAB_TUKEY + "\n\nWhich comparisons are NOT significant at α = 0.05?",
options="""A) major removed - intact male and minor removed - intact male
B) intact male - female and minor removed - female
C) major removed - female and minor removed - major removed
D) All six comparisons are significant at α = 0.05""", answer="A",
explanation="p = 0.208 and 0.778; all others are below 0.05.",
why_wrong="B) and C) are significant. D) Two are not.", hint="Find p adj > 0.05."),
V("ch18-book-11", 2, question=CRABS + "\n\n" + CRAB_TUKEY + "\n\nIf female is in significance group 'a', which group(s) is 'male major removed' in?",
options="""A) b only
B) c only
C) a, b
D) b, c""", answer="A",
explanation="Major removed differs from female (a) and from minor removed (c), but not from intact male (b, c), so it's 'b'.",
why_wrong="""B) It differs from minor removed, which is c.
C) It differs from female.
D) It differs from minor removed (c).""", hint="Start from the female/minor-removed letters."),
]
