# Applied Biostats tutor: question bank, chapters 18–19 (Exam 2, chapters 13–21, plus an Exam 1 review as chapter 0)

Knowledge file for the course tutor. Each question has an ID, its concepts, the question, options, the answer, an explanation, why each wrong option is wrong, and a hint. Fields marked **tutor only** must never be shown to the student before they have answered.

- **Course originals** come from the instructor's homework, quizzes, Chime Ins and book.
- **AI-written versions** test the same idea with a new scenario or numbers. Their ID ends in -v1 or -v2 and names the original.
- 1020 questions in all. 139 use a figure and are marked **Figure question (website only)**: students practice those on the study-guide website, where the figure is shown. Use one only when a student brings it to you; its figure link is included.

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

## Chapter 18: >2 Groups

### ch18-book-01
- **Kind:** Course original
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** numeric
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

There are four groups. How many possible pairwise comparisons are there?

- **Answer (tutor only):** 6
- **Explanation (tutor only):** 4 × 3 / 2 = 6.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: 4 × 3 = 12, counting each pair twice.
- **Hint:** k(k - 1) / 2.

### ch18-book-01-v1
- **Kind:** AI-written version of ch18-book-01
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** numeric
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

If the researchers had added a fifth group (males with both claws removed), how many possible pairwise comparisons would there be?

- **Answer (tutor only):** 10
- **Explanation (tutor only):** 5 × 4 / 2 = 10.
- **Hint:** k(k - 1) / 2.

### ch18-book-01-v2
- **Kind:** AI-written version of ch18-book-01
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** numeric
- **Question:**

A study compares three diets. How many possible pairwise comparisons are there?

- **Answer (tutor only):** 3
- **Explanation (tutor only):** 3 × 2 / 2 = 3.
- **Hint:** k(k - 1) / 2.

### ch18-book-02
- **Kind:** Course original
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** numeric
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

If all four groups came from the same population (the null is true) and we did all 6 pairwise tests at α = 0.05, what is the probability of rejecting at least one true null? (Treat the tests as independent.)

- **Answer (tutor only):** 0.265
- **Explanation (tutor only):** 1 - 0.95⁶ = 1 - 0.735 = 0.265.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: 6 × 0.05 = 0.30.
- **Hint:** Find the chance of no false positives first.

### ch18-book-02-v1
- **Kind:** AI-written version of ch18-book-02
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** numeric
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

If all four groups came from the same population and we did all 6 pairwise tests at α = 0.01, what is the probability of rejecting at least one true null? (Treat the tests as independent.)

- **Answer (tutor only):** 0.059
- **Explanation (tutor only):** 1 - 0.99⁶ = 1 - 0.941 = 0.059.
- **Hint:** 1 - (1 - α)^tests.

### ch18-book-02-v2
- **Kind:** AI-written version of ch18-book-02
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** numeric
- **Question:**

If three groups all came from the same population and we did all 3 pairwise tests at α = 0.05, what is the probability of rejecting at least one true null? (Treat the tests as independent.)

- **Answer (tutor only):** 0.143
- **Explanation (tutor only):** 1 - 0.95³ = 1 - 0.857 = 0.143.
- **Hint:** 1 - (1 - α)^tests.

### ch18-book-03
- **Kind:** Course original
- **Concepts:** SD vs SE
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch18-book-crabs.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch18-book-crabs.png)
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

Looking at the plot (individual crabs, with means and 95% CIs), which comparison is most likely to be significantly different?

- **Options:**

  A) female vs male major removed
  B) female vs male minor removed
  C) intact male vs male major removed
  D) intact male vs male minor removed
  E) male major removed vs male minor removed

- **Answer (tutor only):** B
- **Explanation (tutor only):** Females have the highest mean and males with the minor claw removed the lowest; their CIs are far apart.
- **Why the wrong options are wrong (tutor only):**
  The other pairs have closer means and more overlapping CIs.
- **Hint:** Which two means are farthest apart?

### ch18-book-03-v1
- **Kind:** AI-written version of ch18-book-03
- **Concepts:** SD vs SE
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch18-book-crabs.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch18-book-crabs.png)
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

Looking at the plot (individual crabs, with means and 95% CIs), which comparison is LEAST likely to be significantly different?

- **Options:**

  A) intact male vs male minor removed
  B) female vs male minor removed
  C) female vs intact male
  D) female vs male major removed

- **Answer (tutor only):** A
- **Explanation (tutor only):** Intact males and males with the minor claw removed have similar means and overlapping CIs (Tukey p = 0.78).
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) all involve females, whose mean is well above the males'.
- **Hint:** Which two means are closest?

### ch18-book-03-v2
- **Kind:** AI-written version of ch18-book-03
- **Concepts:** SD vs SE
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch18-book-crabs.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch18-book-crabs.png)
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

Looking at the plot (individual crabs, with means and 95% CIs), which group has the highest mean rate of heat gain?

- **Options:**

  A) female
  B) intact male
  C) male major removed
  D) male minor removed

- **Answer (tutor only):** A
- **Explanation (tutor only):** Females have the highest mean (1.67), consistent with males' claws helping shed heat.
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) are lower.
- **Hint:** Find the highest mean.

### ch18-book-04
- **Kind:** Course original
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

crabType | mean | variance | n
female | 1.673 | 0.0412 | 19
intact male | 1.317 | 0.0521 | 19
male major removed | 1.456 | 0.0497 | 18
male minor removed | 1.253 | 0.0392 | 20

What is the largest fold difference in variance between treatments, and how concerned should we be about the equal variance assumption?

- **Options:**

  A) Less than two-fold; probably not a major concern
  B) Between two- and five-fold; somewhat worrisome, but we can plow ahead
  C) Between five- and ten-fold; a big concern
  D) More than ten-fold; we must transform or use Welch's ANOVA

- **Answer (tutor only):** A
- **Explanation (tutor only):** 0.0521 / 0.0392 = 1.33-fold, so the variances are very similar.
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) Overstate the difference.
- **Hint:** Divide the largest variance by the smallest.

### ch18-book-04-v1
- **Kind:** AI-written version of ch18-book-04
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

crabType | mean | variance | n
female | 1.673 | 0.0412 | 19
intact male | 1.317 | 0.0521 | 19
male major removed | 1.456 | 0.0497 | 18
male minor removed | 1.253 | 0.0392 | 20

Which two groups have the most different variances?

- **Options:**

  A) intact male and male minor removed
  B) female and intact male
  C) female and male major removed
  D) male major removed and male minor removed

- **Answer (tutor only):** A
- **Explanation (tutor only):** Largest: intact male (0.0521); smallest: male minor removed (0.0392).
- **Why the wrong options are wrong (tutor only):**
  Find the largest and smallest.
- **Hint:** Look at the variance column.

### ch18-book-04-v2
- **Kind:** AI-written version of ch18-book-04
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

crabType | mean | variance | n
female | 1.673 | 0.0412 | 19
intact male | 1.317 | 0.0521 | 19
male major removed | 1.456 | 0.0497 | 18
male minor removed | 1.253 | 0.0392 | 20

How many crabs were in the study?

- **Options:**

  A) 76
  B) 72
  C) 4
  D) 19

- **Answer (tutor only):** A
- **Explanation (tutor only):** 19 + 19 + 18 + 20 = 76.
- **Why the wrong options are wrong (tutor only):**
  B) That's the residual df.
  C) That's the number of groups.
  D) That's one group.
- **Hint:** Add the n column.

### ch18-book-05
- **Kind:** Course original
- **Concepts:** ANOVA calculations
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch18-book-crab-deviations.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch18-book-crab-deviations.png)
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

Each panel shows individual crabs, the group means (colored lines) and the grand mean (black line). Match each kind of deviation to its panel:

1. Total deviations
2. Model deviations
3. Error deviations

- **Options:**

  A) Panel a
  B) Panel b
  C) Panel c

- **Answer (tutor only):** 1-B, 2-C, 3-A
- **Explanation (tutor only):** a: crabs to their group mean (error). b: crabs to the grand mean (total). c: group means to the grand mean (model).
- **Why the wrong options are wrong (tutor only):**
  Check where each vertical line starts and ends.
- **Hint:** Which panel's lines never touch the points?

### ch18-book-05-v1
- **Kind:** AI-written version of ch18-book-05
- **Concepts:** ANOVA calculations
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch18-book-crab-deviations.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch18-book-crab-deviations.png)
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

Each panel shows individual crabs, the group means (colored lines) and the grand mean (black line). In which panel do all crabs in the same group have the same length of line?

- **Options:**

  A) Panel a
  B) Panel b
  C) Panel c

- **Answer (tutor only):** C
- **Explanation (tutor only):** Panel c shows model deviations: each group mean minus the grand mean, the same for every crab in a group.
- **Why the wrong options are wrong (tutor only):**
  A) Error deviations vary crab to crab.
  B) Total deviations vary crab to crab.
- **Hint:** Which deviation ignores individual values?

### ch18-book-05-v2
- **Kind:** AI-written version of ch18-book-05
- **Concepts:** ANOVA calculations
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch18-book-crab-deviations.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch18-book-crab-deviations.png)
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

Each panel shows individual crabs, the group means (colored lines) and the grand mean (black line). Squaring and summing the lines in which two panels gives SS model + SS error = SS total?

- **Options:**

  A) Panels c and a add to panel b
  B) Panels a and b add to panel c
  C) Panels b and c add to panel a

- **Answer (tutor only):** A
- **Explanation (tutor only):** c is model, a is error, b is total.
- **Why the wrong options are wrong (tutor only):**
  Identify which panel is total first.
- **Hint:** Which panel is total?

### ch18-book-06
- **Kind:** Course original
- **Concepts:** ANOVA calculations
- **Type:** MC
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

crabs |>
  mutate(grand_mean = mean(bodyTemperature)) |>
  group_by(crabType) |>
  mutate(group_mean = mean(bodyTemperature)) |>
  ungroup() |>
  summarise(this_partition = sum((group_mean - grand_mean)^2))

What is the best name for this_partition?

- **Options:**

  A) MS_total
  B) MS_model
  C) MS_error
  D) SS_total
  E) SS_model
  F) SS_error

- **Answer (tutor only):** E
- **Explanation (tutor only):** It sums squared deviations of group means from the grand mean (one per crab): the model sum of squares. It isn't divided by df, so it's not a mean square.
- **Why the wrong options are wrong (tutor only):**
  A), B) and C) Nothing is divided by df. D) and F) Those use the individual observations.
- **Hint:** What is compared to what, and is anything divided by df?

### ch18-book-06-v1
- **Kind:** AI-written version of ch18-book-06
- **Concepts:** ANOVA calculations
- **Type:** MC
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

crabs |>
  group_by(crabType) |>
  mutate(group_mean = mean(bodyTemperature)) |>
  ungroup() |>
  summarise(this_partition = sum((bodyTemperature - group_mean)^2))

What is the best name for this_partition?

- **Options:**

  A) SS_total
  B) SS_model
  C) SS_error
  D) MS_error

- **Answer (tutor only):** C
- **Explanation (tutor only):** Each crab minus its group mean, squared and summed: SS error. Not divided by df.
- **Why the wrong options are wrong (tutor only):**
  A) Uses the grand mean.
  B) Uses group means minus the grand mean.
  D) Would divide by df.
- **Hint:** What is subtracted?

### ch18-book-06-v2
- **Kind:** AI-written version of ch18-book-06
- **Concepts:** ANOVA calculations
- **Type:** MC
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

The model sum of squares is 1.9964 with 3 df. What is the model mean square?

- **Options:**

  A) 0.66546
  B) 1.9964
  C) 5.9892
  D) 0.04541

- **Answer (tutor only):** A
- **Explanation (tutor only):** MS = SS / df = 1.9964 / 3 = 0.665.
- **Why the wrong options are wrong (tutor only):**
  B) That's SS.
  C) Multiplies by df.
  D) That's MS residual.
- **Hint:** SS / df.

### ch18-book-07
- **Kind:** Course original
- **Concepts:** Assumptions & diagnostics; ANOVA in R
- **Type:** MC
- **Question:**

This code was meant to make QQ plots of residuals from an ANOVA but didn't work:

augmented_crab <- lm(bodyTemperature ~ crabType, data = crabs) |> augment()
augmented_crab |>
  ggplot(aes(x = .resid)) +
  geom_qq() +
  geom_qq_line() +
  facet_wrap(~crabType)

Why not?

- **Options:**

  A) We did not load the broom package
  B) We never generated augmented_crab
  C) You must use the original tibble, not augment() output, to make a plot
  D) geom_qq() expects the aesthetic to be called sample, not x

- **Answer (tutor only):** D
- **Explanation (tutor only):** geom_qq() and geom_qq_line() need aes(sample = .resid).
- **Why the wrong options are wrong (tutor only):**
  A) augment() comes from broom, but that isn't the problem here.
  B) It's created in the first line.
  C) augment() output works fine with ggplot.
- **Hint:** Which aesthetic does a QQ plot need?

### ch18-book-07-v1
- **Kind:** AI-written version of ch18-book-07
- **Concepts:** Assumptions & diagnostics; ANOVA in R
- **Type:** MC
- **Question:**

This code was meant to make a QQ plot of ANOVA residuals:

lm(bodyTemperature ~ crabType, data = crabs) |>
  augment() |>
  ggplot(aes(sample = .fitted)) +
  geom_qq() +
  geom_qq_line()

What's wrong?

- **Options:**

  A) It plots fitted values instead of residuals
  B) geom_qq() needs aes(x = ...) instead of sample
  C) augment() can't be used with lm() output
  D) Nothing; this plots the residuals

- **Answer (tutor only):** A
- **Explanation (tutor only):** Use aes(sample = .resid). Fitted values are just the group means.
- **Why the wrong options are wrong (tutor only):**
  B) sample is correct.
  C) augment() works with lm().
  D) .fitted isn't the residuals.
- **Hint:** Which column holds the residuals?

### ch18-book-07-v2
- **Kind:** AI-written version of ch18-book-07
- **Concepts:** Assumptions & diagnostics; ANOVA in R
- **Type:** MC
- **Question:**

Which line correctly sets up a QQ plot of residuals from augment() output?

- **Options:**

  A) ggplot(aes(sample = .resid))
  B) ggplot(aes(x = .resid))
  C) ggplot(aes(sample = .fitted))
  D) ggplot(aes(y = .resid))

- **Answer (tutor only):** A
- **Explanation (tutor only):** geom_qq() needs the sample aesthetic, and the residuals are in .resid.
- **Why the wrong options are wrong (tutor only):**
  B) and D) Wrong aesthetic.
  C) Wrong column.
- **Hint:** geom_qq() expects sample.

### ch18-book-08
- **Kind:** Course original
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Question:**

Four QQ plots were proposed for an ANOVA of crab heat gain by crabType:

Plot 1: raw bodyTemperature, faceted by crabType
Plot 2: raw bodyTemperature, all groups together
Plot 3: fitted values (.fitted), faceted by crabType
Plot 4: residuals (.resid), faceted by crabType

These plots evaluate the assumption of normally distributed residuals. Which two are reasonable ways to do so?

- **Options:**

  A) Plot 1 and Plot 2
  B) Plot 1 and Plot 4
  C) Plot 2 and Plot 4
  D) Plot 3 and Plot 4

- **Answer (tutor only):** B
- **Explanation (tutor only):** Within a group, raw values and residuals differ only by the group mean, so Plot 1 and Plot 4 show the same shape. Plot 2 mixes groups with different means. Plot 3: every fitted value in a group is the same number.
- **Why the wrong options are wrong (tutor only):**
  A) and C) Plot 2 pools groups with different means, which can look non-normal even when residuals are fine.
  D) Fitted values carry no information about residual shape.
- **Hint:** Residuals are the data minus their group mean.

### ch18-book-08-v1
- **Kind:** AI-written version of ch18-book-08
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Question:**

Why is a QQ plot of raw bodyTemperature with all four crab groups pooled a poor check of the ANOVA's normality assumption?

- **Options:**

  A) Pooling groups with different means distorts the shape
  B) Raw data can never be used to check normality at all
  C) QQ plots only work for data with a single group
  D) Pooled data always look perfectly normal

- **Answer (tutor only):** A
- **Explanation (tutor only):** The assumption is about residuals within groups. Mixing groups with different means can make normal residuals look non-normal.
- **Why the wrong options are wrong (tutor only):**
  B) Raw values within a group work.
  C) You can facet.
  D) Pooling can look odd.
- **Hint:** What does the assumption concern?

### ch18-book-08-v2
- **Kind:** AI-written version of ch18-book-08
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Question:**

Why is a QQ plot of fitted values (.fitted), faceted by crabType, useless for checking normality?

- **Options:**

  A) Every fitted value within a group is the same number
  B) Fitted values are always perfectly normally distributed
  C) Fitted values exist only for the reference group
  D) Faceting by group removes all of the information

- **Answer (tutor only):** A
- **Explanation (tutor only):** In a one-way ANOVA the fitted value is the group mean, so each panel is a single repeated value.
- **Why the wrong options are wrong (tutor only):**
  B) They're constant within a group.
  C) Every crab has a fitted value.
  D) Faceting is fine for residuals.
- **Hint:** What's the fitted value in an ANOVA?

### ch18-book-09
- **Kind:** Course original
- **Concepts:** ANOVA in R
- **Type:** matching
- **Question:**

In the context of an ANOVA, which R code gives you each of the following?

1. Estimates of model coefficients only
2. An ANOVA table
3. Results of a post-hoc test
4. Coefficients and standard errors, plus many potentially misleading t- and p-values

- **Options:**

  A) lm(y ~ x) |> anova()  OR  aov(y ~ x) |> summary()
  B) aov(y ~ x) |> TukeyHSD()
  C) lm(y ~ x) |> summary()
  D) lm(y ~ x)

- **Answer (tutor only):** 1-D, 2-A, 3-B, 4-C
- **Explanation (tutor only):** lm() alone prints coefficients. anova() (or summary() of aov()) gives the ANOVA table. TukeyHSD() runs a post-hoc test. summary() of an lm gives coefficient t-tests, which mostly test comparisons with the reference group and aren't the tests we want.
- **Why the wrong options are wrong (tutor only):**
  Common mix-up: summary() of an lm vs summary() of an aov. They give different output.
- **Hint:** Which one prints a table with Sum Sq and F?

### ch18-book-09-v1
- **Kind:** AI-written version of ch18-book-09
- **Concepts:** ANOVA in R
- **Type:** MC
- **Question:**

You want to know which pairs of crab groups differ after a significant ANOVA. Which code should you use?

- **Options:**

  A) aov(y ~ x) |> TukeyHSD()
  B) lm(y ~ x) |> summary()
  C) lm(y ~ x) |> anova()
  D) lm(y ~ x)

- **Answer (tutor only):** A
- **Explanation (tutor only):** TukeyHSD() runs the post-hoc comparisons.
- **Why the wrong options are wrong (tutor only):**
  B) Compares each group only with the reference.
  C) Gives the overall F test.
  D) Prints coefficients.
- **Hint:** Post-hoc test.

### ch18-book-09-v2
- **Kind:** AI-written version of ch18-book-09
- **Concepts:** ANOVA in R
- **Type:** matching
- **Question:**

Match each code to what it reports:

1. lm(y ~ x) |> anova()
2. lm(y ~ x)

- **Options:**

  A) An ANOVA table with SS, MS, F and p
  B) Model coefficients only
  C) Pairwise post-hoc comparisons
  D) Coefficients with t- and p-values

- **Answer (tutor only):** 1-A, 2-B
- **Explanation (tutor only):** anova() gives the ANOVA table; lm() alone prints coefficients.
- **Why the wrong options are wrong (tutor only):**
  TukeyHSD() and summary() do the others.
- **Hint:** What does each function add?

### ch18-book-10
- **Kind:** Course original
- **Concepts:** ANOVA calculations; ANOVA in R
- **Type:** MC
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

lm(bodyTemperature ~ crabType, data = crabs) |> anova()

          Df Sum Sq Mean Sq F value    Pr(>F)
