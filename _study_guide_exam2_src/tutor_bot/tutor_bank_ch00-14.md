# Applied Biostats tutor: question bank, chapters 0–14 (Exam 2, chapters 13–21, plus an Exam 1 review as chapter 0)

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

## Chapter 0: Key concepts from Exam 1 (review)

### rev-ch08-book-03
- **Kind:** Course original
- **Concepts:** Samples, populations & bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-book-biased-sampdist.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch08-book-biased-sampdist.png)
- **Question:**

I tried to estimate mean human gene length by randomly selecting nucleotides from the genome, finding the gene they were in, and recording that gene's length, until I had 50 genes. I did this 1000 times. The plot shows my 1000 estimates; the red dashed line is the true population mean (2.62 kb).

The difference between the true mean and my estimates is most likely explained by:

- **Options:**

  A) Sampling bias
  B) Non-independence
  C) Sampling error
  D) The unreliability of the law of large numbers

- **Answer (tutor only):** A
- **Explanation (tutor only):** Every one of the 1000 estimates is above the true mean (the whole distribution sits around 4 kb). That's a systematic shift, i.e., bias, not chance.
- **Why the wrong options are wrong (tutor only):**
  B) Non-independence would widen the distribution, not shift it away from the truth.
  C) Sampling error would scatter estimates on both sides of the truth.
  D) The law of large numbers works fine for random samples.
- **Hint:** Are the estimates scattered around the truth, or all off in one direction?

### rev-ch08-book-03-v1
- **Kind:** AI-written version of rev-ch08-book-03
- **Concepts:** Samples, populations & bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-family-biased.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch08-var-family-biased.png)
- **Question:**

To estimate the mean number of children per family in a town, I asked 40 randomly chosen high-school students how many children are in their family (counting themselves), and averaged their answers. I repeated this 1000 times. The plot shows my 1000 estimates; the red line is the true mean number of children per family with children (2.56).

The difference between the true mean and my estimates is most likely explained by:

- **Options:**

  A) Too few repetitions
  B) Sampling error
  C) Sampling bias
  D) Non-independence

- **Answer (tutor only):** C
- **Explanation (tutor only):** Nearly all 1000 estimates are above 2.56: a systematic shift. Families with more children have more students to be asked, so big families are oversampled (size-biased sampling). Sampling error would scatter estimates on both sides of the truth.
- **Why the wrong options are wrong (tutor only):**
  A) More repetitions would show the same shift.
  B) Chance would put estimates on both sides of the line.
  D) Non-independence would widen the spread, not shift it.
- **Hint:** Are the estimates scattered around the truth, or all off in one direction?

### rev-ch08-book-03-v2
- **Kind:** AI-written version of rev-ch08-book-03
- **Concepts:** Samples, populations & bias; Sampling distribution, SD & SE
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-trout-unbiased.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch08-var-trout-unbiased.png)
- **Question:**

A hatchery pond holds thousands of trout with a true mean length of 31.0 cm. A technician nets 25 fish at random, measures them, and returns them, and does this 1000 times. The plot shows the 1000 estimated means (red line = true mean).

The individual estimates range from about 27 to 34.5 cm. This spread is best explained by:

- **Options:**

  A) Sampling bias
  B) Measurement error
  C) Non-independence
  D) Sampling error

- **Answer (tutor only):** D
- **Explanation (tutor only):** The estimates are scattered evenly on both sides of the true mean, as expected from chance differences among random samples. There's no systematic shift, so no bias.
- **Why the wrong options are wrong (tutor only):**
  A) Bias would shift the whole histogram away from the red line.
  B) Even perfect measurements would give this spread, because each net catches different fish.
  C) Nothing suggests related fish.
- **Hint:** Is the histogram centered on the red line?

### rev-ch08-book-06
- **Kind:** Course original
- **Concepts:** Sampling distribution, SD & SE
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-book-sampdist-n.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch08-book-sampdist-n.png)
- **Question:**

The plot shows sampling distributions of mean human gene length from 1000 random samples each of n = 5, 30 and 500 genes (red line = true mean). What explains the difference between the panels, and which n has the smallest standard error?

- **Options:**

  A) Less sampling error in larger samples; they all have about the same SE
  B) Less sampling bias in larger samples; n = 500 has the smallest SE
  C) Less non-independence in larger samples; n = 5 has the smallest SE
  D) Less sampling error in larger samples; n = 500 has the smallest SE

- **Answer (tutor only):** D
- **Explanation (tutor only):** All three are centered on the truth (no bias). They get narrower as n increases. The SEs computed from the data are about 1.04 kb (n = 5), 0.37 (n = 30) and 0.09 (n = 500).
- **Why the wrong options are wrong (tutor only):**
  A) The widths clearly differ.
  B) None of the three is biased; they're all centered on the red line.
  C) Sample size doesn't change independence.
- **Hint:** Center = bias; width = sampling error / SE.

### rev-ch08-book-06-v1
- **Kind:** AI-written version of rev-ch08-book-06
- **Concepts:** Sampling distribution, SD & SE
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-pink-sampdist.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch08-var-pink-sampdist.png)
- **Question:**

In a large Clarkia population, 30% of plants have pink flowers. The plot shows the sampling distributions of the proportion of pink plants in random samples of n = 10, 40 and 160 plants (red line = true proportion, 0.30).

What explains the difference between the panels, and which n has the smallest standard error?

- **Options:**

  A) Less sampling error in larger samples; n = 160 has the smallest SE
  B) Less sampling error in larger samples; they all have about the same SE
  C) Less non-independence in larger samples; n = 10 has the smallest SE
  D) Less sampling bias in larger samples; n = 160 has the smallest SE

- **Answer (tutor only):** A
- **Explanation (tutor only):** All three are centered on 0.30 (no bias) and get narrower as n increases. SE = √(0.3 × 0.7 / n): about 0.145, 0.072 and 0.036.
- **Why the wrong options are wrong (tutor only):**
  B) The widths clearly differ.
  C) Sample size doesn't change independence; n = 10 has the largest SE.
  D) None is biased.
- **Hint:** Center = bias; width = sampling error / SE.

### rev-ch08-book-06-v2
- **Kind:** AI-written version of rev-ch08-book-06
- **Concepts:** Sampling distribution, SD & SE
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-oak-sampdist.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch08-var-oak-sampdist.png)
- **Question:**

Imagine we could measure every one of the 8,000 red oaks in a forest: their mean height is 18.0 m and the SD is 4.0 m. The plot shows sampling distributions of the mean height for random samples of n = 4, 16 and 64 trees (each panel is a histogram of 10,000 sample means; red line = true mean).

Going from n = 16 to n = 64 (four times as many trees), what happens to the standard error?

- **Options:**

  A) It doubles
  B) It halves (about 1 m → 0.5 m)
  C) It shrinks to a quarter, since there are four times as many trees
  D) It stays the same

- **Answer (tutor only):** B
- **Explanation (tutor only):** SE = SD/√n. Quadrupling n doubles √n, so the SE halves: 4/√16 = 1 m, 4/√64 = 0.5 m. You can see the n = 64 panel is about half as wide as n = 16.
- **Why the wrong options are wrong (tutor only):**
  A) Larger samples reduce the SE.
  C) That would need 16 times the sample.
  D) The SE depends on n.
- **Hint:** SE = SD / √n. What happens to √n when n quadruples?

### rev-ch08-gquiz-02
- **Kind:** Course original
- **Concepts:** Samples, populations & bias
- **Type:** MC
- **Question:**

In class, students sampled 10 crayons (without replacement) from a bin and reported the number that were red, using a Google form.

I asked that no more than one person per table report results for the crayon sampling. Why?

- **Options:**

  A) To minimize sampling bias
  B) To minimize sampling error
  C) To minimize non-independence
  D) To be a pedantic jerk

- **Answer (tutor only):** C
- **Explanation (tutor only):** People at the same table may have shared one sample (or influenced each other), so their reports aren't independent: two reports of the same draw would count as two observations when they're really one.
- **Why the wrong options are wrong (tutor only):**
  A) Duplicate reports don't systematically shift the center.
  B) More reports would seem to reduce error, but non-independent reports only fake it.
  D) 😉
- **Hint:** If two people at one table report the same sample, how many independent samples is that?

### rev-ch08-gquiz-02-v1
- **Kind:** AI-written version of rev-ch08-gquiz-02
- **Concepts:** Samples, populations & bias
- **Type:** MC
- **Question:**

For a class survey of sleep hours, a teacher asks only one person per household to respond. Why?

- **Options:**

  A) To reduce the number of responses
  B) To minimize sampling error
  C) To minimize sampling bias
  D) To minimize non-independence

- **Answer (tutor only):** D
- **Explanation (tutor only):** People in the same household share routines (and noise!), so their sleep is more alike. Counting several per household would treat related observations as independent.
- **Why the wrong options are wrong (tutor only):**
  A) That's a side effect, not the reason.
  B) Fewer responses would increase, not reduce, sampling error.
  C) It doesn't systematically shift the estimate.
- **Hint:** Would two people from the same household be more alike than two random students?

### rev-ch08-gquiz-02-v2
- **Kind:** AI-written version of rev-ch08-gquiz-02
- **Concepts:** Samples, populations & bias
- **Type:** MC
- **Question:**

In a class activity, each table drew one sample of 10 crayons, but everyone at the table entered that same sample into the form, so 30 entries came from 6 samples. What's the problem?

- **Options:**

  A) The entries aren't independent: there are really only 6 samples
  B) There's no problem; more entries is always better
  C) The sample size for each draw (10 crayons) was too small
  D) The estimates will be biased toward red, since tables share the same bin

- **Answer (tutor only):** A
- **Explanation (tutor only):** Duplicate entries of one draw aren't new information. Treating them as 30 independent samples overstates how much data we have, making results look more precise than they are.
- **Why the wrong options are wrong (tutor only):**
  B) More entries only help if they're independent.
  C) That's a separate issue.
  D) Duplicating samples doesn't shift the center.
- **Hint:** How many independent draws were there?

### rev-ch08-hw-01
- **Kind:** Course original
- **Concepts:** Samples, populations & bias
- **Type:** matching
- **Question:**

Fill in the blanks:

When we do science, our data summaries represent (1) ____ found by considering all individuals in our (2) ____. These give us a hint of the truth we really care about: true (3) ____ from the entire (4) ____.

- **Options:**

  A) estimates
  B) parameters
  C) sample
  D) population

- **Answer (tutor only):** 1-A, 2-C, 3-B, 4-D
- **Explanation (tutor only):** We compute estimates (e.g., a sample mean) from the sample we actually measured. They're our best guess at parameters, the true values for the whole population, which we almost never get to see.
- **Why the wrong options are wrong (tutor only):**
  Parameters describe populations and estimates describe samples. Swapping them is the classic mix-up.
- **Hint:** Which one do we calculate, and which one do we want to know?

### rev-ch08-hw-01-v1
- **Kind:** AI-written version of rev-ch08-hw-01
- **Concepts:** Samples, populations & bias
- **Type:** matching
- **Question:**

A survey team measures the wingspan of 120 randomly caught monarch butterflies and finds a mean of 9.6 cm.

Fill in the blanks: 9.6 cm is our (1) ____, calculated from our (2) ____. We use it to learn about the true mean wingspan: the (3) ____ that describes the whole (4) ____ of monarchs.

- **Options:**

  A) estimate
  B) parameter
  C) sample
  D) population

- **Answer (tutor only):** 1-A, 2-C, 3-B, 4-D
- **Explanation (tutor only):** We calculate estimates (like this mean of 9.6 cm) from the sample we measured. They're our best guess at parameters, the true values for the whole population.
- **Why the wrong options are wrong (tutor only):**
  Parameters describe populations, estimates describe samples. 9.6 cm came from 120 butterflies, so it's an estimate.
- **Hint:** Which one did the team actually calculate?

### rev-ch08-hw-01-v2
- **Kind:** AI-written version of rev-ch08-hw-01
- **Concepts:** Samples, populations & bias
- **Type:** matching
- **Question:**

Classify each:

1. The true proportion of all ballots in a state that went to candidate X
2. The proportion of 1,000 polled voters who say they voted for X
3. The 1,000 polled voters
4. Every voter in the state

- **Options:**

  A) estimate
  B) parameter
  C) sample
  D) population

- **Answer (tutor only):** 1-B, 2-A, 3-C, 4-D
- **Explanation (tutor only):** The true proportion over all ballots is a parameter of the population (every voter). The poll's proportion is an estimate calculated from the sample of 1,000.
- **Why the wrong options are wrong (tutor only):**
  Swapping estimate and parameter is the classic mix-up: if it's calculated from a subset, it's an estimate.
- **Hint:** Which number would you only know if you counted everyone?

### rev-ch08-hw-04
- **Kind:** Course original
- **Concepts:** Sampling distribution, SD & SE
- **Type:** matching
- **Question:**

Fill in the blanks:

1. The ____ estimates the expected variation among individuals in the population.
2. The ____ estimates the expected variation among sample estimates from the population.

- **Options:**

  A) standard deviation
  B) standard error

- **Answer (tutor only):** 1-A, 2-B
- **Explanation (tutor only):** The SD describes spread among individuals. The SE is the SD of the sampling distribution, i.e., spread among estimates. The SE shrinks as n grows; the SD doesn't.
- **Why the wrong options are wrong (tutor only):**
  Swapping them is the most common confusion in the chapter.
- **Hint:** Individuals → SD. Estimates → SE.

### rev-ch08-hw-04-v1
- **Kind:** AI-written version of rev-ch08-hw-04
- **Concepts:** Sampling distribution, SD & SE
- **Type:** matching
- **Question:**

Bill length in a population of finches has an SD of 1.2 mm. You take samples of 36 birds.

1. Which describes how much individual finches differ from each other?
2. Which describes how much the mean of 36 birds would vary from sample to sample?

- **Options:**

  A) standard deviation
  B) standard error

- **Answer (tutor only):** 1-A, 2-B
- **Explanation (tutor only):** The SD (1.2 mm) is the spread of individuals. The SE is the spread of estimates: here about 1.2/√36 = 0.2 mm.
- **Why the wrong options are wrong (tutor only):**
  Swapping them is the most common confusion in the chapter.
- **Hint:** Individuals → SD. Estimates → SE.

### rev-ch08-hw-04-v2
- **Kind:** AI-written version of rev-ch08-hw-04
- **Concepts:** Sampling distribution, SD & SE
- **Type:** MC
- **Question:**

A paper reports: "mean body mass = 24.1 g (± 0.3 g, SE), n = 100 mice." What does the 0.3 g tell you?

- **Options:**

  A) How far a typical mouse is from the mean
  B) The measurement error of the scale
  C) The difference between the heaviest and the lightest mouse in the sample
  D) How far a typical sample mean (n = 100) is from the true mean

- **Answer (tutor only):** D
- **Explanation (tutor only):** A standard error describes the variability of an estimate (the mean of 100 mice). Individual mice vary much more: the SD here would be about 0.3 × √100 = 3 g.
- **Why the wrong options are wrong (tutor only):**
  A) That's the SD.
  B) Measurement error is a different thing; the SE comes from sampling.
  C) That's the range.
- **Hint:** SE = spread of what?

### rev-ch08-hw-05
- **Kind:** Course original
- **Concepts:** Sampling distribution, SD & SE
- **Type:** MC
- **Question:**

Sampling error can never be fully eliminated. Which of the following best mitigates sampling error?

- **Options:**

  A) Taking precise measurements
  B) Sampling at random
  C) Taking a large sample
  D) There is nothing to be done; you can't fight chance deviations

- **Answer (tutor only):** C
- **Explanation (tutor only):** Sampling error is chance variation from who happens to be in your sample. Larger samples average out more of that chance, so estimates land closer to the parameter (the SE shrinks with √n).
- **Why the wrong options are wrong (tutor only):**
  A) Precise measurements reduce measurement error, a different thing.
  B) Random sampling prevents bias, not sampling error.
  D) You can't eliminate it, but you can shrink it.
- **Hint:** What makes sampling distributions narrower?

### rev-ch08-hw-05-v1
- **Kind:** AI-written version of rev-ch08-hw-05
- **Concepts:** Sampling distribution, SD & SE
- **Type:** MC
- **Question:**

A lab estimates the mean seed mass of a weed from 15 randomly chosen plants. The estimate seems imprecise. What change would most reduce sampling error?

- **Options:**

  A) Weigh the seeds on a more precise scale, so each measurement has less error
  B) Choose the 15 healthiest-looking plants, so the seeds are more uniform
  C) Nothing; sampling error can't be reduced
  D) Measure 150 randomly chosen plants

- **Answer (tutor only):** D
- **Explanation (tutor only):** Sampling error comes from which individuals happen to be in the sample. Larger random samples average over more individuals, so the SE shrinks (with √n).
- **Why the wrong options are wrong (tutor only):**
  A) Reduces measurement error, a different source of error.
  B) Non-random selection adds bias.
  C) It can't be eliminated, but it can be reduced.
- **Hint:** What makes a sampling distribution narrower?

### rev-ch08-hw-05-v2
- **Kind:** AI-written version of rev-ch08-hw-05
- **Concepts:** Samples, populations & bias; Sampling distribution, SD & SE
- **Type:** MC
- **Question:**

A researcher doubles her sample size but keeps sampling only from plants near the road. What happens?

- **Options:**

  A) Sampling error decreases; the roadside bias remains
  B) Bias decreases, but sampling error stays the same
  C) Both sampling error and bias decrease, since more data fixes both
  D) Nothing changes

- **Answer (tutor only):** A
- **Explanation (tutor only):** A larger sample makes the estimate more precise (less sampling error), but if roadside plants differ from the rest, the estimate is still systematically off. A bigger biased sample is precisely wrong.
- **Why the wrong options are wrong (tutor only):**
  C) and B) Sample size doesn't fix bias.
  D) Precision does improve.
- **Hint:** Does sampling more from the same place fix who's being sampled?

### rev-ch09-book-04
- **Kind:** Course original
- **Concepts:** Bootstrap & confidence intervals
- **Type:** select-all
- **Question:**

You calculated a 95% confidence interval from a random sample. What is the probability that the interval captured the true population parameter? (Check all that apply.)

- **Options:**

  A) There is no probability about this; it either did or it did not
  B) 95%
  C) It depends on the sample size
  D) It depends on the sample standard deviation

- **Answer (tutor only):** A
- **Explanation (tutor only):** Your interval (e.g., 0.108–0.199) and the parameter are both fixed numbers, so the chance part is over.
- **Why the wrong options are wrong (tutor only):**
  B) 95% is the method's long-run rate.
  C) and D) These change the width, not the interpretation.
- **Hint:** Is anything random left?

### rev-ch09-book-04-v1
- **Kind:** AI-written version of rev-ch09-book-04
- **Concepts:** Bootstrap & confidence intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-gquiz-ringtoss.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch09-gquiz-ringtoss.png)
- **Question:**

A 95% CI for the proportion of infected ticks is 0.21 to 0.34. Which statement is correct?

- **Options:**

  A) It either does or doesn't contain the true proportion
  B) The true proportion is 0.275
  C) There's a 95% chance the true proportion is between 0.21 and 0.34
  D) 95% of ticks have infection proportions between 0.21 and 0.34

- **Answer (tutor only):** A
- **Explanation (tutor only):** After calculation, the interval and the parameter are fixed. The 95% refers to the method.
- **Why the wrong options are wrong (tutor only):**
  B) 0.275 is the midpoint, an estimate, not the truth.
  C) Attaches the method's rate to this one interval.
  D) Individual ticks are infected or not; the CI is about the population proportion.
- **Hint:** Is anything random left once the interval is computed?

### rev-ch09-book-04-v2
- **Kind:** AI-written version of rev-ch09-book-04
- **Concepts:** Bootstrap & confidence intervals
- **Type:** select-all
- **Question:**

Which change would make a newly calculated 95% CI narrower? (Select all that apply.)

- **Options:**

  A) A larger sample
  B) Less variable data
  C) Choosing 99% instead of 95% confidence
  D) Calculating it more carefully

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** Width depends on the SE (SD/√n): more data or less variability narrows it. Higher confidence widens it.
- **Why the wrong options are wrong (tutor only):**
  C) A 99% interval must be wider to catch the truth more often.
  D) A correct calculation doesn't change the width.
- **Hint:** Width tracks the SE and the confidence level.

### rev-ch09-chime-04
- **Kind:** Course original
- **Concepts:** Sampling distribution, SD & SE; Bootstrap & confidence intervals
- **Type:** select-all
- **Question:**

Which will get smaller as the sample size increases? (Select all correct.)

- **Options:**

  A) The standard deviation
  B) The variance
  C) The standard error
  D) The width of a confidence interval (e.g., upper minus lower 99% CI)

- **Answer (tutor only):** C, D
- **Explanation (tutor only):** More data means less uncertainty in estimates: the SE and CI width shrink. The SD and variance describe the population's spread; larger samples estimate them more precisely but don't make them smaller.
- **Why the wrong options are wrong (tutor only):**
  A) and B) These estimate a fixed population property; they don't trend downward with n.
- **Hint:** Which of these describe the data, and which describe uncertainty about an estimate?

### rev-ch09-chime-04-v1
- **Kind:** AI-written version of rev-ch09-chime-04
- **Concepts:** Sampling distribution, SD & SE
- **Type:** select-all
- **Question:**

A lab increases sample size from 25 to 100. Which will tend to stay about the same? (Select all correct.)

- **Options:**

  A) The standard deviation
  B) The mean
  C) The standard error
  D) The width of a 95% CI

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** The SD and mean describe the population and don't trend with n. The SE (≈ SD/√n) halves when n quadruples, and the CI narrows with it.
- **Why the wrong options are wrong (tutor only):**
  C) and D) These shrink: four times the data gives half the SE.
- **Hint:** Which quantities describe the population, and which describe your precision?

### rev-ch09-chime-04-v2
- **Kind:** AI-written version of rev-ch09-chime-04
- **Concepts:** Sampling distribution, SD & SE
- **Type:** MC
- **Question:**

If the SD stays the same, by how much does the standard error of the mean change when n goes from 25 to 100?

- **Options:**

  A) It doubles
  B) It is cut to a quarter
  C) It stays the same
  D) It is cut in half

- **Answer (tutor only):** D
- **Explanation (tutor only):** SE = SD/√n. √25 = 5 and √100 = 10, so the SE is halved.
- **Why the wrong options are wrong (tutor only):**
  A) More data reduces, not increases, the SE.
  B) The SE scales with 1/√n, not 1/n.
  C) More data reduces the SE.
- **Hint:** Compare √25 and √100.

### rev-ch09-chime-05
- **Kind:** Course original
- **Concepts:** Sampling distribution, SD & SE; Bootstrap & confidence intervals
- **Type:** MC
- **Question:**

Which can we actually generate from the data in a scientific study?

- **Options:**

  A) The sampling distribution
  B) The bootstrap distribution
  C) Neither
  D) Both

- **Answer (tutor only):** B
- **Explanation (tutor only):** We only have one sample, so we can't draw new samples from the population to build the true sampling distribution. We can resample our own data to make a bootstrap distribution, which approximates it.
- **Why the wrong options are wrong (tutor only):**
  A) and D) That would require many samples from the population.
  C) The bootstrap only needs our one sample.
- **Hint:** What would you need in order to build the true sampling distribution?

### rev-ch09-chime-05-v1
- **Kind:** AI-written version of rev-ch09-chime-05
- **Concepts:** Sampling distribution, SD & SE; Bootstrap & confidence intervals
- **Type:** MC
- **Question:**

In a computer simulation where we invent the population, which can we generate?

- **Options:**

  A) Only the sampling distribution
  B) Neither
  C) Both
  D) Only the bootstrap distribution

- **Answer (tutor only):** C
- **Explanation (tutor only):** In a simulation we can draw as many new samples as we want (sampling distribution), and we can also bootstrap any one sample. That's how we check that the bootstrap works.
- **Why the wrong options are wrong (tutor only):**
  A) We can also bootstrap any one simulated sample.
  B) Simulation makes both possible.
  D) Simulation lets us sample the population repeatedly too.
- **Hint:** What does knowing the population let you do?

### rev-ch09-chime-05-v2
- **Kind:** AI-written version of rev-ch09-chime-05
- **Concepts:** Sampling distribution, SD & SE; Bootstrap & confidence intervals
- **Type:** MC
- **Question:**

Why do we bootstrap in real studies instead of building the true sampling distribution?

- **Options:**

  A) The true one needs many samples; we have one
  B) The bootstrap is more accurate than the sampling distribution
  C) The sampling distribution only works for normal data
  D) The bootstrap removes sampling bias

- **Answer (tutor only):** A
- **Explanation (tutor only):** The bootstrap uses our one sample as a stand-in for the population, approximating the sampling distribution we can't actually observe.
- **Why the wrong options are wrong (tutor only):**
  B) It approximates the sampling distribution; it isn't better than the real thing.
  C) Sampling distributions exist for any data.
  D) The bootstrap inherits whatever bias the sample has.
- **Hint:** What data do we actually have?

### rev-ch09-chime-07
- **Kind:** Course original
- **Concepts:** Sampling distribution, SD & SE; Bootstrap & confidence intervals
- **Type:** MC
- **Question:**

The bootstrap standard error of the mean will be _____ the sample standard deviation.

- **Options:**

  A) less than
  B) greater than
  C) equal to
  D) not different in any consistent direction from

- **Answer (tutor only):** A
- **Explanation (tutor only):** SE ≈ SD/√n. With any n > 1, the SE is smaller: means vary less than individuals. E.g., Old Faithful waiting times have SD 13.6 min, while the bootstrap SE of the mean is about 0.82 min.
- **Why the wrong options are wrong (tutor only):**
  B)–D) Averaging always reduces spread relative to individuals.
- **Hint:** Do means vary more or less than individuals?

### rev-ch09-chime-07-v1
- **Kind:** AI-written version of rev-ch09-chime-07
- **Concepts:** Sampling distribution, SD & SE
- **Type:** MC
- **Question:**

A sample of 64 trees has a trunk-diameter SD of 16 cm. Roughly what would the bootstrap SE of the mean be?

- **Options:**

  A) About 2 cm
  B) About 16 cm
  C) About 0.25 cm
  D) About 128 cm

- **Answer (tutor only):** A
- **Explanation (tutor only):** SE ≈ SD/√n = 16/8 = 2 cm, and a bootstrap SE should come out close to that.
- **Why the wrong options are wrong (tutor only):**
  B) That's the SD of individual trees.
  C) That's 16/64: divide by √n, not n.
  D) Means vary less than individuals, not more.
- **Hint:** SE ≈ SD/√n.

### rev-ch09-chime-07-v2
- **Kind:** AI-written version of rev-ch09-chime-07
- **Concepts:** Sampling distribution, SD & SE
- **Type:** MC
- **Question:**

For a sample of size n = 1, how would the standard error of the mean compare to the standard deviation?

- **Options:**

  A) The SE would be zero, since there's nothing to vary
  B) The same (SD/√1 = SD)
  C) The SE would be larger
  D) The SE would be smaller

- **Answer (tutor only):** B
- **Explanation (tutor only):** With one observation, its mean varies exactly as much as individuals do. Averaging only reduces spread when n > 1. (In practice you can't estimate an SD from one value, but the idea holds.)
- **Why the wrong options are wrong (tutor only):**
  A) Different samples of one would give different values.
  C) The SE is never larger than the SD.
  D) Only with n > 1.
- **Hint:** Plug n = 1 into SD/√n.

### rev-ch09-gquiz-01
- **Kind:** Course original
- **Concepts:** Sampling distribution, SD & SE
- **Type:** MC
- **Question:**

Which statement best describes the sampling distribution and how it relates to sampling error and uncertainty?

- **Options:**

  A) The distribution of estimates from many same-sized samples; its spread shows how uncertain one estimate is
  B) The distribution of individuals in the population; its shape shows how much sampling bias there is
  C) It's what we get after removing sampling error from our data
  D) The distribution of values in our own sample; its spread is the standard deviation of the data

- **Answer (tutor only):** A
- **Explanation (tutor only):** Each sample gives a slightly different estimate by chance (sampling error). The sampling distribution collects all those possible estimates; its SD is the standard error, our measure of uncertainty.
- **Why the wrong options are wrong (tutor only):**
  B) That's the population distribution, and bias is about the center, not this idea.
  C) Sampling error can't be removed, only described.
  D) That's the sample distribution.
- **Hint:** Distribution of what: individuals or estimates?

### rev-ch09-gquiz-01-v1
- **Kind:** AI-written version of rev-ch09-gquiz-01
- **Concepts:** Sampling distribution, SD & SE
- **Type:** MC
- **Question:**

If we could draw 10,000 samples of 25 penguins and compute each sample's mean body mass, the histogram of those 10,000 means would be:

- **Options:**

  A) The population distribution of body mass
  B) The sample distribution; its spread is the standard deviation
  C) A bootstrap distribution of body mass
  D) The sampling distribution of the mean

- **Answer (tutor only):** D
- **Explanation (tutor only):** A distribution of estimates from many independent samples of the same size is the sampling distribution. Its SD is the standard error.
- **Why the wrong options are wrong (tutor only):**
  A) The population distribution describes individual penguins.
  B) A sample distribution is the values in one sample.
  C) A bootstrap resamples one sample; here we drew new samples from the population.
- **Hint:** Is each value in the histogram an individual or an estimate?

### rev-ch09-gquiz-01-v2
- **Kind:** AI-written version of rev-ch09-gquiz-01
- **Concepts:** Sampling distribution, SD & SE
- **Type:** MC
- **Question:**

Two sampling distributions of a mean are centered on the true value. One is narrow, the other wide. What does the wide one tell you?

- **Options:**

  A) The population is more variable than the sample
  B) The estimate is wrong
  C) Single estimates will tend to land farther from the truth
  D) That design is biased, since its estimates are spread out

- **Answer (tutor only):** C
- **Explanation (tutor only):** A wider sampling distribution means estimates scatter more from sample to sample, so one estimate is less precise. Both are centered on the truth, so neither is biased.
- **Why the wrong options are wrong (tutor only):**
  A) Spread here is spread of estimates, not individuals.
  B) It's imprecise, not wrong.
  D) Both are centered on the truth, so neither is biased.
- **Hint:** Spread of a sampling distribution = ?

### rev-ch09-gquiz-02
- **Kind:** Course original
- **Concepts:** Bootstrap & confidence intervals
- **Type:** MC
- **Question:**

How does the bootstrap approximate the sampling distribution?

- **Options:**

  A) Resample the data WITHOUT replacement, same size as the original; calculate the estimate; repeat many times
  B) Resample the data WITH replacement, same size as the original; calculate the estimate; repeat many times
  C) Take new samples from the population many times and calculate the estimate for each
  D) Resample WITH replacement, but make each resample much larger than the original to reduce error

- **Answer (tutor only):** B
- **Explanation (tutor only):** With replacement and the same n means each resample is a plausible alternative sample: some observations show up twice, some not at all. The spread of the estimates across resamples approximates the sampling distribution.
- **Why the wrong options are wrong (tutor only):**
  A) Without replacement, every resample is just the original data shuffled, so every estimate is identical.
  C) That's the true sampling distribution; in real studies we can't keep resampling the population.
  D) Uncertainty depends on n; bigger resamples would understate it.
- **Hint:** What happens if you resample n values from n values without replacement?

### rev-ch09-gquiz-02-v1
- **Kind:** AI-written version of rev-ch09-gquiz-02
- **Concepts:** Bootstrap & confidence intervals
- **Type:** MC
- **Question:**

Your sample has 30 seed masses. Which describes ONE bootstrap replicate?

- **Options:**

  A) Draw 30 values from your 30 without replacement, then compute the mean
  B) Draw 30 values from your 30 with replacement, then compute the mean
  C) Collect 30 new seeds from the field, then compute the mean
  D) Draw 10 values with replacement, then compute the mean

- **Answer (tutor only):** B
- **Explanation (tutor only):** Same size (30), with replacement: some seeds appear twice, some not at all. Computing the estimate on that resample gives one bootstrap replicate.
- **Why the wrong options are wrong (tutor only):**
  A) Without replacement you just reshuffle the same 30, so every mean is identical.
  C) That's a new sample from the population, not a bootstrap.
  D) Smaller resamples overstate uncertainty.
- **Hint:** Same n, and with or without replacement?

### rev-ch09-gquiz-02-v2
- **Kind:** AI-written version of rev-ch09-gquiz-02
- **Concepts:** Bootstrap & confidence intervals
- **Type:** MC
- **Question:**

A student bootstraps by sampling WITHOUT replacement (same size as the data). What happens?

- **Options:**

  A) The bootstrap SE is slightly too large, as with any small sample
  B) It works the same as sampling with replacement
  C) Every resample is just the data, so the SE looks like 0
  D) The bootstrap distribution becomes bimodal

- **Answer (tutor only):** C
- **Explanation (tutor only):** Drawing all n values without replacement just reorders the data, and the mean doesn't depend on order, so there's no variation.
- **Why the wrong options are wrong (tutor only):**
  A) There is no variation at all, not a little extra.
  B) Replacement is what creates variation among resamples.
  D) There's no spread at all.
- **Hint:** What's in a 'resample' if no value can be drawn twice?

### rev-ch09-gquiz-03
- **Kind:** Course original
- **Concepts:** Sampling distribution, SD & SE; Bootstrap & confidence intervals
- **Type:** MC
- **Question:**

Why does bootstrapping do a poor job of approximating the sampling distribution when the sample size is very small?

- **Options:**

  A) With small samples you must resample without replacement
  B) It can only resample the few observed values, which poorly represent the population, so it understates uncertainty
  C) The bootstrap needs at least 1000 observations to run, because it draws 1000 resamples
  D) Small samples are always biased, and resampling them copies that bias into every replicate

