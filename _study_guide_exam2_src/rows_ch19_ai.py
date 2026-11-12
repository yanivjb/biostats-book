from ai_helpers import V, r
from scipy.stats import f as F
import importlib.util, os
spec = importlib.util.spec_from_file_location('o19', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rows_ch19.py')); o = importlib.util.module_from_spec(spec); spec.loader.exec_module(o)
LIZ, LIZ_OUT, GCV, SRP = o.LIZ, o.LIZ_OUT, o.GCV, o.SRP
L = LIZ + "\n\n" + LIZ_OUT
SR_SUM = "Mean petal area = 62.9 mm²; variance in petal area = 232; mean proportion hybrid = 0.173; variance in proportion hybrid = 0.0651; covariance = 0.92."
GC_SUM = "Sample size 49; covariance between visits and proportion hybrid = 0.039.\n\nvariable | mean | var | sd\nprop_hybrid | 0.260 | 0.078 | 0.280\nvisits | 0.197 | 0.149 | 0.386"
ROWS = [
V("ch19-quiz-01", 1, image="ch19-quiz-lizard.png", question=L + "\n\nIn the equation territoryᵢ = a + b × biteᵢ + eᵢ, what is eᵢ?",
options="""A) The residual: lizard i's territory minus its prediction
B) The standard error of the slope for lizard i
C) The predicted territory size for lizard i
D) The bite force of lizard i, minus the mean bite force""", answer="A",
explanation="eᵢ is lizard i's residual: what's left after the line's prediction.",
why_wrong="""B) Standard errors describe estimates, not individual lizards.
C) That's a + b × biteᵢ.
D) That's a deviation in x.""", hint="Observed = predicted + ?"),
V("ch19-quiz-01", 2, image="ch19-quiz-lizard.png", question=L + "\n\nWhich equation gives the model's PREDICTED territory size for lizard i?",
options="""A) territorŷᵢ = -31.54 + 11.68 × biteᵢ
B) territorŷᵢ = -31.54 + 11.68 × biteᵢ + eᵢ
C) territorŷᵢ = 11.68 - 31.54 × biteᵢ
D) territorŷᵢ = -31.54 + 4.85 × biteᵢ""", answer="A",
explanation="Predictions come from the line alone; the residual is the gap between the observation and the prediction.",
why_wrong="""B) Adding eᵢ gives the observed value.
C) Swaps intercept and slope.
D) Uses the slope's SE instead of the slope.""", hint="Predictions have no residual term."),

V("ch19-quiz-02", 1, question=L + "\n\nWhat is the 95% confidence interval for the intercept, and does it include zero?",
options="""A) (-84.7, 21.7); yes, it includes zero
B) (0.71, 22.6); no, it excludes zero
C) (-84.7, 21.7); no, it excludes zero
D) (23.5, 4.85); yes, it includes zero""", answer="A",
explanation="The intercept's CI is -84.73 to 21.65, which includes zero.",
why_wrong="""B) That's the slope's CI.
C) The interval spans zero.
D) Those are standard errors.""", hint="Look at the (Intercept) row."),
V("ch19-quiz-02", 2, question=L + "\n\nWhy is the slope's 95% CI (0.71 to 22.6) so wide?",
options="""A) With only 11 lizards, the slope's SE is large
B) Because the slope is statistically significant
C) Because bite force causes larger territories
D) Because R² is greater than 0.3""", answer="A",
explanation="Small samples give large SEs (4.85 here), so the CI (estimate ± about 2.26 × SE) is wide.",
why_wrong="""B) Significance doesn't widen a CI.
C) Causation isn't shown and doesn't affect width.
D) R² doesn't set the CI width directly.""", hint="CI = estimate ± critical t × SE."),

V("ch19-quiz-03", 1, question=LIZ + "\n\nThe fitted model is territory = -31.54 + 11.68 × bite. A lizard with a bite force of 4.5 N has a territory of 25 m². What is its residual?",
answer=r(25-(-31.54+11.68*4.5),2), explanation="Prediction = -31.54 + 11.68 × 4.5 = 21.02. Residual = 25 - 21.02 = 3.98 m².", hint="Observed - predicted."),
V("ch19-quiz-03", 2, question=LIZ + "\n\nThe fitted model is territory = -31.54 + 11.68 × bite. What territory size does the model predict for a lizard with a bite force of 5.0 N?",
answer=r(-31.54+11.68*5,2), explanation="-31.54 + 11.68 × 5.0 = 26.86 m².", hint="Intercept + slope × 5.0."),

V("ch19-quiz-04", 1, question=LIZ + "\n\nThe fitted model is territory = -31.54 + 11.68 × bite. Which prediction is most trustworthy?",
options="""A) For a lizard with a bite force of 4.8 N
B) For a lizard with a bite force of 2.0 N
C) For a lizard with a bite force of 8.0 N
D) All are equally trustworthy""", answer="A",
explanation="4.8 N lies within the observed range (4.3 to 5.4 N); the others are extrapolations.",
why_wrong="""B) and C) Far outside the data.
D) Extrapolations are less trustworthy.""", hint="Which is inside the data?"),
V("ch19-quiz-04", 2, question=LIZ + "\n\nThe fitted model is territory = -31.54 + 11.68 × bite. For a lizard with a 10 N bite, the model predicts 85.3 m². Why should we be cautious?",
options="""A) 10 N is far above the bite forces we observed
B) The prediction is a positive number of square meters
C) The slope's confidence interval doesn't include zero
D) We shouldn't; the model gives a sensible prediction""", answer="A",
explanation="Our data cover 4.3 to 5.4 N; we don't know if the line holds far beyond that.",
why_wrong="""B) Positive is fine.
C) Irrelevant to extrapolation.
D) Plausible-looking extrapolations are still extrapolations.""", hint="Range of the data."),

V("ch19-quiz-06", 1, question=L + "\n\nWhat proportion of the variance in territory area is NOT explained by bite force in this study?",
answer=r(1-0.392,3), explanation="1 - R² = 1 - 0.392 = 0.608.", hint="1 - R²."),
V("ch19-quiz-06", 2, question=L + "\n\nWhat is the correlation between bite force and territory size? (The slope is positive.) Report it to two decimals.",
answer=r(0.392**0.5,2), explanation="In a simple regression, r = ±√R² = √0.392 = 0.63 (positive, like the slope).", hint="√R², with the slope's sign."),

V("ch19-quiz-07", 1, question=LIZ + "\n\nIf we measured bite force (x) perfectly, instead of with random error, what would we expect? (Select all that apply.)",
options="""A) The estimated slope would tend to be farther from zero
B) The estimated slope would tend to be closer to zero
C) The slope's uncertainty would be smaller
D) Nothing would change""", answer="A, C",
explanation="Removing error in x removes regression dilution (the slope moves away from zero toward its true value) and reduces noise.",
why_wrong="""B) Error in x biases toward zero; removing it does the reverse.
D) Error in x does matter.""", hint="Regression dilution."),
V("ch19-quiz-07", 2, question="A biologist measures body size (x) with a lot of random error and regresses metabolic rate (y) on it. Compared with the true relationship, the estimated slope is likely to be: (Select all that apply.)",
options="""A) Closer to zero than the true slope
B) Farther from zero than the true slope
C) Less precise than with perfect measurements
D) Exactly unbiased, because error averages out""", answer="A, C",
explanation="Error in x dilutes the slope toward zero and adds noise.",
why_wrong="""B) Bias is toward zero.
D) Error in x does not average out in the slope.""", hint="Regression dilution."),

V("ch19-quiz-08", 1, question=LIZ + "\n\nIf we measured territory size (y) perfectly, instead of with random error, what would we expect? (Select all that apply.)",
options="""A) The estimated slope would tend to be farther from zero
B) The estimated slope would be no more or less biased
C) The slope's uncertainty would be smaller
D) The slope's uncertainty would be larger""", answer="B, C",
explanation="Error in y doesn't bias the slope, so removing it doesn't change bias, but it reduces residual scatter and the SE.",
why_wrong="""A) Error in y doesn't bias the slope.
D) Less error means less uncertainty.""", hint="Error in y vs error in x."),
V("ch19-quiz-08", 2, question="A biologist measures metabolic rate (y) with a lot of random error and regresses it on body size (x), measured precisely. The estimated slope is likely to be: (Select all that apply.)",
options="""A) Unbiased, but with a larger standard error
B) Biased toward zero, with a smaller standard error
C) Biased away from zero, with a larger standard error
D) Biased toward zero, with the same standard error""", answer="A",
explanation="Random error in y just adds residual scatter: no bias, more uncertainty.",
why_wrong="""B), C) and D) Error in y doesn't bias the slope.""", hint="Which variable has the error?"),

V("ch19-quiz-09", 1, question=LIZ + "\n\nSuppose a second study of 11 lizards found p = 0.21 for the slope. At α = 0.05, what do we do, and what does it mean?",
options="""A) Reject; bite force predicts territory size
B) Reject; we can't say for sure whether the null is true
C) Fail to reject; bite force has no effect
D) Fail to reject; we can't say for sure""", answer="D",
explanation="p > 0.05, so we fail to reject. With only 11 lizards we may lack power; this isn't evidence of no effect.",
why_wrong="""A) and B) p > α.
C) Failing to reject isn't proof.""", hint="Compare p with 0.05."),
V("ch19-quiz-09", 2, question=L + "\n\nThe slope's p-value is 0.039 and its 95% CI is 0.71 to 22.64. How are these consistent?",
options="""A) p < 0.05, and the CI excludes zero
B) p < 0.05, and the CI includes zero
C) p > 0.05, and the CI excludes zero
D) They aren't consistent with each other""", answer="A",
explanation="A two-tailed test at α = 0.05 rejects exactly when the 95% CI excludes the null value (0).",
why_wrong="""B) The CI excludes zero.
C) p < 0.05.
D) They agree.""", hint="Is 0 in the CI?"),

V("ch19-hw-01", 1, image="ch19-hw-sr.png", question=SRP + "\n\nMatch each interval to what it describes:\n\n1. Confidence interval (the grey band)\n2. Prediction interval",
options="""A) Where the true mean response at each x plausibly lies
B) Where new individual observations are expected to fall
C) Where 95% of the current data points fall
D) The range of x values in the data""", answer="1-A, 2-B",
explanation="A confidence band is for the mean response; a prediction interval adds individual scatter.", why_wrong="Mean vs individuals.", hint="Which one includes individual scatter?"),
V("ch19-hw-01", 2, image="ch19-hw-sr.png", question=SRP + "\n\nThe grey confidence band is narrowest near the middle of the petal areas and wider at the ends. Fill in the blanks: the band is narrowest near the (1) ____ of x, because the line's (2) ____ matters more far from that point.",
options="""A) mean
B) maximum
C) slope uncertainty
D) intercept""", answer="1-A, 2-C",
explanation="The line pivots around (mean x, mean y), so uncertainty in the slope matters more far from the mean.", why_wrong="The line always passes through the means.", hint="Where does the line pivot?"),

V("ch19-hw-02", 1, image="ch19-hw-sr.png", question=SRP + "\n\nWhy do most individual points fall OUTSIDE the grey 95% confidence band?",
options="""A) The band describes the mean, not individual RILs
B) The model is wrong and should be discarded
C) The band should contain 95% of the points
D) Most points are outliers in this dataset""", answer="A",
explanation="The confidence band is about the true mean response, not where individuals fall.",
why_wrong="""B) Points outside a confidence band are expected.
C) That's a prediction interval.
D) They're ordinary scatter.""", hint="Mean vs individuals."),
V("ch19-hw-02", 2, image="ch19-hw-sr.png", question=SRP + "\n\nWith more RILs (and similar data), what would happen to the grey 95% confidence band?",
options="""A) It would get narrower
B) It would get wider
C) It would stay the same
D) It would disappear""", answer="A",
explanation="More data shrink the standard errors of the intercept and slope, narrowing the band.",
why_wrong="""B) More data reduce uncertainty.
C) Uncertainty depends on n.
D) Some uncertainty always remains.""", hint="What does n do to SEs?"),

V("ch19-hw-03", 1, image="ch19-hw-sr-diag.png", question=SRP + "\n\nWhich assumptions CAN'T be evaluated from diagnostic plots? (Select all that apply.)",
options="""A) Independence
B) Unbiased data collection
C) Normality of residuals
D) Homoscedasticity (equal variance)""", answer="A, B",
explanation="Independence and bias depend on the study design; QQ and residual plots address normality and equal variance.",
why_wrong="C) and D) are what the plots show.", hint="What do the plots actually display?"),
V("ch19-hw-03", 2, image="ch19-hw-sr-diag.png", question=SRP + "\n\nWhat does the QQ plot of residuals suggest?",
options="""A) The residuals are skewed, not normally distributed
B) The residuals are perfectly normally distributed
C) The residuals are not independent of each other
D) The residuals have equal variance across x""", answer="A",
explanation="The points curve away from the line, as expected for proportions with many zeros.",
why_wrong="""B) They deviate.
C) and D) A QQ plot doesn't show these.""", hint="Do the points follow the line?"),

V("ch19-hw-04", 1, question=SRP + "\n\nThe residuals are non-normal and their variance isn't constant. Which is a reasonable way to check the conclusion?",
options="""A) Compare with a permutation test or bootstrap
B) Delete points until the residuals look normal
C) Report the result without mentioning the problems
D) Switch to a smaller α and keep the same model""", answer="A",
explanation="Resampling methods don't rely on normal, equal-variance residuals.",
why_wrong="""B) Deleting data to fit assumptions is wrong.
C) Be honest about violations.
D) α doesn't fix assumption violations.""", hint="Which methods don't need these assumptions?"),
V("ch19-hw-04", 2, question=SRP + "\n\nThe residuals are somewhat non-normal. Why is this less of a worry with 113 RILs than it would be with 10?",
options="""A) The CLT makes the slope's sampling distribution near normal
B) Large samples make the residuals themselves normal
C) Large samples make the model's assumptions unnecessary
D) It is not less of a worry with more data""", answer="A",
explanation="With large samples, estimates like the slope have roughly normal sampling distributions even when residuals aren't normal.",
why_wrong="""B) Residuals keep their shape.
C) Assumptions still matter (e.g. independence).
D) Large n helps.""", hint="Central limit theorem."),

V("ch19-hw-05", 1, question=SRP + "\n\n" + SR_SUM + "\n\nWhat is the correlation between petal area and proportion hybrid? Report it to two decimals.",
answer=r(0.92/((232**0.5)*(0.0651**0.5)),2), explanation="r = 0.92 / (√232 × √0.0651) = 0.92 / (15.23 × 0.255) = 0.24.", hint="cov / (sd_x × sd_y)."),
V("ch19-hw-05", 2, question=SRP + "\n\n" + SR_SUM + "\n\nHow much more hybrid seed (as a proportion) do we expect for a RIL with 10 mm² more petal area?",
answer=r(10*0.92/232,3), explanation="Slope = 0.92 / 232 = 0.0040 per mm², so 10 mm² → 0.040.", hint="Slope × 10."),

V("ch19-hw-06", 1, question=SRP + "\n\nThe intercept is -0.078 and the slope is 0.0040. What does the model predict for a RIL with a petal area of 60 mm²?",
options="""A) About 0.16
B) About -0.08
C) About 0.24
D) About 0.004""", answer="A",
explanation="-0.078 + 0.0040 × 60 = -0.078 + 0.24 = 0.162.",
why_wrong="""B) That's the intercept.
C) Forgets the intercept.
D) That's the slope.""", hint="Intercept + slope × 60."),
V("ch19-hw-06", 2, question=SRP + "\n\nPetal areas range from about 35 to 110 mm². Over what range of petal areas does the model predict a NEGATIVE proportion of hybrid seed (intercept -0.078, slope 0.0040)?",
options="""A) Below about 20 mm², outside our data
B) Below about 60 mm², within our data
C) Above about 110 mm², outside our data
D) It never predicts a negative proportion""", answer="A",
explanation="The line crosses zero at 0.078 / 0.0040 ≈ 19.5 mm², below the smallest petals observed.",
why_wrong="""B) At 60 mm² the prediction is 0.16.
C) Predictions increase with area.
D) The intercept is negative.""", hint="Solve -0.078 + 0.004 × x = 0."),

V("ch19-hw-07", 1, image="ch19-hw-sr-deviations.png", question=SRP + "\n\nEach plot shows 30 randomly chosen RILs, the regression line (blue) and the mean proportion hybrid (black). Which plot's lines would ALL shrink to zero if petal area had no relationship with hybrid seed (a flat line at the mean)?",
options="""A) Plot A
B) Plot B
C) Plot C""", answer="C",
explanation="Model deviations (line to mean) vanish when the line is the mean.",
why_wrong="""A) Points still scatter around the line.
B) Points still scatter around the mean.""", hint="Which lines connect the regression line to the mean?"),
V("ch19-hw-07", 2, image="ch19-hw-sr-deviations.png", question=SRP + "\n\nEach plot shows 30 randomly chosen RILs, the regression line (blue) and the mean proportion hybrid (black). Which plot shows the residuals?",
options="""A) Plot A
B) Plot B
C) Plot C""", answer="A",
explanation="Residuals are the vertical distances from each point to the regression line (Plot A).",
why_wrong="""B) Total deviations.
C) Model deviations.""", hint="Point to line."),

V("ch19-hw-08", 1, question=SRP + "\n\nSS model = 0.413, SS error = 6.88. What is SS total?",
options="""A) 7.29
B) 6.47
C) 0.06
D) 16.7""", answer="A",
explanation="SS total = 0.413 + 6.88 = 7.29.",
why_wrong="""B) Subtracts.
C) That's R².
D) That's 6.88 / 0.413.""", hint="SS total = SS model + SS error."),
V("ch19-hw-08", 2, question="Match each formula to its sum of squares in a regression:\n\n1. sum((y - .fitted)^2)\n2. sum((.fitted - mean(y))^2)\n3. sum((y - mean(y))^2)",
options="""A) Model
B) Error
C) Total""", answer="1-B, 2-A, 3-C",
explanation="Observation - prediction: error. Prediction - mean: model. Observation - mean: total.", why_wrong="Which two quantities are compared?", hint="Error uses the observations and predictions."),

V("ch19-hw-09", 1, question=SRP + "\n\nSS model = 0.413 and SS error = 6.88, with 1 and 111 df. What is the mean square error? Report it to four decimals.",
answer=r(6.88/111,4), explanation="MS error = 6.88 / 111 = 0.0620.", hint="SS error / df error."),
V("ch19-hw-09", 2, question="A regression on 52 points has SS model = 2.0 and SS error = 25.0. What is F?",
answer=r(2.0/(25/50),2), explanation="df = 1 and 50. MS error = 25 / 50 = 0.5. F = 2.0 / 0.5 = 4.", hint="F = MS model / MS error."),

V("ch19-hw-10", 1, question="A simple regression on 30 data points. Match each degree of freedom to its value:\n\n1. df1 (model)\n2. df2 (error)",
options="""A) 1
B) 2
C) 28
D) 29""", answer="1-A, 2-C",
explanation="Model df = 1 (one slope). Error df = 30 - 2 = 28.", why_wrong="Two parameters are estimated.", hint="n - 2 for error."),
V("ch19-hw-10", 2, question=SRP + "\n\nWhy is the error df 111 (not 112) in this regression on 113 RILs?",
options="""A) Two parameters, intercept and slope, are estimated
B) One data point was removed as an outlier
C) The model df is always subtracted twice
D) R uses n - 2 for every type of model""", answer="A",
explanation="Error df = n minus the number of estimated parameters (2).",
why_wrong="""B) No points were removed.
C) Not how df work.
D) It depends on the number of parameters.""", hint="Count the estimated parameters."),

V("ch19-hw-11", 1, question=SRP + "\n\nF = 6.66 on 1 and 111 df gives p = 0.011. Which statement is correct?",
options="""A) Petal area is associated with hybrid seed, but explains little variation
B) Petal area explains most of the variation in hybrid seed
C) Larger petals definitely cause more hybrid seed
D) There is a 1.1% chance there's no relationship""", answer="A",
explanation="p < 0.05 shows an association; R² = 0.057 shows it explains little of the variation.",
why_wrong="""B) R² is only 0.057.
C) Association isn't causation.
D) p isn't P(null).""", hint="Significance vs R²."),
V("ch19-hw-11", 2, question=SRP + "\n\nWhy is the regression's F (6.66) equal to the square of the slope's t?",
options="""A) With one predictor, F = t² and both test the same null
B) Coincidence; F and t are unrelated in regression
C) F always equals t² regardless of the model
D) Because R² is the square of the correlation""", answer="A",
explanation="With one predictor, the F test of the model and the t test of the slope test the same null (slope = 0), and F = t².",
why_wrong="""B) It's not a coincidence.
C) Only with one numerator df.
D) True, but not the reason.""", hint="How many predictors?"),

V("ch19-hw-12", 1, question=SRP + "\n\nSS model = 0.413 and SS total = 7.29. What proportion of the variance in proportion hybrid is NOT explained by petal area? Report it to three decimals.",
answer=r(1-0.413/7.29,3), explanation="1 - 0.413 / 7.29 = 1 - 0.057 = 0.943.", hint="1 - R²."),
V("ch19-hw-12", 2, question=SRP + "\n\nThe correlation between petal area and proportion hybrid is 0.24. What is R²? Report it to three decimals.",
answer=r(0.24**2,3), explanation="In simple regression, R² = r² = 0.24² = 0.058.", hint="Square the correlation."),

V("ch19-chimein-01", 1, question="Match each quantity to its units, for a regression of territory size (m²) on bite force (N):\n\n1. Slope\n2. Correlation\n3. Covariance",
options="""A) m² per N
B) No units
C) m² × N""", answer="1-A, 2-B, 3-C",
explanation="Slope: change in y per unit x. Correlation is unitless. Covariance has units of x times y.", why_wrong="Correlation is standardized.", hint="Which one is standardized?"),
V("ch19-chimein-01", 2, question="Match each description to the term it describes:\n\n1. The predicted value of y when x = 0\n2. The observed y minus the predicted y\n3. Bounded between -1 and 1",
options="""A) Intercept
B) Residual
C) Correlation
D) Slope""", answer="1-A, 2-B, 3-C",
explanation="Intercept: prediction at x = 0. Residual: observed - predicted. Correlation: between -1 and 1.", why_wrong="The slope isn't described.", hint="Which is bounded?"),

V("ch19-chimein-02", 1, question="Two regressions have the same R² but very different sample sizes (n = 10 and n = 1,000). Which will be the same in both?",
options="""A) R², the strength of association
B) F, the deviation from the null
C) p, the surprise under the null
D) All three would be the same""", answer="A",
explanation="F and p depend on sample size; R² measures strength of association.",
why_wrong="""B) and C) Change with n.
D) Only R² is the same.""", hint="Which ignores n?"),
V("ch19-chimein-02", 2, question="Which quantity tells you how SURPRISING the data would be if there were no relationship?",
options="""A) p
B) R²
C) The slope
D) The correlation""", answer="A",
explanation="p measures surprise under the null.",
why_wrong="B), C) and D) describe the relationship, not surprise.", hint="Probability under the null."),

V("ch19-chimein-03", 1, question="In linear models, Yᵢ = Ŷᵢ + eᵢ. Which equation is always true?",
options="""A) Σ(Yᵢ - Ȳ)² = Σ(Ŷᵢ - Ȳ)² + Σ(Yᵢ - Ŷᵢ)²
B) Σ(Yᵢ - Ŷᵢ)² = Σ(Ŷᵢ - Ȳ)² + Σ(Yᵢ - Ȳ)²
C) Σ(Ŷᵢ - Ȳ)² = Σ(Yᵢ - Ȳ)² + Σ(Yᵢ - Ŷᵢ)²
D) Σ(Yᵢ - Ȳ)² = Σ(Ŷᵢ - Ȳ)² × Σ(Yᵢ - Ŷᵢ)²""", answer="A",
explanation="SS total = SS model + SS error.",
why_wrong="Identify SS total first.", hint="Total = model + error."),
V("ch19-chimein-03", 2, question="Which expression is R²?",
options="""A) Σ(Ŷᵢ - Ȳ)² / Σ(Yᵢ - Ȳ)²
B) Σ(Yᵢ - Ŷᵢ)² / Σ(Yᵢ - Ȳ)²
C) Σ(Ŷᵢ - Ȳ)² / Σ(Yᵢ - Ŷᵢ)²
D) Σ(Yᵢ - Ȳ)² / Σ(Ŷᵢ - Ȳ)²""", answer="A",
explanation="R² = SS model / SS total.",
why_wrong="""B) That's 1 - R².
C) Model / error.
D) Upside down.""", hint="Model / total."),

V("ch19-chimein-04", 1, question="Two labs measure the same relationship. Lab A measures x precisely; Lab B measures x with a lot of random error. Compared with Lab A, Lab B's estimated slope will tend to be: (Select all that apply.)",
options="""A) Closer to zero
B) Farther from zero
C) Exactly the same on average
D) Associated with a weaker correlation""", answer="A, D",
explanation="Error in x biases both the slope and the correlation toward zero.",
why_wrong="""B) Bias is toward zero.
C) Error in x causes bias.""", hint="Regression dilution."),
V("ch19-chimein-04", 2, question="What is 'regression dilution'?",
options="""A) Error in x biases the estimated slope toward zero
B) Error in y biases the estimated slope toward zero
C) Adding predictors reduces each one's slope
D) Large samples shrink the slope toward zero""", answer="A",
explanation="Random error in the explanatory variable flattens the estimated slope.",
why_wrong="""B) Error in y doesn't bias the slope.
C) and D) Not what it means.""", hint="Which variable has the error?"),

V("ch19-chimein-05", 1, question="Two labs measure the same relationship. Lab A measures y precisely; Lab B measures y with a lot of random error. Compared with Lab A, Lab B will tend to have: (Select all that apply.)",
options="""A) A slope that is biased toward zero
B) A weaker correlation
C) A larger standard error for the slope
D) A slope that is biased away from zero""", answer="B, C",
explanation="Error in y adds scatter: the slope stays unbiased but less precise, and the correlation drops.",
why_wrong="""A) and D) Error in y doesn't bias the slope.""", hint="Scatter vs bias."),
V("ch19-chimein-05", 2, question="Random measurement error in Y does NOT: (Select all that apply.)",
options="""A) Bias the estimated slope
B) Reduce the estimated correlation
C) Increase the slope's standard error
D) Increase the residual variance""", answer="A",
explanation="Error in y leaves the slope unbiased but lowers the correlation and raises the SE and residual variance.",
why_wrong="B), C) and D) all happen.", hint="Which one stays unbiased?"),

V("ch19-book-01", 1, image="ch19-book-regression.png", question=GCV + "\n\nThe grey band is a 95% confidence interval. If we instead drew a 95% prediction interval, how would it compare?",
options="""A) Wider: it adds individual scatter
B) Narrower: it ignores uncertainty
C) The same: they're two names for one band
D) It would only cover the mean x value""", answer="A",
explanation="Prediction intervals include both uncertainty in the line and scatter of individuals.",
why_wrong="""B) It's wider.
C) They're different.
D) It spans all x.""", hint="Individuals vary more than means."),
V("ch19-book-01", 2, image="ch19-book-regression.png", question=GCV + "\n\nThe grey band is a 95% confidence interval. Which statement is correct?",
options="""A) 95% of bands made this way contain the true line
B) 95% of the 49 RILs fall inside the grey band
C) 95% of future RILs will fall in the grey band
D) The band shows where the residuals fall""", answer="A",
explanation="Like any CI, the 95% describes the procedure: intervals built this way usually capture the true mean response.",
why_wrong="""B) and C) That's about individuals.
D) Residuals aren't plotted.""", hint="CIs are about the mean."),

V("ch19-book-02", 1, image="ch19-book-regression.png", question=GCV + "\n\nBased on the blue line, roughly what proportion of hybrid seed is predicted for a RIL with 1 visit per session?",
options="""A) About 0.47
B) About 0.21
C) About 0.73
D) About 0.26""", answer="A",
explanation="0.208 + 0.262 × 1 = 0.47.",
why_wrong="""B) That's the intercept (0 visits).
C) That's at 2 visits.
D) That's the slope.""", hint="Intercept + slope × 1."),
V("ch19-book-02", 2, image="ch19-book-regression.png", question=GCV + "\n\nIs the slope of the blue line positive or negative, and what does that mean?",
options="""A) Positive: RILs with more visits set more hybrid seed
B) Negative: RILs with more visits set less hybrid seed
C) Zero: visits are unrelated to hybrid seed
D) Positive: more hybrid seed causes more visits""", answer="A",
explanation="The line rises with visits.",
why_wrong="""B) and C) The line rises.
D) Reverses cause and effect; regression shows association.""", hint="Does the line go up or down?"),

V("ch19-book-03", 1, question=GCV + "\n\n" + GC_SUM + "\n\nUsing the slope (0.26), what is the intercept of the regression of proportion hybrid on visits?",
options="""A) About 0.21
B) About 0.26
C) About 0.05
D) About 0.36""", answer="A",
explanation="a = mean(y) - b × mean(x) = 0.260 - 0.26 × 0.197 = 0.209.",
why_wrong="""B) That's mean y.
C) That's b × mean x.
D) That's the correlation.""", hint="The line passes through the means."),
V("ch19-book-03", 2, question=GCV + "\n\n" + GC_SUM + "\n\nWhat is R²?",
options="""A) About 0.13
B) About 0.36
C) About 0.26
D) About 0.60""", answer="A",
explanation="R² = r² = 0.36² = 0.13.",
why_wrong="""B) That's r.
C) That's the slope.
D) That's √0.36.""", hint="Square the correlation."),

V("ch19-book-04", 1, question=GCV + "\n\nThe slope is 0.262 (SE 0.098, p = 0.011). What null hypothesis does the slope's p-value test?",
options="""A) That proportion hybrid doesn't change with visits
B) That RILs with zero visits set no hybrid seed
C) That the mean proportion hybrid is zero
D) That visits explain all the variation""", answer="A",
explanation="The slope's p-value tests whether the true slope is zero: the biologically interesting question.",
why_wrong="""B) That's the intercept's test.
C) Not this test.
D) Not a null hypothesis we test.""", hint="Slope = 0."),
V("ch19-book-04", 2, question=GCV + "\n\nIn summary() output, which p-value is biologically interesting here?",
options="""A) The slope's: it asks whether hybrid seed changes with visits
B) The intercept's: it asks if hybrid seed is zero at zero visits
C) Both are equally interesting for the biological question
D) Neither; p-values are never interesting in a regression""", answer="A",
explanation="The slope tests the relationship we care about; the intercept tests a null nobody proposed.",
why_wrong="""B) Not a question anyone asked.
C) The intercept's test is irrelevant here.
D) The slope's test is useful.""", hint="What's the research question?"),

V("ch19-book-05", 1, question=GCV + "\n\nThe fitted model is prop_hybrid = 0.208 + 0.262 × visits. Predict the proportion hybrid seed for a RIL that received 1.5 visits per session.",
answer=r(0.208+0.262*1.5,3), explanation="0.208 + 0.262 × 1.5 = 0.601.", hint="Intercept + slope × 1.5."),
V("ch19-book-05", 2, question=GCV + "\n\nThe fitted model is prop_hybrid = 0.208 + 0.262 × visits. A RIL with 0.5 visits per session set 0.10 hybrid seed. What is its residual?",
answer=r(0.10-(0.208+0.262*0.5),3), explanation="Prediction = 0.339; residual = 0.10 - 0.339 = -0.239.", hint="Observed - predicted."),

V("ch19-book-06", 1, question=GCV + "\n\nVisits ranged from 0 to 2 per session. Which prediction is NOT an extrapolation?",
options="""A) For a RIL with 1.2 visits
B) For a RIL with 2.5 visits
C) For a RIL with 4 visits
D) For a RIL with -1 visits""", answer="A",
explanation="1.2 is within the observed range (0 to 2).",
why_wrong="B), C) and D) are outside it.", hint="Inside 0 to 2?"),
V("ch19-book-06", 2, question=GCV + "\n\nThe model predicts 1.26 for a RIL with 4 visits per session. What does this show?",
options="""A) A straight line can't hold far beyond the data
B) RILs with 4 visits set more seed than they make
C) The slope must have been estimated incorrectly
D) Nothing; the prediction is perfectly reasonable""", answer="A",
explanation="A proportion can't exceed 1. Extrapolating beyond 2 visits breaks the model.",
why_wrong="""B) That's impossible.
C) The slope is fine within the data.
D) It's impossible.""", hint="Can a proportion exceed 1?"),

V("ch19-book-07", 1, image="ch19-book-diagnostics.png", question=GCV + "\n\nThe diagnostic plots for lm(prop_hybrid ~ visits) are shown. Why are non-normal residuals and unequal variance common for proportion data like these?",
options="""A) Proportions are bounded (0 to 1) and often pile up at zero
B) Proportions are always perfectly normally distributed
C) Pollinator visits can't be measured at all precisely
D) Small sample sizes always produce perfect diagnostics""", answer="A",
explanation="Bounded responses with many zeros produce skewed residuals and variance that changes with the mean.",
why_wrong="""B) They often aren't.
C) Measurement precision isn't the main issue.
D) Not true.""", hint="What values can a proportion take?"),
V("ch19-book-07", 2, image="ch19-book-diagnostics.png", question=GCV + "\n\nThe diagnostic plots for lm(prop_hybrid ~ visits) are shown. Which plot is most useful for spotting unequal variance?",
options="""A) The scale-location plot
B) The QQ plot of residuals
C) A histogram of visits
D) Residuals vs leverage""", answer="A",
explanation="Unequal variance shows up as spread that changes with fitted values, in the scale-location (or residuals vs fitted) plot.",
why_wrong="""B) QQ plots address normality.
C) Not a diagnostic of residuals.
D) That's for influence.""", hint="Spread vs fitted values."),

V("ch19-book-08", 1, image="ch19-book-diagnostics.png", question=GCV + "\n\nUsing the labeled points in the diagnostic plots, which point has by far the highest leverage?",
options="""A) 13
B) 34
C) 9
D) 44""", answer="A",
explanation="Point 13 stands far to the right in the residuals vs leverage plot.",
why_wrong="""B) 34 has the largest residual, not leverage.
C) and D) Lower leverage.""", hint="Look at the x-axis of residuals vs leverage."),
V("ch19-book-08", 2, image="ch19-book-diagnostics.png", question=GCV + "\n\nUsing the labeled points in the diagnostic plots, what makes a point influential?",
options="""A) A combination of high leverage and a large residual
B) A large residual alone, wherever its x value is
C) A small residual combined with low leverage
D) Being the first point in the dataset""", answer="A",
explanation="Influence (e.g. Cook's distance) depends on both leverage (unusual x) and the residual.",
why_wrong="""B) A large residual near mean x has little pull.
C) That's a typical point.
D) Order doesn't matter.""", hint="Leverage × residual."),

V("ch19-book-09", 1, question="After removing an influential point, the slope drops from 0.26 to 0.05 and is no longer significant. What should you report?",
options="""A) Both analyses, noting conclusions depend on that point
B) Only the original analysis, since it was significant
C) Only the new analysis, since the point was influential
D) Neither; the data are unusable and must be discarded""", answer="A",
explanation="Transparency: say that the conclusion hinges on one point.",
why_wrong="""B) and C) Hiding either is misleading.
D) The data still tell us something.""", hint="Sensitivity analysis."),
V("ch19-book-09", 2, question="Which is a legitimate reason to remove a data point from an analysis?",
options="""A) It was a documented recording or measurement error
B) It makes the p-value larger than you would like
C) It has the largest residual in the regression
D) It falls outside the confidence band of the line""", answer="A",
explanation="Points can be removed for documented errors, not because they're inconvenient.",
why_wrong="""B) That's p-hacking.
C) and D) Large residuals are part of the data.""", hint="Errors vs inconvenience."),

V("ch19-book-10", 1, image="ch19-book-deviations.png", question=GCV + "\n\nEach panel shows the RILs, the regression line (blue) and the mean proportion hybrid (black). Which panel's deviations, squared and summed, give SS error?",
options="""A) Panel A
B) Panel B
C) Panel C""", answer="B",
explanation="Panel B shows each point to the line (residuals).",
why_wrong="""A) Total.
C) Model.""", hint="Point to line."),
V("ch19-book-10", 2, image="ch19-book-deviations.png", question=GCV + "\n\nEach panel shows the RILs, the regression line (blue) and the mean proportion hybrid (black). Which panel's deviations are largest for RILs with the most visits (far right)?",
options="""A) Panel C, since the line is farthest from the mean there
B) Panel B, since residuals always grow with x
C) None; model deviations are the same for every RIL
D) Panel A, since total deviations never vary""", answer="A",
explanation="Model deviations (line minus mean) grow the farther x is from its mean.",
why_wrong="""B) Residuals needn't grow with x.
C) In regression they vary with x.
D) Total deviations vary point to point.""", hint="Where is the line farthest from the mean?"),

V("ch19-book-11", 1, question=GCV + "\n\nSS model = 0.493 and SS total = 3.76. What is SS error, and what is R²?",
options="""A) 3.26 and 0.13
B) 4.25 and 0.13
C) 3.26 and 0.87
D) 0.493 and 0.15""", answer="A",
explanation="SS error = 3.76 - 0.493 = 3.27 ≈ 3.26. R² = 0.493 / 3.76 = 0.13.",
why_wrong="""B) Adds instead of subtracts.
C) 0.87 is 1 - R².
D) Wrong on both.""", hint="Total = model + error."),
V("ch19-book-11", 2, question=GCV + "\n\nlm(prop_hybrid ~ visits, data1) |> augment() |>\n  summarise(ssa = sum((prop_hybrid - .fitted)^2),\n            ssb = sum((.fitted - mean(prop_hybrid))^2),\n            ssc = sum((prop_hybrid - mean(prop_hybrid))^2))\n\nssa = 3.26; ssb = 0.493; ssc = 3.76\n\nWhich of these is the share of variation NOT explained by visits?",
options="""A) ssa / ssc = 0.87
B) ssb / ssc = 0.13
C) ssb / ssa = 0.15
D) ssc / ssa = 1.15""", answer="A",
explanation="SS error / SS total = 3.26 / 3.76 = 0.87 = 1 - R².",
why_wrong="""B) That's R².
C) and D) Not meaningful shares.""", hint="Error / total."),

V("ch19-book-12", 1, question=GCV + "\n\nWhat is the alternative hypothesis (two-tailed) for testing this regression?",
options="""A) The true slope is not zero
B) The true slope is positive
C) The true intercept is not zero
D) The observed slope is not zero""", answer="A",
explanation="Two-tailed: the response changes with visits in either direction.",
why_wrong="""B) One-tailed.
C) Wrong parameter.
D) Hypotheses are about true values.""", hint="Two-tailed, about the slope."),
V("ch19-book-12", 2, question=GCV + "\n\nIf the null hypothesis (slope = 0) were true, what would the regression line look like in the population?",
options="""A) Flat, at the mean proportion hybrid
B) Passing through the origin (0, 0)
C) Rising steeply with visits
D) Vertical, at mean visits""", answer="A",
explanation="Slope = 0 means predictions don't change with visits: a flat line at the mean.",
why_wrong="""B) That's intercept = 0.
C) That's a positive slope.
D) Not a regression line.""", hint="What does slope = 0 mean?"),

V("ch19-book-13", 1, question=GCV + "\n\nSS model = 0.493 and SS error = 3.26, with N = 49. What is the mean square error? Report it to four decimals.",
answer=r(3.26/47,4), explanation="MS error = 3.26 / 47 = 0.0694.", hint="SS error / (N - 2)."),
V("ch19-book-13", 2, question="A regression on 22 points has SS model = 5.0 and SS error = 40.0. What is F?",
answer=r(5/(40/20),2), explanation="df = 1 and 20. MS error = 40 / 20 = 2. F = 5 / 2 = 2.5.", hint="F = MS model / MS error."),

V("ch19-book-14", 1, question=GCV + "\n\nF = 7.1 on 1 and 47 df gives p = 0.011, and R² = 0.13. Which statement is correct?",
options="""A) The association is significant but explains little variation
B) Visits explain most of the variation in hybrid seed
C) Visits definitely cause hybrid seed production
D) There's no association between visits and hybrid seed""", answer="A",
explanation="p < 0.05 indicates an association; R² = 0.13 means visits explain about 13% of the variation.",
why_wrong="""B) R² is only 0.13.
C) Association isn't causation.
D) p < 0.05.""", hint="Significance vs R²."),
V("ch19-book-14", 2, question=GCV + "\n\nF = 7.1 on 1 and 47 df gives p = 0.011. Why can't we conclude that pollinator visits CAUSE hybrid seed production?",
options="""A) These are observational data; other traits may drive both
B) Because the p-value isn't below 0.001
C) Because R² is greater than zero
D) We can; a significant slope demonstrates causation""", answer="A",
explanation="RILs that attract more visits may differ in other traits (e.g. flower size, timing) that also affect hybridization.",
why_wrong="""B) Smaller p wouldn't prove causation.
C) Irrelevant.
D) Significance doesn't show causation.""", hint="Observational vs experimental."),
]
