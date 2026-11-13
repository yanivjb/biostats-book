# Applied Biostats tutor: question bank, chapter 22 (Exam 2, chapters 13–21, plus an Exam 1 review as chapter 0)

Knowledge file for the course tutor. Each question has an ID, its concepts, the question, options, the answer, an explanation, why each wrong option is wrong, and a hint. Fields marked **tutor only** must never be shown to the student before they have answered.

- **Course originals** come from the instructor's homework, quizzes, Chime Ins and book.
- **AI-written versions** test the same idea with a new scenario or numbers. Their ID ends in -v1 or -v2 and names the original.
- 1047 questions in all. 145 use a figure and are marked **Figure question (website only)**: students practice those on the study-guide website, where the figure is shown. Use one only when a student brings it to you; its figure link is included.

## Chapters and concepts

- **Chapter 0: Key concepts from Exam 1 (review)** — Samples, populations & bias; Sampling distribution, SD & SE; Bootstrap & confidence intervals; Hypotheses & p-values; Errors & power; Permutation; Causation & study design
- **Chapter 13: Linear Models** — Statistical vs scientific models; Categorical predictors & reference levels; Coefficients & predictions; Residuals & model fit; Regression from summaries
- **Chapter 14: Normal distribution** — The normal & Z; Density & R's _norm functions; Sampling distribution & CLT; Z tests & p-values; Normality & transformations
- **Chapter 15: The t distribution** — t vs z; The t statistic & SE; p-values & NHST; Effect size & CIs; Paired designs
- **Chapter 16: Comparing two means** — Effect size vs significance; Two-sample t & equal variance; Confidence intervals; Interpreting tests; p-hacking & HARKing
- **Chapter 17: F this!** — Sums of squares & deviations; F & the ANOVA table; Hypotheses & p-values; Effect size & R²; SD vs SE
- **Chapter 18: >2 Groups** — Multiple testing & post-hoc tests; ANOVA calculations; Assumptions & diagnostics; ANOVA in R; SD vs SE
- **Chapter 19: Regression** — Slopes, intercepts & predictions; Confidence & prediction intervals; Sums of squares, F & R²; Assumptions & diagnostics; Measurement error & causation
- **Chapter 20: Multiple Predictors** — Coefficients & predictions; Adjusting vs controlling; Type I vs Type II sums of squares; Partial R² & multicollinearity; Plots & diagnostics; Adjusted means
- **Chapter 21: Interactions** — What interactions mean; Predictions & coefficients; Main effects with interactions; Visualizing interactions; Testing interactions
- **Chapter 22: Model Evaluation** — Is my model any good?; Diagnostics & robustness; Penalizing complexity; Cross-validation; Biology & study design

## Chapter 22: Model Evaluation

### ch22-hw-01
- **Kind:** Course original
- **Concepts:** Is my model any good?
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch22-anscombe.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch22-anscombe.png)
- **Question:**

Anscombe's quartet is a famous fake dataset: four groups of 11 points, each fit with its own linear model, lm(y ~ x). The plot shows each group with its regression line.

What do you notice?

- **Options:**

  A) All four groups show the same straight-line pattern, with similar scatter around the line
  B) The four groups have very different x ranges, so their regression lines can't be compared
  C) The groups look very different (a line, a curve, an outlier, one extreme point) despite similar lines
  D) Only group 1 has a clear relationship; groups 2-4 show no association between x and y

- **Answer (tutor only):** C
- **Explanation (tutor only):** The four lines are essentially identical (intercept 3, slope 0.5), but the data are not: group 1 is ordinary linear scatter, group 2 is a smooth curve, group 3 is a near-perfect line plus one outlier, and in group 4 a single point at x = 19 creates the whole slope.
- **Why the wrong options are wrong (tutor only):**
  A) Only group 1 looks like ordinary scatter around a line.
  B) Groups 1-3 share the same x values and group 4's fall in the same range. The lines are nearly identical.
  D) Groups 2 and 3 have strong relationships: a curve, and a near-perfect line plus one outlier.
- **Hint:** Ignore the lines and look at the points. Does each group follow the same pattern?

### ch22-hw-01-v1
- **Kind:** AI-written version of ch22-hw-01
- **Concepts:** Is my model any good?
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch22-anscombe.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch22-anscombe.png)
- **Question:**

Anscombe's quartet is a famous fake dataset: four groups of 11 points, each fit with its own linear model, lm(y ~ x). The plot shows each group with its regression line.