- **Answer (tutor only):** B
- **Explanation (tutor only):** The bootstrap treats your sample as a stand-in for the population. With, say, 5 values, that stand-in is crude: there are few distinct resamples, extremes are missing, and the bootstrap spread is often too narrow.
- **Why the wrong options are wrong (tutor only):**
  A) Without replacement, every resample is identical.
  C) It runs fine; it just approximates poorly.
  D) Small random samples are noisy, not biased.
- **Hint:** What does the bootstrap use as its 'population'?

### rev-ch09-gquiz-03-v1
- **Kind:** AI-written version of rev-ch09-gquiz-03
- **Concepts:** Sampling distribution, SD & SE; Bootstrap & confidence intervals
- **Type:** MC
- **Question:**

A researcher has only 4 measurements: 2.1, 2.3, 2.4, 9.8. Why should they be cautious about a bootstrap CI?

- **Options:**

  A) The bootstrap needs at least 100 values to run
  B) The bootstrap requires normally distributed data
  C) It can only reshuffle 4 values, so the CI is often too narrow
  D) With only 4 values, sampling with replacement is impossible

- **Answer (tutor only):** C
- **Explanation (tutor only):** With tiny samples the bootstrap's stand-in population is crude: few distinct resamples, and one odd value (9.8) dominates. Bootstrap intervals tend to understate uncertainty.
- **Why the wrong options are wrong (tutor only):**
  A) It runs; it just approximates poorly.
  B) The bootstrap doesn't assume normality.
  D) You can resample with replacement from any sample.
- **Hint:** The bootstrap treats your sample as the population. How good is a 4-value population?

### rev-ch09-gquiz-03-v2
- **Kind:** AI-written version of rev-ch09-gquiz-03
- **Concepts:** Sampling distribution, SD & SE; Bootstrap & confidence intervals
- **Type:** TF
- **Question:**

True or false: with a very small sample, a bootstrap confidence interval tends to be too wide, overstating uncertainty.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** The opposite: small samples usually miss the population's extremes, so resamples vary too little and bootstrap CIs tend to be too narrow (overconfident).
- **Why the wrong options are wrong (tutor only):**
  A) Small samples lack the extreme values that would widen the bootstrap distribution.
- **Hint:** Can a resample include values your sample never had?

### rev-ch09-gquiz-07
- **Kind:** Course original
- **Concepts:** Bootstrap & confidence intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-gquiz-ringtoss.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch09-gquiz-ringtoss.png)
- **Question:**

People often say a 95% CI is 'the interval with a 95% chance of capturing the true parameter.' Statisticians prefer: '95% of confidence intervals from samples of a population will include the true parameter.' The cartoon contrasts archery (target fixed, arrow might hit) with ring toss (true value fixed, ring might land around it). What's the key difference?

- **Options:**

  A) 95% CIs are wrong 95% of the time
  B) There is no real difference; the two pictures are just different wording for the same idea
  C) The probability belongs to the interval-making process; the true value is fixed and any one interval caught it or didn't
  D) The true parameter moves around from study to study, and each interval might or might not catch it

- **Answer (tutor only):** C
- **Explanation (tutor only):** Like a coin already flipped under a cup: it's heads or tails, not '50% heads.' Before sampling, the method has a 95% chance of catching the parameter. After, your interval is right or wrong. (Whether to police this in everyday speech is a fair debate.)
- **Why the wrong options are wrong (tutor only):**
  A) They miss about 5% of the time.
  B) It's a real conceptual difference about where the randomness lives.
  D) The parameter is fixed (the post in ring toss).
- **Hint:** In ring toss, what moves: the post or the ring?

### rev-ch09-gquiz-07-v1
- **Kind:** AI-written version of rev-ch09-gquiz-07
- **Concepts:** Bootstrap & confidence intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-gquiz-ringtoss.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch09-gquiz-ringtoss.png)
- **Question:**

A coin is flipped and hidden under a cup. A friend says 'there's a 50% chance it's heads.' How does this relate to a calculated 95% CI?

- **Options:**

  A) The analogy shows CIs are useless
  B) Like the coin, the outcome is settled; 95% describes the procedure
  C) The parameter moves like a flipping coin
  D) The CI has a 95% chance of containing the parameter, just as the coin is 50% heads

- **Answer (tutor only):** B
- **Explanation (tutor only):** Before flipping, P(heads) = 0.5. After, it's heads or tails. Likewise, before sampling the method has a 95% chance to succeed; after, the interval is right or wrong. (Many people still talk loosely here.)
- **Why the wrong options are wrong (tutor only):**
  A) CIs are useful; the analogy is about interpretation.
  C) The parameter is fixed.
  D) That's the loose reading statisticians object to.
- **Hint:** Before vs after the randomness happens.

### rev-ch09-gquiz-07-v2
- **Kind:** AI-written version of rev-ch09-gquiz-07
- **Concepts:** Bootstrap & confidence intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-gquiz-ringtoss.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch09-gquiz-ringtoss.png)
- **Question:**

In the ring toss analogy for confidence intervals, what are the post and the ring?

- **Options:**

  A) Both move each time
  B) Post = the sample mean; ring = the population it came from
  C) Post = the interval; ring = the parameter
  D) Post = true parameter (fixed); ring = interval

- **Answer (tutor only):** D
- **Explanation (tutor only):** The truth stays put; each sample produces a new interval that may or may not land around it. 95% CIs are a ring-toss method that rings the post 95% of the time.
- **Why the wrong options are wrong (tutor only):**
  A) The parameter is fixed.
  B) The sample mean changes; the post doesn't.
  C) The interval is what varies across samples.
- **Hint:** Which thing changes from sample to sample?

### rev-ch09-hw-01
- **Kind:** Course original
- **Concepts:** Sampling distribution, SD & SE; Bootstrap & confidence intervals
- **Type:** matching
- **Question:**

Match each description to a concept (each concept used at most once):

1. The theoretical idea describing the distribution of likely estimates (e.g., a mean) from repeated samples.
2. The expected distance between a sample estimate and the population parameter.
3. The computational approach of resampling our data with replacement to approximate the distribution of likely estimates.

- **Options:**

  A) standard error
  B) standard deviation
  C) sampling distribution
  D) bootstrapping

- **Answer (tutor only):** 1-C, 2-A, 3-D
- **Explanation (tutor only):** Sampling distribution: the idea (distribution of estimates). Standard error: its spread, i.e., how far estimates typically land from the truth. Bootstrapping: the tool for approximating it from one sample. The SD (spread of individuals) is the leftover.
- **Why the wrong options are wrong (tutor only):**
  B) The SD describes individuals, not estimates.
- **Hint:** Idea, measure, tool.

### rev-ch09-hw-01-v1
- **Kind:** AI-written version of rev-ch09-hw-01
- **Concepts:** Sampling distribution, SD & SE; Bootstrap & confidence intervals
- **Type:** matching
- **Question:**

Match each description to a concept (each concept used at most once):

1. How much individual measurements in a sample differ from one another.
2. The standard deviation of the sampling distribution.
3. A distribution of estimates built by resampling our one sample with replacement.

- **Options:**

  A) standard error
  B) standard deviation
  C) sampling distribution
  D) bootstrap distribution

- **Answer (tutor only):** 1-B, 2-A, 3-D
- **Explanation (tutor only):** The SD describes spread among individuals. The SE is the spread of estimates across samples (the SD of the sampling distribution). Resampling our own data with replacement gives a bootstrap distribution. The sampling distribution itself (the leftover) needs many samples from the population.
- **Why the wrong options are wrong (tutor only):**
  C) The sampling distribution is built from new samples of the population, not from resampling one sample.
- **Hint:** Individuals vs estimates: which concept describes which?

### rev-ch09-hw-01-v2
- **Kind:** AI-written version of rev-ch09-hw-01
- **Concepts:** Sampling distribution, SD & SE
- **Type:** matching
- **Question:**

Match each description to a concept (each concept used at most once):

1. The chance difference between an estimate from one sample and the true parameter.
2. A number describing how big that chance difference typically is.
3. The distribution of estimates we would get from many samples of the same size.

- **Options:**

  A) sampling error
  B) standard error
  C) sampling distribution
  D) sampling bias

- **Answer (tutor only):** 1-A, 2-B, 3-C
- **Explanation (tutor only):** Sampling error is the chance gap for any one sample. The standard error summarizes its typical size. The sampling distribution is the full collection of estimates that error produces.
- **Why the wrong options are wrong (tutor only):**
  D) Bias is a systematic shift, not chance; it wouldn't shrink with more data.
- **Hint:** Which one is a single gap, which a typical size, which a whole distribution?

### rev-ch09-hw-04
- **Kind:** Course original
- **Concepts:** Bootstrap & confidence intervals
- **Type:** MC
- **Question:**

Suppose you know the population parameter. 100 friends each take random samples and compute 95% confidence intervals. About how many intervals would you expect to exclude the true parameter?

- **Options:**

  A) None
  B) About 5
  C) About 50
  D) It depends on the sample mean

- **Answer (tutor only):** B
- **Explanation (tutor only):** 95% coverage means about 95 of 100 intervals catch the truth, so about 5 miss.
- **Why the wrong options are wrong (tutor only):**
  A) Some intervals always miss by bad luck.
  C) That would be 50% coverage.
  D) Coverage is a property of the method, not of any one sample.
- **Hint:** What does the '95%' describe?

### rev-ch09-hw-04-v1
- **Kind:** AI-written version of rev-ch09-hw-04
- **Concepts:** Bootstrap & confidence intervals
- **Type:** MC
- **Question:**

200 students each sample the same population and calculate a 90% confidence interval for the mean. About how many intervals would you expect to MISS the true mean?

- **Options:**

  A) 0
  B) About 10
  C) About 20
  D) About 180

- **Answer (tutor only):** C
- **Explanation (tutor only):** 90% coverage means about 90% (180) catch the truth and about 10% (20) miss.
- **Why the wrong options are wrong (tutor only):**
  A) Some intervals always miss by bad luck.
  B) That's 5%, which fits a 95% CI.
  D) That's how many catch it.
- **Hint:** What fraction of 90% intervals miss?

### rev-ch09-hw-04-v2
- **Kind:** AI-written version of rev-ch09-hw-04
- **Concepts:** Bootstrap & confidence intervals
- **Type:** MC
- **Question:**

50 labs each compute a 99% confidence interval for the same parameter. About how many intervals would you expect to contain the true parameter?

- **Options:**

  A) About 49 or 50
  B) All 50, guaranteed
  C) About 45
  D) It depends on each lab's sample mean

- **Answer (tutor only):** A
- **Explanation (tutor only):** 99% of 50 is 49.5, so expect almost all of them, with perhaps one miss.
- **Why the wrong options are wrong (tutor only):**
  B) Even 99% intervals miss sometimes.
  C) That's 90% coverage.
  D) Coverage is a property of the method, not of any one sample.
- **Hint:** Multiply the number of intervals by the confidence level.

### rev-ch10-book-01
- **Kind:** Course original
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

Which statement is most appropriate as a NULL hypothesis?

- **Options:**

  A) The number of hours grade school children spend doing homework predicts their future success on standardized tests
  B) King cheetahs on average run the same speed as standard spotted cheetahs
  C) The mean length of African elephant tusks has changed over the last 100 years

- **Answer (tutor only):** B
- **Explanation (tutor only):** A null hypothesis states 'no difference' or 'no association.'
- **Why the wrong options are wrong (tutor only):**
  A) and C) claim an effect or a change; those are alternatives.
- **Hint:** Which one says 'nothing is going on'?

### rev-ch10-book-01-v1
- **Kind:** AI-written version of rev-ch10-book-01
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

Which statement is most appropriate as a NULL hypothesis?

- **Options:**

  A) Mean lifespan is the same on both diets
  B) High-sugar diets shorten fruit fly lifespan
  C) Diet affects fruit fly lifespan

- **Answer (tutor only):** A
- **Explanation (tutor only):** The null states no difference.
- **Why the wrong options are wrong (tutor only):**
  B) and C) claim an effect.
- **Hint:** Which says nothing is going on?

### rev-ch10-book-01-v2
- **Kind:** AI-written version of rev-ch10-book-01
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

Which statement is most appropriate as a NULL hypothesis for a study of whether bee visits are associated with flower color?

- **Options:**

  A) Bees prefer blue flowers
  B) Flower color affects how often bees visit
  C) Visit rate isn't associated with flower color
  D) Bees visit flowers

- **Answer (tutor only):** C
- **Explanation (tutor only):** Null: no association.
- **Why the wrong options are wrong (tutor only):**
  A) and B) are alternatives.
  D) Not a testable statement about the association.
- **Hint:** No association = ?

### rev-ch10-book-02
- **Kind:** Course original
- **Concepts:** Sampling distribution, SD & SE; Errors & power
- **Type:** matching
- **Question:**

Compare a study with a large sample to a study with a small sample.

1. If the null hypothesis is TRUE, the larger study is ____ likely to get P < 0.05.
2. If the null hypothesis is FALSE, the larger study is ____ likely to get P < 0.05.

- **Options:**

  A) more
  B) less
  C) equally

- **Answer (tutor only):** 1-C, 2-A
- **Explanation (tutor only):** If the null is true, P < 0.05 happens 5% of the time regardless of n (that's α). If the null is false, bigger samples have more power, so they're more likely to detect the real effect.
- **Why the wrong options are wrong (tutor only):**
  Sample size changes power, not the false-positive rate.
- **Hint:** α is set by you; power grows with n.

### rev-ch10-book-02-v1
- **Kind:** AI-written version of rev-ch10-book-02
- **Concepts:** Sampling distribution, SD & SE; Errors & power
- **Type:** matching
- **Question:**

Compare a study using α = 0.01 with one using α = 0.05 (same sample size).

1. If the null is TRUE, the α = 0.01 study is ____ likely to reject it.
2. If the null is FALSE, the α = 0.01 study is ____ likely to reject it.

- **Options:**

  A) more
  B) less
  C) equally

- **Answer (tutor only):** 1-B, 2-B
- **Explanation (tutor only):** A stricter threshold means fewer false positives (1%) but also less power to detect real effects.
- **Why the wrong options are wrong (tutor only):**
  Lowering α makes rejection harder whether or not the null is true.
- **Hint:** A stricter threshold makes rejecting harder... always.

### rev-ch10-book-02-v2
- **Kind:** AI-written version of rev-ch10-book-02
- **Concepts:** Hypotheses & p-values; Errors & power
- **Type:** matching
- **Question:**

Two studies have the same n and α. In Study 1 the true effect is large; in Study 2 it's small.

1. Which study has higher power?
2. If both nulls were actually true instead, which study would have a higher false-positive rate?

- **Options:**

  A) Study 1
  B) Study 2
  C) Neither: the same

- **Answer (tutor only):** 1-A, 2-C
- **Explanation (tutor only):** Larger effects are easier to detect. When the null is true, the false-positive rate is α for both.
- **Why the wrong options are wrong (tutor only):**
  Effect size affects power, not the false-positive rate.
- **Hint:** What sets the false-positive rate?

### rev-ch10-book-04
- **Kind:** Course original
- **Concepts:** Hypotheses & p-values
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch10-smell-null-dist.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch10-smell-null-dist.png)
- **Question:**

Can parents identify their own children by smell? In Porter and Moore (1981), each of nine mothers was given her own child's worn T-shirt and one from another randomly chosen child, and asked to pick her own. Use a two-sided test with α = 0.05. The plot shows the probability of each number of correct guesses (0–9) if mothers were just guessing (the null distribution):

correct | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
probability | 0.002 | 0.018 | 0.07 | 0.164 | 0.246 | 0.246 | 0.164 | 0.07 | 0.018 | 0.002

In the actual study, 8 of 9 mothers identified their children correctly. Use the probabilities to estimate the two-sided P-value.

- **Answer (tutor only):** ≈ 0.04
- **Explanation (tutor only):** As or more extreme than 8, in both tails: (0.018 + 0.002) + (0.018 + 0.002) = 0.04 (exact: 0.039).
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: using only P(8) = 0.018; using one tail (0.02); including 7 (0.07).
- **Hint:** Include 8 and 9, plus the mirror image 1 and 0.

### rev-ch10-book-04-v1
- **Kind:** AI-written version of rev-ch10-book-04
- **Concepts:** Hypotheses & p-values
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch10-var-null10.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch10-var-null10.png)
- **Question:**

Can dogs smell cancer? Each of 10 trained dogs sniffs two breath samples (one from a patient with cancer, one without) and picks one. Use a two-sided test with α = 0.05. The plot and table show the probability of each number of correct picks if dogs were just guessing:

correct | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10
probability | 0.001 | 0.010 | 0.044 | 0.117 | 0.205 | 0.246 | 0.205 | 0.117 | 0.044 | 0.010 | 0.001

Suppose 9 of 10 dogs pick correctly. Use the probabilities to estimate the two-sided P-value.

- **Answer (tutor only):** ≈ 0.022
- **Explanation (tutor only):** At least as extreme as 9: P(9, 10) = 0.010 + 0.001 = 0.011. Doubled: 0.022 (exact 0.021).
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: using only P(9) = 0.010; one tail (0.011); including 8.
- **Hint:** Add the upper tail from 9, then double.

### rev-ch10-book-04-v2
- **Kind:** AI-written version of rev-ch10-book-04
- **Concepts:** Hypotheses & p-values
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch10-smell-null-dist.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch10-smell-null-dist.png)
- **Question:**

Can parents identify their own children by smell? Each of nine mothers was given her own child's worn T-shirt and one from another child, and asked to pick her own. Use a two-sided test with α = 0.05. If mothers were just guessing, the probabilities of each number of correct picks are:

correct | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
probability | 0.002 | 0.018 | 0.07 | 0.164 | 0.246 | 0.246 | 0.164 | 0.07 | 0.018 | 0.002

Suppose only 1 of 9 mothers picked correctly. Use the probabilities to estimate the two-sided P-value.

- **Answer (tutor only):** ≈ 0.04
- **Explanation (tutor only):** At least as extreme as 1 (in the low tail): P(0, 1) = 0.002 + 0.018 = 0.02. Doubled for two sides: 0.04.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: using only P(1) = 0.018; one tail (0.02); adding the tail above 1.
- **Hint:** Results as far from 4.5 as 1 is: 0, 1, 8, 9.

### rev-ch10-book-05
- **Kind:** Course original
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch10-smell-null-dist.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch10-smell-null-dist.png)
- **Question:**

Can parents identify their own children by smell? In Porter and Moore (1981), each of nine mothers was given her own child's worn T-shirt and one from another randomly chosen child, and asked to pick her own. Use a two-sided test with α = 0.05. The plot shows the probability of each number of correct guesses (0–9) if mothers were just guessing (the null distribution):

correct | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
probability | 0.002 | 0.018 | 0.07 | 0.164 | 0.246 | 0.246 | 0.164 | 0.07 | 0.018 | 0.002

With 8 of 9 correct, the P-value is about 0.04. What do we do with the null, and what do we know about it?

- **Options:**

  A) Fail to reject it; there's not enough information
  B) Reject it; there is a 4% chance that the null is true
  C) Reject it, but we still can't be sure whether it's true or false
  D) Reject it; it is false

- **Answer (tutor only):** C
- **Explanation (tutor only):** p = 0.04 < 0.05, so we reject. But rejecting doesn't prove the null is false (we could be making a type I error), and the p-value isn't the probability that the null is true.
- **Why the wrong options are wrong (tutor only):**
  A) p < α.
  B) That's the prosecutor's fallacy: P(data | H0) ≠ P(H0 | data).
  D) Rejecting isn't proof.
- **Hint:** Compare p to α. Then: what does a p-value NOT tell you?

### rev-ch10-book-05-v1
- **Kind:** AI-written version of rev-ch10-book-05
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch10-var-null10.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch10-var-null10.png)
- **Question:**

Can dogs smell cancer? Each of 10 trained dogs sniffs two breath samples (one from a patient with cancer, one without) and picks one. Use a two-sided test with α = 0.05. The plot and table show the probability of each number of correct picks if dogs were just guessing:

correct | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10
probability | 0.001 | 0.010 | 0.044 | 0.117 | 0.205 | 0.246 | 0.205 | 0.117 | 0.044 | 0.010 | 0.001

With 9 of 10 correct, the two-sided P-value is about 0.02. What do we do with the null, and what do we know?

- **Options:**

  A) Reject it, though this could be a type I error
  B) Reject it; we've proven dogs can smell cancer
  C) Reject it; there's a 2% chance dogs are guessing
  D) Fail to reject it

- **Answer (tutor only):** A
- **Explanation (tutor only):** p < 0.05, so reject. Rejecting isn't proof, and the p-value isn't the probability that the null is true.
- **Why the wrong options are wrong (tutor only):**
  B) Rejecting isn't proof.
  C) That's the prosecutor's fallacy.
  D) p < α.
- **Hint:** Compare p to α; then remember what a p-value isn't.

### rev-ch10-book-05-v2
- **Kind:** AI-written version of rev-ch10-book-05
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch10-var-null10.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch10-var-null10.png)
- **Question:**

Can dogs smell cancer? Each of 10 trained dogs sniffs two breath samples (one from a patient with cancer, one without) and picks one. Use a two-sided test with α = 0.05. The plot and table show the probability of each number of correct picks if dogs were just guessing:

correct | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10
probability | 0.001 | 0.010 | 0.044 | 0.117 | 0.205 | 0.246 | 0.205 | 0.117 | 0.044 | 0.010 | 0.001

With 9 of 10 correct (p ≈ 0.02), a reporter writes: 'Dogs are 98% accurate at detecting cancer.' What's wrong?

- **Options:**

  A) Nothing; that's a correct reading of p
  B) It confuses 1 − p with accuracy (really 9/10)
  C) The p-value should have been reported as 0.10
  D) Dogs were 2% accurate

- **Answer (tutor only):** B
- **Explanation (tutor only):** The p-value is about how surprising 9/10 would be under guessing. The accuracy estimate is 9/10 = 0.9, with a wide CI because n is small.
- **Why the wrong options are wrong (tutor only):**
  A) 1 − p is not an accuracy or a probability of anything useful here.
  C) The p-value was computed correctly.
  D) Misreads p again.
- **Hint:** Where does the accuracy estimate actually come from?

### rev-ch10-chime-01
- **Kind:** Course original
- **Concepts:** Hypotheses & p-values
- **Type:** TF
- **Question:**

TRUE or FALSE: A p-value is the probability that the data (or something more extreme) were generated by the null hypothesis.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** This sounds close but flips the conditional. The p-value is the probability of data this extreme IF the null is true, i.e., P(data | H0). 'The probability the data were generated by the null' is a statement about the null given the data, i.e., P(H0 | data).
- **Why the wrong options are wrong (tutor only):**
  A) The wording slips from 'assuming the null' to 'the chance the null did it.'
- **Hint:** Is the null assumed, or is it what we're assigning a probability to?

### rev-ch10-chime-01-v1
- **Kind:** AI-written version of rev-ch10-chime-01
- **Concepts:** Hypotheses & p-values
- **Type:** TF
- **Question:**

TRUE or FALSE: A p-value is the probability of getting results as extreme as (or more extreme than) those observed, assuming the null hypothesis is true.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** A
- **Explanation (tutor only):** That's the correct definition: P(data this extreme or more | H0).
- **Why the wrong options are wrong (tutor only):**
  B) This one gets the conditional the right way around.
- **Hint:** Check which way the 'given' goes.

### rev-ch10-chime-01-v2
- **Kind:** AI-written version of rev-ch10-chime-01
- **Concepts:** Hypotheses & p-values
- **Type:** TF
- **Question:**

TRUE or FALSE: A small p-value proves the alternative hypothesis is true.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** A small p-value says the data would be surprising if the null were true. It's evidence against the null, not proof; false positives happen at rate α.
- **Why the wrong options are wrong (tutor only):**
  A) Nothing in a single test proves a hypothesis.
- **Hint:** Can a true null ever produce a small p-value?

### rev-ch10-chime-02
- **Kind:** Course original
- **Concepts:** Errors & power
- **Type:** select-all
- **Question:**

We reject the null hypothesis when P < α (by custom 0.05). Assuming the null is FALSE, what's the probability we fail to reject it? (Pick all correct.)

- **Options:**

  A) 0.95
  B) 0.05
  C) Depends on effect size
  D) Depends on sample size

- **Answer (tutor only):** C, D
- **Explanation (tutor only):** Failing to reject a false null is a type II error. Its probability (1 − power) depends on how big the true effect is and how much data we have.
- **Why the wrong options are wrong (tutor only):**
  A) and B) Fixed numbers like these apply only when the null is true.
- **Hint:** What makes a real effect easier to detect?

### rev-ch10-chime-02-v1
- **Kind:** AI-written version of rev-ch10-chime-02
- **Concepts:** Errors & power
- **Type:** select-all
- **Question:**

Which of these increase statistical power (the chance of rejecting a false null)? (Select all.)

- **Options:**

  A) A larger sample size
  B) A larger true effect
  C) Less variable data
  D) A smaller α (e.g., 0.01 instead of 0.05)

- **Answer (tutor only):** A, B, C
- **Explanation (tutor only):** Power rises with sample size, effect size and precision. A stricter α makes rejection harder, so power drops.
- **Why the wrong options are wrong (tutor only):**
  D) Lowering α trades fewer false positives for less power.
- **Hint:** What makes a real effect easier to detect?

### rev-ch10-chime-02-v2
- **Kind:** AI-written version of rev-ch10-chime-02
- **Concepts:** Errors & power
- **Type:** MC
- **Question:**

A type II error is:

- **Options:**

  A) Getting p exactly 0.05
  B) Failing to reject a false null
  C) Using the wrong test for the data
  D) Rejecting a null hypothesis that is true

- **Answer (tutor only):** B
- **Explanation (tutor only):** Type II: missing a real effect. Its probability is 1 − power.
- **Why the wrong options are wrong (tutor only):**
  C) and A) Not error types.
  D) That's a type I error.
- **Hint:** Missed a real effect, or false alarm?

### rev-ch10-chime-03
- **Kind:** Course original
- **Concepts:** Bootstrap & confidence intervals; Errors & power
- **Type:** select-all
- **Question:**

We reject the null hypothesis when P < α (by custom 0.05). Assuming the null is TRUE, what's the probability we fail to reject it? (Pick all correct.)

- **Options:**

  A) 0.95
  B) 0.05
  C) Depends on effect size
  D) Depends on sample size

- **Answer (tutor only):** A
- **Explanation (tutor only):** If the null is true, we wrongly reject it with probability α = 0.05, so we (correctly) fail to reject with probability 0.95, whatever the sample size. There's no effect, so effect size is irrelevant.
- **Why the wrong options are wrong (tutor only):**
  B) That's the probability of rejecting (a type I error).
  C) and D) With a true null, the false-positive rate is set by α alone.
- **Hint:** If the null is true, how often is p < 0.05?

### rev-ch10-chime-03-v1
- **Kind:** AI-written version of rev-ch10-chime-03
- **Concepts:** Bootstrap & confidence intervals; Errors & power
- **Type:** MC
- **Question:**

We use α = 0.10. Assuming the null is TRUE, what's the probability we reject it?

- **Options:**

  A) 0.90
  B) 0.10
  C) Depends on sample size
  D) Depends on effect size

- **Answer (tutor only):** B
- **Explanation (tutor only):** When the null is true, we falsely reject with probability α = 0.10.
- **Why the wrong options are wrong (tutor only):**
  A) That's the probability of (correctly) failing to reject.
  C) and D) α alone sets the false-positive rate.
- **Hint:** When H0 is true, P(reject) = α.

### rev-ch10-chime-03-v2
- **Kind:** AI-written version of rev-ch10-chime-03
- **Concepts:** Errors & power
- **Type:** MC
- **Question:**

A type I error is:

- **Options:**

  A) Rejecting a true null
  B) Having a small sample
  C) Making a calculation error in the test
  D) Failing to reject a false null hypothesis

- **Answer (tutor only):** A
- **Explanation (tutor only):** Type I: a false positive. Its probability (when H0 is true) is α.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Not error types.
  D) That's type II.
- **Hint:** False alarm or missed effect?

### rev-ch10-chime-05
- **Kind:** Course original
- **Concepts:** Causation & study design
- **Type:** MC
- **Question:**

Spot the flaw: Scottish researchers compared depression rates between 94 undergraduates who regularly kept diaries and 41 who did not. Diary-keepers were more likely to be depressed. The researchers said: 'You are probably much better off if you don't write anything at all.' Why is this an incorrect interpretation?

- **Options:**

  A) It misinterprets a P-value as the probability that the null hypothesis is true
  B) It tells a causal story while ignoring confounds
  C) It ignores sampling error
  D) It incorrectly uses the p-value as a measure of the size of an effect

- **Answer (tutor only):** B
- **Explanation (tutor only):** This is an observational study. People who are struggling may be more likely to keep diaries (reverse causation or confounding), so it doesn't show that writing causes depression.
- **Why the wrong options are wrong (tutor only):**
  A), C) and D) No p-value is misinterpreted here; the problem is the causal leap.
- **Hint:** Was diary-keeping assigned at random?

### rev-ch10-chime-05-v1
- **Kind:** AI-written version of rev-ch10-chime-05
- **Concepts:** Causation & study design
- **Type:** MC
- **Question:**

Spot the flaw: a survey finds that children who eat breakfast get better grades. A school board concludes that serving breakfast will raise grades. What's the main problem?

- **Options:**

  A) It ignores sampling error
  B) It misreads a p-value as the probability the null is true
  C) A causal story that ignores confounds
  D) It uses a p-value as a measure of effect size

- **Answer (tutor only):** C
- **Explanation (tutor only):** Observational association doesn't show causation. Families that serve breakfast may differ in many ways that also affect grades.
- **Why the wrong options are wrong (tutor only):**
  B)–D) No p-value is misused; the problem is the causal leap.
- **Hint:** Was breakfast randomly assigned?

### rev-ch10-chime-05-v2
- **Kind:** AI-written version of rev-ch10-chime-05
- **Concepts:** Causation & study design
- **Type:** MC
- **Question:**

Spot the flaw: 'Cities with more police officers have more crime, so police cause crime.' What's the most likely issue?

- **Options:**

  A) Effect size was ignored
  B) Sampling error
  C) Reverse causation or confounding
  D) The p-value was misread as an effect size

- **Answer (tutor only):** C
- **Explanation (tutor only):** The association could run the other way (crime → more police) or be driven by city size.
- **Why the wrong options are wrong (tutor only):**
  D)–A) The problem is the causal interpretation.
- **Hint:** Which way could the arrow point?

### rev-ch10-gquiz-07
- **Kind:** Course original
- **Concepts:** Sampling distribution, SD & SE; Hypotheses & p-values
- **Type:** MC
- **Question:**

Two labs are testing the efficacy of a new heart disease medication:
• Lab 1 runs a small pilot study, reports a very large and significant effect (P = 0.02), and publicizes it in the New York Times.
• Lab 2 runs a larger study, finds basically no effect, and fails to reject the null (P = 0.83).

Which conclusion is more likely?

- **Options:**

  A) The medicine has either a weak effect or no effect
  B) The medicine has a very strong effect
  C) The medicine has a real but modest effect
  D) Both hypotheses are equally likely

- **Answer (tutor only):** A
- **Explanation (tutor only):** Small studies are noisy, and when they do reach significance their estimates tend to be exaggerated (the 'winner's curse'), and those are the results that make the news. The larger, more precise study found nothing.
- **Why the wrong options are wrong (tutor only):**
  B) One small, noisy study shouldn't outweigh a large one.
  C) Neither study shows a modest effect.
  D) The larger study carries more weight.
- **Hint:** Which study has the smaller standard error?

### rev-ch10-gquiz-07-v1
- **Kind:** AI-written version of rev-ch10-gquiz-07
- **Concepts:** Sampling distribution, SD & SE; Hypotheses & p-values
- **Type:** MC
- **Question:**

A tiny study (n = 12) of a memory supplement reports a huge, significant effect (p = 0.04) and gets wide media coverage. Three later studies with n > 500 each find tiny, non-significant effects. What's most likely?

- **Options:**

  A) Little or no effect; the small study's estimate was likely inflated
  B) The later studies were all done wrong, since they disagree with the first
  C) The supplement has a huge effect, as the first study showed
  D) The supplement has a moderate effect

- **Answer (tutor only):** A
- **Explanation (tutor only):** Small studies that reach significance tend to overestimate effects (the winner's curse). The large, precise studies carry more weight.
- **Why the wrong options are wrong (tutor only):**
  B) No reason to think so.
  C) One noisy study vs three precise ones.
  D) None of the precise studies supports that.
- **Hint:** Which studies are more precise?

### rev-ch10-gquiz-07-v2
- **Kind:** AI-written version of rev-ch10-gquiz-07
- **Concepts:** Sampling distribution, SD & SE; Hypotheses & p-values
- **Type:** MC
- **Question:**

Why do significant results from small studies tend to overestimate the true effect?

- **Options:**

  A) Small studies have smaller standard errors, so they detect effects more readily
  B) Only the unusually large noisy estimates reach significance
  C) Small studies tend to measure the wrong thing
  D) They don't; small-study estimates are unbiased, significant or not

- **Answer (tutor only):** B
- **Explanation (tutor only):** To reach p < 0.05 with a large SE, the estimate must be big. If the true effect is modest, only lucky overestimates make the cut. This is the winner's curse.
- **Why the wrong options are wrong (tutor only):**
  A) Small studies have larger SEs.
  C) Small isn't wrong.
  D) Each estimate is unbiased, but the significant subset is biased upward.
- **Hint:** What has to happen for a small study to reach p < 0.05?

### rev-ch10-hw-01
- **Kind:** Course original
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

Which of the following statements is most appropriate as an ALTERNATIVE hypothesis?

- **Options:**

  A) After a drought reduced the supply of small, soft seeds, the average beak depth of medium ground finches was greater than before the drought, as larger beaks were needed to crack the remaining large, hard seeds
  B) The average beak depth of medium ground finches was the same before and after a drought that reduced the supply of small, soft seeds
  C) After the drought, the average beak depth of medium ground finches increased by exactly 0.5 mm compared to the pre-drought population