crabType   3 1.9964 0.66546  14.654 1.521e-07
Residuals 72 3.2696 0.04541

What do we do to the null hypothesis?

- **Options:**

  A) Reject it
  B) Fail to reject it
  C) Accept it
  D) Fail to accept it

- **Answer (tutor only):** A
- **Explanation (tutor only):** F = 14.7 on 3 and 72 df gives p = 1.5 × 10⁻⁷, far below 0.05: rates of heat gain differ among crab groups.
- **Why the wrong options are wrong (tutor only):**
  B) p is tiny. C) and D) We don't accept nulls.
- **Hint:** Compare p with α.

### ch18-book-10-v1
- **Kind:** AI-written version of ch18-book-10
- **Concepts:** ANOVA calculations; ANOVA in R
- **Type:** MC
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

lm(bodyTemperature ~ crabType, data = crabs) |> anova()

          Df Sum Sq Mean Sq F value    Pr(>F)
crabType   3 1.9964 0.66546  14.654 1.521e-07
Residuals 72 3.2696 0.04541

What does this result tell us?

- **Options:**

  A) Not all crab groups have the same mean heat gain
  B) All four crab groups differ in mean heat gain
  C) Females gain heat faster than every male group
  D) The major claw definitely works as a heat sink

- **Answer (tutor only):** A
- **Explanation (tutor only):** Rejecting the ANOVA null means not all means are equal. Which differ needs post-hoc tests; causes need biology.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Need post-hoc tests.
  D) A p-value doesn't prove a mechanism.
- **Hint:** What's the ANOVA's alternative?

### ch18-book-10-v2
- **Kind:** AI-written version of ch18-book-10
- **Concepts:** ANOVA calculations; ANOVA in R
- **Type:** MC
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

lm(bodyTemperature ~ crabType, data = crabs) |> anova()

          Df Sum Sq Mean Sq F value    Pr(>F)
crabType   3 1.9964 0.66546  14.654 1.521e-07
Residuals 72 3.2696 0.04541

If the null hypothesis were true, about what value would we expect F to be?

- **Options:**

  A) About 1
  B) About 0
  C) About 14.7
  D) About 72

- **Answer (tutor only):** A
- **Explanation (tutor only):** Under the null, both mean squares estimate the same variance, so F ≈ 1.
- **Why the wrong options are wrong (tutor only):**
  B) F near 0 is unusual.
  C) That's the observed F.
  D) That's a df.
- **Hint:** Ratio of two estimates of the same variance.

### ch18-book-11
- **Kind:** Course original
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** MC
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

aov(bodyTemperature ~ crabType, data = crabs) |> TukeyHSD()

comparison | diff | p adj
intact male - female | -0.355 | < 0.001
male major removed - female | -0.217 | 0.015
male minor removed - female | -0.420 | < 0.001
male major removed - intact male | 0.138 | 0.208
male minor removed - intact male | -0.065 | 0.778
male minor removed - male major removed | -0.203 | 0.023

If female is in significance group 'a', which group(s) is intact male in?

- **Options:**

  A) a only
  B) b only
  C) c only
  D) a, b
  E) b, c
  F) a, b, c

- **Answer (tutor only):** E
- **Explanation (tutor only):** Female differs from all males: a. Male major removed and male minor removed differ (p = 0.023), so they get different letters, b and c. Intact male doesn't differ from either of them (p = 0.21 and 0.78), so it shares both letters: b, c.
- **Why the wrong options are wrong (tutor only):**
  A) and D) Intact male differs from female.
  B) and C) Intact male doesn't differ from either 'major removed' (b) or 'minor removed' (c).
- **Hint:** Groups that don't differ share a letter. Assign letters to the two claw-removed groups first.

### ch18-book-11-v1
- **Kind:** AI-written version of ch18-book-11
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** MC
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

aov(bodyTemperature ~ crabType, data = crabs) |> TukeyHSD()

comparison | diff | p adj
intact male - female | -0.355 | < 0.001
male major removed - female | -0.217 | 0.015
male minor removed - female | -0.420 | < 0.001
male major removed - intact male | 0.138 | 0.208
male minor removed - intact male | -0.065 | 0.778
male minor removed - male major removed | -0.203 | 0.023

Which comparisons are NOT significant at α = 0.05?

- **Options:**

  A) major removed - intact male and minor removed - intact male
  B) intact male - female and minor removed - female
  C) major removed - female and minor removed - major removed
  D) All six comparisons are significant at α = 0.05

- **Answer (tutor only):** A
- **Explanation (tutor only):** p = 0.208 and 0.778; all others are below 0.05.
- **Why the wrong options are wrong (tutor only):**
  B) and C) are significant. D) Two are not.
- **Hint:** Find p adj > 0.05.

### ch18-book-11-v2
- **Kind:** AI-written version of ch18-book-11
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** MC
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

aov(bodyTemperature ~ crabType, data = crabs) |> TukeyHSD()

comparison | diff | p adj
intact male - female | -0.355 | < 0.001
male major removed - female | -0.217 | 0.015
male minor removed - female | -0.420 | < 0.001
male major removed - intact male | 0.138 | 0.208
male minor removed - intact male | -0.065 | 0.778
male minor removed - male major removed | -0.203 | 0.023

If female is in significance group 'a', which group(s) is 'male major removed' in?

- **Options:**

  A) b only
  B) c only
  C) a, b
  D) b, c

- **Answer (tutor only):** A
- **Explanation (tutor only):** Major removed differs from female (a) and from minor removed (c), but not from intact male (b, c), so it's 'b'.
- **Why the wrong options are wrong (tutor only):**
  B) It differs from minor removed, which is c.
  C) It differs from female.
  D) It differs from minor removed (c).
- **Hint:** Start from the female/minor-removed letters.

### ch18-chimein-01
- **Kind:** Course original
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** matching
- **Question:**

Match each question to its answer:

1. Why is it a bad idea to conduct all pairwise t-tests when you have more than two groups?
2. How does an ANOVA overcome the multiple testing problem?

- **Options:**

  A) Because the false positive rate is no longer what we advertise (α)
  B) By testing one hypothesis, not many
  C) Because it's more work
  D) By lowering α for each test

- **Answer (tutor only):** 1-A, 2-B
- **Explanation (tutor only):** Many tests each with α = 0.05 give a much higher chance of at least one false positive. ANOVA tests a single null (all means equal).
- **Why the wrong options are wrong (tutor only):**
  C) Effort isn't the issue. D) ANOVA doesn't adjust α; post-hoc corrections do something like that.
- **Hint:** What happens to the chance of a false positive as you run more tests?

### ch18-chimein-01-v1
- **Kind:** AI-written version of ch18-chimein-01
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** matching
- **Question:**

Match each scenario to its consequence:

1. Running 20 t-tests on groups that all come from the same population, each at α = 0.05
2. Running one ANOVA on those same groups at α = 0.05

- **Options:**

  A) About a 64% chance of at least one false positive
  B) A 5% chance of a false positive
  C) A 0% chance of a false positive
  D) A 100% chance of a false positive

- **Answer (tutor only):** 1-A, 2-B
- **Explanation (tutor only):** 1 - 0.95²⁰ = 0.64. One ANOVA keeps the false positive rate at α.
- **Why the wrong options are wrong (tutor only):**
  Multiple tests multiply chances.
- **Hint:** 1 - 0.95²⁰.

### ch18-chimein-01-v2
- **Kind:** AI-written version of ch18-chimein-01
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** matching
- **Question:**

Match each approach to what it does about multiple testing:

1. ANOVA
2. Tukey's post-hoc test

- **Options:**

  A) Tests a single null hypothesis that all means are equal
  B) Compares pairs while controlling the overall false positive rate
  C) Runs each pairwise t-test at α = 0.05 with no adjustment
  D) Ignores the problem entirely

- **Answer (tutor only):** 1-A, 2-B
- **Explanation (tutor only):** ANOVA avoids many tests; Tukey adjusts for them.
- **Why the wrong options are wrong (tutor only):**
  Neither ignores the problem.
- **Hint:** One test vs adjusted tests.

### ch18-chimein-02
- **Kind:** Course original
- **Concepts:** SD vs SE
- **Type:** MC
- **Question:**

Which of the following is true about sampling distributions?

- **Options:**

  A) The sampling distribution shows how values in your data are spread
  B) The sampling distribution shows the distribution of samples in your data
  C) The sampling distribution shows the distribution of estimates from many samples (or bootstraps)

- **Answer (tutor only):** C
- **Explanation (tutor only):** A sampling distribution is the distribution of an estimate (like a mean) across many hypothetical samples, which we approximate by bootstrapping or theory.
- **Why the wrong options are wrong (tutor only):**
  A) That's the distribution of the data.
  B) Not a meaningful description.
- **Hint:** It's a distribution of estimates, not of data points.

### ch18-chimein-02-v1
- **Kind:** AI-written version of ch18-chimein-02
- **Concepts:** SD vs SE
- **Type:** MC
- **Question:**

A researcher bootstraps the mean egg length of cuckoos 1,000 times and plots a histogram of the 1,000 bootstrap means. What does this histogram approximate?

- **Options:**

  A) The sampling distribution of the mean
  B) The distribution of egg lengths in the population
  C) The distribution of egg lengths in the sample
  D) The null distribution of the egg-length difference

- **Answer (tutor only):** A
- **Explanation (tutor only):** Bootstrapping approximates the distribution of an estimate across many samples.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Those are about individual eggs.
  D) Null distributions come from permutation or theory under the null.
- **Hint:** Distribution of estimates.

### ch18-chimein-02-v2
- **Kind:** AI-written version of ch18-chimein-02
- **Concepts:** SD vs SE
- **Type:** MC
- **Question:**

The spread (standard deviation) of a sampling distribution is called:

- **Options:**

  A) The standard error
  B) The standard deviation of the data
  C) The residual variance
  D) The sum of squares

- **Answer (tutor only):** A
- **Explanation (tutor only):** The SE is the SD of a sampling distribution.
- **Why the wrong options are wrong (tutor only):**
  B) That's spread among individuals.
  C) and D) Those are ANOVA quantities.
- **Hint:** SD of estimates.

### ch18-chimein-03
- **Kind:** Course original
- **Concepts:** SD vs SE
- **Type:** MC
- **Question:**

What is the distinction between the standard error and the standard deviation?

- **Options:**

  A) The standard error is always greater than the standard deviation
  B) The standard deviation reflects variability in your data, while the standard error reflects uncertainty in an estimate
  C) The standard error reflects variability in your data, while the standard deviation reflects uncertainty in an estimate

- **Answer (tutor only):** B
- **Explanation (tutor only):** SD describes spread among individuals; SE (= SD / √n) describes how much an estimate would vary across samples.
- **Why the wrong options are wrong (tutor only):**
  A) The SE is smaller than the SD for any n > 1.
  C) Backwards.
- **Hint:** Which one shrinks as sample size grows?

### ch18-chimein-03-v1
- **Kind:** AI-written version of ch18-chimein-03
- **Concepts:** SD vs SE
- **Type:** MC
- **Question:**

A sample of 100 crabs has an SD of 0.2 for heat gain. What is the standard error of the mean, and what does it describe?

- **Options:**

  A) 0.02; uncertainty in the mean
  B) 0.02; variability among crabs
  C) 0.2; uncertainty in the mean
  D) 2.0; variability among crabs

- **Answer (tutor only):** A
- **Explanation (tutor only):** SE = 0.2 / √100 = 0.02, describing uncertainty in the estimated mean.
- **Why the wrong options are wrong (tutor only):**
  B) The SD (0.2) describes variability.
  C) That's the SD.
  D) Multiplies instead of divides.
- **Hint:** SD / √n.

### ch18-chimein-03-v2
- **Kind:** AI-written version of ch18-chimein-03
- **Concepts:** SD vs SE
- **Type:** MC
- **Question:**

Which quantity would you report to describe how much individual cuckoo eggs vary in length?

- **Options:**

  A) The standard deviation
  B) The standard error
  C) The 95% confidence interval
  D) The p-value

- **Answer (tutor only):** A
- **Explanation (tutor only):** The SD describes variability among individuals; SE and CI describe uncertainty in an estimate.
- **Why the wrong options are wrong (tutor only):**
  B) and C) describe uncertainty in the mean.
  D) p is about a hypothesis test.
- **Hint:** Variability vs uncertainty.

### ch18-hw-01
- **Kind:** Course original
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** numeric
- **Question:**

To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species.

With six groups, how many possible pairwise comparisons are there?

- **Answer (tutor only):** 15
- **Explanation (tutor only):** k(k - 1) / 2 = 6 × 5 / 2 = 15.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: 6 × 5 = 30, counting each pair twice.
- **Hint:** Each pair counts once: A vs B is the same as B vs A.

### ch18-hw-01-v1
- **Kind:** AI-written version of ch18-hw-01
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** numeric
- **Question:**

To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species. If researchers had studied only four host species, how many possible pairwise comparisons would there be?

- **Answer (tutor only):** 6
- **Explanation (tutor only):** 4 × 3 / 2 = 6.
- **Hint:** k(k - 1) / 2.

### ch18-hw-01-v2
- **Kind:** AI-written version of ch18-hw-01
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** numeric
- **Question:**

A study compares eight populations of lizards. How many possible pairwise comparisons are there?

- **Answer (tutor only):** 28
- **Explanation (tutor only):** 8 × 7 / 2 = 28.
- **Hint:** k(k - 1) / 2.

### ch18-hw-02
- **Kind:** Course original
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** numeric
- **Question:**

To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species.

If we conducted all 15 pairwise comparisons and every null hypothesis were true, what is the probability of rejecting at least one true null at α = 0.05? (Treat the tests as independent.)

- **Answer (tutor only):** 0.537
- **Explanation (tutor only):** P(no false positives) = 0.95¹⁵ = 0.463, so P(at least one) = 1 - 0.463 = 0.537.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: 15 × 0.05 = 0.75. Adding probabilities overcounts.
- **Hint:** Find the chance of no false positives in all 15 tests first.

### ch18-hw-02-v1
- **Kind:** AI-written version of ch18-hw-02
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** numeric
- **Question:**

To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species. If we conducted 10 pairwise comparisons and every null hypothesis were true, what is the probability of rejecting at least one true null at α = 0.05? (Treat the tests as independent.)

- **Answer (tutor only):** 0.401
- **Explanation (tutor only):** 1 - 0.95¹⁰ = 1 - 0.599 = 0.401.
- **Hint:** 1 - P(no false positives).

### ch18-hw-02-v2
- **Kind:** AI-written version of ch18-hw-02
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** numeric
- **Question:**

If we conducted 15 pairwise comparisons at α = 0.01 and every null hypothesis were true, what is the probability of rejecting at least one true null? (Treat the tests as independent.)

- **Answer (tutor only):** 0.14
- **Explanation (tutor only):** 1 - 0.99¹⁵ = 1 - 0.860 = 0.140.
- **Hint:** 1 - (1 - α)^tests.

### ch18-hw-03
- **Kind:** Course original
- **Concepts:** ANOVA calculations
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch18-hw-cuckoo-deviations.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch18-hw-cuckoo-deviations.png)
- **Question:**

To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species.

Each plot shows cuckoo egg lengths by host (colored points), the group means (colored lines) and the grand mean (black line). Match each kind of deviation to the plot that shows it:

1. Error deviations
2. Model deviations
3. Total deviations

- **Options:**

  A) Plot A
  B) Plot B
  C) Plot C

- **Answer (tutor only):** 1-B, 2-A, 3-C
- **Explanation (tutor only):** A: group means to the grand mean (model). B: each egg to its group mean (error). C: each egg to the grand mean (total).
- **Why the wrong options are wrong (tutor only):**
  Check where each vertical line starts and ends.
- **Hint:** In which plot do the lines never reach the points?

### ch18-hw-03-v1
- **Kind:** AI-written version of ch18-hw-03
- **Concepts:** ANOVA calculations
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch18-hw-cuckoo-deviations.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch18-hw-cuckoo-deviations.png)
- **Question:**

To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species.

Each plot shows cuckoo egg lengths by host (colored points), the group means (colored lines) and the grand mean (black line). Which plot shows the deviations whose sum of squares goes in the DENOMINATOR of F (after dividing by df)?

- **Options:**

  A) Plot A
  B) Plot B
  C) Plot C

- **Answer (tutor only):** B
- **Explanation (tutor only):** F = MS model / MS error. MS error comes from error deviations: each egg to its group mean (Plot B).
- **Why the wrong options are wrong (tutor only):**
  A) Model (numerator).
  C) Total.
- **Hint:** Denominator = error.

### ch18-hw-03-v2
- **Kind:** AI-written version of ch18-hw-03
- **Concepts:** ANOVA calculations
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch18-hw-cuckoo-deviations.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch18-hw-cuckoo-deviations.png)
- **Question:**

To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species.

Each plot shows cuckoo egg lengths by host (colored points), the group means (colored lines) and the grand mean (black line). Which plot shows the deviations that would be large if host species had a big effect on egg length?

- **Options:**

  A) Plot A
  B) Plot B
  C) Plot C

- **Answer (tutor only):** A
- **Explanation (tutor only):** Model deviations (group means to the grand mean) are large when groups differ a lot.
- **Why the wrong options are wrong (tutor only):**
  B) Error deviations reflect within-group spread.
  C) Total deviations include both.
- **Hint:** Between-group differences.

### ch18-hw-04
- **Kind:** Course original
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Question:**

To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species.

host | mean egg length (mm) | variance | n
Hedge Sparrow | 23.12 | 1.142 | 14
Meadow Pipit | 22.30 | 0.848 | 45
Pied Wagtail | 22.90 | 1.140 | 15
Robin | 22.58 | 0.469 | 16
Tree Pipit | 23.09 | 0.813 | 15
Wren | 21.13 | 0.553 | 15

What is the largest fold difference in variance between host species, and how worried should we be about the equal variance assumption?

- **Options:**

  A) Less than two-fold; not a concern
  B) Between two- and five-fold; probably not a major concern
  C) Between five- and ten-fold; somewhat worrisome
  D) More than ten-fold; a big concern, so we should transform or use Welch's ANOVA

- **Answer (tutor only):** B
- **Explanation (tutor only):** Largest / smallest = 1.142 / 0.469 = 2.4-fold, within the rule of thumb (less than about 5), so the equal variance assumption is probably fine.
- **Why the wrong options are wrong (tutor only):**
  A) 2.4 is more than two-fold.
  C) and D) Overstate the difference.
- **Hint:** Divide the largest variance by the smallest.

### ch18-hw-04-v1
- **Kind:** AI-written version of ch18-hw-04
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Question:**

To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species.

host | mean egg length (mm) | variance | n
Hedge Sparrow | 23.12 | 1.142 | 14
Meadow Pipit | 22.30 | 0.848 | 45
Pied Wagtail | 22.90 | 1.140 | 15
Robin | 22.58 | 0.469 | 16
Tree Pipit | 23.09 | 0.813 | 15
Wren | 21.13 | 0.553 | 15

Which two host species have the most different variances?

- **Options:**

  A) Hedge Sparrow and Robin
  B) Meadow Pipit and Wren
  C) Pied Wagtail and Tree Pipit
  D) Hedge Sparrow and Pied Wagtail

- **Answer (tutor only):** A
- **Explanation (tutor only):** Largest variance: Hedge Sparrow (1.142); smallest: Robin (0.469).
- **Why the wrong options are wrong (tutor only):**
  Find the largest and smallest variances.
- **Hint:** Look at the variance column.

### ch18-hw-04-v2
- **Kind:** AI-written version of ch18-hw-04
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Question:**

Five groups of snails have variances in shell length of 2.1, 2.8, 3.0, 4.2 and 25.0 mm². How worried should we be about the equal variance assumption?

- **Options:**

  A) Less than two-fold; not a concern
  B) Two- to five-fold; probably fine
  C) Five- to ten-fold; somewhat worrisome
  D) Over ten-fold; a big concern