Which group's straight line misses a curved relationship?

- **Options:**

  A) Group 2
  B) Group 1
  C) Group 4
  D) Group 3

- **Answer (tutor only):** A
- **Explanation (tutor only):** Group 2's points rise and then fall in a smooth arc. A straight line can't follow that shape, even though its slope and R² match the other groups.
- **Why the wrong options are wrong (tutor only):**
  B) Group 1's points scatter evenly around the line.
  C) Group 4's slope comes from one extreme point, not a curve.
  D) Group 3 is a near-perfect line with one outlier.
- **Hint:** Look for points that bend rather than scatter.

### ch22-hw-01-v2
- **Kind:** AI-written version of ch22-hw-01
- **Concepts:** Is my model any good?
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch22-anscombe.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch22-anscombe.png)
- **Question:**

Anscombe's quartet is a famous fake dataset: four groups of 11 points, each fit with its own linear model, lm(y ~ x). The plot shows each group with its regression line. All four lines have intercept 3, slope 0.5, R² = 0.67 and p = 0.002.

What's the main lesson of this plot?

- **Options:**

  A) With only 11 points, the four datasets can't really differ from each other
  B) Identical model summaries can come from very different patterns, so always plot the data
  C) A p-value of 0.002 guarantees that a straight line describes the data well
  D) R² = 0.67 means two-thirds of the points fall exactly on the line

- **Answer (tutor only):** B
- **Explanation (tutor only):** Same coefficients, R² and p-value, but a line, a curve, an outlier and a single extreme point. Summary numbers can't tell these apart; a plot can.
- **Why the wrong options are wrong (tutor only):**
  A) The plots show they differ a lot.
  C) Group 2 has the same p-value but is clearly curved.
  D) R² is the proportion of variance explained, not the share of points on the line.
- **Hint:** What do the summary numbers miss?

### ch22-hw-02
- **Kind:** Course original
- **Concepts:** Is my model any good?
- **Type:** MC
- **Question:**

Anscombe's quartet is a famous fake dataset: four groups of 11 points, each fit with its own linear model, lm(y ~ x).

anova(lm(y ~ x)) for each group:

group 1    Df  Sum Sq  F value  Pr(>F)
x           1  27.51    17.99   0.00217
Residuals   9  13.76

group 2    Df  Sum Sq  F value  Pr(>F)
x           1  27.50    17.97   0.00218
Residuals   9  13.78

group 3    Df  Sum Sq  F value  Pr(>F)
x           1  27.47    17.97   0.00218
Residuals   9  13.76

group 4    Df  Sum Sq  F value  Pr(>F)
x           1  27.49    18.00   0.00216
Residuals   9  13.74

What do you notice?

- **Options:**

  A) Group 1 fits best: its F is much larger and its p-value much smaller than the others'
  B) All four datasets yield remarkably similar ANOVA tables (sums of squares, F and p)
  C) The tables show y is independent of x in all four groups, since every p-value is large
  D) Groups 2 and 4 have much larger error sums of squares, so their models fit worse

- **Answer (tutor only):** B
- **Explanation (tutor only):** Every group has a model sum of squares of about 27.5, an error sum of squares of about 13.8, F ≈ 18 and p ≈ 0.002. Yet the plots of these groups look completely different, so an ANOVA table alone can't tell you whether a model describes the data well.
- **Why the wrong options are wrong (tutor only):**
  A) The F values (17.97 to 18.00) and p-values (0.00216 to 0.00218) are essentially identical.
  C) Every p is about 0.002, so we reject the null of no association in all four groups.
  D) The error sums of squares are all about 13.8.
- **Hint:** Compare the numbers across the four tables.

### ch22-hw-02-v1
- **Kind:** AI-written version of ch22-hw-02
- **Concepts:** Is my model any good?
- **Type:** MC
- **Question:**

Anscombe's quartet is a famous fake dataset: four groups of 11 points, each fit with its own linear model, lm(y ~ x).

anova(lm(y ~ x)) for each group:

group 1    Df  Sum Sq  F value  Pr(>F)
x           1  27.51    17.99   0.00217
Residuals   9  13.76

group 2    Df  Sum Sq  F value  Pr(>F)
x           1  27.50    17.97   0.00218
Residuals   9  13.78

group 3    Df  Sum Sq  F value  Pr(>F)
x           1  27.47    17.97   0.00218
Residuals   9  13.76