- **Answer (tutor only):** A
- **Explanation (tutor only):** An alternative hypothesis states that there is a difference (here, a larger beak depth).
- **Why the wrong options are wrong (tutor only):**
  B) 'The same' is the null.
  C) Hypotheses aren't usually 'exactly 0.5 mm'; a specific value is something you'd test against, not a typical alternative.
- **Hint:** The null says 'no difference.' What does the alternative say?

### rev-ch10-hw-01-v1
- **Kind:** AI-written version of rev-ch10-hw-01
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

Which statement is most appropriate as an ALTERNATIVE hypothesis?

- **Options:**

  A) Mean seed size differs between plants in shaded and sunny plots
  B) Shaded plants produce seeds exactly 1.2 mg heavier than sunny plants
  C) Mean seed size is the same in shaded and sunny plots

- **Answer (tutor only):** A
- **Explanation (tutor only):** An alternative hypothesis claims a difference or association.
- **Why the wrong options are wrong (tutor only):**
  B) Alternatives don't usually claim an exact value.
  C) 'The same' is the null.
- **Hint:** Which statement claims something is going on?

### rev-ch10-hw-01-v2
- **Kind:** AI-written version of rev-ch10-hw-01
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

A researcher asks whether salamander abundance is associated with stream temperature. Which is the null hypothesis?

- **Options:**

  A) No association between abundance and temperature
  B) Salamanders are more abundant in cooler streams
  C) Salamanders are rare
  D) Stream temperature affects how many salamanders there are

- **Answer (tutor only):** A
- **Explanation (tutor only):** The null is 'no association'.
- **Why the wrong options are wrong (tutor only):**
  B) and D) These claim an association (alternatives).
  C) That isn't a hypothesis about the relationship.
- **Hint:** The null says nothing is going on.

### rev-ch10-hw-02
- **Kind:** Course original
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

Consider this alternative hypothesis: 'After the drought, the average beak depth of medium ground finches was GREATER than before the drought.' Is it one-tailed or two-tailed?

- **Options:**

  A) One-tailed
  B) Two-tailed

- **Answer (tutor only):** A
- **Explanation (tutor only):** It specifies a direction (greater), so it's one-tailed. A two-tailed alternative would say 'different' (either direction). The book recommends two-tailed tests unless there's a strong reason otherwise.
- **Why the wrong options are wrong (tutor only):**
  B) A two-tailed alternative doesn't choose a direction.
- **Hint:** Does the alternative pick a direction?

### rev-ch10-hw-02-v1
- **Kind:** AI-written version of rev-ch10-hw-02
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

Alternative hypothesis: 'Mean heart rate DIFFERS between people who drink coffee and those who don't.' One-tailed or two-tailed?

- **Options:**

  A) One-tailed
  B) Two-tailed

- **Answer (tutor only):** B
- **Explanation (tutor only):** 'Differs' allows either direction, so it's two-tailed.
- **Why the wrong options are wrong (tutor only):**
  A) A one-tailed alternative would say 'higher' or 'lower.'
- **Hint:** Is a direction specified?

### rev-ch10-hw-02-v2
- **Kind:** AI-written version of rev-ch10-hw-02
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

Why does the book generally recommend two-tailed tests?

- **Options:**

  A) Two-tailed tests don't need a null hypothesis
  B) Two-tailed tests always give smaller p-values, so they find effects more easily
  C) One-tailed tests are mathematically invalid
  D) Effects in the 'wrong' direction matter, and one-tailed tests invite cherry-picking

- **Answer (tutor only):** D
- **Explanation (tutor only):** A one-tailed test ignores effects in the other direction and halves the p-value for the chosen one, which is tempting to pick after the fact.
- **Why the wrong options are wrong (tutor only):**
  A) Every test needs a null.
  B) For the same data, two-tailed p-values are larger.
  C) They're valid when justified in advance.
- **Hint:** What does a one-tailed test ignore?

### rev-ch10-hw-03
- **Kind:** Course original
- **Concepts:** Sampling distribution, SD & SE; Hypotheses & p-values
- **Type:** MC
- **Question:**

Which statement best explains why very large studies sometimes detect 'significant' effects that are practically meaningless?

- **Options:**

  A) Because with large N, even tiny differences become statistically detectable
  B) Because large studies have biased estimators
  C) Because large studies violate null assumptions more often

- **Answer (tutor only):** A
- **Explanation (tutor only):** The SE shrinks with √n, so with huge samples even a trivially small (but nonzero) effect yields a small p-value. Statistical significance ≠ practical importance; look at the effect size.
- **Why the wrong options are wrong (tutor only):**
  B) Large studies aren't more biased.
  C) Sample size doesn't change whether the null is true.
- **Hint:** What happens to the SE as n grows?

### rev-ch10-hw-03-v1
- **Kind:** AI-written version of rev-ch10-hw-03
- **Concepts:** Sampling distribution, SD & SE; Hypotheses & p-values
- **Type:** MC
- **Question:**

A study of 2 million smartphone users finds that a new app layout increases time on the app by 0.4 seconds per day (p < 0.0001). What's the best interpretation?

- **Options:**

  A) The study was biased because it was so large
  B) The result is probably due to chance
  C) Almost certainly real but practically negligible
  D) The effect is large, because p is so small

- **Answer (tutor only):** C
- **Explanation (tutor only):** Huge samples detect tiny effects. Significance tells you the effect is probably not zero; the estimate (0.4 s) tells you it doesn't matter much.
- **Why the wrong options are wrong (tutor only):**
  A) Size doesn't cause bias.
  B) p < 0.0001 makes chance an unlikely explanation.
  D) p-values don't measure effect size.
- **Hint:** Separate 'is there an effect?' from 'how big is it?'

### rev-ch10-hw-03-v2
- **Kind:** AI-written version of rev-ch10-hw-03
- **Concepts:** Sampling distribution, SD & SE; Hypotheses & p-values
- **Type:** MC
- **Question:**

If the true effect is small but not zero, what happens to the p-value as sample size grows (on average)?

- **Options:**

  A) It gets larger
  B) It gets smaller, eventually below 0.05
  C) It equals the effect size
  D) It stays about the same, since the effect doesn't change

- **Answer (tutor only):** B
- **Explanation (tutor only):** A larger n shrinks the SE, so even a small real effect becomes more and more detectable.
- **Why the wrong options are wrong (tutor only):**
  A) More data gives more evidence, not less.
  C) p-values aren't effect sizes.
  D) The p-value depends on n.
- **Hint:** What does a bigger n do to the SE?

### rev-ch10-hw-07
- **Kind:** Course original
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

The prosecutor's fallacy is the error of:

- **Options:**

  A) Assuming all evidence is independent
  B) Assuming sampling error is zero
  C) Using p < 0.05 as proof of the alternative
  D) Confusing the probability of the evidence under a hypothesis with the probability that the hypothesis is true given the evidence

- **Answer (tutor only):** D
- **Explanation (tutor only):** P(evidence | innocent) is not P(innocent | evidence). In statistics: a p-value is P(data | H0), not P(H0 | data).
- **Why the wrong options are wrong (tutor only):**
  A)–C) Real problems, but not this fallacy.
- **Hint:** Which way does the 'given' go?

### rev-ch10-hw-07-v1
- **Kind:** AI-written version of rev-ch10-hw-07
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

A DNA match has a 1-in-a-million chance of occurring for an innocent person. A prosecutor says: 'So there's only a 1-in-a-million chance the defendant is innocent.' What's wrong?

- **Options:**

  A) It confuses P(match | innocent) with P(innocent | match)
  B) The chance should be 1 in 2 million, since there are two alleles
  C) Nothing; that's correct
  D) DNA evidence is never reliable enough to use in court

- **Answer (tutor only):** A
- **Explanation (tutor only):** The probability of the evidence given innocence isn't the probability of innocence given the evidence. Same for p-values: P(data | H0) ≠ P(H0 | data).
- **Why the wrong options are wrong (tutor only):**
  B) The number isn't the problem.
  C) This is the classic fallacy.
  D) The issue is the logic, not DNA.
- **Hint:** Which way does the 'given' go?

### rev-ch10-hw-07-v2
- **Kind:** AI-written version of rev-ch10-hw-07
- **Concepts:** Hypotheses & p-values
- **Type:** MC
- **Question:**

Which statement commits the prosecutor's fallacy?

- **Options:**

  A) 'p = 0.02 is below α = 0.05, so we reject the null'
  B) 'p = 0.02 doesn't tell us the effect size'
  C) 'If the null were true, data this extreme would occur 2% of the time'
  D) 'p = 0.02, so there's a 2% chance the null hypothesis is true'

- **Answer (tutor only):** D
- **Explanation (tutor only):** It flips P(data | H0) into P(H0 | data).
- **Why the wrong options are wrong (tutor only):**
  A) A correct decision rule.
  B) True and not a fallacy.
  C) That's the correct definition.
- **Hint:** Find the one that makes the p-value a probability about the hypothesis.

### rev-ch11-book-01
- **Kind:** Course original
- **Concepts:** Bootstrap & confidence intervals; Permutation
- **Type:** matching
- **Question:**

Which method (bootstrap, permutation, both, or neither):

1. keeps the overall mean of the entire dataset identical in every replicate?
2. generates a confidence interval by simulating sampling error around an observed statistic?
3. is mainly used to generate a p-value by simulating a null hypothesis?

- **Options:**

  A) Bootstrap
  B) Permutation
  C) Both
  D) Neither

- **Answer (tutor only):** 1-B, 2-A, 3-B
- **Explanation (tutor only):** Permutation only shuffles labels, so the overall mean never changes, and it simulates the null to produce p-values. The bootstrap resamples with replacement, so values (and the overall mean) change, and it is used to estimate uncertainty (CIs).
- **Why the wrong options are wrong (tutor only):**
  The bootstrap changes which values appear; permutation never does.
- **Hint:** Shuffle vs resample.

### rev-ch11-book-01-v1
- **Kind:** AI-written version of rev-ch11-book-01
- **Concepts:** Bootstrap & confidence intervals; Permutation
- **Type:** matching
- **Question:**

Which method (bootstrap, permutation, both, or neither):

1. uses every original observation exactly once in each replicate?
2. can give some observations twice in a replicate?
3. requires collecting new data from the population?

- **Options:**

  A) Bootstrap
  B) Permutation
  C) Both
  D) Neither

- **Answer (tutor only):** 1-B, 2-A, 3-D
- **Explanation (tutor only):** Permutation reshuffles the same values; the bootstrap samples with replacement. Neither collects new data; that's their whole appeal.
- **Why the wrong options are wrong (tutor only):**
  3: Both methods work from the one sample we have.
- **Hint:** Shuffling vs resampling with replacement.

### rev-ch11-book-01-v2
- **Kind:** AI-written version of rev-ch11-book-01
- **Concepts:** Bootstrap & confidence intervals; Permutation
- **Type:** matching
- **Question:**

Which method (bootstrap, permutation, both, or neither):

1. approximates a distribution using only our sample?
2. assumes the data are normally distributed?
3. keeps the association between the explanatory and response variables?

- **Options:**

  A) Bootstrap
  B) Permutation
  C) Both
  D) Neither

- **Answer (tutor only):** 1-C, 2-D, 3-A
- **Explanation (tutor only):** Both are computational methods using only our data, and neither assumes normality. Only the bootstrap keeps each individual's x and y together.
- **Why the wrong options are wrong (tutor only):**
  3: Permutation deliberately breaks the association.
- **Hint:** Which keeps pairs intact?

### rev-ch11-book-02
- **Kind:** Course original
- **Concepts:** Bootstrap & confidence intervals; Hypotheses & p-values; Permutation
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-book-penguin-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch11-book-penguin-boot-perm.png)
- **Question:**

Adelie penguins from Torgersen island (23 males, 24 females). Males are 639 g heavier on average. One plot shows 5000 bootstrap replicates of the male − female difference, and the other shows 5000 permutations (blue line = observed 639 g).

For each statement, which method makes it true?

1. The overall mean body mass is identical in every replicate
2. The male mean body mass is identical in every replicate
3. The distribution of the sex difference is centered around the original estimate (639 g)
4. The distribution of the sex difference is centered around the null value (0)

- **Options:**

  A) Bootstrap
  B) Permutation
  C) Both
  D) Neither

- **Answer (tutor only):** 1-B, 2-D, 3-A, 4-B
- **Explanation (tutor only):** Permutation: same numbers reshuffled, so the overall mean is fixed, the male mean changes, and the distribution is centered at 0. Bootstrap: values resampled, so all the means vary, and the distribution is centered near the observed 639 g.
- **Why the wrong options are wrong (tutor only):**
  2: Neither method keeps the male mean fixed. Shuffling changes which values are labeled male, and resampling changes the values themselves.
- **Hint:** Where is each histogram centered?

### rev-ch11-book-02-v1
- **Kind:** AI-written version of rev-ch11-book-02
- **Concepts:** Bootstrap & confidence intervals; Hypotheses & p-values; Permutation
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-var-chin-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch11-var-chin-boot-perm.png)
- **Question:**

Chinstrap penguins (34 males, 34 females). Males' flippers are 8.2 mm longer on average. One plot shows 5000 bootstrap replicates of the male − female difference, and the other shows 5000 permutations (blue line = observed 8.2 mm).

For each statement, which method makes it true?

1. The overall mean flipper length (195.8 mm) is identical in every replicate
2. The female mean is identical in every replicate
3. The distribution of the sex difference is centered near 0
4. The distribution of the sex difference is centered near 8.2 mm

- **Options:**

  A) Bootstrap
  B) Permutation
  C) Both
  D) Neither

- **Answer (tutor only):** 1-B, 2-D, 3-B, 4-A
- **Explanation (tutor only):** Permutation reuses the same 68 values (fixed overall mean) and centers the difference at 0. The bootstrap centers near the observed 8.2 mm. Neither keeps the female mean fixed.
- **Why the wrong options are wrong (tutor only):**
  2: Shuffling changes which values are labeled female; resampling changes the values.
- **Hint:** What stays the same when you shuffle labels?

### rev-ch11-book-02-v2
- **Kind:** AI-written version of rev-ch11-book-02
- **Concepts:** Bootstrap & confidence intervals; Permutation
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-var-chin-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch11-var-chin-boot-perm.png)
- **Question:**

Chinstrap penguins (34 males, 34 females). Males' flippers are 8.2 mm longer on average. One plot shows 5000 bootstrap replicates of the male − female difference, and the other shows 5000 permutations (blue line = observed 8.2 mm).

Why is the permutation distribution centered at 0 while the bootstrap distribution is centered near 8.2 mm?

- **Options:**

  A) Shuffling removes the sex difference; bootstrapping keeps it
  B) The bootstrap removes sampling error, so it centers on the truth
  C) Permutation uses fewer replicates than the bootstrap
  D) It's a coincidence

- **Answer (tutor only):** A
- **Explanation (tutor only):** Permutation simulates the null (no difference); the bootstrap simulates sampling variation around our estimate.
- **Why the wrong options are wrong (tutor only):**
  B) The bootstrap shows sampling error.
  C) Both use 5000.
  D) It's by design.
- **Hint:** Which method keeps the association?

### rev-ch11-book-03
- **Kind:** Course original
- **Concepts:** Bootstrap & confidence intervals; Hypotheses & p-values; Permutation
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-book-penguin-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch11-book-penguin-boot-perm.png)
- **Question:**

Adelie penguins from Torgersen island (23 males, 24 females). Males are 639 g heavier on average. One plot shows 5000 bootstrap replicates of the male − female difference, and the other shows 5000 permutations (blue line = observed 639 g).

Which plot is which?

- **Options:**

  A) Distribution 1 is the permutation (null) distribution; Distribution 2 is the bootstrap distribution
  B) Distribution 1 is the bootstrap distribution; Distribution 2 is the permutation (null) distribution

- **Answer (tutor only):** A
- **Explanation (tutor only):** Distribution 1 is centered at 0 (the null), and the observed 639 g is far outside it, so it's the permutation. Distribution 2 is centered on the observed 639 g, so it's the bootstrap.
- **Why the wrong options are wrong (tutor only):**
  B) Distribution 1 is centered at 0, the null value. A bootstrap is centered on the estimate (639 g).
- **Hint:** Where is each one centered?

### rev-ch11-book-03-v1
- **Kind:** AI-written version of rev-ch11-book-03
- **Concepts:** Bootstrap & confidence intervals; Hypotheses & p-values; Permutation
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-var-chin-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch11-var-chin-boot-perm.png)
- **Question:**

Chinstrap penguins (34 males, 34 females). Males' flippers are 8.2 mm longer on average. One plot shows 5000 bootstrap replicates of the male − female difference, and the other shows 5000 permutations (blue line = observed 8.2 mm).

Which plot is which?

- **Options:**

  A) Distribution 1 is the permutation (null) distribution; Distribution 2 is the bootstrap distribution
  B) Distribution 1 is the bootstrap distribution; Distribution 2 is the permutation (null) distribution

- **Answer (tutor only):** B
- **Explanation (tutor only):** Distribution 1 is centered on the observed 8.2 mm (bootstrap). Distribution 2 is centered at 0, with 8.2 far in the tail (permutation).
- **Why the wrong options are wrong (tutor only):**
  A) Distribution 1 is centered on the observed 8.2 mm, not 0. A permutation (null) distribution is centered at 0.
- **Hint:** Where is each centered?

### rev-ch11-book-03-v2
- **Kind:** AI-written version of rev-ch11-book-03
- **Concepts:** Hypotheses & p-values; Permutation
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-var-chin-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch11-var-chin-boot-perm.png)
- **Question:**

Chinstrap penguins (34 males, 34 females). Males' flippers are 8.2 mm longer on average. One plot shows 5000 bootstrap replicates of the male − female difference, and the other shows 5000 permutations (blue line = observed 8.2 mm).

What does the position of the blue line in Distribution 2 tell you?

- **Options:**

  A) The observed difference is typical under the null
  B) The bootstrap failed
  C) The CI includes 0, so the difference isn't significant
  D) Shuffling never produced a difference that big, so p is tiny

- **Answer (tutor only):** D
- **Explanation (tutor only):** The blue line (8.2 mm) lies well past the largest permuted difference (about 6.5 mm in absolute value).
- **Why the wrong options are wrong (tutor only):**
  A) It's way out in the tail.
  B) Distribution 2 is the permutation.
  C) Distribution 2 isn't used for a CI.
- **Hint:** Is 8.2 mm unusual for the null distribution?

### rev-ch11-chime-01
- **Kind:** Course original
- **Concepts:** Samples, populations & bias; Permutation
- **Type:** select-all
- **Question:**

The permutation test assumes that samples are collected (choose all correct):

- **Options:**

  A) without sampling error
  B) without bias
  C) independently (though non-independence can be incorporated)
  D) generating a null hypothesis

- **Answer (tutor only):** B, C
- **Explanation (tutor only):** Like other tests, permutation assumes unbiased, independent data. Non-independence can be handled by shuffling within groups (e.g., within beds).
- **Why the wrong options are wrong (tutor only):**
  A) Sampling error is exactly what the test accounts for.
  D) Not an assumption about data collection.
- **Hint:** What can't shuffling fix?

### rev-ch11-chime-01-v1
- **Kind:** AI-written version of rev-ch11-chime-01
- **Concepts:** Samples, populations & bias; Permutation
- **Type:** select-all
- **Question:**

Which of these is a permutation test robust to, or not dependent on? (Select all correct.)

- **Options:**

  A) Non-normal data
  B) Biased sampling
  C) Non-independent observations analyzed as independent

- **Answer (tutor only):** A
- **Explanation (tutor only):** Permutation makes no normality assumption. But like any test it needs unbiased, independent data (or a shuffling scheme that respects the dependence).
- **Why the wrong options are wrong (tutor only):**
  B) Bias gives a misleading answer whatever the test.
  C) Must be handled, e.g., by shuffling within groups.
- **Hint:** What does shuffling assume about the data?

### rev-ch11-chime-01-v2
- **Kind:** AI-written version of rev-ch11-chime-01
- **Concepts:** Samples, populations & bias; Permutation
- **Type:** MC
- **Question:**

A permutation test finds a significant difference in songbird size between two forests, but all birds were caught with nets that miss small birds in one forest only. What's the problem?

- **Options:**

  A) Not enough permutations were run
  B) Biased sampling, which permutation can't fix
  C) No problem
  D) Permutation tests require normally distributed data

- **Answer (tutor only):** B
- **Explanation (tutor only):** Permutation tests assume unbiased sampling. A difference created by the nets would look 'significant' too.
- **Why the wrong options are wrong (tutor only):**
  A) More shuffles won't remove bias.
  C) The bias could explain the result.
  D) Permutation doesn't assume normality.
- **Hint:** Can any test fix biased data?

### rev-ch11-chime-02
- **Kind:** Course original
- **Concepts:** Hypotheses & p-values; Permutation
- **Type:** MC
- **Question:**

The idea of the permutation test is to 'shuffle' the treatments so as to remove what from the data?

- **Options:**

  A) outliers
  B) sampling error
  C) bias in our sampling
  D) an actual association

- **Answer (tutor only):** D
- **Explanation (tutor only):** Shuffling destroys any real association, so the permuted data show what the null (no association) would produce.
- **Why the wrong options are wrong (tutor only):**
  A)–C) Shuffling doesn't remove these.
- **Hint:** Why do we want data with no association?

### rev-ch11-chime-02-v1
- **Kind:** AI-written version of rev-ch11-chime-02
- **Concepts:** Hypotheses & p-values; Permutation
- **Type:** MC
- **Question:**

What does each permuted replicate represent?

- **Options:**

  A) A resample of our data, drawn with replacement
  B) Data like ours with any real association removed
  C) A new sample from the population
  D) A dataset with the outliers removed

- **Answer (tutor only):** B
- **Explanation (tutor only):** Shuffling breaks the link between variables, so each replicate is one possible 'null world' version of our data.
- **Why the wrong options are wrong (tutor only):**
  A) That's the bootstrap.
  C) No new data are collected.
  D) All values are kept.
- **Hint:** What does shuffling destroy?

### rev-ch11-chime-02-v2
- **Kind:** AI-written version of rev-ch11-chime-02
- **Concepts:** Hypotheses & p-values; Permutation
- **Type:** MC
- **Question:**

After building a permutation null distribution, how is the p-value found?

- **Options:**

  A) The proportion as or more extreme than observed
  B) The SD of the permuted statistics
  C) The 2.5th and 97.5th percentiles of the permuted statistics
  D) The mean of the permuted statistics

- **Answer (tutor only):** A
- **Explanation (tutor only):** How often does the null world produce something as extreme as what we saw?
- **Why the wrong options are wrong (tutor only):**
  B) That's a spread, not a p-value.
  C) Those percentiles would give an interval, not a p-value (and bootstrap percentiles give the CI).
  D) That's near 0 by design.
- **Hint:** How often does the null produce data like ours?

### rev-ch11-new-01
- **Kind:** Course original
- **Concepts:** Hypotheses & p-values; Permutation
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-lineup-null.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch11-lineup-null.png)
- **Question:**

Permutation eye-test: the plot shows 20 panels of Adelie penguin body mass on Biscoe vs Dream islands, with means and 95% CIs. One panel is the real data; the other 19 were made by shuffling the island labels.

The real data are in panel 14. Most people can't pick it out, and many guess panel 13. What does that tell us?

- **Options:**

  A) The shuffling was done wrong, because the real data should always stand out
  B) Penguins on the two islands have exactly the same mean body mass
  C) Panel 13 shows that there is a real difference between the islands, not panel 14
  D) It looks like what shuffling produces: p is probably large. Not proof the islands are the same

- **Answer (tutor only):** D
- **Explanation (tutor only):** If the real panel blends in with the shuffled ones, chance alone easily produces data like ours. Here the real difference is about 21 g, and a permutation test gives p ≈ 0.8. We fail to reject the null, but the data are also consistent with a small difference, so we can't conclude there is none.
- **Why the wrong options are wrong (tutor only):**
  A) The real data stand out only when there is a strong association; with no real difference, they shouldn't.
  B) Failing to reject the null isn't evidence that the means are exactly equal.
  C) Panel 13 is a shuffle. With 19 shuffles, one of them will look a bit different by chance alone.
- **Hint:** If island didn't matter, would the real panel look any different from a shuffled one?

### rev-ch11-new-01-v1
- **Kind:** AI-written version of rev-ch11-new-01
- **Concepts:** Hypotheses & p-values; Permutation
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-lineup-null.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch11-lineup-null.png)
- **Question:**

Permutation eye-test: the plot shows 20 panels of Adelie penguin body mass on Biscoe vs Dream islands, with means and 95% CIs. One panel is the real data; the other 19 were made by shuffling the island labels.

What do the 19 shuffled panels represent?

- **Options:**

  A) What data would look like if island had no effect on mass
  B) What data would look like if Biscoe penguins were heavier
  C) Repeated real samples taken from the two penguin islands
  D) Bootstrap resamples used to build a confidence interval

- **Answer (tutor only):** A
- **Explanation (tutor only):** Shuffling labels breaks any link between island and mass, simulating the null.
- **Why the wrong options are wrong (tutor only):**
  B) That's an alternative.
  C) They're not new samples.
  D) Bootstrapping resamples with replacement within groups; this shuffles labels.
- **Hint:** What does shuffling remove?

### rev-ch11-new-01-v2
- **Kind:** AI-written version of rev-ch11-new-01
- **Concepts:** Hypotheses & p-values; Permutation
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-lineup-null.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch11-lineup-null.png)
- **Question:**

Permutation eye-test: the plot shows 20 panels of Adelie penguin body mass on Biscoe vs Dream islands, with means and 95% CIs. One panel is the real data; the other 19 were made by shuffling the island labels.

If the real panel clearly stood out from all 19 shuffled panels, what would that suggest?

- **Options:**

  A) The real difference is unusual under the null (p ≤ 1/20)
  B) Shuffling was done incorrectly, so the test is invalid
  C) The islands certainly have identical mean body masses
  D) Nothing; line-ups can't tell us anything about the data

- **Answer (tutor only):** A
- **Explanation (tutor only):** If the real data stand out from 19 null panels, a pattern that strong would rarely arise by chance (like p ≤ 0.05).
- **Why the wrong options are wrong (tutor only):**
  B) Standing out is the point.
  C) The opposite.
  D) Line-ups are a visual permutation test.
- **Hint:** 1 real vs 19 null.

### rev-ch12-book-05
- **Kind:** Course original
- **Concepts:** Causation & study design
- **Type:** TF
- **Question:**

TRUE or FALSE: Random assignment controls for covariates by modeling the effect of each one.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** Random assignment works through design, not modeling. Treatment is assigned independently of everything else, so confounders (even unknown ones) are balanced across groups on average. Modeling covariates is a separate statistical adjustment.
- **Why the wrong options are wrong (tutor only):**
  A) No model is involved; that's the beauty of it. You don't even need to know what the confounders are.
- **Hint:** Does random assignment require knowing what the confounders are?

### rev-ch12-book-05-v1
- **Kind:** AI-written version of rev-ch12-book-05
- **Concepts:** Causation & study design
- **Type:** TF
- **Question:**

TRUE or FALSE: Random assignment balances confounders across treatment groups on average, even confounders the researcher never thought to measure.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** A
- **Explanation (tutor only):** Because treatment is assigned by chance, it can't be systematically related to anything about the subjects, measured or not.
- **Why the wrong options are wrong (tutor only):**
  B) This is the main power of random assignment.
- **Hint:** Does a coin flip know who's healthier?

### rev-ch12-book-05-v2
- **Kind:** AI-written version of rev-ch12-book-05
- **Concepts:** Causation & study design
- **Type:** MC
- **Question:**

How does statistically adjusting for covariates (e.g., including age in a model) differ from random assignment?

- **Options:**

  A) Adjustment is always better than random assignment
  B) Random assignment only works for measured covariates
  C) Adjustment only handles measured covariates
  D) They're the same thing, done at different stages

- **Answer (tutor only):** C
- **Explanation (tutor only):** Unmeasured confounders can still bias an adjusted observational analysis, but not a randomized experiment (on average).
- **Why the wrong options are wrong (tutor only):**
  A) Adjustment can't fix unmeasured confounding.
  B) Backwards.
  D) One is design, the other is modeling.
- **Hint:** What about confounders you never measured?

### rev-ch12-hw-02
- **Kind:** Course original
- **Concepts:** Sampling distribution, SD & SE; Causation & study design
- **Type:** select-all
- **Question:**

Potential explanations for a significant relationship between two variables, A and B, in an OBSERVATIONAL study are (select all correct):

- **Options:**

  A) A causes B
  B) B causes A
  C) Both A and B are caused by some other variable, C
  D) Sampling error

- **Answer (tutor only):** A, B, C, D
- **Explanation (tutor only):** Without random assignment, any of these can produce an association: a causal effect in either direction, a confounder, or chance (a significant result can still be a false positive).
- **Why the wrong options are wrong (tutor only):**
  Leaving any out ignores a real possibility.
- **Hint:** Name every way two things can end up correlated.

### rev-ch12-hw-02-v1
- **Kind:** AI-written version of rev-ch12-hw-02
- **Concepts:** Causation & study design
- **Type:** MC
- **Question:**

In an observational study, people who sleep more report less anxiety. Which explanation is reverse causation?

- **Options:**

  A) More sleep reduces anxiety
  B) The association is a chance result
  C) A third factor (e.g., stress at work) affects both
  D) Less anxious people find it easier to sleep

- **Answer (tutor only):** D
- **Explanation (tutor only):** Reverse causation: the response is actually causing the explanatory variable.
- **Why the wrong options are wrong (tutor only):**
  A) That's the forward causal story.
  B) That's sampling error.
  C) That's confounding.
- **Hint:** Flip the arrow.

### rev-ch12-hw-02-v2
- **Kind:** AI-written version of rev-ch12-hw-02
- **Concepts:** Causation & study design
- **Type:** MC
- **Question:**

Ice cream sales and sunburns are positively correlated across days. What's the most likely explanation?

- **Options:**

  A) Sunburns make people buy ice cream to cool down
  B) It must be sampling error
  C) Ice cream causes sunburn
  D) Hot, sunny weather increases both

- **Answer (tutor only):** D
- **Explanation (tutor only):** Sunny days drive both. This is the classic common-cause pattern.
- **Why the wrong options are wrong (tutor only):**
  B) Possible, but a confounder is far more likely with an obvious common cause.
  C) and A) No plausible mechanism.
- **Hint:** What makes both go up?

### rev-exam1-q04
- **Kind:** Course original
- **Concepts:** Sampling distribution, SD & SE
- **Type:** select-all
- **Question:**

You conduct the same study twice, once with a sample of size ten, and once with a sample of size 100. Which estimate(s) is (are) most likely to get smaller in the study with a larger sample? Select all correct.

- **Options:**

  A) Mean
  B) Standard deviation
  C) Variance
  D) Coefficient of variation
  E) Standard error

- **Answer (tutor only):** E
- **Explanation (tutor only):** The standard error describes how much an estimate would vary from sample to sample. Think of bootstrapping: in a resample of 10 values, a few unusually high or low values can easily pile up by chance and pull the mean far off. In a resample of 100, highs and lows almost always cancel out (the law of large numbers). So the bootstrap distribution is narrower and the SE is smaller. The mean, SD, variance and CV describe the population itself; a bigger sample estimates them more precisely but doesn't make them smaller.
- **Why the wrong options are wrong (tutor only):**
  A) The mean estimates the population's center. More data makes it more precise, not smaller.
  B) The SD estimates how spread out individuals are. More data doesn't make individuals less variable.
  C) Variance is the SD squared, so it doesn't systematically shrink either.
  D) The CV is SD / mean, both of which describe the population, so it doesn't systematically shrink.
- **Hint:** Which of these describes uncertainty in an estimate, rather than the population itself?

### rev-exam1-q04-v1
- **Kind:** AI-written version of rev-exam1-q04
- **Concepts:** Sampling distribution, SD & SE
- **Type:** select-all
- **Question:**

You conduct the same study twice, once with 20 individuals and once with 500. Which estimate(s) are most likely to be smaller in the study with 500? (Select all that apply.)

- **Options:**

  A) The standard error
  B) The width of the 95% confidence interval
  C) The standard deviation
  D) The mean

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** Uncertainty (SE, CI width) shrinks with n; the SD and mean estimate population values that don't depend on n.
- **Why the wrong options are wrong (tutor only):**
  C) and D) don't systematically change with n.
- **Hint:** Uncertainty vs population values.

### rev-exam1-q04-v2
- **Kind:** AI-written version of rev-exam1-q04
- **Concepts:** Sampling distribution, SD & SE
- **Type:** select-all
- **Question:**

As sample size increases, which estimates are expected to stay about the same (but become more precise)? (Select all that apply.)

- **Options:**

  A) The mean
  B) The standard deviation
  C) The standard error
  D) The width of the 95% CI

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** The mean and SD estimate fixed population values. The SE and CI width shrink with n.
- **Why the wrong options are wrong (tutor only):**
  C) and D) shrink.
- **Hint:** Which ones estimate population parameters?

### rev-exam1-q06
- **Kind:** Course original
- **Concepts:** Sampling distribution, SD & SE
- **Type:** MC
- **Question:**

A student says, "The sampling distribution shows how the values in my dataset are spread." Why are they wrong?

- **Options:**

  A) Because the sampling distribution describes variation in estimates across repeated samples, not variation within a single sample
  B) Because the sampling distribution only applies to categorical data
  C) Because the sampling distribution is calculated before collecting data
  D) Because the sampling distribution depends on the population size, not the sample size
  E) They aren't wrong

- **Answer (tutor only):** A
- **Explanation (tutor only):** The sampling distribution is the distribution of an estimate (like the mean) across many samples. The spread of values within one dataset is the distribution of the data, summarized by the SD.
- **Why the wrong options are wrong (tutor only):**
  B) Sampling distributions exist for any estimate, numeric or categorical.
  C) It describes estimates from many samples; when it's calculated isn't the issue.
  D) It depends on the sample size: bigger samples give narrower sampling distributions.
  E) They are wrong: they're describing the distribution of the data, not of an estimate.