- **Answer (tutor only):** D
- **Explanation (tutor only):** 25.0 / 2.1 = 11.9-fold: transform or use Welch's ANOVA.
- **Why the wrong options are wrong (tutor only):**
  A), B) and C) The ratio is about 12.
- **Hint:** Largest / smallest.

### ch18-hw-05
- **Kind:** Course original
- **Concepts:** ANOVA calculations; ANOVA in R
- **Type:** MC
- **Question:**

To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species.

lm(egg_length ~ host_species, data = cuckoo) |> anova()

              Df Sum Sq Mean Sq F value    Pr(>F)
host_species   5 42.940  8.5879  10.388 3.152e-08
Residuals    114 94.248  0.8267

What is the p-value, and what do we do with the null hypothesis at α = 0.05?

- **Options:**

  A) Less than 10⁻¹⁰; reject
  B) Between 10⁻¹⁰ and 10⁻³; reject
  C) Between 10⁻³ and 0.05; reject
  D) Greater than 0.05; fail to reject

- **Answer (tutor only):** B
- **Explanation (tutor only):** p = 3.2 × 10⁻⁸ is between 10⁻¹⁰ and 10⁻³, far below 0.05, so we reject the null that all hosts have the same mean egg length.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: misreading scientific notation. 3.2e-08 means 0.000000032.
- **Hint:** e-08 means ×10⁻⁸.

### ch18-hw-05-v1
- **Kind:** AI-written version of ch18-hw-05
- **Concepts:** ANOVA calculations; ANOVA in R
- **Type:** MC
- **Question:**

To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species.

lm(egg_length ~ host_species, data = cuckoo) |> anova()

              Df Sum Sq Mean Sq F value    Pr(>F)
host_species   5 42.940  8.5879  10.388 3.152e-08
Residuals    114 94.248  0.8267

How many cuckoo eggs were measured?

- **Options:**

  A) 120
  B) 114
  C) 119
  D) 6

- **Answer (tutor only):** A
- **Explanation (tutor only):** df residual = n - groups, so n = 114 + 6 = 120.
- **Why the wrong options are wrong (tutor only):**
  B) That's the residual df.
  C) That's df total (n - 1).
  D) That's the number of hosts.
- **Hint:** Residual df = n - number of groups.

### ch18-hw-05-v2
- **Kind:** AI-written version of ch18-hw-05
- **Concepts:** ANOVA calculations; ANOVA in R
- **Type:** MC
- **Question:**

To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species.

lm(egg_length ~ host_species, data = cuckoo) |> anova()

              Df Sum Sq Mean Sq F value    Pr(>F)
host_species   5 42.940  8.5879  10.388 3.152e-08
Residuals    114 94.248  0.8267

How was the F value of 10.388 calculated?

- **Options:**

  A) 8.5879 / 0.8267
  B) 42.940 / 94.248
  C) 42.940 / 5
  D) 5 / 114

- **Answer (tutor only):** A
- **Explanation (tutor only):** F = MS model / MS residual = 8.5879 / 0.8267.
- **Why the wrong options are wrong (tutor only):**
  B) Ratio of SS, not MS.
  C) That's MS model.
  D) Ratio of df.
- **Hint:** Ratio of mean squares.

### ch18-hw-06
- **Kind:** Course original
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** select-all
- **Question:**

To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species.

Tukey post-hoc test (only significant pairs shown, adjusted p < 0.05):
Hedge Sparrow - Meadow Pipit: p = 0.043
Hedge Sparrow - Wren: p < 0.001
Meadow Pipit - Tree Pipit: p = 0.048
Meadow Pipit - Wren: p < 0.001
Pied Wagtail - Wren: p < 0.001
Robin - Wren: p < 0.001
Tree Pipit - Wren: p < 0.001
(All other pairs: p > 0.2)

Which host species (if any) is significantly different from all the others? (Select all that apply.)

- **Options:**

  A) Wren
  B) Meadow Pipit
  C) Robin
  D) Hedge Sparrow
  E) Pied Wagtail
  F) Tree Pipit
  G) None

- **Answer (tutor only):** A
- **Explanation (tutor only):** Wren differs from all five other hosts (cuckoo eggs in wren nests are much smaller). Meadow Pipit differs from only three of the five.
- **Why the wrong options are wrong (tutor only):**
  B) Meadow Pipit doesn't differ significantly from Pied Wagtail or Robin.
- **Hint:** Which host appears in a significant comparison with every other host?

### ch18-hw-06-v1
- **Kind:** AI-written version of ch18-hw-06
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** select-all
- **Question:**

To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species.

Tukey post-hoc test (only significant pairs shown, adjusted p < 0.05):
Hedge Sparrow - Meadow Pipit: p = 0.043
Hedge Sparrow - Wren: p < 0.001
Meadow Pipit - Tree Pipit: p = 0.048
Meadow Pipit - Wren: p < 0.001
Pied Wagtail - Wren: p < 0.001
Robin - Wren: p < 0.001
Tree Pipit - Wren: p < 0.001
(All other pairs: p > 0.2)

Which host species does NOT differ significantly from Robin?

- **Options:**

  A) Hedge Sparrow
  B) Wren
  C) Both of these differ from Robin
  D) Neither of these differs from Robin

- **Answer (tutor only):** A
- **Explanation (tutor only):** Robin - Wren is significant (p < 0.001), but Robin - Hedge Sparrow isn't listed, so p > 0.2.
- **Why the wrong options are wrong (tutor only):**
  B) Robin - Wren is significant.
  C) and D) Only one differs.
- **Hint:** Is the pair listed?

### ch18-hw-06-v2
- **Kind:** AI-written version of ch18-hw-06
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** select-all
- **Question:**

To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species.

Tukey post-hoc test (only significant pairs shown, adjusted p < 0.05):
Hedge Sparrow - Meadow Pipit: p = 0.043
Hedge Sparrow - Wren: p < 0.001
Meadow Pipit - Tree Pipit: p = 0.048
Meadow Pipit - Wren: p < 0.001
Pied Wagtail - Wren: p < 0.001
Robin - Wren: p < 0.001
Tree Pipit - Wren: p < 0.001
(All other pairs: p > 0.2)

How many hosts does Meadow Pipit differ from significantly?

- **Options:**

  A) 3
  B) 1
  C) 5
  D) 0

- **Answer (tutor only):** A
- **Explanation (tutor only):** Meadow Pipit differs from Hedge Sparrow, Tree Pipit and Wren.
- **Why the wrong options are wrong (tutor only):**
  Count the pairs that include Meadow Pipit.
- **Hint:** Count the lines with Meadow Pipit.

### ch18-hw-07
- **Kind:** Course original
- **Concepts:** ANOVA in R
- **Type:** MC
- **Question:**

To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species.

Piping lm(egg_length ~ host_species) into summary() shows a p-value for the (Intercept) of < 2e-16. Why don't we care?

- **Options:**

  A) Because it's just a p-value, not an effect size
  B) Because it tests the silly null that mean cuckoo egg length is zero
  C) Because it tests the silly null that mean Hedge Sparrow-nest egg length is 0
  D) We should care: it shows host species matters

- **Answer (tutor only):** C
- **Explanation (tutor only):** Hedge Sparrow comes first alphabetically, so it's the reference level and the intercept is its mean. The intercept's p-value tests whether that mean is zero, which no one doubts for an egg.
- **Why the wrong options are wrong (tutor only):**
  A) Not the reason.
  B) The intercept is the reference group's mean, not the overall mean.
  D) It tests a null we already know is false.
- **Hint:** Which group does the intercept describe?

### ch18-hw-07-v1
- **Kind:** AI-written version of ch18-hw-07
- **Concepts:** ANOVA in R
- **Type:** MC
- **Question:**

To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species. Piping lm(egg_length ~ host_species) into summary() shows a coefficient for host_speciesWren of -1.99 with p < 0.001. What does this test?

- **Options:**

  A) Whether Wren eggs differ from Hedge Sparrow eggs
  B) Whether Wren eggs differ from all other hosts' eggs
  C) Whether the mean Wren egg length is zero
  D) Whether host species affects egg length overall

- **Answer (tutor only):** A
- **Explanation (tutor only):** Hedge Sparrow is the reference level, so each coefficient is a difference from it.
- **Why the wrong options are wrong (tutor only):**
  B) Only versus the reference.
  C) That's what the intercept tests (for Hedge Sparrow).
  D) That's the ANOVA F test.
- **Hint:** Which host is the reference level?

### ch18-hw-07-v2
- **Kind:** AI-written version of ch18-hw-07
- **Concepts:** ANOVA in R
- **Type:** MC
- **Question:**

To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species. Why is the ANOVA F test, rather than the coefficient p-values from summary(), the right first test of whether host species matters?

- **Options:**

  A) It tests one null (all hosts equal), avoiding multiple tests
  B) It always gives smaller p-values than the coefficient tests
  C) The coefficients' p-values can't be calculated for factors
  D) summary() ignores the host species variable entirely

- **Answer (tutor only):** A
- **Explanation (tutor only):** The coefficient tests compare each host only with the reference, and there are many of them. The F test asks one question about all groups.
- **Why the wrong options are wrong (tutor only):**
  B) Not always.
  C) They are calculated.
  D) summary() includes it.
- **Hint:** One test vs many.

### ch18-quiz-01
- **Kind:** Course original
- **Concepts:** ANOVA calculations
- **Type:** matching
- **Question:**

A study has 30 samples spread across 4 groups. Complete its ANOVA table:

source | df | Sum Sq | Mean Sq | F | p-value
Model | [A] | 5 | [C] | [E] | 0.48
Residuals | [B] | 52 | [D] | |

Match each missing entry to its value:

1. [A] model df
2. [B] residual df
3. [C] model mean square
4. [D] residual mean square
5. [E] F

- **Options:**

  A) 3
  B) 26
  C) 1.67
  D) 2
  E) 0.83

- **Answer (tutor only):** 1-A, 2-B, 3-C, 4-D, 5-E
- **Explanation (tutor only):** df model = groups - 1 = 3. df residual = n - groups = 30 - 4 = 26. MS model = 5 / 3 = 1.67. MS residual = 52 / 26 = 2. F = 1.67 / 2 = 0.83.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: residual df = n - 1 (29), or F = SS model / SS residual (0.096).
- **Hint:** Mean square = sum of squares / df; F = MS model / MS residual.

### ch18-quiz-01-v1
- **Kind:** AI-written version of ch18-quiz-01
- **Concepts:** ANOVA calculations
- **Type:** matching
- **Question:**

A study has 25 samples spread across 5 groups. Complete its ANOVA table:

source | df | Sum Sq | Mean Sq | F
Model | [A] | 20 | [C] | [E]
Residuals | [B] | 40 | [D] |

Match each missing entry to its value:

1. [A] model df
2. [B] residual df
3. [C] model mean square
4. [D] residual mean square
5. [E] F

- **Options:**

  A) 4
  B) 20
  C) 5
  D) 2
  E) 2.5

- **Answer (tutor only):** 1-A, 2-B, 3-C, 4-D, 5-E
- **Explanation (tutor only):** df model = 5 - 1 = 4. df residual = 25 - 5 = 20. MS model = 20 / 4 = 5. MS residual = 40 / 20 = 2. F = 5 / 2 = 2.5.
- **Why the wrong options are wrong (tutor only):**
  Mean square = SS / df.
- **Hint:** Start with the degrees of freedom.

### ch18-quiz-01-v2
- **Kind:** AI-written version of ch18-quiz-01
- **Concepts:** ANOVA calculations
- **Type:** matching
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

lm(bodyTemperature ~ crabType, data = crabs) |> anova()

          Df Sum Sq Mean Sq F value    Pr(>F)
crabType   3 1.9964 0.66546  14.654 1.521e-07
Residuals 72 3.2696 0.04541

Match each quantity to how it was calculated:

1. 3 (crabType df)
2. 72 (Residuals df)
3. 0.66546 (crabType Mean Sq)
4. 14.654 (F value)

- **Options:**

  A) Number of groups - 1
  B) Number of crabs - number of groups
  C) Sum Sq / Df for crabType
  D) Mean Sq crabType / Mean Sq Residuals

- **Answer (tutor only):** 1-A, 2-B, 3-C, 4-D
- **Explanation (tutor only):** df model = 4 - 1 = 3; df residual = 76 - 4 = 72; MS = 1.9964 / 3; F = 0.66546 / 0.04541.
- **Why the wrong options are wrong (tutor only):**
  Follow the ANOVA table's logic left to right.
- **Hint:** df, then SS / df, then the ratio.

### ch18-quiz-02
- **Kind:** Course original
- **Concepts:** ANOVA in R
- **Type:** MC
- **Question:**

A study of 30 samples in 4 groups gives F = 0.83 (3 and 26 df), p = 0.48. What do you do to the null hypothesis at α = 0.05?

- **Options:**

  A) Reject it
  B) Fail to reject it
  C) Accept it

- **Answer (tutor only):** B
- **Explanation (tutor only):** p = 0.48 > 0.05. An F below 1 means the groups differ less than we'd expect by chance alone.
- **Why the wrong options are wrong (tutor only):**
  A) p is far above α.
  C) We never accept the null.
- **Hint:** Compare p with α.

### ch18-quiz-02-v1
- **Kind:** AI-written version of ch18-quiz-02
- **Concepts:** ANOVA in R
- **Type:** MC
- **Question:**

A study of 25 samples in 5 groups gives F = 2.5 (4 and 20 df). In R:

pf(2.5, df1 = 4, df2 = 20, lower.tail = FALSE)
[1] 0.075

What do you do to the null hypothesis at α = 0.05?

- **Options:**

  A) Reject it
  B) Fail to reject it
  C) Accept it
  D) Fail to accept it

- **Answer (tutor only):** B
- **Explanation (tutor only):** p = 0.075 > 0.05, so we fail to reject. (We never 'accept' the null.)
- **Why the wrong options are wrong (tutor only):**
  A) p > α.
  C) and D) We never accept the null.
- **Hint:** Compare p with 0.05.

### ch18-quiz-02-v2
- **Kind:** AI-written version of ch18-quiz-02
- **Concepts:** ANOVA in R
- **Type:** MC
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

lm(bodyTemperature ~ crabType, data = crabs) |> anova()

          Df Sum Sq Mean Sq F value    Pr(>F)
crabType   3 1.9964 0.66546  14.654 1.521e-07
Residuals 72 3.2696 0.04541

What do you do to the null hypothesis at α = 0.01?

- **Options:**

  A) Reject it
  B) Fail to reject it
  C) Accept it

- **Answer (tutor only):** A
- **Explanation (tutor only):** p = 1.5 × 10⁻⁷ is far below 0.01.
- **Why the wrong options are wrong (tutor only):**
  B) p < α.
  C) We never accept the null.
- **Hint:** Compare p with 0.01.

### ch18-quiz-03
- **Kind:** Course original
- **Concepts:** ANOVA calculations
- **Type:** numeric
- **Question:**

In an ANOVA, SS model = 5 and SS residual = 52. What proportion of the variance in the response does the model explain in this study (R²)?

- **Answer (tutor only):** 0.088
- **Explanation (tutor only):** R² = SS model / SS total = 5 / (5 + 52) = 5 / 57 = 0.088.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: SS model / SS residual (5 / 52 = 0.096). The denominator is the total.
- **Hint:** SS total = SS model + SS residual.

### ch18-quiz-03-v1
- **Kind:** AI-written version of ch18-quiz-03
- **Concepts:** ANOVA calculations
- **Type:** numeric
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed.

lm(bodyTemperature ~ crabType, data = crabs) |> anova()

          Df Sum Sq Mean Sq F value    Pr(>F)
crabType   3 1.9964 0.66546  14.654 1.521e-07
Residuals 72 3.2696 0.04541

What proportion of the variance in heat gain does crab type explain in this study (R²)? Report it to three decimals.

- **Answer (tutor only):** 0.379
- **Explanation (tutor only):** R² = 1.9964 / (1.9964 + 3.2696) = 1.9964 / 5.266 = 0.379.
- **Hint:** SS model / SS total.

### ch18-quiz-03-v2
- **Kind:** AI-written version of ch18-quiz-03
- **Concepts:** ANOVA calculations
- **Type:** numeric
- **Question:**

To ask whether brood-parasitic cuckoos adjust their eggs to match their hosts, researchers measured the length of cuckoo eggs (mm) laid in the nests of six host species.

lm(egg_length ~ host_species, data = cuckoo) |> anova()

              Df Sum Sq Mean Sq F value    Pr(>F)
host_species   5 42.940  8.5879  10.388 3.152e-08
Residuals    114 94.248  0.8267

What proportion of the variance in cuckoo egg length does host species explain in this study (R²)? Report it to three decimals.

- **Answer (tutor only):** 0.313
- **Explanation (tutor only):** R² = 42.940 / (42.940 + 94.248) = 42.940 / 137.188 = 0.313.
- **Hint:** SS model / SS total.

### ch18-quiz-04
- **Kind:** Course original
- **Concepts:** ANOVA calculations
- **Type:** TF
- **Question:**

An ANOVA in one study gives R² = 0.088. TRUE or FALSE: the explanatory variable explains 8.8% of the variation in the response in nature.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** R² describes this study only. It depends on which groups were included, how many samples were in each, and the conditions of the study, so it doesn't carry over to nature.
- **Why the wrong options are wrong (tutor only):**
  TRUE: R² can't be extrapolated beyond the study that produced it.
- **Hint:** Would R² change if the study had sampled different groups, or different numbers per group?

### ch18-quiz-04-v1
- **Kind:** AI-written version of ch18-quiz-04
- **Concepts:** ANOVA calculations
- **Type:** TF
- **Question:**

To test whether a male fiddler crab's huge "major" claw works as a heat sink, Darnell and Munguia (2011) heated four groups of crabs and measured their rate of heat gain (bodyTemperature): females, intact males, males with the major claw removed, and males with the minor claw removed. An ANOVA gives R² = 0.38. TRUE or FALSE: If the researchers had included only females and intact males, R² would necessarily stay 0.38.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** R² depends on which groups are in the study. Changing the groups changes how much variation they explain.
- **Why the wrong options are wrong (tutor only):**
  TRUE: R² is study-specific.
- **Hint:** Does R² depend on the design?

### ch18-quiz-04-v2
- **Kind:** AI-written version of ch18-quiz-04
- **Concepts:** ANOVA calculations
- **Type:** TF
- **Question:**

An ANOVA in one greenhouse study gives R² = 0.65 for fertilizer treatment. TRUE or FALSE: fertilizer explains 65% of the variation in plant growth among wild plants.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** R² describes this study's treatments and conditions, not variation in nature.
- **Why the wrong options are wrong (tutor only):**
  TRUE: R² doesn't transfer to nature.
- **Hint:** Is the greenhouse nature?

### ch18-quiz-05
- **Kind:** Course original
- **Concepts:** Assumptions & diagnostics
- **Type:** select-all
- **Question:**

Which of the following are assumptions of an ANOVA? (Select all that apply.)

- **Options:**

  A) Random and independent values of the response variable (conditional on the explanatory variable)
  B) Normal distributions (of residuals) for each population
  C) Equal variances for all groups
  D) The frequency of each group in the study is proportional to its frequency in nature

- **Answer (tutor only):** A, B, C
- **Explanation (tutor only):** ANOVA assumes independent, unbiased data, normally distributed residuals, and equal variance among groups. Group sizes don't need to match nature.
- **Why the wrong options are wrong (tutor only):**
  D) Sample sizes per group are a design choice, not an assumption (though they do affect R²).
- **Hint:** Which option is about study design rather than the data-generating process?

### ch18-quiz-05-v1
- **Kind:** AI-written version of ch18-quiz-05
- **Concepts:** Assumptions & diagnostics
- **Type:** select-all
- **Question:**

Which of the following are NOT assumptions of an ANOVA? (Select all that apply.)

- **Options:**

  A) Each group has the same number of samples
  B) The response variable itself is normally distributed overall
  C) Residuals are normally distributed within groups
  D) Groups have roughly equal variances

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** ANOVA doesn't need equal sample sizes (though they help), and it's the residuals, not the overall response, that should be normal.
- **Why the wrong options are wrong (tutor only):**
  C) and D) are assumptions.