group 4    Df  Sum Sq  F value  Pr(>F)
x           1  27.49    18.00   0.00216
Residuals   9  13.74

Based only on these ANOVA tables, what can you conclude?

- **Options:**

  A) In every group, the data would be unlikely if x and y were unrelated
  B) A straight line is a good description of all four groups
  C) Group 4 fits best because it has the largest F
  D) None of the groups shows a significant association

- **Answer (tutor only):** A
- **Explanation (tutor only):** All four p-values are about 0.002, so in every group we reject the null of no association. But the tables can't tell you whether a straight line is the right shape; the plots show it isn't for groups 2-4.
- **Why the wrong options are wrong (tutor only):**
  B) A small p-value says the null is unlikely, not that the model is adequate.
  C) F ranges from 17.97 to 18.00, a meaningless difference.
  D) Every p-value is about 0.002.
- **Hint:** What does a small p-value tell you, and what doesn't it?

### ch22-hw-02-v2
- **Kind:** AI-written version of ch22-hw-02
- **Concepts:** Is my model any good?
- **Type:** MC
- **Question:**

Anscombe's quartet is a famous fake dataset: four groups of 11 points, each fit with its own linear model, lm(y ~ x).

anova(lm(y ~ x)) for each group:

group 1    Df  Sum Sq  F value  Pr(>F)
x           1  27.51    17.99   0.00217
Residuals   9  13.76

group 2    Df  Sum Sq  F value  Pr(>F)
x           1  27.50    17.97   0.00218
Residuals   9  13.78

group 3    Df  Sum Sq  F value  Pr(>F)
x           1  27.47    17.97   0.00218
Residuals   9  13.76

group 4    Df  Sum Sq  F value  Pr(>F)
x           1  27.49    18.00   0.00216
Residuals   9  13.74

The four groups look completely different when plotted. Why can't these tables tell them apart?

- **Options:**

  A) The tables are wrong: R must have fit the same data four times
  B) The tables summarize total variation explained, not the shape of the pattern or which points drive it
  C) The groups have different x values, so the tables can't be compared
  D) ANOVA tables only work when there are more than 11 data points

- **Answer (tutor only):** B
- **Explanation (tutor only):** Sums of squares, F and p summarize how much variation the line explains overall. A curve, an outlier or one extreme point can produce exactly the same totals.
- **Why the wrong options are wrong (tutor only):**
  A) The data really are different; Anscombe built them to have matching summaries.
  C) Tables from different data can be compared, and here they match.
  D) ANOVA works with 11 points.
- **Hint:** What information does a sum of squares throw away?

### ch22-hw-03
- **Kind:** Course original
- **Concepts:** Diagnostics & robustness
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch22-anscombe-diag.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch22-anscombe-diag.png)
- **Question:**

Anscombe's quartet is a famous fake dataset: four groups of 11 points, each fit with its own linear model, lm(y ~ x). The figure shows two diagnostic plots for each group's model: residuals vs fitted values (top) and residuals vs leverage (bottom).

Match each group to what its diagnostic plots show.

1. Group 1
2. Group 2
3. Group 3
4. Group 4

- **Options:**

  A) No obvious problems
  B) One point has a large residual
  C) The residuals follow a curve
  D) One point has a lot of leverage

- **Answer (tutor only):** 1-A, 2-C, 3-B, 4-D
- **Explanation (tutor only):** Group 1: residuals scatter evenly around zero. Group 2: the residuals form an upside-down U, negative at both ends and positive in the middle, so the relationship is curved. Group 3: one point sits far above the line the others follow; its x value is ordinary, so its leverage isn't high, but its residual (about 3 standard deviations) is the biggest in any group. Group 4: the point at x = 19 is far from the other x values (all 8), so its leverage is 1 and the line passes right through it with a residual of zero. On its own, that point creates the whole slope.
- **Why the wrong options are wrong (tutor only):**
  Group 3 vs group 4 is the common mix-up. A large residual means a point is far from the line (group 3); high leverage means a point is far out on x (group 4), and the line is pulled right through it.
- **Hint:** In the bottom row, which group has a point far to the right? In the top row, which has a point far from zero?

### ch22-hw-03-v1
- **Kind:** AI-written version of ch22-hw-03
- **Concepts:** Diagnostics & robustness
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch22-anscombe-diag.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch22-anscombe-diag.png)
- **Question:**

Anscombe's quartet is a famous fake dataset: four groups of 11 points, each fit with its own linear model, lm(y ~ x). The figure shows residuals vs fitted values (top) and residuals vs leverage (bottom) for each group.