- **Hint:** Is a sampling distribution made of individual values or of estimates?

### rev-exam1-q06-v1
- **Kind:** AI-written version of rev-exam1-q06
- **Concepts:** Sampling distribution, SD & SE
- **Type:** MC
- **Question:**

A student says, "The standard error tells me how much the individuals in my sample differ from each other." Why are they wrong?

- **Options:**

  A) The SE describes how much estimates vary among samples, not individuals
  B) The SE is only defined for categorical data, not for measurements
  C) The SE is calculated before any data are collected in a study
  D) They aren't wrong; that is what the standard error describes

- **Answer (tutor only):** A
- **Explanation (tutor only):** Variation among individuals is the SD. The SE describes uncertainty in an estimate across repeated samples.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Not true.
  D) That's the SD.
- **Hint:** Individuals vs estimates.

### rev-exam1-q06-v2
- **Kind:** AI-written version of rev-exam1-q06
- **Concepts:** Sampling distribution, SD & SE
- **Type:** MC
- **Question:**

Which describes the sampling distribution of a mean?

- **Options:**

  A) The distribution of means from many samples of the same size
  B) The distribution of individual values within one sample
  C) The distribution of individual values in the population
  D) The distribution of p-values from many repeated studies

- **Answer (tutor only):** A
- **Explanation (tutor only):** A sampling distribution is the distribution of an estimate across repeated samples.
- **Why the wrong options are wrong (tutor only):**
  B) That's the sample distribution.
  C) That's the population distribution.
  D) Not what it means.
- **Hint:** Distribution of estimates.

### rev-exam1-q08
- **Kind:** Course original
- **Concepts:** Samples, populations & bias
- **Type:** MC
- **Question:**

Because turtle hatchlings are difficult to catch, you scatter food to attract them and measure the running speed of the first 30 individuals that reach the food. This sampling method likely introduces...

- **Options:**

  A) Sampling error, because estimates differ across samples by chance
  B) Sampling bias, because faster turtles are more likely to be measured
  C) Non-independence, because turtles from the same nest share genetics
  D) Measurement error, because timing turtles is imprecise

- **Answer (tutor only):** B
- **Explanation (tutor only):** The first 30 turtles to reach the food are probably the fastest, so the sample systematically overestimates running speed. Sampling more turtles the same way wouldn't fix it.
- **Why the wrong options are wrong (tutor only):**
  A) Every sample has sampling error; the special problem here is that the method favors fast turtles.
  C) Nothing in the setup says the turtles come from the same nest.
  D) Timing may be imprecise, but the bigger problem is who gets measured.
- **Hint:** Which turtles reach the food first?

### rev-exam1-q08-v1
- **Kind:** AI-written version of rev-exam1-q08
- **Concepts:** Samples, populations & bias
- **Type:** MC
- **Question:**

To estimate the average size of fish in a lake, you measure fish caught with a net whose holes let small fish escape. This sampling method likely introduces...

- **Options:**

  A) Sampling bias, because small fish are less likely to be measured
  B) Sampling error, because estimates differ among samples by chance
  C) Non-independence, because fish from one school are related
  D) Measurement error, because rulers are imprecise for fish

- **Answer (tutor only):** A
- **Explanation (tutor only):** The net systematically misses small fish, so the estimate will be too large: bias.
- **Why the wrong options are wrong (tutor only):**
  B) Sampling error is random, not systematic.
  C) and D) Not the main issue.
- **Hint:** Is the error systematic?

### rev-exam1-q08-v2
- **Kind:** AI-written version of rev-exam1-q08
- **Concepts:** Samples, populations & bias
- **Type:** MC
- **Question:**

To estimate how much time people spend outdoors, a researcher surveys visitors at a national park. Which problem is this design most likely to have?

- **Options:**

  A) Sampling bias: park visitors likely spend more time outdoors
  B) Sampling error: a larger sample would remove the problem
  C) Non-independence: visitors were all asked the same questions
  D) No problem: anyone could visit the park on any day

- **Answer (tutor only):** A
- **Explanation (tutor only):** Park visitors aren't representative of everyone; more data won't fix a biased sampling frame.
- **Why the wrong options are wrong (tutor only):**
  B) Larger samples don't fix bias.
  C) Same questions don't cause non-independence.
  D) The sample isn't representative.
- **Hint:** Who gets sampled?

### rev-exam1-q09
- **Kind:** Course original
- **Concepts:** Hypotheses & p-values
- **Type:** select-all
- **Question:**

A p-value of 0.01 means: (select all correct)

- **Options:**

  A) We reject the null hypothesis
  B) We fail to reject the null hypothesis
  C) The null is false
  D) There is a 1% chance the null is correct
  E) There is a 1% chance the null generated our data (or something more extreme)
  F) 1% of samples from the null will be as or more extreme than our observation

- **Answer (tutor only):** A, F
- **Explanation (tutor only):** With the usual α = 0.05, p = 0.01 < 0.05, so we reject the null. F is the definition of a p-value: the probability of a result as or more extreme than ours, if the null were true.
- **Why the wrong options are wrong (tutor only):**
  B) p = 0.01 is below the usual α = 0.05, so we reject.
  C) Rejecting the null doesn't prove it false; we could be making a type I error.
  D) A p-value is calculated assuming the null is true, so it can't be the probability that the null is true.
  E) This reads as the chance the null caused our data, a probability about the hypothesis. A p-value is P(data this extreme | null), not P(null | data).
- **Hint:** A p-value is calculated assuming what?

### rev-exam1-q09-v1
- **Kind:** AI-written version of rev-exam1-q09
- **Concepts:** Hypotheses & p-values
- **Type:** select-all
- **Question:**

A p-value of 0.30 means: (select all correct)

- **Options:**

  A) We fail to reject the null hypothesis (at α = 0.05)
  B) 30% of samples from the null would be as or more extreme than ours
  C) There is a 30% chance that the null is true
  D) The null is true

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** p > 0.05, so we fail to reject. B is the definition of a p-value.
- **Why the wrong options are wrong (tutor only):**
  C) p isn't P(null).
  D) Failing to reject isn't proof.
- **Hint:** Definition of p.

### rev-exam1-q09-v2
- **Kind:** AI-written version of rev-exam1-q09
- **Concepts:** Hypotheses & p-values
- **Type:** select-all
- **Question:**

Which statements about a p-value are correct? (select all correct)

- **Options:**

  A) It is calculated assuming the null hypothesis is true
  B) It's the probability of a result at least this extreme if the null were true
  C) It is the probability that the null hypothesis is true
  D) It measures how large the effect is

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** p assumes the null and gives the probability of data at least this extreme.
- **Why the wrong options are wrong (tutor only):**
  C) Reversed conditional.
  D) p mixes effect size and sample size.
- **Hint:** P(data | null).

### rev-exam1-q11
- **Kind:** Course original
- **Concepts:** Bootstrap & confidence intervals; Errors & power
- **Type:** select-all
- **Question:**

In statistics we usually use an alpha threshold of 0.05. What would happen if the field changed the custom to alpha = 0.01 (select all correct)?

- **Options:**

  A) We would reject more false nulls
  B) We would reject more true nulls
  C) We would fail to reject more false nulls
  D) We would fail to reject more true nulls
  E) We would have wider confidence intervals (we use 99% confidence intervals)
  F) We would have narrower confidence intervals (we use 99% confidence intervals)

- **Answer (tutor only):** C, D, E
- **Explanation (tutor only):** A lower α makes it harder to reject the null, so we reject fewer nulls, true or false: fewer type I errors but more type II errors (C), and we fail to reject more true nulls (D). To match α = 0.01 we'd report 99% CIs, which are wider than 95% CIs (E).
- **Why the wrong options are wrong (tutor only):**
  A) Backwards: a stricter threshold means we reject fewer nulls, including false ones.
  B) Backwards: we'd reject fewer true nulls (fewer type I errors).
  F) Backwards: to be 99% confident, the interval has to be wider.
- **Hint:** Is it easier or harder to get p < 0.01 than p < 0.05?

### rev-exam1-q11-v1
- **Kind:** AI-written version of rev-exam1-q11
- **Concepts:** Bootstrap & confidence intervals; Errors & power
- **Type:** select-all
- **Question:**

What would happen if the field changed the custom from α = 0.05 to α = 0.10? (select all correct)

- **Options:**

  A) We would reject more true nulls (more type I errors)
  B) We would reject fewer false nulls (less power)
  C) We would reject more false nulls (more power)
  D) We would use 90% confidence intervals, which are narrower

- **Answer (tutor only):** A, C, D
- **Explanation (tutor only):** A larger α makes rejecting easier: more false positives, more power, and narrower (90%) intervals.
- **Why the wrong options are wrong (tutor only):**
  B) Power goes up.
- **Hint:** Easier to reject.

### rev-exam1-q11-v2
- **Kind:** AI-written version of rev-exam1-q11
- **Concepts:** Bootstrap & confidence intervals; Errors & power
- **Type:** select-all
- **Question:**

Lowering α from 0.05 to 0.01 makes which error MORE likely? (select all correct)

- **Options:**

  A) Failing to reject a false null (type II error)
  B) Rejecting a true null (type I error)
  C) Both type I and type II errors
  D) Neither type I nor type II errors

- **Answer (tutor only):** A
- **Explanation (tutor only):** A stricter α reduces type I errors but increases type II errors (lower power).
- **Why the wrong options are wrong (tutor only):**
  B) Type I errors become less likely.
  C) and D) There's a trade-off.
- **Hint:** Harder to reject.

### rev-exam1-q21
- **Kind:** Course original
- **Concepts:** Samples, populations & bias
- **Type:** MC
- **Question:**

You give fertilizer to one greenhouse bench and none to another, then measure 50 plants on each bench. What is the problem?

- **Options:**

  A) A sample of 50 plants per treatment is too small
  B) Data are not independent
  C) There is sampling bias
  D) The researcher should have been blinded
  E) There's no problem

- **Answer (tutor only):** B
- **Explanation (tutor only):** The treatment was applied to whole benches, so the bench (not the plant) is the experimental unit: there is really one replicate per treatment. Plants on a bench share light, temperature and watering, so they aren't independent, and any bench difference is confounded with fertilizer. Fix: randomly assign fertilizer to plants (or pots) across several benches.
- **Why the wrong options are wrong (tutor only):**
  A) 50 per bench would be plenty if the plants were independent.
  C) Nothing suggests the plants measured are unrepresentative of their bench.
  D) Blinding can help, but the core problem is that plants on a bench aren't independent.
  E) With one bench per treatment, any bench difference looks like a fertilizer effect.
- **Hint:** What was randomly assigned: plants or benches?

### rev-exam1-q21-v1
- **Kind:** AI-written version of rev-exam1-q21
- **Concepts:** Samples, populations & bias
- **Type:** MC
- **Question:**

You put one bird feeder in each of two backyards (one with seed A, one with seed B) and count visits by 40 birds at each. What's the main problem?

- **Options:**

  A) Birds at each feeder share a backyard, so they aren't independent
  B) A sample of 40 birds per feeder is far too small to say anything
  C) The researcher should have been blinded to the type of seed
  D) There's no problem with this design for comparing the seeds

- **Answer (tutor only):** A
- **Explanation (tutor only):** Seed type is confounded with backyard; the real replicates are feeders (n = 1 each).
- **Why the wrong options are wrong (tutor only):**
  B) Not the main problem.
  C) Blinding doesn't fix pseudoreplication.
  D) There's a big problem.
- **Hint:** What's the unit of replication?

### rev-exam1-q21-v2
- **Kind:** AI-written version of rev-exam1-q21
- **Concepts:** Samples, populations & bias
- **Type:** MC
- **Question:**

A researcher compares two diets by giving each diet to one cage of 20 mice. How many independent replicates are there per diet?

- **Options:**

  A) 1
  B) 20
  C) 40
  D) 10

- **Answer (tutor only):** A
- **Explanation (tutor only):** Diet was applied to whole cages, so each cage is one replicate; mice in a cage are not independent.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Count mice, not cages.
  D) No basis.
- **Hint:** What received the treatment?

### rev-exam1-q23
- **Kind:** Course original
- **Concepts:** Sampling distribution, SD & SE
- **Type:** MC
- **Question:**

In plain words, the standard error of a sample mean roughly conveys: (pick the best answer)

- **Options:**

  A) How far a typical data point is from the mean
  B) The amount of error introduced by sampling bias
  C) How far a sample mean typically is from the true population mean
  D) The probability that our estimate is wrong
  E) Mistakes made while measuring or recording the data

- **Answer (tutor only):** C
- **Explanation (tutor only):** The SE is the standard deviation of the sampling distribution: how far a sample mean typically lands from the true mean, by chance alone.
- **Why the wrong options are wrong (tutor only):**
  A) That's the standard deviation.
  B) The SE describes chance variation (sampling error), not bias.
  D) The SE isn't a probability.
  E) The SE doesn't measure recording mistakes.
- **Hint:** Is the SE about individual data points or about estimates?

### rev-exam1-q23-v1
- **Kind:** AI-written version of rev-exam1-q23
- **Concepts:** Sampling distribution, SD & SE
- **Type:** MC
- **Question:**

A study reports a mean beak depth of 9.4 mm with a standard error of 0.1 mm. In plain words, the 0.1 mm roughly conveys:

- **Options:**

  A) How far the sample mean typically is from the true mean
  B) How far a typical bird's beak is from the mean beak depth
  C) The probability that the sample mean is wrong
  D) The amount of bias introduced by the sampling method

- **Answer (tutor only):** A
- **Explanation (tutor only):** The SE describes uncertainty in the estimate due to sampling error.
- **Why the wrong options are wrong (tutor only):**
  B) That's the SD.
  C) Not a probability.
  D) The SE doesn't measure bias.
- **Hint:** Uncertainty in the estimate.

### rev-exam1-q23-v2
- **Kind:** AI-written version of rev-exam1-q23
- **Concepts:** Sampling distribution, SD & SE
- **Type:** MC
- **Question:**

Two studies measure the same trait with the same SD, but one has n = 25 and the other n = 100. How do their standard errors compare?

- **Options:**

  A) The n = 100 study's SE is half as large
  B) The n = 100 study's SE is a quarter as large
  C) Both studies have exactly the same SE
  D) The n = 100 study's SE is twice as large

- **Answer (tutor only):** A
- **Explanation (tutor only):** SE = SD / √n; √100 / √25 = 2, so the SE halves.
- **Why the wrong options are wrong (tutor only):**
  B) SE scales with √n.
  C) n differs.
  D) Larger n means smaller SE.
- **Hint:** SD / √n.

### rev-exam1-q24
- **Kind:** Course original
- **Concepts:** Causation & study design
- **Type:** MC
- **Question:**

The key difference between an experimental and an observational study is that, in an experiment: (pick the best answer)

- **Options:**

  A) The study takes place in a lab rather than in the field
  B) The researcher assigns the values of the explanatory variable (ideally at random)
  C) The sample size is larger
  D) There is a comparison group

- **Answer (tutor only):** B
- **Explanation (tutor only):** In an experiment, the researcher sets the explanatory variable, ideally by random assignment, which breaks links with confounders and lets us infer causation.
- **Why the wrong options are wrong (tutor only):**
  A) Experiments can be done in the field, and observational studies in the lab.
  C) Observational studies can be very large.
  D) Observational studies often have comparison groups too.
- **Hint:** Who decides which individuals get which treatment?

### rev-exam1-q24-v1
- **Kind:** AI-written version of rev-exam1-q24
- **Concepts:** Causation & study design
- **Type:** MC
- **Question:**

Which study is an experiment?

- **Options:**

  A) Randomly assigning plants to shade or full sun, then measuring growth
  B) Comparing growth of plants that happen to grow in shade or sun
  C) Measuring growth of plants along a natural light gradient
  D) Surveying gardeners about where their plants grow best

- **Answer (tutor only):** A
- **Explanation (tutor only):** In an experiment the researcher assigns the explanatory variable (ideally at random).
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) observe existing conditions.
- **Hint:** Who sets the explanatory variable?

### rev-exam1-q24-v2
- **Kind:** AI-written version of rev-exam1-q24
- **Concepts:** Causation & study design
- **Type:** MC
- **Question:**

Why does random assignment allow causal conclusions?

- **Options:**

  A) It balances confounders, measured or not, on average
  B) It guarantees a large sample size for the study
  C) It removes all sampling error from the results
  D) It ensures every individual responds the same way

- **Answer (tutor only):** A
- **Explanation (tutor only):** Randomization breaks links between the treatment and other variables, so differences can be attributed to the treatment.
- **Why the wrong options are wrong (tutor only):**
  B) Unrelated.
  C) Sampling error remains.
  D) Individuals still vary.
- **Hint:** What happens to confounders?

## Chapter 13: Linear Models

### ch13-book-01
- **Kind:** Course original
- **Concepts:** Statistical vs scientific models
- **Type:** MC
- **Question:**

What is the key difference between a scientific and a statistical model?

- **Options:**

  A) Statistical models make predictions, scientific models do not
  B) Statistical models can be wrong, scientific models cannot
  C) Statistical models describe patterns, scientific models are built on understanding processes
  D) Statistical models make assumptions, scientific models do not
  E) There are no differences between scientific and statistical models

- **Answer (tutor only):** C
- **Explanation (tutor only):** A statistical model describes patterns in data. A scientific model proposes the process or mechanism that produces them.
- **Why the wrong options are wrong (tutor only):**
  A) Both kinds of models can make predictions.
  B) Both can be wrong.
  D) Both make assumptions.
  E) The distinction is real and useful.
- **Hint:** Which kind of model tries to explain why the pattern exists?

### ch13-book-01-v1
- **Kind:** AI-written version of ch13-book-01
- **Concepts:** Statistical vs scientific models
- **Type:** MC
- **Question:**

A researcher says, "Warmer water speeds up fish metabolism, so fish in warm lakes grow faster." Another fits lm(growth ~ temperature). Which is the scientific model and which is the statistical model?

- **Options:**

  A) The metabolism idea is scientific; the lm() is statistical
  B) The lm() is scientific; the metabolism idea is statistical
  C) Both are statistical models of the same pattern
  D) Both are scientific models of the same process

- **Answer (tutor only):** A
- **Explanation (tutor only):** The metabolism idea proposes a process. The regression describes a pattern in the data.
- **Why the wrong options are wrong (tutor only):**
  Scientific models explain how; statistical models describe what the data look like.
- **Hint:** Which one proposes a mechanism?

### ch13-book-01-v2
- **Kind:** AI-written version of ch13-book-01
- **Concepts:** Statistical vs scientific models
- **Type:** MC
- **Question:**

Which statement about scientific and statistical models is true?

- **Options:**

  A) Statistical models describe patterns; scientific models propose processes
  B) Scientific models are always correct; statistical models can be wrong
  C) Only statistical models can be used to make predictions about data
  D) Only scientific models make assumptions about the world

- **Answer (tutor only):** A
- **Explanation (tutor only):** Statistical models summarize patterns in data; scientific models are built on ideas about the processes that generate them. Both can be wrong, make predictions and rest on assumptions.
- **Why the wrong options are wrong (tutor only):**
  B) Both can be wrong.
  C) Scientific models make predictions too.
  D) Statistical models have assumptions too.
- **Hint:** Pattern vs process.

### ch13-book-02
- **Kind:** Course original
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

Consider this code and output:

lm(bill_depth_mm ~ 1, penguins)

Coefficients:
(Intercept)
      17.15

The (Intercept) describes:

- **Options:**

  A) The mean bill depth of penguins in this dataset
  B) The mean bill depth of all penguins
  C) The mean bill depth of penguins of the "reference level" species
  D) The expected bill depth if all the predictors are set to zero

- **Answer (tutor only):** A
- **Explanation (tutor only):** With only an intercept, the model's single prediction is the sample mean: the mean bill depth of the penguins in this dataset.
- **Why the wrong options are wrong (tutor only):**
  B) It's an estimate from this sample, not the true mean of all penguins (a parameter).
  C) Species isn't in this model.
  D) There are no predictors here, so there's nothing to set to zero.
- **Hint:** Is 17.15 calculated from a sample or from every penguin?

### ch13-book-02-v1
- **Kind:** AI-written version of ch13-book-02
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

lm(flipper_length_mm ~ 1, penguins)

Coefficients:
(Intercept)
      200.9

The (Intercept) describes:

- **Options:**

  A) The mean flipper length of the penguins in this dataset
  B) The mean flipper length of all penguins in the world
  C) The mean flipper length of the reference-level species
  D) The expected flipper length when body mass is zero

- **Answer (tutor only):** A
- **Explanation (tutor only):** An intercept-only model predicts the sample mean of the response.
- **Why the wrong options are wrong (tutor only):**
  B) It's an estimate from a sample, not the population value.
  C) No species term is in the model.
  D) No body mass term is in the model.
- **Hint:** What does ~ 1 estimate?

### ch13-book-02-v2
- **Kind:** AI-written version of ch13-book-02
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

lm(bill_depth_mm ~ 1, penguins) gives an intercept of 17.15. What would the model predict for the bill depth of a Gentoo penguin with a 50 mm bill?

- **Options:**

  A) 17.15 mm, the same prediction as for any penguin
  B) It can't predict, since species isn't in the model
  C) 17.15 mm plus the Gentoo species coefficient
  D) 17.15 mm plus 50 times the bill length slope

- **Answer (tutor only):** A
- **Explanation (tutor only):** With no predictors, every penguin gets the same prediction: the sample mean, 17.15 mm.
- **Why the wrong options are wrong (tutor only):**
  B) It can predict; it just ignores species.
  C) and D) There are no species or bill length terms in this model.
- **Hint:** How many different predictions can an intercept-only model make?

### ch13-book-03
- **Kind:** Course original
- **Concepts:** Categorical predictors & reference levels
- **Type:** MC
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

Without running it, which sex will be the reference level in lm(bill_length_mm ~ sex, penguins)? The two values of sex are "female" and "male".

- **Options:**

  A) male
  B) female
  C) whichever has the smaller mean
  D) impossible to predict

- **Answer (tutor only):** B
- **Explanation (tutor only):** By default, R uses the first level in alphabetical order as the reference. "female" comes before "male".
- **Why the wrong options are wrong (tutor only):**
  A) "male" comes second alphabetically.
  C) R doesn't look at the means when choosing the reference.
  D) The default rule (alphabetical) makes it predictable.
- **Hint:** How does R order the levels of a categorical variable by default?

### ch13-book-03-v1
- **Kind:** AI-written version of ch13-book-03
- **Concepts:** Categorical predictors & reference levels
- **Type:** MC
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

Without running it, which species will be the reference level in lm(bill_length_mm ~ species, penguins)? The species are Adelie, Chinstrap and Gentoo.

- **Options:**

  A) Adelie
  B) Chinstrap
  C) Gentoo
  D) Whichever species has the most penguins

- **Answer (tutor only):** A
- **Explanation (tutor only):** By default R uses the first level alphabetically. Adelie comes first.
- **Why the wrong options are wrong (tutor only):**
  Sample size and means don't set the default reference.
- **Hint:** Alphabetical order.

### ch13-book-03-v2
- **Kind:** AI-written version of ch13-book-03
- **Concepts:** Categorical predictors & reference levels
- **Type:** MC
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

Penguins were sampled on three islands: Biscoe, Dream and Torgersen. Without running it, which island will be the reference level in lm(body_mass_g ~ island, penguins)?

- **Options:**

  A) Biscoe
  B) Dream
  C) Torgersen
  D) Whichever island has the lightest penguins

- **Answer (tutor only):** A
- **Explanation (tutor only):** R uses the first level alphabetically as the reference: Biscoe.
- **Why the wrong options are wrong (tutor only):**
  Means don't set the default reference level.
- **Hint:** Alphabetical order.

### ch13-book-04
- **Kind:** Course original
- **Concepts:** Categorical predictors & reference levels; Coefficients & predictions
- **Type:** numeric
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

Consider this output:

lm(bill_length_mm ~ species, penguins)

Coefficients:
     (Intercept)  speciesChinstrap     speciesGentoo
          38.791            10.042             8.713

What is the mean bill length of Chinstrap penguins in the dataset?

- **Answer (tutor only):** 48.833
- **Explanation (tutor only):** Adelie is the reference, so 38.791 is the Adelie mean. Chinstrap mean = 38.791 + 10.042 = 48.833.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: answering 10.042, which is the Chinstrap minus Adelie difference.
- **Hint:** Which species does the intercept describe?

### ch13-book-04-v1
- **Kind:** AI-written version of ch13-book-04
- **Concepts:** Categorical predictors & reference levels; Coefficients & predictions
- **Type:** numeric
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

lm(bill_length_mm ~ species, penguins)

     (Intercept)  speciesChinstrap     speciesGentoo
          38.791            10.042             8.713

What is the mean bill length of Gentoo penguins in the dataset?

- **Answer (tutor only):** 47.504
- **Explanation (tutor only):** Adelie is the reference (38.791). Gentoo = 38.791 + 8.713 = 47.504.
- **Hint:** Intercept + the Gentoo coefficient.

### ch13-book-04-v2
- **Kind:** AI-written version of ch13-book-04
- **Concepts:** Categorical predictors & reference levels; Coefficients & predictions
- **Type:** numeric
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

lm(bill_length_mm ~ species, penguins)

     (Intercept)  speciesChinstrap     speciesGentoo
          38.791            10.042             8.713

What is the mean bill length of Adelie penguins in the dataset?

- **Answer (tutor only):** 38.791
- **Explanation (tutor only):** Adelie is the reference level, so its mean is the intercept: 38.791.
- **Hint:** Which species has no coefficient of its own?

### ch13-book-05
- **Kind:** Course original
- **Concepts:** Categorical predictors & reference levels; Coefficients & predictions
- **Type:** numeric
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

lm(bill_length_mm ~ species, penguins)

     (Intercept)  speciesChinstrap     speciesGentoo
          38.791            10.042             8.713

How many mm longer are Chinstrap bills than Gentoo bills, on average, in this dataset?

- **Answer (tutor only):** 1.329
- **Explanation (tutor only):** Both coefficients are differences from Adelie, so the Chinstrap minus Gentoo difference is 10.042 - 8.713 = 1.329. The intercept cancels out.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: answering 10.042 or 8.713. Each of those compares a species to Adelie, not to each other.
- **Hint:** Both coefficients are measured from the same starting point.

### ch13-book-05-v1
- **Kind:** AI-written version of ch13-book-05
- **Concepts:** Categorical predictors & reference levels; Coefficients & predictions
- **Type:** numeric
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

lm(bill_length_mm ~ species, penguins)

     (Intercept)  speciesChinstrap     speciesGentoo
          38.791            10.042             8.713

How many mm longer are Gentoo bills than Adelie bills, on average, in this dataset?

- **Answer (tutor only):** 8.713
- **Explanation (tutor only):** Adelie is the reference, so the Gentoo coefficient (8.713) is exactly the Gentoo - Adelie difference.
- **Hint:** What does a coefficient for a non-reference level measure?

### ch13-book-05-v2
- **Kind:** AI-written version of ch13-book-05
- **Concepts:** Categorical predictors & reference levels; Coefficients & predictions
- **Type:** numeric
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

lm(bill_length_mm ~ species, penguins)

     (Intercept)  speciesChinstrap     speciesGentoo
          38.791            10.042             8.713

How many mm shorter are Gentoo bills than Chinstrap bills, on average, in this dataset?

- **Answer (tutor only):** 1.329
- **Explanation (tutor only):** Chinstrap - Gentoo = 10.042 - 8.713 = 1.329 mm. The intercept cancels.
- **Hint:** Subtract the two coefficients.

### ch13-book-06
- **Kind:** Course original
- **Concepts:** Categorical predictors & reference levels
- **Type:** MC
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

Using only this output:

lm(bill_length_mm ~ species, penguins)

     (Intercept)  speciesChinstrap     speciesGentoo
          38.791            10.042             8.713

What is the mean bill length of all penguins in this dataset?

- **Options:**

  A) 38.791
  B) 19.182
  C) 45.042 (the average of the three species means)
  D) Not enough information

- **Answer (tutor only):** D
- **Explanation (tutor only):** The overall mean depends on how many penguins of each species there are. The output gives the three species means but not the sample sizes, so we can't weight them.
- **Why the wrong options are wrong (tutor only):**
  A) That's the Adelie (reference) mean.
  B) That's just the sum of the two coefficients.
  C) Averaging the species means is only right if every species has the same sample size.
- **Hint:** Would the overall mean change if there were many more Adelie penguins than Chinstraps?

### ch13-book-06-v1
- **Kind:** AI-written version of ch13-book-06
- **Concepts:** Categorical predictors & reference levels
- **Type:** MC
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

lm(bill_length_mm ~ species, penguins)

     (Intercept)  speciesChinstrap     speciesGentoo
          38.791            10.042             8.713

The dataset has 151 Adelie, 68 Chinstrap and 123 Gentoo penguins. Why isn't the overall mean bill length simply the average of the three species means?

- **Options:**

  A) The species have different sample sizes, so their means need weighting
  B) The intercept is already the mean bill length of all the penguins
  C) Species means can't be combined because they come from a model
  D) It is; the overall mean always equals the average of group means

- **Answer (tutor only):** A
- **Explanation (tutor only):** The overall mean weights each species by its number of penguins. Adelie (151) counts more than Chinstrap (68).
- **Why the wrong options are wrong (tutor only):**
  B) The intercept is the Adelie mean.
  C) Model-based group means are just the sample means here.
  D) Only true when groups are the same size.
- **Hint:** Each penguin counts once.

### ch13-book-06-v2
- **Kind:** AI-written version of ch13-book-06
- **Concepts:** Categorical predictors & reference levels
- **Type:** MC
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

lm(bill_length_mm ~ species, penguins)

     (Intercept)  speciesChinstrap     speciesGentoo
          38.791            10.042             8.713

Which of these can you calculate using ONLY this output?

- **Options:**

  A) The mean bill length of Gentoo penguins
  B) The mean bill length of all penguins
  C) The number of Chinstrap penguins sampled
  D) The standard deviation of Adelie bills

- **Answer (tutor only):** A
- **Explanation (tutor only):** Gentoo mean = 38.791 + 8.713. The overall mean needs sample sizes; counts and SDs aren't in the coefficients.
- **Why the wrong options are wrong (tutor only):**
  B) Needs the sample size of each species.
  C) and D) Coefficients don't report counts or spread.
- **Hint:** Coefficients give group means, nothing more.

### ch13-book-07
- **Kind:** Course original
- **Concepts:** Regression from summaries
- **Type:** numeric
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

Use these summaries to model bill depth (response) as a function of bill length (explanatory):

mean_depth | mean_length | cov | sd_depth | sd_length
17.59 | 46.57 | 0.62 | 0.78 | 3.11

(Bill depth ranges from 16.4 to 19.4 mm, bill length from 40.9 to 58 mm, n = 34.)

What is the correlation between bill depth and bill length?

- **Answer (tutor only):** 0.256
- **Explanation (tutor only):** r = cov / (sd_x × sd_y) = 0.62 / (3.11 × 0.78) = 0.256.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: dividing by the variance of x (that gives the slope, 0.064).
- **Hint:** r = cov(x, y) / (sd(x) × sd(y)).

### ch13-book-07-v1
- **Kind:** AI-written version of ch13-book-07
- **Concepts:** Regression from summaries
- **Type:** numeric
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

For 34 penguins:

mean_depth | mean_length | cov | sd_depth | sd_length
17.59 | 46.57 | 0.62 | 0.78 | 3.11

What is the variance of bill length?

- **Answer (tutor only):** 9.67
- **Explanation (tutor only):** Variance = SD² = 3.11² = 9.67.
- **Hint:** Square the SD.

### ch13-book-07-v2
- **Kind:** AI-written version of ch13-book-07
- **Concepts:** Regression from summaries
- **Type:** numeric
- **Question:**

For 40 lizards, the covariance between body length and sprint speed is 1.2, the SD of body length is 2.0 and the SD of sprint speed is 1.5. What is the correlation between body length and sprint speed?

- **Answer (tutor only):** 0.4
- **Explanation (tutor only):** r = cov / (sd_x × sd_y) = 1.2 / (2.0 × 1.5) = 0.40.
- **Hint:** Divide the covariance by the product of the SDs.

### ch13-book-08
- **Kind:** Course original
- **Concepts:** Regression from summaries
- **Type:** numeric
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

For 34 penguins, we model bill depth (response) as a function of bill length (explanatory) using these summaries:

mean_depth | mean_length | cov | sd_depth | sd_length
17.59 | 46.57 | 0.62 | 0.78 | 3.11

What is the slope of the regression of bill depth (response) on bill length (explanatory)?

- **Answer (tutor only):** 0.0641
- **Explanation (tutor only):** b = cov(x, y) / var(x) = 0.62 / 3.11² = 0.62 / 9.67 = 0.0641 mm of depth per mm of length.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: dividing by sd(x) instead of var(x) (0.199), or using the response's variance.
- **Hint:** b = cov(x, y) / var(x), and var(x) = sd(x)².

### ch13-book-08-v1
- **Kind:** AI-written version of ch13-book-08
- **Concepts:** Regression from summaries
- **Type:** numeric
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

For 34 penguins, we model bill length (response) as a function of bill depth (explanatory):

mean_depth | mean_length | cov | sd_depth | sd_length
17.59 | 46.57 | 0.62 | 0.78 | 3.11

What is the slope of the regression of bill LENGTH on bill DEPTH?

- **Answer (tutor only):** 1.02
- **Explanation (tutor only):** b = cov / var(x). Now depth is x: 0.62 / 0.78² = 0.62 / 0.608 = 1.02 mm of length per mm of depth.
- **Hint:** Divide by the variance of the explanatory variable (depth).

### ch13-book-08-v2
- **Kind:** AI-written version of ch13-book-08
- **Concepts:** Regression from summaries
- **Type:** numeric
- **Question:**