- **Hint:** Residuals vs raw data.

### ch18-quiz-05-v2
- **Kind:** AI-written version of ch18-quiz-05
- **Concepts:** Assumptions & diagnostics
- **Type:** select-all
- **Question:**

A researcher measures 10 leaves from each of 3 trees per treatment, and runs an ANOVA treating all 30 leaves per treatment as independent. Which ANOVA assumption is violated? (Select all that apply.)

- **Options:**

  A) Independence of observations
  B) Equal variance among groups
  C) Normality of residuals
  D) Equal sample sizes

- **Answer (tutor only):** A
- **Explanation (tutor only):** Leaves from the same tree are not independent; the real replicates are trees.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Nothing suggests these are violated.
  D) Not an ANOVA assumption.
- **Hint:** Are leaves on the same tree independent?

### ch18-quiz-06
- **Kind:** Course original
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** MC
- **Question:**

After you reject the null hypothesis in an ANOVA, you:

- **Options:**

  A) Assume all group means differ, while acknowledging this could be a false positive
  B) Conduct standard t-tests between all pairs to find out which groups differ
  C) Conduct post-hoc tests to see which means differ

- **Answer (tutor only):** C
- **Explanation (tutor only):** Rejecting the ANOVA null says not all means are equal, not that all differ. Post-hoc tests (e.g. Tukey) find which pairs differ while controlling the overall false positive rate.
- **Why the wrong options are wrong (tutor only):**
  A) Rejecting doesn't mean every mean differs.
  B) Uncorrected pairwise t-tests bring back the multiple testing problem.
- **Hint:** What does the ANOVA's alternative hypothesis actually say?

### ch18-quiz-06-v1
- **Kind:** AI-written version of ch18-quiz-06
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** MC
- **Question:**

After an ANOVA comparing five diets rejects the null, a student runs 10 standard t-tests between all pairs at α = 0.05. What's the problem?

- **Options:**

  A) The chance of at least one false positive is well above 5%
  B) Standard t-tests can't be used with five groups of data
  C) The ANOVA already shows that all five diets differ
  D) Nothing; this is the standard post-hoc procedure

- **Answer (tutor only):** A
- **Explanation (tutor only):** Ten tests at α = 0.05 inflate the family-wise false positive rate. Post-hoc tests like Tukey's control it.
- **Why the wrong options are wrong (tutor only):**
  B) They can be run; that's the problem.
  C) ANOVA shows not all are equal.
  D) Use a post-hoc test.
- **Hint:** Multiple testing.

### ch18-quiz-06-v2
- **Kind:** AI-written version of ch18-quiz-06
- **Concepts:** Multiple testing & post-hoc tests
- **Type:** MC
- **Question:**

What does a post-hoc test (like Tukey's) do after an ANOVA?

- **Options:**

  A) Compares pairs of groups while controlling overall false positives
  B) Tests whether the ANOVA's assumptions are met by the data
  C) Recalculates the ANOVA's F using only the largest groups
  D) Tells us whether all group means differ from one another

- **Answer (tutor only):** A
- **Explanation (tutor only):** Post-hoc tests identify which pairs differ, adjusting for the number of comparisons.
- **Why the wrong options are wrong (tutor only):**
  B) That's diagnostics.
  C) Not what it does.
  D) It identifies which pairs differ.
- **Hint:** Which groups differ?

### ch18-quiz-08
- **Kind:** Course original
- **Concepts:** ANOVA calculations; ANOVA in R
- **Type:** MC
- **Question:**

A student wrote this code to calculate an ANOVA by hand (on PLP1 gene expression across groups of patients):

summarise(n_group = n_distinct(group), n_total = n(),
          df_group = n_group - 1,
          df_error = n_total - n_group,
          ss_group = sum(group_sqrd_dev),
          ss_error = sum(error_sqrd_dev),
          ms_group = ss_group / df_group,
          ms_error = ss_error / df_error,
          f_val = ss_group / ss_error,
          p_val = pf(q = f_val, df1 = df_group, df2 = df_error, lower.tail = FALSE))

Which line has a mistake?

- **Options:**

  A) df_error = n_total - n_group
  B) ms_group = ss_group / df_group
  C) f_val = ss_group / ss_error
  D) p_val = pf(q = f_val, df1 = df_group, df2 = df_error, lower.tail = FALSE)

- **Answer (tutor only):** C
- **Explanation (tutor only):** F is a ratio of mean squares, not sums of squares: f_val = ms_group / ms_error.
- **Why the wrong options are wrong (tutor only):**
  A) Correct: error df = n - number of groups.
  B) Correct.
  D) Correct: F tests use the upper tail.
- **Hint:** Is F a ratio of sums of squares or of mean squares?

### ch18-quiz-08-v1
- **Kind:** AI-written version of ch18-quiz-08
- **Concepts:** ANOVA calculations; ANOVA in R
- **Type:** MC
- **Question:**

A student wrote this code to calculate an ANOVA by hand:

summarise(n_group = n_distinct(group), n_total = n(),
          df_group = n_group - 1,
          df_error = n_total - 1,
          ss_group = sum(group_sqrd_dev),
          ss_error = sum(error_sqrd_dev),
          ms_group = ss_group / df_group,
          ms_error = ss_error / df_error,
          f_val = ms_group / ms_error)

Which line has a mistake?

- **Options:**

  A) df_group = n_group - 1
  B) df_error = n_total - 1
  C) ms_group = ss_group / df_group
  D) f_val = ms_group / ms_error

- **Answer (tutor only):** B
- **Explanation (tutor only):** Error df = n_total - n_group (one df lost per group mean), not n_total - 1.
- **Why the wrong options are wrong (tutor only):**
  A), C) and D) are correct.
- **Hint:** How many means are estimated?

### ch18-quiz-08-v2
- **Kind:** AI-written version of ch18-quiz-08
- **Concepts:** ANOVA calculations; ANOVA in R
- **Type:** MC
- **Question:**

A student wrote this code to calculate an ANOVA p-value:

p_val = pf(q = f_val, df1 = df_group, df2 = df_error)

What's wrong?

- **Options:**

  A) It returns the lower tail; it needs lower.tail = FALSE
  B) df1 and df2 are swapped; df1 should be df_error
  C) pf() should be pt(), since this is a t-test
  D) Nothing; this gives the correct p-value

- **Answer (tutor only):** A
- **Explanation (tutor only):** By default pf() returns the area below F. The p-value is the area above.
- **Why the wrong options are wrong (tutor only):**
  B) df1 = model df is right.
  C) It's an F test.
  D) It gives 1 - p.
- **Hint:** Which tail is the p-value?

### ch18-quiz-09
- **Kind:** Course original
- **Concepts:** Multiple testing & post-hoc tests; ANOVA in R
- **Type:** MC
- **Question:**

Pea aphids can carry the bacterium Rickettsiella, which may change their body color. Researchers compared color among aphids that never had the bacterium (original), aphids born infected to lab-infected mothers (infected), and aphids born uninfected to lab-infected mothers (uninfected).

aov(color ~ infectionStatus, data = rickettsia) |> summary()
                Df Sum Sq Mean Sq F value   Pr(>F)
infectionStatus  2 2379.3  1189.6   65.59 1.73e-11
Residuals       29  525.9    18.1

aov(color ~ infectionStatus, data = rickettsia) |> TukeyHSD()
comparison | diff | lwr | upr | p adj
original - infected | -17.3 | -21.7 | -12.9 | < 0.0001
uninfected - infected | -19.2 | -23.9 | -14.4 | < 0.0001
uninfected - original | -1.9 | -6.5 | 2.8 | 0.58

Which summary is correct?

- **Options:**

  A) Infection status didn't affect color (p = 0.58)
  B) All three groups differ significantly from each other in color
  C) Infected differ from the other two, which don't differ from each other
  D) Original aphids differ in color from the other two groups

- **Answer (tutor only):** C
- **Explanation (tutor only):** The ANOVA rejects equal means (F = 65.6, df = 2 and 29, p = 1.7 × 10⁻¹¹). The Tukey tests show infected aphids differ from both other groups, which don't differ from each other.
- **Why the wrong options are wrong (tutor only):**
  A) 0.58 is the p-value for just one pair; the overall ANOVA is highly significant.
  B) Original vs uninfected isn't significant.
  D) The odd group out is infected, not original.
- **Hint:** Look at the Tukey table: which comparisons have small p-values?

### ch18-quiz-09-v1
- **Kind:** AI-written version of ch18-quiz-09
- **Concepts:** Multiple testing & post-hoc tests; ANOVA in R
- **Type:** MC
- **Question:**

Pea aphids can carry the bacterium Rickettsiella, which may change their body color. Researchers compared color among aphids that never had the bacterium (original), aphids born infected to lab-infected mothers (infected), and aphids born uninfected to lab-infected mothers (uninfected).

Tukey HSD:
comparison | diff | lwr | upr | p adj
original - infected | -17.3 | -21.7 | -12.9 | < 0.0001
uninfected - infected | -19.2 | -23.9 | -14.4 | < 0.0001
uninfected - original | -1.9 | -6.5 | 2.8 | 0.58

If infected aphids are in significance group 'a', which group letters do original and uninfected aphids get?

- **Options:**

  A) Both are 'b'
  B) Original is 'b'; uninfected is 'c'
  C) Both are 'a'
  D) Original is 'a'; uninfected is 'b'

- **Answer (tutor only):** A
- **Explanation (tutor only):** Both differ from infected, but not from each other, so they share a letter.
- **Why the wrong options are wrong (tutor only):**
  B) They don't differ from each other.
  C) They differ from infected.
  D) Original differs from infected.
- **Hint:** Same letter = not significantly different.

### ch18-quiz-09-v2
- **Kind:** AI-written version of ch18-quiz-09
- **Concepts:** Multiple testing & post-hoc tests; ANOVA in R
- **Type:** MC
- **Question:**

Pea aphids can carry the bacterium Rickettsiella, which may change their body color. Researchers compared color among aphids that never had the bacterium (original), aphids born infected to lab-infected mothers (infected), and aphids born uninfected to lab-infected mothers (uninfected).

Tukey HSD:
comparison | diff | lwr | upr | p adj
original - infected | -17.3 | -21.7 | -12.9 | < 0.0001
uninfected - infected | -19.2 | -23.9 | -14.4 | < 0.0001
uninfected - original | -1.9 | -6.5 | 2.8 | 0.58

Which comparison's confidence interval includes zero?

- **Options:**

  A) uninfected - original
  B) original - infected
  C) uninfected - infected
  D) None of the three

- **Answer (tutor only):** A
- **Explanation (tutor only):** (-6.5, 2.8) includes 0, matching its non-significant p of 0.58.
- **Why the wrong options are wrong (tutor only):**
  B) and C) are entirely below 0.
- **Hint:** Look at lwr and upr.

## Chapter 19: Regression

### ch19-book-01
- **Kind:** Course original
- **Concepts:** Confidence & prediction intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-book-regression.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-book-regression.png)
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

The grey band is a 95% confidence interval. What does it mean?

- **Options:**

  A) 95% of data points should fall in that region
  B) The true mean proportion hybrid seed, conditional on visits, is plausibly within this region
  C) 95% of future observations should fall in that region
  D) There is a 95% chance that the true mean proportion hybrid seed, conditional on visits, is within this region

- **Answer (tutor only):** B
- **Explanation (tutor only):** A confidence band describes uncertainty in the mean response at each x: a range of plausible values for the true line.
- **Why the wrong options are wrong (tutor only):**
  A) and C) Those describe individual observations (a prediction interval).
  D) Treats the 95% as a probability about this one band.
- **Hint:** Is the band about the line or about individual RILs?

### ch19-book-01-v1
- **Kind:** AI-written version of ch19-book-01
- **Concepts:** Confidence & prediction intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-book-regression.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-book-regression.png)
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

The grey band is a 95% confidence interval. If we instead drew a 95% prediction interval, how would it compare?

- **Options:**

  A) Wider: it adds individual scatter
  B) Narrower: it ignores uncertainty
  C) The same: they're two names for one band
  D) It would only cover the mean x value

- **Answer (tutor only):** A
- **Explanation (tutor only):** Prediction intervals include both uncertainty in the line and scatter of individuals.
- **Why the wrong options are wrong (tutor only):**
  B) It's wider.
  C) They're different.
  D) It spans all x.
- **Hint:** Individuals vary more than means.

### ch19-book-01-v2
- **Kind:** AI-written version of ch19-book-01
- **Concepts:** Confidence & prediction intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-book-regression.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-book-regression.png)
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

The grey band is a 95% confidence interval. Which statement is correct?

- **Options:**

  A) 95% of bands made this way contain the true line
  B) 95% of the 49 RILs fall inside the grey band
  C) 95% of future RILs will fall in the grey band
  D) The band shows where the residuals fall

- **Answer (tutor only):** A
- **Explanation (tutor only):** Like any CI, the 95% describes the procedure: intervals built this way usually capture the true mean response.
- **Why the wrong options are wrong (tutor only):**
  B) and C) That's about individuals.
  D) Residuals aren't plotted.
- **Hint:** CIs are about the mean.

### ch19-book-02
- **Kind:** Course original
- **Concepts:** Slopes, intercepts & predictions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-book-regression.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-book-regression.png)
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

Visually estimate the intercept and slope of the blue line.

- **Options:**

  A) Intercept ≈ 0.2, slope ≈ 0.27
  B) Intercept ≈ 0.2, slope ≈ 0.73
  C) Intercept ≈ 0, slope ≈ 0.27
  D) Intercept ≈ 0.73, slope ≈ 0.2

- **Answer (tutor only):** A
- **Explanation (tutor only):** The line starts near 0.2 at zero visits and rises to about 0.73 at 2 visits: (0.73 - 0.2) / 2 ≈ 0.27 per visit. The fitted values are 0.208 and 0.262.
- **Why the wrong options are wrong (tutor only):**
  B) 0.73 is the height at x = 2, not the slope.
  C) The line doesn't start at zero.
  D) Swaps them.
- **Hint:** Slope = rise / run between two points on the line.

### ch19-book-02-v1
- **Kind:** AI-written version of ch19-book-02
- **Concepts:** Slopes, intercepts & predictions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-book-regression.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-book-regression.png)
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

Based on the blue line, roughly what proportion of hybrid seed is predicted for a RIL with 1 visit per session?

- **Options:**

  A) About 0.47
  B) About 0.21
  C) About 0.73
  D) About 0.26

- **Answer (tutor only):** A
- **Explanation (tutor only):** 0.208 + 0.262 × 1 = 0.47.
- **Why the wrong options are wrong (tutor only):**
  B) That's the intercept (0 visits).
  C) That's at 2 visits.
  D) That's the slope.
- **Hint:** Intercept + slope × 1.

### ch19-book-02-v2
- **Kind:** AI-written version of ch19-book-02
- **Concepts:** Slopes, intercepts & predictions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-book-regression.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-book-regression.png)
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

Is the slope of the blue line positive or negative, and what does that mean?

- **Options:**

  A) Positive: RILs with more visits set more hybrid seed
  B) Negative: RILs with more visits set less hybrid seed
  C) Zero: visits are unrelated to hybrid seed
  D) Positive: more hybrid seed causes more visits

- **Answer (tutor only):** A
- **Explanation (tutor only):** The line rises with visits.
- **Why the wrong options are wrong (tutor only):**
  B) and C) The line rises.
  D) Reverses cause and effect; regression shows association.
- **Hint:** Does the line go up or down?

### ch19-book-03
- **Kind:** Course original
- **Concepts:** Slopes, intercepts & predictions
- **Type:** matching
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

Sample size 49; covariance between visits and proportion hybrid = 0.039.

variable | mean | var | sd
prop_hybrid | 0.260 | 0.078 | 0.280
visits | 0.197 | 0.149 | 0.386

Match each quantity to its value:

1. The slope (change in proportion hybrid per extra visit)
2. The correlation

- **Options:**

  A) 0.26
  B) 0.36
  C) 0.04
  D) 0.78

- **Answer (tutor only):** 1-A, 2-B
- **Explanation (tutor only):** Slope = cov / var(visits) = 0.039 / 0.149 = 0.26. Correlation = cov / (sd_x × sd_y) = 0.039 / (0.386 × 0.280) = 0.36.
- **Why the wrong options are wrong (tutor only):**
  C) is the covariance. D) is unrelated here.
- **Hint:** Slope divides by the variance of x; correlation divides by both SDs.

### ch19-book-03-v1
- **Kind:** AI-written version of ch19-book-03
- **Concepts:** Slopes, intercepts & predictions
- **Type:** MC
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

Sample size 49; covariance between visits and proportion hybrid = 0.039.

variable | mean | var | sd
prop_hybrid | 0.260 | 0.078 | 0.280
visits | 0.197 | 0.149 | 0.386

Using the slope (0.26), what is the intercept of the regression of proportion hybrid on visits?

- **Options:**

  A) About 0.21
  B) About 0.26
  C) About 0.05
  D) About 0.36

- **Answer (tutor only):** A
- **Explanation (tutor only):** a = mean(y) - b × mean(x) = 0.260 - 0.26 × 0.197 = 0.209.
- **Why the wrong options are wrong (tutor only):**
  B) That's mean y.
  C) That's b × mean x.
  D) That's the correlation.
- **Hint:** The line passes through the means.

### ch19-book-03-v2
- **Kind:** AI-written version of ch19-book-03
- **Concepts:** Slopes, intercepts & predictions
- **Type:** MC
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

Sample size 49; covariance between visits and proportion hybrid = 0.039.

variable | mean | var | sd
prop_hybrid | 0.260 | 0.078 | 0.280
visits | 0.197 | 0.149 | 0.386

What is R²?

- **Options:**

  A) About 0.13
  B) About 0.36
  C) About 0.26
  D) About 0.60

- **Answer (tutor only):** A
- **Explanation (tutor only):** R² = r² = 0.36² = 0.13.
- **Why the wrong options are wrong (tutor only):**
  B) That's r.
  C) That's the slope.
  D) That's √0.36.
- **Hint:** Square the correlation.

### ch19-book-04
- **Kind:** Course original
- **Concepts:** Slopes, intercepts & predictions; Sums of squares, F & R²
- **Type:** MC
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

The intercept is 0.208 (SE 0.042, p = 1.1 × 10⁻⁵). Why don't we care about this p-value?

- **Options:**

  A) Because a p-value this small is probably wrong
  B) It tests a null (no hybrid seed at zero visits) no one proposed
  C) Because p-values are P(data | model), not P(model | data)
  D) We do care: it shows visits affect hybrid seed

- **Answer (tutor only):** B
- **Explanation (tutor only):** The intercept's p-value tests whether the predicted hybrid proportion at zero visits is zero. That's not a biological question anyone asked, and several RILs with no observed visits already set hybrid seed.
- **Why the wrong options are wrong (tutor only):**
  A) Small p-values aren't wrong for being small.
  C) True of all p-values, so it doesn't single out this one.
  D) It tests an uninteresting null.
- **Hint:** What null hypothesis does the intercept's p-value test?

### ch19-book-04-v1
- **Kind:** AI-written version of ch19-book-04
- **Concepts:** Slopes, intercepts & predictions; Sums of squares, F & R²
- **Type:** MC
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

The slope is 0.262 (SE 0.098, p = 0.011). What null hypothesis does the slope's p-value test?

- **Options:**

  A) That proportion hybrid doesn't change with visits
  B) That RILs with zero visits set no hybrid seed
  C) That the mean proportion hybrid is zero
  D) That visits explain all the variation

- **Answer (tutor only):** A
- **Explanation (tutor only):** The slope's p-value tests whether the true slope is zero: the biologically interesting question.
- **Why the wrong options are wrong (tutor only):**
  B) That's the intercept's test.
  C) Not this test.
  D) Not a null hypothesis we test.
- **Hint:** Slope = 0.

### ch19-book-04-v2
- **Kind:** AI-written version of ch19-book-04
- **Concepts:** Slopes, intercepts & predictions; Sums of squares, F & R²
- **Type:** MC
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

