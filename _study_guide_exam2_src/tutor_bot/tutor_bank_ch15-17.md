# Applied Biostats tutor: question bank, chapters 15–17 (Exam 2, chapters 13–21, plus an Exam 1 review as chapter 0)

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

## Chapter 15: The t distribution

### ch15-book-01
- **Kind:** Course original
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

The difference between a t value and a z value is:

- **Options:**

  A) The z assumes the mean is zero; the t does not
  B) The z assumes samples come from a normal distribution; the t does not
  C) The z assumes we know the population SD; the t uses an estimate

- **Answer (tutor only):** C
- **Explanation (tutor only):** Both assume normality. The t adds uncertainty because the SD is estimated from the sample.
- **Why the wrong options are wrong (tutor only):**
  A) Both are calculated relative to a null value, which need not be zero.
  B) The t also assumes (approximate) normality.
- **Hint:** Where does the SD in each formula come from?

### ch15-book-01-v1
- **Kind:** AI-written version of ch15-book-01
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

Which assumption do the z and t share?

- **Options:**

  A) The sampling distribution of the estimate is normal
  B) The population standard deviation is known
  C) The population mean is exactly zero
  D) The sample size is larger than 100

- **Answer (tutor only):** A
- **Explanation (tutor only):** Both assume a normal sampling distribution. Only z assumes σ is known.
- **Why the wrong options are wrong (tutor only):**
  B) Only z assumes that.
  C) Neither does.
  D) Neither requires this.
- **Hint:** What do both rely on?

### ch15-book-01-v2
- **Kind:** AI-written version of ch15-book-01
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

A t-based test differs from a z-based test because the t:

- **Options:**

  A) Assumes the true mean is zero
  B) Is only for comparing two groups
  C) Does not assume normality at all
  D) Uses an SD estimated from the sample

- **Answer (tutor only):** D
- **Explanation (tutor only):** The t accounts for estimating the SD from the sample.
- **Why the wrong options are wrong (tutor only):**
  A) Neither assumes that.
  B) The t is used for one sample, two samples and more.
  C) Both assume normality.
- **Hint:** What does the t not know?

### ch15-book-02
- **Kind:** Course original
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

If our sample is not perfectly normal:

- **Options:**

  A) We cannot use t-based tests at all, as they assume normality
  B) We can, if n is large and the deviations are modest (thanks to the CLT)
  C) It has no impact; that's why we use a t distribution instead of a z

- **Answer (tutor only):** B
- **Explanation (tutor only):** t-tests are robust to modest non-normality, especially in larger samples, because sampling distributions of means become roughly normal.
- **Why the wrong options are wrong (tutor only):**
  A) Perfect normality is never required (and never true).
  C) The t handles an estimated SD, not non-normality.
- **Hint:** Which theorem is about means of large samples?

### ch15-book-02-v1
- **Kind:** AI-written version of ch15-book-02
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

A sample of 80 leaf areas is slightly right-skewed. Can we use a t-test?

- **Options:**

  A) No: t-tests require perfectly normal data
  B) Yes: the t is designed to correct for skewed data
  C) No: skewed data can never be analyzed with t
  D) Yes, probably: the CLT makes the mean nearly normal

- **Answer (tutor only):** D
- **Explanation (tutor only):** With 80 observations and mild skew, the sampling distribution of the mean is close to normal.
- **Why the wrong options are wrong (tutor only):**
  A) and C) Perfect normality isn't required.
  B) The t corrects for estimating the SD, not for skew.
- **Hint:** Central limit theorem.

### ch15-book-02-v2
- **Kind:** AI-written version of ch15-book-02
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

Which situation is the BIGGEST concern for using a t-test?

- **Options:**

  A) A large sample with normal data
  B) A small sample with normal data
  C) A large sample with mild skew
  D) A small sample with strong skew

- **Answer (tutor only):** D
- **Explanation (tutor only):** Strong skew with few observations means the CLT can't make the sampling distribution normal.
- **Why the wrong options are wrong (tutor only):**
  A) and B) Normal data are fine.
  C) The CLT handles mild skew in large samples.
- **Hint:** When can't the CLT help?

### ch15-book-03
- **Kind:** Course original
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

The t and z distributions are never perfectly identical. When are they very close to one another?

- **Options:**

  A) When the sample size is large
  B) When the standard deviation is small
  C) When the data are normal
  D) Never: they are very different distributions

- **Answer (tutor only):** A
- **Explanation (tutor only):** As df grow, the estimated SD gets more precise and the t converges to the z.
- **Why the wrong options are wrong (tutor only):**
  B) The size of the SD doesn't change the shape of t.
  C) Normal data don't remove the extra uncertainty from estimating the SD.
  D) They converge with large samples.
- **Hint:** What happens to the t's fat tails as the sample grows?

### ch15-book-03-v1
- **Kind:** AI-written version of ch15-book-03
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

With which degrees of freedom are the t and z distributions most different?

- **Options:**

  A) 20 df
  B) They're equally different at every df
  C) 200 df
  D) 2 df

- **Answer (tutor only):** D
- **Explanation (tutor only):** With very few df, the t has much fatter tails; it approaches z as df grow.
- **Why the wrong options are wrong (tutor only):**
  A) and C) t is closer to z there.
  B) The difference shrinks with df.
- **Hint:** When is the SD estimate least reliable?

### ch15-book-03-v2
- **Kind:** AI-written version of ch15-book-03
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

Why does the t approach the z as sample size grows?

- **Options:**

  A) The SD estimate gets more precise, adding less uncertainty
  B) The null hypothesis becomes more likely to be true
  C) The data themselves become more normally distributed
  D) The sample mean gets closer and closer to zero

- **Answer (tutor only):** A
- **Explanation (tutor only):** With many observations, the estimated SD is close to σ, so the extra uncertainty that fattens t's tails disappears.
- **Why the wrong options are wrong (tutor only):**
  C) Data keep their shape.
  D) and B) Irrelevant to the t's shape.
- **Hint:** What extra uncertainty does the t include?

### ch15-book-04
- **Kind:** Course original
- **Concepts:** Effect size & CIs
- **Type:** MC
- **Question:**

Which is the best summary of the effect size for normally distributed data?

- **Options:**

  A) The p-value
  B) The difference between the estimate and its null value
  C) The difference between the estimate and its null value, standardized by the standard deviation
  D) The difference between the estimate and its null value, standardized by the standard error

- **Answer (tutor only):** C
- **Explanation (tutor only):** That's Cohen's d: the difference in SD units, comparable across studies and independent of sample size.
- **Why the wrong options are wrong (tutor only):**
  A) p depends on sample size.
  B) Useful, but depends on units.
  D) That's t, which grows with sample size.
- **Hint:** Which one doesn't change if you collect more data?

### ch15-book-04-v1
- **Kind:** AI-written version of ch15-book-04
- **Concepts:** Effect size & CIs
- **Type:** MC
- **Question:**

Two studies of beak depth find mean differences of 0.5 mm and 0.6 mm from the null value. The SDs are 0.25 mm and 1.2 mm. Which study has the larger effect size?

- **Options:**

  A) The first: d = 2.0 vs d = 0.5
  B) The second: its difference is larger
  C) They are equal, since the differences are similar
  D) Can't tell without the p-values

- **Answer (tutor only):** A
- **Explanation (tutor only):** d = difference / SD: 0.5 / 0.25 = 2.0 versus 0.6 / 1.2 = 0.5.
- **Why the wrong options are wrong (tutor only):**
  B) Raw differences ignore spread.
  C) Standardizing by SD makes them very different.
  D) Effect size doesn't need p.
- **Hint:** Standardize by the SD.

### ch15-book-04-v2
- **Kind:** AI-written version of ch15-book-04
- **Concepts:** Effect size & CIs
- **Type:** MC
- **Question:**

Why is effect size standardized by the SD rather than by the SE?

- **Options:**

  A) The SE describes variation among individuals
  B) The SD doesn't shrink with sample size
  C) The SD always gives a larger effect size
  D) The SE is harder to calculate than the SD

- **Answer (tutor only):** B
- **Explanation (tutor only):** Dividing by the SE would make the 'effect size' grow with n (that's t). The SD keeps it independent of sample size.
- **Why the wrong options are wrong (tutor only):**
  A) The SD describes individuals; the SE describes estimates.
  C) Dividing by the larger SD gives a smaller value.
  D) The SE is easy: SD / √n.
- **Hint:** Which one depends on n?

### ch15-book-05
- **Kind:** Course original
- **Concepts:** t vs z
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch15-book-hyena-qq.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch15-book-hyena-qq.png)
- **Question:**

To ask whether hyena "laughter" signals social rank, Mathevon et al. (2010) measured giggling in nine natural pairs of one dominant and one subordinate hyena (differences are subordinate minus dominant):

pair | dominant | subordinate | diff
1 | 0.384 | 0.507 | 0.123
2 | 0.386 | 0.569 | 0.183
3 | 0.252 | 0.235 | -0.017
4 | 0.226 | 0.415 | 0.189
5 | 0.323 | 0.436 | 0.113
6 | 0.287 | 0.451 | 0.164
7 | 0.303 | 0.399 | 0.096
8 | 0.317 | 0.220 | -0.097
9 | 0.277 | 0.338 | 0.061

Mean difference = 0.0906; SD of the differences = 0.0954.

The QQ plot of the nine differences is shown. Evaluate it in relation to the normality assumption.

- **Options:**

  A) The data are perfectly normal
  B) The data likely deviate somewhat from normality, but a t-test is probably OK
  C) The data deviate strongly from normality, so any test assuming normality can't be trusted

- **Answer (tutor only):** B
- **Explanation (tutor only):** The points follow the line reasonably well, with some wobble at the ends, which is expected with only nine points. Nothing suggests a serious problem.
- **Why the wrong options are wrong (tutor only):**
  A) Real data are never perfectly normal.
  C) The departures are modest; with nine points some scatter around the line is normal.
- **Hint:** With only nine points, how closely would you expect them to follow the line?

### ch15-book-05-v1
- **Kind:** AI-written version of ch15-book-05
- **Concepts:** t vs z
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch15-book-hyena-qq.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch15-book-hyena-qq.png)
- **Question:**

To ask whether hyena "laughter" signals social rank, Mathevon et al. (2010) measured giggling in nine natural pairs of one dominant and one subordinate hyena (differences are subordinate minus dominant):

pair | dominant | subordinate | diff
1 | 0.384 | 0.507 | 0.123
2 | 0.386 | 0.569 | 0.183
3 | 0.252 | 0.235 | -0.017
4 | 0.226 | 0.415 | 0.189
5 | 0.323 | 0.436 | 0.113
6 | 0.287 | 0.451 | 0.164
7 | 0.303 | 0.399 | 0.096
8 | 0.317 | 0.220 | -0.097
9 | 0.277 | 0.338 | 0.061

Mean difference = 0.0906; SD of the differences = 0.0954.

The QQ plot of the nine differences is shown. Which feature would most worry you about the normality assumption?

- **Options:**

  A) Points wobbling a little around the line at the ends
  B) The plot having only nine points
  C) Points that are exactly on the line from end to end
  D) Points curving far from the line, e.g. a strong bend

- **Answer (tutor only):** D
- **Explanation (tutor only):** A systematic curve suggests skew. Small wobbles are expected, especially with few points.
- **Why the wrong options are wrong (tutor only):**
  A) Expected with small samples.
  B) Few points make the plot noisy but aren't a violation.
  C) That would be reassuring.
- **Hint:** Wobble vs systematic curve.

### ch15-book-05-v2
- **Kind:** AI-written version of ch15-book-05
- **Concepts:** t vs z
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch15-book-hyena-qq.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch15-book-hyena-qq.png)
- **Question:**

To ask whether hyena "laughter" signals social rank, Mathevon et al. (2010) measured giggling in nine natural pairs of one dominant and one subordinate hyena (differences are subordinate minus dominant):

pair | dominant | subordinate | diff
1 | 0.384 | 0.507 | 0.123
2 | 0.386 | 0.569 | 0.183
3 | 0.252 | 0.235 | -0.017
4 | 0.226 | 0.415 | 0.189
5 | 0.323 | 0.436 | 0.113
6 | 0.287 | 0.451 | 0.164
7 | 0.303 | 0.399 | 0.096
8 | 0.317 | 0.220 | -0.097
9 | 0.277 | 0.338 | 0.061

Mean difference = 0.0906; SD of the differences = 0.0954.

For a paired t-test, which values should be checked for normality?

- **Options:**

  A) All 18 values pooled together
  B) The nine differences
  C) The dominant values only
  D) The dominant and subordinate values separately

- **Answer (tutor only):** B
- **Explanation (tutor only):** A paired t-test is a one-sample t-test on the differences, so it assumes the differences are normal.
- **Why the wrong options are wrong (tutor only):**
  D), C) and A) The test is on the differences.
- **Hint:** What does the paired t-test analyze?

### ch15-book-06
- **Kind:** Course original
- **Concepts:** The t statistic & SE; Paired designs
- **Type:** numeric
- **Question:**

To ask whether hyena "laughter" signals social rank, Mathevon et al. (2010) measured giggling in nine natural pairs of one dominant and one subordinate hyena (differences are subordinate minus dominant):

pair | dominant | subordinate | diff
1 | 0.384 | 0.507 | 0.123
2 | 0.386 | 0.569 | 0.183
3 | 0.252 | 0.235 | -0.017
4 | 0.226 | 0.415 | 0.189
5 | 0.323 | 0.436 | 0.113
6 | 0.287 | 0.451 | 0.164
7 | 0.303 | 0.399 | 0.096
8 | 0.317 | 0.220 | -0.097
9 | 0.277 | 0.338 | 0.061

Mean difference = 0.0906; SD of the differences = 0.0954.

How many standard errors away from zero is the mean difference in giggling? (That is, what is t?)

- **Answer (tutor only):** 2.85
- **Explanation (tutor only):** SE = 0.0954 / √9 = 0.0318. t = 0.0906 / 0.0318 = 2.85.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: dividing by the SD instead of the SE (gives 0.95, Cohen's d).
- **Hint:** First find the SE = SD / √n.

### ch15-book-06-v1
- **Kind:** AI-written version of ch15-book-06
- **Concepts:** The t statistic & SE; Paired designs
- **Type:** numeric
- **Question:**

To ask whether hyena "laughter" signals social rank, Mathevon et al. (2010) measured giggling in nine natural pairs of one dominant and one subordinate hyena (differences are subordinate minus dominant):

pair | dominant | subordinate | diff
1 | 0.384 | 0.507 | 0.123
2 | 0.386 | 0.569 | 0.183
3 | 0.252 | 0.235 | -0.017
4 | 0.226 | 0.415 | 0.189
5 | 0.323 | 0.436 | 0.113
6 | 0.287 | 0.451 | 0.164
7 | 0.303 | 0.399 | 0.096
8 | 0.317 | 0.220 | -0.097
9 | 0.277 | 0.338 | 0.061

Mean difference = 0.0906; SD of the differences = 0.0954.

What is the standard error of the mean difference?

- **Answer (tutor only):** 0.0318
- **Explanation (tutor only):** SE = 0.0954 / √9 = 0.0954 / 3 = 0.0318.
- **Hint:** SD / √n.

### ch15-book-06-v2
- **Kind:** AI-written version of ch15-book-06
- **Concepts:** The t statistic & SE; Paired designs
- **Type:** numeric
- **Question:**

To ask whether hyena "laughter" signals social rank, Mathevon et al. (2010) measured giggling in nine natural pairs of one dominant and one subordinate hyena (differences are subordinate minus dominant):

pair | dominant | subordinate | diff
1 | 0.384 | 0.507 | 0.123
2 | 0.386 | 0.569 | 0.183
3 | 0.252 | 0.235 | -0.017
4 | 0.226 | 0.415 | 0.189
5 | 0.323 | 0.436 | 0.113
6 | 0.287 | 0.451 | 0.164
7 | 0.303 | 0.399 | 0.096
8 | 0.317 | 0.220 | -0.097
9 | 0.277 | 0.338 | 0.061

Mean difference = 0.0906; SD of the differences = 0.0954.

What is Cohen's d for the difference in giggling?

- **Answer (tutor only):** 0.95
- **Explanation (tutor only):** d = 0.0906 / 0.0954 = 0.95, a large effect.
- **Hint:** Mean difference ÷ SD.

### ch15-book-07
- **Kind:** Course original
- **Concepts:** Effect size & CIs
- **Type:** MC
- **Question:**

The 95% CI is calculated as the estimate ± the critical t value (at α = 0.05) times ____.

- **Options:**

  A) Cohen's d
  B) The standard deviation
  C) The variance
  D) t
  E) The standard error
  F) 1.96

- **Answer (tutor only):** E
- **Explanation (tutor only):** CI = estimate ± critical t × SE.
- **Why the wrong options are wrong (tutor only):**
  B) Using the SD would describe where individuals fall, not uncertainty in the estimate.
  F) 1.96 is the z critical value; with the t we use the critical t.
- **Hint:** Which quantity describes uncertainty in the estimate?

### ch15-book-07-v1
- **Kind:** AI-written version of ch15-book-07
- **Concepts:** Effect size & CIs
- **Type:** MC
- **Question:**

A 95% CI is calculated as the estimate ± ____ × the standard error.

- **Options:**

  A) the p-value
  B) Cohen's d
  C) the observed t value
  D) the critical t value

- **Answer (tutor only):** D
- **Explanation (tutor only):** CI = estimate ± critical t × SE.
- **Why the wrong options are wrong (tutor only):**
  B) and A) Not used to build the CI.
  C) The observed t is for the test.
- **Hint:** Which t is a cutoff?

### ch15-book-07-v2
- **Kind:** AI-written version of ch15-book-07
- **Concepts:** Effect size & CIs
- **Type:** MC
- **Question:**

Which change would make a 95% confidence interval narrower?

- **Options:**

  A) A larger standard deviation
  B) Using fewer degrees of freedom
  C) Using a 99% interval instead
  D) A larger sample size

- **Answer (tutor only):** D
- **Explanation (tutor only):** Larger n shrinks the SE (and slightly the critical t).
- **Why the wrong options are wrong (tutor only):**
  A) Larger SD widens the CI.
  B) Fewer df means a larger critical t.
  C) 99% needs a larger critical value.
- **Hint:** What shrinks the SE?

### ch15-book-08
- **Kind:** Course original
- **Concepts:** t vs z; The t statistic & SE
- **Type:** MC
- **Question:**

For the nine hyena pairs (8 df), which R code gives the (absolute) critical t value for a two-tailed 95% confidence interval?

- **Options:**

  A) qt(0.025, df = 8, lower.tail = FALSE)
  B) qt(0.05, df = 8, lower.tail = FALSE)
  C) pt(0.025, df = 8)
  D) qt(0.025, df = 9, lower.tail = FALSE)

- **Answer (tutor only):** A
- **Explanation (tutor only):** A two-tailed 95% interval leaves 2.5% in each tail, and a paired test with nine pairs has 9 - 1 = 8 df. qt(0.025, 8, lower.tail = FALSE) = 2.31.
- **Why the wrong options are wrong (tutor only):**
  B) 0.05 in one tail gives a 90% two-tailed interval.
  C) pt() returns a probability, not a quantile.
  D) Wrong df: n - 1 = 8.
- **Hint:** How much area goes in each tail? How many df?

### ch15-book-08-v1
- **Kind:** AI-written version of ch15-book-08
- **Concepts:** t vs z; The t statistic & SE
- **Type:** MC
- **Question:**

For a paired study of 12 pairs, which R code gives the critical t value for a two-tailed 95% confidence interval?

- **Options:**

  A) pt(0.025, df = 11)
  B) qt(0.05, df = 11, lower.tail = FALSE)
  C) qt(0.025, df = 11, lower.tail = FALSE)
  D) qt(0.025, df = 12, lower.tail = FALSE)

- **Answer (tutor only):** C
- **Explanation (tutor only):** 2.5% in each tail; df = 12 pairs - 1 = 11.
- **Why the wrong options are wrong (tutor only):**
  A) pt() returns a probability.
  B) That's for a 90% two-tailed interval.
  D) df is pairs - 1.
- **Hint:** df = pairs - 1; 2.5% per tail.

### ch15-book-08-v2
- **Kind:** AI-written version of ch15-book-08
- **Concepts:** t vs z; The t statistic & SE
- **Type:** MC
- **Question:**

For the nine hyena pairs, which R code gives the critical t value for a two-tailed 99% confidence interval?

- **Options:**

  A) qt(0.005, df = 9, lower.tail = FALSE)
  B) qt(0.025, df = 8, lower.tail = FALSE)
  C) qt(0.01, df = 8, lower.tail = FALSE)
  D) qt(0.005, df = 8, lower.tail = FALSE)

- **Answer (tutor only):** D
- **Explanation (tutor only):** A 99% two-tailed interval leaves 0.5% in each tail; df = 9 - 1 = 8.
- **Why the wrong options are wrong (tutor only):**
  A) df should be 8.
  B) That's for 95%.
  C) That puts 1% in each tail (98% CI).
- **Hint:** Split 1% between two tails.

### ch15-book-09
- **Kind:** Course original
- **Concepts:** t vs z; p-values & NHST
- **Type:** MC
- **Question:**

To ask whether hyena "laughter" signals social rank, Mathevon et al. (2010) measured giggling in nine natural pairs of one dominant and one subordinate hyena (differences are subordinate minus dominant):

pair | dominant | subordinate | diff
1 | 0.384 | 0.507 | 0.123
2 | 0.386 | 0.569 | 0.183
3 | 0.252 | 0.235 | -0.017
4 | 0.226 | 0.415 | 0.189
5 | 0.323 | 0.436 | 0.113
6 | 0.287 | 0.451 | 0.164
7 | 0.303 | 0.399 | 0.096
8 | 0.317 | 0.220 | -0.097
9 | 0.277 | 0.338 | 0.061

Mean difference = 0.0906; SD of the differences = 0.0954.

t = 2.85 and the critical t value is 2.31 (8 df, α = 0.05). What should we conclude?

- **Options:**

  A) Reject the null, since t exceeds the critical value; we could be wrong
  B) Fail to reject the null, since t exceeds the critical value
  C) We can't know what to do until we find the exact p-value
  D) Reject the null, which proves that subordinates giggle more

- **Answer (tutor only):** A
- **Explanation (tutor only):** |t| exceeds the critical value, so p < 0.05 (it's 0.022). We act as if the null is false while acknowledging a real chance of a type I error.
- **Why the wrong options are wrong (tutor only):**
  B) A t beyond the critical value means rejection.
  C) Comparing t to the critical value gives the same decision as comparing p to α.
  D) Rejecting the null doesn't prove anything.
- **Hint:** Being beyond the critical value is the same as p < α.

### ch15-book-09-v1
- **Kind:** AI-written version of ch15-book-09
- **Concepts:** t vs z; p-values & NHST
- **Type:** MC
- **Question:**

To ask whether hyena "laughter" signals social rank, Mathevon et al. (2010) measured giggling in nine natural pairs of one dominant and one subordinate hyena (differences are subordinate minus dominant):

pair | dominant | subordinate | diff
1 | 0.384 | 0.507 | 0.123
2 | 0.386 | 0.569 | 0.183
3 | 0.252 | 0.235 | -0.017
4 | 0.226 | 0.415 | 0.189
5 | 0.323 | 0.436 | 0.113
6 | 0.287 | 0.451 | 0.164
7 | 0.303 | 0.399 | 0.096
8 | 0.317 | 0.220 | -0.097
9 | 0.277 | 0.338 | 0.061

Mean difference = 0.0906; SD of the differences = 0.0954.

Suppose t had been 1.9, with a critical t value of 2.31 (8 df, α = 0.05). What should we conclude?

- **Options:**

  A) Fail to reject: |t| is below the critical value
  B) Reject: |t| is close to the critical value
  C) Fail to reject, so subordinates and dominants giggle equally
  D) Reject, because t is positive in this study

- **Answer (tutor only):** A
- **Explanation (tutor only):** |t| < critical t means p > 0.05, so we fail to reject. That doesn't show no difference.
- **Why the wrong options are wrong (tutor only):**
  B) Close doesn't count.
  C) Failing to reject isn't proof of no difference.
  D) The sign doesn't decide significance.
- **Hint:** Compare |t| with 2.31.

### ch15-book-09-v2
- **Kind:** AI-written version of ch15-book-09
- **Concepts:** t vs z; p-values & NHST
- **Type:** MC
- **Question:**

To ask whether hyena "laughter" signals social rank, Mathevon et al. (2010) measured giggling in nine natural pairs of one dominant and one subordinate hyena (differences are subordinate minus dominant):

pair | dominant | subordinate | diff
1 | 0.384 | 0.507 | 0.123
2 | 0.386 | 0.569 | 0.183
3 | 0.252 | 0.235 | -0.017
4 | 0.226 | 0.415 | 0.189
5 | 0.323 | 0.436 | 0.113
6 | 0.287 | 0.451 | 0.164
7 | 0.303 | 0.399 | 0.096
8 | 0.317 | 0.220 | -0.097
9 | 0.277 | 0.338 | 0.061

Mean difference = 0.0906; SD of the differences = 0.0954.

t = 2.85 and p = 0.022. Which statement is correct?

- **Options:**

  A) We fail to reject, because 2.85 is larger than 2.31
  B) There's a 2.2% chance subordinates giggle the same amount
  C) We reject the null, which proves subordinates giggle more
  D) We reject the null, but could be making a type I error

- **Answer (tutor only):** D
- **Explanation (tutor only):** p < 0.05, so we reject, accepting a chance of a false positive.
- **Why the wrong options are wrong (tutor only):**
  A) |t| > critical t means reject.
  B) p isn't the probability the null is true.
  C) Rejection isn't proof.
- **Hint:** What can p < α not guarantee?

### ch15-book-10
- **Kind:** Course original
- **Concepts:** p-values & NHST
- **Type:** MC
- **Question:**

Say you found a p-value of p. Which is a correct interpretation?

- **Options:**

  A) p is the probability that the null hypothesis generated the data
  B) p is the probability that the null hypothesis is true
  C) p is the probability that a random sample from the null distribution would be as or more extreme than our data

- **Answer (tutor only):** C
- **Explanation (tutor only):** A p-value is calculated assuming the null is true: how often would the null produce a result at least this extreme?
- **Why the wrong options are wrong (tutor only):**
  A) and B) Both treat p as a probability about the null itself, which it isn't.
- **Hint:** Is p calculated assuming the null is true?

### ch15-book-10-v1
- **Kind:** AI-written version of ch15-book-10
- **Concepts:** p-values & NHST
- **Type:** MC
- **Question:**

A study reports p = 0.01. Which interpretation is correct?

- **Options:**

  A) The effect is large, because p is small
  B) There is a 1% chance the null hypothesis is true
  C) There is a 99% chance the alternative hypothesis is true
  D) If the null were true, 1% of samples would be this extreme or more

- **Answer (tutor only):** D
- **Explanation (tutor only):** p is calculated assuming the null is true.
- **Why the wrong options are wrong (tutor only):**
  A) Small p can come from a tiny effect in a big sample.
  B) and C) p is not a probability about hypotheses.
- **Hint:** What does p assume?

### ch15-book-10-v2
- **Kind:** AI-written version of ch15-book-10
- **Concepts:** p-values & NHST
- **Type:** MC
- **Question:**

Which statement about p-values is FALSE?

- **Options:**

  A) Smaller p-values mean data less compatible with the null
  B) A p-value depends on both effect size and sample size
  C) A p-value is calculated assuming the null is true
  D) A p-value is the probability that the null is true

- **Answer (tutor only):** D
- **Explanation (tutor only):** p is P(data this extreme | null), not P(null | data).
- **Why the wrong options are wrong (tutor only):**
  C), A) and B) are all true.
- **Hint:** Look for the reversed conditional.

### ch15-book-11
- **Kind:** Course original
- **Concepts:** Paired designs
- **Type:** TF
- **Question:**

Say you had data from two more dominant and two more subordinate hyenas, but they weren't in pairs. Would it be legitimate to pair them at random and do a paired t-test?

- **Options:**

  A) Yes
  B) No

- **Answer (tutor only):** B
- **Explanation (tutor only):** Pairs must share something real (here, living together). Random pairs share nothing, so the paired analysis would be invalid; use a two-sample approach instead.
- **Why the wrong options are wrong (tutor only):**
  A) Random pairing creates the appearance of a design that doesn't exist.
- **Hint:** What makes a pair a pair?

### ch15-book-11-v1
- **Kind:** AI-written version of ch15-book-11
- **Concepts:** Paired designs
- **Type:** MC
- **Question:**

A researcher measured giggling in 10 dominant and 10 subordinate hyenas from different groups. Is a paired t-test appropriate?

- **Options:**

  A) Yes
  B) No

- **Answer (tutor only):** B
- **Explanation (tutor only):** The hyenas aren't in natural pairs (they don't share a group), so a two-sample test is appropriate.
- **Why the wrong options are wrong (tutor only):**
  A) Equal group sizes don't create pairs.
- **Hint:** Is there a real basis for pairing?

### ch15-book-11-v2
- **Kind:** AI-written version of ch15-book-11
- **Concepts:** Paired designs
- **Type:** MC
- **Question:**

A researcher measured giggling in the same hyenas when they were dominant in one group and subordinate after moving to another. Is a paired t-test appropriate?

- **Options:**

  A) Yes
  B) No

- **Answer (tutor only):** A
- **Explanation (tutor only):** Each hyena is measured twice (repeated measures), so the two measurements form a natural pair.
- **Why the wrong options are wrong (tutor only):**
  B) The same individual measured twice is a natural pair.
- **Hint:** Same individual, two conditions.

### ch15-chimein-01
- **Kind:** Course original
- **Concepts:** The t statistic & SE
- **Type:** matching
- **Question:**