For 40 lizards, the covariance between body length (explanatory) and sprint speed (response) is 1.2, and the SD of body length is 2.0. What is the slope of the regression of sprint speed on body length?

- **Answer (tutor only):** 0.3
- **Explanation (tutor only):** b = cov / var(x) = 1.2 / 2.0² = 1.2 / 4 = 0.30.
- **Hint:** var(x) = SD².

### ch13-book-09
- **Kind:** Course original
- **Concepts:** Regression from summaries
- **Type:** numeric
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

For 34 penguins, mean bill depth = 17.59 mm and mean bill length = 46.57 mm. Given a slope of 0.0641, what is the intercept of the regression of bill depth on bill length?

- **Answer (tutor only):** 14.6
- **Explanation (tutor only):** a = mean(y) - b × mean(x) = 17.59 - 0.0641 × 46.57 = 17.59 - 2.99 = 14.6. A regression line always passes through the point (mean x, mean y).
- **Why the wrong options are wrong (tutor only):**
  Common mistake: using mean(x) in place of mean(y).
- **Hint:** The line passes through (mean bill length, mean bill depth).

### ch13-book-09-v1
- **Kind:** AI-written version of ch13-book-09
- **Concepts:** Regression from summaries
- **Type:** numeric
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

For 34 penguins, mean bill depth = 17.59 mm and mean bill length = 46.57 mm. The regression of bill depth on bill length has slope 0.0641. What does the model predict for a penguin with an average bill length (46.57 mm)?

- **Answer (tutor only):** 17.59
- **Explanation (tutor only):** A regression line always passes through (mean x, mean y), so the prediction at mean length is mean depth: 17.59 mm.
- **Hint:** Where does every regression line pass?

### ch13-book-09-v2
- **Kind:** AI-written version of ch13-book-09
- **Concepts:** Regression from summaries
- **Type:** numeric
- **Question:**

For 40 lizards, mean body length is 10 cm and mean sprint speed is 5 m/s. The regression of sprint speed on body length has slope 0.30. What is the intercept?

- **Answer (tutor only):** 2
- **Explanation (tutor only):** a = mean(y) - b × mean(x) = 5 - 0.30 × 10 = 2.0.
- **Hint:** The line passes through (mean x, mean y).

### ch13-book-10
- **Kind:** Course original
- **Concepts:** Coefficients & predictions; Residuals & model fit
- **Type:** numeric
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

For 34 penguins, the regression of bill depth on bill length has intercept 14.6 and slope 0.0641. A penguin has a bill 50 mm long and 20 mm deep. What is its residual (in mm)?

- **Answer (tutor only):** 2.19
- **Explanation (tutor only):** Prediction = 14.6 + 0.0641 × 50 = 17.81 mm. Residual = 20 - 17.81 = 2.19 mm.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: predicted - observed (-2.19).
- **Hint:** Predict first, then subtract the prediction from the observed depth.

### ch13-book-10-v1
- **Kind:** AI-written version of ch13-book-10
- **Concepts:** Coefficients & predictions; Residuals & model fit
- **Type:** numeric
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

For 34 penguins, the regression of bill depth on bill length has intercept 14.6 and slope 0.0641. A penguin has a bill 45 mm long and 16.5 mm deep. What is its residual (in mm)?

- **Answer (tutor only):** -0.98
- **Explanation (tutor only):** Prediction = 14.6 + 0.0641 × 45 = 17.48. Residual = 16.5 - 17.48 = -0.98.
- **Hint:** Residual = observed - predicted.

### ch13-book-10-v2
- **Kind:** AI-written version of ch13-book-10
- **Concepts:** Coefficients & predictions; Residuals & model fit
- **Type:** numeric
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

For 34 penguins, the regression of bill depth on bill length has intercept 14.6 and slope 0.0641. What bill depth does the model predict for a penguin with a 55 mm bill?

- **Answer (tutor only):** 18.13
- **Explanation (tutor only):** 14.6 + 0.0641 × 55 = 14.6 + 3.53 = 18.13 mm.
- **Hint:** Intercept + slope × length.

### ch13-book-11
- **Kind:** Course original
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

The regression of bill depth on bill length (intercept 14.6, slope 0.0641) was fit to penguins with bill lengths from 40.9 to 58 mm. What should we make of its prediction for a penguin with a 500 mm long bill?

- **Options:**

  A) It's about 46.7 mm, and we can trust it because the formula gives an answer
  B) It's not trustworthy: 500 mm is far outside the range of the data, so this is an extrapolation
  C) The model can't produce a number for x = 500
  D) It's trustworthy because the correlation is positive

- **Answer (tutor only):** B
- **Explanation (tutor only):** The formula will happily give 14.6 + 0.0641 × 500 = 46.7 mm, but the model only describes bill lengths between about 41 and 58 mm. Nothing tells us the relationship stays a straight line (or that such a penguin could exist) far outside that range.
- **Why the wrong options are wrong (tutor only):**
  A) Getting a number is not the same as getting a sensible prediction.
  C) The equation works for any x; the problem is whether to believe it.
  D) A positive correlation within the data says nothing about values far beyond it.
- **Hint:** What range of bill lengths was the model built on?

### ch13-book-11-v1
- **Kind:** AI-written version of ch13-book-11
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

The regression of bill depth on bill length (intercept 14.6, slope 0.0641) was fit to penguins with bill lengths from 40.9 to 58 mm. Which prediction is most trustworthy?

- **Options:**

  A) The prediction for a bill 50 mm long
  B) The prediction for a bill 5 mm long
  C) The prediction for a bill 100 mm long
  D) They are all equally trustworthy

- **Answer (tutor only):** A
- **Explanation (tutor only):** 50 mm lies within the data (40.9 to 58 mm). The others are extrapolations.
- **Why the wrong options are wrong (tutor only):**
  B) and C) are far outside the data.
  D) Predictions outside the data range are not trustworthy.
- **Hint:** Which one is inside the range of the data?

### ch13-book-11-v2
- **Kind:** AI-written version of ch13-book-11
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

The regression of bill depth on bill length (intercept 14.6, slope 0.0641) was fit to penguins with bill lengths from 40.9 to 58 mm. Why shouldn't we interpret the intercept (14.6 mm) as the bill depth of a penguin with no bill?

- **Options:**

  A) A bill length of 0 mm is far outside the data, so it's an extrapolation
  B) The intercept is the mean bill depth, not a prediction for any penguin
  C) The intercept is only meaningful when the slope is negative
  D) We should; 14.6 mm is the expected depth of a bill 0 mm long

- **Answer (tutor only):** A
- **Explanation (tutor only):** The intercept is the prediction at x = 0, which is far outside the observed bill lengths, so it has no biological meaning here.
- **Why the wrong options are wrong (tutor only):**
  B) The mean depth is 17.59, not 14.6.
  C) The slope's sign doesn't matter.
  D) The math gives a number, but it's an extrapolation.
- **Hint:** Is 0 mm within the range of the data?

### ch13-book-12
- **Kind:** Course original
- **Concepts:** Coefficients & predictions; Residuals & model fit
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch13-book-gentoo-resid.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch13-book-gentoo-resid.png)
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

The figure shows bill depth vs bill length for Gentoo penguins. Solid lines are predictions from lm(bill_depth_mm ~ bill_length_mm + sex); dashed lines are separate fits for each sex.

The male penguin with a bill about 56 mm long (the second point from the right) has a bill depth of 17.0 mm. Using the solid male line, approximate its residual.

- **Answer (tutor only):** 0.68
- **Explanation (tutor only):** Read the solid male line at 56 mm: about 16.3 mm. Residual = 17.0 - 16.3 ≈ 0.7 mm (the model gives 16.32, so 0.68). The point sits a bit above its line.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: using the female line, or the dashed (separate fit) line instead of the model's solid line.
- **Hint:** Find the solid male line at 56 mm, then compare it to the point.

### ch13-book-12-v1
- **Kind:** AI-written version of ch13-book-12
- **Concepts:** Coefficients & predictions; Residuals & model fit
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch13-book-gentoo-resid.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch13-book-gentoo-resid.png)
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

The figure shows bill depth vs bill length for Gentoo penguins. Solid lines are predictions from lm(bill_depth_mm ~ bill_length_mm + sex); dashed lines are separate fits for each sex.

The model's solid male line predicts a bill depth of about 16.3 mm at 56 mm. A male with a 56 mm bill has a residual of 0.7 mm. What is its actual bill depth?

- **Answer (tutor only):** 17
- **Explanation (tutor only):** Observed = predicted + residual = 16.3 + 0.7 = 17.0 mm.
- **Hint:** Residual = observed - predicted.

### ch13-book-12-v2
- **Kind:** AI-written version of ch13-book-12
- **Concepts:** Coefficients & predictions; Residuals & model fit
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch13-book-gentoo-resid.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch13-book-gentoo-resid.png)
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

The figure shows bill depth vs bill length for Gentoo penguins. Solid lines are predictions from lm(bill_depth_mm ~ bill_length_mm + sex); dashed lines are separate fits for each sex.

A female Gentoo has a bill 46 mm long and 13.6 mm deep. The solid female line predicts about 14.3 mm at that length. What is her residual?

- **Answer (tutor only):** -0.7
- **Explanation (tutor only):** Residual = 13.6 - 14.3 = -0.7 mm. She sits below her line.
- **Hint:** Residual = observed - predicted.

### ch13-book-13
- **Kind:** Course original
- **Concepts:** Coefficients & predictions
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch13-book-gentoo-resid.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch13-book-gentoo-resid.png)
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

The figure shows Gentoo bill depth vs bill length, with solid lines from lm(bill_depth_mm ~ bill_length_mm + sex) and dashed lines from separate fits for each sex. Which of the following are nearly identical for male and female Gentoo penguins? (Select all that apply.)

- **Options:**

  A) Mean bill lengths
  B) Mean bill depths
  C) Slopes
  D) Intercepts

- **Answer (tutor only):** C
- **Explanation (tutor only):** The separate (dashed) lines for males and females are nearly parallel, so the slopes are similar. Males sit higher (deeper bills) and to the right (longer bills), so means and intercepts differ.
- **Why the wrong options are wrong (tutor only):**
  A) and B) The male points are shifted right and up: males have longer and deeper bills.
  D) The lines are parallel but offset vertically, so their intercepts differ.
- **Hint:** Compare the dashed lines: are they parallel? Are they on top of each other?

### ch13-book-13-v1
- **Kind:** AI-written version of ch13-book-13
- **Concepts:** Coefficients & predictions
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch13-book-gentoo-resid.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch13-book-gentoo-resid.png)
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

The figure shows Gentoo bill depth vs bill length, with solid lines from lm(bill_depth_mm ~ bill_length_mm + sex) and dashed lines from separate fits for each sex. Which of the following differ clearly between male and female Gentoo penguins? (Select all that apply.)

- **Options:**

  A) Mean bill lengths
  B) Mean bill depths
  C) Slopes
  D) Intercepts

- **Answer (tutor only):** A, B, D
- **Explanation (tutor only):** Males have longer and deeper bills (different means) and their line sits higher (different intercept), but the slopes are nearly the same (parallel dashed lines).
- **Why the wrong options are wrong (tutor only):**
  C) The dashed lines are nearly parallel.
- **Hint:** Look at where the clouds sit, and whether the dashed lines are parallel.

### ch13-book-13-v2
- **Kind:** AI-written version of ch13-book-13
- **Concepts:** Coefficients & predictions
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch13-book-gentoo-resid.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch13-book-gentoo-resid.png)
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

The figure shows Gentoo bill depth vs bill length, with solid lines from lm(bill_depth_mm ~ bill_length_mm + sex) and dashed lines from separate fits for each sex. Why are the solid lines from the model exactly parallel?

- **Options:**

  A) The additive model gives both sexes one shared slope
  B) Males and females have exactly the same mean bill length
  C) The dashed separate fits are also exactly parallel
  D) Bill depth was measured more precisely for one sex

- **Answer (tutor only):** A
- **Explanation (tutor only):** Without an interaction, the model estimates one bill length slope for both sexes; sex only shifts the line up or down.
- **Why the wrong options are wrong (tutor only):**
  B) The means differ.
  C) The dashed lines are close but not exactly parallel.
  D) Measurement precision doesn't set the slope.
- **Hint:** How many slopes does bill_length_mm + sex estimate?

### ch13-book-14
- **Kind:** Course original
- **Concepts:** Residuals & model fit
- **Type:** numeric
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

For Chinstrap penguins, lm(flipper_length_mm ~ body_mass_g + sex) has a residual standard error of 5.186 on 65 degrees of freedom. What is the sum of squared residuals?

- **Answer (tutor only):** 1748
- **Explanation (tutor only):** Residual SE = √(sum of squares / df). So sum of squares = SE² × df = 5.186² × 65 = 26.89 × 65 = 1748.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: SE × df (337), forgetting to square.
- **Hint:** Undo the square root, then undo the division by df.

### ch13-book-14-v1
- **Kind:** AI-written version of ch13-book-14
- **Concepts:** Residuals & model fit
- **Type:** numeric
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

For Chinstrap penguins, lm(flipper_length_mm ~ body_mass_g + sex) has a sum of squared residuals of 1748 on 65 degrees of freedom. What is the residual standard error?

- **Answer (tutor only):** 5.19
- **Explanation (tutor only):** Residual SE = √(SS / df) = √(1748 / 65) = √26.89 = 5.19.
- **Hint:** Divide by df, then take the square root.

### ch13-book-14-v2
- **Kind:** AI-written version of ch13-book-14
- **Concepts:** Residuals & model fit
- **Type:** numeric
- **Question:**

Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

For Chinstrap penguins, lm(flipper_length_mm ~ body_mass_g + sex) has a residual standard error of 5.186 on 65 degrees of freedom. What is the mean square residual (the residual variance)?

- **Answer (tutor only):** 26.89
- **Explanation (tutor only):** Mean square = residual SE² = 5.186² = 26.89.
- **Hint:** Square the residual SE.

### ch13-chimein-01
- **Kind:** Course original
- **Concepts:** Categorical predictors & reference levels; Coefficients & predictions
- **Type:** numeric
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica).

Consider this model of iris sepal length as a function of species:

lm(Sepal.Length ~ Species, data = iris)

Coefficients:
      (Intercept)  Speciesversicolor   Speciesvirginica
            5.006              0.930              1.582

What is the predicted (mean) sepal length of virginica flowers?

- **Answer (tutor only):** 6.588
- **Explanation (tutor only):** setosa is the reference level, so the intercept (5.006) is the setosa mean. Add the virginica coefficient: 5.006 + 1.582 = 6.588.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: answering 1.582. That's the difference between virginica and setosa, not the virginica mean.
- **Hint:** Which species is the reference level (it has no coefficient of its own)?

### ch13-chimein-01-v1
- **Kind:** AI-written version of ch13-chimein-01
- **Concepts:** Categorical predictors & reference levels; Coefficients & predictions
- **Type:** numeric
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica).

lm(Sepal.Length ~ Species, data = iris)

      (Intercept)  Speciesversicolor   Speciesvirginica
            5.006              0.930              1.582

What is the predicted (mean) sepal length of versicolor flowers?

- **Answer (tutor only):** 5.936
- **Explanation (tutor only):** setosa is the reference (intercept 5.006). versicolor: 5.006 + 0.930 = 5.936.
- **Hint:** Intercept + the versicolor coefficient.

### ch13-chimein-01-v2
- **Kind:** AI-written version of ch13-chimein-01
- **Concepts:** Categorical predictors & reference levels; Coefficients & predictions
- **Type:** numeric
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica).

lm(Sepal.Length ~ Species, data = iris)

      (Intercept)  Speciesversicolor   Speciesvirginica
            5.006              0.930              1.582

How much longer are virginica sepals than versicolor sepals, on average?

- **Answer (tutor only):** 0.652
- **Explanation (tutor only):** Both coefficients are differences from setosa, so virginica - versicolor = 1.582 - 0.930 = 0.652.
- **Hint:** The intercept cancels out.

### ch13-chimein-02
- **Kind:** Course original
- **Concepts:** Categorical predictors & reference levels; Residuals & model fit
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch13-chimein-iris-AB.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch13-chimein-iris-AB.png)
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica).

The plot shows iris sepal lengths by species. Black lines are the species means from:

lm(Sepal.Length ~ Species, data = iris)

      (Intercept)  Speciesversicolor   Speciesvirginica
            5.006              0.930              1.582

What is the residual for data point B?

- **Answer (tutor only):** -0.788
- **Explanation (tutor only):** Point B is a virginica flower with a sepal length of 5.8 cm. The model predicts the virginica mean for it: 5.006 + 1.582 = 6.588. Residual = 5.8 - 6.588 = -0.788. B sits below its species' line, so its residual is negative.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: using the setosa mean (5.006) as B's prediction, or subtracting in the wrong order (+0.788).
- **Hint:** Which species is B? What does the model predict for every flower of that species?

### ch13-chimein-02-v1
- **Kind:** AI-written version of ch13-chimein-02
- **Concepts:** Categorical predictors & reference levels; Residuals & model fit
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch13-chimein-iris-AB.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch13-chimein-iris-AB.png)
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica).

The plot shows iris sepal lengths by species. Black lines are the species means from:

lm(Sepal.Length ~ Species, data = iris)

      (Intercept)  Speciesversicolor   Speciesvirginica
            5.006              0.930              1.582

What is the model's predicted value (fitted value) for data point B?

- **Answer (tutor only):** 6.588
- **Explanation (tutor only):** Point B is a virginica flower, so its prediction is the virginica mean: 5.006 + 1.582 = 6.588.
- **Hint:** Every flower of a species gets the same prediction.

### ch13-chimein-02-v2
- **Kind:** AI-written version of ch13-chimein-02
- **Concepts:** Categorical predictors & reference levels; Residuals & model fit
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch13-chimein-iris-AB.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch13-chimein-iris-AB.png)
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica).

The plot shows iris sepal lengths by species. Black lines are the species means from:

lm(Sepal.Length ~ Species, data = iris)

      (Intercept)  Speciesversicolor   Speciesvirginica
            5.006              0.930              1.582

Data point B has a sepal length of 5.8 cm. Is its residual positive or negative, and how big is it?

- **Answer (tutor only):** -0.788
- **Explanation (tutor only):** B is virginica: predicted 6.588. Residual = 5.8 - 6.588 = -0.788. Negative, because B is below its species' line.
- **Hint:** Residual = observed - the virginica mean.

### ch13-chimein-03
- **Kind:** Course original
- **Concepts:** Categorical predictors & reference levels; Residuals & model fit
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch13-chimein-iris-AB.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch13-chimein-iris-AB.png)
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). The plot shows iris sepal lengths by species; black lines are the species means from lm(Sepal.Length ~ Species):

      (Intercept)  Speciesversicolor   Speciesvirginica
            5.006              0.930              1.582

What is the residual for data point A?

- **Answer (tutor only):** 0.694
- **Explanation (tutor only):** Point A is a setosa flower with a sepal length of 5.7 cm. Setosa is the reference level, so its prediction is the intercept, 5.006. Residual = 5.7 - 5.006 = 0.694.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: reading A's value off the wrong gridline. Each faint line is 0.1 cm.
- **Hint:** Setosa has no coefficient of its own. What does that tell you about its prediction?

### ch13-chimein-03-v1
- **Kind:** AI-written version of ch13-chimein-03
- **Concepts:** Categorical predictors & reference levels; Residuals & model fit
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch13-chimein-iris-AB.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch13-chimein-iris-AB.png)
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). The plot shows iris sepal lengths by species; black lines are the species means from lm(Sepal.Length ~ Species):

      (Intercept)  Speciesversicolor   Speciesvirginica
            5.006              0.930              1.582

What is the model's predicted value for data point A?

- **Answer (tutor only):** 5.006
- **Explanation (tutor only):** Point A is a setosa flower. Setosa is the reference level, so its prediction is the intercept, 5.006.
- **Hint:** Which species is the reference level?

### ch13-chimein-03-v2
- **Kind:** AI-written version of ch13-chimein-03
- **Concepts:** Categorical predictors & reference levels; Residuals & model fit
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch13-chimein-iris-AB.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch13-chimein-iris-AB.png)
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). The plot shows iris sepal lengths by species; black lines are the species means from lm(Sepal.Length ~ Species):

      (Intercept)  Speciesversicolor   Speciesvirginica
            5.006              0.930              1.582

Point A has a sepal length of 5.7 cm. What would its residual be if it were a versicolor flower instead of setosa?

- **Answer (tutor only):** -0.236
- **Explanation (tutor only):** The versicolor prediction is 5.006 + 0.930 = 5.936, so the residual would be 5.7 - 5.936 = -0.236.
- **Hint:** Use the versicolor mean as the prediction.

### ch13-hw-01
- **Kind:** Course original
- **Concepts:** Statistical vs scientific models
- **Type:** select-all
- **Question:**

Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. Which of the following are scientific models? (Select all that apply. A scientific model need not be correct.)

- **Options:**

  A) A theory that compounds in chocolate improve brain function, leading to more Nobel-worthy discoveries
  B) A model describing how research funding, education systems, cultural values, and a society's wealth to spend on luxuries like chocolate interact to shape Nobel Prize rates
  C) A regression showing that for every additional 0.5 kg of chocolate consumed per person per year, the number of Nobel laureates per 10 million people increases by 2

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** Scientific models propose mechanisms (brain chemistry; funding, education and wealth). A regression describes a pattern in data and knows nothing about brains or funding, so it is a statistical model.
- **Why the wrong options are wrong (tutor only):**
  C) A regression is a statistical model: it summarizes the pattern without explaining what causes it.
- **Hint:** Which options propose a process that could produce the pattern?

### ch13-hw-01-v1
- **Kind:** AI-written version of ch13-hw-01
- **Concepts:** Statistical vs scientific models
- **Type:** select-all
- **Question:**

Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year. Which of the following are statistical (not scientific) models? (Select all that apply.)

- **Options:**

  A) A regression of Nobel laureates per 10 million people on chocolate consumption
  B) An idea that flavonoids in chocolate improve memory, boosting scientific output
  C) A correlation coefficient describing how chocolate and Nobel prizes covary
  D) An idea that wealthy countries both fund science and buy more luxuries like chocolate

- **Answer (tutor only):** A, C
- **Explanation (tutor only):** Regressions and correlations describe patterns in data. Ideas about flavonoids or wealth propose mechanisms, so they are scientific models.
- **Why the wrong options are wrong (tutor only):**
  B) and D) propose processes: scientific models.
- **Hint:** Does it describe a pattern, or propose a process?

### ch13-hw-01-v2
- **Kind:** AI-written version of ch13-hw-01
- **Concepts:** Statistical vs scientific models
- **Type:** select-all
- **Question:**

Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year. Which of the following are scientific models? (Select all that apply. A scientific model need not be correct.)

- **Options:**

  A) Chocolate makes people happier, and happier scientists do more creative work
  B) A scatterplot with a best-fit line through the country-level data points
  C) Richer countries spend more on both research and luxury foods like chocolate

- **Answer (tutor only):** A, C
- **Explanation (tutor only):** A and C propose processes (happiness; wealth). A best-fit line describes a pattern, so it's a statistical model.
- **Why the wrong options are wrong (tutor only):**
  B) A fitted line describes a pattern; it says nothing about why.
- **Hint:** Which ones explain why?

### ch13-hw-02
- **Kind:** Course original
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

I ran this code and got the output below:

lm(nobel_prizes ~ 1, data = chocolate_data)

Coefficients:
(Intercept)
     11.061

nobel_prizes is the number of Nobel laureates per 10 million people. What does the (Intercept) of 11.061 represent?

- **Options:**

  A) The expected number of Nobel laureates per 10 million people in a country with no chocolate consumption
  B) The expected chocolate consumption in a country with no Nobel laureates
  C) The average chocolate consumption across countries
  D) The average number of Nobel laureates per 10 million people across countries
  E) The expected increase in Nobel laureates per 10 million people for each 1 kg/person increase in chocolate consumption

- **Answer (tutor only):** D
- **Explanation (tutor only):** A model with only an intercept (~ 1) predicts the same value for everyone: the mean of the response. So 11.061 is the mean number of laureates per 10 million people across the countries in the data.
- **Why the wrong options are wrong (tutor only):**
  A) Chocolate isn't in this model, so the intercept can't be about 'no chocolate'.
  B) and C) Chocolate consumption isn't the response.
  E) That would be a slope, and this model has none.
- **Hint:** With nothing on the right side of ~, what is the best single prediction?

### ch13-hw-02-v1
- **Kind:** AI-written version of ch13-hw-02
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year.

lm(chocolate_consumption ~ 1, data = chocolate_data)

Coefficients:
(Intercept)
      4.63

What does the (Intercept) of 4.63 represent?

- **Options:**

  A) The expected chocolate consumption in a country with no Nobel laureates
  B) The average chocolate consumption (kg/person/year) across countries
  C) The average number of Nobel laureates per 10 million people
  D) The increase in chocolate consumption per extra Nobel laureate

- **Answer (tutor only):** B
- **Explanation (tutor only):** A model with only an intercept predicts the mean of the response for everyone. Here the response is chocolate consumption.
- **Why the wrong options are wrong (tutor only):**
  A) There's no predictor here, so nothing is set to zero.
  C) Nobel prizes aren't in this model.
  D) There's no slope in an intercept-only model.
- **Hint:** What does ~ 1 predict for every country?

### ch13-hw-02-v2
- **Kind:** AI-written version of ch13-hw-02
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year. Which code produces a model whose only coefficient is the mean number of Nobel laureates per 10 million people across countries?

- **Options:**

  A) lm(nobel_prizes ~ 1, data = chocolate_data)
  B) lm(nobel_prizes ~ chocolate_consumption, data = chocolate_data)
  C) lm(chocolate_consumption ~ 1, data = chocolate_data)
  D) lm(1 ~ nobel_prizes, data = chocolate_data)

- **Answer (tutor only):** A
- **Explanation (tutor only):** ~ 1 fits an intercept only, and the intercept-only model's estimate is the mean of the response.
- **Why the wrong options are wrong (tutor only):**
  B) That also fits a slope.
  C) That gives mean chocolate consumption.
  D) The response must be on the left.
- **Hint:** Response on the left; ~ 1 means 'intercept only'.

### ch13-hw-03
- **Kind:** Course original
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

I ran this code and got the output below:

lm(nobel_prizes ~ chocolate_consumption, data = chocolate_data)

Coefficients:
          (Intercept)  chocolate_consumption
               -3.396                  2.527

nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year. According to the model, what does the (Intercept) of -3.396 represent?

- **Options:**

  A) The expected number of Nobel laureates per 10 million people in a country with no chocolate consumption
  B) The expected chocolate consumption in a country with no Nobel laureates
  C) The average number of Nobel laureates per 10 million people across countries
  D) The expected increase in Nobel laureates per 10 million people for each 1 kg/person increase in chocolate consumption
  E) The strength of the association between chocolate consumption and Nobel laureates

- **Answer (tutor only):** A
- **Explanation (tutor only):** The intercept is the prediction when every explanatory variable equals zero: a country eating 0 kg of chocolate. A negative number of laureates is impossible, a reminder that 0 kg is outside the data and the intercept is just where the line crosses x = 0.
- **Why the wrong options are wrong (tutor only):**
  B) Reverses the roles of the variables.
  C) That would be the intercept of a model with no predictors.
  D) That's the slope (2.527).
  E) Coefficients aren't measures of strength; that's what r or R² describe.
- **Hint:** What value of chocolate consumption does the intercept correspond to?

### ch13-hw-03-v1
- **Kind:** AI-written version of ch13-hw-03
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year.

lm(nobel_prizes ~ chocolate_consumption, data = chocolate_data)

          (Intercept)  chocolate_consumption
               -3.396                  2.527

Why is the intercept (-3.396) negative, even though a country can't have negative Nobel laureates?

- **Options:**

  A) It's the prediction at 0 kg of chocolate, far outside the data
  B) Countries with no chocolate truly lose Nobel laureates on average
  C) The model must have been fit to the data incorrectly
  D) Intercepts are always negative when the slope is positive

- **Answer (tutor only):** A
- **Explanation (tutor only):** The intercept is where the line crosses chocolate = 0. No country in the data eats 0 kg, so this is an extrapolation and needn't make biological sense.
- **Why the wrong options are wrong (tutor only):**
  B) Laureate counts can't be negative.
  C) The fit can be correct; it's just extrapolated.
  D) Sign of the intercept doesn't depend on the slope's sign.
- **Hint:** What value of chocolate consumption does the intercept correspond to?

### ch13-hw-03-v2
- **Kind:** AI-written version of ch13-hw-03
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year.

lm(nobel_prizes ~ chocolate_consumption, data = chocolate_data)

          (Intercept)  chocolate_consumption
               -3.396                  2.527

What does the model predict for a country with 0 kg of chocolate consumption per person per year?

- **Options:**

  A) 2.527 laureates per 10 million people
  B) -3.396 laureates per 10 million people
  C) The mean number of laureates across countries
  D) 0 laureates per 10 million people

- **Answer (tutor only):** B
- **Explanation (tutor only):** At chocolate = 0, the prediction is just the intercept: -3.396. Impossible in reality, showing the danger of predicting outside the data.
- **Why the wrong options are wrong (tutor only):**
  A) That's the slope.
  C) That's what an intercept-only model would give.
  D) The line doesn't pass through the origin.
- **Hint:** Set chocolate_consumption to 0.

### ch13-hw-04
- **Kind:** Course original
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. I ran:

lm(nobel_prizes ~ chocolate_consumption, data = chocolate_data)

          (Intercept)  chocolate_consumption
               -3.396                  2.527

nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year. According to the model, what does the chocolate_consumption coefficient of 2.527 represent?

- **Options:**

  A) The expected number of Nobel laureates per 10 million people in a country with no chocolate consumption
  B) The average chocolate consumption across countries
  C) The expected increase in Nobel laureates per 10 million people for each 1 kg/person increase in chocolate consumption
  D) The strength of the association between chocolate consumption and Nobel laureates

- **Answer (tutor only):** C
- **Explanation (tutor only):** A slope is the expected change in the response for a one-unit increase in the explanatory variable: about 2.5 more laureates per 10 million people for each extra kg of chocolate per person per year.
- **Why the wrong options are wrong (tutor only):**
  A) That's the intercept.
  B) Not something this model estimates.
  D) A slope depends on units, so it isn't a measure of strength. r or R² measure strength.
- **Hint:** What happens to the prediction if chocolate consumption goes up by 1?

### ch13-hw-04-v1
- **Kind:** AI-written version of ch13-hw-04
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year.

lm(nobel_prizes ~ chocolate_consumption, data = chocolate_data)

          (Intercept)  chocolate_consumption
               -3.396                  2.527

According to the model, how do two countries that differ by 2 kg of chocolate per person per year differ in Nobel laureates?

- **Options:**

  A) By about 2.53 laureates per 10 million people
  B) By about 5.05 laureates per 10 million people
  C) By about 1.65 laureates per 10 million people
  D) By about 6.79 laureates per 10 million people

- **Answer (tutor only):** B
- **Explanation (tutor only):** The slope is 2.527 laureates per kg, so 2 kg → 2 × 2.527 = 5.05.
- **Why the wrong options are wrong (tutor only):**
  A) That's the difference for 1 kg.
  C) That adds the intercept to the slope.
  D) That's 2 × 3.396, the intercept, not the slope.
- **Hint:** Slope × difference in x.

### ch13-hw-04-v2
- **Kind:** AI-written version of ch13-hw-04
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year.

lm(nobel_prizes ~ chocolate_consumption, data = chocolate_data)

          (Intercept)  chocolate_consumption
               -3.396                  2.527

Which statement correctly interprets the slope of 2.527?

- **Options:**

  A) Eating 1 kg more chocolate causes 2.527 more Nobel laureates per 10 million
  B) Countries eating 1 kg more chocolate have about 2.527 more laureates per 10 million
  C) 2.527 is the correlation between chocolate consumption and Nobel laureates
  D) 2.527 is the number of Nobel laureates in a country that eats no chocolate

- **Answer (tutor only):** B
- **Explanation (tutor only):** The slope describes the expected difference in the response per one-unit difference in the explanatory variable. These are observational data, so it says nothing about cause.
- **Why the wrong options are wrong (tutor only):**
  A) A regression of observational data can't show causation.
  C) A slope is not a correlation (it has units).
  D) That's the intercept.
- **Hint:** Slopes describe associations, in the units of the data.

### ch13-hw-05
- **Kind:** Course original
- **Concepts:** Coefficients & predictions; Regression from summaries
- **Type:** numeric
- **Question:**

Using lm(nobel_prizes ~ chocolate_consumption) with intercept -3.396 and slope 2.527, what is the predicted number of Nobel laureates (per 10 million people) for a country that eats 8 kg of chocolate per person per year?

- **Answer (tutor only):** 16.82
- **Explanation (tutor only):** -3.396 + 2.527 × 8 = -3.396 + 20.216 = 16.82.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: forgetting the intercept (20.22).
- **Hint:** Prediction = intercept + slope × x.

### ch13-hw-05-v1
- **Kind:** AI-written version of ch13-hw-05
- **Concepts:** Coefficients & predictions; Regression from summaries
- **Type:** numeric
- **Question:**

Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year.

lm(nobel_prizes ~ chocolate_consumption, data = chocolate_data)

          (Intercept)  chocolate_consumption
               -3.396                  2.527

What is the predicted number of Nobel laureates (per 10 million people) for a country that eats 5 kg of chocolate per person per year?

- **Answer (tutor only):** 9.24
- **Explanation (tutor only):** -3.396 + 2.527 × 5 = -3.396 + 12.635 = 9.24.
- **Hint:** Intercept + slope × 5.

### ch13-hw-05-v2
- **Kind:** AI-written version of ch13-hw-05
- **Concepts:** Coefficients & predictions; Regression from summaries
- **Type:** numeric
- **Question:**

Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year.