In summary() output, which p-value is biologically interesting here?

- **Options:**

  A) The slope's: it asks whether hybrid seed changes with visits
  B) The intercept's: it asks if hybrid seed is zero at zero visits
  C) Both are equally interesting for the biological question
  D) Neither; p-values are never interesting in a regression

- **Answer (tutor only):** A
- **Explanation (tutor only):** The slope tests the relationship we care about; the intercept tests a null nobody proposed.
- **Why the wrong options are wrong (tutor only):**
  B) Not a question anyone asked.
  C) The intercept's test is irrelevant here.
  D) The slope's test is useful.
- **Hint:** What's the research question?

### ch19-book-05
- **Kind:** Course original
- **Concepts:** Slopes, intercepts & predictions
- **Type:** numeric
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

The fitted model is prop_hybrid = 0.208 + 0.262 × visits. Predict the proportion hybrid seed for a RIL that received half a visit (on average) per observation session.

- **Answer (tutor only):** 0.339
- **Explanation (tutor only):** 0.208 + 0.262 × 0.5 = 0.208 + 0.131 = 0.339.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: forgetting the intercept (0.131).
- **Hint:** Prediction = intercept + slope × x.

### ch19-book-05-v1
- **Kind:** AI-written version of ch19-book-05
- **Concepts:** Slopes, intercepts & predictions
- **Type:** numeric
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

The fitted model is prop_hybrid = 0.208 + 0.262 × visits. Predict the proportion hybrid seed for a RIL that received 1.5 visits per session.

- **Answer (tutor only):** 0.601
- **Explanation (tutor only):** 0.208 + 0.262 × 1.5 = 0.601.
- **Hint:** Intercept + slope × 1.5.

### ch19-book-05-v2
- **Kind:** AI-written version of ch19-book-05
- **Concepts:** Slopes, intercepts & predictions
- **Type:** numeric
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

The fitted model is prop_hybrid = 0.208 + 0.262 × visits. A RIL with 0.5 visits per session set 0.10 hybrid seed. What is its residual?

- **Answer (tutor only):** -0.239
- **Explanation (tutor only):** Prediction = 0.339; residual = 0.10 - 0.339 = -0.239.
- **Hint:** Observed - predicted.

### ch19-book-06
- **Kind:** Course original
- **Concepts:** Slopes, intercepts & predictions
- **Type:** MC
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

Visits in these data ranged from 0 to 2 per observation session. Should we predict the proportion hybrid seed for a RIL with 3 visits per session?

- **Options:**

  A) Yes: 0.208 + 0.262 × 3 = 0.994
  B) No: 3 visits is beyond our data, so it's an extrapolation
  C) Yes, but only if we report it with a prediction interval

- **Answer (tutor only):** B
- **Explanation (tutor only):** Our data stop at 2 visits. The prediction (0.99) is close to the maximum possible proportion, a sign that the straight line can't continue far beyond the data.
- **Why the wrong options are wrong (tutor only):**
  A) The arithmetic works, but the prediction isn't trustworthy.
  C) A prediction interval doesn't fix extrapolation.
- **Hint:** What range of visits did we observe?

### ch19-book-06-v1
- **Kind:** AI-written version of ch19-book-06
- **Concepts:** Slopes, intercepts & predictions
- **Type:** MC
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

Visits ranged from 0 to 2 per session. Which prediction is NOT an extrapolation?

- **Options:**

  A) For a RIL with 1.2 visits
  B) For a RIL with 2.5 visits
  C) For a RIL with 4 visits
  D) For a RIL with -1 visits

- **Answer (tutor only):** A
- **Explanation (tutor only):** 1.2 is within the observed range (0 to 2).
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) are outside it.
- **Hint:** Inside 0 to 2?

### ch19-book-06-v2
- **Kind:** AI-written version of ch19-book-06
- **Concepts:** Slopes, intercepts & predictions
- **Type:** MC
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

The model predicts 1.26 for a RIL with 4 visits per session. What does this show?

- **Options:**

  A) A straight line can't hold far beyond the data
  B) RILs with 4 visits set more seed than they make
  C) The slope must have been estimated incorrectly
  D) Nothing; the prediction is perfectly reasonable

- **Answer (tutor only):** A
- **Explanation (tutor only):** A proportion can't exceed 1. Extrapolating beyond 2 visits breaks the model.
- **Why the wrong options are wrong (tutor only):**
  B) That's impossible.
  C) The slope is fine within the data.
  D) It's impossible.
- **Hint:** Can a proportion exceed 1?

### ch19-book-07
- **Kind:** Course original
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-book-diagnostics.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-book-diagnostics.png)
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

The diagnostic plots for lm(prop_hybrid ~ visits) are shown. Which assumption seems most problematic, and how would you move forward?

- **Options:**

  A) Normality of residuals and equal variance; treat the model as a useful first summary but check robustness (bootstrap or permutation, and refitting without influential points)
  B) Independence, because the plots prove nearby plants influenced each other; delete extreme points
  C) The existence of an intercept, because its p-value is small; report only the intercept
  D) Random sampling of x, because visits must be normally distributed; ignore the diagnostics

- **Answer (tutor only):** A
- **Explanation (tutor only):** The QQ plot bends away from the line and the residual spread changes with fitted values, which is typical for proportions with many zeros. A linear model is still a reasonable summary, but robustness checks are wise.
- **Why the wrong options are wrong (tutor only):**
  B) Diagnostic plots can't prove non-independence, and deleting points isn't a fix.
  C) Not an assumption.
  D) x doesn't need to be normal.
- **Hint:** Look at the QQ plot and at whether residual spread changes across fitted values.

### ch19-book-07-v1
- **Kind:** AI-written version of ch19-book-07
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-book-diagnostics.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-book-diagnostics.png)
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

The diagnostic plots for lm(prop_hybrid ~ visits) are shown. Why are non-normal residuals and unequal variance common for proportion data like these?

- **Options:**

  A) Proportions are bounded (0 to 1) and often pile up at zero
  B) Proportions are always perfectly normally distributed
  C) Pollinator visits can't be measured at all precisely
  D) Small sample sizes always produce perfect diagnostics

- **Answer (tutor only):** A
- **Explanation (tutor only):** Bounded responses with many zeros produce skewed residuals and variance that changes with the mean.
- **Why the wrong options are wrong (tutor only):**
  B) They often aren't.
  C) Measurement precision isn't the main issue.
  D) Not true.
- **Hint:** What values can a proportion take?

### ch19-book-07-v2
- **Kind:** AI-written version of ch19-book-07
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-book-diagnostics.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-book-diagnostics.png)
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

The diagnostic plots for lm(prop_hybrid ~ visits) are shown. Which plot is most useful for spotting unequal variance?

- **Options:**

  A) The scale-location plot
  B) The QQ plot of residuals
  C) A histogram of visits
  D) Residuals vs leverage

- **Answer (tutor only):** A
- **Explanation (tutor only):** Unequal variance shows up as spread that changes with fitted values, in the scale-location (or residuals vs fitted) plot.
- **Why the wrong options are wrong (tutor only):**
  B) QQ plots address normality.
  C) Not a diagnostic of residuals.
  D) That's for influence.
- **Hint:** Spread vs fitted values.

### ch19-book-08
- **Kind:** Course original
- **Concepts:** Assumptions & diagnostics
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-book-diagnostics.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-book-diagnostics.png)
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

Using the labeled points in the diagnostic plots, match each description to a data point:

1. The greatest outlier (largest residual)
2. The most influential point (high leverage and large residual)

- **Options:**

  A) 34
  B) 13
  C) 9
  D) 44

- **Answer (tutor only):** 1-A, 2-B
- **Explanation (tutor only):** Point 34 has the largest residual (top of the residuals and QQ plots). Point 13 has by far the highest leverage, with a sizable residual, so it pulls the line most (in the residuals vs leverage plot).
- **Why the wrong options are wrong (tutor only):**
  9 is a big residual but not the biggest; 44 has moderate leverage.
- **Hint:** Outliers are far from the line; influence also needs leverage (an extreme x).

### ch19-book-08-v1
- **Kind:** AI-written version of ch19-book-08
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-book-diagnostics.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-book-diagnostics.png)
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

Using the labeled points in the diagnostic plots, which point has by far the highest leverage?

- **Options:**

  A) 13
  B) 34
  C) 9
  D) 44

- **Answer (tutor only):** A
- **Explanation (tutor only):** Point 13 stands far to the right in the residuals vs leverage plot.
- **Why the wrong options are wrong (tutor only):**
  B) 34 has the largest residual, not leverage.
  C) and D) Lower leverage.
- **Hint:** Look at the x-axis of residuals vs leverage.

### ch19-book-08-v2
- **Kind:** AI-written version of ch19-book-08
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-book-diagnostics.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-book-diagnostics.png)
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

Using the labeled points in the diagnostic plots, what makes a point influential?

- **Options:**

  A) A combination of high leverage and a large residual
  B) A large residual alone, wherever its x value is
  C) A small residual combined with low leverage
  D) Being the first point in the dataset

- **Answer (tutor only):** A
- **Explanation (tutor only):** Influence (e.g. Cook's distance) depends on both leverage (unusual x) and the residual.
- **Why the wrong options are wrong (tutor only):**
  B) A large residual near mean x has little pull.
  C) That's a typical point.
  D) Order doesn't matter.
- **Hint:** Leverage × residual.

### ch19-book-09
- **Kind:** Course original
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Question:**

How would you check whether influential points are undermining your conclusions?

- **Options:**

  A) Remove every point with a large residual and refit the model
  B) Check whether the intercept p-value is still small
  C) Use only the plot with the nicest-looking regression line
  D) Refit without the influential point(s) and compare the results

- **Answer (tutor only):** D
- **Explanation (tutor only):** A sensitivity analysis: if conclusions change a lot without one or two points, report that they depend on those points.
- **Why the wrong options are wrong (tutor only):**
  A) Deleting inconvenient points is data manipulation.
  B) The intercept isn't the question.
  C) Cherry-picking.
- **Hint:** How would you see whether one point drives the result?

### ch19-book-09-v1
- **Kind:** AI-written version of ch19-book-09
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Question:**

After removing an influential point, the slope drops from 0.26 to 0.05 and is no longer significant. What should you report?

- **Options:**

  A) Both analyses, noting conclusions depend on that point
  B) Only the original analysis, since it was significant
  C) Only the new analysis, since the point was influential
  D) Neither; the data are unusable and must be discarded

- **Answer (tutor only):** A
- **Explanation (tutor only):** Transparency: say that the conclusion hinges on one point.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Hiding either is misleading.
  D) The data still tell us something.
- **Hint:** Sensitivity analysis.

### ch19-book-09-v2
- **Kind:** AI-written version of ch19-book-09
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Question:**

Which is a legitimate reason to remove a data point from an analysis?

- **Options:**

  A) It was a documented recording or measurement error
  B) It makes the p-value larger than you would like
  C) It has the largest residual in the regression
  D) It falls outside the confidence band of the line

- **Answer (tutor only):** A
- **Explanation (tutor only):** Points can be removed for documented errors, not because they're inconvenient.
- **Why the wrong options are wrong (tutor only):**
  B) That's p-hacking.
  C) and D) Large residuals are part of the data.
- **Hint:** Errors vs inconvenience.

### ch19-book-10
- **Kind:** Course original
- **Concepts:** Sums of squares, F & R²
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-book-deviations.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-book-deviations.png)
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

Each panel shows the RILs, the regression line (blue) and the mean proportion hybrid (black). Match each kind of deviation to its panel:

1. Model deviation
2. Total deviation
3. Residual deviation

- **Options:**

  A) Panel A
  B) Panel B
  C) Panel C

- **Answer (tutor only):** 1-C, 2-A, 3-B
- **Explanation (tutor only):** A: points to the mean (total). B: points to the line (residual). C: line to the mean (model).
- **Why the wrong options are wrong (tutor only):**
  Check where each line starts and ends.
- **Hint:** Which panel's lines never touch the points?

### ch19-book-10-v1
- **Kind:** AI-written version of ch19-book-10
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-book-deviations.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-book-deviations.png)
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

Each panel shows the RILs, the regression line (blue) and the mean proportion hybrid (black). Which panel's deviations, squared and summed, give SS error?

- **Options:**

  A) Panel A
  B) Panel B
  C) Panel C

- **Answer (tutor only):** B
- **Explanation (tutor only):** Panel B shows each point to the line (residuals).
- **Why the wrong options are wrong (tutor only):**
  A) Total.
  C) Model.
- **Hint:** Point to line.

### ch19-book-10-v2
- **Kind:** AI-written version of ch19-book-10
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-book-deviations.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-book-deviations.png)
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

Each panel shows the RILs, the regression line (blue) and the mean proportion hybrid (black). Which panel's deviations are largest for RILs with the most visits (far right)?

- **Options:**

  A) Panel C, since the line is farthest from the mean there
  B) Panel B, since residuals always grow with x
  C) None; model deviations are the same for every RIL
  D) Panel A, since total deviations never vary

- **Answer (tutor only):** A
- **Explanation (tutor only):** Model deviations (line minus mean) grow the farther x is from its mean.
- **Why the wrong options are wrong (tutor only):**
  B) Residuals needn't grow with x.
  C) In regression they vary with x.
  D) Total deviations vary point to point.
- **Hint:** Where is the line farthest from the mean?

### ch19-book-11
- **Kind:** Course original
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

lm(prop_hybrid ~ visits, data1) |> augment() |>
  summarise(ssa = sum((prop_hybrid - .fitted)^2),
            ssb = sum((.fitted - mean(prop_hybrid))^2),
            ssc = sum((prop_hybrid - mean(prop_hybrid))^2))

ssa = 3.26; ssb = 0.493; ssc = 3.76

Which statement is correct?

- **Options:**

  A) ssa is SS error, ssb is SS model, ssc is SS total, and R² = ssb / ssc = 0.13
  B) ssa is SS model, ssb is SS error, ssc is SS total, and R² = ssa / ssc = 0.87
  C) ssa is SS error, ssb is SS model, ssc is SS total, and R² = ssb / ssa = 0.15
  D) SS total = SS model / SS error

- **Answer (tutor only):** A
- **Explanation (tutor only):** SS total = SS model + SS error (0.493 + 3.26 = 3.76), and R² = SS model / SS total = 0.493 / 3.76 = 0.13.
- **Why the wrong options are wrong (tutor only):**
  B) Mixes up model and error.
  C) R² divides by SS total, not SS error.
  D) The SSs add; they don't divide.
- **Hint:** Which line compares observations to predictions?

### ch19-book-11-v1
- **Kind:** AI-written version of ch19-book-11
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

SS model = 0.493 and SS total = 3.76. What is SS error, and what is R²?

- **Options:**

  A) 3.26 and 0.13
  B) 4.25 and 0.13
  C) 3.26 and 0.87
  D) 0.493 and 0.15

- **Answer (tutor only):** A
- **Explanation (tutor only):** SS error = 3.76 - 0.493 = 3.27 ≈ 3.26. R² = 0.493 / 3.76 = 0.13.
- **Why the wrong options are wrong (tutor only):**
  B) Adds instead of subtracts.
  C) 0.87 is 1 - R².
  D) Wrong on both.
- **Hint:** Total = model + error.

### ch19-book-11-v2
- **Kind:** AI-written version of ch19-book-11
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

lm(prop_hybrid ~ visits, data1) |> augment() |>
  summarise(ssa = sum((prop_hybrid - .fitted)^2),
            ssb = sum((.fitted - mean(prop_hybrid))^2),
            ssc = sum((prop_hybrid - mean(prop_hybrid))^2))

ssa = 3.26; ssb = 0.493; ssc = 3.76

Which of these is the share of variation NOT explained by visits?

- **Options:**

  A) ssa / ssc = 0.87
  B) ssb / ssc = 0.13
  C) ssb / ssa = 0.15
  D) ssc / ssa = 1.15

- **Answer (tutor only):** A
- **Explanation (tutor only):** SS error / SS total = 3.26 / 3.76 = 0.87 = 1 - R².
- **Why the wrong options are wrong (tutor only):**
  B) That's R².
  C) and D) Not meaningful shares.
- **Hint:** Error / total.

### ch19-book-12
- **Kind:** Course original
- **Concepts:** Slopes, intercepts & predictions; Sums of squares, F & R²
- **Type:** MC
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

What is the null hypothesis for testing this regression?

- **Options:**

  A) The true slope relating pollinator visits to proportion hybrid seed is zero
  B) The true intercept is zero
  C) The observed number of pollinator visits is zero
  D) The model explains all variation in proportion hybrid seed

- **Answer (tutor only):** A
- **Explanation (tutor only):** The regression test asks whether the response changes with x at all, i.e. whether the true slope is zero.
- **Why the wrong options are wrong (tutor only):**
  B) That's the uninteresting intercept test.
  C) Not a hypothesis about a parameter.
  D) That would mean R² = 1.
- **Hint:** What would 'no relationship' look like for a line?

### ch19-book-12-v1
- **Kind:** AI-written version of ch19-book-12
- **Concepts:** Slopes, intercepts & predictions; Sums of squares, F & R²
- **Type:** MC
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

What is the alternative hypothesis (two-tailed) for testing this regression?

- **Options:**

  A) The true slope is not zero
  B) The true slope is positive
  C) The true intercept is not zero
  D) The observed slope is not zero

- **Answer (tutor only):** A
- **Explanation (tutor only):** Two-tailed: the response changes with visits in either direction.
- **Why the wrong options are wrong (tutor only):**
  B) One-tailed.
  C) Wrong parameter.
  D) Hypotheses are about true values.
- **Hint:** Two-tailed, about the slope.

### ch19-book-12-v2
- **Kind:** AI-written version of ch19-book-12
- **Concepts:** Slopes, intercepts & predictions; Sums of squares, F & R²
- **Type:** MC
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

If the null hypothesis (slope = 0) were true, what would the regression line look like in the population?

- **Options:**

  A) Flat, at the mean proportion hybrid
  B) Passing through the origin (0, 0)
  C) Rising steeply with visits
  D) Vertical, at mean visits

- **Answer (tutor only):** A
- **Explanation (tutor only):** Slope = 0 means predictions don't change with visits: a flat line at the mean.
- **Why the wrong options are wrong (tutor only):**
  B) That's intercept = 0.
  C) That's a positive slope.
  D) Not a regression line.
- **Hint:** What does slope = 0 mean?

### ch19-book-13
- **Kind:** Course original
- **Concepts:** Sums of squares, F & R²
- **Type:** numeric
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

SS model = 0.493 and SS error = 3.26, with N = 49. What is F?

- **Answer (tutor only):** 7.1
- **Explanation (tutor only):** df = 1 and 47. MS model = 0.493; MS error = 3.26 / 47 = 0.0694. F = 0.493 / 0.0694 = 7.1.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: using 48 or 49 for the error df.
- **Hint:** Error df = n - 2.

### ch19-book-13-v1
- **Kind:** AI-written version of ch19-book-13
- **Concepts:** Sums of squares, F & R²
- **Type:** numeric
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

SS model = 0.493 and SS error = 3.26, with N = 49. What is the mean square error? Report it to four decimals.

- **Answer (tutor only):** 0.0694
- **Explanation (tutor only):** MS error = 3.26 / 47 = 0.0694.
- **Hint:** SS error / (N - 2).

### ch19-book-13-v2
- **Kind:** AI-written version of ch19-book-13
- **Concepts:** Sums of squares, F & R²
- **Type:** numeric
- **Question:**

A regression on 22 points has SS model = 5.0 and SS error = 40.0. What is F?

- **Answer (tutor only):** 2.5
- **Explanation (tutor only):** df = 1 and 20. MS error = 40 / 20 = 2. F = 5 / 2 = 2.5.
- **Hint:** F = MS model / MS error.

### ch19-book-14
- **Kind:** Course original
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

F = 7.1 on 1 and 47 df gives p = 0.011. What do we do, and what does it mean?

