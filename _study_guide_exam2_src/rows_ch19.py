LIZ = "Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N)."
LIZ_OUT = """lm(territory ~ bite, data = lizards)

term | estimate | std.error | conf.low | conf.high
(Intercept) | -31.54 | 23.51 | -84.73 | 21.65
bite | 11.68 | 4.85 | 0.71 | 22.64

R² = 0.392; F = 5.80 on 1 and 9 df; p = 0.039"""
GCV = "To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set."
SRP = "To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR)."
MEAS = [("A) Bring the estimated slope closer to zero than it really is", "B) Bring the estimated correlation closer to zero than it really is", "C) Add unbiased noise to the estimated slope, increasing its standard error", "D) Have no effect at all")]

ROWS = [
# ---------------- Quiz: regression (lizard bite force) ----------------
dict(id="ch19-quiz-01", source="Regression quiz (2026), Q1-2", topics="regression, linear model equation", type="MC",
question=LIZ + "\n\n" + LIZ_OUT + "\n\nWhich equation describes this model?",
image="ch19-quiz-lizard.png",
options="""A) territoryᵢ = -31.54 + 11.68 × biteᵢ + eᵢ
B) territoryᵢ = 11.68 - 31.54 × biteᵢ + eᵢ
C) biteᵢ = -31.54 + 11.68 × territoryᵢ + eᵢ
D) territoryᵢ = -31.54 + 11.68 × biteᵢ""",
answer="A",
explanation="Each lizard's territory equals the intercept plus the slope times its bite force, plus its residual. Territory increases by about 11.7 m² per newton of bite force.",
why_wrong="""B) Swaps intercept and slope.
C) Swaps the response and explanatory variables.
D) That's the prediction (Ŷ), not the observation (Yᵢ needs + eᵢ).""",
hint="Yᵢ = intercept + slope × xᵢ + residual."),

dict(id="ch19-quiz-02", source="Regression quiz (2026), Q3", topics="confidence intervals, slope", type="MC",
question=LIZ + "\n\n" + LIZ_OUT + "\n\nWhat is the 95% confidence interval for the slope, and what does it tell us?",
options="""A) (-84.7, 21.7); the slope could plausibly be zero
B) (0.71, 22.6); all positive, but from tiny to large
C) (0.71, 22.6); the true slope is exactly 11.68
D) (4.85, 11.68); the slope is very precisely known""",
answer="B",
explanation="The slope's CI runs from 0.71 to 22.6 m² per N. It excludes zero (consistent with p = 0.039), but with only 11 lizards it's very wide.",
why_wrong="""A) That's the intercept's CI.
C) 11.68 is the estimate; the CI says many other values are plausible.
D) Those are the SE and the estimate.""",
hint="Find the row for bite."),

dict(id="ch19-quiz-03", source="Regression quiz (2026), Q4", topics="residuals, predictions", type="numeric",
question=LIZ + "\n\nThe fitted model is territory = -31.54 + 11.68 × bite. A lizard with a bite force of 5.2 N has a territory of 28 m². What is its residual?",
answer="-1.18", explanation="Prediction = -31.54 + 11.68 × 5.2 = 29.18 m². Residual = 28 - 29.18 = -1.18 m².",
why_wrong="Common mistake: predicted - observed (+1.18).",
hint="Predict first, then subtract the prediction from the observed value."),

dict(id="ch19-quiz-04", source="Regression quiz (2026), Q5-6", topics="extrapolation, predictions", type="MC",
question=LIZ + "\n\nThe fitted model is territory = -31.54 + 11.68 × bite. Plugging in a bite force of 2.5 N gives a predicted territory of -2.3 m². What's wrong with this prediction?",
options="""A) Nothing; the model simply predicts a small territory
B) It's an extrapolation far below the bite forces we measured
C) We should have used the confidence interval instead
D) The slope isn't significant, so no prediction is possible""",
answer="B",
explanation="The model only describes lizards with bite forces between about 4.3 and 5.4 N. Far outside that range the straight line need not hold, as the impossible negative area shows.",
why_wrong="""A) A territory can't be negative.
C) A CI wouldn't fix an extrapolation.
D) p = 0.039, and significance isn't the issue.""",
hint="What range of bite forces was the model built on?"),

dict(id="ch19-quiz-05", source="Regression quiz (2026), Q7", topics="regression assumptions, diagnostics", type="open", include="no",
question=LIZ + "\n\nThe diagnostic plots for lm(territory ~ bite) are shown. Which (if any) assumptions of the linear model concern you? Point to features of the study design and/or the plots. What, if anything, can you do about it?",
image="ch19-quiz-lizard-diag.png",
answer="Model answer: With only 11 lizards, the diagnostic plots can't tell us much: patterns could easily be noise, and a single lizard can strongly influence the slope. Bite force covers a narrow range (4.3 to 5.4 N), so linearity can't really be checked. Independence could be an issue if neighboring lizards' territories constrain each other. Unbiased sampling matters too (were the lizards a random sample, or the easiest to catch?). Options: interpret cautiously, check robustness by refitting without the most influential point, use a permutation test or bootstrap, and collect more data across a wider range of bite forces.",
explanation="Good answers connect assumptions to the study (small n, narrow x range, possible non-independence of territories) and suggest sensible checks.",
hint="Think about sample size, the range of bite forces, and whether one lizard's territory affects another's."),

dict(id="ch19-quiz-06", source="Regression quiz (2026), Q8", topics="R squared", type="numeric",
question=LIZ + "\n\n" + LIZ_OUT + "\n\nWhat proportion of the variance in territory area is explained by bite force in this study?",
answer="0.392", explanation="That's R² = 0.392: about 39% of the variation in territory size among these lizards is associated with bite force.",
why_wrong="Common mistake: reporting the p-value (0.039) or the correlation (r = 0.63).",
hint="Which statistic is the proportion of variance explained?"),

dict(id="ch19-quiz-07", source="Regression quiz (2026), Q9", topics="measurement error", type="select-all",
question=LIZ + "\n\nOur measurements of bite force (x) are probably off by some random amount. This means: (Select all that apply.)",
options="""A) Our estimate of the slope is likely biased upwards (farther from zero than the true slope)
B) Our estimate of the slope is likely biased downwards (closer to zero than the true slope)
C) Uncertainty in the estimate is larger than if we had perfect measurements
D) Uncertainty in the estimate is smaller than if we had perfect measurements
E) Nothing: measurement error is accounted for in regressions""",
answer="B, C",
explanation="Random error in x blurs the relationship, pulling the estimated slope toward zero ('regression dilution') and adding noise.",
why_wrong="""A) Error in x biases the slope toward zero, not away.
D) Extra noise increases uncertainty.
E) Standard regression assumes x is measured without error.""",
hint="If x were pure noise, what slope would you estimate?"),

dict(id="ch19-quiz-08", source="Regression quiz (2026), Q10", topics="measurement error", type="select-all",
question=LIZ + "\n\nOur measurements of territory size (y) are probably off by some random amount. This means: (Select all that apply.)",
options="""A) Our estimate of the slope is likely biased upwards
B) Our estimate of the slope is likely biased downwards
C) Uncertainty in the estimate is larger than if we had perfect measurements
D) Uncertainty in the estimate is smaller than if we had perfect measurements
E) Nothing: measurement error is accounted for in regressions""",
answer="C",
explanation="Random error in y just adds to the residual variation: the slope stays unbiased, but its standard error grows.",
why_wrong="""A) and B) Error in y doesn't bias the slope.
D) More noise means more uncertainty.
E) It's absorbed into the residuals, which increases uncertainty.""",
hint="Where does random error in the response end up in a regression?"),

dict(id="ch19-quiz-09", source="Regression quiz (2026), Q11-12", topics="NHST, interpreting results", type="MC",
question=LIZ + "\n\n" + LIZ_OUT + "\n\nAt α = 0.05, what do we do with the null hypothesis (slope = 0), and what does that mean?",
options="""A) Reject it; the null is false
B) Reject it; but the null could still be true
C) Fail to reject it; the null is true
D) Fail to reject it; we can't say for sure""",
answer="B",
explanation="p = 0.039 < 0.05, so we reject. That doesn't prove the null false, especially with 11 lizards and a p-value near the threshold.",
why_wrong="""A) Rejecting isn't proof.
C) and D) p is below α.""",
hint="Compare p with α, then think about what a p-value can't do."),

dict(id="ch19-quiz-10", source="Regression quiz (2026), Q13", topics="causation, study design", type="open", include="no",
question=LIZ + "\n\nTwo explanations for the pattern: (1) males with stronger bites win bigger territories; (2) males with bigger territories get stronger bites (e.g. by eating better). Which do you prefer and why? Describe an experiment to tease these apart. Can you think of other explanations?",
answer="Model answer: Either is plausible, and this observational regression can't distinguish them; it shows an association, not its direction. A third variable (e.g. body size or age) could also drive both. Experiments: (1) for bite → territory, reduce some males' bite force (or compare matched males) and see whether they lose territory; (2) for territory → bite, give some males larger or richer territories and measure bite force later. Measuring and adjusting for body size would address the third-variable explanation.",
explanation="The key ideas: correlation doesn't show direction, confounders are possible, and manipulative experiments can separate cause from effect.",
hint="What could you manipulate, and what would you measure afterward?"),

# ---------------- Homework (SR petal area) ----------------
dict(id="ch19-hw-01", source="Regression homework, Q1", topics="confidence vs prediction intervals", type="matching",
question=SRP + "\n\nThe grey band in the plot is a (1) ____ interval. If we wanted the band to show where we expect individual observations to fall, we'd use a (2) ____ interval, and the band would be (3) ____.",
image="ch19-hw-sr.png",
options="""A) confidence
B) prediction
C) wider
D) narrower""",
answer="1-A, 2-B, 3-C",
explanation="A confidence band shows uncertainty in the mean response at each x. A prediction interval also includes the scatter of individual points around that mean, so it's much wider.",
why_wrong="Common mix-up: thinking the grey band should contain most points. It describes the mean, not individuals.",
hint="Is the band about the line or about individual RILs?"),

dict(id="ch19-hw-02", source="Regression homework, Q1b", topics="confidence intervals, interpretation", type="MC",
question=SRP + "\n\nThe grey band is a 95% confidence interval. What does it mean?",
image="ch19-hw-sr.png",
options="""A) If we repeatedly sampled data and refit the model, about 95% of such intervals would contain the true mean response at each x
B) 95% of new observations will fall within this band
C) There is a 95% probability that the true mean response lies within this particular band
D) The band shows the range of fitted values predicted by the model""",
answer="A",
explanation="Like any confidence interval, the '95%' describes how often intervals built this way capture the true value (here, the true mean response at each x).",
why_wrong="""B) That would be a prediction interval.
C) A common misreading: the true mean either is or isn't in this particular band.
D) The fitted values are the line itself.""",
hint="What does the 95% in a confidence interval refer to?"),

dict(id="ch19-hw-03", source="Regression homework, Q2-3", topics="regression assumptions, diagnostics", type="select-all",
question=SRP + "\n\nConsider the diagnostic plots. Which assumptions do they show to be violated? (Select all that apply.)",
image="ch19-hw-sr-diag.png",
options="""A) Normality of residuals
B) Homoscedasticity (equal variance)
C) Independence
D) Unbiased data collection""",
answer="A, B",
explanation="The QQ plot curves away from the line (skewed residuals: many RILs set no hybrid seed), and the spread of residuals changes with fitted values. Independence and bias can't be judged from these plots; they depend on the study design.",
why_wrong="C) and D) Diagnostic plots can't show these.",
hint="Which assumptions can a residual plot actually reveal?"),

dict(id="ch19-hw-04", source="Regression homework, Q3", topics="regression assumptions", type="MC",
question=SRP + "\n\nThe residuals are non-normal and their variance isn't constant. How should we treat the analysis?",
options="""A) Throw it in the garbage: the data don't meet assumptions
B) Note the violations and check results with resampling
C) Don't worry about it: linear models never need assumptions""",
answer="B",
explanation="Linear models are fairly robust, especially with 113 points, but we should be honest about violations and check that conclusions hold with methods that don't rely on them.",
why_wrong="""A) Real data rarely meet every assumption; this throws away useful information.
C) Ignoring violations risks overconfident conclusions.""",
hint="What's the middle ground between ignoring and discarding?"),

dict(id="ch19-hw-05", source="Regression homework, Q4", topics="regression slope, covariance", type="numeric",
question=SRP + "\n\nMean petal area = 62.9 mm²; variance in petal area = 232; mean proportion hybrid = 0.173; variance in proportion hybrid = 0.0651; covariance = 0.92.\n\nHow much do we expect the proportion of hybrid seed to change for each 1 mm² increase in petal area?",
answer="0.004", explanation="Slope = cov(x, y) / var(x) = 0.92 / 232 = 0.0040.",
why_wrong="Common mistake: dividing by the variance of y (0.92 / 0.0651 = 14.1).",
hint="Slope = covariance / variance of x."),

dict(id="ch19-hw-06", source="Regression homework, Q5", topics="intercept, extrapolation", type="MC",
question=SRP + "\n\nThe intercept is -0.078. What does a negative intercept mean here?",
options="""A) We should not believe our model, since it can't be negative
B) We expect a flower with no petals to have negative hybrid seed
C) It anchors the line; zero petal area is far outside our data""",
answer="C",
explanation="The intercept is where the line crosses x = 0. No plant has zero petal area (they range from about 35 to 110 mm²), so it's just an anchor for the line, not a biological prediction.",
why_wrong="""A) A meaningless intercept doesn't invalidate the slope.
B) Literally what the line says at x = 0, but that's an extrapolation we shouldn't make.""",
hint="Is zero petal area within the range of the data?"),

dict(id="ch19-hw-07", source="Regression homework, Q6", topics="sums of squares, deviations", type="matching",
question=SRP + "\n\nEach plot shows 30 randomly chosen RILs, the regression line (blue) and the mean proportion hybrid (black). Match each plot to the deviations it shows:\n\n1. Plot A\n2. Plot B\n3. Plot C",
image="ch19-hw-sr-deviations.png",
options="""A) Error
B) Total
C) Model""",
answer="1-A, 2-B, 3-C",
explanation="A: points to the regression line (error). B: points to the mean (total). C: the line to the mean (model).",
why_wrong="Check where each pink line starts and ends.",
hint="Which plot's lines never touch the points?"),

dict(id="ch19-hw-08", source="Regression homework, Q7", topics="sums of squares", type="matching",
question=SRP + """

model_dat |>
  summarise(ssa = sum((.fitted - grand_mean)^2),
            ssb = sum((prop_hybrid - .fitted)^2),
            ssc = sum((prop_hybrid - grand_mean)^2))

ssa = 0.413; ssb = 6.88; ssc = 7.29

Match each to its sum of squares:

1. ssa
2. ssb
3. ssc""",
options="""A) Model
B) Error
C) Total""",
answer="1-A, 2-B, 3-C",
explanation="ssa compares predictions to the mean (model), ssb compares observations to predictions (error), and ssc compares observations to the mean (total). Check: 0.413 + 6.88 = 7.29.",
why_wrong="Common mix-up: model vs total.",
hint=".fitted is each RIL's predicted value."),

dict(id="ch19-hw-09", source="Regression homework, Q8-9", topics="degrees of freedom, F statistic", type="numeric",
question=SRP + "\n\nSS model = 0.413 and SS error = 6.88, with 113 data points. The model has 1 and 111 degrees of freedom. What is F?",
answer="6.66", explanation="MS model = 0.413 / 1 = 0.413. MS error = 6.88 / 111 = 0.0620. F = 0.413 / 0.0620 = 6.66.",
why_wrong="Common mistakes: using 112 or 113 for the error df, or F = SS model / SS error (0.06).",
hint="Error df = n - 2 for a simple regression."),

dict(id="ch19-hw-10", source="Regression homework, Q8", topics="degrees of freedom", type="matching",
question=SRP + "\n\nA simple regression on 113 data points. Match each degree of freedom to its value:\n\n1. df1 (model)\n2. df2 (error)",
options="""A) 1
B) 2
C) 111
D) 112""",
answer="1-A, 2-C",
explanation="The model estimates one slope beyond the mean (df = 1). Error df = n - 2 = 111 (we estimated an intercept and a slope).",
why_wrong="Common mistake: n - 1 = 112 for the error df.",
hint="How many parameters did the model estimate?"),

dict(id="ch19-hw-11", source="Regression homework, Q10-11", topics="p-values, NHST", type="MC",
question=SRP + "\n\nF = 6.66 on 1 and 111 df gives p = 0.011. How would you describe this p-value, and what do we do with the null?",
options="""A) Extremely small (p < 10⁻⁷); reject
B) Comfortably below 0.05 but not minuscule; reject
C) Near significance (0.05 < p < 0.10); fail to reject
D) Large (p > 0.10); fail to reject""",
answer="B",
explanation="p = 0.011 < 0.05, so we reject the null of no relationship between petal area and hybrid seed.",
why_wrong="A) It's not that small. C) and D) p is below 0.05.",
hint="Compare 0.011 to 0.05."),

dict(id="ch19-hw-12", source="Regression homework, Q13", topics="R squared", type="numeric",
question=SRP + "\n\nSS model = 0.413 and SS total = 7.29. What proportion of the variance in proportion hybrid seed is explained by petal area in this sample?",
answer="0.057", explanation="R² = 0.413 / 7.29 = 0.057. Petal area is significantly associated with hybrid seed, but it explains less than 6% of the variation.",
why_wrong="Common mistake: SS model / SS error (0.06): close here, but not the right formula.",
hint="R² = SS model / SS total."),

# ---------------- ChimeIn ----------------
dict(id="ch19-chimein-01", source="Chime In (regression), Q1-5", topics="regression concepts", type="matching",
question="Match each description to the term it describes:\n\n1. How much two variables jointly deviate from their means\n2. How predictably the response changes with x (strength of the linear relationship)\n3. The difference between an observation and its predicted value\n4. How much the response changes with x",
options="""A) Covariance
B) Correlation
C) Residual
D) Slope
E) Intercept""",
answer="1-A, 2-B, 3-C, 4-D",
explanation="Covariance measures joint deviation (in units of x times y). Correlation standardizes it to measure how tightly points follow a line. The slope gives the change in y per unit x. A residual is observed minus predicted.",
why_wrong="Common mix-up: correlation (how predictable) vs slope (how much).",
hint="Which one has no units?"),

dict(id="ch19-chimein-02", source="Chime In (regression), Q6-8", topics="test statistics, p-values, R squared", type="matching",
question="Match each quantity to what it measures:\n\n1. F and t\n2. p\n3. R²",
options="""A) Deviation from the null
B) Surprise (how unusual the data would be under the null)
C) Strength of association""",
answer="1-A, 2-B, 3-C",
explanation="F and t measure how far the estimate is from the null in standardized units. p converts that into how surprising the data would be if the null were true. R² measures the proportion of variance explained.",
why_wrong="Common mix-up: p and the test statistic. The p-value is the probability; t and F are distances.",
hint="Which one is a probability?"),

dict(id="ch19-chimein-03", source="Chime In (regression), Q9-13", topics="sums of squares", type="matching",
question="In linear models, each observation Yᵢ equals its prediction Ŷᵢ plus its residual eᵢ. Match each expression to the sum of squares it represents:\n\n1. Σ(Yᵢ - Ŷᵢ)²\n2. Σ(Ŷᵢ - Ȳ)²\n3. Σ(Yᵢ - Ȳ)²",
options="""A) SS model
B) SS error
C) SS total""",
answer="1-B, 2-A, 3-C",
explanation="Observations minus predictions: error. Predictions minus the mean: model. Observations minus the mean: total.",
why_wrong="Common mix-up: model vs total.",
hint="Ŷ is the prediction and Ȳ is the overall mean."),

dict(id="ch19-chimein-04", source="Chime In (regression), Q17", topics="measurement error", type="select-all",
question="There is often measurement error, so values of x or y might not be exactly right. Random measurement error in X tends to: (Select all that apply.)",
options="""A) Bring the estimated slope closer to zero than it really is
B) Bring the estimated correlation closer to zero than it really is
C) Add unbiased noise to the estimated slope, increasing its standard error
D) Not affect the estimated slope""",
answer="A, B",
explanation="Error in x weakens the apparent relationship: both the slope and the correlation are biased toward zero ('regression dilution').",
why_wrong="""C) That's what error in y does to the slope.
D) Error in x does bias the slope.""",
hint="If x were measured with huge error, what would the scatterplot look like?"),

dict(id="ch19-chimein-05", source="Chime In (regression), Q18", topics="measurement error", type="select-all",
question="Random measurement error in Y tends to: (Select all that apply.)",
options="""A) Bring the estimated slope closer to zero than it really is
B) Bring the estimated correlation closer to zero than it really is
C) Add unbiased noise to the estimated slope, increasing its standard error
D) Not affect the estimated correlation""",
answer="B, C",
explanation="Error in y adds scatter around the line: the slope stays unbiased but less precise, while the correlation (which measures how tightly points follow the line) drops.",
why_wrong="""A) Error in y doesn't bias the slope.
D) More scatter lowers the correlation.""",
hint="Does adding noise to y tilt the line, or just scatter points around it?"),

# ---------------- Book: Regression summary (pink RILs at GC) ----------------
dict(id="ch19-book-01", source="Book: Regression summary (Q1-2)", topics="confidence intervals", type="MC",
question=GCV + "\n\nThe grey band is a 95% confidence interval. What does it mean?",
image="ch19-book-regression.png",
options="""A) 95% of data points should fall in that region
B) The true mean proportion hybrid seed, conditional on visits, is plausibly within this region
C) 95% of future observations should fall in that region
D) There is a 95% chance that the true mean proportion hybrid seed, conditional on visits, is within this region""",
answer="B", near_duplicate_of="ch19-hw-02",
explanation="A confidence band describes uncertainty in the mean response at each x: a range of plausible values for the true line.",
why_wrong="""A) and C) Those describe individual observations (a prediction interval).
D) Treats the 95% as a probability about this one band.""",
hint="Is the band about the line or about individual RILs?"),

dict(id="ch19-book-02", source="Book: Regression summary (Q3-4)", topics="regression, intercept, slope", type="MC",
question=GCV + "\n\nVisually estimate the intercept and slope of the blue line.",
image="ch19-book-regression.png",
options="""A) Intercept ≈ 0.2, slope ≈ 0.27
B) Intercept ≈ 0.2, slope ≈ 0.73
C) Intercept ≈ 0, slope ≈ 0.27
D) Intercept ≈ 0.73, slope ≈ 0.2""",
answer="A",
explanation="The line starts near 0.2 at zero visits and rises to about 0.73 at 2 visits: (0.73 - 0.2) / 2 ≈ 0.27 per visit. The fitted values are 0.208 and 0.262.",
why_wrong="""B) 0.73 is the height at x = 2, not the slope.
C) The line doesn't start at zero.
D) Swaps them.""",
hint="Slope = rise / run between two points on the line."),

dict(id="ch19-book-03", source="Book: Regression summary (Q5-6)", topics="regression slope, correlation", type="matching",
question=GCV + "\n\nSample size 49; covariance between visits and proportion hybrid = 0.039.\n\nvariable | mean | var | sd\nprop_hybrid | 0.260 | 0.078 | 0.280\nvisits | 0.197 | 0.149 | 0.386\n\nMatch each quantity to its value:\n\n1. The slope (change in proportion hybrid per extra visit)\n2. The correlation",
options="""A) 0.26
B) 0.36
C) 0.04
D) 0.78""",
answer="1-A, 2-B",
explanation="Slope = cov / var(visits) = 0.039 / 0.149 = 0.26. Correlation = cov / (sd_x × sd_y) = 0.039 / (0.386 × 0.280) = 0.36.",
why_wrong="C) is the covariance. D) is unrelated here.",
hint="Slope divides by the variance of x; correlation divides by both SDs."),

dict(id="ch19-book-04", source="Book: Regression summary (Q7)", topics="intercept, p-values", type="MC",
question=GCV + "\n\nThe intercept is 0.208 (SE 0.042, p = 1.1 × 10⁻⁵). Why don't we care about this p-value?",
options="""A) Because a p-value this small is probably wrong
B) It tests a null (no hybrid seed at zero visits) no one proposed
C) Because p-values are P(data | model), not P(model | data)
D) We do care: it shows visits affect hybrid seed""",
answer="B",
explanation="The intercept's p-value tests whether the predicted hybrid proportion at zero visits is zero. That's not a biological question anyone asked, and several RILs with no observed visits already set hybrid seed.",
why_wrong="""A) Small p-values aren't wrong for being small.
C) True of all p-values, so it doesn't single out this one.
D) It tests an uninteresting null.""",
hint="What null hypothesis does the intercept's p-value test?"),

dict(id="ch19-book-05", source="Book: Regression summary (Q8)", topics="predictions", type="numeric",
question=GCV + "\n\nThe fitted model is prop_hybrid = 0.208 + 0.262 × visits. Predict the proportion hybrid seed for a RIL that received half a visit (on average) per observation session.",
answer="0.339", explanation="0.208 + 0.262 × 0.5 = 0.208 + 0.131 = 0.339.",
why_wrong="Common mistake: forgetting the intercept (0.131).",
hint="Prediction = intercept + slope × x."),

dict(id="ch19-book-06", source="Book: Regression summary (Q9)", topics="extrapolation", type="MC",
question=GCV + "\n\nVisits in these data ranged from 0 to 2 per observation session. Should we predict the proportion hybrid seed for a RIL with 3 visits per session?",
options="""A) Yes: 0.208 + 0.262 × 3 = 0.994
B) No: 3 visits is beyond our data, so it's an extrapolation
C) Yes, but only if we report it with a prediction interval""",
answer="B",
explanation="Our data stop at 2 visits. The prediction (0.99) is close to the maximum possible proportion, a sign that the straight line can't continue far beyond the data.",
why_wrong="""A) The arithmetic works, but the prediction isn't trustworthy.
C) A prediction interval doesn't fix extrapolation.""",
hint="What range of visits did we observe?"),

dict(id="ch19-book-07", source="Book: Regression summary (Q10-11)", topics="regression assumptions, diagnostics", type="MC",
question=GCV + "\n\nThe diagnostic plots for lm(prop_hybrid ~ visits) are shown. Which assumption seems most problematic, and how would you move forward?",
image="ch19-book-diagnostics.png",
options="""A) Normality of residuals and equal variance; treat the model as a useful first summary but check robustness (bootstrap or permutation, and refitting without influential points)
B) Independence, because the plots prove nearby plants influenced each other; delete extreme points
C) The existence of an intercept, because its p-value is small; report only the intercept
D) Random sampling of x, because visits must be normally distributed; ignore the diagnostics""",
answer="A",
explanation="The QQ plot bends away from the line and the residual spread changes with fitted values, which is typical for proportions with many zeros. A linear model is still a reasonable summary, but robustness checks are wise.",
why_wrong="""B) Diagnostic plots can't prove non-independence, and deleting points isn't a fix.
C) Not an assumption.
D) x doesn't need to be normal.""",
hint="Look at the QQ plot and at whether residual spread changes across fitted values."),

dict(id="ch19-book-08", source="Book: Regression summary (Q12-13)", topics="outliers, leverage, influence", type="matching",
question=GCV + "\n\nUsing the labeled points in the diagnostic plots, match each description to a data point:\n\n1. The greatest outlier (largest residual)\n2. The most influential point (high leverage and large residual)",
image="ch19-book-diagnostics.png",
options="""A) 34
B) 13
C) 9
D) 44""",
answer="1-A, 2-B",
explanation="Point 34 has the largest residual (top of the residuals and QQ plots). Point 13 has by far the highest leverage, with a sizable residual, so it pulls the line most (in the residuals vs leverage plot).",
why_wrong="9 is a big residual but not the biggest; 44 has moderate leverage.",
hint="Outliers are far from the line; influence also needs leverage (an extreme x)."),

dict(id="ch19-book-09", source="Book: Regression summary (Q14)", topics="influence, robustness", type="MC",
question="How would you check whether influential points are undermining your conclusions?",
options="""A) Remove every point with a large residual and refit the model
B) Check whether the intercept p-value is still small
C) Use only the plot with the nicest-looking regression line
D) Refit without the influential point(s) and compare the results""",
answer="D",
explanation="A sensitivity analysis: if conclusions change a lot without one or two points, report that they depend on those points.",
why_wrong="""A) Deleting inconvenient points is data manipulation.
B) The intercept isn't the question.
C) Cherry-picking.""",
hint="How would you see whether one point drives the result?"),

dict(id="ch19-book-10", source="Book: Regression summary (Q15-17)", topics="sums of squares, deviations", type="matching",
question=GCV + "\n\nEach panel shows the RILs, the regression line (blue) and the mean proportion hybrid (black). Match each kind of deviation to its panel:\n\n1. Model deviation\n2. Total deviation\n3. Residual deviation",
image="ch19-book-deviations.png",
options="""A) Panel A
B) Panel B
C) Panel C""",
answer="1-C, 2-A, 3-B",
explanation="A: points to the mean (total). B: points to the line (residual). C: line to the mean (model).",
why_wrong="Check where each line starts and ends.",
hint="Which panel's lines never touch the points?"),

dict(id="ch19-book-11", source="Book: Regression summary (Q18-22)", topics="sums of squares, R squared", type="MC",
question=GCV + """

lm(prop_hybrid ~ visits, data1) |> augment() |>
  summarise(ssa = sum((prop_hybrid - .fitted)^2),
            ssb = sum((.fitted - mean(prop_hybrid))^2),
            ssc = sum((prop_hybrid - mean(prop_hybrid))^2))

ssa = 3.26; ssb = 0.493; ssc = 3.76

Which statement is correct?""",
options="""A) ssa is SS error, ssb is SS model, ssc is SS total, and R² = ssb / ssc = 0.13
B) ssa is SS model, ssb is SS error, ssc is SS total, and R² = ssa / ssc = 0.87
C) ssa is SS error, ssb is SS model, ssc is SS total, and R² = ssb / ssa = 0.15
D) SS total = SS model / SS error""",
answer="A",
explanation="SS total = SS model + SS error (0.493 + 3.26 = 3.76), and R² = SS model / SS total = 0.493 / 3.76 = 0.13.",
why_wrong="""B) Mixes up model and error.
C) R² divides by SS total, not SS error.
D) The SSs add; they don't divide.""",
hint="Which line compares observations to predictions?"),

dict(id="ch19-book-12", source="Book: Regression summary (Q23)", topics="null hypothesis, regression", type="MC",
question=GCV + "\n\nWhat is the null hypothesis for testing this regression?",
options="""A) The true slope relating pollinator visits to proportion hybrid seed is zero
B) The true intercept is zero
C) The observed number of pollinator visits is zero
D) The model explains all variation in proportion hybrid seed""",
answer="A",
explanation="The regression test asks whether the response changes with x at all, i.e. whether the true slope is zero.",
why_wrong="""B) That's the uninteresting intercept test.
C) Not a hypothesis about a parameter.
D) That would mean R² = 1.""",
hint="What would 'no relationship' look like for a line?"),

dict(id="ch19-book-13", source="Book: Regression summary (Q24)", topics="F statistic", type="numeric",
question=GCV + "\n\nSS model = 0.493 and SS error = 3.26, with N = 49. What is F?",
answer="7.1", explanation="df = 1 and 47. MS model = 0.493; MS error = 3.26 / 47 = 0.0694. F = 0.493 / 0.0694 = 7.1.",
why_wrong="Common mistake: using 48 or 49 for the error df.",
hint="Error df = n - 2."),

dict(id="ch19-book-14", source="Book: Regression summary (Q25-27)", topics="NHST, interpreting results", type="MC",
question=GCV + "\n\nF = 7.1 on 1 and 47 df gives p = 0.011. What do we do, and what does it mean?",
options="""A) Reject the null; pollinator visits definitely cause hybrid seed
B) Reject the null; visits are associated with hybrid seed
C) Fail to reject the null; there is no relationship at all
D) Reject the null; the model explains all variation in hybrid seed""",
answer="B",
explanation="p < 0.05, so we reject. That's evidence of an association, not proof of causation, and the model explains only about 13% of the variation.",
why_wrong="""A) An association isn't proof of causation.
C) p is below 0.05.
D) R² is only 0.13.""",
hint="What can, and can't, a significant regression tell you?"),
]