Fill in the blanks: A t value is the distance in (1) ____ between a parameter estimate and its (2) ____ value.

- **Options:**

  A) standard deviations
  B) null
  C) standard errors
  D) true

- **Answer (tutor only):** 1-C, 2-B
- **Explanation (tutor only):** t = (estimate - null value) / SE: how many standard errors the estimate is from the null.
- **Why the wrong options are wrong (tutor only):**
  Common mix-ups: standard deviations (that's Cohen's d) and the true value (which we don't know).
- **Hint:** What's in the denominator of t?

### ch15-chimein-01-v1
- **Kind:** AI-written version of ch15-chimein-01
- **Concepts:** The t statistic & SE
- **Type:** MC
- **Question:**

A t value of -3 means that the parameter estimate is:

- **Options:**

  A) 3 times smaller than its null value
  B) 3 standard deviations below its null value
  C) 3 standard errors below its null value
  D) 3 units below its true population value

- **Answer (tutor only):** C
- **Explanation (tutor only):** t = (estimate - null) / SE: the distance from the null in standard errors.
- **Why the wrong options are wrong (tutor only):**
  B) That would be like Cohen's d.
  D) and A) t is in SE units, measured from the null.
- **Hint:** t's denominator is the SE.

### ch15-chimein-01-v2
- **Kind:** AI-written version of ch15-chimein-01
- **Concepts:** The t statistic & SE
- **Type:** matching
- **Question:**

Fill in the blanks: t = (1) ____ minus its null value, divided by its (2) ____.

- **Options:**

  A) standard error
  B) the estimate
  C) the true parameter
  D) standard deviation

- **Answer (tutor only):** 1-B, 2-A
- **Explanation (tutor only):** t = (estimate - null) / SE.
- **Why the wrong options are wrong (tutor only):**
  We never know the true parameter; dividing by the SD gives an effect size.
- **Hint:** What do we actually have from the sample?

### ch15-chimein-02
- **Kind:** Course original
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

The main difference between a t value and a z value is that for t we estimate the standard error from the sample. As a consequence, compared to the z (standard normal) distribution, the t distribution has:

- **Options:**

  A) A taller peak
  B) Fatter tails
  C) More tolerance for non-independence
  D) No symmetry around its mean

- **Answer (tutor only):** B
- **Explanation (tutor only):** Estimating the SE adds uncertainty, so extreme t values are more common than extreme z values: the t has fatter tails (and needs a larger critical value).
- **Why the wrong options are wrong (tutor only):**
  A) The t's peak is actually a bit lower.
  C) Non-independence is a problem for both.
  D) The t is symmetric.
- **Hint:** More uncertainty means extreme values are more likely.

### ch15-chimein-02-v1
- **Kind:** AI-written version of ch15-chimein-02
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

Because the t distribution has fatter tails than the z, the critical value for a 95% confidence interval with a small sample is:

- **Options:**

  A) Exactly 1.96
  B) Larger than 1.96
  C) Negative
  D) Smaller than 1.96

- **Answer (tutor only):** B
- **Explanation (tutor only):** Fatter tails push 2.5% of the area farther out, so the critical t exceeds 1.96 (e.g. 2.78 for 4 df).
- **Why the wrong options are wrong (tutor only):**
  C) We use the absolute value.
  D) and A) Fatter tails mean a larger cutoff.
- **Hint:** Where does the outer 2.5% start in a fat-tailed distribution?

### ch15-chimein-02-v2
- **Kind:** AI-written version of ch15-chimein-02
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

Why does the t distribution have fatter tails than the standard normal (z)?

- **Options:**

  A) Because biological data are skewed, adding extreme values
  B) Because the t is used only for paired data, not independent data
  C) Because the null hypothesis is usually false in real studies
  D) Because the SD is estimated from the sample, adding uncertainty

- **Answer (tutor only):** D
- **Explanation (tutor only):** Estimating the SD (and so the SE) adds uncertainty, making extreme t values more common.
- **Why the wrong options are wrong (tutor only):**
  A) The t assumes normal data.
  B) The t is used for many tests.
  C) Tails come from the sampling math, not the truth of the null.
- **Hint:** What does the t estimate that the z knows?

### ch15-chimein-03
- **Kind:** Course original
- **Concepts:** p-values & NHST
- **Type:** MC
- **Question:**

A very low p-value means that ____ rarely produces a sample as extreme as ours (or more extreme).

- **Options:**

  A) Sampling error
  B) Sampling bias
  C) The alternative model
  D) Non-independence

- **Answer (tutor only):** A
- **Explanation (tutor only):** A p-value asks how often chance alone (sampling error when the null is true) would give a result at least as extreme as ours.
- **Why the wrong options are wrong (tutor only):**
  B) A p-value assumes no bias; it can't detect it.
  C) The p-value is calculated under the null, not the alternative.
  D) Non-independence violates the test's assumptions; it isn't what p measures.
- **Hint:** What model is the p-value calculated under?

### ch15-chimein-03-v1
- **Kind:** AI-written version of ch15-chimein-03
- **Concepts:** p-values & NHST
- **Type:** MC
- **Question:**

A large p-value (say 0.6) means that, if the null were true, sampling error would ____ produce a sample as extreme as ours (or more extreme).

- **Options:**

  A) often
  B) always
  C) rarely
  D) never

- **Answer (tutor only):** A
- **Explanation (tutor only):** p = 0.6 means 60% of samples under the null would be at least as extreme: very common.
- **Why the wrong options are wrong (tutor only):**
  C) That's a small p.
  D) and B) p is between 0 and 1.
- **Hint:** What fraction of null samples are this extreme?

### ch15-chimein-03-v2
- **Kind:** AI-written version of ch15-chimein-03
- **Concepts:** p-values & NHST
- **Type:** MC
- **Question:**

A p-value is the probability of a result at least as extreme as ours, assuming:

- **Options:**

  A) The sample is very large
  B) The alternative hypothesis is true
  C) The null hypothesis is true
  D) There is no sampling error

- **Answer (tutor only):** C
- **Explanation (tutor only):** p-values are calculated under the null: how often would chance alone produce this?
- **Why the wrong options are wrong (tutor only):**
  A) p-values exist for any sample size.
  B) p doesn't assume the alternative.
  D) Sampling error is what p accounts for.
- **Hint:** Which hypothesis do we assume?

### ch15-chimein-04
- **Kind:** Course original
- **Concepts:** Effect size & CIs
- **Type:** MC
- **Question:**

Which best captures the effect size?

- **Options:**

  A) The number of standard deviations our estimate is from the null (distance from null / SD)
  B) The number of standard errors our estimate is from the null (distance from null / SE)
  C) The p-value

- **Answer (tutor only):** A
- **Explanation (tutor only):** Effect size (Cohen's d) divides by the SD, which doesn't shrink with sample size. Dividing by the SE gives t, which grows with sample size.
- **Why the wrong options are wrong (tutor only):**
  B) That's t: it measures evidence against the null and depends on n.
  C) The p-value also depends on n.
- **Hint:** Which quantity stays the same if you collect more data?

### ch15-chimein-04-v1
- **Kind:** AI-written version of ch15-chimein-04
- **Concepts:** Effect size & CIs
- **Type:** MC
- **Question:**

Two studies find the same difference from the null and the same SD, but one has n = 10 and the other n = 1,000. Which is the same in both?

- **Options:**

  A) Cohen's d
  B) The standard error
  C) The p-value
  D) t

- **Answer (tutor only):** A
- **Explanation (tutor only):** d = difference / SD, which doesn't depend on n. The SE, t and p all change with n.
- **Why the wrong options are wrong (tutor only):**
  D), C) and B) All depend on sample size.
- **Hint:** Which one doesn't involve n?

### ch15-chimein-04-v2
- **Kind:** AI-written version of ch15-chimein-04
- **Concepts:** Effect size & CIs
- **Type:** MC
- **Question:**

Which quantity measures how far an estimate is from the null in units of standard errors?

- **Options:**

  A) The p-value
  B) Cohen's d
  C) t

- **Answer (tutor only):** C
- **Explanation (tutor only):** t = (estimate - null) / SE. Cohen's d uses the SD instead.
- **Why the wrong options are wrong (tutor only):**
  A) p is a probability.
  B) d uses the SD.
- **Hint:** SE units.

### ch15-chimein-05
- **Kind:** Course original
- **Concepts:** t vs z; The t statistic & SE
- **Type:** MC
- **Question:**

Sample size plays two roles when we use the t to describe uncertainty and test null hypotheses:

Role 1: It accounts for uncertainty in our estimate of the SD (the t starts quite different from the z but approaches it as n gets big)
Role 2: It sets the size of the standard error, which describes uncertainty in our estimate of the mean

For most sample sizes, which role matters more?

- **Options:**

  A) Role 1 (t vs z)
  B) Role 2 (the standard error)

- **Answer (tutor only):** B
- **Explanation (tutor only):** The SE shrinks with √n at every sample size: quadrupling n halves the SE. The difference between t and z matters only for small samples (with 20 or more observations, critical t values are within a few percent of 1.96).
- **Why the wrong options are wrong (tutor only):**
  A) The t/z difference is real but quickly becomes small; the SE keeps shrinking as n grows.
- **Hint:** Compare how much the critical t changes from n = 10 to 100 with how much the SE changes.

### ch15-chimein-05-v1
- **Kind:** AI-written version of ch15-chimein-05
- **Concepts:** t vs z; The t statistic & SE
- **Type:** MC
- **Question:**

A researcher increases sample size from 10 to 40. Which effect on their 95% CI is larger?

- **Options:**

  A) The critical t shrinks from 2.26 to 2.02
  B) The SE halves, since √40 is double √10

- **Answer (tutor only):** B
- **Explanation (tutor only):** Halving the SE halves the CI width. The drop in critical t (about 11%) is much smaller.
- **Why the wrong options are wrong (tutor only):**
  A) It's real but small compared with the SE change.
- **Hint:** Compare a halving with an 11% change.

### ch15-chimein-05-v2
- **Kind:** AI-written version of ch15-chimein-05
- **Concepts:** t vs z; The t statistic & SE
- **Type:** MC
- **Question:**

For samples larger than about 30, the main reason confidence intervals keep shrinking as n grows is:

- **Options:**

  A) The standard error keeps shrinking with √n
  B) The t distribution keeps getting closer to z

- **Answer (tutor only):** A
- **Explanation (tutor only):** By n ≈ 30 the t is already close to z, but the SE keeps shrinking as 1/√n.
- **Why the wrong options are wrong (tutor only):**
  B) The t vs z difference is already tiny by then.
- **Hint:** Which change continues at all sample sizes?

### ch15-chimein-07
- **Kind:** Course original
- **Concepts:** Paired designs
- **Type:** MC
- **Question:**

What is the advantage of a paired t-test over a two-sample t-test?

- **Options:**

  A) The paired t-test is an easier experiment to pull off
  B) The paired t-test does not assume a normal distribution of residuals
  C) The paired t-test has more power, because it controls for extraneous variation

- **Answer (tutor only):** C
- **Explanation (tutor only):** Comparing within pairs removes variation among pairs (e.g. some hyena pairs giggle more overall), making the treatment effect easier to see.
- **Why the wrong options are wrong (tutor only):**
  A) Finding good pairs is often harder.
  B) It assumes the differences are roughly normal.
- **Hint:** What variation disappears when you look at within-pair differences?

### ch15-chimein-07-v1
- **Kind:** AI-written version of ch15-chimein-07
- **Concepts:** Paired designs
- **Type:** MC
- **Question:**

Researchers measure blood pressure in 20 patients before and after a drug. Why is a paired t-test better than a two-sample t-test here?

- **Options:**

  A) It removes variation among patients, increasing power
  B) It needs only half as many patients as a two-sample test
  C) It doesn't assume the differences are normally distributed
  D) It works even when the measurements are not independent pairs

- **Answer (tutor only):** A
- **Explanation (tutor only):** Each patient is their own control, so differences among patients drop out.
- **Why the wrong options are wrong (tutor only):**
  B) It's about power, not a rule on sample size.
  C) The paired t assumes normal differences.
  D) It needs genuine pairs.
- **Hint:** What does comparing within a patient remove?

### ch15-chimein-07-v2
- **Kind:** AI-written version of ch15-chimein-07
- **Concepts:** Paired designs
- **Type:** MC
- **Question:**

Compared with ignoring the pairs and running a two-sample t-test, a paired t-test on naturally paired data usually gives:

- **Options:**

  A) A larger SE and less power
  B) A smaller SE and more power
  C) The same SE and the same power

- **Answer (tutor only):** B
- **Explanation (tutor only):** Removing pair-to-pair variation shrinks the SE, increasing power.
- **Why the wrong options are wrong (tutor only):**
  A) Pairing reduces noise.
  C) Pairing changes the SE when pairs share variation.
- **Hint:** What happens to noise when you compare within pairs?

### ch15-chimein-08
- **Kind:** Course original
- **Concepts:** Paired designs
- **Type:** select-all
- **Question:**

When can you use a paired t-test? (Select all that apply.)

- **Options:**

  A) When you have natural pairs, one with the treatment and one with the control
  B) When you pair individuals who are similar in most ways, with one receiving the treatment and the other the control
  C) Whenever you have a balanced design, by making artificial pairs after the fact (one treatment, one control)

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** Pairing has to reflect real shared features (twins, the same individual before and after, matched individuals). Pairing at random after the fact adds no information and is wrong.
- **Why the wrong options are wrong (tutor only):**
  C) Arbitrary pairs don't share anything, so a paired test would be invalid.
- **Hint:** What makes two observations a real pair?

### ch15-chimein-08-v1
- **Kind:** AI-written version of ch15-chimein-08
- **Concepts:** Paired designs
- **Type:** select-all
- **Question:**

Which designs are appropriate for a paired t-test? (Select all that apply.)

- **Options:**

  A) Matching ten treatment and ten control mice at random after the experiment
  B) Measuring the same lizards' sprint speed at two temperatures
  C) Comparing twins, one given a supplement and one a placebo

- **Answer (tutor only):** B, C
- **Explanation (tutor only):** Repeated measures and twins are real pairs. Random after-the-fact matching shares nothing.
- **Why the wrong options are wrong (tutor only):**
  A) Random pairing adds no information.
- **Hint:** Do the pairs share something real?

### ch15-chimein-08-v2
- **Kind:** AI-written version of ch15-chimein-08
- **Concepts:** Paired designs
- **Type:** select-all
- **Question:**

Which designs are NOT appropriate for a paired t-test? (Select all that apply.)

- **Options:**

  A) Comparing left and right leaves on the same plant, one treated and one not
  B) Pairing plants at random after the experiment because the design is balanced
  C) Pairing the tallest treated plant with the tallest control plant after the experiment

- **Answer (tutor only):** B, C
- **Explanation (tutor only):** Pairs must be set by real shared features before treatment. Pairing after the fact (randomly or by the outcome) is invalid.
- **Why the wrong options are wrong (tutor only):**
  A) Two leaves on the same plant are natural pairs.
- **Hint:** When and how were the pairs formed?

### ch15-chimein-09
- **Kind:** Course original
- **Concepts:** The t statistic & SE
- **Type:** MC
- **Question:**

Fill in the blanks: The ____ and the ____ describe uncertainty, while the ____ describes variability.

- **Options:**

  A) standard error and standard deviation describe uncertainty; the t statistic describes variability
  B) standard error and t statistic describe uncertainty; the standard deviation describes variability
  C) standard deviation and t statistic describe uncertainty; the standard error describes variability

- **Answer (tutor only):** B
- **Explanation (tutor only):** The SD describes how much individuals vary. The SE (and t, which is built on it) describe uncertainty in an estimate.
- **Why the wrong options are wrong (tutor only):**
  A) The SD describes spread among individuals, not uncertainty in the mean.
  C) The SE describes uncertainty, not variability among individuals.
- **Hint:** Which of these describes how different individuals are from each other?

### ch15-chimein-09-v1
- **Kind:** AI-written version of ch15-chimein-09
- **Concepts:** The t statistic & SE
- **Type:** MC
- **Question:**

Which quantity describes VARIABILITY among individuals rather than uncertainty in an estimate?

- **Options:**

  A) The standard error
  B) The standard deviation
  C) The width of the confidence interval

- **Answer (tutor only):** B
- **Explanation (tutor only):** The SD describes spread among individuals; the SE and CI describe uncertainty in an estimate.
- **Why the wrong options are wrong (tutor only):**
  A) and C) describe uncertainty.
- **Hint:** Individuals vs estimates.

### ch15-chimein-09-v2
- **Kind:** AI-written version of ch15-chimein-09
- **Concepts:** The t statistic & SE
- **Type:** MC
- **Question:**

As sample size increases, which of these is expected to shrink?

- **Options:**

  A) The standard error
  B) The standard deviation
  C) The variance

- **Answer (tutor only):** A
- **Explanation (tutor only):** Uncertainty (SE) shrinks with n; variability (SD, variance) is a property of the population and doesn't.
- **Why the wrong options are wrong (tutor only):**
  B) and C) estimate population variability, which doesn't depend on n.
- **Hint:** Uncertainty vs variability.

### ch15-chimein-10
- **Kind:** Course original
- **Concepts:** The t statistic & SE; p-values & NHST; Effect size & CIs
- **Type:** MC
- **Question:**

Which measures how 'surprising' it would be to see our data if the null were true?

- **Options:**

  A) t
  B) p
  C) Cohen's d

- **Answer (tutor only):** B
- **Explanation (tutor only):** The p-value is the probability of a result at least as extreme as ours if the null were true: small p means surprising.
- **Why the wrong options are wrong (tutor only):**
  A) t is a test statistic; we need its null distribution to turn it into a probability.
  C) Cohen's d is an effect size.
- **Hint:** Which one is a probability?

### ch15-chimein-10-v1
- **Kind:** AI-written version of ch15-chimein-10
- **Concepts:** The t statistic & SE; p-values & NHST; Effect size & CIs
- **Type:** MC
- **Question:**

Which tells us how large an effect is, regardless of sample size?

- **Options:**

  A) The p-value
  B) Cohen's d
  C) The t value

- **Answer (tutor only):** B
- **Explanation (tutor only):** d standardizes the difference by the SD. t and p both depend on sample size.
- **Why the wrong options are wrong (tutor only):**
  C) and A) change with n.
- **Hint:** Which one ignores n?

### ch15-chimein-10-v2
- **Kind:** AI-written version of ch15-chimein-10
- **Concepts:** The t statistic & SE; p-values & NHST; Effect size & CIs
- **Type:** MC
- **Question:**

Which measures how many standard errors our estimate is from the null value?

- **Options:**

  A) t
  B) Cohen's d
  C) p

- **Answer (tutor only):** A
- **Explanation (tutor only):** t = (estimate - null) / SE.
- **Why the wrong options are wrong (tutor only):**
  C) p is a probability. B) d uses the SD.
- **Hint:** SE units.

### ch15-chimein-11
- **Kind:** Course original
- **Concepts:** p-values & NHST
- **Type:** TF
- **Question:**

TRUE or FALSE: A p-value is the probability that our null hypothesis is true.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** A p-value assumes the null is true and asks how often we'd see data this extreme. It's a statement about the data given the null, not about the null given the data.
- **Why the wrong options are wrong (tutor only):**
  TRUE: a very common misreading of p-values.
- **Hint:** Is p calculated assuming the null is true, or is it about whether the null is true?

### ch15-chimein-11-v1
- **Kind:** AI-written version of ch15-chimein-11
- **Concepts:** p-values & NHST
- **Type:** TF
- **Question:**

TRUE or FALSE: A p-value of 0.03 means there is a 3% chance that the alternative hypothesis is false.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** p is the probability of data this extreme if the null were true. It says nothing directly about the probability of either hypothesis.
- **Why the wrong options are wrong (tutor only):**
  TRUE: p is not a probability about hypotheses.
- **Hint:** What does p condition on?

### ch15-chimein-11-v2
- **Kind:** AI-written version of ch15-chimein-11
- **Concepts:** p-values & NHST
- **Type:** TF
- **Question:**

TRUE or FALSE: A p-value is the probability of getting a result at least as extreme as ours if the null hypothesis were true.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** A
- **Explanation (tutor only):** That's exactly the definition.
- **Why the wrong options are wrong (tutor only):**
  FALSE: this is the correct definition.
- **Hint:** Data given the null.

### ch15-hw-01
- **Kind:** Course original
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

When would you use a t distribution instead of a z (standard normal) distribution?

- **Options:**

  A) When you are comparing two proportions
  B) When the population standard deviation is unknown and must be estimated from the sample
  C) When the data are not approximately normal
  D) When the sample size is very large
  E) When the mean is not zero and/or the standard deviation is not one

- **Answer (tutor only):** B
- **Explanation (tutor only):** The t accounts for the extra uncertainty from estimating the SD from the sample. If we knew σ, we'd use z.
- **Why the wrong options are wrong (tutor only):**
  A) Proportions are a different problem.
  C) The t still assumes (roughly) normal data or sampling distributions.
  D) With very large samples, t and z are nearly identical, so it barely matters.
  E) Any normal can be standardized; that's what Z scores do.
- **Hint:** What does the t do that the z doesn't?

### ch15-hw-01-v1
- **Kind:** AI-written version of ch15-hw-01
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

A researcher knows the true population SD of fish length from decades of census data, and samples 12 fish. Should they use a z or a t to test whether mean length has changed?

- **Options:**

  A) t, because the sample size is small
  B) z, because fish length is continuous
  C) z, because the population SD is known
  D) t, because the mean is not zero

- **Answer (tutor only):** C
- **Explanation (tutor only):** The t accounts for estimating the SD. If σ is truly known, z is appropriate even for small samples.
- **Why the wrong options are wrong (tutor only):**
  A) Small n matters only because the SD is estimated.
  B) Both handle continuous data.
  D) Neither needs the mean to be 0.
- **Hint:** What extra uncertainty does the t account for?

### ch15-hw-01-v2
- **Kind:** AI-written version of ch15-hw-01
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

Why do we usually use a t distribution rather than a z for a sample mean in biology?

- **Options:**

  A) The t works for proportions, and the z only works for means
  B) Biological data are rarely normally distributed, and the t corrects for that
  C) Our sample sizes are almost always larger than 1,000 individuals
  D) We rarely know the population SD, so we estimate it from the sample

- **Answer (tutor only):** D
- **Explanation (tutor only):** The t adds uncertainty for estimating σ from the data.
- **Why the wrong options are wrong (tutor only):**
  A) Not the distinction.
  B) The t assumes normality too.
  C) Large n would make t ≈ z anyway.
- **Hint:** What does the t assume we don't know?

### ch15-hw-02
- **Kind:** Course original
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

A researcher runs a t-test on 100 measurements of flower height, which are slightly right-skewed. Which statement best describes whether the test is appropriate?

- **Options:**

  A) It's inappropriate: t-tests need symmetric data, even for large samples
  B) It's inappropriate: t-tests strictly require perfectly normal data
  C) It's probably fine: the t distribution automatically corrects for skew
  D) It's probably fine: with n = 100, the CLT makes t-tests robust to mild skew

- **Answer (tutor only):** D
- **Explanation (tutor only):** With 100 observations, the sampling distribution of the mean is close to normal even if the data are a bit skewed, so the t-test works well.
- **Why the wrong options are wrong (tutor only):**
  A) and B) t-tests are robust to mild departures from normality, especially with large samples.
  C) The t doesn't correct for skew; the CLT is what helps.
- **Hint:** Which theorem helps when n is large?

### ch15-hw-02-v1
- **Kind:** AI-written version of ch15-hw-02
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

A researcher runs a t-test on 6 measurements of flower height, and the data are strongly right-skewed with one huge value. Which statement best describes whether the test is appropriate?

- **Options:**

  A) It's risky: with so few points, the CLT can't fix the skew
  B) It's risky only because the sample mean is not zero
  C) It's fine: the t distribution automatically corrects for skew
  D) It's fine: t-tests make no assumptions about the data

- **Answer (tutor only):** A
- **Explanation (tutor only):** The t-test is robust to skew mainly in larger samples. With n = 6 and strong skew, the sampling distribution of the mean may be far from normal.
- **Why the wrong options are wrong (tutor only):**
  B) The mean being zero is irrelevant.
  C) The t corrects for estimating the SD, not for skew.
  D) It assumes normality of the sampling distribution.
- **Hint:** Does the CLT help with n = 6?

### ch15-hw-02-v2
- **Kind:** AI-written version of ch15-hw-02
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

Which situation makes a t-test MOST robust to mildly skewed data?

- **Options:**

  A) A small sample, such as 5 observations
  B) A large sample, such as 200 observations
  C) A sample with a large standard deviation
  D) A sample whose mean happens to be near zero

- **Answer (tutor only):** B
- **Explanation (tutor only):** With large samples, the CLT makes the sampling distribution of the mean nearly normal.
- **Why the wrong options are wrong (tutor only):**
  A) Small samples don't benefit from the CLT.
  D) and C) These don't affect robustness to skew.
- **Hint:** Central limit theorem.

### ch15-hw-03
- **Kind:** Course original
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

Your advisor tells you to just use a z-test instead of a t-test, claiming they are practically the same. When would this substitution make little practical difference?

- **Options:**

  A) When the sample is large, so the t and z distributions are nearly identical
  B) When your data contain no outliers
  C) When you have more than one predictor variable
  D) When the sample mean equals the population mean

- **Answer (tutor only):** A
- **Explanation (tutor only):** As degrees of freedom grow, the t distribution's tails shrink toward the z's. With large samples the critical values are nearly the same (e.g. 1.98 vs 1.96 at 100 df).
- **Why the wrong options are wrong (tutor only):**
  B) Outliers matter for both tests equally.
  C) The number of predictors doesn't make t and z alike.
  D) The estimate's value doesn't change the shape of the distribution.
- **Hint:** When does the t's fatter tails stop mattering?

### ch15-hw-03-v1
- **Kind:** AI-written version of ch15-hw-03
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

With which sample would a t-test and a z-test give the MOST different p-values?

- **Options:**

  A) n = 400
  B) n = 40
  C) n = 4
  D) They always give identical p-values

- **Answer (tutor only):** C
- **Explanation (tutor only):** With few df, the t has much fatter tails than the z (critical t for 3 df is 3.18 vs 1.96).
- **Why the wrong options are wrong (tutor only):**
  B) and A) t approaches z as n grows.
  D) They differ, especially for small n.
- **Hint:** When does t look least like z?

### ch15-hw-03-v2
- **Kind:** AI-written version of ch15-hw-03
- **Concepts:** t vs z
- **Type:** MC
- **Question:**

The critical t value (α = 0.05, two-tailed) is 2.78 for 4 df, 2.09 for 20 df and 1.98 for 100 df. What does this pattern show?

- **Options:**

  A) The t approaches the z (1.96) as degrees of freedom grow
  B) Larger samples need larger t values to reject the null
  C) The critical value depends on the sample mean
  D) The t has thinner tails than the z for small samples

- **Answer (tutor only):** A
- **Explanation (tutor only):** As df grow, the SD is estimated more precisely and the t converges to the z.
- **Why the wrong options are wrong (tutor only):**
  B) The critical value shrinks with n.
  C) It depends only on df and α.
  D) The t has fatter tails for small samples.
- **Hint:** Compare each to 1.96.

### ch15-hw-04
- **Kind:** Course original
- **Concepts:** p-values & NHST; Paired designs
- **Type:** matching
- **Question:**

To test whether a chatbot tutor helps students study, five pairs of students matched on their first exam scores were split so one got the tutor and the other did not.

• Mean difference in exam scores (chatbot minus control): 5.25
• Variance of the differences: 13.716
• t = 3.170

For a two-tailed test, match each hypothesis to its statement:

1. Null hypothesis
2. Alternative hypothesis

- **Options:**

  A) Chatbots help you learn
  B) The mean difference in exam scores (chatbot - control) does not equal 0
  C) The mean difference in exam scores (chatbot - control) is greater than 0
  D) The mean difference in exam scores (chatbot - control) equals 0

- **Answer (tutor only):** 1-D, 2-B
- **Explanation (tutor only):** The null is a specific value (no difference). A two-tailed alternative is 'not equal to', allowing a difference in either direction.
- **Why the wrong options are wrong (tutor only):**
  C) That's a one-tailed alternative.
  A) That's a biological hypothesis, not a statistical one.
- **Hint:** Two-tailed means either direction counts.

### ch15-hw-04-v1
- **Kind:** AI-written version of ch15-hw-04
- **Concepts:** p-values & NHST; Paired designs
- **Type:** matching
- **Question:**

To ask whether ant colonies forage more in warm weather, a researcher counted foragers leaving 10 nests on a cool morning and again on a warm afternoon (difference = warm minus cool). The mean difference is 12 ants, and the variance of the differences is 100.

For a two-tailed test, match each hypothesis to its statement:

1. Null hypothesis
2. Alternative hypothesis

- **Options:**

  A) The mean difference in foragers (warm - cool) does not equal 0
  B) Warm weather makes ants forage more
  C) The mean difference in foragers (warm - cool) equals 0
  D) The mean difference in foragers (warm - cool) is greater than 0

- **Answer (tutor only):** 1-C, 2-A
- **Explanation (tutor only):** Null: no difference. Two-tailed alternative: a difference in either direction.
- **Why the wrong options are wrong (tutor only):**
  D) is one-tailed; B) is a scientific hypothesis, not a statistical one.
- **Hint:** Two-tailed means 'not equal'.

### ch15-hw-04-v2
- **Kind:** AI-written version of ch15-hw-04
- **Concepts:** p-values & NHST; Paired designs
- **Type:** matching
- **Question:**

To test whether a chatbot tutor helps students study, five pairs of students matched on their first exam scores were split so one got the tutor and the other did not.