- **Options:**

  A) Reject the null; pollinator visits definitely cause hybrid seed
  B) Reject the null; visits are associated with hybrid seed
  C) Fail to reject the null; there is no relationship at all
  D) Reject the null; the model explains all variation in hybrid seed

- **Answer (tutor only):** B
- **Explanation (tutor only):** p < 0.05, so we reject. That's evidence of an association, not proof of causation, and the model explains only about 13% of the variation.
- **Why the wrong options are wrong (tutor only):**
  A) An association isn't proof of causation.
  C) p is below 0.05.
  D) R² is only 0.13.
- **Hint:** What can, and can't, a significant regression tell you?

### ch19-book-14-v1
- **Kind:** AI-written version of ch19-book-14
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

F = 7.1 on 1 and 47 df gives p = 0.011, and R² = 0.13. Which statement is correct?

- **Options:**

  A) The association is significant but explains little variation
  B) Visits explain most of the variation in hybrid seed
  C) Visits definitely cause hybrid seed production
  D) There's no association between visits and hybrid seed

- **Answer (tutor only):** A
- **Explanation (tutor only):** p < 0.05 indicates an association; R² = 0.13 means visits explain about 13% of the variation.
- **Why the wrong options are wrong (tutor only):**
  B) R² is only 0.13.
  C) Association isn't causation.
  D) p < 0.05.
- **Hint:** Significance vs R².

### ch19-book-14-v2
- **Kind:** AI-written version of ch19-book-14
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Question:**

To see whether pollinator visits predict hybridization, we looked at 49 pink-flowered Clarkia RILs at one site, recording mean pollinator visits per observation and the proportion of hybrid seed each set.

F = 7.1 on 1 and 47 df gives p = 0.011. Why can't we conclude that pollinator visits CAUSE hybrid seed production?

- **Options:**

  A) These are observational data; other traits may drive both
  B) Because the p-value isn't below 0.001
  C) Because R² is greater than zero
  D) We can; a significant slope demonstrates causation

- **Answer (tutor only):** A
- **Explanation (tutor only):** RILs that attract more visits may differ in other traits (e.g. flower size, timing) that also affect hybridization.
- **Why the wrong options are wrong (tutor only):**
  B) Smaller p wouldn't prove causation.
  C) Irrelevant.
  D) Significance doesn't show causation.
- **Hint:** Observational vs experimental.

### ch19-chimein-01
- **Kind:** Course original
- **Concepts:** Slopes, intercepts & predictions
- **Type:** matching
- **Question:**

Match each description to the term it describes:

1. How much two variables jointly deviate from their means
2. How predictably the response changes with x (strength of the linear relationship)
3. The difference between an observation and its predicted value
4. How much the response changes with x

- **Options:**

  A) Covariance
  B) Correlation
  C) Residual
  D) Slope
  E) Intercept

- **Answer (tutor only):** 1-A, 2-B, 3-C, 4-D
- **Explanation (tutor only):** Covariance measures joint deviation (in units of x times y). Correlation standardizes it to measure how tightly points follow a line. The slope gives the change in y per unit x. A residual is observed minus predicted.
- **Why the wrong options are wrong (tutor only):**
  Common mix-up: correlation (how predictable) vs slope (how much).
- **Hint:** Which one has no units?

### ch19-chimein-01-v1
- **Kind:** AI-written version of ch19-chimein-01
- **Concepts:** Slopes, intercepts & predictions
- **Type:** matching
- **Question:**

Match each quantity to its units, for a regression of territory size (m²) on bite force (N):

1. Slope
2. Correlation
3. Covariance

- **Options:**

  A) m² per N
  B) No units
  C) m² × N

- **Answer (tutor only):** 1-A, 2-B, 3-C
- **Explanation (tutor only):** Slope: change in y per unit x. Correlation is unitless. Covariance has units of x times y.
- **Why the wrong options are wrong (tutor only):**
  Correlation is standardized.
- **Hint:** Which one is standardized?

### ch19-chimein-01-v2
- **Kind:** AI-written version of ch19-chimein-01
- **Concepts:** Slopes, intercepts & predictions
- **Type:** matching
- **Question:**

Match each description to the term it describes:

1. The predicted value of y when x = 0
2. The observed y minus the predicted y
3. Bounded between -1 and 1

- **Options:**

  A) Intercept
  B) Residual
  C) Correlation
  D) Slope

- **Answer (tutor only):** 1-A, 2-B, 3-C
- **Explanation (tutor only):** Intercept: prediction at x = 0. Residual: observed - predicted. Correlation: between -1 and 1.
- **Why the wrong options are wrong (tutor only):**
  The slope isn't described.
- **Hint:** Which is bounded?

### ch19-chimein-02
- **Kind:** Course original
- **Concepts:** Sums of squares, F & R²
- **Type:** matching
- **Question:**

Match each quantity to what it measures:

1. F and t
2. p
3. R²

- **Options:**

  A) Deviation from the null
  B) Surprise (how unusual the data would be under the null)
  C) Strength of association

- **Answer (tutor only):** 1-A, 2-B, 3-C
- **Explanation (tutor only):** F and t measure how far the estimate is from the null in standardized units. p converts that into how surprising the data would be if the null were true. R² measures the proportion of variance explained.
- **Why the wrong options are wrong (tutor only):**
  Common mix-up: p and the test statistic. The p-value is the probability; t and F are distances.
- **Hint:** Which one is a probability?

### ch19-chimein-02-v1
- **Kind:** AI-written version of ch19-chimein-02
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Question:**

Two regressions have the same R² but very different sample sizes (n = 10 and n = 1,000). Which will be the same in both?

- **Options:**

  A) R², the strength of association
  B) F, the deviation from the null
  C) p, the surprise under the null
  D) All three would be the same

- **Answer (tutor only):** A
- **Explanation (tutor only):** F and p depend on sample size; R² measures strength of association.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Change with n.
  D) Only R² is the same.
- **Hint:** Which ignores n?

### ch19-chimein-02-v2
- **Kind:** AI-written version of ch19-chimein-02
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Question:**

Which quantity tells you how SURPRISING the data would be if there were no relationship?

- **Options:**

  A) p
  B) R²
  C) The slope
  D) The correlation

- **Answer (tutor only):** A
- **Explanation (tutor only):** p measures surprise under the null.
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) describe the relationship, not surprise.
- **Hint:** Probability under the null.

### ch19-chimein-03
- **Kind:** Course original
- **Concepts:** Sums of squares, F & R²
- **Type:** matching
- **Question:**

In linear models, each observation Yᵢ equals its prediction Ŷᵢ plus its residual eᵢ. Match each expression to the sum of squares it represents:

1. Σ(Yᵢ - Ŷᵢ)²
2. Σ(Ŷᵢ - Ȳ)²
3. Σ(Yᵢ - Ȳ)²

- **Options:**

  A) SS model
  B) SS error
  C) SS total

- **Answer (tutor only):** 1-B, 2-A, 3-C
- **Explanation (tutor only):** Observations minus predictions: error. Predictions minus the mean: model. Observations minus the mean: total.
- **Why the wrong options are wrong (tutor only):**
  Common mix-up: model vs total.
- **Hint:** Ŷ is the prediction and Ȳ is the overall mean.

### ch19-chimein-03-v1
- **Kind:** AI-written version of ch19-chimein-03
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Question:**

In linear models, Yᵢ = Ŷᵢ + eᵢ. Which equation is always true?

- **Options:**

  A) Σ(Yᵢ - Ȳ)² = Σ(Ŷᵢ - Ȳ)² + Σ(Yᵢ - Ŷᵢ)²
  B) Σ(Yᵢ - Ŷᵢ)² = Σ(Ŷᵢ - Ȳ)² + Σ(Yᵢ - Ȳ)²
  C) Σ(Ŷᵢ - Ȳ)² = Σ(Yᵢ - Ȳ)² + Σ(Yᵢ - Ŷᵢ)²
  D) Σ(Yᵢ - Ȳ)² = Σ(Ŷᵢ - Ȳ)² × Σ(Yᵢ - Ŷᵢ)²

- **Answer (tutor only):** A
- **Explanation (tutor only):** SS total = SS model + SS error.
- **Why the wrong options are wrong (tutor only):**
  Identify SS total first.
- **Hint:** Total = model + error.

### ch19-chimein-03-v2
- **Kind:** AI-written version of ch19-chimein-03
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Question:**

Which expression is R²?

- **Options:**

  A) Σ(Ŷᵢ - Ȳ)² / Σ(Yᵢ - Ȳ)²
  B) Σ(Yᵢ - Ŷᵢ)² / Σ(Yᵢ - Ȳ)²
  C) Σ(Ŷᵢ - Ȳ)² / Σ(Yᵢ - Ŷᵢ)²
  D) Σ(Yᵢ - Ȳ)² / Σ(Ŷᵢ - Ȳ)²

- **Answer (tutor only):** A
- **Explanation (tutor only):** R² = SS model / SS total.
- **Why the wrong options are wrong (tutor only):**
  B) That's 1 - R².
  C) Model / error.
  D) Upside down.
- **Hint:** Model / total.

### ch19-chimein-04
- **Kind:** Course original
- **Concepts:** Measurement error & causation
- **Type:** select-all
- **Question:**

There is often measurement error, so values of x or y might not be exactly right. Random measurement error in X tends to: (Select all that apply.)

- **Options:**

  A) Bring the estimated slope closer to zero than it really is
  B) Bring the estimated correlation closer to zero than it really is
  C) Add unbiased noise to the estimated slope, increasing its standard error
  D) Not affect the estimated slope

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** Error in x weakens the apparent relationship: both the slope and the correlation are biased toward zero ('regression dilution').
- **Why the wrong options are wrong (tutor only):**
  C) That's what error in y does to the slope.
  D) Error in x does bias the slope.
- **Hint:** If x were measured with huge error, what would the scatterplot look like?

### ch19-chimein-04-v1
- **Kind:** AI-written version of ch19-chimein-04
- **Concepts:** Measurement error & causation
- **Type:** select-all
- **Question:**

Two labs measure the same relationship. Lab A measures x precisely; Lab B measures x with a lot of random error. Compared with Lab A, Lab B's estimated slope will tend to be: (Select all that apply.)

- **Options:**

  A) Closer to zero
  B) Farther from zero
  C) Exactly the same on average
  D) Associated with a weaker correlation

- **Answer (tutor only):** A, D
- **Explanation (tutor only):** Error in x biases both the slope and the correlation toward zero.
- **Why the wrong options are wrong (tutor only):**
  B) Bias is toward zero.
  C) Error in x causes bias.
- **Hint:** Regression dilution.

### ch19-chimein-04-v2
- **Kind:** AI-written version of ch19-chimein-04
- **Concepts:** Measurement error & causation
- **Type:** select-all
- **Question:**

What is 'regression dilution'?

- **Options:**

  A) Error in x biases the estimated slope toward zero
  B) Error in y biases the estimated slope toward zero
  C) Adding predictors reduces each one's slope
  D) Large samples shrink the slope toward zero

- **Answer (tutor only):** A
- **Explanation (tutor only):** Random error in the explanatory variable flattens the estimated slope.
- **Why the wrong options are wrong (tutor only):**
  B) Error in y doesn't bias the slope.
  C) and D) Not what it means.
- **Hint:** Which variable has the error?

### ch19-chimein-05
- **Kind:** Course original
- **Concepts:** Measurement error & causation
- **Type:** select-all
- **Question:**

Random measurement error in Y tends to: (Select all that apply.)

- **Options:**

  A) Bring the estimated slope closer to zero than it really is
  B) Bring the estimated correlation closer to zero than it really is
  C) Add unbiased noise to the estimated slope, increasing its standard error
  D) Not affect the estimated correlation

- **Answer (tutor only):** B, C
- **Explanation (tutor only):** Error in y adds scatter around the line: the slope stays unbiased but less precise, while the correlation (which measures how tightly points follow the line) drops.
- **Why the wrong options are wrong (tutor only):**
  A) Error in y doesn't bias the slope.
  D) More scatter lowers the correlation.
- **Hint:** Does adding noise to y tilt the line, or just scatter points around it?

### ch19-chimein-05-v1
- **Kind:** AI-written version of ch19-chimein-05
- **Concepts:** Measurement error & causation
- **Type:** select-all
- **Question:**

Two labs measure the same relationship. Lab A measures y precisely; Lab B measures y with a lot of random error. Compared with Lab A, Lab B will tend to have: (Select all that apply.)

- **Options:**

  A) A slope that is biased toward zero
  B) A weaker correlation
  C) A larger standard error for the slope
  D) A slope that is biased away from zero

- **Answer (tutor only):** B, C
- **Explanation (tutor only):** Error in y adds scatter: the slope stays unbiased but less precise, and the correlation drops.
- **Why the wrong options are wrong (tutor only):**
  A) and D) Error in y doesn't bias the slope.
- **Hint:** Scatter vs bias.

### ch19-chimein-05-v2
- **Kind:** AI-written version of ch19-chimein-05
- **Concepts:** Measurement error & causation
- **Type:** select-all
- **Question:**

Random measurement error in Y does NOT: (Select all that apply.)

- **Options:**

  A) Bias the estimated slope
  B) Reduce the estimated correlation
  C) Increase the slope's standard error
  D) Increase the residual variance

- **Answer (tutor only):** A
- **Explanation (tutor only):** Error in y leaves the slope unbiased but lowers the correlation and raises the SE and residual variance.
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) all happen.
- **Hint:** Which one stays unbiased?

### ch19-hw-01
- **Kind:** Course original
- **Concepts:** Confidence & prediction intervals
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-hw-sr.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-hw-sr.png)
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

The grey band in the plot is a (1) ____ interval. If we wanted the band to show where we expect individual observations to fall, we'd use a (2) ____ interval, and the band would be (3) ____.

- **Options:**

  A) confidence
  B) prediction
  C) wider
  D) narrower

- **Answer (tutor only):** 1-A, 2-B, 3-C
- **Explanation (tutor only):** A confidence band shows uncertainty in the mean response at each x. A prediction interval also includes the scatter of individual points around that mean, so it's much wider.
- **Why the wrong options are wrong (tutor only):**
  Common mix-up: thinking the grey band should contain most points. It describes the mean, not individuals.
- **Hint:** Is the band about the line or about individual RILs?

### ch19-hw-01-v1
- **Kind:** AI-written version of ch19-hw-01
- **Concepts:** Confidence & prediction intervals
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-hw-sr.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-hw-sr.png)
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

Match each interval to what it describes:

1. Confidence interval (the grey band)
2. Prediction interval

- **Options:**

  A) Where the true mean response at each x plausibly lies
  B) Where new individual observations are expected to fall
  C) Where 95% of the current data points fall
  D) The range of x values in the data

- **Answer (tutor only):** 1-A, 2-B
- **Explanation (tutor only):** A confidence band is for the mean response; a prediction interval adds individual scatter.
- **Why the wrong options are wrong (tutor only):**
  Mean vs individuals.
- **Hint:** Which one includes individual scatter?

### ch19-hw-01-v2
- **Kind:** AI-written version of ch19-hw-01
- **Concepts:** Confidence & prediction intervals
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-hw-sr.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-hw-sr.png)
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

The grey confidence band is narrowest near the middle of the petal areas and wider at the ends. Fill in the blanks: the band is narrowest near the (1) ____ of x, because the line's (2) ____ matters more far from that point.

- **Options:**

  A) mean
  B) maximum
  C) slope uncertainty
  D) intercept

- **Answer (tutor only):** 1-A, 2-C
- **Explanation (tutor only):** The line pivots around (mean x, mean y), so uncertainty in the slope matters more far from the mean.
- **Why the wrong options are wrong (tutor only):**
  The line always passes through the means.
- **Hint:** Where does the line pivot?

### ch19-hw-02
- **Kind:** Course original
- **Concepts:** Slopes, intercepts & predictions; Confidence & prediction intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-hw-sr.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-hw-sr.png)
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

The grey band is a 95% confidence interval. What does it mean?

- **Options:**

  A) If we repeatedly sampled data and refit the model, about 95% of such intervals would contain the true mean response at each x
  B) 95% of new observations will fall within this band
  C) There is a 95% probability that the true mean response lies within this particular band
  D) The band shows the range of fitted values predicted by the model

- **Answer (tutor only):** A
- **Explanation (tutor only):** Like any confidence interval, the '95%' describes how often intervals built this way capture the true value (here, the true mean response at each x).
- **Why the wrong options are wrong (tutor only):**
  B) That would be a prediction interval.
  C) A common misreading: the true mean either is or isn't in this particular band.
  D) The fitted values are the line itself.
- **Hint:** What does the 95% in a confidence interval refer to?

### ch19-hw-02-v1
- **Kind:** AI-written version of ch19-hw-02
- **Concepts:** Slopes, intercepts & predictions; Confidence & prediction intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-hw-sr.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-hw-sr.png)
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

Why do most individual points fall OUTSIDE the grey 95% confidence band?

- **Options:**

  A) The band describes the mean, not individual RILs
  B) The model is wrong and should be discarded
  C) The band should contain 95% of the points
  D) Most points are outliers in this dataset

- **Answer (tutor only):** A
- **Explanation (tutor only):** The confidence band is about the true mean response, not where individuals fall.
- **Why the wrong options are wrong (tutor only):**
  B) Points outside a confidence band are expected.
  C) That's a prediction interval.
  D) They're ordinary scatter.
- **Hint:** Mean vs individuals.

### ch19-hw-02-v2
- **Kind:** AI-written version of ch19-hw-02
- **Concepts:** Slopes, intercepts & predictions; Confidence & prediction intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-hw-sr.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-hw-sr.png)
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

With more RILs (and similar data), what would happen to the grey 95% confidence band?

- **Options:**

  A) It would get narrower
  B) It would get wider
  C) It would stay the same
  D) It would disappear

- **Answer (tutor only):** A
- **Explanation (tutor only):** More data shrink the standard errors of the intercept and slope, narrowing the band.
- **Why the wrong options are wrong (tutor only):**
  B) More data reduce uncertainty.
  C) Uncertainty depends on n.
  D) Some uncertainty always remains.
- **Hint:** What does n do to SEs?

### ch19-hw-03
- **Kind:** Course original
- **Concepts:** Assumptions & diagnostics
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-hw-sr-diag.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-hw-sr-diag.png)
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

Consider the diagnostic plots. Which assumptions do they show to be violated? (Select all that apply.)

- **Options:**

  A) Normality of residuals
  B) Homoscedasticity (equal variance)
  C) Independence
  D) Unbiased data collection

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** The QQ plot curves away from the line (skewed residuals: many RILs set no hybrid seed), and the spread of residuals changes with fitted values. Independence and bias can't be judged from these plots; they depend on the study design.
- **Why the wrong options are wrong (tutor only):**
  C) and D) Diagnostic plots can't show these.
- **Hint:** Which assumptions can a residual plot actually reveal?

### ch19-hw-03-v1
- **Kind:** AI-written version of ch19-hw-03
- **Concepts:** Assumptions & diagnostics
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-hw-sr-diag.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-hw-sr-diag.png)
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

Which assumptions CAN'T be evaluated from diagnostic plots? (Select all that apply.)

- **Options:**

  A) Independence
  B) Unbiased data collection
  C) Normality of residuals
  D) Homoscedasticity (equal variance)

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** Independence and bias depend on the study design; QQ and residual plots address normality and equal variance.
- **Why the wrong options are wrong (tutor only):**
  C) and D) are what the plots show.
- **Hint:** What do the plots actually display?

### ch19-hw-03-v2
- **Kind:** AI-written version of ch19-hw-03
- **Concepts:** Assumptions & diagnostics
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-hw-sr-diag.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-hw-sr-diag.png)
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

What does the QQ plot of residuals suggest?

- **Options:**

  A) The residuals are skewed, not normally distributed
  B) The residuals are perfectly normally distributed
  C) The residuals are not independent of each other
  D) The residuals have equal variance across x

- **Answer (tutor only):** A
- **Explanation (tutor only):** The points curve away from the line, as expected for proportions with many zeros.
- **Why the wrong options are wrong (tutor only):**
  B) They deviate.
  C) and D) A QQ plot doesn't show these.