Match each problem to the plot that reveals it best.

1. A curved relationship
2. A high-leverage point
3. A point with a large residual

- **Options:**

  A) Residuals vs fitted: a point far from zero
  B) Residuals vs fitted: a U-shaped pattern
  C) Residuals vs leverage: a point far to the right

- **Answer (tutor only):** 1-B, 2-C, 3-A
- **Explanation (tutor only):** A curve shows up as a U (or upside-down U) in residuals vs fitted (group 2). A point with a big residual sits far from zero in residuals vs fitted (group 3). Leverage is on the x-axis of the bottom plots, so a high-leverage point sits far to the right (group 4).
- **Why the wrong options are wrong (tutor only):**
  Leverage is about x values, not distance from the line, so it can't show up as a large residual.
- **Hint:** Which axis shows leverage?

### ch22-hw-03-v2
- **Kind:** AI-written version of ch22-hw-03
- **Concepts:** Diagnostics & robustness
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch22-anscombe-diag.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch22-anscombe-diag.png)
- **Question:**

Anscombe's quartet is a famous fake dataset: four groups of 11 points, each fit with its own linear model, lm(y ~ x). The figure shows residuals vs fitted values (top) and residuals vs leverage (bottom) for each group.

In group 4, the point at x = 19 has a residual of exactly zero. Why isn't that reassuring?

- **Options:**

  A) A residual of zero means the point was measured incorrectly
  B) It is reassuring: a point on the line fits the model perfectly
  C) Zero residuals only occur when the relationship is curved
  D) Its leverage is 1, so the line is forced through it: that one point alone sets the slope

- **Answer (tutor only):** D
- **Explanation (tutor only):** With all other x values at 8, the x = 19 point has leverage 1. The line has to pass through it, so its residual is zero by construction, not because the model is good. Remove it and there's no slope at all.
- **Why the wrong options are wrong (tutor only):**
  A) Zero residual says nothing about measurement error.
  B) The fit is perfect only because the point decides where the line goes.
  C) Group 4 isn't curved; zero residual comes from leverage.
- **Hint:** Could the line have missed that point?

### ch22-hw-04
- **Kind:** Course original
- **Concepts:** Cross-validation
- **Type:** MC
- **Question:**

Anscombe's quartet is a famous fake dataset: four groups of 11 points, each fit with its own linear model, lm(y ~ x).

Leave-one-out cross-validation of lm(y ~ x):

group   RMSE
1       1.37
2       1.48
3       1.47
4       2.07

On which group does the linear model predict held-out data best?

- **Options:**

  A) Group 3
  B) Group 1
  C) Group 4
  D) They're all about equal, since their ANOVA tables are the same

- **Answer (tutor only):** B
- **Explanation (tutor only):** Lower cross-validation RMSE means smaller prediction errors for points the model didn't see. Group 1 has the lowest (1.37). Group 4 is worst (2.07): when its x = 19 point is held out, the other ten points all have x = 8, so there's no slope to predict it with.
- **Why the wrong options are wrong (tutor only):**
  A) Group 3 is close (1.47) but worse: its outlier is badly predicted when it's held out.
  C) Group 4 is the worst by far.
  D) This is the trap. Identical ANOVA tables don't mean identical predictive performance.
- **Hint:** RMSE is the typical size of a prediction error. Do you want it big or small?

### ch22-hw-04-v1
- **Kind:** AI-written version of ch22-hw-04
- **Concepts:** Cross-validation
- **Type:** MC
- **Question:**

Anscombe's quartet is a famous fake dataset: four groups of 11 points, each fit with its own linear model, lm(y ~ x).

Leave-one-out cross-validation RMSE:

group   intercept-only   lm(y ~ x)
1       2.13             1.37
2       2.13             1.48
3       2.13             1.47
4       2.13             2.07

For which group does the linear model barely beat the intercept-only model?

- **Options:**

  A) Group 1
  B) None: the linear model is much better for all four
  C) Group 4
  D) Group 2

- **Answer (tutor only):** C
- **Explanation (tutor only):** Group 4's linear model only gets from 2.13 to 2.07, even though its p-value is 0.002. Its slope comes from one point; when that point is held out, the remaining points (all at x = 8) can't predict it.
- **Why the wrong options are wrong (tutor only):**
  A) Group 1 drops from 2.13 to 1.37.
  B) Group 4's improvement is tiny.
  D) Group 2 drops to 1.48.