• Mean difference in exam scores (chatbot minus control): 5.25
• Variance of the differences: 13.716
• t = 3.170

For a ONE-tailed test of whether the chatbot improves scores, match each hypothesis to its statement:

1. Null hypothesis
2. Alternative hypothesis

- **Options:**

  A) The mean difference in exam scores (chatbot - control) is greater than 0
  B) The mean difference in exam scores (chatbot - control) does not equal 0
  C) The mean difference in exam scores (chatbot - control) is 0 or less
  D) Chatbots help you learn

- **Answer (tutor only):** 1-C, 2-A
- **Explanation (tutor only):** A one-tailed alternative specifies a direction (greater than 0); the null covers everything else.
- **Why the wrong options are wrong (tutor only):**
  B) is two-tailed; D) is not a statistical hypothesis.
- **Hint:** One-tailed means one direction.

### ch15-hw-05
- **Kind:** Course original
- **Concepts:** Effect size & CIs
- **Type:** MC
- **Question:**

To test whether a chatbot tutor helps students study, five pairs of students matched on their first exam scores were split so one got the tutor and the other did not.

• Mean difference in exam scores (chatbot minus control): 5.25
• Variance of the differences: 13.716
• t = 3.170

What is the best measure of the effect size?

- **Options:**

  A) The mean difference between chatbot and control, 5.25
  B) The p-value
  C) Cohen's d, 1.42
  D) The t value, 3.170

- **Answer (tutor only):** C
- **Explanation (tutor only):** Cohen's d = mean difference / SD = 5.25 / √13.716 = 5.25 / 3.70 = 1.42. It puts the difference on a standard scale, independent of sample size.
- **Why the wrong options are wrong (tutor only):**
  A) The raw difference is useful but depends on the units (exam points).
  B) A p-value depends on sample size and isn't an effect size.
  D) t also grows with sample size; it measures evidence, not effect size.
- **Hint:** Which measure doesn't depend on sample size?

### ch15-hw-05-v1
- **Kind:** AI-written version of ch15-hw-05
- **Concepts:** Effect size & CIs
- **Type:** MC
- **Question:**

To ask whether ant colonies forage more in warm weather, a researcher counted foragers leaving 10 nests on a cool morning and again on a warm afternoon (difference = warm minus cool). The mean difference is 12 ants, and the variance of the differences is 100.

What is Cohen's d for this difference?

- **Options:**

  A) 12
  B) 0.12
  C) 1.2
  D) 3.8

- **Answer (tutor only):** C
- **Explanation (tutor only):** SD = √100 = 10, so d = 12 / 10 = 1.2.
- **Why the wrong options are wrong (tutor only):**
  A) That's the raw difference.
  B) Divides by the variance.
  D) That's t (12 / SE of 3.16).
- **Hint:** Mean difference ÷ SD.

### ch15-hw-05-v2
- **Kind:** AI-written version of ch15-hw-05
- **Concepts:** Effect size & CIs
- **Type:** MC
- **Question:**

To test whether a chatbot tutor helps students study, five pairs of students matched on their first exam scores were split so one got the tutor and the other did not.

• Mean difference in exam scores (chatbot minus control): 5.25
• Variance of the differences: 13.716
• t = 3.170

Why is Cohen's d (1.42) a better measure of effect size here than t (3.17)?

- **Options:**

  A) d accounts for sample size; t ignores it entirely
  B) d is a probability; t is not a probability at all
  C) d is always larger than t, so it's easier to detect
  D) d doesn't change with sample size; t grows as n grows

- **Answer (tutor only):** D
- **Explanation (tutor only):** d = difference / SD describes the size of the effect. t = difference / SE grows with √n, so it mixes effect size with sample size.
- **Why the wrong options are wrong (tutor only):**
  A) It's the reverse.
  B) Neither is a probability.
  C) d is usually smaller than t.
- **Hint:** Which one depends on n?

### ch15-hw-06
- **Kind:** Course original
- **Concepts:** The t statistic & SE; Paired designs
- **Type:** numeric
- **Question:**

To test whether a chatbot tutor helps students study, five pairs of students matched on their first exam scores were split so one got the tutor and the other did not.

• Mean difference in exam scores (chatbot minus control): 5.25
• Variance of the differences: 13.716
• t = 3.170

What is the standard error of the mean difference?

- **Answer (tutor only):** 1.656
- **Explanation (tutor only):** SD = √13.716 = 3.704. SE = SD / √n = 3.704 / √5 = 1.656. (Check: 5.25 / 1.656 = 3.17 = t.)
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: using the variance instead of the SD, or dividing by n instead of √n.
- **Hint:** Start by turning the variance into an SD.

### ch15-hw-06-v1
- **Kind:** AI-written version of ch15-hw-06
- **Concepts:** The t statistic & SE; Paired designs
- **Type:** numeric
- **Question:**

To ask whether ant colonies forage more in warm weather, a researcher counted foragers leaving 10 nests on a cool morning and again on a warm afternoon (difference = warm minus cool). The mean difference is 12 ants, and the variance of the differences is 100.

What is the standard error of the mean difference?

- **Answer (tutor only):** 3.16
- **Explanation (tutor only):** SD = √100 = 10; SE = 10 / √10 = 3.16.
- **Hint:** SD / √n.

### ch15-hw-06-v2
- **Kind:** AI-written version of ch15-hw-06
- **Concepts:** The t statistic & SE; Paired designs
- **Type:** numeric
- **Question:**

To ask whether ant colonies forage more in warm weather, a researcher counted foragers leaving 10 nests on a cool morning and again on a warm afternoon (difference = warm minus cool). The mean difference is 12 ants, and the variance of the differences is 100.

The standard error of the mean difference is 3.16. What is t?

- **Answer (tutor only):** 3.79
- **Explanation (tutor only):** t = 12 / 3.16 = 3.79.
- **Hint:** Mean difference ÷ SE.

### ch15-hw-07
- **Kind:** Course original
- **Concepts:** p-values & NHST; Paired designs
- **Type:** numeric
- **Question:**

To test whether a chatbot tutor helps students study, five pairs of students matched on their first exam scores were split so one got the tutor and the other did not.

• Mean difference in exam scores (chatbot minus control): 5.25
• Variance of the differences: 13.716
• t = 3.170

In R:
2 * pt(3.170, df = 4, lower.tail = FALSE)
[1] 0.0339

What is the two-tailed p-value? Report it to three decimals.

- **Answer (tutor only):** 0.034
- **Explanation (tutor only):** With five pairs, df = 5 - 1 = 4. The two-tailed p-value is 0.034.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: halving or doubling again. The code already doubles the one-tailed area.
- **Hint:** The R output gives it directly; make sure you understand why df = 4.

### ch15-hw-07-v1
- **Kind:** AI-written version of ch15-hw-07
- **Concepts:** p-values & NHST; Paired designs
- **Type:** numeric
- **Question:**

To ask whether ant colonies forage more in warm weather, a researcher counted foragers leaving 10 nests on a cool morning and again on a warm afternoon (difference = warm minus cool). The mean difference is 12 ants, and the variance of the differences is 100. t = 3.79.

In R:
2 * pt(3.79, df = 9, lower.tail = FALSE)
[1] 0.0043

What is the two-tailed p-value? Report it to three decimals.

- **Answer (tutor only):** 0.004
- **Explanation (tutor only):** With 10 nests, df = 9. The p-value is 0.004.
- **Hint:** Read it from the R output.

### ch15-hw-07-v2
- **Kind:** AI-written version of ch15-hw-07
- **Concepts:** p-values & NHST; Paired designs
- **Type:** numeric
- **Question:**

To test whether a chatbot tutor helps students study, five pairs of students matched on their first exam scores were split so one got the tutor and the other did not.

• Mean difference in exam scores (chatbot minus control): 5.25
• Variance of the differences: 13.716
• t = 3.170

How many degrees of freedom does this paired t-test have?

- **Answer (tutor only):** 4
- **Explanation (tutor only):** A paired t-test is a one-sample test on the differences: df = number of pairs - 1 = 5 - 1 = 4.
- **Hint:** Count pairs, not students.

### ch15-hw-08
- **Kind:** Course original
- **Concepts:** p-values & NHST
- **Type:** MC
- **Question:**

To test whether a chatbot tutor helps students study, five pairs of students matched on their first exam scores were split so one got the tutor and the other did not.

• Mean difference in exam scores (chatbot minus control): 5.25
• Variance of the differences: 13.716
• t = 3.170

The two-tailed p-value is 0.034. At α = 0.05, what do we do to the null, and what does this mean?

- **Options:**

  A) Reject it; this proves the null is false
  B) Reject it; act as if it's false, but may be wrong
  C) Fail to reject it; so the null must be true
  D) Accept it; so the alternative must be false

- **Answer (tutor only):** B
- **Explanation (tutor only):** 0.034 < 0.05, so we reject the null. That doesn't prove the null false: with only five pairs, we could be making a type I error.
- **Why the wrong options are wrong (tutor only):**
  A) Rejecting is not proof.
  C) and D) p < α means we reject; and we never 'accept' a null.
- **Hint:** Compare p to α. Can a p-value prove anything for certain?

### ch15-hw-08-v1
- **Kind:** AI-written version of ch15-hw-08
- **Concepts:** p-values & NHST
- **Type:** MC
- **Question:**

To ask whether ant colonies forage more in warm weather, a researcher counted foragers leaving 10 nests on a cool morning and again on a warm afternoon (difference = warm minus cool). The mean difference is 12 ants, and the variance of the differences is 100. The two-tailed p-value is 0.004. At α = 0.05, what do we do, and what does it mean?

- **Options:**

  A) Fail to reject; we need more nests before deciding
  B) Reject; we act as if the null is false, knowing we could be wrong
  C) Fail to reject; foraging is the same at both temperatures
  D) Reject; warm weather definitely increases foraging

- **Answer (tutor only):** B
- **Explanation (tutor only):** p < 0.05, so we reject. That's not proof: a type I error is possible.
- **Why the wrong options are wrong (tutor only):**
  C) and A) p < α.
  D) Rejection isn't proof.
- **Hint:** Rejecting isn't proving.

### ch15-hw-08-v2
- **Kind:** AI-written version of ch15-hw-08
- **Concepts:** p-values & NHST
- **Type:** MC
- **Question:**

To test whether a chatbot tutor helps students study, five pairs of students matched on their first exam scores were split so one got the tutor and the other did not.

• Mean difference in exam scores (chatbot minus control): 5.25
• Variance of the differences: 13.716
• t = 3.170

Suppose instead the p-value had been 0.21. At α = 0.05, what would we do, and what would it mean?

- **Options:**

  A) Fail to reject; the chatbot has no effect on exam scores
  B) Reject; the chatbot has no effect on exam scores
  C) Accept the null; the chatbot certainly does not help
  D) Fail to reject; the data don't show a clear effect either way

- **Answer (tutor only):** D
- **Explanation (tutor only):** p > α, so we fail to reject. With five pairs, we may simply lack power; it doesn't show there's no effect.
- **Why the wrong options are wrong (tutor only):**
  A) and C) Failing to reject isn't evidence of no effect.
  B) p > α.
- **Hint:** Absence of evidence…

### ch15-hw-09
- **Kind:** Course original
- **Concepts:** t vs z; Effect size & CIs
- **Type:** MC
- **Question:**

To test whether a chatbot tutor helps students study, five pairs of students matched on their first exam scores were split so one got the tutor and the other did not.

• Mean difference in exam scores (chatbot minus control): 5.25
• Variance of the differences: 13.716
• t = 3.170

The SE is 1.656, and the critical t value for 4 df at α = 0.05 is 2.776. What is the 95% confidence interval for the mean difference?

- **Options:**

  A) (1.50, 9.00)
  B) (1.71, 8.79)
  C) (1.90, 8.60)
  D) (0.65, 9.85)
  E) (2.00, 8.50)

- **Answer (tutor only):** D
- **Explanation (tutor only):** 95% CI = 5.25 ± 2.776 × 1.656 = 5.25 ± 4.60, giving (0.65, 9.85). The interval excludes 0, consistent with rejecting the null.
- **Why the wrong options are wrong (tutor only):**
  B) Uses 1.96 (the z critical value) instead of the t critical value for 4 df.
  A), C) and E) Don't match the formula.
- **Hint:** CI = estimate ± critical t × SE.

### ch15-hw-09-v1
- **Kind:** AI-written version of ch15-hw-09
- **Concepts:** t vs z; Effect size & CIs
- **Type:** MC
- **Question:**

To ask whether ant colonies forage more in warm weather, a researcher counted foragers leaving 10 nests on a cool morning and again on a warm afternoon (difference = warm minus cool). The mean difference is 12 ants, and the variance of the differences is 100. The SE is 3.16, and the critical t value for 9 df at α = 0.05 is 2.262. What is the 95% confidence interval for the mean difference?

- **Options:**

  A) (5.80, 18.20)
  B) (4.85, 19.15)
  C) (-10.6, 34.6)
  D) (8.84, 15.16)

- **Answer (tutor only):** B
- **Explanation (tutor only):** 12 ± 2.262 × 3.16 = 12 ± 7.15 → (4.85, 19.15). It excludes 0, matching p < 0.05.
- **Why the wrong options are wrong (tutor only):**
  A) Uses 1.96 × 3.16, the z value, instead of the critical t.
  C) Uses the SD instead of the SE.
  D) Forgets the critical t.
- **Hint:** Estimate ± critical t × SE.

### ch15-hw-09-v2
- **Kind:** AI-written version of ch15-hw-09
- **Concepts:** t vs z; Effect size & CIs
- **Type:** MC
- **Question:**

To test whether a chatbot tutor helps students study, five pairs of students matched on their first exam scores were split so one got the tutor and the other did not.

• Mean difference in exam scores (chatbot minus control): 5.25
• Variance of the differences: 13.716
• t = 3.170

The 95% CI for the mean difference is (0.65, 9.85). Which statement is correct?

- **Options:**

  A) There is a 95% chance the true difference is between 0.65 and 9.85
  B) It excludes 0, consistent with rejecting the null at α = 0.05
  C) It includes 5.25, so we fail to reject the null at α = 0.05
  D) It is wide, so the chatbot must have no real effect on scores

- **Answer (tutor only):** B
- **Explanation (tutor only):** A 95% CI excluding 0 corresponds to p < 0.05 for a two-tailed test of no difference.
- **Why the wrong options are wrong (tutor only):**
  A) The 95% describes the procedure, not this interval.
  C) The CI always contains the estimate; what matters is the null value (0).
  D) A wide CI means imprecision, not no effect.
- **Hint:** Is the null value inside the interval?

### ch15-quiz-01
- **Kind:** Course original
- **Concepts:** The t statistic & SE
- **Type:** numeric
- **Question:**

To check the folk value of 98.6 °F for human body temperature, researchers measured 25 random people: mean 98.524 °F, sample variance 0.4594.

Testing the null hypothesis that mean body temperature is 98.6 °F, what is the numerator of t (the estimate minus its null value)?

- **Answer (tutor only):** -0.076
- **Explanation (tutor only):** Numerator = estimate - null value = 98.524 - 98.6 = -0.076 °F.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: subtracting in the other order (+0.076). Either sign gives the same two-tailed test, but by convention it's estimate minus null.
- **Hint:** t = (estimate - null value) / SE.

### ch15-quiz-01-v1
- **Kind:** AI-written version of ch15-quiz-01
- **Concepts:** The t statistic & SE
- **Type:** numeric
- **Question:**

To check the folk value of 98.6 °F for human body temperature, a class measured 16 healthy volunteers: mean 98.30 °F, sample variance 0.64.

Testing the null hypothesis that mean body temperature is 98.6 °F, what is the numerator of t (the estimate minus its null value)?

- **Answer (tutor only):** -0.3
- **Explanation (tutor only):** 98.30 - 98.6 = -0.30 °F.
- **Hint:** Estimate minus null value.

### ch15-quiz-01-v2
- **Kind:** AI-written version of ch15-quiz-01
- **Concepts:** The t statistic & SE
- **Type:** numeric
- **Question:**

To check the folk value of 98.6 °F for human body temperature, researchers measured 25 random people: mean 98.524 °F, sample variance 0.4594.

If instead we tested the null hypothesis that mean body temperature is 98.2 °F, what would the numerator of t be?

- **Answer (tutor only):** 0.324
- **Explanation (tutor only):** 98.524 - 98.2 = 0.324 °F.
- **Hint:** Estimate minus the new null value.

### ch15-quiz-02
- **Kind:** Course original
- **Concepts:** The t statistic & SE
- **Type:** numeric
- **Question:**

To check the folk value of 98.6 °F for human body temperature, researchers measured 25 random people: mean 98.524 °F, sample variance 0.4594.

What is the sample standard deviation?

- **Answer (tutor only):** 0.678
- **Explanation (tutor only):** SD = √variance = √0.4594 = 0.678 °F.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: using the variance (0.4594) as the SD.
- **Hint:** How are the variance and the SD related?

### ch15-quiz-02-v1
- **Kind:** AI-written version of ch15-quiz-02
- **Concepts:** The t statistic & SE
- **Type:** numeric
- **Question:**

To check the folk value of 98.6 °F for human body temperature, a class measured 16 healthy volunteers: mean 98.30 °F, sample variance 0.64.

What is the sample standard deviation?

- **Answer (tutor only):** 0.8
- **Explanation (tutor only):** SD = √0.64 = 0.80 °F.
- **Hint:** Square root of the variance.

### ch15-quiz-02-v2
- **Kind:** AI-written version of ch15-quiz-02
- **Concepts:** The t statistic & SE
- **Type:** numeric
- **Question:**

A sample of 25 body temperatures has a standard deviation of 0.678 °F. What is the sample variance?

- **Answer (tutor only):** 0.46
- **Explanation (tutor only):** Variance = SD² = 0.678² = 0.460.
- **Hint:** Square the SD.

### ch15-quiz-03
- **Kind:** Course original
- **Concepts:** Effect size & CIs
- **Type:** MC
- **Question:**

To check the folk value of 98.6 °F for human body temperature, researchers measured 25 random people: mean 98.524 °F, sample variance 0.4594.

The mean is 0.076 °F below 98.6, and the SD is 0.678 °F. What is Cohen's d, and how big is this effect?

- **Options:**

  A) d ≈ 0.11, a small effect (< 0.5)
  B) d ≈ 0.56, a medium effect (0.5 to 0.8)
  C) d ≈ 8.9, a large effect (> 0.8)
  D) d ≈ 0.076, a small effect

- **Answer (tutor only):** A
- **Explanation (tutor only):** Cohen's d = |difference| / SD = 0.076 / 0.678 = 0.11, a small effect: the average differs from 98.6 by about a tenth of an SD.
- **Why the wrong options are wrong (tutor only):**
  B) 0.56 is the t value (difference / SE), not d.
  C) That's SD / difference, upside down.
  D) 0.076 is the raw difference, not standardized.
- **Hint:** Cohen's d divides by the standard deviation, not the standard error.

### ch15-quiz-03-v1
- **Kind:** AI-written version of ch15-quiz-03
- **Concepts:** Effect size & CIs
- **Type:** MC
- **Question:**

To check the folk value of 98.6 °F for human body temperature, a class measured 16 healthy volunteers: mean 98.30 °F, sample variance 0.64.

The mean is 0.30 °F below 98.6, and the SD is 0.80 °F. What is Cohen's d, and how big is this effect?

- **Options:**

  A) d ≈ 0.09, a small effect (< 0.5)
  B) d ≈ 0.60, a medium effect (0.5 to 0.8)
  C) d ≈ 1.50, a large effect (> 0.8)
  D) d ≈ 0.38, a small effect (< 0.5)

- **Answer (tutor only):** D
- **Explanation (tutor only):** d = 0.30 / 0.80 = 0.375, a small effect.
- **Why the wrong options are wrong (tutor only):**
  A) That's 0.30 × 0.30.
  B) Divides by something other than the SD.
  C) That's t (0.30 / SE of 0.20), not d.
- **Hint:** Difference ÷ SD.

### ch15-quiz-03-v2
- **Kind:** AI-written version of ch15-quiz-03
- **Concepts:** Effect size & CIs
- **Type:** MC
- **Question:**

To check the folk value of 98.6 °F for human body temperature, researchers measured 25 random people: mean 98.524 °F, sample variance 0.4594.

Why is Cohen's d (0.11) so much smaller than |t| (0.56) for these data?

- **Options:**

  A) d is a probability, so it must be less than t
  B) d divides by the SD, while t divides by the smaller SE
  C) d divides by the SE, while t divides by the larger SD
  D) d ignores the sign of the difference, so it is smaller

- **Answer (tutor only):** B
- **Explanation (tutor only):** d = difference / SD; t = difference / SE, and SE = SD / √n is smaller, so |t| = d × √n = 0.11 × 5 = 0.56.
- **Why the wrong options are wrong (tutor only):**
  A) d is not a probability.
  C) It's the other way around.
  D) Ignoring the sign doesn't change the size.
- **Hint:** Compare the denominators.

### ch15-quiz-04
- **Kind:** Course original
- **Concepts:** The t statistic & SE
- **Type:** numeric
- **Question:**

To check the folk value of 98.6 °F for human body temperature, researchers measured 25 random people: mean 98.524 °F, sample variance 0.4594.

The sample SD is 0.678 °F. What is the standard error of the mean?

- **Answer (tutor only):** 0.136
- **Explanation (tutor only):** SE = SD / √n = 0.678 / √25 = 0.678 / 5 = 0.136 °F.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: dividing by n (0.027), or using the variance (0.092).
- **Hint:** SE = SD / √n.

### ch15-quiz-04-v1
- **Kind:** AI-written version of ch15-quiz-04
- **Concepts:** The t statistic & SE
- **Type:** numeric
- **Question:**

To check the folk value of 98.6 °F for human body temperature, a class measured 16 healthy volunteers: mean 98.30 °F, sample variance 0.64.

The sample SD is 0.80 °F. What is the standard error of the mean?

- **Answer (tutor only):** 0.2
- **Explanation (tutor only):** SE = 0.80 / √16 = 0.80 / 4 = 0.20 °F.
- **Hint:** SD / √n.

### ch15-quiz-04-v2
- **Kind:** AI-written version of ch15-quiz-04
- **Concepts:** The t statistic & SE
- **Type:** numeric
- **Question:**

To check the folk value of 98.6 °F for human body temperature, researchers measured 25 random people: mean 98.524 °F, sample variance 0.4594.

The sample SD is 0.678 °F. What would the standard error be if the same SD came from a sample of 100 people?

- **Answer (tutor only):** 0.0678
- **Explanation (tutor only):** SE = 0.678 / √100 = 0.0678 °F.
- **Hint:** SD / √n with n = 100.

### ch15-quiz-05
- **Kind:** Course original
- **Concepts:** The t statistic & SE
- **Type:** numeric
- **Question:**

To check the folk value of 98.6 °F for human body temperature, researchers measured 25 random people: mean 98.524 °F, sample variance 0.4594.

The estimate minus the null value is -0.076, and the standard error is 0.136. What is t?

- **Answer (tutor only):** -0.56
- **Explanation (tutor only):** t = -0.076 / 0.136 = -0.56. The sample mean is about half a standard error below 98.6.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: dividing by the SD (gives -0.11, which is Cohen's d).
- **Hint:** t = (estimate - null) / SE.

### ch15-quiz-05-v1
- **Kind:** AI-written version of ch15-quiz-05
- **Concepts:** The t statistic & SE
- **Type:** numeric
- **Question:**

To check the folk value of 98.6 °F for human body temperature, a class measured 16 healthy volunteers: mean 98.30 °F, sample variance 0.64.

The estimate minus the null value is -0.30, and the standard error is 0.20. What is t?

- **Answer (tutor only):** -1.5
- **Explanation (tutor only):** t = -0.30 / 0.20 = -1.5.
- **Hint:** Numerator ÷ SE.

### ch15-quiz-05-v2
- **Kind:** AI-written version of ch15-quiz-05
- **Concepts:** The t statistic & SE
- **Type:** numeric
- **Question:**

To check the folk value of 98.6 °F for human body temperature, researchers measured 25 random people: mean 98.524 °F, sample variance 0.4594.

The numerator of t is -0.076 and the standard error is 0.136. If the sample had been 4 times larger with the same mean and SD, the SE would be 0.068. What would t be?

- **Answer (tutor only):** -1.12
- **Explanation (tutor only):** t = -0.076 / 0.068 = -1.12. Quadrupling n halves the SE and doubles t.
- **Hint:** Numerator ÷ the new SE.

### ch15-quiz-06
- **Kind:** Course original
- **Concepts:** The t statistic & SE; p-values & NHST
- **Type:** MC
- **Question:**

To check the folk value of 98.6 °F for human body temperature, researchers measured 25 random people: mean 98.524 °F, sample variance 0.4594.

t = -0.56 (24 df). Before calculating a p-value, what do you expect to do with the null hypothesis at α = 0.05?

- **Options:**

  A) Obviously reject the null
  B) Obviously fail to reject the null
  C) Uncertain: it's on the border, so I should look it up

- **Answer (tutor only):** B
- **Explanation (tutor only):** To reject at α = 0.05 we need |t| of roughly 2 or more. A t of -0.56 means the sample mean is only about half a standard error from 98.6, which happens all the time by chance. (The p-value is 0.58.)
- **Why the wrong options are wrong (tutor only):**
  A) t is far too small to reject.
  C) Borderline would be |t| near 2.
- **Hint:** Roughly how many standard errors away does an estimate need to be to reject at α = 0.05?

### ch15-quiz-06-v1
- **Kind:** AI-written version of ch15-quiz-06
- **Concepts:** The t statistic & SE; p-values & NHST
- **Type:** MC
- **Question:**

To check the folk value of 98.6 °F for human body temperature, a class measured 16 healthy volunteers: mean 98.30 °F, sample variance 0.64.

t = -1.5 (15 df). Before calculating a p-value, what do you expect to do with the null hypothesis at α = 0.05?

- **Options:**

  A) Obviously reject the null
  B) Probably fail to reject the null
  C) Can't tell without knowing the SD

- **Answer (tutor only):** B
- **Explanation (tutor only):** Rejecting at α = 0.05 needs |t| of about 2 or more (2.13 for 15 df). -1.5 isn't there. (p = 0.15.)
- **Why the wrong options are wrong (tutor only):**
  A) |t| is below ~2.
  C) t already incorporates the SD.
- **Hint:** Compare |t| with about 2.

### ch15-quiz-06-v2
- **Kind:** AI-written version of ch15-quiz-06
- **Concepts:** The t statistic & SE; p-values & NHST
- **Type:** MC
- **Question:**

A one-sample t-test with 24 df gives t = 4.8. Before calculating a p-value, what do you expect to do with the null hypothesis at α = 0.05?

- **Options:**

  A) Clearly fail to reject the null
  B) Uncertain: it's on the border
  C) Clearly reject the null

- **Answer (tutor only):** C
- **Explanation (tutor only):** |t| = 4.8 is far beyond the critical value of about 2.06, so p is tiny (< 0.001).
- **Why the wrong options are wrong (tutor only):**
  A) Large |t| means the estimate is far from the null.
  B) 4.8 is nowhere near the border of ~2.
- **Hint:** Compare |t| with about 2.

### ch15-quiz-07
- **Kind:** Course original
- **Concepts:** p-values & NHST
- **Type:** MC
- **Question:**

To check the folk value of 98.6 °F for human body temperature, researchers measured 25 random people: mean 98.524 °F, sample variance 0.4594.

The two-tailed p-value is 0.58. At α = 0.05, what do we do and conclude?

- **Options:**

  A) Reject the null; mean body temperature is not 98.6 °F
  B) Fail to reject the null; mean body temperature is exactly 98.6 °F
  C) Fail to reject the null; we act as if it's true, but could be wrong
  D) Accept the null; the null has a greater than 0.5 chance of being true

- **Answer (tutor only):** C
- **Explanation (tutor only):** p = 0.58 > 0.05, so we fail to reject. That doesn't prove the mean is exactly 98.6; it means our data are consistent with it. A p-value also isn't the probability the null is true.
- **Why the wrong options are wrong (tutor only):**
  A) p is much bigger than 0.05.
  B) Failing to reject isn't proof the null is true.
  D) We never 'accept' the null, and p isn't the probability the null is true.
- **Hint:** Compare p to α. Then ask what a non-significant result can and can't tell you.

### ch15-quiz-07-v1
- **Kind:** AI-written version of ch15-quiz-07
- **Concepts:** p-values & NHST
- **Type:** MC
- **Question:**

To check the folk value of 98.6 °F for human body temperature, a class measured 16 healthy volunteers: mean 98.30 °F, sample variance 0.64.

The two-tailed p-value is 0.15. At α = 0.05, what do we do and conclude?

- **Options:**

  A) Reject the null; mean body temperature is not 98.6 °F
  B) Fail to reject; mean body temperature is exactly 98.6 °F
  C) Fail to reject; the data are consistent with a mean of 98.6 °F
  D) Accept the null; it has an 85% chance of being true

- **Answer (tutor only):** C
- **Explanation (tutor only):** p > 0.05, so we fail to reject. That means the data are consistent with 98.6, not that it's proven.
- **Why the wrong options are wrong (tutor only):**
  A) p > α.
  B) Failing to reject doesn't prove the null.
  D) p isn't the probability the null is false.
- **Hint:** Failing to reject ≠ proving the null.

### ch15-quiz-07-v2
- **Kind:** AI-written version of ch15-quiz-07
- **Concepts:** p-values & NHST
- **Type:** MC
- **Question:**

A one-sample t-test of whether mean body temperature equals 98.6 °F gives p = 0.002. At α = 0.05, what do we do and conclude?