lm(nobel_prizes ~ chocolate_consumption, data = chocolate_data)

          (Intercept)  chocolate_consumption
               -3.396                  2.527

What is the predicted number of Nobel laureates (per 10 million people) for a country that eats 10 kg of chocolate per person per year?

- **Answer (tutor only):** 21.87
- **Explanation (tutor only):** -3.396 + 2.527 × 10 = -3.396 + 25.27 = 21.87.
- **Hint:** Intercept + slope × 10.

### ch13-hw-06
- **Kind:** Course original
- **Concepts:** Regression from summaries
- **Type:** numeric
- **Question:**

Use these summaries of the chocolate data to estimate the correlation between Nobel prizes and chocolate consumption:

var_nobel | var_chocolate | cov_chocolate_nobel
104 | 10.3 | 25.9

- **Answer (tutor only):** 0.792
- **Explanation (tutor only):** r = cov(x, y) / (sd(x) × sd(y)). The SDs are the square roots of the variances: √104 = 10.2 and √10.3 = 3.21. So r = 25.9 / (10.2 × 3.21) = 0.79.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: dividing by the variances instead of the SDs (25.9 / (104 × 10.3) = 0.024).
- **Hint:** The formula needs standard deviations, but you were given variances.

### ch13-hw-06-v1
- **Kind:** AI-written version of ch13-hw-06
- **Concepts:** Regression from summaries
- **Type:** numeric
- **Question:**

Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year. Use these summaries to find the slope of the regression of Nobel prizes (response) on chocolate consumption (explanatory):

var_nobel | var_chocolate | cov_chocolate_nobel
104 | 10.3 | 25.9

- **Answer (tutor only):** 2.51
- **Explanation (tutor only):** Slope = cov(x, y) / var(x) = 25.9 / 10.3 = 2.51 laureates per kg (close to the fitted 2.527, which used unrounded values).
- **Hint:** Divide the covariance by the variance of the explanatory variable.

### ch13-hw-06-v2
- **Kind:** AI-written version of ch13-hw-06
- **Concepts:** Regression from summaries
- **Type:** numeric
- **Question:**

For 20 lakes, the variance of water temperature is 16, the variance of algal density is 25, and their covariance is 12. What is the correlation between temperature and algal density?

- **Answer (tutor only):** 0.6
- **Explanation (tutor only):** r = cov / (sd_x × sd_y) = 12 / (√16 × √25) = 12 / (4 × 5) = 0.60.
- **Hint:** Take square roots of the variances first.

### ch13-hw-07
- **Kind:** Course original
- **Concepts:** Coefficients & predictions; Residuals & model fit
- **Type:** numeric
- **Question:**

Using lm(nobel_prizes ~ chocolate_consumption) with intercept -3.396 and slope 2.527, calculate the residual for Sweden (chocolate consumption = 6.4 kg/person/year; Nobel laureates = 31.9 per 10 million people).

- **Answer (tutor only):** 19.1
- **Explanation (tutor only):** Prediction = -3.396 + 2.527 × 6.4 = 12.78. Residual = observed - predicted = 31.9 - 12.78 = 19.1. Sweden has many more laureates than its chocolate consumption predicts.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: predicted - observed (-19.1).
- **Hint:** Find Sweden's prediction first, then subtract it from what was observed.

### ch13-hw-07-v1
- **Kind:** AI-written version of ch13-hw-07
- **Concepts:** Coefficients & predictions; Residuals & model fit
- **Type:** numeric
- **Question:**

Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year.

lm(nobel_prizes ~ chocolate_consumption, data = chocolate_data)

          (Intercept)  chocolate_consumption
               -3.396                  2.527

Calculate the residual for Switzerland (chocolate consumption = 12.0 kg/person/year; Nobel laureates = 31.5 per 10 million people).

- **Answer (tutor only):** 4.57
- **Explanation (tutor only):** Prediction = -3.396 + 2.527 × 12 = 26.93. Residual = 31.5 - 26.93 = 4.58.
- **Hint:** Residual = observed - predicted.

### ch13-hw-07-v2
- **Kind:** AI-written version of ch13-hw-07
- **Concepts:** Coefficients & predictions; Residuals & model fit
- **Type:** numeric
- **Question:**

Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year.

lm(nobel_prizes ~ chocolate_consumption, data = chocolate_data)

          (Intercept)  chocolate_consumption
               -3.396                  2.527

Calculate the residual for a country that eats 4.0 kg of chocolate per person per year and has 2.0 Nobel laureates per 10 million people.

- **Answer (tutor only):** -4.71
- **Explanation (tutor only):** Prediction = -3.396 + 2.527 × 4 = 6.71. Residual = 2.0 - 6.71 = -4.71: fewer laureates than predicted.
- **Hint:** Residual = observed - predicted.

### ch13-hw-08
- **Kind:** Course original
- **Concepts:** Residuals & model fit
- **Type:** MC
- **Question:**

Consider two models of the same response:

model_A <- lm(nobel_prizes ~ 1, data = chocolate_data)
model_B <- lm(nobel_prizes ~ chocolate_consumption, data = chocolate_data)

model_A has a residual standard deviation of 10.2, and model_B has a residual standard deviation of 1.4. Which statement must be true?

- **Options:**

  A) Observations fall closer to model A's predictions, on average
  B) Observations fall closer to model B's predictions, on average
  C) Model B is statistically significant, while model A is not
  D) None of these: the residual SD can't be compared across models of the same response

- **Answer (tutor only):** B
- **Explanation (tutor only):** The residual SD describes how far observations typically fall from the model's predictions. Smaller is closer, so model B's predictions are closer.
- **Why the wrong options are wrong (tutor only):**
  A) Backwards: a larger residual SD means points are farther from the predictions.
  C) The residual SD alone says nothing about statistical significance.
  D) Comparing residual SDs is meaningful for models of the same response (same units).
- **Hint:** What does a residual SD measure, in words?

### ch13-hw-08-v1
- **Kind:** AI-written version of ch13-hw-08
- **Concepts:** Residuals & model fit
- **Type:** MC
- **Question:**

Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year. Two models of Nobel prizes:

model_A <- lm(nobel_prizes ~ 1, data = chocolate_data)
model_B <- lm(nobel_prizes ~ chocolate_consumption, data = chocolate_data)

model_A has a residual standard deviation of 10.2 and model_B of 6.1. What does this tell us?

- **Options:**

  A) Data points fall closer, on average, to model B's predictions
  B) Data points fall closer, on average, to model A's predictions
  C) Chocolate consumption causes differences in Nobel prizes
  D) Model A is statistically significant, while model B is not

- **Answer (tutor only):** A
- **Explanation (tutor only):** Smaller residual SD = observations closer to the predictions.
- **Why the wrong options are wrong (tutor only):**
  B) Larger residual SD means farther.
  C) Fit doesn't show causation.
  D) Residual SD isn't a significance test.
- **Hint:** What does the residual SD measure?

### ch13-hw-08-v2
- **Kind:** AI-written version of ch13-hw-08
- **Concepts:** Residuals & model fit
- **Type:** MC
- **Question:**

Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year. For lm(nobel_prizes ~ chocolate_consumption), the residual standard deviation is 6.1 laureates per 10 million. What does this mean?

- **Options:**

  A) A country's laureate count is typically about 6 away from the model's prediction
  B) Each extra kg of chocolate predicts about 6.1 more laureates per 10 million
  C) The model explains about 61% of the variation in Nobel laureates
  D) The standard deviation of chocolate consumption across countries is 6.1

- **Answer (tutor only):** A
- **Explanation (tutor only):** The residual SD is roughly the typical distance between observations and the model's predictions, in units of the response.
- **Why the wrong options are wrong (tutor only):**
  B) That's a slope.
  C) That's R², not the residual SD.
  D) The residual SD is about the response, not the explanatory variable.
- **Hint:** Residuals are observed minus predicted.

### ch13-quiz-01
- **Kind:** Course original
- **Concepts:** Categorical predictors & reference levels; Coefficients & predictions
- **Type:** MC
- **Question:**

Orange juice increases tooth growth, so researchers asked whether vitamin C alone does the job: they gave hamsters vitamin C at three doses: Dose A (0.5 mg/day), Dose B (1 mg/day) or Dose C (2 mg/day), either in water (SuppVC) or as orange juice (OJ). They fit this linear model:

tooth_length = 12.45 - 3.70 × SuppVC + 9.13 × DOSE_B + 15.50 × DOSE_C

Dose was modeled as a categorical variable, not as a number (0.5, 1, 2). What does this choice mean?

- **Options:**

  A) Each dose gets its own mean, so no constant change per mg is assumed
  B) The model fits a single slope: the change in tooth length per mg
  C) It makes no difference; the predictions are identical either way
  D) Categorical predictors are required whenever there are 3+ values

- **Answer (tutor only):** A
- **Explanation (tutor only):** As a category, each dose level gets its own coefficient (compared to the reference, Dose A). The model makes no assumption about the shape of the dose-response, e.g. that going from 0.5 to 1 mg has half the effect of going from 1 to 2 mg. Treating dose as a number would fit one straight-line slope.
- **Why the wrong options are wrong (tutor only):**
  B) That's what you get when dose is a number: one slope for 'per mg'.
  C) The predictions differ unless tooth length happens to change perfectly linearly with dose.
  D) Numbers with three or more values can be modeled either way. It's a choice about what we want to assume.
- **Hint:** How many coefficients does dose get in this model? How many would it get as a number?

### ch13-quiz-01-v1
- **Kind:** AI-written version of ch13-quiz-01
- **Concepts:** Categorical predictors & reference levels; Coefficients & predictions
- **Type:** MC
- **Question:**

Orange juice increases tooth growth, so researchers asked whether vitamin C alone does the job: they gave hamsters vitamin C at Dose A (0.5 mg/day), Dose B (1 mg/day) or Dose C (2 mg/day), either in water (SuppVC) or as orange juice (OJ). The linear model is:

tooth_length = 12.45 - 3.70 × SuppVC + 9.13 × DOSE_B + 15.50 × DOSE_C

(SuppVC, DOSE_B and DOSE_C are 1 if true and 0 otherwise; orange juice and Dose A are the reference levels.)

If dose had instead been entered as a number (0.5, 1, 2), what would the model assume that the categorical version does not?

- **Options:**

  A) That tooth length changes by the same amount for every extra mg of vitamin C
  B) That orange juice and water have the same effect at every dose of vitamin C
  C) That every hamster in a dose group has exactly the same tooth length
  D) That the dose effects must be estimated separately for OJ and for water

- **Answer (tutor only):** A
- **Explanation (tutor only):** A numeric dose gets one slope: the same change in tooth length per mg everywhere. As a category, each dose gets its own mean, so the dose-response can have any shape.
- **Why the wrong options are wrong (tutor only):**
  B) Both versions are additive, so both assume the supplement effect is the same at every dose.
  C) Neither version assumes no variation within groups.
  D) Neither version has a dose × supplement interaction.
- **Hint:** What does a single slope imply about going from 0.5 to 1 mg versus 1 to 2 mg?

### ch13-quiz-01-v2
- **Kind:** AI-written version of ch13-quiz-01
- **Concepts:** Categorical predictors & reference levels; Coefficients & predictions
- **Type:** MC
- **Question:**

A plant biologist grows seedlings at three fertilizer levels (low, medium, high) and fits lm(height ~ fertilizer), with fertilizer as a categorical variable. Compared with treating fertilizer as a number (1, 2, 3), what does this choice allow?

- **Options:**

  A) Each fertilizer level gets its own mean, so height need not change by equal steps
  B) The model estimates a single slope for the change in height per fertilizer level
  C) The model no longer needs a reference level or an intercept to make predictions
  D) The predictions are guaranteed to be identical to those from the numeric version

- **Answer (tutor only):** A
- **Explanation (tutor only):** A categorical predictor gives each level its own coefficient (relative to the reference), so the model doesn't assume a straight-line, equal-step response.
- **Why the wrong options are wrong (tutor only):**
  B) That's what the numeric version does.
  C) Categorical predictors still use a reference level and intercept.
  D) Predictions match only if the true means happen to fall on a straight line.
- **Hint:** One slope, or one mean per level?

### ch13-quiz-02
- **Kind:** Course original
- **Concepts:** Categorical predictors & reference levels; Coefficients & predictions
- **Type:** numeric
- **Question:**

Orange juice increases tooth growth, so researchers asked whether vitamin C alone does the job: they gave hamsters vitamin C at Dose A (0.5 mg/day), Dose B (1 mg/day) or Dose C (2 mg/day), either in water (SuppVC) or as orange juice (OJ). The linear model is:

tooth_length = 12.45 - 3.70 × SuppVC + 9.13 × DOSE_B + 15.50 × DOSE_C

(SuppVC, DOSE_B and DOSE_C are 1 if true and 0 otherwise.)

What is the predicted mean tooth length for a hamster given Dose A of orange juice?

- **Answer (tutor only):** 12.45
- **Explanation (tutor only):** OJ and Dose A are both reference levels, so SuppVC = 0, DOSE_B = 0 and DOSE_C = 0. The prediction is just the intercept: 12.45.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: subtracting 3.70. That coefficient applies only to the vitamin C in water (SuppVC) group.
- **Hint:** Which of the indicator variables equal 1 for an OJ, Dose A hamster?

### ch13-quiz-02-v1
- **Kind:** AI-written version of ch13-quiz-02
- **Concepts:** Categorical predictors & reference levels; Coefficients & predictions
- **Type:** numeric
- **Question:**

Orange juice increases tooth growth, so researchers asked whether vitamin C alone does the job: they gave hamsters vitamin C at Dose A (0.5 mg/day), Dose B (1 mg/day) or Dose C (2 mg/day), either in water (SuppVC) or as orange juice (OJ). The linear model is:

tooth_length = 12.45 - 3.70 × SuppVC + 9.13 × DOSE_B + 15.50 × DOSE_C

(SuppVC, DOSE_B and DOSE_C are 1 if true and 0 otherwise; orange juice and Dose A are the reference levels.)

What is the predicted mean tooth length for a hamster given Dose B (1 mg/day) of orange juice?

- **Answer (tutor only):** 21.58
- **Explanation (tutor only):** OJ is the reference (SuppVC = 0) and DOSE_B = 1: 12.45 + 9.13 = 21.58.
- **Hint:** Which indicator variables equal 1 for OJ at Dose B?

### ch13-quiz-02-v2
- **Kind:** AI-written version of ch13-quiz-02
- **Concepts:** Categorical predictors & reference levels; Coefficients & predictions
- **Type:** numeric
- **Question:**

Orange juice increases tooth growth, so researchers asked whether vitamin C alone does the job: they gave hamsters vitamin C at Dose A (0.5 mg/day), Dose B (1 mg/day) or Dose C (2 mg/day), either in water (SuppVC) or as orange juice (OJ). The linear model is:

tooth_length = 12.45 - 3.70 × SuppVC + 9.13 × DOSE_B + 15.50 × DOSE_C

(SuppVC, DOSE_B and DOSE_C are 1 if true and 0 otherwise; orange juice and Dose A are the reference levels.)

What is the predicted mean tooth length for a hamster given Dose A (0.5 mg/day) of vitamin C in water (SuppVC)?

- **Answer (tutor only):** 8.75
- **Explanation (tutor only):** SuppVC = 1 and Dose A is the reference (DOSE_B = DOSE_C = 0): 12.45 - 3.70 = 8.75.
- **Hint:** Dose A is a reference level; SuppVC is not.

### ch13-quiz-03
- **Kind:** Course original
- **Concepts:** Categorical predictors & reference levels; Coefficients & predictions
- **Type:** numeric
- **Question:**

Hamster tooth growth with vitamin C in water (SuppVC) or orange juice, at three doses:

tooth_length = 12.45 - 3.70 × SuppVC + 9.13 × DOSE_B + 15.50 × DOSE_C

(SuppVC, DOSE_B and DOSE_C are 1 if true and 0 otherwise; orange juice and Dose A are the reference levels.)

What is the predicted mean tooth length for a hamster given Dose C (2 mg/day) of vitamin C in water (SuppVC)?

- **Answer (tutor only):** 24.25
- **Explanation (tutor only):** SuppVC = 1 and DOSE_C = 1 (DOSE_B = 0): 12.45 - 3.70 + 15.50 = 24.25.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: forgetting the -3.70 for SuppVC (gives 27.95), or adding the Dose B coefficient too.
- **Hint:** Start at the intercept, then add each coefficient whose indicator equals 1.

### ch13-quiz-03-v1
- **Kind:** AI-written version of ch13-quiz-03
- **Concepts:** Categorical predictors & reference levels; Coefficients & predictions
- **Type:** numeric
- **Question:**

Orange juice increases tooth growth, so researchers asked whether vitamin C alone does the job: they gave hamsters vitamin C at Dose A (0.5 mg/day), Dose B (1 mg/day) or Dose C (2 mg/day), either in water (SuppVC) or as orange juice (OJ). The linear model is:

tooth_length = 12.45 - 3.70 × SuppVC + 9.13 × DOSE_B + 15.50 × DOSE_C

(SuppVC, DOSE_B and DOSE_C are 1 if true and 0 otherwise; orange juice and Dose A are the reference levels.)

What is the predicted mean tooth length for a hamster given Dose B (1 mg/day) of vitamin C in water (SuppVC)?

- **Answer (tutor only):** 17.88
- **Explanation (tutor only):** SuppVC = 1 and DOSE_B = 1: 12.45 - 3.70 + 9.13 = 17.88.
- **Hint:** Add every coefficient whose indicator is 1.

### ch13-quiz-03-v2
- **Kind:** AI-written version of ch13-quiz-03
- **Concepts:** Categorical predictors & reference levels; Coefficients & predictions
- **Type:** numeric
- **Question:**

Orange juice increases tooth growth, so researchers asked whether vitamin C alone does the job: they gave hamsters vitamin C at Dose A (0.5 mg/day), Dose B (1 mg/day) or Dose C (2 mg/day), either in water (SuppVC) or as orange juice (OJ). The linear model is:

tooth_length = 12.45 - 3.70 × SuppVC + 9.13 × DOSE_B + 15.50 × DOSE_C

(SuppVC, DOSE_B and DOSE_C are 1 if true and 0 otherwise; orange juice and Dose A are the reference levels.)

What is the predicted mean tooth length for a hamster given Dose C (2 mg/day) of orange juice?

- **Answer (tutor only):** 27.95
- **Explanation (tutor only):** OJ is the reference (SuppVC = 0) and DOSE_C = 1: 12.45 + 15.50 = 27.95.
- **Hint:** Which indicators are 1 for OJ at Dose C?

### ch13-quiz-04
- **Kind:** Course original
- **Concepts:** Coefficients & predictions; Residuals & model fit
- **Type:** numeric
- **Question:**

Hamster tooth growth with vitamin C in water (SuppVC) or orange juice, at three doses:

tooth_length = 12.45 - 3.70 × SuppVC + 9.13 × DOSE_B + 15.50 × DOSE_C

(SuppVC, DOSE_B and DOSE_C are 1 if true and 0 otherwise; orange juice and Dose A are the reference levels.)

A hamster given Dose A (0.5 mg/day) of vitamin C in water (SuppVC) had a tooth length of 8.00. What is its residual?

- **Answer (tutor only):** -0.75
- **Explanation (tutor only):** Prediction = 12.45 - 3.70 = 8.75. Residual = observed - predicted = 8.00 - 8.75 = -0.75. The negative sign means this hamster's teeth were shorter than the model predicted.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: predicted - observed (+0.75). Residuals are observed minus predicted.
- **Hint:** First find the prediction, then subtract it from the observed value.

### ch13-quiz-04-v1
- **Kind:** AI-written version of ch13-quiz-04
- **Concepts:** Coefficients & predictions; Residuals & model fit
- **Type:** numeric
- **Question:**

Orange juice increases tooth growth, so researchers asked whether vitamin C alone does the job: they gave hamsters vitamin C at Dose A (0.5 mg/day), Dose B (1 mg/day) or Dose C (2 mg/day), either in water (SuppVC) or as orange juice (OJ). The linear model is:

tooth_length = 12.45 - 3.70 × SuppVC + 9.13 × DOSE_B + 15.50 × DOSE_C

(SuppVC, DOSE_B and DOSE_C are 1 if true and 0 otherwise; orange juice and Dose A are the reference levels.)

A hamster given Dose B (1 mg/day) of orange juice had a tooth length of 23.00. What is its residual?

- **Answer (tutor only):** 1.42
- **Explanation (tutor only):** Prediction = 12.45 + 9.13 = 21.58. Residual = observed - predicted = 23.00 - 21.58 = 1.42.
- **Hint:** Residual = observed - predicted.

### ch13-quiz-04-v2
- **Kind:** AI-written version of ch13-quiz-04
- **Concepts:** Coefficients & predictions; Residuals & model fit
- **Type:** numeric
- **Question:**

Orange juice increases tooth growth, so researchers asked whether vitamin C alone does the job: they gave hamsters vitamin C at Dose A (0.5 mg/day), Dose B (1 mg/day) or Dose C (2 mg/day), either in water (SuppVC) or as orange juice (OJ). The linear model is:

tooth_length = 12.45 - 3.70 × SuppVC + 9.13 × DOSE_B + 15.50 × DOSE_C

(SuppVC, DOSE_B and DOSE_C are 1 if true and 0 otherwise; orange juice and Dose A are the reference levels.)

A hamster given Dose C (2 mg/day) of vitamin C in water (SuppVC) had a tooth length of 22.50. What is its residual?

- **Answer (tutor only):** -1.75
- **Explanation (tutor only):** Prediction = 12.45 - 3.70 + 15.50 = 24.25. Residual = 22.50 - 24.25 = -1.75. Negative: shorter than predicted.
- **Hint:** Residual = observed - predicted.

### ch13-quiz-05
- **Kind:** Course original
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Hsieh et al. (2006) compared the year-to-year coefficient of variation (cv) in larval population size between exploited and unexploited fish species. Their model adjusted for age at maturation (age), which also seemed to influence cv. Which linear model matches this design?

- **Options:**

  A) lm(cv ~ exploited + age)
  B) lm(exploited ~ cv + age)
  C) lm(age ~ cv + exploited)
  D) lm(cv ~ exploited)

- **Answer (tutor only):** A
- **Explanation (tutor only):** The response (cv) goes on the left. The key explanatory variable (exploited or not) and the variable we adjust for (age at maturation) both go on the right.
- **Why the wrong options are wrong (tutor only):**
  B) and C) put an explanatory variable on the left as the response.
  D) leaves out age at maturation, so it doesn't adjust for it.
- **Hint:** What is the response variable? Which variables are we using to predict it?

### ch13-quiz-05-v1
- **Kind:** AI-written version of ch13-quiz-05
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Researchers ask whether fishing changes the year-to-year coefficient of variation (cv) in larval abundance. They compare exploited and unexploited species, and they want to adjust for body size at maturation (size), which also affects cv. Which model matches this design?

- **Options:**

  A) lm(cv ~ exploited + size)
  B) lm(size ~ cv + exploited)
  C) lm(exploited ~ cv + size)
  D) lm(cv ~ size)

- **Answer (tutor only):** A
- **Explanation (tutor only):** cv is the response, so it goes on the left. Exploitation status (the question of interest) and size (the variable we adjust for) both go on the right.
- **Why the wrong options are wrong (tutor only):**
  B) and C) put the wrong variable as the response.
  D) leaves out exploitation, the variable we care about.
- **Hint:** Which variable is being explained?

### ch13-quiz-05-v2
- **Kind:** AI-written version of ch13-quiz-05
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

A study asks whether exploited fish species have more variable larval populations (cv) than unexploited ones, after adjusting for age at maturation (age). A student fits lm(cv ~ exploited). What is wrong with this model for the study's question?

- **Options:**

  A) It leaves out age, so it does not adjust for age at maturation
  B) It puts cv as the response when exploited should be the response
  C) It should include age instead of exploited as the only predictor
  D) Nothing; the adjustment happens automatically in lm()

- **Answer (tutor only):** A
- **Explanation (tutor only):** To adjust for age at maturation, age must be in the model: lm(cv ~ exploited + age).
- **Why the wrong options are wrong (tutor only):**
  B) cv is the response in this design.
  C) Dropping exploited removes the variable of interest.
  D) lm() only adjusts for variables you include.
- **Hint:** Which variable from the design is missing?

### ch13-quiz-06
- **Kind:** Course original
- **Concepts:** Residuals & model fit
- **Type:** matching
- **Question:**

To ask whether fishing makes fish populations more variable, a model compared the year-to-year coefficient of variation (cv) in larval abundance of exploited and unexploited fish species, adjusting for age at maturation: lm(cv ~ exploited + age). The model gives three summaries of its residuals. Match each to how it is calculated:

1. Residual sum of squares = 2.45
2. Mean square residual = 0.098
3. Residual standard deviation = 0.313

- **Options:**

  A) Square root of the mean square residual
  B) Sum of the squared residuals
  C) Residual sum of squares divided by its degrees of freedom

- **Answer (tutor only):** 1-B, 2-C, 3-A
- **Explanation (tutor only):** Square each residual and add them up to get the residual sum of squares (2.45). Divide by the residual degrees of freedom to get the mean square, an estimate of the residual variance (0.098). Its square root (0.313) is the residual standard deviation: roughly how far a typical point falls from its prediction, in the units of cv.
- **Why the wrong options are wrong (tutor only):**
  Common mix-up: the mean square and the standard deviation. The mean square is a variance (squared units); the SD is its square root.
- **Hint:** Which of these three is in the same units as the response?

### ch13-quiz-06-v1
- **Kind:** AI-written version of ch13-quiz-06
- **Concepts:** Residuals & model fit
- **Type:** matching
- **Question:**

To ask whether fishing makes fish populations more variable, a model compared the year-to-year coefficient of variation (cv) in larval abundance of exploited and unexploited fish species, adjusting for age at maturation: lm(cv ~ exploited + age). Fill in the blanks:

1. The ____ is found by squaring each residual and adding them up.
2. Dividing that by the residual degrees of freedom gives the ____.
3. Taking the square root of that gives the ____.

- **Options:**

  A) residual standard deviation
  B) residual sum of squares
  C) mean square residual

- **Answer (tutor only):** 1-B, 2-C, 3-A
- **Explanation (tutor only):** Sum of squares → divide by df → mean square (the residual variance) → square root → residual standard deviation.
- **Why the wrong options are wrong (tutor only):**
  Follow the order: square and sum, then average, then take the root.
- **Hint:** Which one is in the original units of cv?

### ch13-quiz-06-v2
- **Kind:** AI-written version of ch13-quiz-06
- **Concepts:** Residuals & model fit
- **Type:** matching
- **Question:**

To ask whether fishing makes fish populations more variable, a model compared the year-to-year coefficient of variation (cv) in larval abundance of exploited and unexploited fish species, adjusting for age at maturation: lm(cv ~ exploited + age). The model's residual sum of squares is 2.45, with 25 degrees of freedom. Match each value to what it is:

1. 2.45
2. 0.098
3. 0.313

- **Options:**

  A) The residual standard deviation (√0.098)
  B) The residual sum of squares
  C) The mean square residual (2.45 / 25)

- **Answer (tutor only):** 1-B, 2-C, 3-A
- **Explanation (tutor only):** 2.45 is the sum of squared residuals; 2.45 / 25 = 0.098 is the mean square; √0.098 = 0.313 is the residual SD.
- **Why the wrong options are wrong (tutor only):**
  Each value is calculated from the one before it.
- **Hint:** Start from the sum of squares.

### ch13-quiz-07
- **Kind:** Course original
- **Concepts:** Residuals & model fit
- **Type:** numeric
- **Question:**

To ask whether fishing makes fish populations more variable, a model compared the year-to-year coefficient of variation (cv) in larval abundance of exploited and unexploited fish species, adjusting for age at maturation: lm(cv ~ exploited + age). The model has a residual sum of squares of 2.45 and a mean square residual of 0.098. How many residual degrees of freedom does the model have?

- **Answer (tutor only):** 25
- **Explanation (tutor only):** Mean square = sum of squares / df, so df = 2.45 / 0.098 = 25.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: multiplying instead of dividing (2.45 × 0.098 = 0.24).
- **Hint:** How do you get from a sum of squares to a mean square?

### ch13-quiz-07-v1
- **Kind:** AI-written version of ch13-quiz-07
- **Concepts:** Residuals & model fit
- **Type:** numeric
- **Question:**

To ask whether fishing makes fish populations more variable, a model compared the year-to-year coefficient of variation (cv) in larval abundance of exploited and unexploited fish species, adjusting for age at maturation: lm(cv ~ exploited + age). The model has a residual sum of squares of 2.45 and 25 residual degrees of freedom. What is the mean square residual?

- **Answer (tutor only):** 0.098
- **Explanation (tutor only):** Mean square = sum of squares / df = 2.45 / 25 = 0.098.
- **Hint:** Divide the sum of squares by its degrees of freedom.

### ch13-quiz-07-v2
- **Kind:** AI-written version of ch13-quiz-07
- **Concepts:** Residuals & model fit
- **Type:** numeric
- **Question:**

To ask whether fishing makes fish populations more variable, a model compared the year-to-year coefficient of variation (cv) in larval abundance of exploited and unexploited fish species, adjusting for age at maturation: lm(cv ~ exploited + age). The model has a mean square residual of 0.098 with 25 residual degrees of freedom. What is the residual sum of squares?

- **Answer (tutor only):** 2.45
- **Explanation (tutor only):** Sum of squares = mean square × df = 0.098 × 25 = 2.45.
- **Hint:** Mean square = SS / df, so SS = mean square × df.

### ch13-quiz-08
- **Kind:** Course original
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch13-quiz-fish.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch13-quiz-fish.png)
- **Question:**

The plot shows the coefficient of variation (cv) in larval abundance for exploited and unexploited fish species, against age at maturation. The model is lm(cv ~ exploited + age), where exploited is "yes" or "no" ("no" is the reference level).

Which set of estimates best matches the plot?

- **Options:**

  A) (Intercept) = 1.25, exploitedyes = 0.45, age = -0.04
  B) (Intercept) = 1.25, exploitedyes = -0.45, age = -0.04
  C) (Intercept) = 0.98, exploitedyes = 0.53, age = 0
  D) (Intercept) = 1.50, exploitedyes = 0.45, age = 0.04

- **Answer (tutor only):** A
- **Explanation (tutor only):** Exploited species (orange) sit higher than unexploited species of the same age, so exploitedyes is positive. Within each group, cv tends to fall with age at maturation, so the age slope is negative. The intercept is the predicted cv of an unexploited species at age 0: extend the blue cloud back to age 0, about 1.25.
- **Why the wrong options are wrong (tutor only):**
  B) Gets the direction of the exploited effect backwards.
  C) An age slope of 0 ignores the downward trend; these numbers are close to the simple group means.
  D) A positive age slope doesn't match the downward trend.
- **Hint:** Check the signs first: are exploited species higher or lower? Does cv go up or down with age?

### ch13-quiz-08-v1
- **Kind:** AI-written version of ch13-quiz-08
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch13-quiz-fish.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch13-quiz-fish.png)
- **Question:**

The plot shows the coefficient of variation (cv) in larval abundance for exploited and unexploited fish species, against age at maturation. The model is lm(cv ~ exploited + age), where exploited is "yes" or "no" ("no" is the reference level). What sign should the exploitedyes and age coefficients have?

- **Options:**

  A) exploitedyes positive; age negative
  B) exploitedyes negative; age negative
  C) exploitedyes positive; age positive
  D) exploitedyes negative; age positive

- **Answer (tutor only):** A
- **Explanation (tutor only):** At any given age, exploited species sit higher (positive exploitedyes). Within each group cv falls as age at maturation increases (negative age slope).
- **Why the wrong options are wrong (tutor only):**
  Compare the groups at the same age, then look at the trend within a group.
- **Hint:** Which group is higher? Which way does each cloud slope?

### ch13-quiz-08-v2
- **Kind:** AI-written version of ch13-quiz-08
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch13-quiz-fish.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch13-quiz-fish.png)
- **Question:**

The plot shows the coefficient of variation (cv) in larval abundance for exploited and unexploited fish species, against age at maturation, with lines from lm(cv ~ exploited + age). What feature of the model makes the two lines parallel?

- **Options:**

  A) The model is additive: one age slope is shared by both groups
  B) The exploited coefficient is positive, so the lines never cross
  C) Age at maturation was measured the same way in both groups
  D) The residual standard deviation is the same for both groups

- **Answer (tutor only):** A
- **Explanation (tutor only):** With no interaction, both groups share one age slope; exploited only shifts the line up or down.
- **Why the wrong options are wrong (tutor only):**
  B) A positive shift alone doesn't make lines parallel; a shared slope does.
  C) Measurement method doesn't determine the slope.
  D) Equal residual spread doesn't make lines parallel.
- **Hint:** How many age slopes does lm(cv ~ exploited + age) estimate?

### ch13-quiz-09
- **Kind:** Course original
- **Concepts:** Coefficients & predictions
- **Type:** numeric
- **Question:**

To ask whether fishing makes fish populations more variable, a model compared the year-to-year coefficient of variation (cv) in larval abundance of exploited and unexploited fish species, adjusting for age at maturation: lm(cv ~ exploited + age). The fitted model is (exploitedyes = 1 for exploited species, 0 otherwise):

cv = 1.25 + 0.45 × exploitedyes - 0.04 × age

What is the predicted cv for an exploited species that matures at 5 years?

- **Answer (tutor only):** 1.5
- **Explanation (tutor only):** 1.25 + 0.45 × 1 - 0.04 × 5 = 1.25 + 0.45 - 0.20 = 1.50.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: leaving out the exploited coefficient (1.05), or adding the age term instead of subtracting it (1.90).
- **Hint:** exploitedyes = 1 for an exploited species.

### ch13-quiz-09-v1
- **Kind:** AI-written version of ch13-quiz-09
- **Concepts:** Coefficients & predictions
- **Type:** numeric
- **Question:**