- **Hint:** Compare each pair of RMSE values.

### ch22-hw-04-v2
- **Kind:** AI-written version of ch22-hw-04
- **Concepts:** Cross-validation
- **Type:** MC
- **Question:**

Anscombe's quartet is a famous fake dataset: four groups of 11 points, each fit with its own linear model, lm(y ~ x).

Leave-one-out cross-validation of lm(y ~ x):

group   RMSE
1       1.37
2       1.48
3       1.47
4       2.07

Which group's model predicts held-out data worst?

- **Options:**

  A) Group 4
  B) Group 3
  C) Group 2
  D) Group 1

- **Answer (tutor only):** A
- **Explanation (tutor only):** Group 4 has the highest cross-validation RMSE (2.07). When its x = 19 point is left out, the other ten points all have x = 8, so the model can't estimate a slope to predict it.
- **Why the wrong options are wrong (tutor only):**
  B) Group 3's RMSE is 1.47.
  C) Group 2's RMSE is 1.48.
  D) Group 1 predicts best (1.37).
- **Hint:** Larger RMSE means bigger prediction errors.

### ch22-hw-05
- **Kind:** Course original
- **Concepts:** Cross-validation
- **Type:** MC
- **Question:**

Above, we used leave-one-out cross-validation (LOOCV) to evaluate our models. Leave-one-out cross-validation works by ____

- **Options:**

  A) fitting the model to all the data, then measuring how far each point falls from the line
  B) fitting the model to a random half of the data, then predicting the other half
  C) removing each data point in turn, fitting the model to the rest, and predicting the removed point
  D) removing outliers one at a time until the model's residuals look normally distributed

- **Answer (tutor only):** C
- **Explanation (tutor only):** Each point is set aside in turn, the model is fit to the remaining points, and the left-out point is predicted as if it were new data. The prediction errors are then summarized (e.g. as RMSE).
- **Why the wrong options are wrong (tutor only):**
  A) Those are ordinary residuals. Each point helped fit the line it's measured against, so the error looks smaller than it really is.
  B) That's a single train/test split. LOOCV leaves out one point at a time, and every point gets a turn.
  D) LOOCV never deletes data for good. Each point is set aside only while it's being predicted, then put back.
- **Hint:** What does 'leave one out' leave out, and what happens to it?

### ch22-hw-05-v1
- **Kind:** AI-written version of ch22-hw-05
- **Concepts:** Cross-validation
- **Type:** MC
- **Question:**

Why is a model's leave-one-out cross-validation (LOOCV) RMSE usually larger than the RMSE of its ordinary residuals?

- **Options:**

  A) LOOCV only works for curved models, so straight lines fit worse
  B) LOOCV uses fewer data points, so its arithmetic is less precise
  C) Each point is predicted by a model that never saw it, so overfitting is exposed
  D) LOOCV squares the errors twice, inflating them

- **Answer (tutor only):** C
- **Explanation (tutor only):** A model always fits the data it was built from better than new data. LOOCV mimics new data by predicting each point from a model fit without it, so it shows how much of the fit was really fitting noise.
- **Why the wrong options are wrong (tutor only):**
  A) LOOCV works for any model.
  B) Precision of arithmetic isn't the issue.
  D) Errors are squared once, as for ordinary RMSE.
- **Hint:** Did the point being predicted help fit the model?

### ch22-hw-05-v2
- **Kind:** AI-written version of ch22-hw-05
- **Concepts:** Cross-validation
- **Type:** MC
- **Question:**

In leave-one-out cross-validation with 11 data points, how many times is the model fit?

- **Options:**

  A) Once, using all 11 points
  B) 10 times, because one point is always left out
  C) 11 times, each time leaving out a different point
  D) Twice: once to half the data, once to the other half

- **Answer (tutor only):** C
- **Explanation (tutor only):** Each of the 11 points takes a turn being left out, so the model is fit 11 times, each time to the other 10 points.
- **Why the wrong options are wrong (tutor only):**
  A) Fitting once to all the data gives ordinary residuals.
  B) Every point gets a turn, so there are as many fits as points.
  D) That's a two-fold split.
- **Hint:** Every point gets a turn.

### ch22-hw-06
- **Kind:** Course original
- **Concepts:** Penalizing complexity
- **Type:** MC
- **Question:**

To ask what predicts gene flow between Clarkia subspecies, we estimated the admixture proportion in six C. xantiana xantiana populations and compared two models.