- **Options:**

  A) Fail to reject; p is smaller than α, so the null stands
  B) Reject; there's a 0.2% chance the mean is 98.6 °F
  C) Reject; the data are unlikely if the mean were 98.6 °F
  D) Fail to reject; we need a larger sample to decide

- **Answer (tutor only):** C
- **Explanation (tutor only):** p < α, so we reject: data this extreme would be rare if the true mean were 98.6.
- **Why the wrong options are wrong (tutor only):**
  A) and D) p < α means we reject.
  B) p isn't the probability the null is true.
- **Hint:** What does a small p say about the data under the null?

### ch15-quiz-08
- **Kind:** Course original
- **Concepts:** The t statistic & SE; p-values & NHST
- **Type:** MC
- **Question:**

For the body temperature data (t = -0.56, n = 25, so 24 df), which R code gives the two-tailed p-value?

- **Options:**

  A) 2 * pt(0.56, df = 24, lower.tail = FALSE)
  B) pt(0.56, df = 24, lower.tail = FALSE)
  C) 2 * pt(0.56, df = 25)
  D) qt(0.56, df = 24)

- **Answer (tutor only):** A
- **Explanation (tutor only):** pt(..., lower.tail = FALSE) gives the area above |t| in one tail; doubling it gives a two-tailed p-value. The df for a one-sample t-test are n - 1 = 24.
- **Why the wrong options are wrong (tutor only):**
  B) This is one-tailed.
  C) Uses the wrong df, and the lower tail of a positive value (that's about 0.71 before doubling).
  D) qt() returns a quantile, not a probability.
- **Hint:** Two tails, upper area, n - 1 degrees of freedom.

### ch15-quiz-08-v1
- **Kind:** AI-written version of ch15-quiz-08
- **Concepts:** The t statistic & SE; p-values & NHST
- **Type:** MC
- **Question:**

For the body temperature data (t = -0.56, n = 25, so 24 df), which R code gives the ONE-tailed p-value for the alternative that mean temperature is LESS than 98.6?

- **Options:**

  A) 2 * pt(-0.56, df = 24)
  B) pt(-0.56, df = 24)
  C) qt(-0.56, df = 24)
  D) pt(-0.56, df = 24, lower.tail = FALSE)

- **Answer (tutor only):** B
- **Explanation (tutor only):** pt() gives the area below t, which is the lower tail for this one-sided alternative.
- **Why the wrong options are wrong (tutor only):**
  A) That's two-tailed.
  C) qt() takes a probability.
  D) That's the area above -0.56.
- **Hint:** Which tail matches 'less than'?

### ch15-quiz-08-v2
- **Kind:** AI-written version of ch15-quiz-08
- **Concepts:** The t statistic & SE; p-values & NHST
- **Type:** MC
- **Question:**

For a one-sample t-test with n = 16 and t = 2.1, which R code gives the two-tailed p-value?

- **Options:**

  A) 2 * pt(2.1, df = 15, lower.tail = FALSE)
  B) 2 * pt(2.1, df = 15)
  C) pt(2.1, df = 15, lower.tail = FALSE)
  D) 2 * pt(2.1, df = 16, lower.tail = FALSE)

- **Answer (tutor only):** A
- **Explanation (tutor only):** One-sample df = n - 1 = 15. Area above |t| in one tail, doubled.
- **Why the wrong options are wrong (tutor only):**
  B) That doubles the area BELOW 2.1, giving more than 1.
  C) That's one-tailed.
  D) df should be 15.
- **Hint:** df = n - 1; double one tail.

### ch15-quiz-09
- **Kind:** Course original
- **Concepts:** t vs z; Effect size & CIs
- **Type:** MC
- **Question:**

To check the folk value of 98.6 °F for human body temperature, researchers measured 25 random people: mean 98.524 °F, sample variance 0.4594.

The standard error is 0.136 and the critical t value for 24 df at α = 0.05 is 2.064. What is the 95% confidence interval for mean body temperature?

- **Options:**

  A) 98.52 ± 0.136, i.e. (98.39, 98.66)
  B) 98.52 ± 0.28, i.e. (98.24, 98.80)
  C) 98.52 ± 1.40, i.e. (97.12, 99.92)
  D) 98.6 ± 0.28, i.e. (98.32, 98.88)

- **Answer (tutor only):** B
- **Explanation (tutor only):** 95% CI = estimate ± critical t × SE = 98.524 ± 2.064 × 0.136 = 98.524 ± 0.28, or (98.24, 98.80). The interval includes 98.6, matching our failure to reject.
- **Why the wrong options are wrong (tutor only):**
  A) Forgets to multiply the SE by the critical t.
  C) Uses the SD (0.678) instead of the SE.
  D) Centers the interval on the null value instead of the estimate.
- **Hint:** CI = estimate ± critical t × SE.

### ch15-quiz-09-v1
- **Kind:** AI-written version of ch15-quiz-09
- **Concepts:** t vs z; Effect size & CIs
- **Type:** MC
- **Question:**

To check the folk value of 98.6 °F for human body temperature, a class measured 16 healthy volunteers: mean 98.30 °F, sample variance 0.64.

The standard error is 0.20 and the critical t value for 15 df at α = 0.05 is 2.131. What is the 95% confidence interval for mean body temperature?

- **Options:**

  A) 98.30 ± 0.43, i.e. (97.87, 98.73)
  B) 98.30 ± 0.20, i.e. (98.10, 98.50)
  C) 98.30 ± 1.70, i.e. (96.60, 100.00)
  D) 98.60 ± 0.43, i.e. (98.17, 99.03)

- **Answer (tutor only):** A
- **Explanation (tutor only):** 98.30 ± 2.131 × 0.20 = 98.30 ± 0.43. It includes 98.6, matching p > 0.05.
- **Why the wrong options are wrong (tutor only):**
  B) Forgets the critical t.
  C) Uses the SD × critical t.
  D) Centers on the null value instead of the estimate.
- **Hint:** Estimate ± critical t × SE.

### ch15-quiz-09-v2
- **Kind:** AI-written version of ch15-quiz-09
- **Concepts:** t vs z; Effect size & CIs
- **Type:** MC
- **Question:**

To check the folk value of 98.6 °F for human body temperature, researchers measured 25 random people: mean 98.524 °F, sample variance 0.4594.

The 95% confidence interval for mean body temperature is (98.24, 98.80). Without calculating a p-value, what can you say about a test of the null hypothesis that the mean is 98.6 °F?

- **Options:**

  A) p > 0.05, because 98.6 is inside the 95% CI
  B) p < 0.05, because 98.6 is inside the 95% CI
  C) Nothing; CIs and p-values are unrelated
  D) p > 0.05, because 98.6 is not equal to 98.524

- **Answer (tutor only):** A
- **Explanation (tutor only):** A two-tailed test at α = 0.05 rejects exactly when the null value falls outside the 95% CI. 98.6 is inside, so p > 0.05.
- **Why the wrong options are wrong (tutor only):**
  B) Inside the CI means don't reject.
  C) They're two sides of the same calculation.
  D) The estimate never equals the null exactly.
- **Hint:** Is 98.6 inside the interval?

## Chapter 16: Comparing two means

### ch16-book-01
- **Kind:** Course original
- **Concepts:** Two-sample t & equal variance
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch16-book-frogs.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch16-book-frogs.png)
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

The plot shows each mated pair and the group means with 95% CIs. What pattern do you see?

- **Options:**

  A) Similar numbers (or slight differences) of hatched eggs in the preferred and nonpreferred treatments
  B) Way more hatched eggs in the preferred treatment
  C) Way more hatched eggs in the nonpreferred treatment

- **Answer (tutor only):** A
- **Explanation (tutor only):** The means differ a bit (414 vs 345), but there's huge variation within each group and the CIs overlap broadly.
- **Why the wrong options are wrong (tutor only):**
  B) The preferred mean is actually slightly lower.
  C) The nonpreferred mean is higher, but not by much compared to the spread.
- **Hint:** Compare the difference in means to the spread of points within each group.

### ch16-book-01-v1
- **Kind:** AI-written version of ch16-book-01
- **Concepts:** Two-sample t & equal variance
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch16-book-frogs.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch16-book-frogs.png)
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

The plot shows each mated pair and the group means with 95% CIs. What does the spread of points tell you?

- **Options:**

  A) Only the nonpreferred treatment shows much variation
  B) Hatched eggs are nearly identical within each treatment
  C) Hatched eggs vary hugely among pairs in both treatments
  D) Only the preferred treatment shows much variation

- **Answer (tutor only):** C
- **Explanation (tutor only):** Both groups range from near 0 to around 900 eggs; variation within groups dwarfs the difference between them.
- **Why the wrong options are wrong (tutor only):**
  B) There's huge variation.
  D) and A) Both groups vary similarly (variances 56,118 vs 67,412).
- **Hint:** Look at the range of points in each group.

### ch16-book-01-v2
- **Kind:** AI-written version of ch16-book-01
- **Concepts:** Two-sample t & equal variance
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch16-book-frogs.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch16-book-frogs.png)
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

The plot shows each mated pair and the group means with 95% CIs. What do the overlapping CIs suggest?

- **Options:**

  A) The treatments definitely have identical means
  B) The data don't clearly show a difference between treatments
  C) Preferred females clearly produce more hatched eggs
  D) Nonpreferred females clearly produce more hatched eggs

- **Answer (tutor only):** B
- **Explanation (tutor only):** Broadly overlapping CIs suggest the difference may not be significant (p = 0.30). That's not proof the means are equal.
- **Why the wrong options are wrong (tutor only):**
  A) Overlap doesn't prove equality.
  C) and D) The difference is uncertain.
- **Hint:** Overlap ≠ identical.

### ch16-book-02
- **Kind:** Course original
- **Concepts:** Two-sample t & equal variance
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch16-book-frog-hists.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch16-book-frog-hists.png)
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs. The figure shows histograms of hatched eggs, (A) with both treatments combined and (B) separately for each treatment. Which is more useful for evaluating the normality assumption of the two-sample t-test?

- **Options:**

  A) Both treatments combined
  B) Data separated by treatment
  C) It depends: integrate information from both
  D) Neither plot is appropriate

- **Answer (tutor only):** B
- **Explanation (tutor only):** The t-test assumes the residuals (values minus their group mean) are normal, so we look within each group. A combined histogram can look odd just because the groups have different means.
- **Why the wrong options are wrong (tutor only):**
  A) Mixing two groups with different means can create shapes that aren't a problem.
  C) The combined plot adds nothing for this assumption.
  D) Within-group histograms are appropriate (a QQ plot of residuals is another good option).
- **Hint:** The normality assumption is about variation around each group's mean.

### ch16-book-02-v1
- **Kind:** AI-written version of ch16-book-02
- **Concepts:** Two-sample t & equal variance
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch16-book-frog-hists.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch16-book-frog-hists.png)
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

The figure shows histograms of hatched eggs, (A) with both treatments combined and (B) separately for each treatment. Why can the combined histogram be misleading for checking normality?

- **Options:**

  A) Mixing groups with different means can create odd shapes
  B) Combining groups always makes the data look more normal
  C) The combined plot has too many observations to judge
  D) It isn't misleading; it's the best plot for this purpose

- **Answer (tutor only):** A
- **Explanation (tutor only):** The t-test assumes normal residuals within groups. Two normal groups with different means can make a lumpy or skewed combined histogram.
- **Why the wrong options are wrong (tutor only):**
  B) It can go either way.
  C) More data helps judge shape.
  D) Check within groups.
- **Hint:** What does the t-test assume is normal?

### ch16-book-02-v2
- **Kind:** AI-written version of ch16-book-02
- **Concepts:** Two-sample t & equal variance
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch16-book-frog-hists.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch16-book-frog-hists.png)
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

The figure shows histograms of hatched eggs, (A) with both treatments combined and (B) separately for each treatment. The two-sample t-test assumes that ____ are normally distributed.

- **Options:**

  A) The two treatment means, compared to each other
  B) The values within each treatment (the residuals)
  C) The values with both treatments combined
  D) The p-values from many repeated studies

- **Answer (tutor only):** B
- **Explanation (tutor only):** The assumption is about residuals: each value minus its group mean.
- **Why the wrong options are wrong (tutor only):**
  A) and D) Not the assumption.
  C) Combined data mix two means.
- **Hint:** Residuals.

### ch16-book-03
- **Kind:** Course original
- **Concepts:** Two-sample t & equal variance
- **Type:** MC
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

Should you feel comfortable assuming equal variance?

- **Options:**

  A) Yes
  B) No
  C) Maybe
  D) I don't know (I need to run a statistical test to evaluate this assumption)

- **Answer (tutor only):** A
- **Explanation (tutor only):** 67,412 / 56,118 = 1.2: the variances are very similar, well within the rule of thumb (less than about 5).
- **Why the wrong options are wrong (tutor only):**
  B) and C) The variances differ by only about 20%.
  D) A rule of thumb (and a look at the data) is enough; formal tests of equal variance aren't needed.
- **Hint:** Divide the bigger variance by the smaller one.

### ch16-book-03-v1
- **Kind:** AI-written version of ch16-book-03
- **Concepts:** Two-sample t & equal variance
- **Type:** MC
- **Question:**

Two groups of 15 tadpoles have growth-rate variances of 4.0 and 26.0. Should you feel comfortable assuming equal variance?

- **Options:**

  A) No
  B) Maybe
  C) Yes

- **Answer (tutor only):** A
- **Explanation (tutor only):** 26.0 / 4.0 = 6.5, beyond the rule of thumb of about 5. Welch's t-test would be safer.
- **Why the wrong options are wrong (tutor only):**
  C) and B) The ratio exceeds 5.
- **Hint:** Ratio of variances.

### ch16-book-03-v2
- **Kind:** AI-written version of ch16-book-03
- **Concepts:** Two-sample t & equal variance
- **Type:** MC
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

What is the ratio of the larger variance to the smaller one?

- **Options:**

  A) About 1.2
  B) About 5
  C) About 12
  D) About 68

- **Answer (tutor only):** A
- **Explanation (tutor only):** 67,412 / 56,118 = 1.20.
- **Why the wrong options are wrong (tutor only):**
  B) That's the rule-of-thumb cutoff.
  C) That's the trout ratio.
  D) That's the difference in means.
- **Hint:** Divide the larger variance by the smaller.

### ch16-book-04
- **Kind:** Course original
- **Concepts:** Two-sample t & equal variance
- **Type:** numeric
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

What is the pooled variance?

- **Answer (tutor only):** 61556
- **Explanation (tutor only):** s²ₚ = [(29 - 1) × 56,118 + (27 - 1) × 67,412] / (29 + 27 - 2) = (1,571,304 + 1,752,712) / 54 = 61,556.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: a simple average of the two variances (61,765). The groups differ in size, so weight by degrees of freedom.
- **Hint:** Weight each variance by its degrees of freedom (n - 1).

### ch16-book-04-v1
- **Kind:** AI-written version of ch16-book-04
- **Concepts:** Two-sample t & equal variance
- **Type:** numeric
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

What is the pooled standard deviation? (The pooled variance is 61,556.)

- **Answer (tutor only):** 248.1
- **Explanation (tutor only):** √61,556 = 248.1 eggs.
- **Hint:** Square root of the pooled variance.

### ch16-book-04-v2
- **Kind:** AI-written version of ch16-book-04
- **Concepts:** Two-sample t & equal variance
- **Type:** numeric
- **Question:**

Group 1 has n = 11 and variance 40; group 2 has n = 21 and variance 70. What is the pooled variance?

- **Answer (tutor only):** 60
- **Explanation (tutor only):** (10 × 40 + 20 × 70) / (11 + 21 - 2) = (400 + 1,400) / 30 = 60.
- **Hint:** Weight each variance by n - 1.

### ch16-book-05
- **Kind:** Course original
- **Concepts:** Effect size vs significance
- **Type:** MC
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

The pooled variance is 61,556. How would you characterize the effect size?

- **Options:**

  A) Not worth reporting (d < 0.01)
  B) Tiny (0.01 to 0.20)
  C) Small (0.20 to 0.50)
  D) Medium (0.50 to 0.80)
  E) Large (0.80 to 1.20)
  F) Very large (1.20 to 2.00)
  G) Huge (> 2.00)

- **Answer (tutor only):** C
- **Explanation (tutor only):** Pooled SD = √61,556 = 248. d = (413.9 - 345.1) / 248 = 68.8 / 248 = 0.28, a small effect.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: dividing by the variance (gives about 0.001, 'not worth reporting').
- **Hint:** Use the pooled SD, not the pooled variance.

### ch16-book-05-v1
- **Kind:** AI-written version of ch16-book-05
- **Concepts:** Effect size vs significance
- **Type:** MC
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

The pooled SD is 248. If the difference in means had been 250 eggs instead of 68.8, how would you characterize the effect size?

- **Options:**

  A) Small (0.20 to 0.50)
  B) Medium (0.50 to 0.80)
  C) Large (0.80 to 1.20)
  D) Huge (> 2.00)

- **Answer (tutor only):** C
- **Explanation (tutor only):** d = 250 / 248 = 1.01, large.
- **Why the wrong options are wrong (tutor only):**
  A) and B) Too small.
  D) Not above 2.
- **Hint:** Difference ÷ pooled SD.

### ch16-book-05-v2
- **Kind:** AI-written version of ch16-book-05
- **Concepts:** Effect size vs significance
- **Type:** MC
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

The pooled SD is 248 eggs and the difference in means is 68.8 eggs. What is Cohen's d?

- **Options:**

  A) 0.28
  B) 1.04
  C) 3.6
  D) 68.8

- **Answer (tutor only):** A
- **Explanation (tutor only):** d = 68.8 / 248 = 0.28.
- **Why the wrong options are wrong (tutor only):**
  B) That's t (68.8 / SE of 66.4).
  C) That's 248 / 68.8, upside down.
  D) That's the raw difference.
- **Hint:** Difference ÷ pooled SD.

### ch16-book-06
- **Kind:** Course original
- **Concepts:** Effect size vs significance; Interpreting tests
- **Type:** MC
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

Cohen's d is 0.28. From this value alone, we can conclude that:

- **Options:**

  A) We should reject the null hypothesis
  B) We should fail to reject the null hypothesis
  C) The null is false
  D) The null is true
  E) None of these: d describes size, not evidence

- **Answer (tutor only):** E
- **Explanation (tutor only):** Whether we reject depends on the effect size and the sample size together (through the SE and t). A small effect can be significant in a big study, and a large one non-significant in a small study.
- **Why the wrong options are wrong (tutor only):**
  A) and B) To decide, we need t (or p), which depends on sample size.
  C) and D) No single number proves the null true or false.
- **Hint:** Does Cohen's d depend on sample size?

### ch16-book-06-v1
- **Kind:** AI-written version of ch16-book-06
- **Concepts:** Effect size vs significance; Interpreting tests
- **Type:** MC
- **Question:**

A study reports Cohen's d = 1.5 but doesn't give the sample size. What can you conclude?

- **Options:**

  A) The effect is large, but we can't tell if p < 0.05
  B) The null must be rejected, because the effect is large
  C) The null must be true, because no p-value is given
  D) The study must have had a large sample size

- **Answer (tutor only):** A
- **Explanation (tutor only):** d describes magnitude. Significance also depends on n: with 3 per group, even d = 1.5 may not be significant.
- **Why the wrong options are wrong (tutor only):**
  B) Small samples can miss large effects.
  C) Missing p says nothing.
  D) d doesn't reveal n.
- **Hint:** What else does significance depend on?

### ch16-book-06-v2
- **Kind:** AI-written version of ch16-book-06
- **Concepts:** Effect size vs significance; Interpreting tests
- **Type:** MC
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

The t-test gives p = 0.30 and d = 0.28. Which statement is best?

- **Options:**

  A) The effect is small, so the p-value must be wrong
  B) The p-value shows that preferred females lay fewer eggs
  C) The effect is small, so the null hypothesis must be true
  D) The estimated effect is small, and there's no clear difference

- **Answer (tutor only):** D
- **Explanation (tutor only):** d describes the estimated size; p says the data are consistent with no difference. Neither proves the null.
- **Why the wrong options are wrong (tutor only):**
  A) Small d and large p are consistent.
  B) p > 0.05; no clear difference.
  C) Failing to reject isn't proof.
- **Hint:** Size vs evidence.

### ch16-book-07
- **Kind:** Course original
- **Concepts:** Interpreting tests
- **Type:** matching
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

Match each hypothesis to its statement:

1. Null hypothesis
2. Alternative hypothesis (two-tailed)

- **Options:**

  A) Mean hatched eggs are higher with preferred females
  B) Mean hatched eggs differ between preferred and nonpreferred females
  C) Males prefer females that produce more offspring
  D) Mean hatched eggs are the same with preferred and nonpreferred females

- **Answer (tutor only):** 1-D, 2-B
- **Explanation (tutor only):** The null is no difference in population means. A two-tailed alternative allows a difference in either direction.
- **Why the wrong options are wrong (tutor only):**
  A) That's a one-tailed alternative.
  C) That's a biological hypothesis, not a statistical one.
- **Hint:** Two-tailed: a difference in either direction counts.

### ch16-book-07-v1
- **Kind:** AI-written version of ch16-book-07
- **Concepts:** Interpreting tests
- **Type:** matching
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

If the researchers had predicted in advance that preferred females would produce MORE hatched eggs, match each hypothesis for a one-tailed test:

1. Null hypothesis
2. Alternative hypothesis

- **Options:**

  A) Mean hatched eggs are higher with preferred females
  B) Mean hatched eggs are the same or lower with preferred females
  C) Males prefer females that produce more offspring
  D) Mean hatched eggs differ between the treatments

- **Answer (tutor only):** 1-B, 2-A
- **Explanation (tutor only):** A one-tailed alternative specifies the direction; the null covers everything else.
- **Why the wrong options are wrong (tutor only):**
  D) is two-tailed; C) isn't a statistical hypothesis.
- **Hint:** One direction.

### ch16-book-07-v2
- **Kind:** AI-written version of ch16-book-07
- **Concepts:** Interpreting tests
- **Type:** MC
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

Which is a statistical null hypothesis for this study?

- **Options:**

  A) Preferred females produce more hatched eggs than others
  B) Males can't tell preferred and nonpreferred females apart
  C) Population mean hatched eggs are equal in the two treatments
  D) The sample mean hatched eggs are equal in the two treatments

- **Answer (tutor only):** C
- **Explanation (tutor only):** Hypotheses are about populations. The sample means clearly differ (414 vs 345).
- **Why the wrong options are wrong (tutor only):**
  A) That's an alternative.
  B) That's a biological idea.
  D) Sample means are known and differ.
- **Hint:** Population, not sample.

### ch16-book-08
- **Kind:** Course original
- **Concepts:** Confidence intervals
- **Type:** select-all
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

A two-sample t-test (equal variance) gives a difference (nonpreferred - preferred) of 68.8 eggs, SE = 66.4, and 54 df (critical t = 2.005). Which of these values are NOT in the 95% confidence interval for the difference? (Select all that apply.)

- **Options:**

  A) -92
  B) -42
  C) 2
  D) 52
  E) 102
  F) 152
  G) 202
  H) 252

- **Answer (tutor only):** A, G, H
- **Explanation (tutor only):** 95% CI = 68.8 ± 2.005 × 66.4 = 68.8 ± 133.0, or about (-64.2, 201.8). -92, 202 and 252 fall outside.
- **Why the wrong options are wrong (tutor only):**
  202 is just outside: the upper limit is 201.8.
- **Hint:** CI = estimate ± critical t × SE.

### ch16-book-08-v1
- **Kind:** AI-written version of ch16-book-08
- **Concepts:** Confidence intervals
- **Type:** select-all
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

A two-sample t-test gives a difference of 68.8 eggs, SE = 66.4, and 54 df (critical t = 2.005). Which of these values ARE in the 95% CI for the difference? (Select all that apply.)

- **Options:**

  A) -100
  B) 0
  C) 150
  D) 250

- **Answer (tutor only):** B, C
- **Explanation (tutor only):** 68.8 ± 2.005 × 66.4 = 68.8 ± 133.1 → (-64.3, 201.9). 0 and 150 are inside.
- **Why the wrong options are wrong (tutor only):**
  A) and D) are outside.
- **Hint:** Compute the interval first.

### ch16-book-08-v2
- **Kind:** AI-written version of ch16-book-08
- **Concepts:** Confidence intervals
- **Type:** select-all
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

A two-sample t-test gives a difference of 68.8 eggs and SE = 66.4. What is t?

- **Options:**

  A) About 2.00
  B) About 1.04
  C) About 133
  D) About 0.28

- **Answer (tutor only):** B
- **Explanation (tutor only):** t = 68.8 / 66.4 = 1.04.
- **Why the wrong options are wrong (tutor only):**
  A) That's the critical t.
  C) That's the CI half-width.
  D) That's d.
- **Hint:** Difference ÷ SE.

### ch16-book-09
- **Kind:** Course original
- **Concepts:** Effect size vs significance
- **Type:** MC
- **Question:**

A two-sample t-test gives t = 1.04. If you didn't know the degrees of freedom, could you tell whether to reject the null at α = 0.05?

- **Options:**

  A) Yes: reject the null at α = 0.05
  B) Yes: fail to reject the null at α = 0.05
  C) No: I can't tell without the df

- **Answer (tutor only):** B
- **Explanation (tutor only):** The critical t at α = 0.05 is never below 1.96 (that's its limit with infinite df), so a t of about 1 is never significant, whatever the df.
- **Why the wrong options are wrong (tutor only):**
  A) t = 1.04 is far too small.
  C) For |t| below 1.96 the df don't matter.
- **Hint:** What's the smallest critical t can ever be?

### ch16-book-09-v1
- **Kind:** AI-written version of ch16-book-09
- **Concepts:** Effect size vs significance
- **Type:** MC
- **Question:**

A two-sample t-test gives t = 5.3. If you didn't know the degrees of freedom, could you tell whether to reject the null at α = 0.05?

- **Options:**

  A) Yes: fail to reject
  B) No: I can't tell
  C) Yes: reject

- **Answer (tutor only):** B
- **Explanation (tutor only):** Critical t is 2.0 to 2.8 for most studies, but with 1 df it's 12.7, so 5.3 wouldn't be significant. Without df, we can't be sure (though with any realistic df beyond 2, we'd reject).
- **Why the wrong options are wrong (tutor only):**
  A) With 3 or more df, 5.3 is significant.
  C) With 1 or 2 df the critical t is above 4.3.
- **Hint:** How large can the critical t get with very few df?

### ch16-book-09-v2
- **Kind:** AI-written version of ch16-book-09
- **Concepts:** Effect size vs significance
- **Type:** MC
- **Question:**

A two-sample t-test gives t = 1.5. Could you reject the null at α = 0.05 with any number of degrees of freedom?

- **Options:**

  A) No: the critical t is never below 1.96
  B) Yes: with very few df, 1.5 becomes significant
  C) Yes: with enough df, 1.5 becomes significant

- **Answer (tutor only):** A
- **Explanation (tutor only):** The critical t (two-tailed, α = 0.05) approaches 1.96 from above as df grow, so 1.5 is never significant.
- **Why the wrong options are wrong (tutor only):**
  B) Fewer df make the critical value larger.
  C) The critical value never drops below 1.96.
- **Hint:** What's the smallest the critical t can be?

### ch16-book-10
- **Kind:** Course original
- **Concepts:** Effect size vs significance
- **Type:** MC
- **Question:**

For a different dataset, a t-test gives t = 2.2. If you didn't know the degrees of freedom, could you tell whether to reject the null at α = 0.05?

- **Options:**

  A) Yes: reject the null at α = 0.05
  B) Yes: fail to reject the null at α = 0.05
  C) No: I can't tell without the df

- **Answer (tutor only):** C
- **Explanation (tutor only):** With many df the critical t is near 1.96, so 2.2 would be significant. With few df (e.g. 5 df, critical t = 2.57) it wouldn't.
- **Why the wrong options are wrong (tutor only):**
  A) and B) Values between about 2 and 4 depend on the df.
- **Hint:** How does the critical t change with sample size?

### ch16-book-10-v1
- **Kind:** AI-written version of ch16-book-10
- **Concepts:** Effect size vs significance
- **Type:** MC
- **Question:**

A t-test gives t = 2.4. With which degrees of freedom would you reject the null at α = 0.05? (Critical t: 2.78 for 4 df; 2.09 for 20 df.)

- **Options:**

  A) 20 df but not 4 df
  B) 4 df but not 20 df
  C) Both 4 and 20 df
  D) Neither 4 nor 20 df

- **Answer (tutor only):** A
- **Explanation (tutor only):** 2.4 > 2.09 but 2.4 < 2.78.
- **Why the wrong options are wrong (tutor only):**
  Compare 2.4 with each critical value.
- **Hint:** Is |t| above the critical value?

### ch16-book-10-v2
- **Kind:** AI-written version of ch16-book-10
- **Concepts:** Effect size vs significance
- **Type:** MC
- **Question:**

Why does the same t value (say 2.2) lead to rejection in a large study but not in a very small one?

- **Options:**

  A) Small studies always have larger effect sizes in practice
  B) The t value means different things in each study
  C) Large studies use a smaller α than small studies do
  D) Few df mean fatter t tails and a larger critical value

- **Answer (tutor only):** D
- **Explanation (tutor only):** With few df, the t has fatter tails, so the critical value is larger (2.57 for 5 df vs ~1.96 for large df).
- **Why the wrong options are wrong (tutor only):**
  A) Irrelevant.
  B) t means the same thing.
  C) α is the same.
- **Hint:** How does the critical t change with df?

### ch16-book-11
- **Kind:** Course original
- **Concepts:** Interpreting tests
- **Type:** MC
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

The t-test gives p = 0.30, so we fail to reject the null. What does this mean?