- **Hint:** Do the points follow the line?

### ch19-hw-04
- **Kind:** Course original
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

The residuals are non-normal and their variance isn't constant. How should we treat the analysis?

- **Options:**

  A) Throw it in the garbage: the data don't meet assumptions
  B) Note the violations and check results with resampling
  C) Don't worry about it: linear models never need assumptions

- **Answer (tutor only):** B
- **Explanation (tutor only):** Linear models are fairly robust, especially with 113 points, but we should be honest about violations and check that conclusions hold with methods that don't rely on them.
- **Why the wrong options are wrong (tutor only):**
  A) Real data rarely meet every assumption; this throws away useful information.
  C) Ignoring violations risks overconfident conclusions.
- **Hint:** What's the middle ground between ignoring and discarding?

### ch19-hw-04-v1
- **Kind:** AI-written version of ch19-hw-04
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

The residuals are non-normal and their variance isn't constant. Which is a reasonable way to check the conclusion?

- **Options:**

  A) Compare with a permutation test or bootstrap
  B) Delete points until the residuals look normal
  C) Report the result without mentioning the problems
  D) Switch to a smaller α and keep the same model

- **Answer (tutor only):** A
- **Explanation (tutor only):** Resampling methods don't rely on normal, equal-variance residuals.
- **Why the wrong options are wrong (tutor only):**
  B) Deleting data to fit assumptions is wrong.
  C) Be honest about violations.
  D) α doesn't fix assumption violations.
- **Hint:** Which methods don't need these assumptions?

### ch19-hw-04-v2
- **Kind:** AI-written version of ch19-hw-04
- **Concepts:** Assumptions & diagnostics
- **Type:** MC
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

The residuals are somewhat non-normal. Why is this less of a worry with 113 RILs than it would be with 10?

- **Options:**

  A) The CLT makes the slope's sampling distribution near normal
  B) Large samples make the residuals themselves normal
  C) Large samples make the model's assumptions unnecessary
  D) It is not less of a worry with more data

- **Answer (tutor only):** A
- **Explanation (tutor only):** With large samples, estimates like the slope have roughly normal sampling distributions even when residuals aren't normal.
- **Why the wrong options are wrong (tutor only):**
  B) Residuals keep their shape.
  C) Assumptions still matter (e.g. independence).
  D) Large n helps.
- **Hint:** Central limit theorem.

### ch19-hw-05
- **Kind:** Course original
- **Concepts:** Slopes, intercepts & predictions
- **Type:** numeric
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

Mean petal area = 62.9 mm²; variance in petal area = 232; mean proportion hybrid = 0.173; variance in proportion hybrid = 0.0651; covariance = 0.92.

How much do we expect the proportion of hybrid seed to change for each 1 mm² increase in petal area?

- **Answer (tutor only):** 0.004
- **Explanation (tutor only):** Slope = cov(x, y) / var(x) = 0.92 / 232 = 0.0040.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: dividing by the variance of y (0.92 / 0.0651 = 14.1).
- **Hint:** Slope = covariance / variance of x.

### ch19-hw-05-v1
- **Kind:** AI-written version of ch19-hw-05
- **Concepts:** Slopes, intercepts & predictions
- **Type:** numeric
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

Mean petal area = 62.9 mm²; variance in petal area = 232; mean proportion hybrid = 0.173; variance in proportion hybrid = 0.0651; covariance = 0.92.

What is the correlation between petal area and proportion hybrid? Report it to two decimals.

- **Answer (tutor only):** 0.24
- **Explanation (tutor only):** r = 0.92 / (√232 × √0.0651) = 0.92 / (15.23 × 0.255) = 0.24.
- **Hint:** cov / (sd_x × sd_y).

### ch19-hw-05-v2
- **Kind:** AI-written version of ch19-hw-05
- **Concepts:** Slopes, intercepts & predictions
- **Type:** numeric
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

Mean petal area = 62.9 mm²; variance in petal area = 232; mean proportion hybrid = 0.173; variance in proportion hybrid = 0.0651; covariance = 0.92.

How much more hybrid seed (as a proportion) do we expect for a RIL with 10 mm² more petal area?

- **Answer (tutor only):** 0.04
- **Explanation (tutor only):** Slope = 0.92 / 232 = 0.0040 per mm², so 10 mm² → 0.040.
- **Hint:** Slope × 10.

### ch19-hw-06
- **Kind:** Course original
- **Concepts:** Slopes, intercepts & predictions
- **Type:** MC
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

The intercept is -0.078. What does a negative intercept mean here?

- **Options:**

  A) We should not believe our model, since it can't be negative
  B) We expect a flower with no petals to have negative hybrid seed
  C) It anchors the line; zero petal area is far outside our data

- **Answer (tutor only):** C
- **Explanation (tutor only):** The intercept is where the line crosses x = 0. No plant has zero petal area (they range from about 35 to 110 mm²), so it's just an anchor for the line, not a biological prediction.
- **Why the wrong options are wrong (tutor only):**
  A) A meaningless intercept doesn't invalidate the slope.
  B) Literally what the line says at x = 0, but that's an extrapolation we shouldn't make.
- **Hint:** Is zero petal area within the range of the data?

### ch19-hw-06-v1
- **Kind:** AI-written version of ch19-hw-06
- **Concepts:** Slopes, intercepts & predictions
- **Type:** MC
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

The intercept is -0.078 and the slope is 0.0040. What does the model predict for a RIL with a petal area of 60 mm²?

- **Options:**

  A) About 0.16
  B) About -0.08
  C) About 0.24
  D) About 0.004

- **Answer (tutor only):** A
- **Explanation (tutor only):** -0.078 + 0.0040 × 60 = -0.078 + 0.24 = 0.162.
- **Why the wrong options are wrong (tutor only):**
  B) That's the intercept.
  C) Forgets the intercept.
  D) That's the slope.
- **Hint:** Intercept + slope × 60.

### ch19-hw-06-v2
- **Kind:** AI-written version of ch19-hw-06
- **Concepts:** Slopes, intercepts & predictions
- **Type:** MC
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

Petal areas range from about 35 to 110 mm². Over what range of petal areas does the model predict a NEGATIVE proportion of hybrid seed (intercept -0.078, slope 0.0040)?

- **Options:**

  A) Below about 20 mm², outside our data
  B) Below about 60 mm², within our data
  C) Above about 110 mm², outside our data
  D) It never predicts a negative proportion

- **Answer (tutor only):** A
- **Explanation (tutor only):** The line crosses zero at 0.078 / 0.0040 ≈ 19.5 mm², below the smallest petals observed.
- **Why the wrong options are wrong (tutor only):**
  B) At 60 mm² the prediction is 0.16.
  C) Predictions increase with area.
  D) The intercept is negative.
- **Hint:** Solve -0.078 + 0.004 × x = 0.

### ch19-hw-07
- **Kind:** Course original
- **Concepts:** Sums of squares, F & R²
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-hw-sr-deviations.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-hw-sr-deviations.png)
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

Each plot shows 30 randomly chosen RILs, the regression line (blue) and the mean proportion hybrid (black). Match each plot to the deviations it shows:

1. Plot A
2. Plot B
3. Plot C

- **Options:**

  A) Error
  B) Total
  C) Model

- **Answer (tutor only):** 1-A, 2-B, 3-C
- **Explanation (tutor only):** A: points to the regression line (error). B: points to the mean (total). C: the line to the mean (model).
- **Why the wrong options are wrong (tutor only):**
  Check where each pink line starts and ends.
- **Hint:** Which plot's lines never touch the points?

### ch19-hw-07-v1
- **Kind:** AI-written version of ch19-hw-07
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-hw-sr-deviations.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-hw-sr-deviations.png)
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

Each plot shows 30 randomly chosen RILs, the regression line (blue) and the mean proportion hybrid (black). Which plot's lines would ALL shrink to zero if petal area had no relationship with hybrid seed (a flat line at the mean)?

- **Options:**

  A) Plot A
  B) Plot B
  C) Plot C

- **Answer (tutor only):** C
- **Explanation (tutor only):** Model deviations (line to mean) vanish when the line is the mean.
- **Why the wrong options are wrong (tutor only):**
  A) Points still scatter around the line.
  B) Points still scatter around the mean.
- **Hint:** Which lines connect the regression line to the mean?

### ch19-hw-07-v2
- **Kind:** AI-written version of ch19-hw-07
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-hw-sr-deviations.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-hw-sr-deviations.png)
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

Each plot shows 30 randomly chosen RILs, the regression line (blue) and the mean proportion hybrid (black). Which plot shows the residuals?

- **Options:**

  A) Plot A
  B) Plot B
  C) Plot C

- **Answer (tutor only):** A
- **Explanation (tutor only):** Residuals are the vertical distances from each point to the regression line (Plot A).
- **Why the wrong options are wrong (tutor only):**
  B) Total deviations.
  C) Model deviations.
- **Hint:** Point to line.

### ch19-hw-08
- **Kind:** Course original
- **Concepts:** Sums of squares, F & R²
- **Type:** matching
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

model_dat |>
  summarise(ssa = sum((.fitted - grand_mean)^2),
            ssb = sum((prop_hybrid - .fitted)^2),
            ssc = sum((prop_hybrid - grand_mean)^2))

ssa = 0.413; ssb = 6.88; ssc = 7.29

Match each to its sum of squares:

1. ssa
2. ssb
3. ssc

- **Options:**

  A) Model
  B) Error
  C) Total

- **Answer (tutor only):** 1-A, 2-B, 3-C
- **Explanation (tutor only):** ssa compares predictions to the mean (model), ssb compares observations to predictions (error), and ssc compares observations to the mean (total). Check: 0.413 + 6.88 = 7.29.
- **Why the wrong options are wrong (tutor only):**
  Common mix-up: model vs total.
- **Hint:** .fitted is each RIL's predicted value.

### ch19-hw-08-v1
- **Kind:** AI-written version of ch19-hw-08
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

SS model = 0.413, SS error = 6.88. What is SS total?

- **Options:**

  A) 7.29
  B) 6.47
  C) 0.06
  D) 16.7

- **Answer (tutor only):** A
- **Explanation (tutor only):** SS total = 0.413 + 6.88 = 7.29.
- **Why the wrong options are wrong (tutor only):**
  B) Subtracts.
  C) That's R².
  D) That's 6.88 / 0.413.
- **Hint:** SS total = SS model + SS error.

### ch19-hw-08-v2
- **Kind:** AI-written version of ch19-hw-08
- **Concepts:** Sums of squares, F & R²
- **Type:** matching
- **Question:**

Match each formula to its sum of squares in a regression:

1. sum((y - .fitted)^2)
2. sum((.fitted - mean(y))^2)
3. sum((y - mean(y))^2)

- **Options:**

  A) Model
  B) Error
  C) Total

- **Answer (tutor only):** 1-B, 2-A, 3-C
- **Explanation (tutor only):** Observation - prediction: error. Prediction - mean: model. Observation - mean: total.
- **Why the wrong options are wrong (tutor only):**
  Which two quantities are compared?
- **Hint:** Error uses the observations and predictions.

### ch19-hw-09
- **Kind:** Course original
- **Concepts:** Sums of squares, F & R²
- **Type:** numeric
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

SS model = 0.413 and SS error = 6.88, with 113 data points. The model has 1 and 111 degrees of freedom. What is F?

- **Answer (tutor only):** 6.66
- **Explanation (tutor only):** MS model = 0.413 / 1 = 0.413. MS error = 6.88 / 111 = 0.0620. F = 0.413 / 0.0620 = 6.66.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: using 112 or 113 for the error df, or F = SS model / SS error (0.06).
- **Hint:** Error df = n - 2 for a simple regression.

### ch19-hw-09-v1
- **Kind:** AI-written version of ch19-hw-09
- **Concepts:** Sums of squares, F & R²
- **Type:** numeric
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

SS model = 0.413 and SS error = 6.88, with 1 and 111 df. What is the mean square error? Report it to four decimals.

- **Answer (tutor only):** 0.062
- **Explanation (tutor only):** MS error = 6.88 / 111 = 0.0620.
- **Hint:** SS error / df error.

### ch19-hw-09-v2
- **Kind:** AI-written version of ch19-hw-09
- **Concepts:** Sums of squares, F & R²
- **Type:** numeric
- **Question:**

A regression on 52 points has SS model = 2.0 and SS error = 25.0. What is F?

- **Answer (tutor only):** 4
- **Explanation (tutor only):** df = 1 and 50. MS error = 25 / 50 = 0.5. F = 2.0 / 0.5 = 4.
- **Hint:** F = MS model / MS error.

### ch19-hw-10
- **Kind:** Course original
- **Concepts:** Sums of squares, F & R²
- **Type:** matching
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

A simple regression on 113 data points. Match each degree of freedom to its value:

1. df1 (model)
2. df2 (error)

- **Options:**

  A) 1
  B) 2
  C) 111
  D) 112

- **Answer (tutor only):** 1-A, 2-C
- **Explanation (tutor only):** The model estimates one slope beyond the mean (df = 1). Error df = n - 2 = 111 (we estimated an intercept and a slope).
- **Why the wrong options are wrong (tutor only):**
  Common mistake: n - 1 = 112 for the error df.
- **Hint:** How many parameters did the model estimate?

### ch19-hw-10-v1
- **Kind:** AI-written version of ch19-hw-10
- **Concepts:** Sums of squares, F & R²
- **Type:** matching
- **Question:**

A simple regression on 30 data points. Match each degree of freedom to its value:

1. df1 (model)
2. df2 (error)

- **Options:**

  A) 1
  B) 2
  C) 28
  D) 29

- **Answer (tutor only):** 1-A, 2-C
- **Explanation (tutor only):** Model df = 1 (one slope). Error df = 30 - 2 = 28.
- **Why the wrong options are wrong (tutor only):**
  Two parameters are estimated.
- **Hint:** n - 2 for error.

### ch19-hw-10-v2
- **Kind:** AI-written version of ch19-hw-10
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

Why is the error df 111 (not 112) in this regression on 113 RILs?

- **Options:**

  A) Two parameters, intercept and slope, are estimated
  B) One data point was removed as an outlier
  C) The model df is always subtracted twice
  D) R uses n - 2 for every type of model

- **Answer (tutor only):** A
- **Explanation (tutor only):** Error df = n minus the number of estimated parameters (2).
- **Why the wrong options are wrong (tutor only):**
  B) No points were removed.
  C) Not how df work.
  D) It depends on the number of parameters.
- **Hint:** Count the estimated parameters.

### ch19-hw-11
- **Kind:** Course original
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

F = 6.66 on 1 and 111 df gives p = 0.011. How would you describe this p-value, and what do we do with the null?

- **Options:**

  A) Extremely small (p < 10⁻⁷); reject
  B) Comfortably below 0.05 but not minuscule; reject
  C) Near significance (0.05 < p < 0.10); fail to reject
  D) Large (p > 0.10); fail to reject

- **Answer (tutor only):** B
- **Explanation (tutor only):** p = 0.011 < 0.05, so we reject the null of no relationship between petal area and hybrid seed.
- **Why the wrong options are wrong (tutor only):**
  A) It's not that small. C) and D) p is below 0.05.
- **Hint:** Compare 0.011 to 0.05.

### ch19-hw-11-v1
- **Kind:** AI-written version of ch19-hw-11
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

F = 6.66 on 1 and 111 df gives p = 0.011. Which statement is correct?

- **Options:**

  A) Petal area is associated with hybrid seed, but explains little variation
  B) Petal area explains most of the variation in hybrid seed
  C) Larger petals definitely cause more hybrid seed
  D) There is a 1.1% chance there's no relationship

- **Answer (tutor only):** A
- **Explanation (tutor only):** p < 0.05 shows an association; R² = 0.057 shows it explains little of the variation.
- **Why the wrong options are wrong (tutor only):**
  B) R² is only 0.057.
  C) Association isn't causation.
  D) p isn't P(null).
- **Hint:** Significance vs R².

### ch19-hw-11-v2
- **Kind:** AI-written version of ch19-hw-11
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

Why is the regression's F (6.66) equal to the square of the slope's t?

- **Options:**

  A) With one predictor, F = t² and both test the same null
  B) Coincidence; F and t are unrelated in regression
  C) F always equals t² regardless of the model
  D) Because R² is the square of the correlation

- **Answer (tutor only):** A
- **Explanation (tutor only):** With one predictor, the F test of the model and the t test of the slope test the same null (slope = 0), and F = t².
- **Why the wrong options are wrong (tutor only):**
  B) It's not a coincidence.
  C) Only with one numerator df.
  D) True, but not the reason.
- **Hint:** How many predictors?

### ch19-hw-12
- **Kind:** Course original
- **Concepts:** Sums of squares, F & R²
- **Type:** numeric
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

SS model = 0.413 and SS total = 7.29. What proportion of the variance in proportion hybrid seed is explained by petal area in this sample?

- **Answer (tutor only):** 0.057
- **Explanation (tutor only):** R² = 0.413 / 7.29 = 0.057. Petal area is significantly associated with hybrid seed, but it explains less than 6% of the variation.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: SS model / SS error (0.06): close here, but not the right formula.
- **Hint:** R² = SS model / SS total.

### ch19-hw-12-v1
- **Kind:** AI-written version of ch19-hw-12
- **Concepts:** Sums of squares, F & R²
- **Type:** numeric
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

SS model = 0.413 and SS total = 7.29. What proportion of the variance in proportion hybrid is NOT explained by petal area? Report it to three decimals.

- **Answer (tutor only):** 0.943
- **Explanation (tutor only):** 1 - 0.413 / 7.29 = 1 - 0.057 = 0.943.
- **Hint:** 1 - R².

### ch19-hw-12-v2
- **Kind:** AI-written version of ch19-hw-12
- **Concepts:** Sums of squares, F & R²
- **Type:** numeric
- **Question:**

To ask whether bigger petals attract more cross-pollination, we regressed the proportion of hybrid seed on petal area for 113 parviflora RILs planted at Sawmill Road (SR).

The correlation between petal area and proportion hybrid is 0.24. What is R²? Report it to three decimals.

- **Answer (tutor only):** 0.058
- **Explanation (tutor only):** In simple regression, R² = r² = 0.24² = 0.058.
- **Hint:** Square the correlation.

### ch19-quiz-01
- **Kind:** Course original
- **Concepts:** Slopes, intercepts & predictions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-quiz-lizard.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-quiz-lizard.png)
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

lm(territory ~ bite, data = lizards)

term | estimate | std.error | conf.low | conf.high
(Intercept) | -31.54 | 23.51 | -84.73 | 21.65
bite | 11.68 | 4.85 | 0.71 | 22.64

R² = 0.392; F = 5.80 on 1 and 9 df; p = 0.039

Which equation describes this model?

- **Options:**

  A) territoryᵢ = -31.54 + 11.68 × biteᵢ + eᵢ
  B) territoryᵢ = 11.68 - 31.54 × biteᵢ + eᵢ
  C) biteᵢ = -31.54 + 11.68 × territoryᵢ + eᵢ
  D) territoryᵢ = -31.54 + 11.68 × biteᵢ

- **Answer (tutor only):** A
- **Explanation (tutor only):** Each lizard's territory equals the intercept plus the slope times its bite force, plus its residual. Territory increases by about 11.7 m² per newton of bite force.
- **Why the wrong options are wrong (tutor only):**
  B) Swaps intercept and slope.
  C) Swaps the response and explanatory variables.
  D) That's the prediction (Ŷ), not the observation (Yᵢ needs + eᵢ).
- **Hint:** Yᵢ = intercept + slope × xᵢ + residual.

### ch19-quiz-01-v1
- **Kind:** AI-written version of ch19-quiz-01
- **Concepts:** Slopes, intercepts & predictions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-quiz-lizard.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-quiz-lizard.png)
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

lm(territory ~ bite, data = lizards)

term | estimate | std.error | conf.low | conf.high
(Intercept) | -31.54 | 23.51 | -84.73 | 21.65
bite | 11.68 | 4.85 | 0.71 | 22.64