Model                                             R²      Error df
1: admixture_prop ~ precip_spring_var             0.9249  4
2: admixture_prop ~ precip_spring_var + northing  0.9250  3

Adjusted R² = 1 − (1 − R²)(n − 1) / df_error, where n is the number of populations. Which statement is correct?

- **Options:**

  A) Model 2 is better: both its R² and its adjusted R² are higher
  B) The models are equally good, since their R² values are almost identical
  C) Model 1 has the higher adjusted R² (0.906 vs 0.875): northing doesn't explain enough to justify an extra parameter
  D) Adjusted R² can't be compared between models with different numbers of predictors

- **Answer (tutor only):** C
- **Explanation (tutor only):** Model 1: 1 − (0.0751 × 5)/4 = 0.906. Model 2: 1 − (0.0750 × 5)/3 = 0.875. R² can only rise when you add a predictor, so its 0.0001 increase means nothing. Adjusted R² charges for the lost error degree of freedom, which is costly with only six populations, and northing doesn't earn it back.
- **Why the wrong options are wrong (tutor only):**
  A) Model 2's R² is higher, but its adjusted R² is lower.
  B) Nearly equal R² with one more parameter means the extra parameter isn't pulling its weight.
  D) Comparing models with different numbers of predictors is exactly what adjusted R² is for.
- **Hint:** Plug each model into the formula with n = 6.

### ch22-hw-06-v1
- **Kind:** AI-written version of ch22-hw-06
- **Concepts:** Penalizing complexity
- **Type:** numeric
- **Question:**

To ask what predicts gene flow between Clarkia subspecies, we estimated the admixture proportion in six C. xantiana xantiana populations and compared two models.

Model 1: admixture_prop ~ precip_spring_var has R² = 0.9249 and 4 error df.

Adjusted R² = 1 − (1 − R²)(n − 1) / df_error, where n = 6 populations. What is Model 1's adjusted R²? Round to three decimal places.

- **Answer (tutor only):** 0.906
- **Explanation (tutor only):** 1 − (1 − 0.9249) × 5 / 4 = 1 − 0.0751 × 1.25 = 0.906.
- **Hint:** n − 1 = 5.

### ch22-hw-06-v2
- **Kind:** AI-written version of ch22-hw-06
- **Concepts:** Penalizing complexity
- **Type:** MC
- **Question:**

To ask what predicts gene flow between Clarkia subspecies, we estimated the admixture proportion in six C. xantiana xantiana populations and compared two models.

Model                                             log-likelihood   AIC
1: admixture_prop ~ precip_spring_var             11.71            -17.42
2: admixture_prop ~ precip_spring_var + northing  11.71            -15.43

The two models have the same log-likelihood. Why is Model 2's AIC exactly 2 units higher?

- **Options:**

  A) Northing has a negative effect on admixture
  B) Model 2 fits the data worse than Model 1
  C) AIC adds 2 for each parameter, and Model 2 has one more parameter with no gain in fit
  D) AIC doubles whenever a predictor is added

- **Answer (tutor only):** C
- **Explanation (tutor only):** AIC = 2k − 2 ln(L). The log-likelihoods are equal, and Model 2 has one more parameter (k + 1), so its AIC is exactly 2 higher. AIC prefers Model 1.
- **Why the wrong options are wrong (tutor only):**
  A) AIC doesn't depend on the sign of an effect.
  B) The log-likelihoods are equal, so the fits are the same.
  D) AIC rises by 2 per parameter, not by doubling.
- **Hint:** AIC = 2k − 2 ln(L).

### ch22-hw-07
- **Kind:** Course original
- **Concepts:** Penalizing complexity
- **Type:** select-all
- **Question:**

Adding another predictor to a linear model will ALWAYS: (Select all that apply.)

- **Options:**

  A) Increase (or not change) R²
  B) Increase adjusted R²
  C) Decrease LOOCV RMSE
  D) Decrease (or not change) the error sum of squares
  E) Make the model better

- **Answer (tutor only):** A, D
- **Explanation (tutor only):** The fit to the data used to build the model can never get worse, so R² can't fall and the error sum of squares can't rise. Adjusted R² and LOOCV RMSE can get worse: adding northing to the Clarkia admixture model dropped adjusted R² from 0.906 to 0.875 and raised LOOCV RMSE from 0.049 to 0.136.
- **Why the wrong options are wrong (tutor only):**
  B) Adjusted R² penalizes extra parameters and can fall.
  C) An extra predictor can fit noise and predict new data worse.
  E) 'Better' depends on the goal; extra predictors can make a model worse at predicting new data.