- **Options:**

  A) The null is true: there's no effect of mate choice
  B) The null is false: mate choice affects hatching
  C) We don't know; we act as if it's true, but could be wrong

- **Answer (tutor only):** C
- **Explanation (tutor only):** Failing to reject means the data are consistent with no difference, not that we've shown there is none. The CI (about -64 to 202 eggs) includes both no effect and fairly large effects.
- **Why the wrong options are wrong (tutor only):**
  A) Not rejecting doesn't prove the null.
  B) There's no evidence against the null here.
- **Hint:** Does failing to reject prove anything?

### ch16-book-11-v1
- **Kind:** AI-written version of ch16-book-11
- **Concepts:** Interpreting tests
- **Type:** MC
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

The 95% CI for the difference in hatched eggs is about -64 to 202. What does this tell us?

- **Options:**

  A) The true difference is definitely zero
  B) The true difference is definitely large
  C) Preferred females lay more eggs than nonpreferred
  D) The data fit no difference and also fairly large effects

- **Answer (tutor only):** D
- **Explanation (tutor only):** The interval includes 0 and also differences of 200 eggs; the data are too imprecise to say much.
- **Why the wrong options are wrong (tutor only):**
  A) and B) The CI includes both.
  C) The estimate is in the other direction, and uncertain.
- **Hint:** What range of values does the CI include?

### ch16-book-11-v2
- **Kind:** AI-written version of ch16-book-11
- **Concepts:** Interpreting tests
- **Type:** MC
- **Question:**

To test whether mate choice increases fitness, Swierk & Langkilde (2019) mated male wood frogs with either their preferred or their nonpreferred female and counted hatched eggs.

treatment | mean hatched eggs | variance | n
nonpreferred | 413.9 | 56,118 | 29
preferred | 345.1 | 67,412 | 27

The t-test gives p = 0.30. What would be needed to get a clearer answer about whether mate choice affects hatched eggs?

- **Options:**

  A) A larger sample, to shrink the SE and narrow the CI
  B) Switching to Welch's t-test on the same data
  C) A smaller α, such as 0.01, to make the test stricter
  D) Nothing more; p = 0.30 proves there is no effect

- **Answer (tutor only):** A
- **Explanation (tutor only):** More pairs would reduce the SE, narrowing the CI and increasing power.
- **Why the wrong options are wrong (tutor only):**
  B) The variances are similar; Welch won't help.
  C) A smaller α makes rejecting harder.
  D) Failing to reject isn't proof.
- **Hint:** What controls the width of the CI?

### ch16-chimein-01
- **Kind:** Course original
- **Concepts:** Effect size vs significance
- **Type:** MC
- **Question:**

Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise to see if it improved motor skills; finding no effect, they later decided to compare lifespans instead.

treatment | mean lifespan (days) | variance | n
no exercise | 267.3 | 224.3 | 6
exercise | 310.0 | 874.4 | 6

Pooled variance = 549.3 (pooled SD = 23.4). Difference in means (no exercise - exercise) = -42.7 days.

What is the absolute value of Cohen's d, and how big an effect is this? (Small ≈ 0.2, medium ≈ 0.5, large ≥ 0.8.)

- **Options:**

  A) |d| ≈ 0.08, small
  B) |d| ≈ 0.5, medium
  C) |d| ≈ 1.8, large
  D) |d| ≈ 3.2, large

- **Answer (tutor only):** C
- **Explanation (tutor only):** |d| = 42.7 / 23.4 = 1.82, a large effect: the groups differ by almost two pooled standard deviations.
- **Why the wrong options are wrong (tutor only):**
  A) Divides by the variance instead of the SD.
  D) 3.15 is the t value (difference / SE), not d.
- **Hint:** Divide the difference in means by the pooled SD.

### ch16-chimein-01-v1
- **Kind:** AI-written version of ch16-chimein-01
- **Concepts:** Effect size vs significance
- **Type:** MC
- **Question:**

Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise to see if it improved motor skills; finding no effect, they later decided to compare lifespans instead.

treatment | mean lifespan (days) | variance | n
no exercise | 267.3 | 224.3 | 6
exercise | 310.0 | 874.4 | 6

Pooled variance = 549.3 (pooled SD = 23.4). Difference in means (no exercise - exercise) = -42.7 days.

If the pooled SD had been 46.8 days (twice as large) with the same difference in means, what would |d| be?

- **Options:**

  A) |d| ≈ 0.45, small
  B) |d| ≈ 3.6, huge
  C) |d| ≈ 0.9, large
  D) |d| ≈ 1.8, large

- **Answer (tutor only):** C
- **Explanation (tutor only):** |d| = 42.7 / 46.8 = 0.91. Doubling the SD halves d.
- **Why the wrong options are wrong (tutor only):**
  A) Halves it twice.
  B) Doubles d instead of halving it.
  D) That's with the original SD.
- **Hint:** d = difference ÷ SD.

### ch16-chimein-01-v2
- **Kind:** AI-written version of ch16-chimein-01
- **Concepts:** Effect size vs significance
- **Type:** MC
- **Question:**

Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise to see if it improved motor skills; finding no effect, they later decided to compare lifespans instead.

treatment | mean lifespan (days) | variance | n
no exercise | 267.3 | 224.3 | 6
exercise | 310.0 | 874.4 | 6

Pooled variance = 549.3 (pooled SD = 23.4). Difference in means (no exercise - exercise) = -42.7 days.

To calculate Cohen's d for the difference in lifespan, which value do we divide 42.7 days by?

- **Options:**

  A) 13.5, the SE of the difference
  B) 6, the sample size per group
  C) 23.4, the pooled SD
  D) 549.3, the pooled variance

- **Answer (tutor only):** C
- **Explanation (tutor only):** d = 42.7 / 23.4 = 1.82.
- **Why the wrong options are wrong (tutor only):**
  A) Dividing by the SE gives t.
  B) n isn't part of d.
  D) Variance has squared units.
- **Hint:** Effect size uses the SD.

### ch16-chimein-02
- **Kind:** Course original
- **Concepts:** Interpreting tests
- **Type:** MC
- **Question:**

Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise to see if it improved motor skills; finding no effect, they later decided to compare lifespans instead.

treatment | mean lifespan (days) | variance | n
no exercise | 267.3 | 224.3 | 6
exercise | 310.0 | 874.4 | 6

Pooled variance = 549.3 (pooled SD = 23.4). Difference in means (no exercise - exercise) = -42.7 days.

The two-sample t-test gives p = 0.01. What is the probability that the true difference in lifespan between treatments is zero?

- **Options:**

  A) 0.01, the p-value from the test
  B) 0.05, the significance threshold
  C) We can't know this from a p-value

- **Answer (tutor only):** C
- **Explanation (tutor only):** p = 0.01 is the probability of a difference at least this large if the true difference were zero. It isn't the probability that the true difference is zero.
- **Why the wrong options are wrong (tutor only):**
  A) Confuses P(data | null) with P(null | data).
  B) 0.05 is the α threshold, not a probability about the null.
- **Hint:** What does a p-value assume?

### ch16-chimein-02-v1
- **Kind:** AI-written version of ch16-chimein-02
- **Concepts:** Interpreting tests
- **Type:** MC
- **Question:**

Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise to see if it improved motor skills; finding no effect, they later decided to compare lifespans instead.

treatment | mean lifespan (days) | variance | n
no exercise | 267.3 | 224.3 | 6
exercise | 310.0 | 874.4 | 6

Pooled variance = 549.3 (pooled SD = 23.4). Difference in means (no exercise - exercise) = -42.7 days.

The two-sample t-test gives p = 0.01. Which statement is correct?

- **Options:**

  A) If exercise had no effect, a difference this big would be rare
  B) There is a 1% chance that exercise has no effect on lifespan
  C) The effect of exercise on lifespan must be very large
  D) There is a 99% chance that exercise increases lifespan

- **Answer (tutor only):** A
- **Explanation (tutor only):** p is the probability of a difference at least this large if the null were true.
- **Why the wrong options are wrong (tutor only):**
  B) and D) p isn't a probability about hypotheses.
  C) p doesn't measure effect size.
- **Hint:** p assumes the null.

### ch16-chimein-02-v2
- **Kind:** AI-written version of ch16-chimein-02
- **Concepts:** Interpreting tests
- **Type:** MC
- **Question:**

Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise to see if it improved motor skills; finding no effect, they later decided to compare lifespans instead.

treatment | mean lifespan (days) | variance | n
no exercise | 267.3 | 224.3 | 6
exercise | 310.0 | 874.4 | 6

Pooled variance = 549.3 (pooled SD = 23.4). Difference in means (no exercise - exercise) = -42.7 days.

A classmate says, "p = 0.01, so there's a 99% chance exercise extends lifespan." What's wrong?

- **Options:**

  A) The classmate should have used the Welch p-value
  B) The p-value should have been compared with 0.01
  C) p is computed assuming the null; it isn't P(null)
  D) Nothing; 1 - p is the chance the alternative is true

- **Answer (tutor only):** C
- **Explanation (tutor only):** p = P(data this extreme | null), not P(null | data).
- **Why the wrong options are wrong (tutor only):**
  B) and A) Irrelevant to the misinterpretation.
  D) 1 - p isn't the probability of the alternative.
- **Hint:** Prosecutor's fallacy.

### ch16-chimein-03
- **Kind:** Course original
- **Concepts:** Two-sample t & equal variance
- **Type:** MC
- **Question:**

Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise to see if it improved motor skills; finding no effect, they later decided to compare lifespans instead.

treatment | mean lifespan (days) | variance | n
no exercise | 267.3 | 224.3 | 6
exercise | 310.0 | 874.4 | 6

Pooled variance = 549.3 (pooled SD = 23.4). Difference in means (no exercise - exercise) = -42.7 days.

test | difference | 95% CI | p-value
standard (equal variance) t | -42.7 | (-72.8, -12.5) | 0.010
Welch's t (unequal variance) | -42.7 | (-74.3, -11.0) | 0.015

In this case, compared to the standard t-test, are the p-value and 95% confidence interval from Welch's t-test (which doesn't assume equal variance) smaller, larger, or unchanged?

- **Options:**

  A) Smaller
  B) Larger
  C) Unchanged

- **Answer (tutor only):** B
- **Explanation (tutor only):** Welch's test gives p = 0.015 (vs 0.010) and a CI of (-74.3, -11.0) (vs -72.8 to -12.5). Not assuming equal variance costs some degrees of freedom, so it's a bit more conservative here.
- **Why the wrong options are wrong (tutor only):**
  A) Welch's test is usually a little more conservative.
  C) The estimate is the same, but the uncertainty changes.
- **Hint:** Welch's test uses fewer degrees of freedom.

### ch16-chimein-03-v1
- **Kind:** AI-written version of ch16-chimein-03
- **Concepts:** Two-sample t & equal variance
- **Type:** MC
- **Question:**

Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise to see if it improved motor skills; finding no effect, they later decided to compare lifespans instead.

treatment | mean lifespan (days) | variance | n
no exercise | 267.3 | 224.3 | 6
exercise | 310.0 | 874.4 | 6

Pooled variance = 549.3 (pooled SD = 23.4). Difference in means (no exercise - exercise) = -42.7 days.

The variances are 224.3 (no exercise) and 874.4 (exercise). Why might a researcher choose Welch's t-test here?

- **Options:**

  A) The sample sizes are unequal in the two groups
  B) Welch's test always gives smaller p-values
  C) The means differ by about 43 days
  D) The variances differ by a factor of about 4

- **Answer (tutor only):** D
- **Explanation (tutor only):** 874.4 / 224.3 = 3.9: near the rule-of-thumb limit, so Welch's test is a reasonable check.
- **Why the wrong options are wrong (tutor only):**
  A) Both groups have n = 6.
  B) Welch's p is usually larger.
  C) The difference in means isn't the issue.
- **Hint:** Which assumption does Welch's test drop?

### ch16-chimein-03-v2
- **Kind:** AI-written version of ch16-chimein-03
- **Concepts:** Two-sample t & equal variance
- **Type:** MC
- **Question:**

Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise to see if it improved motor skills; finding no effect, they later decided to compare lifespans instead.

treatment | mean lifespan (days) | variance | n
no exercise | 267.3 | 224.3 | 6
exercise | 310.0 | 874.4 | 6

Pooled variance = 549.3 (pooled SD = 23.4). Difference in means (no exercise - exercise) = -42.7 days.

test | difference | 95% CI | p-value
standard (equal variance) t | -42.7 | (-72.8, -12.5) | 0.010
Welch's t (unequal variance) | -42.7 | (-74.3, -11.0) | 0.015

Does dropping the equal-variance assumption change the conclusion at α = 0.05?

- **Options:**

  A) Yes: only Welch's test rejects
  B) No: neither test rejects the null
  C) Yes: only the standard test rejects
  D) No: both tests reject the null

- **Answer (tutor only):** D
- **Explanation (tutor only):** Both p-values are below 0.05, and neither CI includes 0.
- **Why the wrong options are wrong (tutor only):**
  C), A) and B) Both p < 0.05.
- **Hint:** Compare each p to 0.05.

### ch16-chimein-05
- **Kind:** Course original
- **Concepts:** Interpreting tests
- **Type:** MC
- **Question:**

Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise to see if it improved motor skills; finding no effect, they later decided to compare lifespans instead.

treatment | mean lifespan (days) | variance | n
no exercise | 267.3 | 224.3 | 6
exercise | 310.0 | 874.4 | 6

Pooled variance = 549.3 (pooled SD = 23.4). Difference in means (no exercise - exercise) = -42.7 days.

The two-sample t-test gives t = -3.15 (10 df) and p = 0.010. At α = 0.05, we ____ the null hypothesis.

- **Options:**

  A) reject
  B) accept
  C) fail to reject
  D) fail to accept

- **Answer (tutor only):** A
- **Explanation (tutor only):** 0.010 < 0.05, so we reject the null.
- **Why the wrong options are wrong (tutor only):**
  B) and D) We never 'accept' a null.
  C) p is below α.
- **Hint:** Compare p with α.

### ch16-chimein-05-v1
- **Kind:** AI-written version of ch16-chimein-05
- **Concepts:** Interpreting tests
- **Type:** MC
- **Question:**

Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise to see if it improved motor skills; finding no effect, they later decided to compare lifespans instead.

treatment | mean lifespan (days) | variance | n
no exercise | 267.3 | 224.3 | 6
exercise | 310.0 | 874.4 | 6

Pooled variance = 549.3 (pooled SD = 23.4). Difference in means (no exercise - exercise) = -42.7 days.

If the two-sample t-test had given p = 0.08, at α = 0.05 we would ____ the null hypothesis.

- **Options:**

  A) fail to accept
  B) reject
  C) accept
  D) fail to reject

- **Answer (tutor only):** D
- **Explanation (tutor only):** 0.08 > 0.05, so we fail to reject. We never 'accept' or 'prove' the null.
- **Why the wrong options are wrong (tutor only):**
  B) p > α.
  C) and A) We never accept the null.
- **Hint:** Compare p with α.

### ch16-chimein-05-v2
- **Kind:** AI-written version of ch16-chimein-05
- **Concepts:** Interpreting tests
- **Type:** MC
- **Question:**

Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise to see if it improved motor skills; finding no effect, they later decided to compare lifespans instead.

treatment | mean lifespan (days) | variance | n
no exercise | 267.3 | 224.3 | 6
exercise | 310.0 | 874.4 | 6

Pooled variance = 549.3 (pooled SD = 23.4). Difference in means (no exercise - exercise) = -42.7 days.

The two-sample t-test gives t = -3.15 with 10 df. Where does the 10 come from?

- **Options:**

  A) n₁ + n₂ - 2
  B) n₁ - 1
  C) n₁ + n₂ - 1
  D) n₁ + n₂

- **Answer (tutor only):** A
- **Explanation (tutor only):** A two-sample t-test has n₁ + n₂ - 2 df.
- **Why the wrong options are wrong (tutor only):**
  B) That's one group.
  D) and C) Subtract one df per group.
- **Hint:** One df lost per group mean.

### ch16-chimein-06
- **Kind:** Course original
- **Concepts:** p-hacking & HARKing
- **Type:** select-all
- **Question:**

Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise to see if it improved motor skills; finding no effect, they later decided to compare lifespans instead.

treatment | mean lifespan (days) | variance | n
no exercise | 267.3 | 224.3 | 6
exercise | 310.0 | 874.4 | 6

Pooled variance = 549.3 (pooled SD = 23.4). Difference in means (no exercise - exercise) = -42.7 days.

The researchers ran a two-sample t-test assuming equal variance. Which parts of the study make this p-value most suspect? (Pick the two best.)

- **Options:**

  A) Lifespan wasn't the question that motivated the study
  B) The sample size is too small
  C) They should not assume equal variance
  D) They should not assume a normal distribution
  E) The question may have been inspired by the data

- **Answer (tutor only):** A, E
- **Explanation (tutor only):** The lifespan comparison was decided after the original experiment found nothing, possibly after seeing that lifespans differed. p-values assume the hypothesis was set before looking at the data; testing hypotheses suggested by the data inflates false positives.
- **Why the wrong options are wrong (tutor only):**
  B) Small samples reduce power, but they don't make a significant p-value suspect in the same way.
  C) The variance ratio (about 3.9) is acceptable, and Welch's test agrees.
  D) Nothing suggests a strong departure from normality.
- **Hint:** When, and why, did the researchers decide to compare lifespans?

### ch16-chimein-06-v1
- **Kind:** AI-written version of ch16-chimein-06
- **Concepts:** p-hacking & HARKing
- **Type:** select-all
- **Question:**

Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise to see if it improved motor skills; finding no effect, they later decided to compare lifespans instead.

treatment | mean lifespan (days) | variance | n
no exercise | 267.3 | 224.3 | 6
exercise | 310.0 | 874.4 | 6

Pooled variance = 549.3 (pooled SD = 23.4). Difference in means (no exercise - exercise) = -42.7 days.

Which change to the study design would have made the lifespan p-value trustworthy? (Pick the two best.)

- **Options:**

  A) Using Welch's t-test instead of the standard t-test
  B) Reporting the p-value to more decimal places
  C) Deciding to compare lifespans before collecting any data
  D) Testing lifespan in a new, independent set of mice

- **Answer (tutor only):** C, D
- **Explanation (tutor only):** The problem is that the hypothesis came from the data. Pre-specifying it, or testing it on new data, fixes that.
- **Why the wrong options are wrong (tutor only):**
  A) Welch's test doesn't fix data-driven hypotheses.
  B) Precision isn't the issue.
- **Hint:** When was the hypothesis formed?

### ch16-chimein-06-v2
- **Kind:** AI-written version of ch16-chimein-06
- **Concepts:** p-hacking & HARKing
- **Type:** select-all
- **Question:**

Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise to see if it improved motor skills; finding no effect, they later decided to compare lifespans instead.

treatment | mean lifespan (days) | variance | n
no exercise | 267.3 | 224.3 | 6
exercise | 310.0 | 874.4 | 6

Pooled variance = 549.3 (pooled SD = 23.4). Difference in means (no exercise - exercise) = -42.7 days.

Why does testing a hypothesis suggested by the data inflate false positives?

- **Options:**

  A) It doesn't; p-values are valid whenever we compute them
  B) The sample size shrinks once we pick a hypothesis
  C) We notice differences that are large by chance, then test them
  D) The data become more variable once we look at them

- **Answer (tutor only):** C
- **Explanation (tutor only):** If we only test differences that already look big, many will be flukes, so far more than 5% of tests of true nulls will be 'significant'.
- **Why the wrong options are wrong (tutor only):**
  A) p-values assume a pre-specified test.
  D) and B) Looking doesn't change the data.
- **Hint:** Which differences catch our eye?

### ch16-chimein-08
- **Kind:** Course original
- **Concepts:** Confidence intervals
- **Type:** TF
- **Question:**

Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise to see if it improved motor skills; finding no effect, they later decided to compare lifespans instead.

treatment | mean lifespan (days) | variance | n
no exercise | 267.3 | 224.3 | 6
exercise | 310.0 | 874.4 | 6

Pooled variance = 549.3 (pooled SD = 23.4). Difference in means (no exercise - exercise) = -42.7 days.

The 95% CI for the difference (no exercise - exercise) is -72.8 to -12.5 days. TRUE or FALSE: Assuming all assumptions are valid, there is a 95% chance that the true mean is between -72.8 and -12.5.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** Two problems. The interval is for the difference in means, not 'the true mean'. And a 95% CI means that 95% of intervals built this way would capture the true value; once we've calculated one interval, it either contains the true difference or it doesn't.
- **Why the wrong options are wrong (tutor only):**
  TRUE: a very common way to misread a confidence interval.
- **Hint:** What is the interval about? What does '95%' refer to?

### ch16-chimein-08-v1
- **Kind:** AI-written version of ch16-chimein-08
- **Concepts:** Confidence intervals
- **Type:** TF
- **Question:**

Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise to see if it improved motor skills; finding no effect, they later decided to compare lifespans instead.

treatment | mean lifespan (days) | variance | n
no exercise | 267.3 | 224.3 | 6
exercise | 310.0 | 874.4 | 6

Pooled variance = 549.3 (pooled SD = 23.4). Difference in means (no exercise - exercise) = -42.7 days.

The 95% CI for the difference (no exercise - exercise) is -72.8 to -12.5 days. TRUE or FALSE: If this study were repeated many times, about 95% of the intervals built this way would contain the true difference.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** A
- **Explanation (tutor only):** That's the correct interpretation of a 95% CI.
- **Why the wrong options are wrong (tutor only):**
  FALSE: this is the correct interpretation.
- **Hint:** The 95% is about the procedure.

### ch16-chimein-08-v2
- **Kind:** AI-written version of ch16-chimein-08
- **Concepts:** Confidence intervals
- **Type:** TF
- **Question:**

Researchers had 6 of 12 mice with spinocerebellar ataxia (an incurable inherited motor disease) exercise to see if it improved motor skills; finding no effect, they later decided to compare lifespans instead.

treatment | mean lifespan (days) | variance | n
no exercise | 267.3 | 224.3 | 6
exercise | 310.0 | 874.4 | 6

Pooled variance = 549.3 (pooled SD = 23.4). Difference in means (no exercise - exercise) = -42.7 days.

The 95% CI for the difference (no exercise - exercise) is -72.8 to -12.5 days. TRUE or FALSE: Because 0 is not in the interval, a two-tailed test at α = 0.05 rejects the null of no difference.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** A
- **Explanation (tutor only):** A 95% CI excludes the null value exactly when a two-tailed test at α = 0.05 rejects (p = 0.010 here).
- **Why the wrong options are wrong (tutor only):**
  FALSE: CIs and tests agree.
- **Hint:** Is 0 inside the interval?

### ch16-chimein-09
- **Kind:** Course original
- **Concepts:** Effect size vs significance; Interpreting tests
- **Type:** MC
- **Question:**

Why do p-values fail to communicate effect size?

- **Options:**

  A) They involve too much stats jargon for most people
  B) They mix the size of a difference with sample size
  C) They are great descriptions of effect size

- **Answer (tutor only):** B
- **Explanation (tutor only):** The same small effect can give a tiny p-value with a huge sample, and a large effect can give a big p-value with a small sample. Effect sizes (like Cohen's d) describe how big a difference is.
- **Why the wrong options are wrong (tutor only):**
  A) Jargon isn't the issue.
  C) They aren't: see the blood pressure studies, where the tiny effect had the smaller p-value.
- **Hint:** What happens to a p-value if you collect much more data, but the effect stays the same?

### ch16-chimein-09-v1
- **Kind:** AI-written version of ch16-chimein-09
- **Concepts:** Effect size vs significance; Interpreting tests
- **Type:** MC
- **Question:**

Study A (n = 20) finds p = 0.04; study B (n = 2,000) finds p = 0.0001. Which statement is correct?

- **Options:**

  A) Both studies must have found exactly the same effect size
  B) Study B's effect must be larger because its p-value is smaller
  C) Study A's effect must be larger because its sample is smaller
  D) Study B's effect isn't necessarily larger; its sample is much larger

- **Answer (tutor only):** D
- **Explanation (tutor only):** p depends on both effect size and sample size, so smaller p doesn't imply a bigger effect.
- **Why the wrong options are wrong (tutor only):**
  A) Nothing tells us they're equal.
  B) and C) p-values don't rank effect sizes.
- **Hint:** What else changes p?

### ch16-chimein-09-v2
- **Kind:** AI-written version of ch16-chimein-09
- **Concepts:** Effect size vs significance; Interpreting tests
- **Type:** MC
- **Question:**

Which is the best way to communicate how large a difference between two groups is?

- **Options:**

  A) Report an effect size such as Cohen's d, with its CI
  B) Report the t statistic and its degrees of freedom
  C) Report the p-value with as many decimal places as possible
  D) Report whether the result was significant at α = 0.05

- **Answer (tutor only):** A
- **Explanation (tutor only):** Effect sizes describe magnitude; p-values, significance and t mix magnitude with sample size.
- **Why the wrong options are wrong (tutor only):**
  C), D) and B) All depend on n.
- **Hint:** Magnitude, not evidence.

### ch16-hw-01
- **Kind:** Course original
- **Concepts:** Two-sample t & equal variance; Confidence intervals
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch16-hw-trout.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch16-hw-trout.png)
- **Question:**

To see whether introduced brook trout harm native Chinook salmon, Levin et al. measured the proportion of juvenile salmon surviving in six streams with and six without brook trout.

trout | mean survival | variance | n
absent | 0.235 | 0.01074 | 6
present | 0.194 | 0.00088 | 6

The plot shows each stream and the group means with 95% confidence intervals. Which statements are consistent with the plot? (Select all that apply.)

- **Options:**

  A) Mean survival was higher when trout were absent than when they were present
  B) Mean survival was lower when trout were absent than when they were present
  C) There was no overlap between the 95% confidence intervals for the two treatments
  D) The 95% confidence intervals for the two groups overlap
  E) There appears to be less variation in survival when trout were present

- **Answer (tutor only):** A, D, E
- **Explanation (tutor only):** The mean is a bit higher without trout (0.235 vs 0.194), the CIs overlap broadly, and survival is much less variable among streams with trout.
- **Why the wrong options are wrong (tutor only):**
  B) The absent mean is higher.
  C) The intervals overlap a lot.
- **Hint:** Look at where the black points sit, whether the bars overlap, and how spread out each group's points are.

### ch16-hw-01-v1
- **Kind:** AI-written version of ch16-hw-01
- **Concepts:** Two-sample t & equal variance; Confidence intervals
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch16-hw-trout.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch16-hw-trout.png)
- **Question:**

To see whether introduced brook trout harm native Chinook salmon, Levin et al. measured the proportion of juvenile salmon surviving in six streams with and six without brook trout.

trout | mean survival | variance | n
absent | 0.235 | 0.01074 | 6
present | 0.194 | 0.00088 | 6

The plot shows each stream and the group means with 95% confidence intervals. Which statements are consistent with the plot? (Select all that apply.)

- **Options:**

  A) The CI for streams with trout is narrower
  B) The CI for streams without trout is narrower
  C) Survival varied more among streams without trout
  D) Every stream without trout had higher survival than every stream with trout

- **Answer (tutor only):** A, C
- **Explanation (tutor only):** Streams with trout cluster tightly (variance 0.00088), giving a narrow CI; streams without trout vary widely (0.01074). The groups overlap, so D is false.
- **Why the wrong options are wrong (tutor only):**
  B) The no-trout CI is wider.
  D) The groups overlap.
- **Hint:** Look at the spread of points in each group.

### ch16-hw-01-v2
- **Kind:** AI-written version of ch16-hw-01
- **Concepts:** Two-sample t & equal variance; Confidence intervals
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch16-hw-trout.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch16-hw-trout.png)
- **Question:**

To see whether introduced brook trout harm native Chinook salmon, Levin et al. measured the proportion of juvenile salmon surviving in six streams with and six without brook trout.

trout | mean survival | variance | n
absent | 0.235 | 0.01074 | 6
present | 0.194 | 0.00088 | 6

The plot shows each stream and the group means with 95% confidence intervals. Why is the CI wider for streams without trout, even though both groups have six streams?

- **Options:**

  A) The CI is always wider for the reference group
  B) Survival varies more among streams without trout
  C) Streams without trout had fewer salmon in them
  D) The mean survival is higher in streams without trout

- **Answer (tutor only):** B
- **Explanation (tutor only):** With equal n, CI width depends on the SD. The no-trout variance is about 12 times larger.
- **Why the wrong options are wrong (tutor only):**
  A) No such rule.
  C) Both have n = 6 streams.
  D) The mean doesn't set the width.
- **Hint:** CI width = critical t × SD / √n.

### ch16-hw-02
- **Kind:** Course original
- **Concepts:** Two-sample t & equal variance
- **Type:** MC
- **Question:**

To see whether introduced brook trout harm native Chinook salmon, Levin et al. measured the proportion of juvenile salmon surviving in six streams with and six without brook trout.

trout | mean survival | variance | n
absent | 0.235 | 0.01074 | 6
present | 0.194 | 0.00088 | 6

The standard two-sample t-test assumes equal variance. A common rule of thumb is that we're probably OK if one group's variance is less than about five times the other's. How comfortable are you assuming equal variance?

- **Options:**

  A) Totally cool: the variances are nearly identical
  B) OK, I think: the variance with brook trout is about 5 times larger than without
  C) Pretty nervous: the variances are WAY different

- **Answer (tutor only):** C
- **Explanation (tutor only):** 0.01074 / 0.00088 = 12: the variance without trout is about 12 times the variance with trout, well beyond the rule of thumb.
- **Why the wrong options are wrong (tutor only):**
  A) They differ by more than tenfold.
  B) Gets both the ratio and the direction wrong: the larger variance is where trout are absent.
- **Hint:** Divide the bigger variance by the smaller one.