To ask whether fishing makes fish populations more variable, a model compared the year-to-year coefficient of variation (cv) in larval abundance of exploited and unexploited fish species, adjusting for age at maturation: lm(cv ~ exploited + age). The fitted model is (exploitedyes = 1 for exploited species, 0 otherwise):

cv = 1.25 + 0.45 × exploitedyes - 0.04 × age

What is the predicted cv for an unexploited species that matures at 5 years?

- **Answer (tutor only):** 1.05
- **Explanation (tutor only):** 1.25 + 0.45 × 0 - 0.04 × 5 = 1.25 - 0.20 = 1.05.
- **Hint:** exploitedyes = 0 for unexploited species.

### ch13-quiz-09-v2
- **Kind:** AI-written version of ch13-quiz-09
- **Concepts:** Coefficients & predictions
- **Type:** numeric
- **Question:**

To ask whether fishing makes fish populations more variable, a model compared the year-to-year coefficient of variation (cv) in larval abundance of exploited and unexploited fish species, adjusting for age at maturation: lm(cv ~ exploited + age). The fitted model is (exploitedyes = 1 for exploited species, 0 otherwise):

cv = 1.25 + 0.45 × exploitedyes - 0.04 × age

What is the predicted cv for an exploited species that matures at 10 years?

- **Answer (tutor only):** 1.3
- **Explanation (tutor only):** 1.25 + 0.45 - 0.04 × 10 = 1.70 - 0.40 = 1.30.
- **Hint:** Plug in exploitedyes = 1 and age = 10.

## Chapter 14: Normal distribution

### ch14-book-01
- **Kind:** Course original
- **Concepts:** The normal & Z
- **Type:** numeric
- **Question:**

Birth weight is a key predictor of infant health. The weights of singleton babies born in the U.S. are roughly normal, with a mean of 3.339 kg and an SD of 0.573 kg. Roughly how many standard deviations from the mean is a 5 kg baby?

- **Answer (tutor only):** 2.9
- **Explanation (tutor only):** Z = (5 - 3.339) / 0.573 = 1.661 / 0.573 = 2.9.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: forgetting to subtract the mean (5 / 0.573 = 8.7).
- **Hint:** Z = (value - mean) / SD.

### ch14-book-01-v1
- **Kind:** AI-written version of ch14-book-01
- **Concepts:** The normal & Z
- **Type:** numeric
- **Question:**

Birth weight is a key predictor of infant health. Birth weight of U.S. singleton babies is roughly normal, with mean 3.339 kg and SD 0.573 kg. Roughly how many standard deviations from the mean is a 2 kg baby?

- **Answer (tutor only):** -2.3
- **Explanation (tutor only):** Z = (2 - 3.339) / 0.573 = -1.339 / 0.573 = -2.3.
- **Hint:** (Y - μ) / σ.

### ch14-book-01-v2
- **Kind:** AI-written version of ch14-book-01
- **Concepts:** The normal & Z
- **Type:** numeric
- **Question:**

Birth weight is a key predictor of infant health. Birth weight of U.S. singleton babies is roughly normal, with mean 3.339 kg and SD 0.573 kg. What birth weight (in kg) is two standard deviations above the mean?

- **Answer (tutor only):** 4.48
- **Explanation (tutor only):** 3.339 + 2 × 0.573 = 4.485 kg.
- **Hint:** μ + 2σ.

### ch14-book-02
- **Kind:** Course original
- **Concepts:** Density & R's _norm functions
- **Type:** TF
- **Question:**

Birth weight of U.S. singleton babies is normal with mean 3.339 kg and SD 0.573 kg. In R:

dnorm(5, mean = 3.339, sd = 0.573)
[1] 0.0104

TRUE or FALSE: 1.04% of babies weigh exactly 5 kg at birth.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** dnorm() gives a density (the height of the curve), not a probability. For a continuous variable the probability of any exact value is zero; probabilities are areas over a range.
- **Why the wrong options are wrong (tutor only):**
  TRUE: confuses density with probability.
- **Hint:** Which _norm function gives probabilities?

### ch14-book-02-v1
- **Kind:** AI-written version of ch14-book-02
- **Concepts:** Density & R's _norm functions
- **Type:** TF
- **Question:**

Birth weight is a key predictor of infant health. Birth weight of U.S. singleton babies is roughly normal, with mean 3.339 kg and SD 0.573 kg. In R:

dnorm(3.339, mean = 3.339, sd = 0.573)
[1] 0.696

TRUE or FALSE: 69.6% of babies weigh exactly 3.339 kg.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** dnorm() is the height of the curve, not a probability. The probability of any exact weight is zero.
- **Why the wrong options are wrong (tutor only):**
  TRUE: densities aren't probabilities.
- **Hint:** Height or area?

### ch14-book-02-v2
- **Kind:** AI-written version of ch14-book-02
- **Concepts:** Density & R's _norm functions
- **Type:** TF
- **Question:**

Birth weight is a key predictor of infant health. Birth weight of U.S. singleton babies is roughly normal, with mean 3.339 kg and SD 0.573 kg. TRUE or FALSE: pnorm(3, mean = 3.339, sd = 0.573) gives the probability that a baby weighs less than 3 kg.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** A
- **Explanation (tutor only):** pnorm() returns the area to the left of a value: the probability of a smaller value (here 0.277).
- **Why the wrong options are wrong (tutor only):**
  FALSE: pnorm() is exactly the area below.
- **Hint:** What does pnorm() return?

### ch14-book-03
- **Kind:** Course original
- **Concepts:** The normal & Z; Density & R's _norm functions
- **Type:** MC
- **Question:**

Birth weight of U.S. singleton babies is normal with mean 3.339 kg and SD 0.573 kg. Which R code gives the probability that a baby weighs more than 5 kg?

- **Options:**

  A) dnorm(5, mean = 3.339, sd = 0.573)
  B) pnorm(5, mean = 3.339, sd = 0.573)
  C) pnorm(5, mean = 3.339, sd = 0.573, lower.tail = FALSE)
  D) qnorm(5, mean = 3.339, sd = 0.573, lower.tail = FALSE)

- **Answer (tutor only):** C
- **Explanation (tutor only):** pnorm() gives the area below a value; lower.tail = FALSE gives the area above it. (The answer is 0.0019: about 2 in 1,000 babies.)
- **Why the wrong options are wrong (tutor only):**
  A) dnorm() gives a density, not a probability.
  B) This gives the probability of weighing less than 5 kg.
  D) qnorm() expects a probability, not a weight.
- **Hint:** You want an area, and the upper tail.

### ch14-book-03-v1
- **Kind:** AI-written version of ch14-book-03
- **Concepts:** The normal & Z; Density & R's _norm functions
- **Type:** MC
- **Question:**

Birth weight is a key predictor of infant health. Birth weight of U.S. singleton babies is roughly normal, with mean 3.339 kg and SD 0.573 kg. Which R code gives the probability that a baby weighs less than 2.5 kg?

- **Options:**

  A) dnorm(2.5, mean = 3.339, sd = 0.573)
  B) pnorm(2.5, mean = 3.339, sd = 0.573)
  C) pnorm(2.5, mean = 3.339, sd = 0.573, lower.tail = FALSE)
  D) qnorm(2.5, mean = 3.339, sd = 0.573)

- **Answer (tutor only):** B
- **Explanation (tutor only):** pnorm() gives the area below 2.5 (about 0.07).
- **Why the wrong options are wrong (tutor only):**
  A) dnorm() gives a height.
  C) That's the area above 2.5.
  D) qnorm() takes a probability.
- **Hint:** Area below a value.

### ch14-book-03-v2
- **Kind:** AI-written version of ch14-book-03
- **Concepts:** The normal & Z; Density & R's _norm functions
- **Type:** MC
- **Question:**

Birth weight is a key predictor of infant health. Birth weight of U.S. singleton babies is roughly normal, with mean 3.339 kg and SD 0.573 kg. Which R code gives the birth weight that only 1% of babies exceed?

- **Options:**

  A) qnorm(0.99, mean = 3.339, sd = 0.573)
  B) pnorm(0.99, mean = 3.339, sd = 0.573)
  C) dnorm(0.99, mean = 3.339, sd = 0.573)
  D) qnorm(0.01, mean = 3.339, sd = 0.573)

- **Answer (tutor only):** A
- **Explanation (tutor only):** 99% of babies fall below the 0.99 quantile, so only 1% exceed it (about 4.67 kg).
- **Why the wrong options are wrong (tutor only):**
  B) and C) take a weight, not a probability.
  D) That's the weight 1% fall BELOW.
- **Hint:** Which quantile has 1% above it?

### ch14-book-04
- **Kind:** Course original
- **Concepts:** The normal & Z
- **Type:** MC
- **Question:**

Birth weight of U.S. singleton babies is normal with mean 3.339 kg and SD 0.573 kg. In R:

pnorm(3, mean = 3.339, sd = 0.573)
[1] 0.277
pnorm(4, mean = 3.339, sd = 0.573)
[1] 0.876

What percentage of babies weigh between 3 and 4 kg?

- **Options:**

  A) 40%
  B) 50%
  C) 60%
  D) 70%

- **Answer (tutor only):** C
- **Explanation (tutor only):** 0.876 - 0.277 = 0.599, about 60%.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: using just one of the two numbers, or adding them.
- **Hint:** Area below 4 minus area below 3.

### ch14-book-04-v1
- **Kind:** AI-written version of ch14-book-04
- **Concepts:** The normal & Z
- **Type:** MC
- **Question:**

Birth weight is a key predictor of infant health. Birth weight of U.S. singleton babies is roughly normal, with mean 3.339 kg and SD 0.573 kg. In R:

pnorm(2.5, mean = 3.339, sd = 0.573)
[1] 0.072
pnorm(4.5, mean = 3.339, sd = 0.573)
[1] 0.979

What percentage of babies weigh between 2.5 and 4.5 kg?

- **Options:**

  A) About 7%
  B) About 21%
  C) About 91%
  D) About 98%

- **Answer (tutor only):** C
- **Explanation (tutor only):** 0.979 - 0.072 = 0.907, about 91%.
- **Why the wrong options are wrong (tutor only):**
  A) That's the share below 2.5 kg.
  B) That's not an area from this output.
  D) That's the share below 4.5 kg.
- **Hint:** Subtract the two areas.

### ch14-book-04-v2
- **Kind:** AI-written version of ch14-book-04
- **Concepts:** The normal & Z
- **Type:** MC
- **Question:**

Birth weight is a key predictor of infant health. Birth weight of U.S. singleton babies is roughly normal, with mean 3.339 kg and SD 0.573 kg. In R:

pnorm(4, mean = 3.339, sd = 0.573)
[1] 0.876

What percentage of babies weigh more than 4 kg?

- **Options:**

  A) About 12%
  B) About 24%
  C) About 50%
  D) About 88%

- **Answer (tutor only):** A
- **Explanation (tutor only):** 1 - 0.876 = 0.124, about 12%.
- **Why the wrong options are wrong (tutor only):**
  B) Doubles the tail.
  C) 4 kg is above the mean, so fewer than half are heavier.
  D) That's the share below 4 kg.
- **Hint:** Area above = 1 - area below.

### ch14-book-05
- **Kind:** Course original
- **Concepts:** Sampling distribution & CLT
- **Type:** MC
- **Question:**

Birth weight of U.S. singleton babies is normal with SD 0.573 kg. Imagine we took five babies born in a hospital and calculated their mean weight, and repeated this many times. The standard deviation of this sampling distribution would be about:

- **Options:**

  A) 0.11
  B) 0.15
  C) 0.25

- **Answer (tutor only):** C
- **Explanation (tutor only):** SE = 0.573 / √5 = 0.573 / 2.24 = 0.256.
- **Why the wrong options are wrong (tutor only):**
  A) 0.573 / 5: divides by n instead of √n.
  B) Not a standard calculation here.
- **Hint:** SE = σ / √n.

### ch14-book-05-v1
- **Kind:** AI-written version of ch14-book-05
- **Concepts:** Sampling distribution & CLT
- **Type:** MC
- **Question:**

Birth weight of U.S. singleton babies has SD 0.573 kg. Imagine we took 25 babies, calculated their mean weight, and repeated this many times. The standard deviation of this sampling distribution would be about:

- **Options:**

  A) 0.023
  B) 0.115
  C) 0.573

- **Answer (tutor only):** B
- **Explanation (tutor only):** SE = 0.573 / √25 = 0.573 / 5 = 0.115.
- **Why the wrong options are wrong (tutor only):**
  A) Divides by 25 instead of √25.
  C) That's the SD of individuals.
- **Hint:** σ / √n.

### ch14-book-05-v2
- **Kind:** AI-written version of ch14-book-05
- **Concepts:** Sampling distribution & CLT
- **Type:** MC
- **Question:**

Birth weight of U.S. singleton babies has SD 0.573 kg. If we increase the number of babies in each sample from 5 to 20, what happens to the standard error of the mean?

- **Options:**

  A) It is cut in half
  B) It is cut to a quarter
  C) It stays the same

- **Answer (tutor only):** A
- **Explanation (tutor only):** SE = σ / √n. Quadrupling n doubles √n, so the SE halves (0.256 → 0.128).
- **Why the wrong options are wrong (tutor only):**
  B) The SE scales with √n, not n.
  C) The SE shrinks as n grows.
- **Hint:** How does √n change when n is multiplied by 4?

### ch14-chimein-01
- **Kind:** Course original
- **Concepts:** Sampling distribution & CLT
- **Type:** matching
- **Question:**

Match each statement with its name:

1. An estimate approaches its true parameter value as sample size gets large
2. The sampling distribution of a mean becomes approximately normal as sample size gets large

- **Options:**

  A) The law of large numbers
  B) The central limit theorem

- **Answer (tutor only):** 1-A, 2-B
- **Explanation (tutor only):** The law of large numbers is about where an estimate ends up (close to the truth). The central limit theorem is about the shape of the sampling distribution (normal).
- **Why the wrong options are wrong (tutor only):**
  These two are easy to mix up. 'Large numbers' gets you close to the truth; 'central limit' gives you a normal shape.
- **Hint:** Which statement is about shape?

### ch14-chimein-01-v1
- **Kind:** AI-written version of ch14-chimein-01
- **Concepts:** Sampling distribution & CLT
- **Type:** matching
- **Question:**

Match each example to the idea it illustrates:

1. As a field crew measures more and more trees, their mean height gets closer to the forest's true mean
2. Means of many samples of 50 skewed seed masses form a bell-shaped histogram

- **Options:**

  A) The law of large numbers
  B) The central limit theorem

- **Answer (tutor only):** 1-A, 2-B
- **Explanation (tutor only):** Approaching the truth is the law of large numbers; the bell shape of the sampling distribution is the central limit theorem.
- **Why the wrong options are wrong (tutor only):**
  One is about where the estimate ends up; the other is about the shape.
- **Hint:** Accuracy vs shape.

### ch14-chimein-01-v2
- **Kind:** AI-written version of ch14-chimein-01
- **Concepts:** Sampling distribution & CLT
- **Type:** matching
- **Question:**

Match each statement with its name:

1. Describes the shape of the sampling distribution of a mean in large samples
2. Describes how close a large sample's estimate gets to the true parameter

- **Options:**

  A) The law of large numbers
  B) The central limit theorem

- **Answer (tutor only):** 1-B, 2-A
- **Explanation (tutor only):** The CLT is about shape (normal); the law of large numbers is about estimates approaching the truth.
- **Why the wrong options are wrong (tutor only):**
  Shape → CLT; closeness to truth → law of large numbers.
- **Hint:** Which one is about shape?

### ch14-chimein-02
- **Kind:** Course original
- **Concepts:** The normal & Z
- **Type:** numeric
- **Question:**

What is the probability that a value drawn from a normal distribution with μ = 8 and σ = 4 is greater than 10? In R:

pnorm(10, mean = 8, sd = 4)
[1] 0.691

- **Answer (tutor only):** 0.309
- **Explanation (tutor only):** 10 is half an SD above the mean. pnorm() gives the area below 10 (0.691), so the area above is 1 - 0.691 = 0.309.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: answering 0.691 (the area below 10).
- **Hint:** Which tail does pnorm() give by default?

### ch14-chimein-02-v1
- **Kind:** AI-written version of ch14-chimein-02
- **Concepts:** The normal & Z
- **Type:** numeric
- **Question:**

What is the probability that a value drawn from a normal distribution with μ = 8 and σ = 4 is less than 6? In R:

pnorm(6, mean = 8, sd = 4)
[1] 0.309

- **Answer (tutor only):** 0.309
- **Explanation (tutor only):** pnorm() gives the area below 6 directly: 0.309.
- **Hint:** pnorm() gives the area below the value.

### ch14-chimein-02-v2
- **Kind:** AI-written version of ch14-chimein-02
- **Concepts:** The normal & Z
- **Type:** numeric
- **Question:**

What is the probability that a value drawn from a normal distribution with μ = 8 and σ = 4 is greater than 14? In R:

pnorm(14, mean = 8, sd = 4)
[1] 0.933

- **Answer (tutor only):** 0.067
- **Explanation (tutor only):** pnorm() gives the area below 14 (0.933), so the area above is 1 - 0.933 = 0.067.
- **Hint:** Area above = 1 - area below.

### ch14-chimein-03
- **Kind:** Course original
- **Concepts:** Density & R's _norm functions
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch14-chimein-norm-functions.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch14-chimein-norm-functions.png)
- **Question:**

The figure shows a normal distribution, a value x, the height of the curve at x, and the area to the right of x. Match each R function to what it does:

1. dnorm()
2. pnorm(lower.tail = FALSE)
3. qnorm()
4. rnorm()

- **Options:**

  A) Returns the probability density: the height of the curve (y) at x
  B) Returns the probability of a value greater than x: the shaded area from x to infinity
  C) Returns the value of x for which the area to its left equals a given probability (e.g. the 0.025 quantile)
  D) Draws random values from the distribution

- **Answer (tutor only):** 1-A, 2-B, 3-C, 4-D
- **Explanation (tutor only):** d = density (height), p = probability (area), q = quantile (the x value for a given area), r = random draws.
- **Why the wrong options are wrong (tutor only):**
  Common mix-up: pnorm() and qnorm() are inverses. pnorm() goes from x to an area; qnorm() goes from an area to x.
- **Hint:** d, p, q, r: density, probability, quantile, random.

### ch14-chimein-03-v1
- **Kind:** AI-written version of ch14-chimein-03
- **Concepts:** Density & R's _norm functions
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch14-chimein-norm-functions.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch14-chimein-norm-functions.png)
- **Question:**

The figure shows a normal distribution, a value x, the height of the curve at x, and the area to the right of x. Match each task to the R function you'd use:

1. Simulate 100 values from the distribution
2. Find the height of the curve at x
3. Find the value of x with 2.5% of the area to its left
4. Find the area to the right of x

- **Options:**

  A) dnorm()
  B) pnorm(lower.tail = FALSE)
  C) qnorm()
  D) rnorm()

- **Answer (tutor only):** 1-D, 2-A, 3-C, 4-B
- **Explanation (tutor only):** r = random draws; d = density (height); q = quantile; p = probability (area).
- **Why the wrong options are wrong (tutor only):**
  Match the first letter: d, p, q, r.
- **Hint:** d = density, p = probability, q = quantile, r = random.

### ch14-chimein-03-v2
- **Kind:** AI-written version of ch14-chimein-03
- **Concepts:** Density & R's _norm functions
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch14-chimein-norm-functions.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch14-chimein-norm-functions.png)
- **Question:**

The figure shows a normal distribution, a value x, the height of the curve at x, and the area to the right of x. Match each R function to what it takes as its main input:

1. pnorm()
2. qnorm()
3. rnorm()

- **Options:**

  A) A value of x
  B) A probability (an area)
  C) The number of random values to draw

- **Answer (tutor only):** 1-A, 2-B, 3-C
- **Explanation (tutor only):** pnorm(x) returns an area; qnorm(p) returns a value; rnorm(n) returns n random draws.
- **Why the wrong options are wrong (tutor only):**
  pnorm and qnorm are inverses.
- **Hint:** pnorm and qnorm undo each other.

### ch14-hw-01
- **Kind:** Course original
- **Concepts:** The normal & Z
- **Type:** numeric
- **Question:**

Wing length helps determine flight performance in birds. Wing length of adult house sparrows is normally distributed with a mean of 76 mm and an SD of 2 mm. How many standard deviations from the mean is a sparrow with a wing length of 79.5 mm?

- **Answer (tutor only):** 1.75
- **Explanation (tutor only):** Z = (79.5 - 76) / 2 = 1.75.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: forgetting to divide by the SD (3.5).
- **Hint:** Z = (value - mean) / SD.

### ch14-hw-01-v1
- **Kind:** AI-written version of ch14-hw-01
- **Concepts:** The normal & Z
- **Type:** numeric
- **Question:**

Wing length helps determine flight performance in birds. Wing length of adult house sparrows is normally distributed with a mean of 76 mm and an SD of 2 mm. How many standard deviations from the mean is a sparrow with a wing length of 73 mm?

- **Answer (tutor only):** -1.5
- **Explanation (tutor only):** Z = (73 - 76) / 2 = -1.5.
- **Hint:** (Y - μ) / σ.

### ch14-hw-01-v2
- **Kind:** AI-written version of ch14-hw-01
- **Concepts:** The normal & Z
- **Type:** numeric
- **Question:**

Wing length helps determine flight performance in birds. Wing length of adult house sparrows is normally distributed with a mean of 76 mm and an SD of 2 mm. What wing length is 2.5 standard deviations above the mean?

- **Answer (tutor only):** 81
- **Explanation (tutor only):** Y = μ + Z × σ = 76 + 2.5 × 2 = 81 mm.
- **Hint:** Y = μ + Z × σ.

### ch14-hw-02
- **Kind:** Course original
- **Concepts:** The normal & Z
- **Type:** MC
- **Question:**

Converting a value into the number of standard deviations it is from the mean, as (Y - μ) / σ, is called:

- **Options:**

  A) The central limit theorem
  B) The q-transform
  C) The log-transform
  D) The Z-transform

- **Answer (tutor only):** D
- **Explanation (tutor only):** The Z-transform rescales a value into standard deviations from the mean, putting it on the standard normal scale.
- **Why the wrong options are wrong (tutor only):**
  A) The CLT is about the shape of sampling distributions.
  B) Not a real transform; qnorm() finds quantiles.
  C) A log transform changes the shape of data; it doesn't standardize.
- **Hint:** The result is called a Z score.

### ch14-hw-02-v1
- **Kind:** AI-written version of ch14-hw-02
- **Concepts:** The normal & Z
- **Type:** MC
- **Question:**

A biologist rescales tail lengths by subtracting the population mean and dividing by the population SD. What is this called, and what is the mean of the rescaled values?

- **Options:**

  A) The Z-transform; mean 0
  B) The Z-transform; mean 1
  C) The log-transform; mean 0
  D) The central limit theorem; mean 1

- **Answer (tutor only):** A
- **Explanation (tutor only):** (Y - μ) / σ is the Z-transform. The rescaled values have mean 0 and SD 1.
- **Why the wrong options are wrong (tutor only):**
  B) The SD is 1; the mean is 0.
  C) No logs are taken.
  D) The CLT is about sampling distributions.
- **Hint:** What happens to the mean after subtracting it?

### ch14-hw-02-v2
- **Kind:** AI-written version of ch14-hw-02
- **Concepts:** The normal & Z
- **Type:** MC
- **Question:**

After a Z-transform, (Y - μ) / σ, a value of Z = -1 means the original value was:

- **Options:**

  A) One standard deviation below the mean
  B) One unit below the mean, in the original units
  C) One standard error below the mean
  D) Smaller than every other value in the data

- **Answer (tutor only):** A
- **Explanation (tutor only):** Z counts standard deviations from the mean; negative means below.
- **Why the wrong options are wrong (tutor only):**
  B) Z is in SD units, not original units.
  C) Z uses σ, not the SE.
  D) It's one SD below the mean, not the minimum.
- **Hint:** What units is Z in?

### ch14-hw-03
- **Kind:** Course original
- **Concepts:** Density & R's _norm functions
- **Type:** MC
- **Question:**

Wing length of adult house sparrows is normal with mean 76 mm and SD 2 mm. Which R code gives the probability density at a wing length of 79.5 mm?

- **Options:**

  A) dnorm(79.5, mean = 76, sd = 2)
  B) pnorm(79.5, mean = 76, sd = 2)
  C) qnorm(79.5, mean = 76, sd = 2)
  D) rnorm(79.5, mean = 76, sd = 2)

- **Answer (tutor only):** A
- **Explanation (tutor only):** dnorm() returns the density: the height of the normal curve at a value. (Here it equals 0.043.)
- **Why the wrong options are wrong (tutor only):**
  B) pnorm() returns a probability: the area below the value.
  C) qnorm() takes a probability and returns a value (a quantile).
  D) rnorm() draws random numbers.
- **Hint:** d is for density.

### ch14-hw-03-v1
- **Kind:** AI-written version of ch14-hw-03
- **Concepts:** Density & R's _norm functions
- **Type:** MC
- **Question:**

Wing length helps determine flight performance in birds. Wing length of adult house sparrows is normally distributed with a mean of 76 mm and an SD of 2 mm. Which R code gives the proportion of sparrows with wings shorter than 74 mm?

- **Options:**

  A) dnorm(74, mean = 76, sd = 2)
  B) pnorm(74, mean = 76, sd = 2)
  C) qnorm(74, mean = 76, sd = 2)
  D) rnorm(74, mean = 76, sd = 2)

- **Answer (tutor only):** B
- **Explanation (tutor only):** pnorm() gives the area below a value (here 0.159).
- **Why the wrong options are wrong (tutor only):**
  A) dnorm() gives the curve's height.
  C) qnorm() takes a probability and returns a value.
  D) rnorm() draws random values.
- **Hint:** p for probability (area).

### ch14-hw-03-v2
- **Kind:** AI-written version of ch14-hw-03
- **Concepts:** Density & R's _norm functions
- **Type:** MC
- **Question:**

Wing length helps determine flight performance in birds. Wing length of adult house sparrows is normally distributed with a mean of 76 mm and an SD of 2 mm. Which R code gives the wing length below which 2.5% of sparrows fall?

- **Options:**

  A) dnorm(0.025, mean = 76, sd = 2)
  B) pnorm(0.025, mean = 76, sd = 2)
  C) qnorm(0.025, mean = 76, sd = 2)
  D) rnorm(0.025, mean = 76, sd = 2)

- **Answer (tutor only):** C
- **Explanation (tutor only):** qnorm() takes a probability and returns the value (quantile) with that area to its left: about 72.1 mm.
- **Why the wrong options are wrong (tutor only):**
  A) dnorm() gives a height.
  B) pnorm() takes a value and returns an area.
  D) rnorm() draws random values.
- **Hint:** q for quantile.

### ch14-hw-04
- **Kind:** Course original
- **Concepts:** Density & R's _norm functions
- **Type:** TF
- **Question:**

Wing length of adult house sparrows is normal with mean 76 mm and SD 2 mm, and dnorm(79.5, mean = 76, sd = 2) = 0.043. TRUE or FALSE: the probability that a sparrow's wing is exactly 79.5 mm long is 0.043.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** For a continuous variable, a density is the height of the curve, not a probability. The probability of any exact value is zero; probabilities come from areas under the curve over a range (e.g. between 79.4 and 79.6 mm).
- **Why the wrong options are wrong (tutor only):**
  TRUE: densities can even be bigger than 1, so they can't be probabilities.
- **Hint:** Is the probability of an exact value a height or an area?

### ch14-hw-04-v1
- **Kind:** AI-written version of ch14-hw-04
- **Concepts:** Density & R's _norm functions
- **Type:** TF
- **Question:**

Wing length helps determine flight performance in birds. Wing length of adult house sparrows is normally distributed with a mean of 76 mm and an SD of 2 mm. TRUE or FALSE: dnorm(76, mean = 76, sd = 2) = 0.199 means that 19.9% of sparrows have wings exactly 76 mm long.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** dnorm() gives the height of the curve (a density). For a continuous variable, the probability of any exact value is zero; probabilities are areas.
- **Why the wrong options are wrong (tutor only):**
  TRUE: a density is not a probability.
- **Hint:** Height or area?

### ch14-hw-04-v2
- **Kind:** AI-written version of ch14-hw-04
- **Concepts:** Density & R's _norm functions
- **Type:** TF
- **Question:**

Wing length helps determine flight performance in birds. Wing length of adult house sparrows is normally distributed with a mean of 76 mm and an SD of 2 mm. TRUE or FALSE: To find the probability a sparrow's wing is between 75 and 77 mm, we calculate pnorm(77, 76, 2) - pnorm(75, 76, 2).

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** A
- **Explanation (tutor only):** Probabilities are areas. The area below 77 minus the area below 75 is the area between them (0.383).
- **Why the wrong options are wrong (tutor only):**
  FALSE: subtracting the two pnorm() areas gives exactly the area between.
- **Hint:** Area below 77 minus area below 75.

### ch14-hw-05
- **Kind:** Course original
- **Concepts:** The normal & Z; Density & R's _norm functions
- **Type:** numeric
- **Question:**

Wing length of adult house sparrows is normal with mean 76 mm and SD 2 mm. In R:

pnorm(77, mean = 76, sd = 2)
[1] 0.691

What proportion of sparrows have wings longer than 77 mm?

- **Answer (tutor only):** 0.309
- **Explanation (tutor only):** pnorm() gives the area below 77 (0.691). The area above is 1 - 0.691 = 0.309.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: answering 0.691, the proportion shorter than 77 mm.
- **Hint:** pnorm() gives the lower tail by default.

### ch14-hw-05-v1
- **Kind:** AI-written version of ch14-hw-05
- **Concepts:** The normal & Z; Density & R's _norm functions
- **Type:** numeric
- **Question:**

Wing length helps determine flight performance in birds. Wing length of adult house sparrows is normally distributed with a mean of 76 mm and an SD of 2 mm. In R:

pnorm(73, mean = 76, sd = 2)
[1] 0.0668

What proportion of sparrows have wings longer than 73 mm?

- **Answer (tutor only):** 0.9332
- **Explanation (tutor only):** 1 - 0.0668 = 0.9332.
- **Hint:** pnorm() gives the area below.

### ch14-hw-05-v2
- **Kind:** AI-written version of ch14-hw-05
- **Concepts:** The normal & Z; Density & R's _norm functions
- **Type:** numeric
- **Question:**

Wing length helps determine flight performance in birds. Wing length of adult house sparrows is normally distributed with a mean of 76 mm and an SD of 2 mm. In R:

pnorm(78, mean = 76, sd = 2, lower.tail = FALSE)
[1] 0.159

What proportion of sparrows have wings shorter than 78 mm?

- **Answer (tutor only):** 0.841
- **Explanation (tutor only):** lower.tail = FALSE gives the area above 78 (0.159), so the area below is 1 - 0.159 = 0.841.
- **Hint:** The two areas add to 1.

### ch14-hw-06
- **Kind:** Course original
- **Concepts:** The normal & Z; Density & R's _norm functions
- **Type:** numeric
- **Question:**

Wing length of adult house sparrows is normal with mean 76 mm and SD 2 mm. In R:

pnorm(77, mean = 76, sd = 2)
[1] 0.691
pnorm(79, mean = 76, sd = 2)
[1] 0.933

What proportion of sparrows have wings between 77 and 79 mm long?

- **Answer (tutor only):** 0.242
- **Explanation (tutor only):** Area below 79 minus area below 77: 0.933 - 0.691 = 0.242.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: adding the two numbers, or using 1 minus one of them.
- **Hint:** Shade the region between 77 and 79. Which two areas can you subtract?

### ch14-hw-06-v1
- **Kind:** AI-written version of ch14-hw-06
- **Concepts:** The normal & Z; Density & R's _norm functions
- **Type:** numeric
- **Question:**

Wing length helps determine flight performance in birds. Wing length of adult house sparrows is normally distributed with a mean of 76 mm and an SD of 2 mm. In R:

pnorm(74, mean = 76, sd = 2)
[1] 0.159
pnorm(78, mean = 76, sd = 2)
[1] 0.841

What proportion of sparrows have wings between 74 and 78 mm long?

- **Answer (tutor only):** 0.682
- **Explanation (tutor only):** 0.841 - 0.159 = 0.682 (within one SD of the mean, as expected).
- **Hint:** Area below 78 minus area below 74.

### ch14-hw-06-v2
- **Kind:** AI-written version of ch14-hw-06
- **Concepts:** The normal & Z; Density & R's _norm functions
- **Type:** numeric
- **Question:**

Wing length helps determine flight performance in birds. Wing length of adult house sparrows is normally distributed with a mean of 76 mm and an SD of 2 mm. In R:

pnorm(72, mean = 76, sd = 2)
[1] 0.0228
pnorm(75, mean = 76, sd = 2)
[1] 0.309

What proportion of sparrows have wings between 72 and 75 mm long?

- **Answer (tutor only):** 0.286
- **Explanation (tutor only):** 0.309 - 0.0228 = 0.286.
- **Hint:** Area below 75 minus area below 72.

### ch14-hw-07
- **Kind:** Course original
- **Concepts:** Sampling distribution & CLT
- **Type:** numeric
- **Question:**

Wing length of adult house sparrows is normal with mean 76 mm and SD 2 mm. Imagine we caught nine sparrows, calculated their mean wing length, and repeated this many times. What would the standard deviation of this sampling distribution be?

- **Answer (tutor only):** 0.667
- **Explanation (tutor only):** SE = σ / √n = 2 / √9 = 2 / 3 = 0.667 mm.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: dividing by n (2 / 9 = 0.22) instead of √n.
- **Hint:** SE = σ / √n.

### ch14-hw-07-v1
- **Kind:** AI-written version of ch14-hw-07
- **Concepts:** Sampling distribution & CLT
- **Type:** numeric
- **Question:**