- **Hint:** Which of these only measure fit to the data the model was built from?

### ch22-hw-07-v1
- **Kind:** AI-written version of ch22-hw-07
- **Concepts:** Penalizing complexity
- **Type:** select-all
- **Question:**

A student adds a fifth predictor to a model of seed set, and R² goes from 0.40 to 0.41. Which conclusions are justified? (Select all that apply.)

- **Options:**

  A) Adjusted R² or cross-validation would help judge whether it's worth including
  B) The model will now predict new plants better
  C) R² was guaranteed not to fall, so the rise alone doesn't show the predictor is useful
  D) The new predictor must reflect a real biological process

- **Answer (tutor only):** A, C
- **Explanation (tutor only):** R² can't go down when a predictor is added, so a small rise means little. Adjusted R², AIC or cross-validation weigh the gain in fit against the extra parameter.
- **Why the wrong options are wrong (tutor only):**
  B) Extra predictors can make predictions of new data worse.
  D) Even a random predictor raises R² a little.
- **Hint:** Could a column of random numbers do the same?

### ch22-hw-07-v2
- **Kind:** AI-written version of ch22-hw-07
- **Concepts:** Penalizing complexity
- **Type:** select-all
- **Question:**

Adding northing to the Clarkia admixture model raised R² from 0.9249 to 0.9250, but raised LOOCV RMSE from 0.049 to 0.136. What does this suggest?

- **Options:**

  A) Northing explains a lot of extra variation in admixture
  B) The extra predictor fits noise in the six populations and predicts new populations worse
  C) LOOCV must be wrong, since R² and LOOCV should always agree
  D) The two-predictor model is better because R² went up

- **Answer (tutor only):** B
- **Explanation (tutor only):** R² always rises when a predictor is added. Cross-validation asks how well the model predicts populations it didn't see, and the extra predictor made those predictions worse: a sign of overfitting.
- **Why the wrong options are wrong (tutor only):**
  A) R² rose by only 0.0001.
  C) R² measures fit to the data used; LOOCV measures prediction of new data. They often disagree.
  D) A rise in R² is guaranteed and tiny here.
- **Hint:** Which number is about new data?

### ch22-hw-08
- **Kind:** Course original
- **Concepts:** Diagnostics & robustness; Biology & study design
- **Type:** MC
- **Question:**

Thanks to the central limit theorem, linear models are fairly robust to non-normal residuals and somewhat robust to unequal variance. Why is it still important to check assumptions and look at diagnostic plots?

- **Options:**

  A) They can reveal that our model is missing key features of the biological story
  B) You can never be too careful when it comes to p-values, better safe than sorry
  C) jk no big deal. Linear models are robust, chillax

- **Answer (tutor only):** A
- **Explanation (tutor only):** Diagnostics aren't just a validity check for p-values. In Anscombe's group 2, the straight line was 'significant', but the real relationship was a curve; a curve, a fan shape or a pattern by site in the residuals tells you the model is missing part of the biology.
- **Why the wrong options are wrong (tutor only):**
  B) Robustness means the p-values are usually fine, so p-values aren't the main reason to look.
  C) The p-values may be fine, but a robust p-value from the wrong model still tells the wrong story (Anscombe's groups 2-4).
- **Hint:** What did the diagnostic plots tell you about Anscombe's group 2 that the ANOVA table didn't?

### ch22-hw-08-v1
- **Kind:** AI-written version of ch22-hw-08
- **Concepts:** Diagnostics & robustness; Biology & study design
- **Type:** MC
- **Question:**

Linear models are fairly robust to non-normal residuals. A student fits a straight line to plant growth over time, gets p < 0.001, and skips the diagnostic plots. The residuals vs fitted plot would have shown a clear upside-down U. What did they miss?

- **Options:**

  A) Growth probably levels off, a key part of the biology the straight line ignores
  B) That the data should be thrown out
  C) Only that the p-value is slightly too small
  D) Nothing important: with p < 0.001 the model is clearly right

- **Answer (tutor only):** A
- **Explanation (tutor only):** A curved pattern in the residuals means the relationship isn't a straight line. Here it suggests growth slows over time, which is a biological insight a straight line hides.
- **Why the wrong options are wrong (tutor only):**
  B) The data are fine; the model needs to change.
  C) The main problem is the model's shape, not the p-value.
  D) A small p-value doesn't mean the model has the right shape (Anscombe's group 2).