### ch16-hw-02-v1
- **Kind:** AI-written version of ch16-hw-02
- **Concepts:** Two-sample t & equal variance
- **Type:** MC
- **Question:**

Two groups of 8 frogs have jumping-distance variances of 120 and 150 cm². Using the rule of thumb (OK if one variance is less than about 5 times the other), how comfortable are you assuming equal variance?

- **Options:**

  A) Comfortable: the ratio is only about 1.25
  B) Can't say without running a formal test
  C) Nervous: the variances are not identical

- **Answer (tutor only):** A
- **Explanation (tutor only):** 150 / 120 = 1.25, far below 5.
- **Why the wrong options are wrong (tutor only):**
  B) The rule of thumb is enough here.
  C) Sample variances never match exactly.
- **Hint:** Divide the larger variance by the smaller.

### ch16-hw-02-v2
- **Kind:** AI-written version of ch16-hw-02
- **Concepts:** Two-sample t & equal variance
- **Type:** MC
- **Question:**

To see whether introduced brook trout harm native Chinook salmon, Levin et al. measured the proportion of juvenile salmon surviving in six streams with and six without brook trout.

trout | mean survival | variance | n
absent | 0.235 | 0.01074 | 6
present | 0.194 | 0.00088 | 6

What is the ratio of the larger variance to the smaller one?

- **Options:**

  A) About 1.2
  B) About 5
  C) About 12
  D) About 120

- **Answer (tutor only):** C
- **Explanation (tutor only):** 0.01074 / 0.00088 = 12.2.
- **Why the wrong options are wrong (tutor only):**
  A) Compares the means, not the variances.
  B) That's the rule-of-thumb cutoff.
  D) Off by a factor of 10.
- **Hint:** Divide 0.01074 by 0.00088.

### ch16-hw-03
- **Kind:** Course original
- **Concepts:** Two-sample t & equal variance
- **Type:** numeric
- **Question:**

To see whether introduced brook trout harm native Chinook salmon, Levin et al. measured the proportion of juvenile salmon surviving in six streams with and six without brook trout.

trout | mean survival | variance | n
absent | 0.235 | 0.01074 | 6
present | 0.194 | 0.00088 | 6

What is the pooled variance? (Hint: with equal sample sizes, it is the average of the two variances.)

- **Answer (tutor only):** 0.00581
- **Explanation (tutor only):** Pooled variance = [(n₁ - 1)s₁² + (n₂ - 1)s₂²] / (n₁ + n₂ - 2) = (5 × 0.01074 + 5 × 0.00088) / 10 = 0.00581.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: averaging the standard deviations instead of the variances.
- **Hint:** Weight each variance by its degrees of freedom.

### ch16-hw-03-v1
- **Kind:** AI-written version of ch16-hw-03
- **Concepts:** Two-sample t & equal variance
- **Type:** numeric
- **Question:**

To see whether introduced brook trout harm native Chinook salmon, Levin et al. measured the proportion of juvenile salmon surviving in six streams with and six without brook trout.

trout | mean survival | variance | n
absent | 0.235 | 0.01074 | 6
present | 0.194 | 0.00088 | 6

What is the pooled standard deviation? (The pooled variance is the average of the two variances, since n is equal.)

- **Answer (tutor only):** 0.0762
- **Explanation (tutor only):** Pooled variance = (0.01074 + 0.00088) / 2 = 0.00581; pooled SD = √0.00581 = 0.0762.
- **Hint:** Average the variances, then take the square root.

### ch16-hw-03-v2
- **Kind:** AI-written version of ch16-hw-03
- **Concepts:** Two-sample t & equal variance
- **Type:** numeric
- **Question:**

Two groups of 11 lizards have variances in body temperature of 2.4 and 3.6 °C². What is the pooled variance?

- **Answer (tutor only):** 3
- **Explanation (tutor only):** (10 × 2.4 + 10 × 3.6) / 20 = 3.0. With equal n it's the average.
- **Hint:** Equal n → average the variances.

### ch16-hw-04
- **Kind:** Course original
- **Concepts:** Effect size vs significance
- **Type:** MC
- **Question:**

To see whether introduced brook trout harm native Chinook salmon, Levin et al. measured the proportion of juvenile salmon surviving in six streams with and six without brook trout.

trout | mean survival | variance | n
absent | 0.235 | 0.01074 | 6
present | 0.194 | 0.00088 | 6

The pooled variance is 0.00581 and the difference in means is 0.041. How big is this effect?

Size | Cohen's d
Not worth reporting | < 0.01
Tiny | 0.01 to 0.20
Small | 0.20 to 0.50
Medium | 0.50 to 0.80
Large | 0.80 to 1.20
Very large | 1.20 to 2.00
Huge | > 2.00

- **Options:**

  A) Not worth reporting to tiny
  B) Small to medium
  C) Large to very large
  D) Huge

- **Answer (tutor only):** B
- **Explanation (tutor only):** Pooled SD = √0.00581 = 0.0762. d = 0.041 / 0.0762 = 0.54, a medium effect (near the small/medium boundary).
- **Why the wrong options are wrong (tutor only):**
  A) Comes from dividing by the variance, or forgetting to take the square root.
  C) and D) Too big: the difference is about half a standard deviation.
- **Hint:** Cohen's d needs the pooled SD, which is the square root of the pooled variance.

### ch16-hw-04-v1
- **Kind:** AI-written version of ch16-hw-04
- **Concepts:** Effect size vs significance
- **Type:** MC
- **Question:**

To see whether introduced brook trout harm native Chinook salmon, Levin et al. measured the proportion of juvenile salmon surviving in six streams with and six without brook trout.

trout | mean survival | variance | n
absent | 0.235 | 0.01074 | 6
present | 0.194 | 0.00088 | 6

The pooled SD is 0.0762. If the difference in means had been 0.10 instead of 0.041, how big would the effect be?

Size | Cohen's d
Tiny | 0.01 to 0.20
Small | 0.20 to 0.50
Medium | 0.50 to 0.80
Large | 0.80 to 1.20
Very large | 1.20 to 2.00
Huge | > 2.00

- **Options:**

  A) A small effect
  B) A medium effect
  C) A very large effect
  D) A huge effect

- **Answer (tutor only):** C
- **Explanation (tutor only):** d = 0.10 / 0.0762 = 1.31, very large.
- **Why the wrong options are wrong (tutor only):**
  A) and B) Too small.
  D) Not above 2.
- **Hint:** Difference ÷ pooled SD.

### ch16-hw-04-v2
- **Kind:** AI-written version of ch16-hw-04
- **Concepts:** Effect size vs significance
- **Type:** MC
- **Question:**

To see whether introduced brook trout harm native Chinook salmon, Levin et al. measured the proportion of juvenile salmon surviving in six streams with and six without brook trout.

trout | mean survival | variance | n
absent | 0.235 | 0.01074 | 6
present | 0.194 | 0.00088 | 6

To calculate Cohen's d for these data, we divide the difference in means (0.041) by:

- **Options:**

  A) The standard error of the difference, 0.044
  B) The difference's 95% confidence interval
  C) The pooled variance, 0.00581
  D) The pooled standard deviation, 0.0762

- **Answer (tutor only):** D
- **Explanation (tutor only):** d = 0.041 / 0.0762 = 0.54.
- **Why the wrong options are wrong (tutor only):**
  A) Dividing by the SE gives t.
  B) A CI isn't a single scale.
  C) Variance has squared units.
- **Hint:** Effect size uses the SD.

### ch16-hw-05
- **Kind:** Course original
- **Concepts:** Effect size vs significance; Two-sample t & equal variance
- **Type:** numeric
- **Question:**

To see whether introduced brook trout harm native Chinook salmon, Levin et al. measured the proportion of juvenile salmon surviving in six streams with and six without brook trout.

trout | mean survival | variance | n
absent | 0.235 | 0.01074 | 6
present | 0.194 | 0.00088 | 6

The pooled variance is 0.00581. What is the standard error of the difference in means? (Report to three decimals.)

- **Answer (tutor only):** 0.044
- **Explanation (tutor only):** SE = √[s²ₚ (1/n₁ + 1/n₂)] = √[0.00581 × (1/6 + 1/6)] = √0.001937 = 0.044.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: forgetting the square root (0.0019), or using only one 1/n term (0.031).
- **Hint:** SE = √(pooled variance × (1/n₁ + 1/n₂)).

### ch16-hw-05-v1
- **Kind:** AI-written version of ch16-hw-05
- **Concepts:** Effect size vs significance; Two-sample t & equal variance
- **Type:** numeric
- **Question:**

To see whether introduced brook trout harm native Chinook salmon, Levin et al. measured the proportion of juvenile salmon surviving in six streams with and six without brook trout.

trout | mean survival | variance | n
absent | 0.235 | 0.01074 | 6
present | 0.194 | 0.00088 | 6

The pooled variance is 0.00581 and the difference in means is 0.041. The SE of the difference is 0.044. What is t? (Report to two decimals.)

- **Answer (tutor only):** 0.93
- **Explanation (tutor only):** t = 0.041 / 0.044 = 0.93.
- **Hint:** Difference ÷ SE.

### ch16-hw-05-v2
- **Kind:** AI-written version of ch16-hw-05
- **Concepts:** Effect size vs significance; Two-sample t & equal variance
- **Type:** numeric
- **Question:**

Two groups of 8 frogs have a pooled variance of 50. What is the standard error of the difference in means? (Report to two decimals.)

- **Answer (tutor only):** 3.54
- **Explanation (tutor only):** SE = √[50 × (1/8 + 1/8)] = √12.5 = 3.54.
- **Hint:** √[s²ₚ (1/n₁ + 1/n₂)].

### ch16-hw-06
- **Kind:** Course original
- **Concepts:** Two-sample t & equal variance
- **Type:** MC
- **Question:**

To see whether introduced brook trout harm native Chinook salmon, Levin et al. measured the proportion of juvenile salmon surviving in six streams with and six without brook trout.

trout | mean survival | variance | n
absent | 0.235 | 0.01074 | 6
present | 0.194 | 0.00088 | 6

Here are results from a standard two-sample t-test and from Welch's t-test (which doesn't assume equal variance):

test | difference (absent - present) | 95% CI | p-value
two-sample t | 0.041 | (-0.057, 0.139) | 0.374
Welch's t | 0.041 | (-0.068, 0.150) | 0.389

In this case, breaking the assumption of equal variance had:

- **Options:**

  A) A very strong effect on our conclusion
  B) A moderate effect on our conclusion
  C) An effect on our analysis small enough to safely ignore

- **Answer (tutor only):** C
- **Explanation (tutor only):** Welch's test gives a slightly wider CI and a slightly larger p-value, but the conclusion is the same: no evidence of a difference. With equal sample sizes, the standard t-test is fairly robust to unequal variances.
- **Why the wrong options are wrong (tutor only):**
  A) and B) Both tests fail to reject the null by a wide margin.
- **Hint:** Would the two tests lead you to different conclusions?

### ch16-hw-06-v1
- **Kind:** AI-written version of ch16-hw-06
- **Concepts:** Two-sample t & equal variance
- **Type:** MC
- **Question:**

To see whether introduced brook trout harm native Chinook salmon, Levin et al. measured the proportion of juvenile salmon surviving in six streams with and six without brook trout.

trout | mean survival | variance | n
absent | 0.235 | 0.01074 | 6
present | 0.194 | 0.00088 | 6

test | difference (absent - present) | 95% CI | p-value
two-sample t | 0.041 | (-0.057, 0.139) | 0.374
Welch's t | 0.041 | (-0.068, 0.150) | 0.389

Why is Welch's CI slightly wider?

- **Options:**

  A) It uses a different estimate of the difference in means
  B) It doesn't assume equal variance and uses fewer df
  C) It assumes the data are not normally distributed
  D) It always gives exactly the same CI as the standard test

- **Answer (tutor only):** B
- **Explanation (tutor only):** Welch's test estimates each group's variance separately and adjusts the df down, giving a larger critical t.
- **Why the wrong options are wrong (tutor only):**
  A) The difference is 0.041 in both.
  C) Welch's test still assumes normality.
  D) They differ here.
- **Hint:** Compare the assumptions.

### ch16-hw-06-v2
- **Kind:** AI-written version of ch16-hw-06
- **Concepts:** Two-sample t & equal variance
- **Type:** MC
- **Question:**

To see whether introduced brook trout harm native Chinook salmon, Levin et al. measured the proportion of juvenile salmon surviving in six streams with and six without brook trout.

trout | mean survival | variance | n
absent | 0.235 | 0.01074 | 6
present | 0.194 | 0.00088 | 6

test | difference (absent - present) | 95% CI | p-value
two-sample t | 0.041 | (-0.057, 0.139) | 0.374
Welch's t | 0.041 | (-0.068, 0.150) | 0.389

Do the two tests lead to the same conclusion at α = 0.05?

- **Options:**

  A) No: only the standard test rejects
  B) Yes: both reject the null
  C) No: only Welch's test rejects
  D) Yes: both fail to reject the null

- **Answer (tutor only):** D
- **Explanation (tutor only):** Both p-values are well above 0.05, and both CIs include 0.
- **Why the wrong options are wrong (tutor only):**
  B), C) and A) Both p > 0.05.
- **Hint:** Compare each p-value to 0.05.

### ch16-hw-07
- **Kind:** Course original
- **Concepts:** Interpreting tests
- **Type:** TF
- **Question:**

To see whether introduced brook trout harm native Chinook salmon, Levin et al. measured the proportion of juvenile salmon surviving in six streams with and six without brook trout.

trout | mean survival | variance | n
absent | 0.235 | 0.01074 | 6
present | 0.194 | 0.00088 | 6

TRUE or FALSE: Because we failed to reject the null hypothesis (p = 0.37), we can confidently conclude that introduced brook trout do not influence the survival of juvenile Chinook salmon.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** Failing to reject is not evidence of no effect. With only six streams per group, the 95% CI runs from about -0.06 to 0.14, which includes effects large enough to matter for salmon.
- **Why the wrong options are wrong (tutor only):**
  TRUE: absence of evidence isn't evidence of absence, especially with small samples.
- **Hint:** What range of effects is consistent with these data?

### ch16-hw-07-v1
- **Kind:** AI-written version of ch16-hw-07
- **Concepts:** Interpreting tests
- **Type:** TF
- **Question:**

To see whether introduced brook trout harm native Chinook salmon, Levin et al. measured the proportion of juvenile salmon surviving in six streams with and six without brook trout.

trout | mean survival | variance | n
absent | 0.235 | 0.01074 | 6
present | 0.194 | 0.00088 | 6

TRUE or FALSE: The 95% CI for the difference in survival (-0.057 to 0.139) includes values large enough to matter for salmon conservation.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** A
- **Explanation (tutor only):** A 14-percentage-point drop in survival would matter, and it's inside the interval. We can't rule out a meaningful effect.
- **Why the wrong options are wrong (tutor only):**
  FALSE: the upper end (0.139) is a big change in survival.
- **Hint:** Look at the upper end of the CI.

### ch16-hw-07-v2
- **Kind:** AI-written version of ch16-hw-07
- **Concepts:** Interpreting tests
- **Type:** TF
- **Question:**

To see whether introduced brook trout harm native Chinook salmon, Levin et al. measured the proportion of juvenile salmon surviving in six streams with and six without brook trout.

trout | mean survival | variance | n
absent | 0.235 | 0.01074 | 6
present | 0.194 | 0.00088 | 6

TRUE or FALSE: With p = 0.37 and only six streams per group, this study had limited power to detect a moderate effect of brook trout.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** A
- **Explanation (tutor only):** Small samples and high variability give wide CIs and low power, so failing to reject says little.
- **Why the wrong options are wrong (tutor only):**
  FALSE: six streams per group is a small study.
- **Hint:** What limits power?

### ch16-quiz-01
- **Kind:** Course original
- **Concepts:** Effect size vs significance
- **Type:** matching
- **Question:**

Two clinical studies each found that a drug lowers blood pressure by 2 mmHg (null value μ₀ = 0).

Study | n | SD (mmHg)
X | 10,000 | 20
Y | 10 | 2

Equations: SE = s / √n, t = (x̄ - μ₀) / SE, d = (x̄ - μ₀) / s

Match each study to its Cohen's d:

1. Study X
2. Study Y

- **Options:**

  A) d = 10
  B) d = 1
  C) d = 3.16
  D) d = 0.1

- **Answer (tutor only):** 1-D, 2-B
- **Explanation (tutor only):** d = difference / SD. Study X: 2 / 20 = 0.1 (tiny). Study Y: 2 / 2 = 1 (large).
- **Why the wrong options are wrong (tutor only):**
  A) and C) are the t values (difference / SE), not Cohen's d.
- **Hint:** Cohen's d uses the SD, not the SE.

### ch16-quiz-01-v1
- **Kind:** AI-written version of ch16-quiz-01
- **Concepts:** Effect size vs significance
- **Type:** matching
- **Question:**

Two field studies each found that a nest-box treatment raised fledgling mass by 3 g (null value μ₀ = 0).

Study | n | SD (g)
P | 900 | 30
Q | 9 | 3

Equations: SE = s / √n, t = (x̄ - μ₀) / SE, d = (x̄ - μ₀) / s

Match each study to its Cohen's d:

1. Study P
2. Study Q

- **Options:**

  A) d = 1
  B) d = 0.1
  C) d = 3
  D) d = 10

- **Answer (tutor only):** 1-B, 2-A
- **Explanation (tutor only):** d = difference / SD. P: 3 / 30 = 0.1. Q: 3 / 3 = 1.
- **Why the wrong options are wrong (tutor only):**
  Divide by the SD, not the SE.
- **Hint:** d = difference ÷ SD.

### ch16-quiz-01-v2
- **Kind:** AI-written version of ch16-quiz-01
- **Concepts:** Effect size vs significance
- **Type:** matching
- **Question:**

Two clinical studies each found that a drug lowers blood pressure by 2 mmHg (null value μ₀ = 0).

Study | n | SD (mmHg)
X | 10,000 | 20
Y | 10 | 2

Equations: SE = s / √n, t = (x̄ - μ₀) / SE, d = (x̄ - μ₀) / s

Match each study to its standard error:

1. Study X
2. Study Y

- **Options:**

  A) SE = 0.63
  B) SE = 0.2
  C) SE = 2
  D) SE = 20

- **Answer (tutor only):** 1-B, 2-A
- **Explanation (tutor only):** X: 20 / √10,000 = 20 / 100 = 0.2. Y: 2 / √10 = 0.63.
- **Why the wrong options are wrong (tutor only):**
  SE = SD / √n.
- **Hint:** SD ÷ √n.

### ch16-quiz-02
- **Kind:** Course original
- **Concepts:** Effect size vs significance
- **Type:** matching
- **Question:**

Two clinical studies each found that a drug lowers blood pressure by 2 mmHg (null value μ₀ = 0).

Study | n | SD (mmHg)
X | 10,000 | 20
Y | 10 | 2

Equations: SE = s / √n, t = (x̄ - μ₀) / SE, d = (x̄ - μ₀) / s

Match each study to its t value:

1. Study X
2. Study Y

- **Options:**

  A) t = 3.16
  B) t = 1
  C) t = 10
  D) t = 0.1

- **Answer (tutor only):** 1-C, 2-A
- **Explanation (tutor only):** Study X: SE = 20 / √10,000 = 0.2, so t = 2 / 0.2 = 10. Study Y: SE = 2 / √10 = 0.63, so t = 2 / 0.63 = 3.16.
- **Why the wrong options are wrong (tutor only):**
  D) and B) are Cohen's d values (difference / SD).
- **Hint:** First find each SE = SD / √n.

### ch16-quiz-02-v1
- **Kind:** AI-written version of ch16-quiz-02
- **Concepts:** Effect size vs significance
- **Type:** matching
- **Question:**

Two field studies each found that a nest-box treatment raised fledgling mass by 3 g (null value μ₀ = 0).

Study | n | SD (g)
P | 900 | 30
Q | 9 | 3

Equations: SE = s / √n, t = (x̄ - μ₀) / SE, d = (x̄ - μ₀) / s

Match each study to its t value:

1. Study P
2. Study Q

- **Options:**

  A) t = 0.1
  B) t = 9
  C) t = 1
  D) t = 3

- **Answer (tutor only):** 1-D, 2-D
- **Explanation (tutor only):** P: SE = 30 / √900 = 1, t = 3 / 1 = 3. Q: SE = 3 / √9 = 1, t = 3 / 1 = 3. Same t, very different effect sizes.
- **Why the wrong options are wrong (tutor only):**
  Find each SE first.
- **Hint:** SE = SD / √n, then t = difference / SE.

### ch16-quiz-02-v2
- **Kind:** AI-written version of ch16-quiz-02
- **Concepts:** Effect size vs significance
- **Type:** MC
- **Question:**

Two clinical studies each found that a drug lowers blood pressure by 2 mmHg (null value μ₀ = 0).

Study | n | SD (mmHg)
X | 10,000 | 20
Y | 10 | 2

Equations: SE = s / √n, t = (x̄ - μ₀) / SE, d = (x̄ - μ₀) / s

If Study Y had 40 people instead of 10 (same SD and difference), what would its t value be?

- **Options:**

  A) t = 6.32
  B) t = 1
  C) t = 3.16
  D) t = 12.6

- **Answer (tutor only):** A
- **Explanation (tutor only):** SE = 2 / √40 = 0.316; t = 2 / 0.316 = 6.32. Quadrupling n doubles t.
- **Why the wrong options are wrong (tutor only):**
  B) That's d.
  C) That's t with n = 10.
  D) That multiplies by 4 instead of √4.
- **Hint:** Quadrupling n halves the SE.

### ch16-quiz-03
- **Kind:** Course original
- **Concepts:** Effect size vs significance; Interpreting tests
- **Type:** MC
- **Question:**

Two clinical studies each found that a drug lowers blood pressure by 2 mmHg (null value μ₀ = 0).

Study | n | SD (mmHg)
X | 10,000 | 20
Y | 10 | 2

Equations: SE = s / √n, t = (x̄ - μ₀) / SE, d = (x̄ - μ₀) / s

Study X has t = 10 (d = 0.1); Study Y has t = 3.16 (d = 1). At α = 0.05, what do we do with H₀ in each study, and which has the smaller p-value?

- **Options:**

  A) Reject H₀ in both; Study X has the smaller p-value
  B) Reject H₀ in both; Study Y has the smaller p-value
  C) Reject H₀ only in Study Y; Study Y has the smaller p-value
  D) Reject H₀ only in Study X; Study X has the smaller p-value

- **Answer (tutor only):** A
- **Explanation (tutor only):** Both t values exceed their critical values (about 1.96 for X; 2.26 for Y with 9 df), so we reject in both. Study X's t is much larger, so its p-value is much smaller, even though its effect is tiny. Huge samples make tiny effects 'significant'.
- **Why the wrong options are wrong (tutor only):**
  B) Y has the bigger effect, but X has the bigger t (and smaller p) because of its huge sample.
  C) X's t of 10 is far beyond the critical value.
  D) Y's t of 3.16 also exceeds its critical value (2.26).
- **Hint:** Compare t values, not effect sizes, to decide about H₀.

### ch16-quiz-03-v1
- **Kind:** AI-written version of ch16-quiz-03
- **Concepts:** Effect size vs significance; Interpreting tests
- **Type:** MC
- **Question:**

Two field studies each found that a nest-box treatment raised fledgling mass by 3 g (null value μ₀ = 0).

Study | n | SD (g)
P | 900 | 30
Q | 9 | 3

Equations: SE = s / √n, t = (x̄ - μ₀) / SE, d = (x̄ - μ₀) / s

Both studies have t = 3, but Study P has d = 0.1 and Study Q has d = 1. Which statement is correct?

- **Options:**

  A) Same t, but Study Q shows a much larger effect
  B) Same t, so the effects are the same size
  C) Study P has the larger effect because it has more data
  D) Neither is significant because their t values are equal

- **Answer (tutor only):** A
- **Explanation (tutor only):** t mixes effect size and sample size. Q's effect is a full SD; P's is a tenth of an SD but detected thanks to its huge sample.
- **Why the wrong options are wrong (tutor only):**
  B) Equal t doesn't mean equal effects.
  C) Sample size doesn't change effect size.
  D) Equal t says nothing about non-significance.
- **Hint:** What does d measure that t doesn't?

### ch16-quiz-03-v2
- **Kind:** AI-written version of ch16-quiz-03
- **Concepts:** Effect size vs significance; Interpreting tests
- **Type:** MC
- **Question:**

Two clinical studies each found that a drug lowers blood pressure by 2 mmHg (null value μ₀ = 0).

Study | n | SD (mmHg)
X | 10,000 | 20
Y | 10 | 2

Equations: SE = s / √n, t = (x̄ - μ₀) / SE, d = (x̄ - μ₀) / s

Study X has a tiny effect (d = 0.1) but the smaller p-value. Why?

- **Options:**

  A) Its effect is actually larger than Study Y's effect
  B) p-values measure the size of an effect directly
  C) Its huge sample makes the SE tiny, so t is large
  D) Its large SD makes the difference more convincing

- **Answer (tutor only):** C
- **Explanation (tutor only):** SE = 20 / 100 = 0.2, so even a small difference is many SEs from zero.
- **Why the wrong options are wrong (tutor only):**
  A) d = 0.1 vs 1.
  B) p mixes effect size with sample size.
  D) A larger SD lowers t.
- **Hint:** What does n do to the SE?

### ch16-quiz-04
- **Kind:** Course original
- **Concepts:** Interpreting tests
- **Type:** MC
- **Question:**

Two clinical studies each found that a drug lowers blood pressure by 2 mmHg (null value μ₀ = 0).

Study | n | SD (mmHg)
X | 10,000 | 20
Y | 10 | 2

Equations: SE = s / √n, t = (x̄ - μ₀) / SE, d = (x̄ - μ₀) / s

Study X has the smaller p-value. Which study has the higher chance that the null hypothesis is false?

- **Options:**

  A) Study X, because its p-value is smaller
  B) Study Y, because its effect size is larger
  C) We can't tell from these numbers

- **Answer (tutor only):** C
- **Explanation (tutor only):** A p-value is the probability of data this extreme if the null were true. It isn't the probability that the null is false, so comparing p-values doesn't tell us which null is more likely to be false.
- **Why the wrong options are wrong (tutor only):**
  A) A smaller p-value isn't a higher probability that the null is false.
  B) A bigger effect size isn't either.
- **Hint:** What is a p-value the probability of?

### ch16-quiz-04-v1
- **Kind:** AI-written version of ch16-quiz-04
- **Concepts:** Interpreting tests
- **Type:** MC
- **Question:**

Two clinical studies each found that a drug lowers blood pressure by 2 mmHg (null value μ₀ = 0).

Study | n | SD (mmHg)
X | 10,000 | 20
Y | 10 | 2

Equations: SE = s / √n, t = (x̄ - μ₀) / SE, d = (x̄ - μ₀) / s

Which study has the larger effect of the drug on blood pressure, relative to individual variation?

- **Options:**

  A) Study X
  B) Study Y
  C) We can't tell from these numbers

- **Answer (tutor only):** B
- **Explanation (tutor only):** Effect size (d) is 1 for Y and 0.1 for X: relative to individual variation, Y's effect is ten times larger.
- **Why the wrong options are wrong (tutor only):**
  A) X has the smaller p-value, but the smaller d.
  C) We can calculate d from these numbers.
- **Hint:** Compare Cohen's d.

### ch16-quiz-04-v2
- **Kind:** AI-written version of ch16-quiz-04
- **Concepts:** Interpreting tests
- **Type:** MC
- **Question:**

Two field studies each found that a nest-box treatment raised fledgling mass by 3 g (null value μ₀ = 0).

Study | n | SD (g)
P | 900 | 30
Q | 9 | 3

Equations: SE = s / √n, t = (x̄ - μ₀) / SE, d = (x̄ - μ₀) / s

Both studies give the same p-value (t = 3). Which study's null hypothesis is more likely to be false?

- **Options:**

  A) Study P, because its sample is larger
  B) Study Q, because its effect is larger
  C) We can't tell from these p-values

- **Answer (tutor only):** C
- **Explanation (tutor only):** A p-value is the probability of data this extreme if the null were true, not the probability the null is false.
- **Why the wrong options are wrong (tutor only):**
  A) and B) p-values don't give the probability a hypothesis is true or false.
- **Hint:** What does a p-value condition on?

### ch16-quiz-05
- **Kind:** Course original
- **Concepts:** Confidence intervals
- **Type:** matching
- **Question:**

25 people had a mean body temperature of 98.52 °F, with a 95% CI of 98.24 to 98.80 °F. Mark each statement as OK or Wrong:

1. 95% of people have a body temperature between 98.24 and 98.80 °F.
2. If we repeated this study many times, about 95% of intervals built this way would contain the true mean.
3. 98.6 °F is inside the interval, so the true mean is 98.6 °F.
4. A 99% CI from the same data would be narrower.

- **Options:**

  A) Wrong
  B) OK

- **Answer (tutor only):** 1-A, 2-B, 3-A, 4-A
- **Explanation (tutor only):** 1) Wrong: the CI describes uncertainty in the mean, not where individual people fall (that's much wider).
2) OK: this is the correct interpretation of a 95% CI.
3) Wrong: 98.6 is plausible, but so is every other value in the interval.
4) Wrong: more confidence requires a wider interval.
- **Why the wrong options are wrong (tutor only):**
  The most common mistake is reading a CI as a range for individuals rather than for the mean.
- **Hint:** Is a CI about individuals or about the mean? What happens to the interval if you want more confidence?

### ch16-quiz-05-v1
- **Kind:** AI-written version of ch16-quiz-05
- **Concepts:** Confidence intervals
- **Type:** matching
- **Question:**