R² = 0.392; F = 5.80 on 1 and 9 df; p = 0.039

In the equation territoryᵢ = a + b × biteᵢ + eᵢ, what is eᵢ?

- **Options:**

  A) The residual: lizard i's territory minus its prediction
  B) The standard error of the slope for lizard i
  C) The predicted territory size for lizard i
  D) The bite force of lizard i, minus the mean bite force

- **Answer (tutor only):** A
- **Explanation (tutor only):** eᵢ is lizard i's residual: what's left after the line's prediction.
- **Why the wrong options are wrong (tutor only):**
  B) Standard errors describe estimates, not individual lizards.
  C) That's a + b × biteᵢ.
  D) That's a deviation in x.
- **Hint:** Observed = predicted + ?

### ch19-quiz-01-v2
- **Kind:** AI-written version of ch19-quiz-01
- **Concepts:** Slopes, intercepts & predictions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch19-quiz-lizard.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch19-quiz-lizard.png)
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

lm(territory ~ bite, data = lizards)

term | estimate | std.error | conf.low | conf.high
(Intercept) | -31.54 | 23.51 | -84.73 | 21.65
bite | 11.68 | 4.85 | 0.71 | 22.64

R² = 0.392; F = 5.80 on 1 and 9 df; p = 0.039

Which equation gives the model's PREDICTED territory size for lizard i?

- **Options:**

  A) territorŷᵢ = -31.54 + 11.68 × biteᵢ
  B) territorŷᵢ = -31.54 + 11.68 × biteᵢ + eᵢ
  C) territorŷᵢ = 11.68 - 31.54 × biteᵢ
  D) territorŷᵢ = -31.54 + 4.85 × biteᵢ

- **Answer (tutor only):** A
- **Explanation (tutor only):** Predictions come from the line alone; the residual is the gap between the observation and the prediction.
- **Why the wrong options are wrong (tutor only):**
  B) Adding eᵢ gives the observed value.
  C) Swaps intercept and slope.
  D) Uses the slope's SE instead of the slope.
- **Hint:** Predictions have no residual term.

### ch19-quiz-02
- **Kind:** Course original
- **Concepts:** Slopes, intercepts & predictions; Confidence & prediction intervals
- **Type:** MC
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

lm(territory ~ bite, data = lizards)

term | estimate | std.error | conf.low | conf.high
(Intercept) | -31.54 | 23.51 | -84.73 | 21.65
bite | 11.68 | 4.85 | 0.71 | 22.64

R² = 0.392; F = 5.80 on 1 and 9 df; p = 0.039

What is the 95% confidence interval for the slope, and what does it tell us?

- **Options:**

  A) (-84.7, 21.7); the slope could plausibly be zero
  B) (0.71, 22.6); all positive, but from tiny to large
  C) (0.71, 22.6); the true slope is exactly 11.68
  D) (4.85, 11.68); the slope is very precisely known

- **Answer (tutor only):** B
- **Explanation (tutor only):** The slope's CI runs from 0.71 to 22.6 m² per N. It excludes zero (consistent with p = 0.039), but with only 11 lizards it's very wide.
- **Why the wrong options are wrong (tutor only):**
  A) That's the intercept's CI.
  C) 11.68 is the estimate; the CI says many other values are plausible.
  D) Those are the SE and the estimate.
- **Hint:** Find the row for bite.

### ch19-quiz-02-v1
- **Kind:** AI-written version of ch19-quiz-02
- **Concepts:** Slopes, intercepts & predictions; Confidence & prediction intervals
- **Type:** MC
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

lm(territory ~ bite, data = lizards)

term | estimate | std.error | conf.low | conf.high
(Intercept) | -31.54 | 23.51 | -84.73 | 21.65
bite | 11.68 | 4.85 | 0.71 | 22.64

R² = 0.392; F = 5.80 on 1 and 9 df; p = 0.039

What is the 95% confidence interval for the intercept, and does it include zero?

- **Options:**

  A) (-84.7, 21.7); yes, it includes zero
  B) (0.71, 22.6); no, it excludes zero
  C) (-84.7, 21.7); no, it excludes zero
  D) (23.5, 4.85); yes, it includes zero

- **Answer (tutor only):** A
- **Explanation (tutor only):** The intercept's CI is -84.73 to 21.65, which includes zero.
- **Why the wrong options are wrong (tutor only):**
  B) That's the slope's CI.
  C) The interval spans zero.
  D) Those are standard errors.
- **Hint:** Look at the (Intercept) row.

### ch19-quiz-02-v2
- **Kind:** AI-written version of ch19-quiz-02
- **Concepts:** Slopes, intercepts & predictions; Confidence & prediction intervals
- **Type:** MC
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

lm(territory ~ bite, data = lizards)

term | estimate | std.error | conf.low | conf.high
(Intercept) | -31.54 | 23.51 | -84.73 | 21.65
bite | 11.68 | 4.85 | 0.71 | 22.64

R² = 0.392; F = 5.80 on 1 and 9 df; p = 0.039

Why is the slope's 95% CI (0.71 to 22.6) so wide?

- **Options:**

  A) With only 11 lizards, the slope's SE is large
  B) Because the slope is statistically significant
  C) Because bite force causes larger territories
  D) Because R² is greater than 0.3

- **Answer (tutor only):** A
- **Explanation (tutor only):** Small samples give large SEs (4.85 here), so the CI (estimate ± about 2.26 × SE) is wide.
- **Why the wrong options are wrong (tutor only):**
  B) Significance doesn't widen a CI.
  C) Causation isn't shown and doesn't affect width.
  D) R² doesn't set the CI width directly.
- **Hint:** CI = estimate ± critical t × SE.

### ch19-quiz-03
- **Kind:** Course original
- **Concepts:** Slopes, intercepts & predictions
- **Type:** numeric
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

The fitted model is territory = -31.54 + 11.68 × bite. A lizard with a bite force of 5.2 N has a territory of 28 m². What is its residual?

- **Answer (tutor only):** -1.18
- **Explanation (tutor only):** Prediction = -31.54 + 11.68 × 5.2 = 29.18 m². Residual = 28 - 29.18 = -1.18 m².
- **Why the wrong options are wrong (tutor only):**
  Common mistake: predicted - observed (+1.18).
- **Hint:** Predict first, then subtract the prediction from the observed value.

### ch19-quiz-03-v1
- **Kind:** AI-written version of ch19-quiz-03
- **Concepts:** Slopes, intercepts & predictions
- **Type:** numeric
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

The fitted model is territory = -31.54 + 11.68 × bite. A lizard with a bite force of 4.5 N has a territory of 25 m². What is its residual?

- **Answer (tutor only):** 3.98
- **Explanation (tutor only):** Prediction = -31.54 + 11.68 × 4.5 = 21.02. Residual = 25 - 21.02 = 3.98 m².
- **Hint:** Observed - predicted.

### ch19-quiz-03-v2
- **Kind:** AI-written version of ch19-quiz-03
- **Concepts:** Slopes, intercepts & predictions
- **Type:** numeric
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

The fitted model is territory = -31.54 + 11.68 × bite. What territory size does the model predict for a lizard with a bite force of 5.0 N?

- **Answer (tutor only):** 26.86
- **Explanation (tutor only):** -31.54 + 11.68 × 5.0 = 26.86 m².
- **Hint:** Intercept + slope × 5.0.

### ch19-quiz-04
- **Kind:** Course original
- **Concepts:** Slopes, intercepts & predictions
- **Type:** MC
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

The fitted model is territory = -31.54 + 11.68 × bite. Plugging in a bite force of 2.5 N gives a predicted territory of -2.3 m². What's wrong with this prediction?

- **Options:**

  A) Nothing; the model simply predicts a small territory
  B) It's an extrapolation far below the bite forces we measured
  C) We should have used the confidence interval instead
  D) The slope isn't significant, so no prediction is possible

- **Answer (tutor only):** B
- **Explanation (tutor only):** The model only describes lizards with bite forces between about 4.3 and 5.4 N. Far outside that range the straight line need not hold, as the impossible negative area shows.
- **Why the wrong options are wrong (tutor only):**
  A) A territory can't be negative.
  C) A CI wouldn't fix an extrapolation.
  D) p = 0.039, and significance isn't the issue.
- **Hint:** What range of bite forces was the model built on?

### ch19-quiz-04-v1
- **Kind:** AI-written version of ch19-quiz-04
- **Concepts:** Slopes, intercepts & predictions
- **Type:** MC
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

The fitted model is territory = -31.54 + 11.68 × bite. Which prediction is most trustworthy?

- **Options:**

  A) For a lizard with a bite force of 4.8 N
  B) For a lizard with a bite force of 2.0 N
  C) For a lizard with a bite force of 8.0 N
  D) All are equally trustworthy

- **Answer (tutor only):** A
- **Explanation (tutor only):** 4.8 N lies within the observed range (4.3 to 5.4 N); the others are extrapolations.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Far outside the data.
  D) Extrapolations are less trustworthy.
- **Hint:** Which is inside the data?

### ch19-quiz-04-v2
- **Kind:** AI-written version of ch19-quiz-04
- **Concepts:** Slopes, intercepts & predictions
- **Type:** MC
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

The fitted model is territory = -31.54 + 11.68 × bite. For a lizard with a 10 N bite, the model predicts 85.3 m². Why should we be cautious?

- **Options:**

  A) 10 N is far above the bite forces we observed
  B) The prediction is a positive number of square meters
  C) The slope's confidence interval doesn't include zero
  D) We shouldn't; the model gives a sensible prediction

- **Answer (tutor only):** A
- **Explanation (tutor only):** Our data cover 4.3 to 5.4 N; we don't know if the line holds far beyond that.
- **Why the wrong options are wrong (tutor only):**
  B) Positive is fine.
  C) Irrelevant to extrapolation.
  D) Plausible-looking extrapolations are still extrapolations.
- **Hint:** Range of the data.

### ch19-quiz-06
- **Kind:** Course original
- **Concepts:** Sums of squares, F & R²
- **Type:** numeric
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

lm(territory ~ bite, data = lizards)

term | estimate | std.error | conf.low | conf.high
(Intercept) | -31.54 | 23.51 | -84.73 | 21.65
bite | 11.68 | 4.85 | 0.71 | 22.64

R² = 0.392; F = 5.80 on 1 and 9 df; p = 0.039

What proportion of the variance in territory area is explained by bite force in this study?

- **Answer (tutor only):** 0.392
- **Explanation (tutor only):** That's R² = 0.392: about 39% of the variation in territory size among these lizards is associated with bite force.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: reporting the p-value (0.039) or the correlation (r = 0.63).
- **Hint:** Which statistic is the proportion of variance explained?

### ch19-quiz-06-v1
- **Kind:** AI-written version of ch19-quiz-06
- **Concepts:** Sums of squares, F & R²
- **Type:** numeric
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

lm(territory ~ bite, data = lizards)

term | estimate | std.error | conf.low | conf.high
(Intercept) | -31.54 | 23.51 | -84.73 | 21.65
bite | 11.68 | 4.85 | 0.71 | 22.64

R² = 0.392; F = 5.80 on 1 and 9 df; p = 0.039

What proportion of the variance in territory area is NOT explained by bite force in this study?

- **Answer (tutor only):** 0.608
- **Explanation (tutor only):** 1 - R² = 1 - 0.392 = 0.608.
- **Hint:** 1 - R².

### ch19-quiz-06-v2
- **Kind:** AI-written version of ch19-quiz-06
- **Concepts:** Sums of squares, F & R²
- **Type:** numeric
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

lm(territory ~ bite, data = lizards)

term | estimate | std.error | conf.low | conf.high
(Intercept) | -31.54 | 23.51 | -84.73 | 21.65
bite | 11.68 | 4.85 | 0.71 | 22.64

R² = 0.392; F = 5.80 on 1 and 9 df; p = 0.039

What is the correlation between bite force and territory size? (The slope is positive.) Report it to two decimals.

- **Answer (tutor only):** 0.63
- **Explanation (tutor only):** In a simple regression, r = ±√R² = √0.392 = 0.63 (positive, like the slope).
- **Hint:** √R², with the slope's sign.

### ch19-quiz-07
- **Kind:** Course original
- **Concepts:** Measurement error & causation
- **Type:** select-all
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

Our measurements of bite force (x) are probably off by some random amount. This means: (Select all that apply.)

- **Options:**

  A) Our estimate of the slope is likely biased upwards (farther from zero than the true slope)
  B) Our estimate of the slope is likely biased downwards (closer to zero than the true slope)
  C) Uncertainty in the estimate is larger than if we had perfect measurements
  D) Uncertainty in the estimate is smaller than if we had perfect measurements
  E) Nothing: measurement error is accounted for in regressions

- **Answer (tutor only):** B, C
- **Explanation (tutor only):** Random error in x blurs the relationship, pulling the estimated slope toward zero ('regression dilution') and adding noise.
- **Why the wrong options are wrong (tutor only):**
  A) Error in x biases the slope toward zero, not away.
  D) Extra noise increases uncertainty.
  E) Standard regression assumes x is measured without error.
- **Hint:** If x were pure noise, what slope would you estimate?

### ch19-quiz-07-v1
- **Kind:** AI-written version of ch19-quiz-07
- **Concepts:** Measurement error & causation
- **Type:** select-all
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

If we measured bite force (x) perfectly, instead of with random error, what would we expect? (Select all that apply.)

- **Options:**

  A) The estimated slope would tend to be farther from zero
  B) The estimated slope would tend to be closer to zero
  C) The slope's uncertainty would be smaller
  D) Nothing would change

- **Answer (tutor only):** A, C
- **Explanation (tutor only):** Removing error in x removes regression dilution (the slope moves away from zero toward its true value) and reduces noise.
- **Why the wrong options are wrong (tutor only):**
  B) Error in x biases toward zero; removing it does the reverse.
  D) Error in x does matter.
- **Hint:** Regression dilution.

### ch19-quiz-07-v2
- **Kind:** AI-written version of ch19-quiz-07
- **Concepts:** Measurement error & causation
- **Type:** select-all
- **Question:**

A biologist measures body size (x) with a lot of random error and regresses metabolic rate (y) on it. Compared with the true relationship, the estimated slope is likely to be: (Select all that apply.)

- **Options:**

  A) Closer to zero than the true slope
  B) Farther from zero than the true slope
  C) Less precise than with perfect measurements
  D) Exactly unbiased, because error averages out

- **Answer (tutor only):** A, C
- **Explanation (tutor only):** Error in x dilutes the slope toward zero and adds noise.
- **Why the wrong options are wrong (tutor only):**
  B) Bias is toward zero.
  D) Error in x does not average out in the slope.
- **Hint:** Regression dilution.

### ch19-quiz-08
- **Kind:** Course original
- **Concepts:** Measurement error & causation
- **Type:** select-all
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

Our measurements of territory size (y) are probably off by some random amount. This means: (Select all that apply.)

- **Options:**

  A) Our estimate of the slope is likely biased upwards
  B) Our estimate of the slope is likely biased downwards
  C) Uncertainty in the estimate is larger than if we had perfect measurements
  D) Uncertainty in the estimate is smaller than if we had perfect measurements
  E) Nothing: measurement error is accounted for in regressions

- **Answer (tutor only):** C
- **Explanation (tutor only):** Random error in y just adds to the residual variation: the slope stays unbiased, but its standard error grows.
- **Why the wrong options are wrong (tutor only):**
  A) and B) Error in y doesn't bias the slope.
  D) More noise means more uncertainty.
  E) It's absorbed into the residuals, which increases uncertainty.
- **Hint:** Where does random error in the response end up in a regression?

### ch19-quiz-08-v1
- **Kind:** AI-written version of ch19-quiz-08
- **Concepts:** Measurement error & causation
- **Type:** select-all
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

If we measured territory size (y) perfectly, instead of with random error, what would we expect? (Select all that apply.)

- **Options:**

  A) The estimated slope would tend to be farther from zero
  B) The estimated slope would be no more or less biased
  C) The slope's uncertainty would be smaller
  D) The slope's uncertainty would be larger

- **Answer (tutor only):** B, C
- **Explanation (tutor only):** Error in y doesn't bias the slope, so removing it doesn't change bias, but it reduces residual scatter and the SE.
- **Why the wrong options are wrong (tutor only):**
  A) Error in y doesn't bias the slope.
  D) Less error means less uncertainty.
- **Hint:** Error in y vs error in x.

### ch19-quiz-08-v2
- **Kind:** AI-written version of ch19-quiz-08
- **Concepts:** Measurement error & causation
- **Type:** select-all
- **Question:**

A biologist measures metabolic rate (y) with a lot of random error and regresses it on body size (x), measured precisely. The estimated slope is likely to be: (Select all that apply.)

- **Options:**

  A) Unbiased, but with a larger standard error
  B) Biased toward zero, with a smaller standard error
  C) Biased away from zero, with a larger standard error
  D) Biased toward zero, with the same standard error

- **Answer (tutor only):** A
- **Explanation (tutor only):** Random error in y just adds residual scatter: no bias, more uncertainty.
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) Error in y doesn't bias the slope.
- **Hint:** Which variable has the error?

### ch19-quiz-09
- **Kind:** Course original
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

lm(territory ~ bite, data = lizards)

term | estimate | std.error | conf.low | conf.high
(Intercept) | -31.54 | 23.51 | -84.73 | 21.65
bite | 11.68 | 4.85 | 0.71 | 22.64

R² = 0.392; F = 5.80 on 1 and 9 df; p = 0.039

At α = 0.05, what do we do with the null hypothesis (slope = 0), and what does that mean?

- **Options:**

  A) Reject it; the null is false
  B) Reject it; but the null could still be true
  C) Fail to reject it; the null is true
  D) Fail to reject it; we can't say for sure

- **Answer (tutor only):** B
- **Explanation (tutor only):** p = 0.039 < 0.05, so we reject. That doesn't prove the null false, especially with 11 lizards and a p-value near the threshold.
- **Why the wrong options are wrong (tutor only):**
  A) Rejecting isn't proof.
  C) and D) p is below α.
- **Hint:** Compare p with α, then think about what a p-value can't do.

### ch19-quiz-09-v1
- **Kind:** AI-written version of ch19-quiz-09
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

Suppose a second study of 11 lizards found p = 0.21 for the slope. At α = 0.05, what do we do, and what does it mean?

- **Options:**

  A) Reject; bite force predicts territory size
  B) Reject; we can't say for sure whether the null is true
  C) Fail to reject; bite force has no effect
  D) Fail to reject; we can't say for sure

- **Answer (tutor only):** D
- **Explanation (tutor only):** p > 0.05, so we fail to reject. With only 11 lizards we may lack power; this isn't evidence of no effect.
- **Why the wrong options are wrong (tutor only):**
  A) and B) p > α.
  C) Failing to reject isn't proof.
- **Hint:** Compare p with 0.05.

### ch19-quiz-09-v2
- **Kind:** AI-written version of ch19-quiz-09
- **Concepts:** Sums of squares, F & R²
- **Type:** MC
- **Question:**

Male collared lizards (Crotaphytus collaris) use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts territory size in 11 males (bite force ranged from 4.3 to 5.4 N).

lm(territory ~ bite, data = lizards)

term | estimate | std.error | conf.low | conf.high
(Intercept) | -31.54 | 23.51 | -84.73 | 21.65
bite | 11.68 | 4.85 | 0.71 | 22.64

R² = 0.392; F = 5.80 on 1 and 9 df; p = 0.039

The slope's p-value is 0.039 and its 95% CI is 0.71 to 22.64. How are these consistent?

- **Options:**

  A) p < 0.05, and the CI excludes zero
  B) p < 0.05, and the CI includes zero
  C) p > 0.05, and the CI excludes zero
  D) They aren't consistent with each other

- **Answer (tutor only):** A
- **Explanation (tutor only):** A two-tailed test at α = 0.05 rejects exactly when the 95% CI excludes the null value (0).
- **Why the wrong options are wrong (tutor only):**
  B) The CI excludes zero.
  C) p < 0.05.
  D) They agree.
- **Hint:** Is 0 in the CI?