- **Hint:** What does a U in the residuals mean?

### ch22-hw-08-v2
- **Kind:** AI-written version of ch22-hw-08
- **Concepts:** Diagnostics & robustness; Biology & study design
- **Type:** MC
- **Question:**

Thanks to the central limit theorem, a linear model's p-values are often fine even when residuals aren't normal. A colleague says: 'So diagnostic plots are pointless.' What's the best response?

- **Options:**

  A) Diagnostics tell us whether the model matches the biology, not only whether p-values are valid
  B) Diagnostics are only useful for checking normality
  C) Diagnostic plots are only needed when the sample size is very large
  D) Agreed: if p-values are valid, the model is correct

- **Answer (tutor only):** A
- **Explanation (tutor only):** A robust p-value from the wrong model still tells the wrong story. Diagnostics can reveal a curve, an outlier, one influential point or a missing variable.
- **Why the wrong options are wrong (tutor only):**
  B) They also reveal curves, outliers and leverage.
  C) Diagnostics matter at any sample size.
  D) Valid p-values and a correct model are different things.
- **Hint:** Think about Anscombe's groups 2-4.

### ch22-hw-09
- **Kind:** Course original
- **Concepts:** Biology & study design
- **Type:** MC
- **Question:**

You designed an experiment to test whether a novel environmentally friendly fertilizer increases maize yield. You grew plants in 4 field blocks, and placed fertilized and control plants in every block.

You included block in the model, lm(yield ~ fertilizer + block). But block had essentially no effect, and removing it decreased your RMSE and the p-value for fertilizer.

What should you do?

- **Options:**

  A) Drop block: including it made your model worse
  B) Drop block: doing so made the p-value you care about better
  C) Keep block: it was part of the study design
  D) There's no right answer here. Be a grown up, pick your approach and defend it

- **Answer (tutor only):** C
- **Explanation (tutor only):** Blocks were built into the experiment because plants in the same block share soil, water and light. The model should reflect how the data were collected, whatever the fit statistics say; you can report that block had little effect.
- **Why the wrong options are wrong (tutor only):**
  A) Better fit numbers aren't a reason to drop part of the design.
  B) Choosing the model that gives the p-value you want is p-hacking.
  D) The design was set before seeing the data, so choosing the model afterwards based on the results isn't a neutral judgment call.
- **Hint:** Why did you put plants in blocks in the first place?

### ch22-hw-09-v1
- **Kind:** AI-written version of ch22-hw-09
- **Concepts:** Biology & study design
- **Type:** MC
- **Question:**

You test whether a new soil amendment increases Clarkia seed set. Plants were grown in 6 greenhouse benches, with treated and control plants on every bench. Bench has little effect, and a model without bench gives a smaller p-value for the amendment.

What should you do?

- **Options:**

  A) Drop bench: it has little effect, so it only adds noise
  B) Drop bench: it makes the amendment's effect look stronger
  C) Fit both and report whichever you like better
  D) Keep bench: it was part of the study design

- **Answer (tutor only):** D
- **Explanation (tutor only):** Benches were built into the design because plants on the same bench share light and temperature. The model should match how the data were collected, whatever the p-value does.
- **Why the wrong options are wrong (tutor only):**
  A) A small block effect doesn't make plants on the same bench independent.
  B) Picking a model for a better p-value is p-hacking.
  C) Choosing after seeing the results is p-hacking.
- **Hint:** Why were plants spread across benches?

### ch22-hw-09-v2
- **Kind:** AI-written version of ch22-hw-09
- **Concepts:** Biology & study design
- **Type:** MC
- **Question:**

In a blocked field experiment, block has almost no effect on yield, and dropping it lowers the RMSE slightly. Why is 'it improves the fit' a poor reason to drop block?

- **Options:**

  A) Dropping any term always biases every coefficient
  B) Block effects are always large in field experiments
  C) RMSE should always increase when terms are dropped
  D) The model should reflect the study design, which was set before seeing the data

- **Answer (tutor only):** D
- **Explanation (tutor only):** Blocks were part of the design to account for shared conditions. Choosing the model by which result looks better after seeing the data invites p-hacking.
- **Why the wrong options are wrong (tutor only):**
  A) Too strong; the issue here is matching the design.
  B) Block effects are sometimes small.
  C) RMSE can go either way when a term is dropped.
- **Hint:** When was the decision to use blocks made?