40 lizards had a mean sprint speed of 2.1 m/s, with a 95% CI of 1.9 to 2.3 m/s. Mark each statement as OK or Wrong:

1. If we repeated this study many times, about 95% of intervals built this way would contain the true mean.
2. 95% of lizards sprint between 1.9 and 2.3 m/s.
3. A 90% CI from the same data would be narrower.
4. With 160 lizards (and similar data), the 95% CI would be about half as wide.

- **Options:**

  A) Wrong
  B) OK

- **Answer (tutor only):** 1-B, 2-A, 3-B, 4-B
- **Explanation (tutor only):** 1) OK: correct interpretation. 2) Wrong: the CI is about the mean, not individuals. 3) OK: less confidence → narrower. 4) OK: 4× n halves the SE.
- **Why the wrong options are wrong (tutor only):**
  CIs describe uncertainty in the mean.
- **Hint:** Mean vs individuals; confidence vs width.

### ch16-quiz-05-v2
- **Kind:** AI-written version of ch16-quiz-05
- **Concepts:** Confidence intervals
- **Type:** matching
- **Question:**

25 people had a mean body temperature of 98.52 °F, with a 95% CI of 98.24 to 98.80 °F. Mark each statement as OK or Wrong:

1. Values outside the interval, like 98.0 °F, are implausible for the true mean.
2. The interval would be wider with only 10 people.
3. There is a 95% chance the sample mean is between 98.24 and 98.80 °F.
4. Most people's temperatures are between 98.24 and 98.80 °F.

- **Options:**

  A) Wrong
  B) OK

- **Answer (tutor only):** 1-B, 2-B, 3-A, 4-A
- **Explanation (tutor only):** 1) OK: values outside a 95% CI would be rejected at α = 0.05. 2) OK: smaller n → bigger SE. 3) Wrong: the sample mean (98.52) is known and is in the interval by construction. 4) Wrong: individuals vary much more than the mean.
- **Why the wrong options are wrong (tutor only):**
  The CI is about the population mean.
- **Hint:** What is the interval about?

## Chapter 17: F this!

### ch17-book-01
- **Kind:** Course original
- **Concepts:** F & the ANOVA table; Hypotheses & p-values
- **Type:** MC
- **Question:**

Under the null hypothesis that all groups come from the same population, the expected value of F is:

- **Options:**

  A) 0
  B) 1
  C) It depends on the degrees of freedom

- **Answer (tutor only):** B
- **Explanation (tutor only):** Under the null, MS model and MS error both estimate the same variance, so F ≈ 1.
- **Why the wrong options are wrong (tutor only):**
  A) Group means vary by chance even under the null.
  C) Its distribution depends on df, but it's centered near 1.
- **Hint:** F is a ratio of two estimates of what, under the null?

### ch17-book-01-v1
- **Kind:** AI-written version of ch17-book-01
- **Concepts:** F & the ANOVA table; Hypotheses & p-values
- **Type:** MC
- **Question:**

Five groups of plants are all drawn from the same population. An ANOVA is run many times on new samples. Around what value should the F statistics cluster?

- **Options:**

  A) 0
  B) 1.96
  C) 1
  D) 5

- **Answer (tutor only):** C
- **Explanation (tutor only):** Under the null, F ≈ 1, since both mean squares estimate the same variance.
- **Why the wrong options are wrong (tutor only):**
  A) F is about 1, not 0.
  B) That's a z critical value.
  D) Not the number of groups.
- **Hint:** Ratio of two estimates of the same variance.

### ch17-book-01-v2
- **Kind:** AI-written version of ch17-book-01
- **Concepts:** F & the ANOVA table; Hypotheses & p-values
- **Type:** MC
- **Question:**

If the null hypothesis of an ANOVA is FALSE, F tends to be:

- **Options:**

  A) Larger than 1
  B) Smaller than 1
  C) Negative
  D) Exactly 1

- **Answer (tutor only):** A
- **Explanation (tutor only):** Real differences add to MS model but not MS error, so F grows.
- **Why the wrong options are wrong (tutor only):**
  B) and D) Those are typical under the null.
  C) F can't be negative.
- **Hint:** What do real differences add to?

### ch17-book-02
- **Kind:** Course original
- **Concepts:** F & the ANOVA table
- **Type:** select-all
- **Question:**

If F is greater than its expected value under the null (about 1), then: (Select all that apply.)

- **Options:**

  A) The null is false
  B) The null is true
  C) We reject the null
  D) We fail to reject the null
  E) We may or may not reject the null, depending on the degrees of freedom

- **Answer (tutor only):** E
- **Explanation (tutor only):** An F a bit above 1 is common by chance. Whether F is big enough to reject depends on its critical value, which depends on the degrees of freedom.
- **Why the wrong options are wrong (tutor only):**
  A) and B) F alone never proves anything about the null.
  C) and D) It depends how much bigger than 1, and on the df.
- **Hint:** Is F = 1.2 significant? It depends on what?

### ch17-book-02-v1
- **Kind:** AI-written version of ch17-book-02
- **Concepts:** F & the ANOVA table
- **Type:** select-all
- **Question:**

An ANOVA gives F = 3.5 on 2 and 6 df (critical F = 5.14), and another gives F = 3.5 on 2 and 60 df (critical F = 3.15). Which reject the null at α = 0.05? (Select all that apply.)

- **Options:**

  A) The test with 2 and 6 df
  B) The test with 2 and 60 df
  C) Neither test rejects the null
  D) Both tests reject the null

- **Answer (tutor only):** B
- **Explanation (tutor only):** 3.5 < 5.14 (fail to reject) but 3.5 > 3.15 (reject). The same F can lead to different decisions depending on df.
- **Why the wrong options are wrong (tutor only):**
  A) 3.5 is below 5.14.
  C) and D) Only one rejects.
- **Hint:** Compare F with each critical value.

### ch17-book-02-v2
- **Kind:** AI-written version of ch17-book-02
- **Concepts:** F & the ANOVA table
- **Type:** select-all
- **Question:**

An ANOVA gives F = 1.3. Which of these could be true? (Select all that apply.)

- **Options:**

  A) The null hypothesis is true
  B) We reject the null at α = 0.05 for most df
  C) We fail to reject the null at α = 0.05 for most df
  D) The null hypothesis is false

- **Answer (tutor only):** A, C, D
- **Explanation (tutor only):** F = 1.3 is usually not significant, but the null might be true or false (we may lack power).
- **Why the wrong options are wrong (tutor only):**
  B) Critical F values are almost always above 1.3 (except with huge df for many groups).
- **Hint:** F near 1 is common under the null.

### ch17-book-03
- **Kind:** Course original
- **Concepts:** F & the ANOVA table
- **Type:** select-all
- **Question:**

If F is less than its expected value under the null (about 1), then: (Select all that apply.)

- **Options:**

  A) The null is false
  B) The null is true
  C) We reject the null
  D) We fail to reject the null
  E) We may or may not reject the null, depending on the degrees of freedom

- **Answer (tutor only):** D
- **Explanation (tutor only):** An F below 1 means groups differ less than we'd expect from chance alone, so it's never in the rejection region (the upper tail). We fail to reject.
- **Why the wrong options are wrong (tutor only):**
  B) Failing to reject doesn't prove the null true.
  E) Critical values are always above 1, so the df don't matter here.
- **Hint:** Where is the rejection region of an F test?

### ch17-book-03-v1
- **Kind:** AI-written version of ch17-book-03
- **Concepts:** F & the ANOVA table
- **Type:** select-all
- **Question:**

An ANOVA gives F = 0.4 with 3 and 40 df. Which of these is correct? (Select all that apply.)

- **Options:**

  A) The null hypothesis must be true
  B) The group means vary less than expected by chance
  C) We fail to reject the null hypothesis
  D) We reject the null hypothesis

- **Answer (tutor only):** B, C
- **Explanation (tutor only):** F < 1 means the group means are closer together than sampling error alone usually produces. We fail to reject, but that doesn't prove the null.
- **Why the wrong options are wrong (tutor only):**
  A) Failing to reject isn't proof.
  D) Small F is never in the rejection region.
- **Hint:** Where is the rejection region?

### ch17-book-03-v2
- **Kind:** AI-written version of ch17-book-03
- **Concepts:** F & the ANOVA table
- **Type:** select-all
- **Question:**

Can an F statistic below 1 ever lead to rejecting the null at α = 0.05? (Select all that apply.)

- **Options:**

  A) No: F below 1 means less variation among means than expected
  B) Yes: with enough degrees of freedom
  C) No: we only reject for large F (upper tail)
  D) Yes: if the groups are very unequal in size

- **Answer (tutor only):** A, C
- **Explanation (tutor only):** Critical F values are always above 1, and small F values reflect less between-group variation than expected by chance.
- **Why the wrong options are wrong (tutor only):**
  B) and D) Critical F stays above 1.
- **Hint:** Where is the rejection region?

### ch17-book-04
- **Kind:** Course original
- **Concepts:** Hypotheses & p-values
- **Type:** select-all
- **Question:**

We used an ANOVA to test whether pink and white parviflora flowers at Squirrel Mountain have the same admixture proportion (the share of their genome from the sister subspecies xantiana). The p-value was very small (much less than 0.05). This means: (Select all that apply.)

- **Options:**

  A) Such an extreme F would be unlikely if the null were true
  B) Pollinators avoid visiting white-flowered parviflora plants
  C) The pink petal color has introgressed from xantiana

- **Answer (tutor only):** A
- **Explanation (tutor only):** A small p-value tells us the data would be surprising under the null. It doesn't identify a biological cause; B and C are possible explanations that the test can't distinguish.
- **Why the wrong options are wrong (tutor only):**
  B) and C) These are biological hypotheses; an association alone doesn't show either one.
- **Hint:** What does a p-value tell you, and what doesn't it?

### ch17-book-04-v1
- **Kind:** AI-written version of ch17-book-04
- **Concepts:** Hypotheses & p-values
- **Type:** select-all
- **Question:**

We used an ANOVA to test whether pink and white parviflora flowers at Squirrel Mountain have the same admixture proportion (the share of their genome from the sister subspecies xantiana). The p-value was 0.40. This means: (Select all that apply.)

- **Options:**

  A) Data like ours would be common if the null hypothesis were true
  B) Petal color has no relationship with admixture
  C) There's a 40% chance pink and white flowers have equal admixture

- **Answer (tutor only):** A
- **Explanation (tutor only):** p = 0.40 means data this extreme are common under the null. It doesn't prove there's no relationship, and it isn't the probability the null is true.
- **Why the wrong options are wrong (tutor only):**
  B) Failing to reject isn't proof of no effect.
  C) p isn't P(null).
- **Hint:** p assumes the null.

### ch17-book-04-v2
- **Kind:** AI-written version of ch17-book-04
- **Concepts:** Hypotheses & p-values
- **Type:** select-all
- **Question:**

An ANOVA finds that pink parviflora plants have significantly higher admixture (more genome from xantiana) than white ones (p < 0.001). Which explanations does this result make unlikely? (Select all that apply.)

- **Options:**

  A) The difference is due to sampling error alone
  B) Pollinators carry xantiana pollen to pink flowers
  C) Pink color itself was introgressed from xantiana

- **Answer (tutor only):** A
- **Explanation (tutor only):** A small p makes chance an unlikely explanation (though not impossible). It can't tell apart the biological explanations B and C.
- **Why the wrong options are wrong (tutor only):**
  C) and B) are both consistent with the result; the test doesn't distinguish them.
- **Hint:** What does a p-value address?

### ch17-book-05
- **Kind:** Course original
- **Concepts:** Sums of squares & deviations
- **Type:** matching
- **Question:**

Consider this code:

SS <- data |>
  mutate(grand_mean = mean(response)) |>
  group_by(explanatory) |>
  mutate(yhat = mean(response)) |>
  ungroup() |>
  summarise(SS_A = sum((yhat - grand_mean)^2),
            SS_B = sum((response - yhat)^2),
            SS_C = sum((response - grand_mean)^2))

Match each sum of squares to the label that calculates it:

1. SS error
2. SS model
3. SS total

- **Options:**

  A) SS_B
  B) SS_C
  C) SS_A

- **Answer (tutor only):** 1-A, 2-C, 3-B
- **Explanation (tutor only):** SS_A: group means vs grand mean (model). SS_B: observations vs group means (error). SS_C: observations vs grand mean (total).
- **Why the wrong options are wrong (tutor only):**
  Common mix-up between SS_A and SS_C: one starts from yhat, the other from the response.
- **Hint:** yhat is each observation's group mean.

### ch17-book-05-v1
- **Kind:** AI-written version of ch17-book-05
- **Concepts:** Sums of squares & deviations
- **Type:** MC
- **Question:**

Consider this code:

data |>
  mutate(gm = mean(y)) |>
  group_by(trt) |>
  mutate(trt_mean = mean(y)) |>
  ungroup() |>
  summarise(X = sum((y - gm)^2),
            Y = sum((y - trt_mean)^2),
            Z = sum((trt_mean - gm)^2))

Which equation must be true?

- **Options:**

  A) X = Y + Z
  B) X = Y × Z
  C) Y = X + Z
  D) Z = X + Y

- **Answer (tutor only):** A
- **Explanation (tutor only):** X is SS total, Y is SS error and Z is SS model, and SS total = SS error + SS model.
- **Why the wrong options are wrong (tutor only):**
  Identify which is total first.
- **Hint:** Which one is SS total?

### ch17-book-05-v2
- **Kind:** AI-written version of ch17-book-05
- **Concepts:** Sums of squares & deviations
- **Type:** MC
- **Question:**

In R, the code

summarise(SS = sum((y - mean(y))^2))

run on ungrouped data calculates which sum of squares?

- **Options:**

  A) SS total
  B) SS model
  C) SS error
  D) None of these

- **Answer (tutor only):** A
- **Explanation (tutor only):** Each observation minus the grand mean, squared and summed: SS total.
- **Why the wrong options are wrong (tutor only):**
  B) Model uses group means.
  C) Error uses group means.
- **Hint:** No grouping, so mean(y) is the grand mean.

### ch17-book-06
- **Kind:** Course original
- **Concepts:** Sums of squares & deviations
- **Type:** numeric
- **Question:**

At Site 22, the mean admixture proportion of pink-flowered parviflora plants is 0.0330 and of white-flowered plants is 0.0132. What is the difference (pink minus white)?

- **Answer (tutor only):** 0.0199
- **Explanation (tutor only):** 0.0330 - 0.0132 = 0.0199 (0.0198 with these rounded means).
- **Why the wrong options are wrong (tutor only):**
  Common mistake: white minus pink (negative).
- **Hint:** Pink minus white.

### ch17-book-06-v1
- **Kind:** AI-written version of ch17-book-06
- **Concepts:** Sums of squares & deviations
- **Type:** numeric
- **Question:**

At Site 22, the mean admixture proportion of pink-flowered parviflora plants is 0.0330. A pink-flowered plant has an admixture proportion of 0.0410. What is this plant's error (residual) deviation?

- **Answer (tutor only):** 0.008
- **Explanation (tutor only):** Observation minus its group mean: 0.0410 - 0.0330 = 0.0080.
- **Hint:** Observation minus group mean.

### ch17-book-06-v2
- **Kind:** AI-written version of ch17-book-06
- **Concepts:** Sums of squares & deviations
- **Type:** numeric
- **Question:**

At Site 22, a white-flowered parviflora plant has an admixture proportion of 0.0250, and the white group mean is 0.0132. What is this plant's error (residual) deviation?

- **Answer (tutor only):** 0.0118
- **Explanation (tutor only):** Observation minus its group mean: 0.0250 - 0.0132 = 0.0118.
- **Hint:** Observation minus group mean.

### ch17-book-07
- **Kind:** Course original
- **Concepts:** Sums of squares & deviations
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch17-book-deviations.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch17-book-deviations.png)
- **Question:**

The plots show admixture proportions of individual pink and white parviflora plants at Site 22, the grand mean (black line) and the group means (dashed lines). Match each kind of deviation to the plot that shows it:

1. Error deviations
2. Model deviations
3. Total deviations

- **Options:**

  A) Plot B
  B) Plot C
  C) Plot A

- **Answer (tutor only):** 1-C, 2-B, 3-A
- **Explanation (tutor only):** A: points to their group mean (error). B: points to the grand mean (total). C: group means to the grand mean (model).
- **Why the wrong options are wrong (tutor only):**
  Check where each line starts and ends.
- **Hint:** Which plot's lines never touch the points?

### ch17-book-07-v1
- **Kind:** AI-written version of ch17-book-07
- **Concepts:** Sums of squares & deviations
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch17-book-deviations.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch17-book-deviations.png)
- **Question:**

The plots show admixture proportions of individual pink and white parviflora plants at Site 22, the grand mean (black line) and the group means (dashed lines). Which plot's deviations, squared and summed, give the sum of squares used in the numerator of F (before dividing by df)?

- **Options:**

  A) Plot A
  B) Plot B
  C) Plot C

- **Answer (tutor only):** C
- **Explanation (tutor only):** F's numerator is MS model, from SS model: group means to the grand mean (Plot C).
- **Why the wrong options are wrong (tutor only):**
  A) Error (denominator).
  B) Total.
- **Hint:** F = MS model / MS error.

### ch17-book-07-v2
- **Kind:** AI-written version of ch17-book-07
- **Concepts:** Sums of squares & deviations
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch17-book-deviations.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch17-book-deviations.png)
- **Question:**

The plots show admixture proportions of individual pink and white parviflora plants at Site 22, the grand mean (black line) and the group means (dashed lines). If petal color explained nothing (both group means equal the grand mean), which plot's lines would all have length zero?

- **Options:**

  A) Plot C
  B) Plot A
  C) Plot B

- **Answer (tutor only):** A
- **Explanation (tutor only):** Model deviations are group mean minus grand mean, so they vanish when the group means equal the grand mean.
- **Why the wrong options are wrong (tutor only):**
  B) Points still vary around their group means.
  C) Points still vary around the grand mean.
- **Hint:** Which lines connect group means to the grand mean?

### ch17-book-08
- **Kind:** Course original
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

To ask whether pink flowers carry more genes from the sister subspecies xantiana, we compared the admixture proportion (the share of the genome from xantiana) of pink- and white-flowered parviflora plants at Site 22:

lm(admix_proportion ~ petal_color, data = clarkia_s22_hz) |> anova()

            Df    Sum Sq    Mean Sq F value   Pr(>F)
petal_color  1 0.0025843 0.00258430  8.1871 0.008049
Residuals   27 0.0085224 0.00031564

What do we do with the null hypothesis, and what does that mean?

- **Options:**

  A) Reject it; the null is false
  B) Reject it; we can't say for sure whether the null is true
  C) Fail to reject it; the null is true
  D) Reject it; the null has a 0.008 chance of being true

- **Answer (tutor only):** B
- **Explanation (tutor only):** p = 0.008 < 0.05, so we reject. But rejecting doesn't prove the null false, and p isn't the probability the null is true.
- **Why the wrong options are wrong (tutor only):**
  A) Rejecting isn't proof.
  C) p is below α.
  D) p is not the probability the null is true.
- **Hint:** Compare p with α, then think about what p does and doesn't mean.

### ch17-book-08-v1
- **Kind:** AI-written version of ch17-book-08
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

To ask whether pink flowers carry more genes from the sister subspecies xantiana, we compared the admixture proportion (the share of the genome from xantiana) of pink- and white-flowered parviflora plants at Site 22:

lm(admix_proportion ~ petal_color, data = clarkia_s22_hz) |> anova()

            Df    Sum Sq    Mean Sq F value   Pr(>F)
petal_color  1 0.0025843 0.00258430  8.1871 0.008049
Residuals   27 0.0085224 0.00031564

What would we conclude at α = 0.01?

- **Options:**

  A) Reject the null, because p < 0.01
  B) Fail to reject, because p > 0.01
  C) Reject, and the null is proven false
  D) It depends on R², not on the p-value

- **Answer (tutor only):** A
- **Explanation (tutor only):** p = 0.008 < 0.01, so we reject even at this stricter level (without proving anything).
- **Why the wrong options are wrong (tutor only):**
  B) 0.008 < 0.01.
  C) Rejection isn't proof.
  D) The decision uses p and α.
- **Hint:** Compare 0.008 with 0.01.

### ch17-book-08-v2
- **Kind:** AI-written version of ch17-book-08
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

To ask whether pink flowers carry more genes from the sister subspecies xantiana, we compared the admixture proportion (the share of the genome from xantiana) of pink- and white-flowered parviflora plants at Site 22:

lm(admix_proportion ~ petal_color, data = clarkia_s22_hz) |> anova()

            Df    Sum Sq    Mean Sq F value   Pr(>F)
petal_color  1 0.0025843 0.00258430  8.1871 0.008049
Residuals   27 0.0085224 0.00031564

What is the mean square error (the pooled variance)?

- **Options:**

  A) 0.0085224
  B) 8.1871
  C) 0.0025843
  D) 0.00031564

- **Answer (tutor only):** D
- **Explanation (tutor only):** MS error = 0.0085224 / 27 = 0.00031564.
- **Why the wrong options are wrong (tutor only):**
  A) That's SS error.
  B) That's F.
  C) That's SS model (and MS model).
- **Hint:** SS error / df error.

### ch17-book-09
- **Kind:** Course original
- **Concepts:** Effect size & R²
- **Type:** numeric
- **Question:**

To ask whether pink flowers carry more genes from the sister subspecies xantiana, we compared the admixture proportion (the share of the genome from xantiana) of pink- and white-flowered parviflora plants at Site 22:

lm(admix_proportion ~ petal_color, data = clarkia_s22_hz) |> anova()

            Df    Sum Sq    Mean Sq F value   Pr(>F)
petal_color  1 0.0025843 0.00258430  8.1871 0.008049
Residuals   27 0.0085224 0.00031564

What is R² for this model?

- **Answer (tutor only):** 0.233
- **Explanation (tutor only):** R² = SS model / SS total = 0.0025843 / (0.0025843 + 0.0085224) = 0.0025843 / 0.0111067 = 0.233. Petal color explains about 23% of the variation in admixture proportion at this site.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: SS model / SS error (0.30).
- **Hint:** SS total = SS model + SS error.

### ch17-book-09-v1
- **Kind:** AI-written version of ch17-book-09
- **Concepts:** Effect size & R²
- **Type:** numeric
- **Question:**

To ask whether pink flowers carry more genes from the sister subspecies xantiana, we compared the admixture proportion (the share of the genome from xantiana) of pink- and white-flowered parviflora plants at Site 22:

lm(admix_proportion ~ petal_color, data = clarkia_s22_hz) |> anova()

            Df    Sum Sq    Mean Sq F value   Pr(>F)
petal_color  1 0.0025843 0.00258430  8.1871 0.008049
Residuals   27 0.0085224 0.00031564

What proportion of the variation in admixture proportion is NOT explained by petal color?

- **Answer (tutor only):** 0.767
- **Explanation (tutor only):** SS error / SS total = 0.0085224 / 0.0111067 = 0.767 (1 - R²).
- **Hint:** SS error / SS total.

### ch17-book-09-v2
- **Kind:** AI-written version of ch17-book-09
- **Concepts:** Effect size & R²
- **Type:** numeric
- **Question:**

To ask whether pink flowers carry more genes from the sister subspecies xantiana, we compared the admixture proportion (the share of the genome from xantiana) of pink- and white-flowered parviflora plants at Site 22:

lm(admix_proportion ~ petal_color, data = clarkia_s22_hz) |> anova()

            Df    Sum Sq    Mean Sq F value   Pr(>F)
petal_color  1 0.0025843 0.00258430  8.1871 0.008049
Residuals   27 0.0085224 0.00031564

How many plants were in this study?

- **Answer (tutor only):** 29
- **Explanation (tutor only):** df total = 1 + 27 = 28 = n - 1, so n = 29.
- **Hint:** Total df = n - 1.

### ch17-book-10
- **Kind:** Course original
- **Concepts:** Effect size & R²
- **Type:** MC
- **Question:**

To ask whether pink flowers carry more genes from the sister subspecies xantiana, we compared the admixture proportion (the share of the genome from xantiana) of pink- and white-flowered parviflora plants at Site 22:

lm(admix_proportion ~ petal_color, data = clarkia_s22_hz) |> anova()

            Df    Sum Sq    Mean Sq F value   Pr(>F)
petal_color  1 0.0025843 0.00258430  8.1871 0.008049
Residuals   27 0.0085224 0.00031564

The difference in mean admixture proportion (pink minus white) is 0.0199. How big is the effect (Cohen's d)?

- **Options:**

  A) Not worth reporting (< 0.01)
  B) Tiny (0.01 to 0.20)
  C) Small (0.20 to 0.50)
  D) Medium (0.50 to 0.80)
  E) Large (0.80 to 1.20)
  F) Very large (1.20 to 2.00)
  G) Huge (> 2.00)

- **Answer (tutor only):** E
- **Explanation (tutor only):** With two groups, MS error is the pooled variance: pooled SD = √0.00031564 = 0.0178. d = 0.0199 / 0.0178 = 1.12, a large effect.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: dividing by the mean square itself (gives about 63) or by the SE.
- **Hint:** Which entry in the table is the pooled variance? Take its square root.

### ch17-book-10-v1
- **Kind:** AI-written version of ch17-book-10
- **Concepts:** Effect size & R²
- **Type:** MC
- **Question:**

To ask whether pink flowers carry more genes from the sister subspecies xantiana, we compared the admixture proportion (the share of the genome from xantiana) of pink- and white-flowered parviflora plants at Site 22:

lm(admix_proportion ~ petal_color, data = clarkia_s22_hz) |> anova()

            Df    Sum Sq    Mean Sq F value   Pr(>F)
petal_color  1 0.0025843 0.00258430  8.1871 0.008049
Residuals   27 0.0085224 0.00031564

The pooled SD is 0.0178. If the difference in means had been 0.0089 instead of 0.0199, how big would the effect be?

- **Options:**

  A) Small (0.20 to 0.50)
  B) Medium (0.50 to 0.80)
  C) Large (0.80 to 1.20)
  D) Huge (> 2.00)

- **Answer (tutor only):** B
- **Explanation (tutor only):** d = 0.0089 / 0.0178 = 0.5, medium (at the boundary).
- **Why the wrong options are wrong (tutor only):**
  A) 0.5 is at the medium boundary.
  C) and D) Too large.
- **Hint:** Difference ÷ pooled SD.

### ch17-book-10-v2
- **Kind:** AI-written version of ch17-book-10
- **Concepts:** Effect size & R²
- **Type:** MC
- **Question:**

To ask whether pink flowers carry more genes from the sister subspecies xantiana, we compared the admixture proportion (the share of the genome from xantiana) of pink- and white-flowered parviflora plants at Site 22:

lm(admix_proportion ~ petal_color, data = clarkia_s22_hz) |> anova()

            Df    Sum Sq    Mean Sq F value   Pr(>F)
petal_color  1 0.0025843 0.00258430  8.1871 0.008049
Residuals   27 0.0085224 0.00031564

To get Cohen's d, we divide the difference in means (0.0199) by:

- **Options:**

  A) √0.00031564, the pooled SD
  B) 0.00031564, the mean square error
  C) √8.1871, the square root of F
  D) 0.0085224, the sum of squares error

- **Answer (tutor only):** A
- **Explanation (tutor only):** d = 0.0199 / 0.0178 = 1.12. The pooled SD is the square root of MS error.
- **Why the wrong options are wrong (tutor only):**
  B) That's a variance.
  C) √F = |t|, not an SD.
  D) Not divided by df.
- **Hint:** Effect size uses an SD.

### ch17-chimein-01
- **Kind:** Course original
- **Concepts:** SD vs SE
- **Type:** matching
- **Question:**

Match each quantity to what it describes:

1. Standard error (SE)
2. Standard deviation (SD)

- **Options:**

  A) Variability: how much individuals in the sample differ
  B) Uncertainty: variability in an estimate across repeated samples

- **Answer (tutor only):** 1-B, 2-A
- **Explanation (tutor only):** Both measure spread, but of different things. The SD describes spread among individuals; the SE describes spread of an estimate (like a mean) across hypothetical repeated samples.
- **Why the wrong options are wrong (tutor only):**
  Common mix-up: they're both 'variability', but the SE is the variability of an estimate, which is what we mean by uncertainty.
- **Hint:** Which one shrinks as you collect more data?

### ch17-chimein-01-v1
- **Kind:** AI-written version of ch17-chimein-01
- **Concepts:** SD vs SE
- **Type:** matching
- **Question:**

Match each scenario to the quantity it describes:

1. How much the mean height of 20 seedlings would vary if we repeated the experiment
2. How much the heights of the 20 seedlings vary from one another

- **Options:**

  A) Standard deviation
  B) Standard error

- **Answer (tutor only):** 1-B, 2-A
- **Explanation (tutor only):** Variation of an estimate across samples is the SE; variation among individuals is the SD.
- **Why the wrong options are wrong (tutor only):**
  Estimates vs individuals.
- **Hint:** Is it about the mean or the plants?

### ch17-chimein-01-v2
- **Kind:** AI-written version of ch17-chimein-01
- **Concepts:** SD vs SE
- **Type:** matching
- **Question:**

Match each quantity to how it changes as sample size increases:

1. Standard error
2. Standard deviation

- **Options:**

  A) Stays about the same, since individuals vary just as much
  B) Shrinks, since estimates get more precise

- **Answer (tutor only):** 1-B, 2-A
- **Explanation (tutor only):** SE = SD / √n shrinks with n. The SD estimates population variability, which doesn't depend on n.
- **Why the wrong options are wrong (tutor only):**
  Uncertainty shrinks; variability doesn't.
- **Hint:** Which one has √n in it?

### ch17-chimein-02
- **Kind:** Course original
- **Concepts:** Sums of squares & deviations
- **Type:** matching
- **Question:**