Wing length helps determine flight performance in birds. Wing length of adult house sparrows is normally distributed with a mean of 76 mm and an SD of 2 mm. Imagine we caught 16 sparrows, calculated their mean wing length, and repeated this many times. What would the standard deviation of this sampling distribution be?

- **Answer (tutor only):** 0.5
- **Explanation (tutor only):** SE = σ / √n = 2 / √16 = 0.5 mm.
- **Hint:** σ / √n.

### ch14-hw-07-v2
- **Kind:** AI-written version of ch14-hw-07
- **Concepts:** Sampling distribution & CLT
- **Type:** numeric
- **Question:**

Wing length helps determine flight performance in birds. Wing length of adult house sparrows is normally distributed with a mean of 76 mm and an SD of 2 mm. Imagine we caught four sparrows, calculated their mean wing length, and repeated this many times. What would the standard deviation of this sampling distribution be?

- **Answer (tutor only):** 1
- **Explanation (tutor only):** SE = σ / √n = 2 / √4 = 1 mm.
- **Hint:** σ / √n.

### ch14-hw-08
- **Kind:** Course original
- **Concepts:** Normality & transformations
- **Type:** TF
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch14-hw-bluetit.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch14-hw-bluetit.png)
- **Question:**

Chick mass shortly before fledging predicts survival in birds. TRUE or FALSE: The mass of these 3,720 blue tit chicks 14 days after hatching is roughly normally distributed.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** The histogram is clearly left-skewed: a long tail of small (probably undernourished) chicks stretches to the left of the main peak.
- **Why the wrong options are wrong (tutor only):**
  TRUE: the main peak looks bell-shaped, but the long left tail is far too big for a normal distribution.
- **Hint:** Is the histogram symmetric?

### ch14-hw-08-v1
- **Kind:** AI-written version of ch14-hw-08
- **Concepts:** Normality & transformations
- **Type:** TF
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch14-hw-bluetit.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch14-hw-bluetit.png)
- **Question:**

Chick mass shortly before fledging predicts survival in birds. The histogram shows the mass of 3,720 blue tit chicks 14 days after hatching. TRUE or FALSE: The distribution of chick mass is left-skewed (a long tail toward small values).

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** A
- **Explanation (tutor only):** Most chicks cluster near the peak, with a long tail of lighter chicks stretching to the left.
- **Why the wrong options are wrong (tutor only):**
  FALSE: look at which side has the long tail.
- **Hint:** Which side has the long tail?

### ch14-hw-08-v2
- **Kind:** AI-written version of ch14-hw-08
- **Concepts:** Normality & transformations
- **Type:** TF
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch14-hw-bluetit.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch14-hw-bluetit.png)
- **Question:**

Chick mass shortly before fledging predicts survival in birds. The histogram shows the mass of 3,720 blue tit chicks 14 days after hatching. TRUE or FALSE: Because there are 3,720 chicks, the central limit theorem makes these individual masses normally distributed.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** The CLT is about sample means, not individual values. The masses themselves stay left-skewed however many chicks we measure.
- **Why the wrong options are wrong (tutor only):**
  TRUE: the CLT applies to the sampling distribution of the mean, not to the data.
- **Hint:** Does the CLT describe data or means?

### ch14-hw-09
- **Kind:** Course original
- **Concepts:** Sampling distribution & CLT
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch14-hw-bluetit.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch14-hw-bluetit.png)
- **Question:**

The histogram shows the mass of 3,720 blue tit chicks 14 days after hatching. Imagine we repeatedly sample chicks and calculate the mean mass of each sample. Of the options below, what is the smallest sample size for which the sampling distribution of the mean would be roughly normal?

- **Options:**

  A) A sample of size 1: it's already normal
  B) Three
  C) Fifty
  D) Never: the data are simply not normal

- **Answer (tutor only):** C
- **Explanation (tutor only):** By the central limit theorem, means of large enough samples are roughly normal even when the data aren't. With a skew this strong, samples of 3 aren't enough; 50 is.
- **Why the wrong options are wrong (tutor only):**
  A) A sample of size 1 has the same skewed shape as the population.
  B) Three values averaged still inherit much of the skew.
  D) The CLT works even when the data aren't normal.
- **Hint:** What does the central limit theorem say happens as sample size grows?

### ch14-hw-09-v1
- **Kind:** AI-written version of ch14-hw-09
- **Concepts:** Sampling distribution & CLT
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch14-hw-bluetit.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch14-hw-bluetit.png)
- **Question:**

The histogram shows the mass of 3,720 blue tit chicks 14 days after hatching. We repeatedly sample chicks and calculate each sample's mean mass. How does the sampling distribution of the mean change as sample size grows from 2 to 100?

- **Options:**

  A) It becomes more normal and narrower
  B) It becomes more skewed and wider
  C) It becomes more normal, but no narrower
  D) It stays the shape of the data

- **Answer (tutor only):** A
- **Explanation (tutor only):** By the CLT, the sampling distribution becomes more normal, and its spread (the SE) shrinks with √n.
- **Why the wrong options are wrong (tutor only):**
  B) Larger samples make it less skewed and narrower.
  C) The SE shrinks as n grows.
  D) Means of large samples become normal.
- **Hint:** Think about both the CLT and σ / √n.

### ch14-hw-09-v2
- **Kind:** AI-written version of ch14-hw-09
- **Concepts:** Sampling distribution & CLT
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch14-hw-bluetit.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch14-hw-bluetit.png)
- **Question:**

The histogram shows the mass of 3,720 blue tit chicks 14 days after hatching. Imagine taking many samples of size 2 and calculating each sample's mean mass. What shape would the sampling distribution most likely have?

- **Options:**

  A) Somewhat left-skewed, like the data
  B) Perfectly normal, by the CLT
  C) Right-skewed, the opposite of the data
  D) Uniform, with all means equally likely

- **Answer (tutor only):** A
- **Explanation (tutor only):** With n = 2, means still carry much of the data's skew. The CLT only kicks in with larger samples.
- **Why the wrong options are wrong (tutor only):**
  B) The CLT needs large samples, especially for skewed data.
  C) Averaging doesn't flip the skew.
  D) There's no reason for a uniform shape.
- **Hint:** Is n = 2 large?

### ch14-quiz-01
- **Kind:** Course original
- **Concepts:** Sampling distribution & CLT
- **Type:** MC
- **Question:**

If you sample from a distribution that is not normal, the sampling distribution of the mean becomes approximately normal when samples are large. What is this rule called?

- **Options:**

  A) The law of large numbers
  B) Bayes' theorem
  C) The normal rule
  D) The central limit theorem

- **Answer (tutor only):** D
- **Explanation (tutor only):** The central limit theorem says the sampling distribution of a mean (or sum) becomes approximately normal as sample size grows, whatever the shape of the original distribution.
- **Why the wrong options are wrong (tutor only):**
  A) The law of large numbers says an estimate gets closer to the true value as n grows. It says nothing about the shape of the sampling distribution.
  B) Bayes' theorem is about updating probabilities with new information.
  C) Not a real rule.
- **Hint:** Which rule is about the shape of a sampling distribution?

### ch14-quiz-01-v1
- **Kind:** AI-written version of ch14-quiz-01
- **Concepts:** Sampling distribution & CLT
- **Type:** MC
- **Question:**

Seed mass in a wildflower is strongly right-skewed. A botanist repeatedly takes samples of 100 seeds and calculates each sample's mean mass. Why is the distribution of these means roughly normal?

- **Options:**

  A) The central limit theorem
  B) The law of large numbers
  C) Bayes' theorem
  D) The seeds themselves are normally distributed

- **Answer (tutor only):** A
- **Explanation (tutor only):** The central limit theorem says means of large samples are approximately normal, whatever the shape of the data.
- **Why the wrong options are wrong (tutor only):**
  B) The law of large numbers says the estimate approaches the truth, not that it becomes normal.
  C) Bayes' theorem is about conditional probability.
  D) The seed masses are skewed.
- **Hint:** Which rule is about the shape of the sampling distribution?

### ch14-quiz-01-v2
- **Kind:** AI-written version of ch14-quiz-01
- **Concepts:** Sampling distribution & CLT
- **Type:** MC
- **Question:**

Which statement describes the central limit theorem?

- **Options:**

  A) Sample means become approximately normal as sample size gets large
  B) Sample estimates get closer to the true value as sample size gets large
  C) Every biological variable is normal if we measure enough individuals
  D) The data in a large sample always become approximately normal

- **Answer (tutor only):** A
- **Explanation (tutor only):** The CLT is about the sampling distribution of means (or sums): it becomes approximately normal with large samples, even when the data aren't.
- **Why the wrong options are wrong (tutor only):**
  B) That's the law of large numbers.
  C) and D) The data keep their own shape; only the sampling distribution of the mean becomes normal.
- **Hint:** Is it about the data or about the means?

### ch14-quiz-02
- **Kind:** Course original
- **Concepts:** The normal & Z
- **Type:** matching
- **Question:**

A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4).

Any normal value can be converted to the standard normal (mean 0, SD 1) with Z = (Y - μ) / σ. Match each value of Y to its Z score:

1. Y = 0
2. Y = 4
3. Y = 12
4. Y = 20

- **Options:**

  A) Z = -2
  B) Z = -1
  C) Z = 1
  D) Z = 3

- **Answer (tutor only):** 1-A, 2-B, 3-C, 4-D
- **Explanation (tutor only):** Subtract the mean (8) and divide by the SD (4): (0 - 8)/4 = -2, (4 - 8)/4 = -1, (12 - 8)/4 = 1, (20 - 8)/4 = 3.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: dividing by the variance (16) instead of the SD (4).
- **Hint:** The formula needs σ, but you were given σ². What is σ?

### ch14-quiz-02-v1
- **Kind:** AI-written version of ch14-quiz-02
- **Concepts:** The normal & Z
- **Type:** matching
- **Question:**

A population is normally distributed with mean μ = 50 and variance σ² = 100 (so σ = 10).

Any normal value can be converted to the standard normal (mean 0, SD 1) with Z = (Y - μ) / σ. Match each value of Y to its Z score:

1. Y = 30
2. Y = 45
3. Y = 60
4. Y = 75

- **Options:**

  A) Z = -2
  B) Z = -0.5
  C) Z = 1
  D) Z = 2.5

- **Answer (tutor only):** 1-A, 2-B, 3-C, 4-D
- **Explanation (tutor only):** (30 - 50)/10 = -2; (45 - 50)/10 = -0.5; (60 - 50)/10 = 1; (75 - 50)/10 = 2.5.
- **Why the wrong options are wrong (tutor only):**
  Subtract the mean, then divide by the SD.
- **Hint:** Z = (Y - 50) / 10.

### ch14-quiz-02-v2
- **Kind:** AI-written version of ch14-quiz-02
- **Concepts:** The normal & Z
- **Type:** matching
- **Question:**

A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4).

Any normal value can be converted to the standard normal (mean 0, SD 1) with Z = (Y - μ) / σ. Match each Z score to its value of Y:

1. Z = -1.5
2. Z = 0
3. Z = 0.5
4. Z = 2

- **Options:**

  A) Y = 2
  B) Y = 8
  C) Y = 10
  D) Y = 16

- **Answer (tutor only):** 1-A, 2-B, 3-C, 4-D
- **Explanation (tutor only):** Y = μ + Z × σ: 8 - 1.5 × 4 = 2; 8 + 0 = 8; 8 + 0.5 × 4 = 10; 8 + 2 × 4 = 16.
- **Why the wrong options are wrong (tutor only):**
  Work backwards: Y = 8 + 4Z.
- **Hint:** Y = μ + Z × σ.

### ch14-quiz-03
- **Kind:** Course original
- **Concepts:** The normal & Z
- **Type:** numeric
- **Question:**

A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4).

What is the probability that a random draw from this population is less than 8?

- **Answer (tutor only):** 0.5
- **Explanation (tutor only):** 8 is the mean, and a normal distribution is symmetric around its mean, so half of all values fall below it.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: thinking the probability of being below the mean depends on the SD. It's always 0.5 for a normal.
- **Hint:** Where is 8 relative to the mean?

### ch14-quiz-03-v1
- **Kind:** AI-written version of ch14-quiz-03
- **Concepts:** The normal & Z
- **Type:** numeric
- **Question:**

A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4).

What is the probability that a random draw from this population is greater than 8?

- **Answer (tutor only):** 0.5
- **Explanation (tutor only):** 8 is the mean, and the normal is symmetric around its mean, so half the values are above it.
- **Hint:** Where is 8 relative to the center?

### ch14-quiz-03-v2
- **Kind:** AI-written version of ch14-quiz-03
- **Concepts:** The normal & Z
- **Type:** numeric
- **Question:**

A population is normally distributed with mean μ = 50 and variance σ² = 100 (so σ = 10).

What is the probability that a random draw from this population is less than 50?

- **Answer (tutor only):** 0.5
- **Explanation (tutor only):** 50 is the mean of a symmetric distribution, so half of all values fall below it.
- **Hint:** Where is 50 relative to the center?

### ch14-quiz-04
- **Kind:** Course original
- **Concepts:** The normal & Z
- **Type:** numeric
- **Question:**

A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4).

Roughly what is the probability that a random draw is more than 12 or less than 4?

- **Answer (tutor only):** 0.32
- **Explanation (tutor only):** 4 and 12 are one SD below and above the mean. About 68% of a normal falls within one SD of the mean, so about 32% falls outside (exactly 0.317).
- **Why the wrong options are wrong (tutor only):**
  Common mistake: answering 0.68, which is the probability of falling between 4 and 12.
- **Hint:** How many SDs from the mean are 4 and 12? What fraction of a normal lies within that range?

### ch14-quiz-04-v1
- **Kind:** AI-written version of ch14-quiz-04
- **Concepts:** The normal & Z
- **Type:** numeric
- **Question:**

A population is normally distributed with mean μ = 50 and variance σ² = 100 (so σ = 10).

Roughly what is the probability that a random draw is more than 60 or less than 40?

- **Answer (tutor only):** 0.32
- **Explanation (tutor only):** 40 and 60 are one SD from the mean. About 68% falls within one SD, so about 32% falls outside (exactly 0.317).
- **Hint:** How many SDs from the mean are 40 and 60?

### ch14-quiz-04-v2
- **Kind:** AI-written version of ch14-quiz-04
- **Concepts:** The normal & Z
- **Type:** numeric
- **Question:**

A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4).

Roughly what is the probability that a random draw is between 4 and 12?

- **Answer (tutor only):** 0.68
- **Explanation (tutor only):** 4 and 12 are one SD below and above the mean, and about 68% of a normal falls within one SD (exactly 0.683).
- **Hint:** How many SDs from the mean are 4 and 12?

### ch14-quiz-05
- **Kind:** Course original
- **Concepts:** The normal & Z
- **Type:** numeric
- **Question:**

A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4).

Roughly what is the probability that a random draw is more than 16 or less than 0?

- **Answer (tutor only):** 0.05
- **Explanation (tutor only):** 0 and 16 are two SDs from the mean. About 95% of a normal falls within two SDs, so about 5% falls outside (exactly 0.0455).
- **Why the wrong options are wrong (tutor only):**
  Common mistake: answering 0.025, which counts only one tail.
- **Hint:** How many SDs away are 0 and 16? Count both tails.

### ch14-quiz-05-v1
- **Kind:** AI-written version of ch14-quiz-05
- **Concepts:** The normal & Z
- **Type:** numeric
- **Question:**

A population is normally distributed with mean μ = 50 and variance σ² = 100 (so σ = 10).

Roughly what is the probability that a random draw is more than 70 or less than 30?

- **Answer (tutor only):** 0.05
- **Explanation (tutor only):** 30 and 70 are two SDs from the mean; about 95% falls within two SDs, so about 5% is outside (exactly 0.0455).
- **Hint:** How many SDs from the mean?

### ch14-quiz-05-v2
- **Kind:** AI-written version of ch14-quiz-05
- **Concepts:** The normal & Z
- **Type:** numeric
- **Question:**

A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4).

Roughly what is the probability that a random draw is between 0 and 16?

- **Answer (tutor only):** 0.95
- **Explanation (tutor only):** 0 and 16 are two SDs from the mean; about 95% of a normal falls within two SDs (exactly 0.954).
- **Hint:** How many SDs from the mean are 0 and 16?

### ch14-quiz-06
- **Kind:** Course original
- **Concepts:** Sampling distribution & CLT
- **Type:** MC
- **Question:**

A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4).

Imagine you take many samples of size four from this population and record the mean of each sample. What is the distribution of these means called?

- **Options:**

  A) The population distribution
  B) The sampling distribution (of the mean)
  C) The null distribution
  D) The standard normal distribution

- **Answer (tutor only):** B
- **Explanation (tutor only):** The distribution of an estimate (here, the mean) across many samples is the sampling distribution.
- **Why the wrong options are wrong (tutor only):**
  A) The population distribution describes individual values, not sample means.
  C) A null distribution is a sampling distribution under the null hypothesis, used for testing.
  D) The standard normal has mean 0 and SD 1; these means are centered on 8.
- **Hint:** These are means of samples, not individual values.

### ch14-quiz-06-v1
- **Kind:** AI-written version of ch14-quiz-06
- **Concepts:** Sampling distribution & CLT
- **Type:** MC
- **Question:**

A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4).

You take many samples of size 10 from this population and record the mean of each. The standard deviation of these means is called the standard error. What is the distribution of the means itself called?

- **Options:**

  A) The sampling distribution of the mean
  B) The population distribution
  C) The standard normal distribution
  D) The null distribution

- **Answer (tutor only):** A
- **Explanation (tutor only):** The distribution of an estimate across repeated samples is its sampling distribution.
- **Why the wrong options are wrong (tutor only):**
  B) That's the distribution of individual values.
  C) That's the normal with mean 0 and SD 1.
  D) A null distribution is a sampling distribution assuming the null is true.
- **Hint:** Distribution of estimates from many samples.

### ch14-quiz-06-v2
- **Kind:** AI-written version of ch14-quiz-06
- **Concepts:** Sampling distribution & CLT
- **Type:** MC
- **Question:**

A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4).

Which of these describes the distribution of individual values in the population, rather than the distribution of sample means?

- **Options:**

  A) The population distribution: mean 8 and SD 4
  B) The sampling distribution: mean 8 and SD 4 / √n
  C) The null distribution: mean 0 and SD 1
  D) The standard normal: mean 8 and SD 1

- **Answer (tutor only):** A
- **Explanation (tutor only):** Individual values follow the population distribution (SD = σ = 4). Sample means follow the sampling distribution, whose SD (the SE) is σ / √n.
- **Why the wrong options are wrong (tutor only):**
  B) That's for sample means.
  C) and D) These aren't this population's distribution of individuals.
- **Hint:** Individuals vs means.

### ch14-quiz-07
- **Kind:** Course original
- **Concepts:** Sampling distribution & CLT
- **Type:** numeric
- **Question:**

A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4).

You take many samples of size four and record each sample's mean. What is the standard deviation of this distribution of sample means (its standard error)?

- **Answer (tutor only):** 2
- **Explanation (tutor only):** SE = σ / √n = 4 / √4 = 4 / 2 = 2.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: using the variance (16 / 2 = 8), or dividing by n instead of √n (4 / 4 = 1).
- **Hint:** SE = σ / √n.

### ch14-quiz-07-v1
- **Kind:** AI-written version of ch14-quiz-07
- **Concepts:** Sampling distribution & CLT
- **Type:** numeric
- **Question:**

A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4).

You take many samples of size 16 and record each sample's mean. What is the standard error of the mean?

- **Answer (tutor only):** 1
- **Explanation (tutor only):** SE = σ / √n = 4 / √16 = 4 / 4 = 1.
- **Hint:** σ / √n.

### ch14-quiz-07-v2
- **Kind:** AI-written version of ch14-quiz-07
- **Concepts:** Sampling distribution & CLT
- **Type:** numeric
- **Question:**

A population is normally distributed with mean μ = 50 and variance σ² = 100 (so σ = 10).

You take many samples of size 25 and record each sample's mean. What is the standard error of the mean?

- **Answer (tutor only):** 2
- **Explanation (tutor only):** SE = σ / √n = 10 / √25 = 10 / 5 = 2.
- **Hint:** σ / √n.

### ch14-quiz-08
- **Kind:** Course original
- **Concepts:** Sampling distribution & CLT
- **Type:** MC
- **Question:**

The standard deviation of the sampling distribution of the mean has a special name. What is it?

- **Options:**

  A) The residual standard deviation
  B) The standard error
  C) The variance
  D) The Z score

- **Answer (tutor only):** B
- **Explanation (tutor only):** The standard error is the standard deviation of a sampling distribution. It describes how much an estimate varies from sample to sample.
- **Why the wrong options are wrong (tutor only):**
  A) The residual SD describes how far individual points fall from a model's predictions.
  C) The variance is the square of an SD.
  D) A Z score is a single value's distance from the mean in SD units.
- **Hint:** It describes the uncertainty in an estimate.

### ch14-quiz-08-v1
- **Kind:** AI-written version of ch14-quiz-08
- **Concepts:** Sampling distribution & CLT
- **Type:** MC
- **Question:**

A researcher repeatedly samples 20 mice, calculates the mean body mass of each sample, and finds the standard deviation of those means. What is this quantity called?

- **Options:**

  A) The standard error of the mean
  B) The residual standard deviation
  C) The population variance
  D) The Z score

- **Answer (tutor only):** A
- **Explanation (tutor only):** The SD of a sampling distribution is the standard error.
- **Why the wrong options are wrong (tutor only):**
  B) That's about residuals from a model.
  C) That's the spread of individuals, squared.
  D) A Z score is a single standardized value.
- **Hint:** SD of the sampling distribution.

### ch14-quiz-08-v2
- **Kind:** AI-written version of ch14-quiz-08
- **Concepts:** Sampling distribution & CLT
- **Type:** MC
- **Question:**

What does the standard error of a mean describe?

- **Options:**

  A) How much the sample mean varies from sample to sample
  B) How much individual values vary around the mean
  C) The probability that the null hypothesis is true
  D) How far the sample is from a normal distribution

- **Answer (tutor only):** A
- **Explanation (tutor only):** The standard error is the SD of the sampling distribution: how much estimates vary among samples.
- **Why the wrong options are wrong (tutor only):**
  B) That's the standard deviation.
  C) Neither SE nor p-values give that.
  D) That's about the shape, not the SE.
- **Hint:** Variation among estimates, not individuals.

### ch14-quiz-09
- **Kind:** Course original
- **Concepts:** Z tests & p-values
- **Type:** numeric
- **Question:**

A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4).

You take one sample of size four and estimate a mean of 4. Testing the null hypothesis that μ = 8, roughly what is the two-tailed p-value?

- **Answer (tutor only):** 0.05
- **Explanation (tutor only):** The standard error is 4 / √4 = 2, so the sample mean is (4 - 8) / 2 = -2 standard errors from the null value. The probability of being at least 2 SEs away (in either direction) is about 0.05 (exactly 0.0455).
- **Why the wrong options are wrong (tutor only):**
  Common mistake: using σ (4) instead of the SE (2). That puts the mean only 1 SD away and gives p ≈ 0.32.
- **Hint:** How many standard errors (not SDs) is 4 from 8?

### ch14-quiz-09-v1
- **Kind:** AI-written version of ch14-quiz-09
- **Concepts:** Z tests & p-values
- **Type:** numeric
- **Question:**

A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4).

You take one sample of size 16 and estimate a mean of 10. Testing the null hypothesis that μ = 8, roughly what is the two-tailed p-value?

- **Answer (tutor only):** 0.05
- **Explanation (tutor only):** SE = 4 / √16 = 1, so the mean is (10 - 8) / 1 = 2 SEs from the null value. About 5% of a normal is at least 2 SDs away (exactly 0.0455).
- **Hint:** First find the SE, then the Z.

### ch14-quiz-09-v2
- **Kind:** AI-written version of ch14-quiz-09
- **Concepts:** Z tests & p-values
- **Type:** numeric
- **Question:**

A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4).

You take one sample of size four and estimate a mean of 10. Testing the null hypothesis that μ = 8, roughly what is the two-tailed p-value?

- **Answer (tutor only):** 0.32
- **Explanation (tutor only):** SE = 4 / √4 = 2, so the mean is (10 - 8) / 2 = 1 SE from the null value. About 32% of a normal is at least 1 SD away (exactly 0.317).
- **Hint:** First find the SE, then the Z.

### ch14-quiz-10
- **Kind:** Course original
- **Concepts:** Z tests & p-values
- **Type:** MC
- **Question:**

A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4).

You take one sample of size four and estimate a mean of 4. The two-tailed p-value for the null hypothesis that μ = 8 is 0.046. Using α = 0.05, what do we do, and what do we know about whether the null is true?

- **Options:**

  A) Reject the null; the null is false
  B) Reject the null; we don't know whether the null is true or false
  C) Fail to reject the null; the null is true
  D) Fail to reject the null; we don't know whether the null is true or false

- **Answer (tutor only):** B
- **Explanation (tutor only):** 0.046 < 0.05, so we reject the null. But a p-value never proves the null false (or true): either the null is false, or it's true and we got an unusual sample (a type I error).
- **Why the wrong options are wrong (tutor only):**
  A) Rejecting the null isn't proof it's false.
  C) and D) 0.046 is less than 0.05, so we reject.
- **Hint:** Compare p to α first. Then ask: can a single p-value tell us the truth for certain?

### ch14-quiz-10-v1
- **Kind:** AI-written version of ch14-quiz-10
- **Concepts:** Z tests & p-values
- **Type:** MC
- **Question:**

A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4).

You take one sample of size four and estimate a mean of 10. The two-tailed p-value for the null hypothesis that μ = 8 is 0.32. Using α = 0.05, what do we do, and what do we know about whether the null is true?

- **Options:**

  A) Reject the null; the null is false
  B) Reject the null; we don't know whether the null is true
  C) Fail to reject the null; the null is true
  D) Fail to reject the null; we don't know whether the null is true

- **Answer (tutor only):** D
- **Explanation (tutor only):** 0.32 > 0.05, so we fail to reject. But failing to reject doesn't show the null is true: we may simply lack power.
- **Why the wrong options are wrong (tutor only):**
  A) and B) p > α, so we don't reject.
  C) Failing to reject isn't evidence the null is true.
- **Hint:** Compare p to α, then remember what p can't tell you.

### ch14-quiz-10-v2
- **Kind:** AI-written version of ch14-quiz-10
- **Concepts:** Z tests & p-values
- **Type:** MC
- **Question:**

A study tests whether a fertilizer changes plant height and gets p = 0.01. Using α = 0.05, which statement is correct?

- **Options:**

  A) We reject the null, and we know the fertilizer changes height
  B) We reject the null, but we don't know for sure that the null is false
  C) We fail to reject the null, so the fertilizer has no effect
  D) We fail to reject the null, but we don't know if it is true

- **Answer (tutor only):** B
- **Explanation (tutor only):** p < α, so we reject. But rejecting doesn't prove the null false: a true null still gives p < 0.05 in 5% of studies (a type I error).
- **Why the wrong options are wrong (tutor only):**
  A) Rejection isn't proof.
  C) and D) p < α, so we reject.
- **Hint:** Can a true null give p = 0.01?

### ch14-quiz-11
- **Kind:** Course original
- **Concepts:** Normality & transformations
- **Type:** MC
- **Question:**

Transformations are one way to proceed when data are skewed and don't meet the assumptions of a statistical test. Which of the following statements is FALSE?

- **Options:**

  A) In many cases, an appropriate transformation can make data roughly normal
  B) We must transform every individual in the same way
  C) We must apply the same transformation to x and to y
  D) We can compare a few transformations to see which best normalizes the data, as long as we choose before running our statistical test

- **Answer (tutor only):** C
- **Explanation (tutor only):** We transform a variable to fix its own problem, so x and y can be transformed differently (or one not at all). But every value of a given variable must get the same transformation, and the choice should be made before looking at test results.
- **Why the wrong options are wrong (tutor only):**
  A) True: log or square-root transforms often normalize right-skewed data.
  B) True: transforming some individuals differently would distort the data.
  D) True: choosing a transformation is fine; choosing it based on which gives the smallest p-value is not.
- **Hint:** Does transforming y force you to transform x?

### ch14-quiz-11-v1
- **Kind:** AI-written version of ch14-quiz-11
- **Concepts:** Normality & transformations
- **Type:** MC
- **Question:**

Body masses of shrews are right-skewed, and a researcher considers transforming them before a statistical test. Which of the following is TRUE?

- **Options:**

  A) Every shrew's mass must be transformed in the same way
  B) If mass is transformed, the explanatory variable must be too
  C) Try many transformations and keep the one with the smallest p
  D) Transforming the data is never appropriate in statistics

- **Answer (tutor only):** A
- **Explanation (tutor only):** All values of a variable get the same transformation. Different variables can be transformed differently, and the choice is made before testing.
- **Why the wrong options are wrong (tutor only):**
  B) Each variable is transformed (or not) on its own merits.
  C) Choosing by p-value is p-hacking.
  D) Transformations are often appropriate.
- **Hint:** What must be consistent within one variable?

### ch14-quiz-11-v2
- **Kind:** AI-written version of ch14-quiz-11
- **Concepts:** Normality & transformations
- **Type:** MC
- **Question:**

Which of these is a legitimate way to choose a transformation for skewed data?

- **Options:**

  A) Compare a few transformations' normality before running the test
  B) Run the test on several transformations; keep the significant one
  C) Transform the large values only, leaving the small values alone
  D) Transform the response only in the group that looks most skewed

- **Answer (tutor only):** A
- **Explanation (tutor only):** It's fine to compare transformations by how well they normalize the data, as long as you decide before seeing test results and apply it to all values.
- **Why the wrong options are wrong (tutor only):**
  B) That's p-hacking.
  C) and D) All values of a variable must get the same transformation.
- **Hint:** When should the choice be made?

### ch14-quiz-12
- **Kind:** Course original
- **Concepts:** Normality & transformations
- **Type:** MC
- **Question:**

What is a potential problem with log and square-root transformations?

- **Options:**

  A) They might remove the one-to-one correspondence with original values
  B) They are undefined for some values
  C) They don't preserve the order of the original values

- **Answer (tutor only):** B
- **Explanation (tutor only):** You can't take the log of zero or a negative number, or the square root of a negative number. Data with zeros often get log(x + 1) instead.
- **Why the wrong options are wrong (tutor only):**
  A) For positive numbers, each original value has exactly one log and one square root.
  C) Both are monotonic for positive values: bigger values stay bigger.
- **Hint:** Try taking log(0) or √(-4).

### ch14-quiz-12-v1
- **Kind:** AI-written version of ch14-quiz-12
- **Concepts:** Normality & transformations
- **Type:** MC
- **Question:**

A dataset of parasite counts includes many zeros. Why can't we simply log-transform the counts?

- **Options:**

  A) The log of zero is undefined
  B) The log changes the order of the values
  C) Logs only work on normally distributed data
  D) Logs turn different counts into the same value

- **Answer (tutor only):** A
- **Explanation (tutor only):** log(0) is undefined (negative infinity). A common fix is log(x + 1).
- **Why the wrong options are wrong (tutor only):**
  B) The log keeps the order.
  C) Logs are often used to make skewed data more normal.
  D) The log is one-to-one.
- **Hint:** What is log(0)?

### ch14-quiz-12-v2
- **Kind:** AI-written version of ch14-quiz-12
- **Concepts:** Normality & transformations
- **Type:** MC
- **Question:**

A variable has values ranging from -5 to 20. Which transformation could NOT be applied to all of these values?

- **Options:**

  A) The square root
  B) Adding a constant of 10
  C) Multiplying by 2
  D) Squaring

- **Answer (tutor only):** A
- **Explanation (tutor only):** The square root of a negative number is undefined (and so is the log).
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) are defined for every number.
- **Hint:** Which one fails for negative numbers?

### ch14-quiz-13
- **Kind:** Course original
- **Concepts:** Normality & transformations
- **Type:** select-all
- **Question:**

What are potential problems with square transformations (x²) when data include negative values? (Select all that apply.)

- **Options:**

  A) They might remove the one-to-one correspondence with original values
  B) They are undefined for some values
  C) They don't preserve the order of the original values (not monotonic)

- **Answer (tutor only):** A, C
- **Explanation (tutor only):** Squaring makes -3 and 3 both equal 9, so different values become the same (no longer one-to-one), and order is scrambled (-3 < 2, but 9 > 4). Squaring is defined for every number, though.
- **Why the wrong options are wrong (tutor only):**
  B) You can square any number.
- **Hint:** What are (-3)² and 3²?

### ch14-quiz-13-v1
- **Kind:** AI-written version of ch14-quiz-13
- **Concepts:** Normality & transformations
- **Type:** select-all
- **Question:**

Data on temperature change include negative and positive values (e.g. -3 and 3). What happens if we square them? (Select all that apply.)

- **Options:**

  A) -3 and 3 both become 9, so different values become the same
  B) The order of values is no longer preserved
  C) The transformation is undefined for negative values
  D) The transformation is undefined when the value is zero

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** Squaring maps -3 and 3 to 9 (not one-to-one), and it scrambles order (-3 < 2, but 9 > 4). Squaring is defined for every number.
- **Why the wrong options are wrong (tutor only):**
  C) and D) Every number, including negatives and zero, can be squared.
- **Hint:** Try squaring -3, 2 and 3.

### ch14-quiz-13-v2
- **Kind:** AI-written version of ch14-quiz-13
- **Concepts:** Normality & transformations
- **Type:** select-all
- **Question:**

Which transformations keep the order of values (a larger value stays larger) when ALL data are positive? (Select all that apply.)

- **Options:**

  A) The log
  B) The square root
  C) Squaring
  D) Taking 1 / x

- **Answer (tutor only):** A, B, C
- **Explanation (tutor only):** For positive numbers, log, square root and squaring are all increasing. 1/x reverses the order (2 < 4, but 1/2 > 1/4).
- **Why the wrong options are wrong (tutor only):**
  D) 1/x reverses the order.
- **Hint:** Try each on the values 2 and 4.