Imagine drawing vertical lines on a plot of data from several groups, then squaring the length of every line and summing them. Which sum of squares would we get for each kind of line?

1. Lines connecting each observation to its group mean
2. Lines connecting each group mean to the grand mean (one per data point)
3. Lines connecting each observation to the grand mean

- **Options:**

  A) Model (aka group)
  B) Error (aka residual)
  C) Total

- **Answer (tutor only):** 1-B, 2-A, 3-C
- **Explanation (tutor only):** Observation to group mean: error. Group mean to grand mean: model. Observation to grand mean: total. And SS total = SS model + SS error.
- **Why the wrong options are wrong (tutor only):**
  Common mix-up: model vs total.
- **Hint:** Which deviations would be zero if every observation equaled its group mean?

### ch17-chimein-02-v1
- **Kind:** AI-written version of ch17-chimein-02
- **Concepts:** Sums of squares & deviations
- **Type:** matching
- **Question:**

In an ANOVA, which sum of squares measures:

1. Variation among individuals within the same group
2. Variation among the group means
3. All the variation in the response

- **Options:**

  A) Model (aka group)
  B) Total
  C) Error (aka residual)

- **Answer (tutor only):** 1-C, 2-A, 3-B
- **Explanation (tutor only):** Within-group variation is error; between-group variation is model; all of it is total.
- **Why the wrong options are wrong (tutor only):**
  SS total = SS model + SS error.
- **Hint:** Within vs between.

### ch17-chimein-02-v2
- **Kind:** AI-written version of ch17-chimein-02
- **Concepts:** Sums of squares & deviations
- **Type:** matching
- **Question:**

An ANOVA has SS model = 30 and SS error = 70. Match each quantity to its value:

1. SS total
2. R²
3. The share of variation left unexplained

- **Options:**

  A) 100
  B) 0.7
  C) 0.3

- **Answer (tutor only):** 1-A, 2-C, 3-B
- **Explanation (tutor only):** SS total = 30 + 70 = 100. R² = 30 / 100 = 0.3. Unexplained = 70 / 100 = 0.7.
- **Why the wrong options are wrong (tutor only):**
  SS total = SS model + SS error.
- **Hint:** Add first, then divide.

### ch17-chimein-03
- **Kind:** Course original
- **Concepts:** F & the ANOVA table; Hypotheses & p-values
- **Type:** MC
- **Question:**

What is the expected value of F under the null hypothesis?

- **Options:**

  A) 0
  B) 1
  C) 1.96
  D) It depends

- **Answer (tutor only):** B
- **Explanation (tutor only):** Under the null, the mean square for groups and the mean square error both estimate the same variance (sampling error), so their ratio is about 1.
- **Why the wrong options are wrong (tutor only):**
  A) Even with no true differences, group means vary by chance, so MS model isn't zero.
  C) 1.96 is a critical value for z.
  D) Its exact distribution depends on the df, but its expectation is about 1.
- **Hint:** Under the null, what do MS model and MS error both estimate?

### ch17-chimein-03-v1
- **Kind:** AI-written version of ch17-chimein-03
- **Concepts:** F & the ANOVA table; Hypotheses & p-values
- **Type:** MC
- **Question:**

An ANOVA gives F = 0.95. What does this suggest?

- **Options:**

  A) The groups differ much more than chance predicts
  B) The groups differ about as much as chance predicts
  C) The ANOVA must have been calculated incorrectly
  D) The group means are all exactly equal

- **Answer (tutor only):** B
- **Explanation (tutor only):** Under the null F ≈ 1, so 0.95 is just what we'd expect from sampling error alone.
- **Why the wrong options are wrong (tutor only):**
  A) That would give a large F.
  C) F near 1 is common.
  D) Sample means are never exactly equal.
- **Hint:** What is F's expected value under the null?

### ch17-chimein-03-v2
- **Kind:** AI-written version of ch17-chimein-03
- **Concepts:** F & the ANOVA table; Hypotheses & p-values
- **Type:** MC
- **Question:**

Under the null hypothesis, why is F expected to be about 1?

- **Options:**

  A) F is defined so that it can never be greater than 1
  B) MS model and MS error both estimate the same variance
  C) The sum of squares model is always zero under the null
  D) The group means are always exactly equal under the null

- **Answer (tutor only):** B
- **Explanation (tutor only):** If all groups share one mean, between-group variation reflects only sampling error, just like within-group variation, so their ratio is about 1.
- **Why the wrong options are wrong (tutor only):**
  A) F can be large.
  D) and C) Sample means differ by chance, so SS model isn't zero.
- **Hint:** What does each mean square estimate under the null?

### ch17-chimein-04
- **Kind:** Course original
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

The alternative hypothesis for an ANOVA is:

- **Options:**

  A) All means differ
  B) Not all means differ
  C) Not all means are equal

- **Answer (tutor only):** C
- **Explanation (tutor only):** The null is that all groups have the same mean. The alternative is that at least one differs, i.e. not all means are equal.
- **Why the wrong options are wrong (tutor only):**
  A) Too strong: just one group differing makes the null false.
  B) Says something different: 'not all differ' allows all to be equal.
- **Hint:** What's the opposite of 'all means are equal'?

### ch17-chimein-04-v1
- **Kind:** AI-written version of ch17-chimein-04
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

The null hypothesis for an ANOVA comparing four diets is:

- **Options:**

  A) All four diets have the same population mean
  B) At least one diet has a different population mean
  C) All four diets have different population means
  D) The sample means of the four diets are equal

- **Answer (tutor only):** A
- **Explanation (tutor only):** H₀: μ₁ = μ₂ = μ₃ = μ₄.
- **Why the wrong options are wrong (tutor only):**
  B) That's the alternative.
  C) Too strong for either.
  D) Hypotheses are about populations.
- **Hint:** No difference at all.

### ch17-chimein-04-v2
- **Kind:** AI-written version of ch17-chimein-04
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

An ANOVA comparing three fertilizers rejects the null. What can we conclude?

- **Options:**

  A) At least one fertilizer's mean differs from another's
  B) All three fertilizers have different means
  C) The first fertilizer differs from the other two
  D) The fertilizer with the highest mean is best

- **Answer (tutor only):** A
- **Explanation (tutor only):** Rejecting H₀ means not all means are equal. Which ones differ needs post-hoc comparisons.
- **Why the wrong options are wrong (tutor only):**
  B) and C) The ANOVA doesn't say which differ.
  D) That's not what the test tells us.
- **Hint:** What's the alternative hypothesis?

### ch17-chimein-05
- **Kind:** Course original
- **Concepts:** F & the ANOVA table
- **Type:** MC
- **Question:**

When conducting an ANOVA we look only at the upper tail of the F distribution. Why is that fine, even though we usually do two-tailed tests?

- **Options:**

  A) It isn't fine: we should double the ANOVA p-value, as for a two-tailed t-test
  B) ANOVA is an exception: with three or more groups, one-tailed tests are allowed
  C) Because the upper tail of F already covers differences in both directions
  D) Because we already know which group should have the larger mean

- **Answer (tutor only):** C
- **Explanation (tutor only):** F is built from squared deviations, so a group mean far above or far below the others both make F bigger. Any kind of difference among means pushes F into the upper tail.
- **Why the wrong options are wrong (tutor only):**
  A) Doubling would be wrong: small F values aren't evidence of differences.
  B) It's not an exception; it's how F is built.
  D) ANOVA doesn't specify a direction.
- **Hint:** What happens to a squared deviation when a mean is unusually low?

### ch17-chimein-05-v1
- **Kind:** AI-written version of ch17-chimein-05
- **Concepts:** F & the ANOVA table
- **Type:** MC
- **Question:**

An ANOVA compares three groups. One group's mean is much LOWER than the other two. What happens to F?

- **Options:**

  A) F gets smaller, possibly falling below 1
  B) F doesn't change, since F ignores direction
  C) F gets larger, just as if the mean were much higher
  D) F becomes negative, in the lower tail

- **Answer (tutor only):** C
- **Explanation (tutor only):** F is built from squared deviations, so a mean far below the others increases SS model just as one far above does.
- **Why the wrong options are wrong (tutor only):**
  A) and D) Squaring removes direction; F can't be negative.
  B) F ignores direction but still grows.
- **Hint:** What does squaring do to a negative deviation?

### ch17-chimein-05-v2
- **Kind:** AI-written version of ch17-chimein-05
- **Concepts:** F & the ANOVA table
- **Type:** MC
- **Question:**

Why don't we double the p-value from an ANOVA's F test, the way we'd account for two tails in a t-test?

- **Options:**

  A) We should double it, but software forgets
  B) F tests are always one-sided by assumption
  C) Large F covers differences in any direction
  D) ANOVAs always use a smaller α of 0.025

- **Answer (tutor only):** C
- **Explanation (tutor only):** Because F uses squared deviations, any difference among means pushes F into the upper tail. Small F isn't evidence against the null.
- **Why the wrong options are wrong (tutor only):**
  A) Doubling would be wrong.
  B) It's not an assumption; it's how F is built.
  D) α is unchanged.
- **Hint:** What does a small F mean?

### ch17-chimein-06
- **Kind:** Course original
- **Concepts:** F & the ANOVA table
- **Type:** numeric
- **Question:**

Pretend we have 2 groups and 23 samples, with SS groups = 7 and SS error = 10. What is F?

- **Answer (tutor only):** 14.7
- **Explanation (tutor only):** df groups = 2 - 1 = 1; df error = 23 - 2 = 21. MS groups = 7 / 1 = 7; MS error = 10 / 21 = 0.476. F = 7 / 0.476 = 14.7.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: F = SS groups / SS error (0.7), skipping the degrees of freedom.
- **Hint:** Turn each sum of squares into a mean square first.

### ch17-chimein-06-v1
- **Kind:** AI-written version of ch17-chimein-06
- **Concepts:** F & the ANOVA table
- **Type:** numeric
- **Question:**

Pretend we have 3 groups and 33 samples, with SS groups = 8 and SS error = 60. What is F?

- **Answer (tutor only):** 2
- **Explanation (tutor only):** df groups = 3 - 1 = 2; df error = 33 - 3 = 30. MS groups = 8 / 2 = 4; MS error = 60 / 30 = 2. F = 4 / 2 = 2.
- **Hint:** Find the df, then the mean squares.

### ch17-chimein-06-v2
- **Kind:** AI-written version of ch17-chimein-06
- **Concepts:** F & the ANOVA table
- **Type:** numeric
- **Question:**

Pretend we have 4 groups and 24 samples, with SS groups = 15 and SS error = 40. What is F?

- **Answer (tutor only):** 2.5
- **Explanation (tutor only):** df groups = 4 - 1 = 3; df error = 24 - 4 = 20. MS groups = 15 / 3 = 5; MS error = 40 / 20 = 2. F = 5 / 2 = 2.5.
- **Hint:** Find the df, then the mean squares.

### ch17-chimein-07
- **Kind:** Course original
- **Concepts:** F & the ANOVA table; Hypotheses & p-values
- **Type:** MC
- **Question:**

Pretend we have 2 groups and 23 samples: F = 14.7 on 1 and 21 degrees of freedom. In R:

pf(14.7, df1 = 1, df2 = 21, lower.tail = FALSE)
[1] 0.00097

What do we conclude at α = 0.05?

- **Options:**

  A) The null is correct
  B) The alternative is correct
  C) We reject the null
  D) We fail to reject the null
  E) We accept the null

- **Answer (tutor only):** C
- **Explanation (tutor only):** F = 14.7 is far above its expected value of about 1, and p = 0.001 < 0.05, so we reject the null. (We still haven't proved the alternative.)
- **Why the wrong options are wrong (tutor only):**
  A) and E) p is tiny, and we never accept the null.
  B) Rejecting the null isn't proof of the alternative.
  D) p is far below α.
- **Hint:** Compare p with α.

### ch17-chimein-07-v1
- **Kind:** AI-written version of ch17-chimein-07
- **Concepts:** F & the ANOVA table; Hypotheses & p-values
- **Type:** MC
- **Question:**

Pretend we have 3 groups and 33 samples: F = 2.0 on 2 and 30 degrees of freedom. In R:

pf(2.0, df1 = 2, df2 = 30, lower.tail = FALSE)
[1] 0.153

What do we conclude at α = 0.05?

- **Options:**

  A) The alternative is correct
  B) We accept the null
  C) We fail to reject the null
  D) We reject the null
  E) The null is correct

- **Answer (tutor only):** C
- **Explanation (tutor only):** p = 0.153 > 0.05, so we fail to reject. That doesn't mean the null is correct.
- **Why the wrong options are wrong (tutor only):**
  A) and D) p > α.
  E) and B) We never accept or prove the null.
- **Hint:** Compare p with 0.05.

### ch17-chimein-07-v2
- **Kind:** AI-written version of ch17-chimein-07
- **Concepts:** F & the ANOVA table; Hypotheses & p-values
- **Type:** MC
- **Question:**

Which R code gives the p-value for F = 14.7 on 1 and 21 degrees of freedom?

- **Options:**

  A) qf(14.7, df1 = 1, df2 = 21)
  B) 2 * pf(14.7, df1 = 1, df2 = 21, lower.tail = FALSE)
  C) pf(14.7, df1 = 1, df2 = 21)
  D) pf(14.7, df1 = 1, df2 = 21, lower.tail = FALSE)

- **Answer (tutor only):** D
- **Explanation (tutor only):** The F test uses the upper tail only: the area above the observed F.
- **Why the wrong options are wrong (tutor only):**
  A) qf() takes a probability.
  B) F tests aren't doubled.
  C) That's the lower tail.
- **Hint:** Upper tail, not doubled.

### ch17-hw-01
- **Kind:** Course original
- **Concepts:** Sums of squares & deviations
- **Type:** matching
- **Question:**

Consider this code:

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
3. SS_C

- **Options:**

  A) Sum of squares total
  B) Sum of squares model
  C) Sum of squares error

- **Answer (tutor only):** 1-C, 2-A, 3-B
- **Explanation (tutor only):** Error: observations minus their group's prediction. Total: observations minus the grand mean. Model: group predictions minus the grand mean.
- **Why the wrong options are wrong (tutor only):**
  Common mix-up: model vs total. Total starts from each observation; model starts from each group's mean.
- **Hint:** For each line, ask: what is being compared to what?

### ch17-hw-01-v1
- **Kind:** AI-written version of ch17-hw-01
- **Concepts:** Sums of squares & deviations
- **Type:** matching
- **Question:**

Consider this code:

SS <- data |>
  mutate(grand = mean(y)) |>
  group_by(group) |>
  mutate(fit = mean(y)) |>
  ungroup() |>
  summarise(SS_1 = sum((y - grand)^2),
            SS_2 = sum((fit - grand)^2),
            SS_3 = sum((y - fit)^2))

Match each label to the sum of squares it calculates:

1. SS_1
2. SS_2
3. SS_3

- **Options:**

  A) Sum of squares error
  B) Sum of squares total
  C) Sum of squares model

- **Answer (tutor only):** 1-B, 2-C, 3-A
- **Explanation (tutor only):** Total: observation - grand mean. Model: group mean (fit) - grand mean. Error: observation - group mean.
- **Why the wrong options are wrong (tutor only):**
  Look at what is subtracted from what.
- **Hint:** Which pair of values does each line compare?

### ch17-hw-01-v2
- **Kind:** AI-written version of ch17-hw-01
- **Concepts:** Sums of squares & deviations
- **Type:** matching
- **Question:**

In an ANOVA, which deviations are squared and summed to get each sum of squares?

1. SS error
2. SS model
3. SS total

- **Options:**

  A) Each observation minus the grand mean
  B) Each group's mean minus the grand mean, once per observation
  C) Each observation minus its own group's mean

- **Answer (tutor only):** 1-C, 2-B, 3-A
- **Explanation (tutor only):** Error: within groups. Model: between group means and the grand mean. Total: everything around the grand mean.
- **Why the wrong options are wrong (tutor only):**
  SS total = SS model + SS error.
- **Hint:** Error is within groups.

### ch17-hw-02
- **Kind:** Course original
- **Concepts:** Sums of squares & deviations
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch17-hw-deviations.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch17-hw-deviations.png)
- **Question:**

Each plot shows the admixture proportion of individual pink and white parviflora plants, the grand mean (black line) and the group means (dashed lines). The vertical lines show deviations. Match each plot to the deviations it shows:

1. plot 1
2. plot 2
3. plot 3

- **Options:**

  A) Error deviations
  B) Model deviations
  C) Total deviations

- **Answer (tutor only):** 1-C, 2-B, 3-A
- **Explanation (tutor only):** Plot 1: each point to the grand mean (total). Plot 2: each group mean to the grand mean (model). Plot 3: each point to its group mean (error).
- **Why the wrong options are wrong (tutor only):**
  Look at where each line starts and ends: a point, a group mean (dashed), or the grand mean (black).
- **Hint:** Where does each vertical line start, and where does it end?

### ch17-hw-02-v1
- **Kind:** AI-written version of ch17-hw-02
- **Concepts:** Sums of squares & deviations
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch17-hw-deviations.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch17-hw-deviations.png)
- **Question:**

Each plot shows the admixture proportion of individual pink and white parviflora plants, the grand mean (black line) and the group means (dashed lines). The vertical lines show deviations. Which plot's squared and summed lines give the sum of squares that the model leaves unexplained?

- **Options:**

  A) plot 1
  B) plot 2
  C) plot 3

- **Answer (tutor only):** C
- **Explanation (tutor only):** The unexplained part is SS error: each point to its group mean (plot 3).
- **Why the wrong options are wrong (tutor only):**
  A) Total deviations.
  B) Model deviations.
- **Hint:** What's left after fitting group means?

### ch17-hw-02-v2
- **Kind:** AI-written version of ch17-hw-02
- **Concepts:** Sums of squares & deviations
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch17-hw-deviations.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch17-hw-deviations.png)
- **Question:**

Each plot shows the admixture proportion of individual pink and white parviflora plants, the grand mean (black line) and the group means (dashed lines). The vertical lines show deviations. In plot 2, all points in the same group have the same length of line. Why?

- **Options:**

  A) Each line goes from a point to its group mean
  B) Each line goes from the group mean to the grand mean
  C) Each line goes from a point to the grand mean

- **Answer (tutor only):** B
- **Explanation (tutor only):** Model deviations depend only on the group, so every member of a group has the same one.
- **Why the wrong options are wrong (tutor only):**
  A) Those vary point to point (error).
  C) Those vary point to point (total).
- **Hint:** Which deviation ignores the individual values?

### ch17-hw-03
- **Kind:** Course original
- **Concepts:** F & the ANOVA table
- **Type:** matching
- **Question:**

Complete this ANOVA table:

source | df | Sum Sq | Mean Sq | F | p-value
model | 1 | 2.8475 | 2.8475 | [B] | [C]
error | 47 | 1.9789 | [A] | |

Match each missing entry to its value:

1. [A] (mean square error)
2. [B] (F)
3. [C] (p-value)

- **Options:**

  A) 0.98
  B) 67.6
  C) 1.19 × 10⁻¹⁰
  D) 0.05
  E) 0.0421
  F) 1.4

- **Answer (tutor only):** 1-E, 2-B, 3-C
- **Explanation (tutor only):** MS error = 1.9789 / 47 = 0.0421. F = MS model / MS error = 2.8475 / 0.0421 = 67.6. An F of 67.6 on 1 and 47 df is extremely unlikely under the null: p = 1.19 × 10⁻¹⁰.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: dividing SS error by the total df, or computing F as MS error / MS model (0.015).
- **Hint:** Mean square = sum of squares / df; F = MS model / MS error.

### ch17-hw-03-v1
- **Kind:** AI-written version of ch17-hw-03
- **Concepts:** F & the ANOVA table
- **Type:** matching
- **Question:**

Complete this ANOVA table:

source | df | Sum Sq | Mean Sq | F | p-value
model | 2 | 12.0 | [A] | [C] | [D]
error | 27 | 54.0 | [B] | |

Match each missing entry to its value:

1. [A] (mean square model)
2. [B] (mean square error)
3. [C] (F)
4. [D] (p-value)

- **Options:**

  A) 0.5
  B) 0.067
  C) 0.22
  D) 3.0
  E) 6.0
  F) 2.0

- **Answer (tutor only):** 1-E, 2-F, 3-D, 4-B
- **Explanation (tutor only):** MS model = 12 / 2 = 6. MS error = 54 / 27 = 2. F = 6 / 2 = 3. With 2 and 27 df, p = 0.067.
- **Why the wrong options are wrong (tutor only):**
  Mean square = SS / df; F = MS model / MS error.
- **Hint:** Divide each SS by its df first.

### ch17-hw-03-v2
- **Kind:** AI-written version of ch17-hw-03
- **Concepts:** F & the ANOVA table
- **Type:** matching
- **Question:**

Complete this ANOVA table:

source | df | Sum Sq | Mean Sq | F
model | 1 | [A] | 3.0 | 6.0
error | 20 | [B] | [C] |

Match each missing entry to its value:

1. [A] (SS model)
2. [B] (SS error)
3. [C] (MS error)

- **Options:**

  A) 10.0
  B) 0.5
  C) 60.0
  D) 3.0

- **Answer (tutor only):** 1-D, 2-A, 3-B
- **Explanation (tutor only):** SS model = 3.0 × 1 = 3.0. MS error = MS model / F = 3.0 / 6.0 = 0.5. SS error = 0.5 × 20 = 10.0.
- **Why the wrong options are wrong (tutor only):**
  Work backwards: F = MS model / MS error and MS = SS / df.
- **Hint:** Start from F to get MS error.

### ch17-hw-04
- **Kind:** Course original
- **Concepts:** Effect size & R²
- **Type:** MC
- **Question:**

An ANOVA comparing two groups gives:

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
Huge | > 2.00

- **Options:**

  A) Tiny
  B) Small
  C) Medium
  D) Large
  E) Very large
  F) Huge

- **Answer (tutor only):** F
- **Explanation (tutor only):** Pooled SD = √0.0421 = 0.205. Cohen's d = 0.51 / 0.205 = 2.49, a huge effect (> 2).
- **Why the wrong options are wrong (tutor only):**
  Common mistake: dividing by the variance (0.0421) instead of the SD, or by MS model.
- **Hint:** Turn the mean square error into a standard deviation first.

### ch17-hw-04-v1
- **Kind:** AI-written version of ch17-hw-04
- **Concepts:** Effect size & R²
- **Type:** MC
- **Question:**

An ANOVA comparing two groups of tadpoles gives a mean square error of 0.25. The difference in group means is 0.3 g. With only two groups, the mean square error equals the pooled variance. How big is the effect?

Size | Cohen's d
Tiny | 0.01 to 0.20
Small | 0.20 to 0.50
Medium | 0.50 to 0.80
Large | 0.80 to 1.20
Very large | 1.20 to 2.00
Huge | > 2.00

- **Options:**

  A) Tiny
  B) Small
  C) Medium
  D) Large
  E) Huge

- **Answer (tutor only):** C
- **Explanation (tutor only):** Pooled SD = √0.25 = 0.5. d = 0.3 / 0.5 = 0.6, medium.
- **Why the wrong options are wrong (tutor only):**
  A), B) Too small. D), E) Too large. (Dividing by the variance, 0.25, would wrongly give 1.2.)
- **Hint:** Take the square root of MS error first.

### ch17-hw-04-v2
- **Kind:** AI-written version of ch17-hw-04
- **Concepts:** Effect size & R²
- **Type:** MC
- **Question:**

An ANOVA comparing two groups gives:

source | df | Sum Sq | Mean Sq
model | 1 | 2.8475 | 2.8475
error | 47 | 1.9789 | 0.0421

With only two groups, the mean square error equals the pooled variance. What is the pooled standard deviation?

- **Options:**

  A) 0.0018
  B) 0.205
  C) 1.41
  D) 0.0421

- **Answer (tutor only):** B
- **Explanation (tutor only):** Pooled SD = √0.0421 = 0.205.
- **Why the wrong options are wrong (tutor only):**
  A) That's 0.0421².
  C) That's √1.9789.
  D) That's the variance.
- **Hint:** Square root of MS error.

### ch17-hw-05
- **Kind:** Course original
- **Concepts:** Effect size & R²
- **Type:** numeric
- **Question:**

An ANOVA comparing two groups gives SS model = 2.8475 (1 df) and SS error = 1.9789 (47 df). What is R², the proportion of variance in Y attributable to the model? Report it to three decimals.

- **Answer (tutor only):** 0.590
- **Explanation (tutor only):** R² = SS model / SS total = 2.8475 / (2.8475 + 1.9789) = 2.8475 / 4.8264 = 0.590.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: SS model / SS error (1.44).
- **Hint:** SS total = SS model + SS error.

### ch17-hw-05-v1
- **Kind:** AI-written version of ch17-hw-05
- **Concepts:** Effect size & R²
- **Type:** numeric
- **Question:**

An ANOVA gives SS model = 12.0 and SS error = 54.0. What is R²? Report it to three decimals.

- **Answer (tutor only):** 0.182
- **Explanation (tutor only):** R² = 12 / (12 + 54) = 12 / 66 = 0.182.
- **Hint:** SS model / SS total.

### ch17-hw-05-v2
- **Kind:** AI-written version of ch17-hw-05
- **Concepts:** Effect size & R²
- **Type:** numeric
- **Question:**

An ANOVA gives SS total = 4.8264 and R² = 0.590. What is SS error? Report it to two decimals.

- **Answer (tutor only):** 1.98
- **Explanation (tutor only):** SS error = SS total × (1 - R²) = 4.8264 × 0.41 = 1.98.
- **Hint:** R² is the share explained; the rest is error.

### ch17-hw-06
- **Kind:** Course original
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

Our p-value equaled the probability of being struck by lightning and bitten by a shark on the same day. Technically, this means that:

- **Options:**

  A) The null would rarely generate data this extreme
  B) There is a very small chance that the null is true
  C) The null is false

- **Answer (tutor only):** A
- **Explanation (tutor only):** A p-value is the probability of data at least this extreme if the null were true. It isn't the probability the null is true, and it doesn't prove the null false.
- **Why the wrong options are wrong (tutor only):**
  B) Treats p as the probability of the null.
  C) Even a tiny p doesn't prove anything for certain.
- **Hint:** What does a p-value assume?

### ch17-hw-06-v1
- **Kind:** AI-written version of ch17-hw-06
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

An ANOVA gives p = 0.0000001. Technically, this means that:

- **Options:**

  A) There is a 0.00001% chance that the null hypothesis is true
  B) The differences among the group means must be very large
  C) Data this extreme would be very rare if the null were true
  D) The group means are definitely different from one another

- **Answer (tutor only):** C
- **Explanation (tutor only):** p is the probability of data at least this extreme under the null.
- **Why the wrong options are wrong (tutor only):**
  A) p isn't P(null).
  B) A tiny p can come from a small effect in a large sample.
  D) Rejection isn't proof.
- **Hint:** p assumes the null.

### ch17-hw-06-v2
- **Kind:** AI-written version of ch17-hw-06
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

An ANOVA gives p = 0.62. Technically, this means that:

- **Options:**

  A) There is a 62% chance that the null hypothesis is true
  B) There is a 38% chance that the alternative is true
  C) The null would often generate data at least this extreme
  D) The group means are definitely equal to one another

- **Answer (tutor only):** C
- **Explanation (tutor only):** 62% of datasets generated under the null would be at least this extreme, so ours isn't surprising.
- **Why the wrong options are wrong (tutor only):**
  A) and B) p isn't a probability about hypotheses.
  D) Failing to reject isn't proof.
- **Hint:** p assumes the null.

### ch17-hw-07
- **Kind:** Course original
- **Concepts:** F & the ANOVA table
- **Type:** MC
- **Question:**

With two groups, we can use a two-sample t-test or an ANOVA. When is a two-sample t-test preferred over an ANOVA?

- **Options:**

  A) Never: an ANOVA is always the better choice
  B) When data are non-independent within groups
  C) Either: they agree (F = t²); t also gives direction

- **Answer (tutor only):** C
- **Explanation (tutor only):** With two groups, F = t² and the p-values are identical. The choice is about presentation; the t also gives the direction of the difference.
- **Why the wrong options are wrong (tutor only):**
  A) Both are fine with two groups.
  B) Non-independence is a problem for both.
- **Hint:** What is t² for two groups?

### ch17-hw-07-v1
- **Kind:** AI-written version of ch17-hw-07
- **Concepts:** F & the ANOVA table
- **Type:** MC
- **Question:**

A two-sample t-test comparing two groups gives t = 3. What F would an ANOVA on the same data give?

- **Options:**

  A) F = 9
  B) F = 3
  C) F = 1.73
  D) F = 6

- **Answer (tutor only):** A
- **Explanation (tutor only):** With two groups, F = t² = 9, and the p-values are identical.
- **Why the wrong options are wrong (tutor only):**
  B) F isn't equal to t.
  C) That's √3.
  D) That's 2t.
- **Hint:** F = t² for two groups.

### ch17-hw-07-v2
- **Kind:** AI-written version of ch17-hw-07
- **Concepts:** F & the ANOVA table
- **Type:** MC
- **Question:**

With two groups, a two-sample t-test and an ANOVA give the same p-value. What does the t-test report that the F does not?

- **Options:**

  A) The direction of the difference, through t's sign
  B) The amount of variance explained by the model
  C) A separate p-value for each group being compared
  D) Whether the difference is statistically significant

- **Answer (tutor only):** A
- **Explanation (tutor only):** F = t² is always positive, so it loses the sign; t tells you which group is larger.
- **Why the wrong options are wrong (tutor only):**
  B) That's R², from the ANOVA table.
  C) Neither does.
  D) Both give the same p.
- **Hint:** What does squaring remove?
