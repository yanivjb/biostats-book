# Applied Biostats tutor: question bank, chapters 10–12 (Exam 1, chapters 0–12)

Knowledge file for the course tutor. Each question has an ID, its concepts, the question, options, the answer, an explanation, why each wrong option is wrong, and a hint. Fields marked **tutor only** must never be shown to the student before they have answered.

- **Course originals** come from the instructor's homework, quizzes, Chime Ins and book.
- **AI-written versions** test the same idea with a new scenario or numbers. Their ID ends in -v1 or -v2 and names the original.
- 718 questions in all. 157 use a figure and are marked **Figure question (website only)**: students practice those on the study-guide website, where the figure is shown. Use one only when a student brings it to you; its figure link is included.

## Chapters and concepts

- **Chapter 0: Types of variables** — Variable types; Explanatory & response variables
- **Chapter 1: Getting started with R** — R basics; Assignment & the environment; Functions, pipes & packages; Errors & debugging; Scripts & reproducibility; Learning R
- **Chapter 2: ggplot** — Plot design principles; Aesthetics & ggplot layers; Visualizing associations
- **Chapter 3: Reproducible science** — Reproducible workflows; Data entry & data dictionaries; Missing data & bias
- **Chapter 4: Data in R** — Tidy data; dplyr verbs; Assignment & the environment; Errors & debugging
- **Chapter 5: Univariate summaries** — Shape of distributions; Center: mean & median; Spread: variance & SD; Range, IQR & boxplots; Coefficient of variation; Summaries in R
- **Chapter 6: Associations I** — Two categorical variables; Difference in means & Cohen's d; Visualizing associations; Association vs causation
- **Chapter 7: Associations II** — Covariance; Correlation; Association vs causation
- **Chapter 8: Sampling** — Samples, populations & estimates; Sampling distribution; SD vs SE; Sampling error vs bias; Non-independence; Shape of distributions
- **Chapter 9: Uncertainty** — Sampling distribution & SE; Bootstrap; Confidence intervals; Visualizing uncertainty
- **Chapter 10: Null hypothesis significance testing** — Null & alternative hypotheses; What a p-value means; Errors, power & sample size; Confounding & non-independence
- **Chapter 11: Shuffling (permutation)** — Bootstrap vs permutation; Permutation p-values; Bootstrap CIs; Non-independence & blocking
- **Chapter 12: Study design** — Experiments vs observational studies; Controls & placebos; Power & precision; Validity; The language of causation

## Chapter 10: Null hypothesis significance testing

### ch10-book-01
- **Kind:** Course original
- **Concepts:** Null & alternative hypotheses
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

### ch10-book-01-v1
- **Kind:** AI-written version of ch10-book-01
- **Concepts:** Null & alternative hypotheses
- **Type:** MC
- **Question:**

Which statement is most appropriate as a NULL hypothesis?

- **Options:**

  A) Mean lifespan is the same for fruit flies raised on high- and low-sugar diets
  B) High-sugar diets shorten fruit fly lifespan
  C) Diet affects fruit fly lifespan

- **Answer (tutor only):** A
- **Explanation (tutor only):** The null states no difference.
- **Why the wrong options are wrong (tutor only):**
  B) and C) claim an effect.
- **Hint:** Which says nothing is going on?

### ch10-book-01-v2
- **Kind:** AI-written version of ch10-book-01
- **Concepts:** Null & alternative hypotheses
- **Type:** MC
- **Question:**

Which statement is most appropriate as a NULL hypothesis for a study of whether bee visits are associated with flower color?

- **Options:**

  A) Bee visit rate is not associated with flower color
  B) Bees prefer blue flowers
  C) Flower color affects bee visits
  D) Bees visit flowers

- **Answer (tutor only):** A
- **Explanation (tutor only):** Null: no association.
- **Why the wrong options are wrong (tutor only):**
  B) and C) are alternatives.
  D) Not a testable statement about the association.
- **Hint:** No association = ?

### ch10-book-02
- **Kind:** Course original
- **Concepts:** Errors, power & sample size
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

### ch10-book-02-v1
- **Kind:** AI-written version of ch10-book-02
- **Concepts:** Errors, power & sample size
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

### ch10-book-02-v2
- **Kind:** AI-written version of ch10-book-02
- **Concepts:** Errors, power & sample size
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

### ch10-book-03
- **Kind:** Course original
- **Concepts:** Null & alternative hypotheses
- **Type:** matching
- **Question:**

In the T-shirt smell study, nine mothers each tried to pick their own child's shirt from two. Using a two-tailed test:

1. The null hypothesis is ____
2. The alternative hypothesis is ____

- **Options:**

  A) Mothers correctly guess their children's shirts half of the time
  B) Mothers correctly guess half of the time or less
  C) Mothers correctly guess more than half of the time
  D) Mothers do not correctly guess half of the time

- **Answer (tutor only):** 1-A, 2-D
- **Explanation (tutor only):** Null: just guessing (50%). Two-tailed alternative: not 50%, whether better or worse.
- **Why the wrong options are wrong (tutor only):**
  B) and C) are one-tailed versions.
- **Hint:** Two-tailed means the alternative doesn't pick a direction.

### ch10-book-03-v1
- **Kind:** AI-written version of ch10-book-03
- **Concepts:** Null & alternative hypotheses
- **Type:** matching
- **Question:**

Ten dogs each pick between two breath samples (one from a cancer patient). Using a two-tailed test:

1. The null hypothesis is ____
2. The alternative hypothesis is ____

- **Options:**

  A) Dogs pick the cancer sample more than half the time
  B) Dogs pick the cancer sample half the time
  C) Dogs do not pick the cancer sample half the time
  D) Dogs pick the cancer sample less than half the time

- **Answer (tutor only):** 1-B, 2-C
- **Explanation (tutor only):** Null: guessing (50%). Two-tailed alternative: not 50%, in either direction.
- **Why the wrong options are wrong (tutor only):**
  A) and D) are one-tailed alternatives.
- **Hint:** Two-tailed: no direction.

### ch10-book-03-v2
- **Kind:** AI-written version of ch10-book-03
- **Concepts:** Null & alternative hypotheses
- **Type:** MC
- **Question:**

In the T-shirt study, a researcher uses the one-tailed alternative 'mothers pick correctly more than half the time.' What is the risk compared with a two-tailed test?

- **Options:**

  A) If mothers were actually worse than chance (e.g., reliably picking the wrong shirt), the test couldn't detect it
  B) The null changes to 'mothers always pick correctly'
  C) The p-value gets larger
  D) There is no difference

- **Answer (tutor only):** A
- **Explanation (tutor only):** A one-tailed test only looks for an effect in one direction. Evidence in the other direction is ignored.
- **Why the wrong options are wrong (tutor only):**
  B) The null is still 50%.
  C) For results in the predicted direction, one-tailed p-values are smaller.
  D) The tails matter.
- **Hint:** What does a one-tailed test ignore?

### ch10-book-04
- **Kind:** Course original
- **Concepts:** What a p-value means
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch10-smell-null-dist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch10-smell-null-dist.png)
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

### ch10-book-04-v1
- **Kind:** AI-written version of ch10-book-04
- **Concepts:** What a p-value means
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch10-var-null10.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch10-var-null10.png)
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

### ch10-book-04-v2
- **Kind:** AI-written version of ch10-book-04
- **Concepts:** What a p-value means
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch10-smell-null-dist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch10-smell-null-dist.png)
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

### ch10-book-05
- **Kind:** Course original
- **Concepts:** What a p-value means
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch10-smell-null-dist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch10-smell-null-dist.png)
- **Question:**

Can parents identify their own children by smell? In Porter and Moore (1981), each of nine mothers was given her own child's worn T-shirt and one from another randomly chosen child, and asked to pick her own. Use a two-sided test with α = 0.05. The plot shows the probability of each number of correct guesses (0–9) if mothers were just guessing (the null distribution):

correct | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
probability | 0.002 | 0.018 | 0.07 | 0.164 | 0.246 | 0.246 | 0.164 | 0.07 | 0.018 | 0.002

With 8 of 9 correct, the P-value is about 0.04. What do we do with the null, and what do we know about it?

- **Options:**

  A) Reject it; but we need more information to know whether it's actually true or false
  B) Reject it; it is false
  C) Reject it; it has a 4% chance of being true
  D) Fail to reject it; not enough information

- **Answer (tutor only):** A
- **Explanation (tutor only):** p = 0.04 < 0.05, so we reject. But rejecting doesn't prove the null is false (we could be making a type I error), and the p-value isn't the probability that the null is true.
- **Why the wrong options are wrong (tutor only):**
  B) Rejecting isn't proof.
  C) That's the prosecutor's fallacy: P(data | H0) ≠ P(H0 | data).
  D) p < α.
- **Hint:** Compare p to α. Then: what does a p-value NOT tell you?

### ch10-book-05-v1
- **Kind:** AI-written version of ch10-book-05
- **Concepts:** What a p-value means
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch10-var-null10.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch10-var-null10.png)
- **Question:**

Can dogs smell cancer? Each of 10 trained dogs sniffs two breath samples (one from a patient with cancer, one without) and picks one. Use a two-sided test with α = 0.05. The plot and table show the probability of each number of correct picks if dogs were just guessing:

correct | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10
probability | 0.001 | 0.010 | 0.044 | 0.117 | 0.205 | 0.246 | 0.205 | 0.117 | 0.044 | 0.010 | 0.001

With 9 of 10 correct, the two-sided P-value is about 0.02. What do we do with the null, and what do we know?

- **Options:**

  A) Reject it; but we can't be certain it's false (this could be a type I error)
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

### ch10-book-05-v2
- **Kind:** AI-written version of ch10-book-05
- **Concepts:** What a p-value means; Errors, power & sample size
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch10-var-null10.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch10-var-null10.png)
- **Question:**

Can dogs smell cancer? Each of 10 trained dogs sniffs two breath samples (one from a patient with cancer, one without) and picks one. Use a two-sided test with α = 0.05. The plot and table show the probability of each number of correct picks if dogs were just guessing:

correct | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10
probability | 0.001 | 0.010 | 0.044 | 0.117 | 0.205 | 0.246 | 0.205 | 0.117 | 0.044 | 0.010 | 0.001

With 9 of 10 correct (p ≈ 0.02), a reporter writes: 'Dogs are 98% accurate at detecting cancer.' What's wrong?

- **Options:**

  A) It turns 1 − p into an accuracy; the observed accuracy was 90% (9/10), and with 10 dogs that estimate is very uncertain
  B) Nothing; that's correct
  C) The p-value should have been 0.10
  D) Dogs were 2% accurate

- **Answer (tutor only):** A
- **Explanation (tutor only):** The p-value is about how surprising 9/10 would be under guessing. The accuracy estimate is 9/10 = 0.9, with a wide CI because n is small.
- **Why the wrong options are wrong (tutor only):**
  B) 1 − p is not an accuracy or a probability of anything useful here.
  C) The p-value was computed correctly.
  D) Misreads p again.
- **Hint:** Where does the accuracy estimate actually come from?

### ch10-book-06
- **Kind:** Course original
- **Concepts:** What a p-value means
- **Type:** MC
- **Question:**

The prosecutor's fallacy is the mistaken thought that arises from assuming that:

- **Options:**

  A) People are innocent until proven guilty
  B) People are guilty until proven innocent
  C) Data are collected without sampling error
  D) The probability of the model given the data is the probability of the data given the model
  E) All evidence in a criminal case is independent and collected without bias

- **Answer (tutor only):** D
- **Explanation (tutor only):** P(model | data) ≠ P(data | model). A p-value is P(data | H0); treating it as P(H0 | data) is the fallacy.
- **Why the wrong options are wrong (tutor only):**
  A)–C) and E) aren't what the fallacy is about.
- **Hint:** Which way does the 'given' go?

### ch10-book-06-v1
- **Kind:** AI-written version of ch10-book-06
- **Concepts:** What a p-value means
- **Type:** MC
- **Question:**

Which pair of probabilities does the prosecutor's fallacy confuse?

- **Options:**

  A) P(evidence | innocent) and P(innocent | evidence)
  B) P(guilty) and P(innocent)
  C) α and β
  D) The mean and the median

- **Answer (tutor only):** A
- **Explanation (tutor only):** The fallacy swaps the conditional: how likely the evidence is if innocent, vs how likely innocence is given the evidence.
- **Why the wrong options are wrong (tutor only):**
  B) These are complements, not the confusion.
  C) Error rates, but not this fallacy.
  D) Unrelated.
- **Hint:** Which way does the 'given' go?

### ch10-book-06-v2
- **Kind:** AI-written version of ch10-book-06
- **Concepts:** What a p-value means
- **Type:** MC
- **Question:**

In hypothesis testing, the prosecutor's fallacy is treating ___ as if it were ___.

- **Options:**

  A) P(data | H0), P(H0 | data)
  B) P(H0 | data), P(data | H0)
  C) α, the power
  D) the effect size, the p-value

- **Answer (tutor only):** A
- **Explanation (tutor only):** The p-value is P(data this extreme | H0). The fallacy reads it as the probability that H0 is true given the data.
- **Why the wrong options are wrong (tutor only):**
  B) Backwards: the p-value is P(data | H0).
  C) and D) Different confusions.
- **Hint:** Which conditional probability is the p-value?

### ch10-chime-01
- **Kind:** Course original
- **Concepts:** What a p-value means
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

### ch10-chime-01-v1
- **Kind:** AI-written version of ch10-chime-01
- **Concepts:** What a p-value means
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

### ch10-chime-01-v2
- **Kind:** AI-written version of ch10-chime-01
- **Concepts:** What a p-value means
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

### ch10-chime-02
- **Kind:** Course original
- **Concepts:** Errors, power & sample size
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

### ch10-chime-02-v1
- **Kind:** AI-written version of ch10-chime-02
- **Concepts:** Errors, power & sample size
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

### ch10-chime-02-v2
- **Kind:** AI-written version of ch10-chime-02
- **Concepts:** Errors, power & sample size
- **Type:** MC
- **Question:**

A type II error is:

- **Options:**

  A) Failing to reject a null hypothesis that is false
  B) Rejecting a null hypothesis that is true
  C) Using the wrong test
  D) Getting p exactly 0.05

- **Answer (tutor only):** A
- **Explanation (tutor only):** Type II: missing a real effect. Its probability is 1 − power.
- **Why the wrong options are wrong (tutor only):**
  B) That's a type I error.
  C) and D) Not error types.
- **Hint:** Missed a real effect, or false alarm?

### ch10-chime-03
- **Kind:** Course original
- **Concepts:** Errors, power & sample size
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

### ch10-chime-03-v1
- **Kind:** AI-written version of ch10-chime-03
- **Concepts:** Errors, power & sample size
- **Type:** MC
- **Question:**

We use α = 0.10. Assuming the null is TRUE, what's the probability we reject it?

- **Options:**

  A) 0.10
  B) 0.90
  C) Depends on sample size
  D) Depends on effect size

- **Answer (tutor only):** A
- **Explanation (tutor only):** When the null is true, we falsely reject with probability α = 0.10.
- **Why the wrong options are wrong (tutor only):**
  B) That's the probability of (correctly) failing to reject.
  C) and D) α alone sets the false-positive rate.
- **Hint:** When H0 is true, P(reject) = α.

### ch10-chime-03-v2
- **Kind:** AI-written version of ch10-chime-03
- **Concepts:** Errors, power & sample size
- **Type:** MC
- **Question:**

A type I error is:

- **Options:**

  A) Rejecting a null hypothesis that is actually true
  B) Failing to reject a false null hypothesis
  C) Having a small sample
  D) Making a calculation error

- **Answer (tutor only):** A
- **Explanation (tutor only):** Type I: a false positive. Its probability (when H0 is true) is α.
- **Why the wrong options are wrong (tutor only):**
  B) That's type II.
  C) and D) Not error types.
- **Hint:** False alarm or missed effect?

### ch10-chime-04
- **Kind:** Course original
- **Concepts:** What a p-value means
- **Type:** MC
- **Question:**

Spot the flaw: researchers found a highly significant (p = 0.01) shift toward more daughters among radiologists compared with the general population. A newspaper wrote: 'this is highly significant as there is only a one percent probability the results were due to chance.' Which misinterpretation is this?

- **Options:**

  A) It misinterprets a P-value as the probability that the null hypothesis is true
  B) It tells a causal story while ignoring confounds
  C) It ignores sampling error
  D) It incorrectly uses the p-value as a measure of the size of an effect

- **Answer (tutor only):** A
- **Explanation (tutor only):** '1% probability the results were due to chance' means '1% chance the null is true.' But a p-value is the probability of results this extreme IF the null were true.
- **Why the wrong options are wrong (tutor only):**
  B) No causal story is told.
  C) The p-value does address sampling error.
  D) Nothing is said about how big the shift is.
- **Hint:** Rephrase 'due to chance' in terms of the null hypothesis.

### ch10-chime-04-v1
- **Kind:** AI-written version of ch10-chime-04
- **Concepts:** What a p-value means
- **Type:** MC
- **Question:**

Spot the flaw: a news article says, 'The trial found the drug reduced migraines (p = 0.04), meaning there is a 96% chance the drug works.' Which misinterpretation is this?

- **Options:**

  A) Treating the p-value as a probability about the hypothesis
  B) A causal story that ignores confounds
  C) Ignoring sampling error
  D) Using the p-value as a measure of effect size

- **Answer (tutor only):** A
- **Explanation (tutor only):** 1 − p isn't the probability the drug works. The p-value is P(data this extreme | no effect).
- **Why the wrong options are wrong (tutor only):**
  B) A randomized trial handles confounds; that's not the error.
  C) The p-value addresses sampling error.
  D) Nothing about effect size is claimed.
- **Hint:** What does the p-value assume?

### ch10-chime-04-v2
- **Kind:** AI-written version of ch10-chime-04
- **Concepts:** What a p-value means; Errors, power & sample size
- **Type:** MC
- **Question:**

Spot the flaw: 'Our new teaching method had a highly significant effect (p < 0.0001), so it's a huge improvement.' Which misinterpretation is this?

- **Options:**

  A) Using the p-value as a measure of effect size
  B) Treating the p-value as the probability that the null is true
  C) A causal story that ignores confounds
  D) Ignoring sampling error

- **Answer (tutor only):** A
- **Explanation (tutor only):** A tiny p-value can come from a small effect in a large study; 'huge' needs the estimate.
- **Why the wrong options are wrong (tutor only):**
  B) No probability of the null is stated.
  C) Possible, but the stated flaw is jumping from p to 'huge'.
  D) The p-value does address sampling error.
- **Hint:** Does p measure 'how big'?

### ch10-chime-05
- **Kind:** Course original
- **Concepts:** Confounding & non-independence
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

### ch10-chime-05-v1
- **Kind:** AI-written version of ch10-chime-05
- **Concepts:** Confounding & non-independence
- **Type:** MC
- **Question:**

Spot the flaw: a survey finds that children who eat breakfast get better grades. A school board concludes that serving breakfast will raise grades. What's the main problem?

- **Options:**

  A) It tells a causal story while ignoring confounds (e.g., family income or routines may affect both breakfast and grades)
  B) It misinterprets a p-value as the probability the null is true
  C) It ignores sampling error
  D) It uses a p-value as a measure of effect size

- **Answer (tutor only):** A
- **Explanation (tutor only):** Observational association doesn't show causation. Families that serve breakfast may differ in many ways that also affect grades.
- **Why the wrong options are wrong (tutor only):**
  B)–D) No p-value is misused; the problem is the causal leap.
- **Hint:** Was breakfast randomly assigned?

### ch10-chime-05-v2
- **Kind:** AI-written version of ch10-chime-05
- **Concepts:** Confounding & non-independence
- **Type:** MC
- **Question:**

Spot the flaw: 'Cities with more police officers have more crime, so police cause crime.' What's the most likely issue?

- **Options:**

  A) Reverse causation or confounding: cities with more crime hire more police, and bigger cities have more of both
  B) The p-value was misread
  C) Sampling error
  D) Effect size was ignored

- **Answer (tutor only):** A
- **Explanation (tutor only):** The association could run the other way (crime → more police) or be driven by city size.
- **Why the wrong options are wrong (tutor only):**
  B)–D) The problem is the causal interpretation.
- **Hint:** Which way could the arrow point?

### ch10-gquiz-01
- **Kind:** Course original
- **Concepts:** Null & alternative hypotheses
- **Type:** matching
- **Question:**

Anna (a former TA) noticed that her dog, Calvin, chases both black and gray squirrels, and wants to know if he has a preference. She conducts a two-tailed test.

Which statement is the null hypothesis, and which is the alternative?

1. Null hypothesis
2. Alternative hypothesis

- **Options:**

  A) Calvin prefers black squirrels
  B) Calvin is not equally interested in black and gray squirrels
  C) Calvin prefers gray squirrels
  D) Calvin is equally interested in black and gray squirrels

- **Answer (tutor only):** 1-D, 2-B
- **Explanation (tutor only):** The null is the 'nothing interesting' claim: no preference. A two-tailed alternative is simply 'not equal', i.e., a preference in either direction.
- **Why the wrong options are wrong (tutor only):**
  A) and C) are one-tailed (directional) alternatives, which don't match a two-tailed test.
- **Hint:** Two-tailed: does the alternative pick a direction?

### ch10-gquiz-01-v1
- **Kind:** AI-written version of ch10-gquiz-01
- **Concepts:** Null & alternative hypotheses
- **Type:** matching
- **Question:**

A birder wonders whether a robin prefers red or yellow berries. She offers both colors many times and runs a two-tailed test.

Which statement is the null hypothesis, and which is the alternative?

1. Null hypothesis
2. Alternative hypothesis

- **Options:**

  A) The robin eats red and yellow berries equally often
  B) The robin prefers red berries
  C) The robin does not eat red and yellow berries equally often
  D) The robin prefers yellow berries

- **Answer (tutor only):** 1-A, 2-C
- **Explanation (tutor only):** Null: no preference. Two-tailed alternative: a preference in either direction ('not equal').
- **Why the wrong options are wrong (tutor only):**
  B) and D) are one-tailed (directional) alternatives, which don't match a two-tailed test.
- **Hint:** Two-tailed means no direction is specified.

### ch10-gquiz-01-v2
- **Kind:** AI-written version of ch10-gquiz-01
- **Concepts:** Null & alternative hypotheses
- **Type:** matching
- **Question:**

A researcher tests whether a new fertilizer changes mean tomato yield. Match each statement to its role:

1. Null hypothesis
2. Two-tailed alternative
3. One-tailed alternative

- **Options:**

  A) Mean yield with fertilizer is different from mean yield without it
  B) Mean yield is the same with and without fertilizer
  C) Mean yield is higher with fertilizer

- **Answer (tutor only):** 1-B, 2-A, 3-C
- **Explanation (tutor only):** The null says no effect. A two-tailed alternative says 'different' in either direction; a one-tailed alternative picks a direction.
- **Why the wrong options are wrong (tutor only):**
  'Higher' commits to one direction, so it's one-tailed.
- **Hint:** Which statement has no direction?

### ch10-gquiz-02
- **Kind:** Course original
- **Concepts:** Confounding & non-independence
- **Type:** MC
- **Question:**

Anna (a former TA) noticed that her dog, Calvin, chases both black and gray squirrels, and wants to know if he has a preference. She conducts a two-tailed test.

Anna records chases and finds that Calvin chases significantly more gray than black squirrels, so she rejects the null. What is the biggest mistake she made?

- **Options:**

  A) She is not considering a Bayesian approach
  B) She is not considering the confound that Calvin may encounter gray and black squirrels at different frequencies
  C) We should never reject the null hypothesis

- **Answer (tutor only):** B
- **Explanation (tutor only):** If gray squirrels are simply more common, Calvin would chase more of them with no preference at all. She has to compare chases to encounters.
- **Why the wrong options are wrong (tutor only):**
  A) A Bayesian approach would have the same problem.
  C) Rejecting the null is fine when the evidence supports it; the problem is what the null was compared to.
- **Hint:** What if there are just more gray squirrels around?

### ch10-gquiz-02-v1
- **Kind:** AI-written version of ch10-gquiz-02
- **Concepts:** Confounding & non-independence
- **Type:** MC
- **Question:**

A birder wonders whether a robin prefers red or yellow berries. She offers both colors many times and runs a two-tailed test.

She counts which berries the robin eats in her yard, finds it eats significantly more red berries, and concludes it prefers red. Her yard has four red-berry bushes and one yellow-berry bush. What's the biggest problem?

- **Options:**

  A) Red berries are more available, so the robin could eat more of them with no preference at all
  B) She should have used a one-tailed test
  C) She should never reject the null
  D) The sample size is too large

- **Answer (tutor only):** A
- **Explanation (tutor only):** Availability is a confound: compare what the robin eats with what it encounters (or offer equal numbers).
- **Why the wrong options are wrong (tutor only):**
  B) The tail choice doesn't fix the comparison problem.
  C) Rejecting is fine when the comparison is fair.
  D) More data doesn't create this problem.
- **Hint:** What would the robin eat if it had no preference?

### ch10-gquiz-02-v2
- **Kind:** AI-written version of ch10-gquiz-02
- **Concepts:** Confounding & non-independence
- **Type:** MC
- **Question:**

A study finds that people who own more houseplants report significantly lower stress (p = 0.003). The authors conclude that houseplants reduce stress. What's the biggest problem?

- **Options:**

  A) Plant owners may differ in other ways (more free time, bigger homes, income) that affect stress, so this doesn't show causation
  B) p = 0.003 is too large to be significant
  C) The p-value measures the size of the stress reduction
  D) There's no problem

- **Answer (tutor only):** A
- **Explanation (tutor only):** This is observational: confounds (or reverse causation, such as relaxed people buying plants) could produce the association.
- **Why the wrong options are wrong (tutor only):**
  B) 0.003 is small.
  C) p-values don't measure effect size.
  D) The causal claim isn't supported.
- **Hint:** Was plant ownership randomly assigned?

### ch10-gquiz-03
- **Kind:** Course original
- **Concepts:** What a p-value means; Errors, power & sample size
- **Type:** MC
- **Question:**

Anna (a former TA) noticed that her dog, Calvin, chases both black and gray squirrels, and wants to know if he has a preference. She conducts a two-tailed test.

Anna fixes the encounter problem and records thousands of encounters over many years. Her p-value is very low (p = 0.001), and she concludes that Calvin has a STRONG preference for gray squirrels. What is her biggest mistake?

- **Options:**

  A) She is using an arbitrary p-value threshold as a 'bright line' for decision making
  B) She is misusing a p-value as a measure of the effect size
  C) She is not considering the possibility that this pattern arose by chance

- **Answer (tutor only):** B
- **Explanation (tutor only):** With thousands of observations, even a tiny preference gives a tiny p-value. A small p says the data are hard to explain under the null; it says nothing about how big the preference is. Look at the estimate (e.g., 56% vs 50%).
- **Why the wrong options are wrong (tutor only):**
  A) No threshold is involved in her mistake: she jumped from small p to 'strong.'
  C) p = 0.001 does address chance.
- **Hint:** With huge n, how big must an effect be to give a small p?

### ch10-gquiz-03-v1
- **Kind:** AI-written version of ch10-gquiz-03
- **Concepts:** What a p-value means; Errors, power & sample size
- **Type:** MC
- **Question:**

A study of 500,000 people finds that a supplement lowers blood pressure by 0.3 mmHg on average (p < 0.0001). A headline says the supplement 'dramatically lowers blood pressure.' What's the main mistake?

- **Options:**

  A) Treating a tiny p-value as evidence of a large effect: 0.3 mmHg is trivially small
  B) Ignoring that the result might be due to chance
  C) Using a two-tailed test
  D) The sample is too small

- **Answer (tutor only):** A
- **Explanation (tutor only):** With half a million people, even a negligible effect is easily detected. The p-value says the effect is probably not zero; the estimate (0.3 mmHg) says it's tiny.
- **Why the wrong options are wrong (tutor only):**
  B) p < 0.0001 addresses chance.
  C) Tail choice isn't the issue.
  D) The sample is enormous.
- **Hint:** Look at the size of the estimate, not the p-value.

### ch10-gquiz-03-v2
- **Kind:** AI-written version of ch10-gquiz-03
- **Concepts:** What a p-value means; Errors, power & sample size
- **Type:** MC
- **Question:**

Study 1 reports p = 0.001; Study 2 reports p = 0.04. Which conclusion is justified?

- **Options:**

  A) Neither p-value tells us which effect is larger; we need the effect sizes (and their CIs)
  B) Study 1 found a bigger effect
  C) Study 2 found a bigger effect
  D) Study 1's effect is 40 times larger

- **Answer (tutor only):** A
- **Explanation (tutor only):** p-values depend on both effect size and sample size. A small p could come from a small effect in a huge study.
- **Why the wrong options are wrong (tutor only):**
  B)–D) These treat the p-value as a measure of effect size.
- **Hint:** What two things does a p-value depend on?

### ch10-gquiz-04
- **Kind:** Course original
- **Concepts:** What a p-value means
- **Type:** MC
- **Question:**

Anna (a former TA) noticed that her dog, Calvin, chases both black and gray squirrels, and wants to know if he has a preference. She conducts a two-tailed test.

Anna's p-value of 0.001 means (pick the best answer):

- **Options:**

  A) There is a 0.1% chance that Calvin has no preference
  B) There is a 0.1% chance that Anna's results are due to chance
  C) If Calvin truly had no preference, there would be a 0.1% chance of seeing a difference this large or larger
  D) There is a 99.9% chance that Calvin has a preference

- **Answer (tutor only):** C
- **Explanation (tutor only):** A p-value is a probability about data, calculated assuming the null is true: P(data this extreme or more | H0). It is not the probability that the null (or the alternative) is true.
- **Why the wrong options are wrong (tutor only):**
  A), B) and D) all flip it into a probability about the hypothesis. That's the prosecutor's fallacy.
- **Hint:** A p-value assumes the null is true. Can it then tell you the probability that the null is true?

### ch10-gquiz-04-v1
- **Kind:** AI-written version of ch10-gquiz-04
- **Concepts:** What a p-value means
- **Type:** MC
- **Question:**

A birder wonders whether a robin prefers red or yellow berries. She offers both colors many times and runs a two-tailed test.

She gets p = 0.03. What does this mean?

- **Options:**

  A) If the robin truly had no preference, there'd be a 3% chance of a difference this large or larger
  B) There's a 3% chance the robin has no preference
  C) There's a 97% chance the robin has a preference
  D) There's a 3% chance her results are wrong

- **Answer (tutor only):** A
- **Explanation (tutor only):** A p-value is P(data this extreme or more | H0 true). It isn't a probability about the hypothesis.
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) all turn it into a probability about the hypothesis (the prosecutor's fallacy).
- **Hint:** Probability of what, assuming what?

### ch10-gquiz-04-v2
- **Kind:** AI-written version of ch10-gquiz-04
- **Concepts:** What a p-value means
- **Type:** TF
- **Question:**

True or false: a p-value of 0.20 means there is a 20% chance the null hypothesis is true.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** p = 0.20 means: if the null were true, results this extreme or more would happen 20% of the time. It says nothing directly about the chance the null is true.
- **Why the wrong options are wrong (tutor only):**
  A) That's the prosecutor's fallacy: P(data | H0) ≠ P(H0 | data).
- **Hint:** The p-value assumes the null is true.

### ch10-gquiz-05
- **Kind:** Course original
- **Concepts:** Confounding & non-independence
- **Type:** MC
- **Question:**

Anna (a former TA) noticed that her dog, Calvin, chases both black and gray squirrels, and wants to know if he has a preference. She conducts a two-tailed test.

Anna realizes her thousands of observations all came from four families of squirrels: one all white, one all gray, and two mixed. Which assumption does this violate?

- **Options:**

  A) Normally distributed error
  B) Data collected without sampling bias
  C) Data collected without sampling error
  D) Data collected independently

- **Answer (tutor only):** D
- **Explanation (tutor only):** Chases within a family are related (same squirrels, same places), so she effectively has about four independent units, not thousands. Non-independence makes p-values look far more convincing than they should.
- **Why the wrong options are wrong (tutor only):**
  A) Not relevant to this design.
  B) It might also be unrepresentative, but the core problem is that the observations are clustered.
  C) Sampling error is always present; it's not an assumption.
- **Hint:** How many truly independent units does she have?

### ch10-gquiz-05-v1
- **Kind:** AI-written version of ch10-gquiz-05
- **Concepts:** Confounding & non-independence
- **Type:** MC
- **Question:**

A researcher compares bill length between two islands by measuring 400 birds, but all birds come from 3 nests per island. Which assumption is most clearly violated?

- **Options:**

  A) Independence of observations
  B) No sampling error
  C) Normally distributed data
  D) A two-tailed test

- **Answer (tutor only):** A
- **Explanation (tutor only):** Siblings from the same nest share genes and environment, so 400 birds act more like 6 independent units. Treating them as 400 inflates confidence and shrinks p-values.
- **Why the wrong options are wrong (tutor only):**
  B) Sampling error is always present.
  C) Not the core issue here.
  D) That's a choice, not an assumption.
- **Hint:** How many truly independent units are there?

### ch10-gquiz-05-v2
- **Kind:** AI-written version of ch10-gquiz-05
- **Concepts:** Confounding & non-independence
- **Type:** MC
- **Question:**

A study measures 50 students' reaction times 20 times each and analyzes all 1000 measurements as independent. What's the likely consequence?

- **Options:**

  A) Standard errors are too small and p-values too small: the study looks more convincing than it is
  B) p-values are too large
  C) There's no consequence
  D) The estimate becomes biased upward

- **Answer (tutor only):** A
- **Explanation (tutor only):** Repeated measurements on the same person are correlated. Treating them as independent overstates the information, giving too-narrow CIs and too-small p-values.
- **Why the wrong options are wrong (tutor only):**
  B) The error goes the other way.
  C) Pseudoreplication matters.
  D) The main problem is overstated precision, not bias.
- **Hint:** Is the 20th measurement of a student new information?

### ch10-gquiz-06
- **Kind:** Course original
- **Concepts:** What a p-value means
- **Type:** select-all
- **Question:**

Anna (a former TA) noticed that her dog, Calvin, chases both black and gray squirrels, and wants to know if he has a preference. She conducts a two-tailed test.

After correcting for encounter rates, Anna estimates that 56% of Calvin's chases are of gray squirrels, 95% CI: 55.3% to 56.7%. Which statements are true? (Select all.)

- **Options:**

  A) If Calvin had no preference we'd expect 50%; because 50% is outside the 95% CI, Anna would reject the null at α = 0.05
  B) There's a 95% chance that Calvin's true preference is between 55.3% and 56.7%
  C) If Anna repeated her study many times, about 95% of the intervals would contain Calvin's true preference
  D) If Anna had studied Calvin for half as long, her CI would probably be wider

- **Answer (tutor only):** A, C, D
- **Explanation (tutor only):** A 95% CI that excludes the null value corresponds to p < 0.05. The 95% describes the method (C), not this particular interval (B). Less data means a bigger SE and a wider CI (D). Also notice: the preference is real but modest (56% vs 50%).
- **Why the wrong options are wrong (tutor only):**
  B) Any one interval either contains the truth or doesn't.
- **Hint:** What does the '95%' describe: this interval, or the method?

### ch10-gquiz-06-v1
- **Kind:** AI-written version of ch10-gquiz-06
- **Concepts:** What a p-value means
- **Type:** select-all
- **Question:**

A study estimates the mean difference in growth between fertilized and control plants as 2.1 cm, 95% CI: −0.4 to 4.6 cm. Which are true? (Select all.)

- **Options:**

  A) Since 0 is inside the 95% CI, the null of no difference would not be rejected at α = 0.05
  B) This shows fertilizer has no effect
  C) The data are consistent with effects ranging from slightly negative to fairly large
  D) A larger study would likely give a narrower interval

- **Answer (tutor only):** A, C, D
- **Explanation (tutor only):** A 95% CI containing 0 corresponds to p > 0.05. That's not evidence of no effect: the interval includes sizable positive effects. More data would narrow it.
- **Why the wrong options are wrong (tutor only):**
  B) Failing to reject isn't the same as showing no effect.
- **Hint:** Is the null value inside the CI? What else is inside it?

### ch10-gquiz-06-v2
- **Kind:** AI-written version of ch10-gquiz-06
- **Concepts:** What a p-value means
- **Type:** select-all
- **Question:**

The proportion of seeds that germinate under a new treatment is estimated at 0.62, 95% CI: 0.55 to 0.69. Untreated seeds germinate at 0.50. Which are true? (Select all.)

- **Options:**

  A) A test of H0: p = 0.50 would reject at α = 0.05
  B) There's a 95% chance the true proportion is between 0.55 and 0.69
  C) About 95% of intervals made this way would contain the true proportion
  D) A 99% CI from the same data would be wider

- **Answer (tutor only):** A, C, D
- **Explanation (tutor only):** 0.50 is outside the 95% CI, so p < 0.05. The 95% describes the method. More confidence requires a wider interval.
- **Why the wrong options are wrong (tutor only):**
  B) The probability belongs to the method, not this one interval.
- **Hint:** Where is 0.50 relative to the interval?

### ch10-gquiz-07
- **Kind:** Course original
- **Concepts:** What a p-value means; Errors, power & sample size
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

### ch10-gquiz-07-v1
- **Kind:** AI-written version of ch10-gquiz-07
- **Concepts:** What a p-value means; Errors, power & sample size
- **Type:** MC
- **Question:**

A tiny study (n = 12) of a memory supplement reports a huge, significant effect (p = 0.04) and gets wide media coverage. Three later studies with n > 500 each find tiny, non-significant effects. What's most likely?

- **Options:**

  A) The supplement has little or no effect; the small study's large estimate was probably exaggerated by chance (and amplified by attention to striking results)
  B) The supplement has a huge effect
  C) The later studies were all done wrong
  D) The supplement has a moderate effect

- **Answer (tutor only):** A
- **Explanation (tutor only):** Small studies that reach significance tend to overestimate effects (the winner's curse). The large, precise studies carry more weight.
- **Why the wrong options are wrong (tutor only):**
  B) One noisy study vs three precise ones.
  C) No reason to think so.
  D) None of the precise studies supports that.
- **Hint:** Which studies are more precise?

### ch10-gquiz-07-v2
- **Kind:** AI-written version of ch10-gquiz-07
- **Concepts:** What a p-value means; Errors, power & sample size
- **Type:** MC
- **Question:**

Why do significant results from small studies tend to overestimate the true effect?

- **Options:**

  A) With small samples, estimates are noisy, and only the ones that happen to be unusually large cross the significance threshold
  B) Small studies always measure the wrong thing
  C) Small studies have smaller standard errors
  D) They don't; small studies are unbiased

- **Answer (tutor only):** A
- **Explanation (tutor only):** To reach p < 0.05 with a large SE, the estimate must be big. If the true effect is modest, only lucky overestimates make the cut. This is the winner's curse.
- **Why the wrong options are wrong (tutor only):**
  B) Small isn't wrong.
  C) Small studies have larger SEs.
  D) Each estimate is unbiased, but the significant subset is biased upward.
- **Hint:** What has to happen for a small study to reach p < 0.05?

### ch10-gquiz-08
- **Kind:** Course original
- **Concepts:** What a p-value means; Errors, power & sample size
- **Type:** MC
- **Question:**

Two labs are testing the efficacy of a new heart disease medication:
• Lab 1 runs a small pilot study, finds a modest, non-significant effect (P = 0.35), and gives up on the drug.
• Lab 2 runs a larger study, finds a very similar modest effect, and rejects the null (P ≪ 0.05).

Which conclusion is more likely?

- **Options:**

  A) The medicine has either a weak effect or no effect
  B) The medicine has a very strong effect
  C) The medicine has a real but modest effect
  D) Both hypotheses are equally likely

- **Answer (tutor only):** C
- **Explanation (tutor only):** Both labs estimated a similar, modest effect. The small study just lacked the power to detect it (its CI was wide and included 0). Non-significant ≠ no effect.
- **Why the wrong options are wrong (tutor only):**
  A) Lab 1's p = 0.35 doesn't show there's no effect.
  B) Both estimates are modest.
  D) The two studies agree on the size of the effect.
- **Hint:** Compare the estimated effects, not the p-values.

### ch10-gquiz-08-v1
- **Kind:** AI-written version of ch10-gquiz-08
- **Concepts:** What a p-value means; Errors, power & sample size
- **Type:** MC
- **Question:**

A small study (n = 15 per group) finds that a mentoring program raises test scores by 4 points (p = 0.30). A large study (n = 800 per group) finds a 3.5-point increase (p < 0.001). Which conclusion is most likely?

- **Options:**

  A) The program has a real but modest effect; the small study lacked power
  B) The program has no effect, because the first study wasn't significant
  C) The studies contradict each other
  D) The program has a huge effect

- **Answer (tutor only):** A
- **Explanation (tutor only):** Both estimates are similar (about 3.5–4 points). The small study's CI was wide and included 0. Not significant ≠ no effect.
- **Why the wrong options are wrong (tutor only):**
  B) p = 0.30 doesn't show no effect.
  C) The estimates agree.
  D) Both estimates are modest.
- **Hint:** Compare the estimates, not just the p-values.

### ch10-gquiz-08-v2
- **Kind:** AI-written version of ch10-gquiz-08
- **Concepts:** What a p-value means; Errors, power & sample size
- **Type:** TF
- **Question:**

True or false: if a study fails to reject the null (p = 0.40), we can conclude the treatment has no effect.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** Failing to reject means the data are consistent with no effect, but they may also be consistent with real effects. The study may have lacked power. Absence of evidence isn't evidence of absence.
- **Why the wrong options are wrong (tutor only):**
  A) Not significant ≠ no effect; look at the CI.
- **Hint:** What range of effects would be consistent with these data?

### ch10-hw-01
- **Kind:** Course original
- **Concepts:** Null & alternative hypotheses
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

### ch10-hw-01-v1
- **Kind:** AI-written version of ch10-hw-01
- **Concepts:** Null & alternative hypotheses
- **Type:** MC
- **Question:**

Which statement is most appropriate as an ALTERNATIVE hypothesis?

- **Options:**

  A) Mean seed size differs between plants in shaded and sunny plots
  B) Mean seed size is the same in shaded and sunny plots
  C) Shaded plants produce seeds exactly 1.2 mg heavier than sunny plants

- **Answer (tutor only):** A
- **Explanation (tutor only):** An alternative hypothesis claims a difference or association.
- **Why the wrong options are wrong (tutor only):**
  B) 'The same' is the null.
  C) Alternatives don't usually claim an exact value.
- **Hint:** Which statement claims something is going on?

### ch10-hw-01-v2
- **Kind:** AI-written version of ch10-hw-01
- **Concepts:** Null & alternative hypotheses
- **Type:** MC
- **Question:**

A researcher asks whether salamander abundance is associated with stream temperature. Which is the null hypothesis?

- **Options:**

  A) There is no association between salamander abundance and stream temperature
  B) Salamanders are more abundant in cooler streams
  C) Stream temperature affects salamander abundance
  D) Salamanders are rare

- **Answer (tutor only):** A
- **Explanation (tutor only):** The null is 'no association'.
- **Why the wrong options are wrong (tutor only):**
  B) and C) These claim an association (alternatives).
  D) That isn't a hypothesis about the relationship.
- **Hint:** The null says nothing is going on.

### ch10-hw-02
- **Kind:** Course original
- **Concepts:** Null & alternative hypotheses
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

### ch10-hw-02-v1
- **Kind:** AI-written version of ch10-hw-02
- **Concepts:** Null & alternative hypotheses
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

### ch10-hw-02-v2
- **Kind:** AI-written version of ch10-hw-02
- **Concepts:** Null & alternative hypotheses
- **Type:** MC
- **Question:**

Why does the book generally recommend two-tailed tests?

- **Options:**

  A) We'd usually want to know about a surprising effect in the 'wrong' direction too, and one-tailed tests make it too easy to get significance after seeing the data
  B) Two-tailed tests always give smaller p-values
  C) One-tailed tests are mathematically invalid
  D) Two-tailed tests don't need a null hypothesis

- **Answer (tutor only):** A
- **Explanation (tutor only):** A one-tailed test ignores effects in the other direction and halves the p-value for the chosen one, which is tempting to pick after the fact.
- **Why the wrong options are wrong (tutor only):**
  B) For the same data, two-tailed p-values are larger.
  C) They're valid when justified in advance.
  D) Every test needs a null.
- **Hint:** What does a one-tailed test ignore?

### ch10-hw-03
- **Kind:** Course original
- **Concepts:** What a p-value means; Errors, power & sample size
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

### ch10-hw-03-v1
- **Kind:** AI-written version of ch10-hw-03
- **Concepts:** What a p-value means; Errors, power & sample size
- **Type:** MC
- **Question:**

A study of 2 million smartphone users finds that a new app layout increases time on the app by 0.4 seconds per day (p < 0.0001). What's the best interpretation?

- **Options:**

  A) The effect is almost certainly real but practically negligible
  B) The effect is large because p is so small
  C) The result is probably due to chance
  D) The study was biased because it was large

- **Answer (tutor only):** A
- **Explanation (tutor only):** Huge samples detect tiny effects. Significance tells you the effect is probably not zero; the estimate (0.4 s) tells you it doesn't matter much.
- **Why the wrong options are wrong (tutor only):**
  B) p-values don't measure effect size.
  C) p < 0.0001 makes chance an unlikely explanation.
  D) Size doesn't cause bias.
- **Hint:** Separate 'is there an effect?' from 'how big is it?'

### ch10-hw-03-v2
- **Kind:** AI-written version of ch10-hw-03
- **Concepts:** What a p-value means; Errors, power & sample size
- **Type:** MC
- **Question:**

If the true effect is small but not zero, what happens to the p-value as sample size grows (on average)?

- **Options:**

  A) It gets smaller, eventually falling below 0.05
  B) It stays about the same
  C) It gets larger
  D) It equals the effect size

- **Answer (tutor only):** A
- **Explanation (tutor only):** A larger n shrinks the SE, so even a small real effect becomes more and more detectable.
- **Why the wrong options are wrong (tutor only):**
  B) The p-value depends on n.
  C) More data gives more evidence, not less.
  D) p-values aren't effect sizes.
- **Hint:** What does a bigger n do to the SE?

### ch10-hw-04
- **Kind:** Course original
- **Concepts:** What a p-value means; Errors, power & sample size
- **Type:** MC
- **Question:**

Two well-designed studies test the same null hypothesis. Study A has 20 participants; Study B has 2,000. If the null hypothesis is actually TRUE, which study is more likely to get a 'statistically significant' result (p < 0.05) just by chance?

- **Options:**

  A) Study A (20 participants)
  B) Study B (2,000 participants)
  C) Both are equally likely

- **Answer (tutor only):** C
- **Explanation (tutor only):** When the null is true, p-values are equally likely to fall anywhere, so P(p < 0.05) = 0.05 regardless of sample size. That's what α means: the false-positive rate is set by the threshold, not by n.
- **Why the wrong options are wrong (tutor only):**
  A) and B) Sample size affects power (the chance of detecting a real effect), not the false-positive rate when the null is true.
- **Hint:** If the null is true, what is P(p < α)?

### ch10-hw-04-v1
- **Kind:** AI-written version of ch10-hw-04
- **Concepts:** Errors, power & sample size
- **Type:** MC
- **Question:**

If the null hypothesis is TRUE and you use α = 0.01, what's the probability of a false positive (p < 0.01)?

- **Options:**

  A) 0.01, regardless of sample size
  B) 0.05
  C) Smaller for bigger studies
  D) Larger for bigger studies

- **Answer (tutor only):** A
- **Explanation (tutor only):** When the null is true, the false-positive rate equals α, whatever the sample size.
- **Why the wrong options are wrong (tutor only):**
  B) That's for α = 0.05.
  C) and D) Sample size affects power, not the false-positive rate.
- **Hint:** When H0 is true, P(reject) = ?

### ch10-hw-04-v2
- **Kind:** AI-written version of ch10-hw-04
- **Concepts:** Errors, power & sample size
- **Type:** MC
- **Question:**

A researcher tests 20 different foods for an effect on sleep, and none truly has any effect. Using α = 0.05, about how many tests would you expect to come out 'significant' anyway?

- **Options:**

  A) About 1
  B) 0
  C) About 5
  D) About 19

- **Answer (tutor only):** A
- **Explanation (tutor only):** Each test has a 5% false-positive rate when the null is true: 20 × 0.05 = 1.
- **Why the wrong options are wrong (tutor only):**
  B) False positives happen at rate α.
  C) That would need 100 tests.
  D) That's how many correctly fail to reject.
- **Hint:** Multiply the number of tests by α.

### ch10-hw-05
- **Kind:** Course original
- **Concepts:** What a p-value means
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch10-smell-null-dist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch10-smell-null-dist.png)
- **Question:**

Can parents identify their own children by smell? In Porter and Moore (1981), each of nine mothers was given her own child's worn T-shirt and one from another randomly chosen child, and asked to pick her own. Use a two-sided test with α = 0.05. The plot shows the probability of each number of correct guesses (0–9) if mothers were just guessing (the null distribution):

correct | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
probability | 0.002 | 0.018 | 0.07 | 0.164 | 0.246 | 0.246 | 0.164 | 0.07 | 0.018 | 0.002

Suppose 7 of 9 mothers identified their children correctly. Use the probabilities to estimate the (two-sided) P-value.

- **Answer (tutor only):** ≈ 0.18
- **Explanation (tutor only):** Add up the probabilities of results at least as extreme as 7, in both tails: P(7, 8 or 9) = 0.07 + 0.018 + 0.002 = 0.09; doubled for two sides = 0.18 (exact: 0.1797).
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: using only P(7) = 0.07; forgetting to double for a two-sided test (0.09); or counting only one tail.
- **Hint:** 'As or more extreme' in BOTH directions: 7, 8, 9 and 2, 1, 0.

### ch10-hw-05-v1
- **Kind:** AI-written version of ch10-hw-05
- **Concepts:** What a p-value means
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch10-smell-null-dist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch10-smell-null-dist.png)
- **Question:**

Can parents identify their own children by smell? Each of nine mothers was given her own child's worn T-shirt and one from another child, and asked to pick her own. Use a two-sided test with α = 0.05. If mothers were just guessing, the probabilities of each number of correct picks are:

correct | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
probability | 0.002 | 0.018 | 0.07 | 0.164 | 0.246 | 0.246 | 0.164 | 0.07 | 0.018 | 0.002

Suppose only 2 of 9 mothers picked correctly. Use the probabilities to estimate the two-sided P-value.

- **Answer (tutor only):** ≈ 0.18
- **Explanation (tutor only):** Results at least as extreme as 2 in the low tail: P(0, 1, 2) = 0.002 + 0.018 + 0.07 = 0.09. Doubled for two sides: 0.18. Doing worse than chance counts as extreme in a two-sided test.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: using only P(2) = 0.07; forgetting to double (0.09); adding the upper tail from 2 upward.
- **Hint:** Which results are as far from 4.5 as 2 is, or farther?

### ch10-hw-05-v2
- **Kind:** AI-written version of ch10-hw-05
- **Concepts:** What a p-value means
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch10-var-null10.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch10-var-null10.png)
- **Question:**

Can dogs smell cancer? Each of 10 trained dogs sniffs two breath samples (one from a patient with cancer, one without) and picks one. Use a two-sided test with α = 0.05. The plot and table show the probability of each number of correct picks if dogs were just guessing:

correct | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10
probability | 0.001 | 0.010 | 0.044 | 0.117 | 0.205 | 0.246 | 0.205 | 0.117 | 0.044 | 0.010 | 0.001

Suppose 8 of 10 dogs pick correctly. Use the probabilities to estimate the two-sided P-value.

- **Answer (tutor only):** ≈ 0.11
- **Explanation (tutor only):** At least as extreme as 8: P(8, 9, 10) = 0.044 + 0.010 + 0.001 = 0.055. Doubled for two sides: 0.11 (exact: 0.109).
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: using only P(8) = 0.044; using one tail (0.055); including 7.
- **Hint:** Add the upper tail from 8, then double.

### ch10-hw-06
- **Kind:** Course original
- **Concepts:** What a p-value means
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch10-smell-null-dist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch10-smell-null-dist.png)
- **Question:**

Can parents identify their own children by smell? In Porter and Moore (1981), each of nine mothers was given her own child's worn T-shirt and one from another randomly chosen child, and asked to pick her own. Use a two-sided test with α = 0.05. The plot shows the probability of each number of correct guesses (0–9) if mothers were just guessing (the null distribution):

correct | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
probability | 0.002 | 0.018 | 0.07 | 0.164 | 0.246 | 0.246 | 0.164 | 0.07 | 0.018 | 0.002

With 7 of 9 correct, the two-sided P-value is about 0.18. What do we do with the null hypothesis, and what do we know about whether it's true?

- **Options:**

  A) Fail to reject it; we don't have enough information to say whether it's true or false
  B) Reject it; it is false
  C) Accept it; it is true
  D) Fail to reject it; it has an 18% chance of being true

- **Answer (tutor only):** A
- **Explanation (tutor only):** 0.18 > 0.05, so we fail to reject. That does not make the null true (we never 'accept' it): with only 9 mothers we have little power. And the p-value isn't the probability that the null is true.
- **Why the wrong options are wrong (tutor only):**
  B) p > α.
  C) Failing to reject ≠ accepting.
  D) The p-value is P(data | H0), not P(H0 | data).
- **Hint:** Compare p to α. Then: can a p-value tell you the probability the null is true?

### ch10-hw-06-v1
- **Kind:** AI-written version of ch10-hw-06
- **Concepts:** What a p-value means
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch10-var-null10.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch10-var-null10.png)
- **Question:**

Can dogs smell cancer? Each of 10 trained dogs sniffs two breath samples (one from a patient with cancer, one without) and picks one. Use a two-sided test with α = 0.05. The plot and table show the probability of each number of correct picks if dogs were just guessing:

correct | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10
probability | 0.001 | 0.010 | 0.044 | 0.117 | 0.205 | 0.246 | 0.205 | 0.117 | 0.044 | 0.010 | 0.001

With 8 of 10 correct, the two-sided P-value is about 0.11. What do we do with the null hypothesis, and what do we know?

- **Options:**

  A) Fail to reject it; the data don't establish whether dogs can smell cancer
  B) Reject it; dogs can smell cancer
  C) Accept it; dogs can't smell cancer
  D) Fail to reject it; there's an 11% chance dogs are guessing

- **Answer (tutor only):** A
- **Explanation (tutor only):** 0.11 > 0.05, so we fail to reject. With only 10 dogs the test has little power, so we can't conclude they're guessing either.
- **Why the wrong options are wrong (tutor only):**
  B) p > α.
  C) Failing to reject ≠ accepting.
  D) The p-value isn't P(H0 | data).
- **Hint:** Compare p with α, then ask what 'fail to reject' does and doesn't mean.

### ch10-hw-06-v2
- **Kind:** AI-written version of ch10-hw-06
- **Concepts:** What a p-value means; Errors, power & sample size
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch10-smell-null-dist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch10-smell-null-dist.png)
- **Question:**

Can parents identify their own children by smell? Each of nine mothers was given her own child's worn T-shirt and one from another child, and asked to pick her own. Use a two-sided test with α = 0.05. If mothers were just guessing, the probabilities of each number of correct picks are:

correct | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
probability | 0.002 | 0.018 | 0.07 | 0.164 | 0.246 | 0.246 | 0.164 | 0.07 | 0.018 | 0.002

Why is it hard to get a significant result with only nine mothers, even if mothers really can identify their child somewhat better than chance?

- **Options:**

  A) With so few trials, only extreme outcomes (8 or 9 correct, or 0 or 1) have p < 0.05, so the test has low power for modest abilities
  B) The null distribution is wrong
  C) Two-sided tests can never reject with n = 9
  D) Small samples always give biased results

- **Answer (tutor only):** A
- **Explanation (tutor only):** From the table, P(7 or more) × 2 = 0.18, so you'd need 8 or 9 correct to reject. A mother who's right 70% of the time would usually fall short.
- **Why the wrong options are wrong (tutor only):**
  B) The null distribution is correct for guessing.
  C) 8 or 9 correct would reject.
  D) Small samples are noisy, not necessarily biased.
- **Hint:** Which outcomes would give p < 0.05?

### ch10-hw-07
- **Kind:** Course original
- **Concepts:** What a p-value means
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

### ch10-hw-07-v1
- **Kind:** AI-written version of ch10-hw-07
- **Concepts:** What a p-value means
- **Type:** MC
- **Question:**

A DNA match has a 1-in-a-million chance of occurring for an innocent person. A prosecutor says: 'So there's only a 1-in-a-million chance the defendant is innocent.' What's wrong?

- **Options:**

  A) It confuses P(match | innocent) with P(innocent | match); in a city of millions, several innocent people could match
  B) DNA evidence is never reliable
  C) The chance should be 1 in 2 million
  D) Nothing; that's correct

- **Answer (tutor only):** A
- **Explanation (tutor only):** The probability of the evidence given innocence isn't the probability of innocence given the evidence. Same for p-values: P(data | H0) ≠ P(H0 | data).
- **Why the wrong options are wrong (tutor only):**
  B) The issue is the logic, not DNA.
  C) The number isn't the problem.
  D) This is the classic fallacy.
- **Hint:** Which way does the 'given' go?

### ch10-hw-07-v2
- **Kind:** AI-written version of ch10-hw-07
- **Concepts:** What a p-value means
- **Type:** MC
- **Question:**

Which statement commits the prosecutor's fallacy?

- **Options:**

  A) 'p = 0.02, so there's a 2% chance the null hypothesis is true'
  B) 'If the null were true, data this extreme would occur 2% of the time'
  C) 'p = 0.02 is below α = 0.05, so we reject the null'
  D) 'p = 0.02 doesn't tell us the effect size'

- **Answer (tutor only):** A
- **Explanation (tutor only):** It flips P(data | H0) into P(H0 | data).
- **Why the wrong options are wrong (tutor only):**
  B) That's the correct definition.
  C) A correct decision rule.
  D) True and not a fallacy.
- **Hint:** Find the one that makes the p-value a probability about the hypothesis.

## Chapter 11: Shuffling (permutation)

### ch11-book-01
- **Kind:** Course original
- **Concepts:** Bootstrap vs permutation
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

### ch11-book-01-v1
- **Kind:** AI-written version of ch11-book-01
- **Concepts:** Bootstrap vs permutation
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

### ch11-book-01-v2
- **Kind:** AI-written version of ch11-book-01
- **Concepts:** Bootstrap vs permutation
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

### ch11-book-02
- **Kind:** Course original
- **Concepts:** Bootstrap vs permutation
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-book-penguin-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-book-penguin-boot-perm.png)
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

### ch11-book-02-v1
- **Kind:** AI-written version of ch11-book-02
- **Concepts:** Bootstrap vs permutation
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-var-chin-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-var-chin-boot-perm.png)
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

### ch11-book-02-v2
- **Kind:** AI-written version of ch11-book-02
- **Concepts:** Bootstrap vs permutation
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-var-chin-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-var-chin-boot-perm.png)
- **Question:**

Chinstrap penguins (34 males, 34 females). Males' flippers are 8.2 mm longer on average. One plot shows 5000 bootstrap replicates of the male − female difference, and the other shows 5000 permutations (blue line = observed 8.2 mm).

Why is the permutation distribution centered at 0 while the bootstrap distribution is centered near 8.2 mm?

- **Options:**

  A) Shuffling sex labels removes any real sex difference; bootstrapping keeps each bird's sex, so the real difference remains
  B) Permutation uses fewer replicates
  C) The bootstrap removes sampling error
  D) It's a coincidence

- **Answer (tutor only):** A
- **Explanation (tutor only):** Permutation simulates the null (no difference); the bootstrap simulates sampling variation around our estimate.
- **Why the wrong options are wrong (tutor only):**
  B) Both use 5000.
  C) The bootstrap shows sampling error.
  D) It's by design.
- **Hint:** Which method keeps the association?

### ch11-book-03
- **Kind:** Course original
- **Concepts:** Bootstrap vs permutation
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-book-penguin-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-book-penguin-boot-perm.png)
- **Question:**

Adelie penguins from Torgersen island (23 males, 24 females). Males are 639 g heavier on average. One plot shows 5000 bootstrap replicates of the male − female difference, and the other shows 5000 permutations (blue line = observed 639 g).

1. Which plot is the permutation (null) distribution?
2. Which plot is the bootstrap distribution?

- **Options:**

  A) Distribution 1
  B) Distribution 2

- **Answer (tutor only):** 1-A, 2-B
- **Explanation (tutor only):** Distribution 1 is centered at 0 (the null), and the observed 639 g is far outside it, so it's the permutation. Distribution 2 is centered on the observed 639 g, so it's the bootstrap.
- **Why the wrong options are wrong (tutor only):**
  Look at the centers: the null value vs the estimate.
- **Hint:** Where is each one centered?

### ch11-book-03-v1
- **Kind:** AI-written version of ch11-book-03
- **Concepts:** Bootstrap vs permutation
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-var-chin-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-var-chin-boot-perm.png)
- **Question:**

Chinstrap penguins (34 males, 34 females). Males' flippers are 8.2 mm longer on average. One plot shows 5000 bootstrap replicates of the male − female difference, and the other shows 5000 permutations (blue line = observed 8.2 mm).

1. Which plot is the bootstrap distribution?
2. Which plot is the permutation (null) distribution?

- **Options:**

  A) Distribution 1
  B) Distribution 2

- **Answer (tutor only):** 1-A, 2-B
- **Explanation (tutor only):** Distribution 1 is centered on the observed 8.2 mm (bootstrap). Distribution 2 is centered at 0, with 8.2 far in the tail (permutation).
- **Why the wrong options are wrong (tutor only):**
  Look at the centers: the estimate vs the null value.
- **Hint:** Where is each centered?

### ch11-book-03-v2
- **Kind:** AI-written version of ch11-book-03
- **Concepts:** Bootstrap vs permutation
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-var-chin-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-var-chin-boot-perm.png)
- **Question:**

Chinstrap penguins (34 males, 34 females). Males' flippers are 8.2 mm longer on average. One plot shows 5000 bootstrap replicates of the male − female difference, and the other shows 5000 permutations (blue line = observed 8.2 mm).

What does the position of the blue line in Distribution 2 tell you?

- **Options:**

  A) The observed difference is far beyond anything shuffling produced, so p is very small
  B) The observed difference is typical under the null
  C) The CI includes 0
  D) The bootstrap failed

- **Answer (tutor only):** A
- **Explanation (tutor only):** The blue line (8.2 mm) lies well past the largest permuted difference (about 6.5 mm in absolute value).
- **Why the wrong options are wrong (tutor only):**
  B) It's way out in the tail.
  C) Distribution 2 isn't used for a CI.
  D) Distribution 2 is the permutation.
- **Hint:** Is 8.2 mm unusual for the null distribution?

### ch11-book-04
- **Kind:** Course original
- **Concepts:** Bootstrap vs permutation; Bootstrap CIs
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-book-penguin-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-book-penguin-boot-perm.png)
- **Question:**

Adelie penguins from Torgersen island (23 males, 24 females). Males are 639 g heavier on average. One plot shows 5000 bootstrap replicates of the male − female difference, and the other shows 5000 permutations (blue line = observed 639 g).

The 2.5th and 97.5th percentiles of the bootstrap distribution are about 458 and 817 g. What is the 95% CI for the sex difference, and how do you read it?

- **Options:**

  A) About 458 to 817 g: a range of plausible values for the true male − female difference
  B) About 458 to 817 g: 95% of individual males are in this range
  C) About −450 to 450 g, from the permutation distribution
  D) 639 ± 1.96 g

- **Answer (tutor only):** A
- **Explanation (tutor only):** The middle 95% of bootstrap estimates gives the CI: males are plausibly about 460–820 g heavier on average. (The book's answer for the lower bound is 455; random resampling gives slightly different values each run.)
- **Why the wrong options are wrong (tutor only):**
  B) The CI is about the mean difference, not individuals.
  C) The permutation distribution is centered on 0; it's for testing, not CIs.
  D) That uses the wrong spread.
- **Hint:** CI = middle 95% of which distribution?

### ch11-book-04-v1
- **Kind:** AI-written version of ch11-book-04
- **Concepts:** Bootstrap vs permutation; Bootstrap CIs
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-var-chin-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-var-chin-boot-perm.png)
- **Question:**

Chinstrap penguins (34 males, 34 females). Males' flippers are 8.2 mm longer on average. One plot shows 5000 bootstrap replicates of the male − female difference, and the other shows 5000 permutations (blue line = observed 8.2 mm).

The 2.5th and 97.5th percentiles of the bootstrap distribution are about 5.5 and 11.1 mm. What is the 95% CI, and how do you read it?

- **Options:**

  A) About 5.5 to 11.1 mm: a range of plausible values for the true male − female difference in mean flipper length
  B) About 5.5 to 11.1 mm: 95% of males have flippers in this range
  C) About −6 to 6 mm, from the permutation distribution
  D) 8.2 ± 1.96 mm

- **Answer (tutor only):** A
- **Explanation (tutor only):** The middle 95% of bootstrap differences gives the CI: males' flippers are plausibly about 5–11 mm longer on average.
- **Why the wrong options are wrong (tutor only):**
  B) The CI is about the mean difference, not individuals.
  C) The permutation distribution is for testing.
  D) Uses the wrong spread.
- **Hint:** Middle 95% of which distribution?

### ch11-book-04-v2
- **Kind:** AI-written version of ch11-book-04
- **Concepts:** Bootstrap vs permutation
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-var-chin-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-var-chin-boot-perm.png)
- **Question:**

Chinstrap penguins (34 males, 34 females). Males' flippers are 8.2 mm longer on average. One plot shows 5000 bootstrap replicates of the male − female difference, and the other shows 5000 permutations (blue line = observed 8.2 mm).

How would you get the standard error of the sex difference?

- **Options:**

  A) The standard deviation of the 5000 bootstrap differences
  B) The standard deviation of the 5000 permuted differences
  C) The mean of the bootstrap differences
  D) 8.2 / √5000

- **Answer (tutor only):** A
- **Explanation (tutor only):** The bootstrap distribution approximates the sampling distribution, so its SD is the SE.
- **Why the wrong options are wrong (tutor only):**
  B) The permutation SD describes the null world, not the uncertainty around our estimate.
  C) That's near the estimate itself.
  D) The number of replicates isn't the sample size.
- **Hint:** SE = spread of which distribution?

### ch11-book-05
- **Kind:** Course original
- **Concepts:** Permutation p-values
- **Type:** matching
- **Question:**

Adelie penguins from Torgersen island (23 males, 24 females). Males are 639 g heavier on average.

1. What is the null hypothesis?
2. What is the (two-tailed) alternative hypothesis?

- **Options:**

  A) Male Adelie penguins are heavier, on average, than females
  B) There is no difference in mean body mass between male and female Adelie penguins
  C) There is a difference in mean body mass between male and female Adelie penguins
  D) The observed difference in our sample is zero

- **Answer (tutor only):** 1-B, 2-C
- **Explanation (tutor only):** Hypotheses are about the population means, not the sample. Null: no difference. Two-tailed alternative: some difference.
- **Why the wrong options are wrong (tutor only):**
  A) One-tailed.
  D) Hypotheses are about the population, not our sample (whose difference is 639, not 0).
- **Hint:** Population or sample? Direction or no direction?

### ch11-book-05-v1
- **Kind:** AI-written version of ch11-book-05
- **Concepts:** Permutation p-values
- **Type:** matching
- **Question:**

Chinstrap penguins (34 males, 34 females). Males' flippers are 8.2 mm longer on average.

1. What is the null hypothesis?
2. What is the (two-tailed) alternative?

- **Options:**

  A) Male and female Chinstraps have the same mean flipper length
  B) Male and female Chinstraps differ in mean flipper length
  C) Male Chinstraps have longer flippers than females
  D) The sample difference is 0

- **Answer (tutor only):** 1-A, 2-B
- **Explanation (tutor only):** Hypotheses are about population means. Null: no difference. Two-tailed alternative: some difference.
- **Why the wrong options are wrong (tutor only):**
  C) One-tailed.
  D) Hypotheses are about the population; our sample difference is 8.2.
- **Hint:** Population, not sample; no direction for two-tailed.

### ch11-book-05-v2
- **Kind:** AI-written version of ch11-book-05
- **Concepts:** Permutation p-values
- **Type:** MC
- **Question:**

Adelie penguins on Torgersen: is bill length correlated with bill depth? Which is the null hypothesis?

- **Options:**

  A) In the population, the correlation between bill length and depth is 0
  B) In our sample, r = 0
  C) The correlation is positive
  D) Longer bills cause deeper bills

- **Answer (tutor only):** A
- **Explanation (tutor only):** The null is about the population: no association (ρ = 0).
- **Why the wrong options are wrong (tutor only):**
  B) Our sample r is 0.22; hypotheses are about the population.
  C) An alternative (one-tailed).
  D) A causal claim, and not a null.
- **Hint:** Null = no association in the population.

### ch11-book-06
- **Kind:** Course original
- **Concepts:** Bootstrap vs permutation; Permutation p-values
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-book-penguin-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-book-penguin-boot-perm.png)
- **Question:**

Adelie penguins from Torgersen island (23 males, 24 females). Males are 639 g heavier on average. One plot shows 5000 bootstrap replicates of the male − female difference, and the other shows 5000 permutations (blue line = observed 639 g).

In the permutation distribution, none of the 5000 permuted differences was as extreme as 639 g (the largest was about 450 g). How should you report the p-value, and what do you do with the null?

- **Options:**

  A) p < 3/5000 (about 0.0006); reject the null
  B) p = 0; the null is impossible
  C) p = 0; reject the null
  D) p > 0.05; fail to reject

- **Answer (tutor only):** A
- **Explanation (tutor only):** A true p-value is never exactly 0. Zero out of 5000 permutations means p is small but unknown; a common rule of thumb reports p < 3/reps. Either way, we reject the null.
- **Why the wrong options are wrong (tutor only):**
  B) and C) A simulated 0 just means we didn't run enough permutations to see such an extreme value.
  D) Nothing in the null distribution comes close.
- **Hint:** Can a p-value really be 0?

### ch11-book-06-v1
- **Kind:** AI-written version of ch11-book-06
- **Concepts:** Bootstrap vs permutation; Permutation p-values
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-var-chin-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-var-chin-boot-perm.png)
- **Question:**

Chinstrap penguins (34 males, 34 females). Males' flippers are 8.2 mm longer on average. One plot shows 5000 bootstrap replicates of the male − female difference, and the other shows 5000 permutations (blue line = observed 8.2 mm).

None of the 5000 permuted differences was as extreme as 8.2 mm (the largest in absolute value was about 6.5 mm). How should you report the p-value?

- **Options:**

  A) p < 3/5000 (about 0.0006); reject the null
  B) p = 0; the null is impossible
  C) p = 0; reject the null
  D) p ≈ 1; fail to reject

- **Answer (tutor only):** A
- **Explanation (tutor only):** Zero out of 5000 means p is very small but not exactly 0; report it as below a bound such as 3/reps.
- **Why the wrong options are wrong (tutor only):**
  B) and C) A true p-value is never 0; we just didn't run enough shuffles to see such an extreme value.
  D) Nothing in the null comes close.
- **Hint:** Can a p-value be exactly zero?

### ch11-book-06-v2
- **Kind:** AI-written version of ch11-book-06
- **Concepts:** Bootstrap vs permutation; Permutation p-values
- **Type:** MC
- **Question:**

A permutation test with 1000 shuffles finds 0 permuted statistics as extreme as the observed one. A classmate reports 'p = 0.000.' What's better?

- **Options:**

  A) Report p < 0.003 (3/1000), or run more permutations
  B) p = 0.000 is correct
  C) Report p = 1
  D) Report p = 0.05

- **Answer (tutor only):** A
- **Explanation (tutor only):** With 1000 shuffles you can't distinguish p = 0.0001 from p = 0.0005; report a bound.
- **Why the wrong options are wrong (tutor only):**
  B) p-values are never exactly 0.
  C) The result is extreme, not typical.
  D) There's no reason to use 0.05.
- **Hint:** What's the smallest p you can resolve with 1000 shuffles?

### ch11-chime-01
- **Kind:** Course original
- **Concepts:** Bootstrap vs permutation; Non-independence & blocking
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

### ch11-chime-01-v1
- **Kind:** AI-written version of ch11-chime-01
- **Concepts:** Bootstrap vs permutation; Non-independence & blocking
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

### ch11-chime-01-v2
- **Kind:** AI-written version of ch11-chime-01
- **Concepts:** Bootstrap vs permutation; Non-independence & blocking
- **Type:** MC
- **Question:**

A permutation test finds a significant difference in songbird size between two forests, but all birds were caught with nets that miss small birds in one forest only. What's the problem?

- **Options:**

  A) Biased sampling: the permutation test can't fix how the data were collected
  B) Not enough permutations
  C) Permutation tests require normal data
  D) No problem

- **Answer (tutor only):** A
- **Explanation (tutor only):** Permutation tests assume unbiased sampling. A difference created by the nets would look 'significant' too.
- **Why the wrong options are wrong (tutor only):**
  B) More shuffles won't remove bias.
  C) Permutation doesn't assume normality.
  D) The bias could explain the result.
- **Hint:** Can any test fix biased data?

### ch11-chime-02
- **Kind:** Course original
- **Concepts:** Bootstrap vs permutation
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

### ch11-chime-02-v1
- **Kind:** AI-written version of ch11-chime-02
- **Concepts:** Bootstrap vs permutation
- **Type:** MC
- **Question:**

What does each permuted replicate represent?

- **Options:**

  A) A dataset like ours in which any real association has been removed: what we might see if the null were true
  B) A new sample from the population
  C) A dataset with the outliers removed
  D) A resample with replacement

- **Answer (tutor only):** A
- **Explanation (tutor only):** Shuffling breaks the link between variables, so each replicate is one possible 'null world' version of our data.
- **Why the wrong options are wrong (tutor only):**
  B) No new data are collected.
  C) All values are kept.
  D) That's the bootstrap.
- **Hint:** What does shuffling destroy?

### ch11-chime-02-v2
- **Kind:** AI-written version of ch11-chime-02
- **Concepts:** Bootstrap vs permutation; Permutation p-values
- **Type:** MC
- **Question:**

After building a permutation null distribution, how is the p-value found?

- **Options:**

  A) The proportion of permuted statistics as or more extreme than the observed statistic
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

### ch11-chime-03
- **Kind:** Course original
- **Concepts:** Bootstrap vs permutation
- **Type:** matching
- **Question:**

The permutation and the bootstrap both use our data to approximate a sampling distribution.

1. The bootstrap aims to approximate the ____
2. Permutation aims to approximate the ____
3. In bootstrapping we ____ to ____
4. In permuting we ____ to ____

- **Options:**

  A) null sampling distribution
  B) sampling distribution that generated our data
  C) resample with replacement, to estimate uncertainty
  D) shuffle associations, to test a hypothesis

- **Answer (tutor only):** 1-B, 2-A, 3-C, 4-D
- **Explanation (tutor only):** Bootstrap: resample with replacement, approximate the sampling distribution around our estimate, and get an SE or CI. Permutation: shuffle to break the association, approximate the null distribution, and get a p-value.
- **Why the wrong options are wrong (tutor only):**
  Swapping them is the key confusion this question targets.
- **Hint:** Which one keeps the association, and which one breaks it?

### ch11-chime-03-v1
- **Kind:** AI-written version of ch11-chime-03
- **Concepts:** Bootstrap vs permutation
- **Type:** matching
- **Question:**

For each output, which method produces it?

1. A p-value
2. A 95% confidence interval
3. A standard error
4. A null distribution

- **Options:**

  A) Bootstrap
  B) Permutation

- **Answer (tutor only):** 1-B, 2-A, 3-A, 4-B
- **Explanation (tutor only):** The bootstrap estimates uncertainty (SE, CI); permutation simulates the null (null distribution, p-value).
- **Why the wrong options are wrong (tutor only):**
  Swapping them is the key confusion.
- **Hint:** Uncertainty vs testing.

### ch11-chime-03-v2
- **Kind:** AI-written version of ch11-chime-03
- **Concepts:** Bootstrap vs permutation
- **Type:** MC
- **Question:**

Where is each distribution centered?

- **Options:**

  A) Bootstrap: near the observed estimate; permutation: near the null value (e.g., 0)
  B) Both near 0
  C) Both near the observed estimate
  D) Bootstrap near 0; permutation near the estimate

- **Answer (tutor only):** A
- **Explanation (tutor only):** The bootstrap keeps the association, so it centers on our estimate. Permutation destroys it, so it centers on the null value.
- **Why the wrong options are wrong (tutor only):**
  B)–D) Mix up which method keeps the association.
- **Hint:** Which one keeps the association?

### ch11-chime-04
- **Kind:** Course original
- **Concepts:** Bootstrap vs permutation; Permutation p-values
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-chime-lineup.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-chime-lineup.png)
- **Question:**

Permutation eye-test: the plot shows 20 panels of 'whole animal resistance' for two localities (Benton vs Warrenton). One panel is the real data; the other 19 were made by shuffling the locality labels.

Which panel do you think is the real data?

- **Options:**

  A) 1
  B) 7
  C) 13
  D) 18
  E) 20

- **Answer (tutor only):** D
- **Explanation (tutor only):** Panel 18 stands out: nearly every Benton point is higher than every Warrenton point, with non-overlapping intervals. The shuffled panels mostly show small, random differences.
- **Why the wrong options are wrong (tutor only):**
  The other panels look like shuffled data: differences go in both directions and the intervals overlap.
  A), B), C) and E) In these panels the groups overlap, and the differences could easily come from shuffling.
- **Hint:** Which panel looks least like the others?

### ch11-chime-04-v1
- **Kind:** AI-written version of ch11-chime-04
- **Concepts:** Bootstrap vs permutation
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-var-lineup.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-var-lineup.png)
- **Question:**

Permutation eye-test: the plot shows 20 panels of Chinstrap penguin flipper length for females (F) and males (M), with means and 95% CIs. One panel is the real data; the other 19 were made by shuffling the sex labels.

Which panel do you think is the real data?

- **Options:**

  A) 2
  B) 6
  C) 13
  D) 20

- **Answer (tutor only):** B
- **Explanation (tutor only):** In panel 6 males are clearly longer-flippered, with non-overlapping intervals. Shuffled panels show small differences in either direction.
- **Why the wrong options are wrong (tutor only):**
  A), C) and D) These show small differences in either direction with overlapping intervals, as expected from shuffling.
- **Hint:** Which panel doesn't look like random shuffling?

### ch11-chime-04-v2
- **Kind:** AI-written version of ch11-chime-04
- **Concepts:** Bootstrap vs permutation
- **Type:** MC
- **Question:**

In a line-up of 20 panels (1 real, 19 shuffled), the real panel can't be distinguished from the shuffled ones. What does that suggest?

- **Options:**

  A) The real data look like what the null produces, so the p-value is probably not small and we likely wouldn't reject the null
  B) The real data show a strong effect
  C) The null is true
  D) The shuffling was done wrong

- **Answer (tutor only):** A
- **Explanation (tutor only):** If data look typical of shuffled data, chance alone can easily explain them. That's not proof the null is true, just no evidence against it.
- **Why the wrong options are wrong (tutor only):**
  B) A strong effect would stand out.
  C) Failing to find evidence isn't proof.
  D) This is what happens when there's little or no effect.
- **Hint:** What would a weak or absent effect look like?

### ch11-chime-05
- **Kind:** Course original
- **Concepts:** Bootstrap vs permutation; Permutation p-values; Bootstrap CIs
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-chime-lineup.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-chime-lineup.png)
- **Question:**

Permutation eye-test: the plot shows 20 panels of 'whole animal resistance' for two localities (Benton vs Warrenton). One panel is the real data; the other 19 were made by shuffling the locality labels.

Suppose you (and most of the class) could pick out the real data from the line-up of 20. Roughly what does that suggest about the p-value, and what does it mean?

- **Options:**

  A) p is about 1/20 = 0.05 or less: if the null were true, the real data would be just one more random-looking panel. We reject the null, meaning the null rarely generates data like ours
  B) p is about 0.95; we accept the null
  C) p is about 0.05, so the null is false
  D) We can't say anything about the p-value from a line-up

- **Answer (tutor only):** A
- **Explanation (tutor only):** If the null were true, the real panel would look like any shuffled panel, so you'd pick it only 1 time in 20 by luck. Picking it reliably means data like ours are rare under the null (p ≲ 0.05). That's evidence against the null, but it doesn't prove the null false.
- **Why the wrong options are wrong (tutor only):**
  B) Picking it out means it's unusual, not typical.
  C) Rejecting ≠ knowing the null is false.
  D) This is exactly the logic of a permutation test.
- **Hint:** If the null were true, what's the chance of picking the real panel by luck?

### ch11-chime-05-v1
- **Kind:** AI-written version of ch11-chime-05
- **Concepts:** Bootstrap vs permutation; Permutation p-values
- **Type:** MC
- **Question:**

In a line-up with 1 real panel and 99 shuffled panels, you correctly pick the real one. If the null were true, what's the chance of that by luck?

- **Options:**

  A) 1/100 = 0.01
  B) 1/20 = 0.05
  C) 99/100
  D) 0

- **Answer (tutor only):** A
- **Explanation (tutor only):** Under the null, the real panel is just one of 100 equally random-looking panels.
- **Why the wrong options are wrong (tutor only):**
  B) That's for 20 panels.
  C) That's the chance of picking wrong.
  D) A lucky guess is always possible.
- **Hint:** One in how many?

### ch11-chime-05-v2
- **Kind:** AI-written version of ch11-chime-05
- **Concepts:** Bootstrap vs permutation; Permutation p-values; Bootstrap CIs
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-var-lineup.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-var-lineup.png)
- **Question:**

Permutation eye-test: the plot shows 20 panels of Chinstrap penguin flipper length for females (F) and males (M), with means and 95% CIs. One panel is the real data; the other 19 were made by shuffling the sex labels.

If most of the class picks panel 6 correctly, what can we say?

- **Options:**

  A) Data like ours are rare under the null (p ≲ 0.05): evidence that flipper length differs by sex, though not proof
  B) The null is definitely false
  C) p ≈ 0.95
  D) Nothing; line-ups are just for fun

- **Answer (tutor only):** A
- **Explanation (tutor only):** Picking the real panel reliably means it doesn't look like a shuffled one: the logic of a permutation test.
- **Why the wrong options are wrong (tutor only):**
  B) Evidence isn't proof.
  C) Standing out means the data are unusual under the null.
  D) The line-up is a visual permutation test.
- **Hint:** If the null were true, how often would you pick it?

### ch11-hw-01
- **Kind:** Course original
- **Concepts:** Bootstrap vs permutation
- **Type:** matching
- **Question:**

In each permutation replicate, are these TRUE or FALSE?

1. The overall mean of the response variable is identical
2. The association between explanatory and response variables is kept constant
3. Some observations may be duplicated while others are omitted

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** 1-A, 2-B, 3-B
- **Explanation (tutor only):** Permutation shuffles labels (or one variable) relative to the other, using every observation exactly once. So the overall mean never changes, but the association is broken at random. Duplicating or omitting observations is what the bootstrap does.
- **Why the wrong options are wrong (tutor only):**
  2: Keeping the association would defeat the purpose; shuffling is meant to destroy it.
  3: That describes resampling with replacement (the bootstrap).
- **Hint:** Shuffling labels: does any number change, appear twice, or disappear?

### ch11-hw-01-v1
- **Kind:** AI-written version of ch11-hw-01
- **Concepts:** Bootstrap vs permutation
- **Type:** matching
- **Question:**

In each BOOTSTRAP replicate, are these TRUE or FALSE?

1. The overall mean of the response variable is identical to the original
2. Some observations may be duplicated while others are omitted
3. Each replicate has the same sample size as the original data

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** 1-B, 2-A, 3-A
- **Explanation (tutor only):** The bootstrap resamples with replacement at the original size, so some observations repeat, others drop out, and the overall mean changes from replicate to replicate.
- **Why the wrong options are wrong (tutor only):**
  1: A fixed overall mean is a feature of permutation, which reuses every observation exactly once.
- **Hint:** Resampling with replacement vs shuffling.

### ch11-hw-01-v2
- **Kind:** AI-written version of ch11-hw-01
- **Concepts:** Bootstrap vs permutation
- **Type:** MC
- **Question:**

In a permutation test of whether mean growth differs between two fertilizers, which stays the same in every permuted replicate?

- **Options:**

  A) The set of growth values (each used exactly once), so the overall mean is unchanged
  B) The mean of each fertilizer group
  C) The difference between group means
  D) Which plants get which fertilizer label

- **Answer (tutor only):** A
- **Explanation (tutor only):** Permutation only reshuffles labels; the same numbers appear in every replicate. Group means and their difference change because the labels move.
- **Why the wrong options are wrong (tutor only):**
  B) and C) These change as labels are shuffled; that variation forms the null distribution.
  D) That's exactly what gets shuffled.
- **Hint:** What does shuffling move, and what does it leave alone?

### ch11-hw-02
- **Kind:** Course original
- **Concepts:** Bootstrap vs permutation
- **Type:** select-all
- **Question:**

Select all true characteristics of bootstrapping:

- **Options:**

  A) Bootstrapping samples with replacement to mimic repeated sampling from the population
  B) Bootstrapping requires a clear null hypothesis

- **Answer (tutor only):** A
- **Explanation (tutor only):** The bootstrap resamples the data with replacement to approximate the sampling distribution and estimate uncertainty. It doesn't involve a null hypothesis; permutation does.
- **Why the wrong options are wrong (tutor only):**
  B) A null hypothesis is needed for permutation tests, not the bootstrap.
- **Hint:** Which method is for uncertainty, and which is for testing?

### ch11-hw-02-v1
- **Kind:** AI-written version of ch11-hw-02
- **Concepts:** Bootstrap vs permutation
- **Type:** select-all
- **Question:**

Select all true characteristics of permutation tests:

- **Options:**

  A) They shuffle labels (or one variable) to break any association
  B) They require a null hypothesis to simulate
  C) They resample with replacement
  D) They're mainly used to produce confidence intervals

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** Permutation simulates the null by breaking the association, producing a null distribution and a p-value.
- **Why the wrong options are wrong (tutor only):**
  C) That's the bootstrap.
  D) CIs come from the bootstrap; permutation gives p-values.
- **Hint:** Which method needs a null?

### ch11-hw-02-v2
- **Kind:** AI-written version of ch11-hw-02
- **Concepts:** Bootstrap vs permutation
- **Type:** MC
- **Question:**

What is the main goal of bootstrapping?

- **Options:**

  A) To estimate the uncertainty in an estimate (an SE or CI) by mimicking repeated sampling
  B) To test a null hypothesis by breaking associations
  C) To remove bias from a sample
  D) To increase the sample size

- **Answer (tutor only):** A
- **Explanation (tutor only):** The bootstrap approximates the sampling distribution, so its spread gives the SE and its percentiles a CI.
- **Why the wrong options are wrong (tutor only):**
  B) That's permutation.
  C) Bias in the sample stays in every resample.
  D) Resamples are the same size as the data.
- **Hint:** Uncertainty or hypothesis test?

### ch11-hw-03
- **Kind:** Course original
- **Concepts:** Bootstrap vs permutation
- **Type:** matching
- **Question:**

Fill in the blanks: (1) ____ takes individuals in our sample and breaks the connection between the explanatory and response variable to (2) ____.

- **Options:**

  A) Bootstrapping
  B) Permutation
  C) The sampling distribution
  D) approximate the sampling distribution for the association, by treating our sample as if it represented the population
  E) approximate the null sampling distribution for the association, by breaking the actual association between explanatory and response variables

- **Answer (tutor only):** 1-B, 2-E
- **Explanation (tutor only):** Shuffling one variable relative to the other destroys any real association, leaving only what chance would produce: the null distribution.
- **Why the wrong options are wrong (tutor only):**
  A) with D) describes the bootstrap, which keeps the association.
- **Hint:** Which method 'breaks the connection'?

### ch11-hw-03-v1
- **Kind:** AI-written version of ch11-hw-03
- **Concepts:** Bootstrap vs permutation
- **Type:** matching
- **Question:**

Fill in the blanks: (1) ____ resamples individuals from our sample with replacement to (2) ____.

- **Options:**

  A) Bootstrapping
  B) Permutation
  C) Random assignment
  D) approximate the sampling distribution of our estimate, treating our sample as if it were the population
  E) approximate the null distribution by breaking the association

- **Answer (tutor only):** 1-A, 2-D
- **Explanation (tutor only):** The bootstrap treats the sample as a stand-in population and resamples it to see how much estimates would vary.
- **Why the wrong options are wrong (tutor only):**
  B) with E) describes permutation.
- **Hint:** With replacement → which method?

### ch11-hw-03-v2
- **Kind:** AI-written version of ch11-hw-03
- **Concepts:** Bootstrap vs permutation
- **Type:** MC
- **Question:**

Why does shuffling the explanatory variable relative to the response produce a null distribution?

- **Options:**

  A) Shuffling destroys any real association, so the statistics from shuffled data show what chance alone produces when there's no association
  B) Shuffling removes sampling error
  C) Shuffling makes the data normal
  D) Shuffling increases the sample size

- **Answer (tutor only):** A
- **Explanation (tutor only):** After shuffling, any remaining pattern is coincidence. Repeating many times shows the range of statistics expected under 'no association'.
- **Why the wrong options are wrong (tutor only):**
  B) Sampling error remains; it's what the null distribution displays.
  C) Shuffling doesn't change the values' distribution.
  D) n stays the same.
- **Hint:** What's left after you break the association?

### ch11-hw-04
- **Kind:** Course original
- **Concepts:** Bootstrap CIs
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-hw-sr-scatter.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-hw-sr-scatter.png)
- **Question:**

Clarkia RILs planted at Sawmill Road (SR; n = 113 plants). We ask whether petal area is associated with the proportion of hybrid seed. The observed correlation is r = 0.24. Panel A shows 5000 bootstrap replicates of r (red dashed lines: 2.5th and 97.5th percentiles, about 0.08 and 0.39). Panel B shows 5000 permuted replicates of r (solid blue line: observed r; dotted line: −r).

Looking at the scatterplot (with best-fit line), it looks like:

- **Options:**

  A) Plants with larger petals make more hybrids
  B) Plants with larger petals make fewer hybrids
  C) There is no obvious association between petal area and proportion hybrid

- **Answer (tutor only):** A
- **Explanation (tutor only):** The line slopes upward: plants with larger petals tend to have a higher proportion of hybrid seed. It's a weak, noisy association (r = 0.24), but it is positive.
- **Why the wrong options are wrong (tutor only):**
  B) The slope is positive.
  C) It's weak, but the line clearly tilts up.
- **Hint:** Which way does the line tilt?

### ch11-hw-04-v1
- **Kind:** AI-written version of ch11-hw-04
- **Concepts:** Bootstrap CIs
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-var-torg-scatter.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-var-torg-scatter.png)
- **Question:**

Adelie penguins on Torgersen island (n = 47). Is bill length associated with bill depth? The observed correlation is r = 0.22. Panel A shows 5000 bootstrap replicates of r (red dashed lines: 2.5th and 97.5th percentiles, about −0.11 and 0.50). Panel B shows 5000 permuted replicates of r (solid blue line: observed r; dotted line: −r).

Looking at the scatterplot (with best-fit line), it looks like:

- **Options:**

  A) Penguins with longer bills tend to have slightly deeper bills, but the association is weak and noisy
  B) Penguins with longer bills have shallower bills
  C) A strong, tight positive association

- **Answer (tutor only):** A
- **Explanation (tutor only):** The line tilts gently upward, but the points scatter widely around it (r = 0.22).
- **Why the wrong options are wrong (tutor only):**
  B) The slope is positive.
  C) The points are far from the line.
- **Hint:** Direction from the line; strength from the scatter.

### ch11-hw-04-v2
- **Kind:** AI-written version of ch11-hw-04
- **Concepts:** Bootstrap CIs
- **Type:** MC
- **Question:**

Two scatterplots both have a positive best-fit line. In Plot 1 the points hug the line; in Plot 2 they scatter widely around it. Which is true?

- **Options:**

  A) Plot 1 has a stronger correlation (r closer to 1)
  B) Plot 2 has a stronger correlation
  C) Both have the same correlation because both lines slope up
  D) The steeper line always has the larger r

- **Answer (tutor only):** A
- **Explanation (tutor only):** Correlation measures how tightly points follow a line, not how steep it is.
- **Why the wrong options are wrong (tutor only):**
  B) Wide scatter means weaker correlation.
  C) Direction alone doesn't set strength.
  D) Slope and r are different things.
- **Hint:** r measures tightness.

### ch11-hw-05
- **Kind:** Course original
- **Concepts:** Bootstrap vs permutation; Bootstrap CIs
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-hw-sr-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-hw-sr-boot-perm.png)
- **Question:**

Clarkia RILs planted at Sawmill Road (SR; n = 113 plants). We ask whether petal area is associated with the proportion of hybrid seed. The observed correlation is r = 0.24. Panel A shows 5000 bootstrap replicates of r (red dashed lines: 2.5th and 97.5th percentiles, about 0.08 and 0.39). Panel B shows 5000 permuted replicates of r (solid blue line: observed r; dotted line: −r).

Using Panel A, which values are within the 95% confidence interval for the correlation? (Select all correct.)

- **Options:**

  A) 0.00
  B) 0.05
  C) 0.10
  D) 0.15
  E) 0.20
  F) 0.25

- **Answer (tutor only):** C, D, E, F
- **Explanation (tutor only):** The bootstrap 95% CI runs from the 2.5th to the 97.5th percentile, about 0.08 to 0.39. 0.10–0.25 are inside; 0 and 0.05 are below the lower bound.
- **Why the wrong options are wrong (tutor only):**
  A) and B) Both are below about 0.08.
- **Hint:** Read the red dashed lines.

### ch11-hw-05-v1
- **Kind:** AI-written version of ch11-hw-05
- **Concepts:** Bootstrap vs permutation; Bootstrap CIs
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-var-torg-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-var-torg-boot-perm.png)
- **Question:**

Adelie penguins on Torgersen island (n = 47). Is bill length associated with bill depth? The observed correlation is r = 0.22. Panel A shows 5000 bootstrap replicates of r (red dashed lines: 2.5th and 97.5th percentiles, about −0.11 and 0.50). Panel B shows 5000 permuted replicates of r (solid blue line: observed r; dotted line: −r).

Using Panel A, which values are within the 95% confidence interval for the correlation? (Select all correct.)

- **Options:**

  A) −0.20
  B) 0.00
  C) 0.20
  D) 0.40
  E) 0.60

- **Answer (tutor only):** B, C, D
- **Explanation (tutor only):** The bootstrap 95% CI runs from about −0.11 to 0.50, so 0, 0.20 and 0.40 are inside. Note that 0 is a plausible value.
- **Why the wrong options are wrong (tutor only):**
  A) Below −0.11.
  E) Above 0.50.
- **Hint:** Read off the dashed lines.

### ch11-hw-05-v2
- **Kind:** AI-written version of ch11-hw-05
- **Concepts:** Bootstrap vs permutation; Bootstrap CIs
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-var-torg-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-var-torg-boot-perm.png)
- **Question:**

Adelie penguins on Torgersen island (n = 47). Is bill length associated with bill depth? The observed correlation is r = 0.22. Panel A shows 5000 bootstrap replicates of r (red dashed lines: 2.5th and 97.5th percentiles, about −0.11 and 0.50). Panel B shows 5000 permuted replicates of r (solid blue line: observed r; dotted line: −r).

The 95% CI includes 0. What does that tell us?

- **Options:**

  A) No association is among the plausible values, so the data don't clearly establish a correlation (a test would not reject at α = 0.05)
  B) The correlation is exactly 0
  C) The correlation is definitely positive
  D) The bootstrap failed

- **Answer (tutor only):** A
- **Explanation (tutor only):** A CI that includes the null value matches a non-significant test. The interval also includes moderate positive values, so we can't say there's no association either.
- **Why the wrong options are wrong (tutor only):**
  B) 0 is plausible, but so are values up to 0.5.
  C) Negative values are also plausible.
  D) Wide intervals are normal with n = 47.
- **Hint:** Is the null value inside the CI?

### ch11-hw-06
- **Kind:** Course original
- **Concepts:** Bootstrap CIs
- **Type:** MC
- **Question:**

Clarkia RILs planted at Sawmill Road (SR; n = 113 plants). We ask whether petal area is associated with the proportion of hybrid seed. The observed correlation is r = 0.24. A bootstrap gave a 95% confidence interval for the correlation of about 0.08 to 0.39.

Which statement best describes the 95% confidence interval for the correlation?

- **Options:**

  A) There is a 95% probability that the true correlation falls inside this one interval
  B) The true correlation will definitely be inside this interval
  C) If we repeated this study many times and built a 95% CI each time, about 95% of those intervals would contain the true correlation

- **Answer (tutor only):** C
- **Explanation (tutor only):** The 95% describes the method's long-run success rate, not this particular interval.
- **Why the wrong options are wrong (tutor only):**
  A) This interval either contains the truth or doesn't.
  B) About 5% of intervals miss.
- **Hint:** Ring toss, not archery.

### ch11-hw-06-v1
- **Kind:** AI-written version of ch11-hw-06
- **Concepts:** Bootstrap CIs
- **Type:** MC
- **Question:**

Adelie penguins on Torgersen (n = 47): the correlation between bill length and bill depth is r = 0.22, with a bootstrap 95% CI of about −0.11 to 0.50. Which statement best describes this CI?

- **Options:**

  A) If we repeated this study many times and built a 95% CI each time, about 95% of those intervals would contain the true correlation
  B) There's a 95% probability the true correlation is between −0.11 and 0.50
  C) 95% of penguins have correlations in this range

- **Answer (tutor only):** A
- **Explanation (tutor only):** The 95% is the method's long-run success rate.
- **Why the wrong options are wrong (tutor only):**
  B) This interval either contains the truth or doesn't.
  C) Correlation describes the population, not individual birds.
- **Hint:** Where does the 95% live?

### ch11-hw-06-v2
- **Kind:** AI-written version of ch11-hw-06
- **Concepts:** Bootstrap CIs
- **Type:** MC
- **Question:**

Adelie penguins on Torgersen (n = 47): r = 0.22, 95% CI about −0.11 to 0.50. If we measured 470 Torgersen Adelies instead, what would most likely happen to the CI?

- **Options:**

  A) It would be narrower
  B) It would be wider
  C) It would stay the same width
  D) It would be guaranteed to exclude 0

- **Answer (tutor only):** A
- **Explanation (tutor only):** More data shrinks the SE, so the interval narrows. Whether it then excludes 0 depends on the true correlation.
- **Why the wrong options are wrong (tutor only):**
  B) More data means less uncertainty.
  C) Width depends on n.
  D) If the true r were near 0, it could still include 0.
- **Hint:** What does a bigger n do to uncertainty?

### ch11-hw-07
- **Kind:** Course original
- **Concepts:** Bootstrap vs permutation; Permutation p-values
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-hw-sr-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-hw-sr-boot-perm.png)
- **Question:**

Clarkia RILs planted at Sawmill Road (SR; n = 113 plants). We ask whether petal area is associated with the proportion of hybrid seed. The observed correlation is r = 0.24. Panel A shows 5000 bootstrap replicates of r (red dashed lines: 2.5th and 97.5th percentiles, about 0.08 and 0.39). Panel B shows 5000 permuted replicates of r (solid blue line: observed r; dotted line: −r).

Using Panel B: about 1% of permuted correlations are as or more extreme (in either direction) than the observed r = 0.24. What is the p-value, and what do we do with the null?

- **Options:**

  A) p ≈ 0.01; reject the null
  B) p ≈ 0.01; accept the alternative and know the null is false
  C) p ≈ 0.99; fail to reject the null
  D) p ≈ 0.01; the chance the null is true is 1%

- **Answer (tutor only):** A
- **Explanation (tutor only):** The two-sided p-value is the proportion of permuted r's at least as extreme as ±0.24, about 0.01 (52 of 5000). Since 0.01 < 0.05, we reject the null. We don't KNOW the null is false, and p isn't the probability the null is true.
- **Why the wrong options are wrong (tutor only):**
  B) Rejecting isn't proof.
  C) 0.99 is the proportion LESS extreme.
  D) That's the prosecutor's fallacy.
- **Hint:** Count what's beyond the blue lines, on both sides.

### ch11-hw-07-v1
- **Kind:** AI-written version of ch11-hw-07
- **Concepts:** Bootstrap vs permutation; Permutation p-values
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-var-torg-boot-perm.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-var-torg-boot-perm.png)
- **Question:**

Adelie penguins on Torgersen island (n = 47). Is bill length associated with bill depth? The observed correlation is r = 0.22. Panel A shows 5000 bootstrap replicates of r (red dashed lines: 2.5th and 97.5th percentiles, about −0.11 and 0.50). Panel B shows 5000 permuted replicates of r (solid blue line: observed r; dotted line: −r).

Using Panel B: about 14% of permuted correlations are as or more extreme (in either direction) than the observed r = 0.22. What's the p-value, and what do we do?

- **Options:**

  A) p ≈ 0.14; fail to reject the null (but this doesn't show there's no association)
  B) p ≈ 0.14; reject the null
  C) p ≈ 0.86; fail to reject
  D) p ≈ 0.14; there's a 14% chance there's no association

- **Answer (tutor only):** A
- **Explanation (tutor only):** The p-value is the proportion of permuted r's at least as extreme as ±0.22: about 0.14 > 0.05. We fail to reject, but the CI shows a moderate correlation is still plausible.
- **Why the wrong options are wrong (tutor only):**
  B) p > 0.05.
  C) 0.86 is the proportion less extreme.
  D) The prosecutor's fallacy.
- **Hint:** What fraction is beyond both blue lines?

### ch11-hw-07-v2
- **Kind:** AI-written version of ch11-hw-07
- **Concepts:** Bootstrap vs permutation; Permutation p-values
- **Type:** MC
- **Question:**

In a permutation test with 1000 shuffles, 37 permuted statistics are as or more extreme (in either direction) than the observed value. What's the approximate two-sided p-value?

- **Options:**

  A) 0.037
  B) 0.074
  C) 0.963
  D) 37

- **Answer (tutor only):** A
- **Explanation (tutor only):** Counting both directions already gives the two-sided count: 37/1000 = 0.037.
- **Why the wrong options are wrong (tutor only):**
  B) Don't double: 'either direction' already covers both tails.
  C) That's the proportion less extreme.
  D) That's a count, not a proportion.
- **Hint:** Proportion of shuffles at least as extreme.

### ch11-hw-08
- **Kind:** Course original
- **Concepts:** Bootstrap vs permutation; Non-independence & blocking
- **Type:** MC
- **Question:**

An agronomist wants to know whether soil type affects sunflower seedling growth. She plants seedlings in either 'clay' or 'sandy' soil in several garden beds (each bed has both soil types). Seedlings in the same bed share a microclimate, so they are not independent. How should she permute?

- **Options:**

  A) Shuffle all soil-type labels across all seedlings from all beds
  B) Shuffle all garden bed labels across all seedlings from all soil types
  C) Shuffle soil-type labels only among seedlings within each bed
  D) The data cannot be permuted because the design is blocked

- **Answer (tutor only):** C
- **Explanation (tutor only):** Shuffling within beds breaks the soil–growth link while keeping the bed structure intact, so the null distribution respects the non-independence.
- **Why the wrong options are wrong (tutor only):**
  A) Ignores beds: it mixes bed effects into the null.
  B) Bed isn't the treatment.
  D) Blocked designs can be permuted, just within blocks.
- **Hint:** What structure should the shuffle preserve?

### ch11-hw-08-v1
- **Kind:** AI-written version of ch11-hw-08
- **Concepts:** Bootstrap vs permutation; Non-independence & blocking
- **Type:** MC
- **Question:**

A researcher tests whether a caffeine pill changes reaction time. Each of 20 people is tested twice: once with caffeine and once with a placebo. How should she permute?

- **Options:**

  A) Within each person, randomly swap (or keep) the caffeine and placebo labels
  B) Shuffle all 40 labels across everyone
  C) Shuffle the people's IDs
  D) This design can't be permuted

- **Answer (tutor only):** A
- **Explanation (tutor only):** Measurements from the same person aren't independent. Shuffling labels within each person breaks the treatment link while keeping each person's pair together.
- **Why the wrong options are wrong (tutor only):**
  B) Ignores the pairing and mixes person-to-person differences into the null.
  C) Person isn't the treatment.
  D) Paired designs can be permuted within pairs.
- **Hint:** Keep the structure; shuffle only the treatment.

### ch11-hw-08-v2
- **Kind:** AI-written version of ch11-hw-08
- **Concepts:** Bootstrap vs permutation; Non-independence & blocking
- **Type:** MC
- **Question:**

Students measure leaf size on sun vs shade branches of 8 trees (several leaves per branch type per tree). Why is shuffling sun/shade labels across ALL leaves from all trees a problem?

- **Options:**

  A) Leaves on the same tree are not independent; shuffling across trees mixes tree-to-tree differences into the null and misrepresents the design
  B) There are too many leaves to shuffle
  C) Sun and shade labels can't be shuffled
  D) It isn't a problem

- **Answer (tutor only):** A
- **Explanation (tutor only):** Shuffle within each tree instead, so the null keeps the tree structure.
- **Why the wrong options are wrong (tutor only):**
  B) Number of leaves isn't the issue.
  C) They can, just within trees.
  D) Ignoring the trees violates independence.
- **Hint:** Which leaves are related to each other?

### ch11-new-01
- **Kind:** Course original
- **Concepts:** Bootstrap vs permutation; Permutation p-values; Bootstrap CIs
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch11-lineup-null.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch11-lineup-null.png)
- **Question:**

Permutation eye-test: the plot shows 20 panels of Adelie penguin body mass on Biscoe vs Dream islands, with means and 95% CIs. One panel is the real data; the other 19 were made by shuffling the island labels.

The real data are in panel 14. Most people can't pick it out, and many guess panel 13. What does that tell us?

- **Options:**

  A) The real difference looks like the differences shuffling alone produces, so the p-value is probably large and we'd fail to reject the null. That isn't proof that the islands' penguins weigh the same
  B) Penguins on the two islands have exactly the same mean body mass
  C) Panel 13 shows that there is a real difference between the islands
  D) The shuffling was done wrong, because the real data should always stand out

- **Answer (tutor only):** A
- **Explanation (tutor only):** If the real panel blends in with the shuffled ones, chance alone easily produces data like ours. Here the real difference is about 21 g, and a permutation test gives p ≈ 0.8. We fail to reject the null, but the data are also consistent with a small difference, so we can't conclude there is none.
- **Why the wrong options are wrong (tutor only):**
  B) Failing to reject the null isn't evidence that the means are exactly equal.
  C) Panel 13 is a shuffle. With 19 shuffles, one of them will look a bit different by chance alone.
  D) The real data stand out only when there is a strong association; with no real difference, they shouldn't.
- **Hint:** If island didn't matter, would the real panel look any different from a shuffled one?

### ch11-new-02
- **Kind:** Course original
- **Concepts:** Bootstrap vs permutation; Permutation p-values; Bootstrap CIs
- **Type:** matching
- **Question:**

In a line-up, 1 panel shows the real data and 19 show data with the labels shuffled. What does each outcome suggest?

1. Most people reliably pick out the real panel.
2. People can't tell the real panel from the shuffled ones.

- **Options:**

  A) Data like ours would be rare if the null were true (p ≲ 1/20 = 0.05): evidence against the null, though not proof it's false
  B) Data like ours are typical of what the null produces (p is probably large): no evidence against the null, though not proof it's true
  C) The null is definitely true
  D) The null is definitely false

- **Answer (tutor only):** 1-A, 2-B
- **Explanation (tutor only):** The shuffled panels show what data look like when the null is true. If the real panel stands out, data like ours rarely arise under the null (by luck you'd pick it only 1 time in 20), so we reject the null. If it blends in, chance can easily explain our data, so we fail to reject. Neither outcome proves the null true or false.
- **Why the wrong options are wrong (tutor only):**
  C) and D) A line-up, like any permutation test, gives evidence, not certainty.
- **Hint:** The shuffled panels show what the null produces. Does the real panel look like them?

## Chapter 12: Study design

### ch12-book-01
- **Kind:** Course original
- **Concepts:** Experiments vs observational studies
- **Type:** MC
- **Question:**

Random assignment describes the key feature of experimental design in which the experimenter:

- **Options:**

  A) Randomly assigns individuals in a study to a treatment
  B) Randomly assigns individuals to a study
  C) Gives participants random homework assignments to ensure they can appropriately complete the experiment

- **Answer (tutor only):** A
- **Explanation (tutor only):** Random assignment means treatments are assigned to study subjects at random, which balances confounders across groups on average.
- **Why the wrong options are wrong (tutor only):**
  B) That's random selection (random sampling): choosing who gets into the study. It helps generalization, not causal inference.
  C) 🙃
- **Hint:** Assigning a treatment vs choosing who is in the study.

### ch12-book-01-v1
- **Kind:** AI-written version of ch12-book-01
- **Concepts:** Validity
- **Type:** MC
- **Question:**

Random sampling (random selection) means the researcher:

- **Options:**

  A) Chooses which individuals from the population are included in the study at random
  B) Randomly assigns study individuals to treatments
  C) Randomly decides which variables to measure

- **Answer (tutor only):** A
- **Explanation (tutor only):** Random sampling is about who gets into the study; it helps results generalize to the population. Random assignment is about who gets which treatment.
- **Why the wrong options are wrong (tutor only):**
  B) That's random assignment.
  C) Not a design principle.
- **Hint:** Into the study, or into a treatment?

### ch12-book-01-v2
- **Kind:** AI-written version of ch12-book-01
- **Concepts:** Experiments vs observational studies
- **Type:** MC
- **Question:**

A study recruits volunteers from one university (not random sampling) but flips a coin to decide who gets a new study technique (random assignment). What can it support?

- **Options:**

  A) A causal claim about the technique for people like these volunteers, but generalizing to everyone is less certain
  B) Generalization to all people, but no causal claim
  C) Neither causation nor generalization
  D) Both, fully

- **Answer (tutor only):** A
- **Explanation (tutor only):** Random assignment supports causation (internal validity); random sampling supports generalization (external validity). Here only the first was done.
- **Why the wrong options are wrong (tutor only):**
  B) Backwards.
  C) The coin flip supports causal inference.
  D) The sample wasn't random.
- **Hint:** Which randomization was done, and what does it buy?

### ch12-book-02
- **Kind:** Course original
- **Concepts:** Experiments vs observational studies; The language of causation
- **Type:** MC
- **Question:**

In our RIL study, the correlation between petal area and proportion hybrid seed was r = 0.227, sometimes called an 'effect size.' Why is calling this an effect size misleading?

- **Options:**

  A) Because effect sizes below a certain threshold don't count as real effects
  B) Because we have shown an association, not an effect: nothing here shows that petal area causes hybrid seed
  C) Because effect sizes are measured as Cohen's d
  D) Because 0.227 is not a measure of size

- **Answer (tutor only):** B
- **Explanation (tutor only):** We measured an association (r = 0.227) in an observational study. 'Effect size' is common shorthand for r, but 'effect' implies that petal area causes the change in hybrid seed, which these data can't show.
- **Why the wrong options are wrong (tutor only):**
  A) There's no threshold for 'real.'
  C) Cohen's d is one effect size, not the only one.
  D) r does measure the strength of an association.
- **Hint:** Does an observational correlation show an effect?

### ch12-book-02-v1
- **Kind:** AI-written version of ch12-book-02
- **Concepts:** Experiments vs observational studies; The language of causation
- **Type:** MC
- **Question:**

A survey finds that people who drink more green tea have slightly lower blood pressure (difference in means = 3 mmHg). A report calls this 'the effect of green tea.' Why is that wording misleading?

- **Options:**

  A) In an observational study we've measured an association, not an effect; tea drinkers may differ in many other ways
  B) 3 mmHg is too small to be an effect
  C) Effects can only be measured as correlations
  D) It isn't misleading

- **Answer (tutor only):** A
- **Explanation (tutor only):** 'Effect' implies causation. Without random assignment, confounders (diet, exercise, income) could create the difference.
- **Why the wrong options are wrong (tutor only):**
  B) Size isn't the problem; causality is.
  C) Effects can be expressed many ways.
  D) The wording implies a causal claim the design can't support.
- **Hint:** Was green tea randomly assigned?

### ch12-book-02-v2
- **Kind:** AI-written version of ch12-book-02
- **Concepts:** Experiments vs observational studies; The language of causation
- **Type:** MC
- **Question:**

When is it most appropriate to call a difference in means an 'effect size'?

- **Options:**

  A) When the explanatory variable was randomly assigned in an experiment
  B) Whenever the p-value is below 0.05
  C) Whenever the difference is large
  D) Never

- **Answer (tutor only):** A
- **Explanation (tutor only):** Random assignment lets us attribute the difference to the treatment, so 'effect' is justified.
- **Why the wrong options are wrong (tutor only):**
  B) Significance doesn't establish causation.
  C) Big associations can still be confounded.
  D) It's fine for well-designed experiments.
- **Hint:** What design justifies a causal word?

### ch12-book-03
- **Kind:** Course original
- **Concepts:** The language of causation
- **Type:** MC
- **Question:**

What distinguishes a scientific model from a statistical model?

- **Options:**

  A) A scientific model describes how (we think) the world actually works; a statistical model is a mathematical description of patterns in data
  B) A statistical model is more accurate than a scientific model
  C) There's no real difference; the terms are interchangeable

- **Answer (tutor only):** A
- **Explanation (tutor only):** Scientific models are about mechanisms (e.g., pollinators prefer large petals). Statistical models describe patterns (e.g., hybrid seed increases linearly with petal area). Good studies connect the two.
- **Why the wrong options are wrong (tutor only):**
  B) They have different jobs, so 'more accurate' isn't the comparison.
  C) Conflating them is what leads to over-interpreting statistical patterns as mechanisms.
- **Hint:** Mechanism vs pattern.

### ch12-book-03-v1
- **Kind:** AI-written version of ch12-book-03
- **Concepts:** The language of causation
- **Type:** MC
- **Question:**

Which of these is a SCIENTIFIC model (rather than a statistical one)?

- **Options:**

  A) Birds with deeper beaks can crack harder seeds, so they survive droughts better
  B) Survival = 0.2 + 0.05 × beak depth + error
  C) Beak depth is normally distributed with mean 9.5 mm
  D) The correlation between beak depth and survival is 0.3

- **Answer (tutor only):** A
- **Explanation (tutor only):** A scientific model proposes a mechanism. B–D describe patterns in data mathematically.
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) These are statistical descriptions of data.
- **Hint:** Which one explains how the world works?

### ch12-book-03-v2
- **Kind:** AI-written version of ch12-book-03
- **Concepts:** The language of causation
- **Type:** MC
- **Question:**

A statistical model shows that hybrid seed increases with petal area. Why doesn't this alone confirm the scientific model 'pollinators prefer large petals'?

- **Options:**

  A) Other mechanisms (e.g., a gene affecting both petal size and mating) could produce the same pattern; the statistical pattern is consistent with the hypothesis but doesn't prove it
  B) Statistical models are always wrong
  C) Scientific models can't be tested
  D) It does confirm it

- **Answer (tutor only):** A
- **Explanation (tutor only):** Many scientific models can predict the same statistical pattern. Distinguishing them needs targeted tests (e.g., experiments with pollinators).
- **Why the wrong options are wrong (tutor only):**
  B) Statistical models are useful descriptions.
  C) They can be tested through their predictions.
  D) A pattern is consistent with, not proof of, a mechanism.
- **Hint:** Could another mechanism produce the same pattern?

### ch12-book-04
- **Kind:** Course original
- **Concepts:** Power & precision
- **Type:** MC
- **Question:**

In blocking, treatments are randomly assigned within 'blocks' (e.g., fields or schools) so that all treatments are represented in every block. In matching, pairs are made as similar as possible and the treatment is randomly applied to one member of each pair. What underlying problem are both techniques trying to solve?

- **Options:**

  A) Both aim to remove confounds
  B) Both improve how well results generalize to new populations
  C) Both remove the need for random assignment
  D) Both aim to increase power and precision by decreasing variability unrelated to the treatment

- **Answer (tutor only):** D
- **Explanation (tutor only):** Comparing within blocks or pairs removes background variation (field to field, person to person) from the comparison, so the treatment effect is estimated more precisely.
- **Why the wrong options are wrong (tutor only):**
  A) Close: random assignment already protects against confounding. Blocking and matching go further by balancing known sources of variation, which mainly buys precision.
  B) They don't change who the results apply to.
  C) Both still randomize within blocks or pairs.
- **Hint:** What does comparing within a field or pair remove from the noise?

### ch12-book-04-v1
- **Kind:** AI-written version of ch12-book-04
- **Concepts:** Power & precision
- **Type:** MC
- **Question:**

A researcher tests two fertilizers on 6 farms, applying both fertilizers to plots within every farm. What's the main benefit of this blocked design?

- **Options:**

  A) Comparing fertilizers within each farm removes farm-to-farm variation, so the fertilizer difference is estimated more precisely
  B) It eliminates the need for randomization
  C) It lets results generalize to all farms worldwide
  D) It removes sampling error

- **Answer (tutor only):** A
- **Explanation (tutor only):** Blocking means each comparison happens under similar conditions, reducing noise unrelated to the treatment.
- **Why the wrong options are wrong (tutor only):**
  B) Treatments are still randomized within farms.
  C) Generalization depends on which farms were sampled.
  D) It reduces noise but can't remove sampling error.
- **Hint:** What variation is taken out of the comparison?

### ch12-book-04-v2
- **Kind:** AI-written version of ch12-book-04
- **Concepts:** Power & precision
- **Type:** MC
- **Question:**

To test a new drug, researchers form pairs of patients matched on age and disease severity, then flip a coin to give the drug to one member of each pair. Why match?

- **Options:**

  A) Comparing similar patients reduces variability from age and severity, increasing precision and power
  B) Matching replaces random assignment
  C) Matching guarantees the drug works
  D) Matching increases the sample size

- **Answer (tutor only):** A
- **Explanation (tutor only):** Within-pair comparisons cancel out shared differences, so the drug effect stands out more clearly. Randomizing within pairs still protects against confounding.
- **Why the wrong options are wrong (tutor only):**
  B) The coin flip is still needed.
  C) Design can't guarantee a result.
  D) n is unchanged.
- **Hint:** What do matched pairs share?

### ch12-book-05
- **Kind:** Course original
- **Concepts:** Experiments vs observational studies
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

### ch12-book-05-v1
- **Kind:** AI-written version of ch12-book-05
- **Concepts:** Experiments vs observational studies
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

### ch12-book-05-v2
- **Kind:** AI-written version of ch12-book-05
- **Concepts:** Experiments vs observational studies
- **Type:** MC
- **Question:**

How does statistically adjusting for covariates (e.g., including age in a model) differ from random assignment?

- **Options:**

  A) Adjustment only handles the covariates you measured and modeled correctly; random assignment balances all of them by design
  B) They're the same thing
  C) Adjustment is always better than random assignment
  D) Random assignment only works for measured covariates

- **Answer (tutor only):** A
- **Explanation (tutor only):** Unmeasured confounders can still bias an adjusted observational analysis, but not a randomized experiment (on average).
- **Why the wrong options are wrong (tutor only):**
  B) One is design, the other is modeling.
  C) Adjustment can't fix unmeasured confounding.
  D) Backwards.
- **Hint:** What about confounders you never measured?

### ch12-book-06
- **Kind:** Course original
- **Concepts:** Power & precision; Validity
- **Type:** matching
- **Question:**

An experiment with appropriate controls fails to reject the null hypothesis. For each statement, is it a valid reason why a TRUE causal effect could still fail to reach significance?

1. The experiment's conditions were unnatural enough to block the causal pathway (e.g., testing a pollinator-attraction hypothesis with no pollinators present)
2. The treatment's intensity or dose differed enough from nature that it didn't trigger the same effect
3. The study was underpowered: too small a sample to reliably detect a real but modest effect
4. Failing to reject the null proves the null hypothesis is true

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** 1-A, 2-A, 3-A, 4-B
- **Explanation (tutor only):** Absence of evidence is not evidence of absence. A null result can come from the wrong context, the wrong dose, or too little power. None of these means the causal hypothesis is wrong.
- **Why the wrong options are wrong (tutor only):**
  4: We never 'accept' or prove the null.
- **Hint:** Could the effect be real but this study unable to see it?

### ch12-book-06-v1
- **Kind:** AI-written version of ch12-book-06
- **Concepts:** Power & precision; Validity
- **Type:** matching
- **Question:**

A greenhouse experiment tests whether a soil fungus increases plant growth, and fails to reject the null. Is each statement a valid reason a real effect could have been missed?

1. The greenhouse soil was so rich in nutrients that plants didn't need the fungus's help
2. Only 6 plants per group were used
3. The fungus was added at a much lower density than occurs in nature
4. The non-significant result shows the fungus has no effect

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** 1-A, 2-A, 3-A, 4-B
- **Explanation (tutor only):** Unnatural conditions, low power and an unrealistic dose can all hide a real effect. A non-significant result doesn't prove no effect.
- **Why the wrong options are wrong (tutor only):**
  4: Failing to reject is not evidence of no effect.
- **Hint:** Absence of evidence ≠ evidence of absence.

### ch12-book-06-v2
- **Kind:** AI-written version of ch12-book-06
- **Concepts:** Power & precision
- **Type:** MC
- **Question:**

A small experiment (n = 8 per group) finds a non-significant effect of a training program, with a 95% CI for the improvement of −2 to +15 points. What's the best conclusion?

- **Options:**

  A) The study is inconclusive: effects from slightly negative to large are consistent with the data; a larger study is needed
  B) The training program doesn't work
  C) The training program clearly works
  D) The CI proves no effect

- **Answer (tutor only):** A
- **Explanation (tutor only):** The CI includes 0 but also big improvements. The study lacked precision to tell.
- **Why the wrong options are wrong (tutor only):**
  B) Non-significant ≠ no effect.
  C) The CI includes 0.
  D) A CI including 0 doesn't prove 0.
- **Hint:** Look at the whole CI, not just whether it includes 0.

### ch12-book-07
- **Kind:** Course original
- **Concepts:** Experiments vs observational studies; Validity
- **Type:** MC
- **Question:**

Glyphosate is the active ingredient in Roundup, a common herbicide. In 2015 the International Agency for Research on Cancer classified it as 'probably carcinogenic to humans,' while the U.S. EPA maintains it's unlikely to cause cancer when used as directed. Bayer (which acquired Roundup's maker, Monsanto) has faced more than 100,000 lawsuits from people who developed non-Hodgkin lymphoma after using it, including a school groundskeeper and a man who sprayed it on his own property for 20 years, and has paid more than $10 billion in settlements while denying that glyphosate causes cancer.

Agricultural workers exposed to glyphosate were often exposed to several other pesticides too. Why is this a threat to INTERNAL validity?

- **Options:**

  A) Because farmers are a small, unrepresentative slice of the population
  B) Because it's unclear whether glyphosate itself, the other pesticides, or some combination is responsible for the elevated cancer rate
  C) Because self-reported pesticide use is not a reliable measurement
  D) Because the sample size of farmers studied was too small to trust

- **Answer (tutor only):** B
- **Explanation (tutor only):** Co-exposure is a classic confound: glyphosate use and other pesticide use go together, so the study can't isolate glyphosate as the cause.
- **Why the wrong options are wrong (tutor only):**
  A) That's about external validity (generalizing).
  C) That's measurement validity.
  D) That's about precision and power.
- **Hint:** Internal validity: can we trust the causal conclusion within this study?

### ch12-book-07-v1
- **Kind:** AI-written version of ch12-book-07
- **Concepts:** Experiments vs observational studies; Validity
- **Type:** MC
- **Question:**

Hypothetical scenario: 'Weedex' is a lawn herbicide. Studies of professional landscapers, who spray it daily for years, find somewhat higher rates of a rare kidney disease than in other workers. Thousands of homeowners who used Weedex occasionally have since filed complaints with a consumer agency.

Landscapers who spray Weedex also handle fuels, fertilizers and other pesticides. Why is this a threat to INTERNAL validity?

- **Options:**

  A) It's unclear whether Weedex, the other chemicals, or a combination is responsible for the higher disease rate
  B) Landscapers aren't representative of homeowners
  C) Disease diagnoses might be inaccurate
  D) The sample is too small

- **Answer (tutor only):** A
- **Explanation (tutor only):** Co-exposure confounds the comparison: Weedex use travels with other exposures, so we can't isolate its role.
- **Why the wrong options are wrong (tutor only):**
  B) That's external validity.
  C) That's measurement.
  D) That's precision/power.
- **Hint:** Internal validity = can we attribute the cause?

### ch12-book-07-v2
- **Kind:** AI-written version of ch12-book-07
- **Concepts:** Experiments vs observational studies; Validity
- **Type:** MC
- **Question:**

An observational study finds that people who own dogs have lower rates of heart disease. Which is the clearest threat to INTERNAL validity?

- **Options:**

  A) Healthier, more active people may be more likely to get dogs in the first place
  B) The study only included people from one country
  C) Heart disease is rare
  D) Some owners had cats too

- **Answer (tutor only):** A
- **Explanation (tutor only):** If fitness affects both dog ownership and heart disease, it confounds the association (or the causation runs in reverse).
- **Why the wrong options are wrong (tutor only):**
  B) That's about generalization (external validity).
  C) Rarity affects power.
  D) Not the main confound.
- **Hint:** Could something cause both dog ownership and heart health?

### ch12-book-08
- **Kind:** Course original
- **Concepts:** Validity
- **Type:** MC
- **Question:**

Glyphosate is the active ingredient in Roundup, a common herbicide. In 2015 the International Agency for Research on Cancer classified it as 'probably carcinogenic to humans,' while the U.S. EPA maintains it's unlikely to cause cancer when used as directed. Bayer (which acquired Roundup's maker, Monsanto) has faced more than 100,000 lawsuits from people who developed non-Hodgkin lymphoma after using it, including a school groundskeeper and a man who sprayed it on his own property for 20 years, and has paid more than $10 billion in settlements while denying that glyphosate causes cancer.

The strongest evidence linking glyphosate to cancer comes from licensed agricultural applicators with heavy, often decades-long exposure. But many plaintiffs had residential exposure. Why does this gap raise a question of EXTERNAL validity?

- **Options:**

  A) Because home gardeners weren't randomly assigned to use Roundup
  B) Because occupational and residential users measure their exposure differently
  C) Because it's unclear whether a result from decades of heavy occupational exposure generalizes to occasional home use
  D) Because agricultural applicators are a larger sample than home gardeners

- **Answer (tutor only):** C
- **Explanation (tutor only):** External validity asks whether results from one population or setting apply to another, here from heavy occupational exposure to occasional home use.
- **Why the wrong options are wrong (tutor only):**
  A) That's about causal inference (internal validity).
  B) That's measurement.
  D) Sample size affects precision, not generalization.
- **Hint:** External = does it generalize?

### ch12-book-08-v1
- **Kind:** AI-written version of ch12-book-08
- **Concepts:** Validity
- **Type:** MC
- **Question:**

Hypothetical scenario: 'Weedex' is a lawn herbicide. Studies of professional landscapers, who spray it daily for years, find somewhat higher rates of a rare kidney disease than in other workers. Thousands of homeowners who used Weedex occasionally have since filed complaints with a consumer agency.

The evidence comes from landscapers with heavy daily exposure, but most complaints come from occasional home users. Why does this raise a question of EXTERNAL validity?

- **Options:**

  A) It's unclear whether results from years of heavy professional exposure apply to occasional home use
  B) Homeowners weren't randomly assigned to use Weedex
  C) Homeowners may misremember how much they used
  D) Landscapers are a larger group

- **Answer (tutor only):** A
- **Explanation (tutor only):** External validity asks whether findings from one group or setting generalize to another.
- **Why the wrong options are wrong (tutor only):**
  B) That's about causal inference.
  C) That's measurement.
  D) Size affects precision, not generalization.
- **Hint:** Do results transfer from one population to another?

### ch12-book-08-v2
- **Kind:** AI-written version of ch12-book-08
- **Concepts:** Validity
- **Type:** MC
- **Question:**

A drug is tested in a randomized trial of adults aged 30–50. A doctor wants to prescribe it to 85-year-olds. What's the concern?

- **Options:**

  A) External validity: the trial's results may not generalize to much older patients
  B) Internal validity: the trial couldn't show causation
  C) The trial had no control group
  D) No concern

- **Answer (tutor only):** A
- **Explanation (tutor only):** Randomization gives internal validity for the trial population, but older patients may respond differently.
- **Why the wrong options are wrong (tutor only):**
  B) Randomization supports causation within the trial.
  C) Not stated.
  D) Age could change how the drug works.
- **Hint:** Does the trial population match the patient?

### ch12-book-09
- **Kind:** Course original
- **Concepts:** Validity
- **Type:** MC
- **Question:**

Glyphosate is the active ingredient in Roundup, a common herbicide. In 2015 the International Agency for Research on Cancer classified it as 'probably carcinogenic to humans,' while the U.S. EPA maintains it's unlikely to cause cancer when used as directed. Bayer (which acquired Roundup's maker, Monsanto) has faced more than 100,000 lawsuits from people who developed non-Hodgkin lymphoma after using it, including a school groundskeeper and a man who sprayed it on his own property for 20 years, and has paid more than $10 billion in settlements while denying that glyphosate causes cancer.

Some animal evidence came from rodent studies using doses far above typical human exposure (the standard 'maximum tolerated dose'). Why does this raise a question of ECOLOGICAL validity?

- **Options:**

  A) Because rodents and humans metabolize chemicals too differently for animal studies to ever be useful
  B) Because a real effect at an extreme, rarely encountered dose doesn't necessarily tell you what happens at the doses people actually encounter
  C) Because the rodents weren't randomly assigned to dose groups
  D) Because tumor rates in animals can't be measured reliably

- **Answer (tutor only):** B
- **Explanation (tutor only):** High-dose testing isn't a flaw in itself: it's often the only practical way to detect a rare effect with a manageable number of animals. But it leaves a gap between the lab conditions and real-world exposure.
- **Why the wrong options are wrong (tutor only):**
  A) Too strong: animal studies are often informative.
  C) There's no indication they weren't randomized.
  D) Not the issue raised.
- **Hint:** Ecological validity: do the study conditions match real life?

### ch12-book-09-v1
- **Kind:** AI-written version of ch12-book-09
- **Concepts:** Validity
- **Type:** MC
- **Question:**

Hypothetical scenario: 'Weedex' is a lawn herbicide. Studies of professional landscapers, who spray it daily for years, find somewhat higher rates of a rare kidney disease than in other workers. Thousands of homeowners who used Weedex occasionally have since filed complaints with a consumer agency.

In lab studies, rats were fed Weedex at 500 times the dose a landscaper would absorb. Some developed kidney damage. Why does this raise a question of ECOLOGICAL validity?

- **Options:**

  A) An effect at an extreme dose doesn't necessarily tell you what happens at realistic exposures
  B) Rats can never tell us anything about humans
  C) The rats weren't randomly assigned
  D) Kidney damage can't be measured in rats

- **Answer (tutor only):** A
- **Explanation (tutor only):** High doses help detect rare effects with few animals, but there's a gap between those conditions and real-world exposure.
- **Why the wrong options are wrong (tutor only):**
  B) Too strong.
  C) Not indicated.
  D) Not the issue.
- **Hint:** Lab conditions vs real-world conditions.

### ch12-book-09-v2
- **Kind:** AI-written version of ch12-book-09
- **Concepts:** Validity
- **Type:** MC
- **Question:**

A study finds that a fish species avoids predators in small aquarium tanks with constant bright light. What's the main ecological validity concern?

- **Options:**

  A) Fish behavior in small, brightly lit tanks may differ from behavior in natural rivers
  B) The fish weren't randomly sampled from the river
  C) The study had too few fish
  D) Fish can't be studied experimentally

- **Answer (tutor only):** A
- **Explanation (tutor only):** Ecological validity asks whether the experimental conditions resemble the natural situation of interest.
- **Why the wrong options are wrong (tutor only):**
  B) That's external validity / sampling.
  C) That's power.
  D) They can.
- **Hint:** Do the lab conditions resemble nature?

### ch12-book-10
- **Kind:** Course original
- **Concepts:** Validity
- **Type:** matching
- **Question:**

Glyphosate is the active ingredient in Roundup, a common herbicide. In 2015 the International Agency for Research on Cancer classified it as 'probably carcinogenic to humans,' while the U.S. EPA maintains it's unlikely to cause cancer when used as directed. Bayer (which acquired Roundup's maker, Monsanto) has faced more than 100,000 lawsuits from people who developed non-Hodgkin lymphoma after using it, including a school groundskeeper and a man who sprayed it on his own property for 20 years, and has paid more than $10 billion in settlements while denying that glyphosate causes cancer.

About 170,000 Roundup-related lawsuits have been filed. Is each statement a legitimate reason this count is an untrustworthy estimate of how many people glyphosate has actually harmed?

1. It could overstate true harm: filing a lawsuit doesn't require proving glyphosate caused that person's cancer
2. It could understate true harm: highly exposed groups, such as undocumented agricultural workers, are unlikely to sue, for reasons unrelated to whether they were harmed
3. 170,000 is simply too large a number to be accurate
4. Bayer has settled most claims, so the true number of harmed people must be lower

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** 1-A, 2-A, 3-B, 4-B
- **Explanation (tutor only):** Lawsuits are a biased sample of harm: who sues depends on access, legal status and incentives, not only on whether someone was harmed. The bias can go in both directions.
- **Why the wrong options are wrong (tutor only):**
  3: Large numbers aren't inherently inaccurate.
  4: Settling says nothing about how many people were harmed.
- **Hint:** What determines whether a harmed person shows up in this count?

### ch12-book-10-v1
- **Kind:** AI-written version of ch12-book-10
- **Concepts:** Validity
- **Type:** matching
- **Question:**

Hypothetical scenario: 'Weedex' is a lawn herbicide. Studies of professional landscapers, who spray it daily for years, find somewhat higher rates of a rare kidney disease than in other workers. Thousands of homeowners who used Weedex occasionally have since filed complaints with a consumer agency.

Is each a legitimate reason the number of consumer complaints is an untrustworthy estimate of how many people Weedex harmed?

1. People with kidney disease for other reasons might blame Weedex and complain anyway
2. Many harmed people may never have heard of the complaint process
3. The complaint count is a round number
4. A lot of complaints means Weedex must be harmful

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** 1-A, 2-A, 3-B, 4-B
- **Explanation (tutor only):** Complaints are a self-selected, biased sample: they can overstate harm (blaming the product without evidence) or understate it (harmed people who never complain).
- **Why the wrong options are wrong (tutor only):**
  3: Roundness says nothing about accuracy.
  4: Complaint counts reflect awareness and incentives, not just harm.
- **Hint:** Who complains, and why?

### ch12-book-10-v2
- **Kind:** AI-written version of ch12-book-10
- **Concepts:** Validity
- **Type:** MC
- **Question:**

A restaurant estimates customer satisfaction from online reviews. Why might this be biased?

- **Options:**

  A) People with very good or very bad experiences are more likely to write reviews, so reviewers aren't representative
  B) Online reviews have too much sampling error
  C) Reviews are always fake
  D) There's no bias with many reviews

- **Answer (tutor only):** A
- **Explanation (tutor only):** Self-selected samples overrepresent strong opinions. More reviews don't fix the bias.
- **Why the wrong options are wrong (tutor only):**
  B) The main problem is bias, not chance.
  C) Too strong.
  D) Bias doesn't shrink with n.
- **Hint:** Who chooses to write a review?

### ch12-book-11
- **Kind:** Course original
- **Concepts:** Experiments vs observational studies
- **Type:** MC
- **Question:**

Glyphosate is the active ingredient in Roundup, a common herbicide. In 2015 the International Agency for Research on Cancer classified it as 'probably carcinogenic to humans,' while the U.S. EPA maintains it's unlikely to cause cancer when used as directed. Bayer (which acquired Roundup's maker, Monsanto) has faced more than 100,000 lawsuits from people who developed non-Hodgkin lymphoma after using it, including a school groundskeeper and a man who sprayed it on his own property for 20 years, and has paid more than $10 billion in settlements while denying that glyphosate causes cancer.

In 2023, Bayer began phasing glyphosate out of U.S. residential lawn-and-garden products, while continuing to sell it for agriculture. If glyphosate exposure really does drive non-Hodgkin lymphoma risk at levels common in residential use, what would you predict?

- **Options:**

  A) Non-Hodgkin lymphoma rates would drop substantially among residential users, but not change much among agricultural workers over the same period
  B) Rates should drop equally in both groups
  C) Rates should rise among agricultural workers, since they now use more glyphosate to compensate
  D) No prediction is safe

- **Answer (tutor only):** A
- **Explanation (tutor only):** Exposure changed for one group but not the other, for reasons unrelated to cancer risk. If glyphosate causes harm, the exposed-then-unexposed group should improve more. An equal drop in both groups would point to something else. (This compare-the-change design is called difference-in-differences.)
- **Why the wrong options are wrong (tutor only):**
  B) An equal drop would suggest a cause other than glyphosate.
  C) Not implied by the scenario.
  D) The whole point is that this makes a distinguishing, checkable prediction.
- **Hint:** Which group's exposure changed?

### ch12-book-11-v1
- **Kind:** AI-written version of ch12-book-11
- **Concepts:** Experiments vs observational studies
- **Type:** MC
- **Question:**

Hypothetical scenario: 'Weedex' is a lawn herbicide. Studies of professional landscapers, who spray it daily for years, find somewhat higher rates of a rare kidney disease than in other workers. Thousands of homeowners who used Weedex occasionally have since filed complaints with a consumer agency.

Suppose one state bans Weedex for home use while a neighboring state doesn't, and landscapers keep using it in both. If home use of Weedex causes kidney disease, what would you predict?

- **Options:**

  A) Disease among homeowners should drop more in the banning state than in the neighboring state
  B) Disease should drop equally in both states
  C) Disease should rise among landscapers in the banning state
  D) No prediction is possible

- **Answer (tutor only):** A
- **Explanation (tutor only):** This natural experiment changes exposure in one group but not a comparable one. A larger drop where the ban applies supports a causal role; equal drops suggest something else.
- **Why the wrong options are wrong (tutor only):**
  B) Equal drops would point to another cause.
  C) Landscapers' exposure didn't change.
  D) The comparison makes a clear prediction.
- **Hint:** Compare the change where exposure changed with where it didn't.

### ch12-book-11-v2
- **Kind:** AI-written version of ch12-book-11
- **Concepts:** Experiments vs observational studies
- **Type:** MC
- **Question:**

A city adds bike lanes on half its streets (chosen by a construction schedule unrelated to accident rates). Bike accidents drop 30% on those streets and 5% on the others. What's the best interpretation?

- **Options:**

  A) The extra drop on bike-lane streets is evidence the lanes reduced accidents, since the other streets account for city-wide trends
  B) The 30% drop proves bike lanes work, regardless of the other streets
  C) Since accidents dropped everywhere, the lanes did nothing
  D) No conclusion is possible without randomization

- **Answer (tutor only):** A
- **Explanation (tutor only):** The untreated streets serve as a comparison for background trends. The difference in changes (about 25 points) is the best estimate of the lanes' effect.
- **Why the wrong options are wrong (tutor only):**
  B) Ignores the 5% background drop.
  C) The drop was much bigger on lane streets.
  D) Natural experiments can support causal inference when assignment is unrelated to the outcome.
- **Hint:** Compare the changes, not just one change.

### ch12-hw-01
- **Kind:** Course original
- **Concepts:** Experiments vs observational studies
- **Type:** MC
- **Question:**

The best way to infer causation is:

- **Options:**

  A) An appropriately designed experiment
  B) A good observational study
  C) We can never infer causation

- **Answer (tutor only):** A
- **Explanation (tutor only):** Random assignment breaks the link between treatment and confounders, so a difference between groups can be attributed to the treatment (plus sampling error).
- **Why the wrong options are wrong (tutor only):**
  B) Observational studies can suggest causes, but confounding is always possible.
  C) Too pessimistic: well-designed experiments support causal claims.
- **Hint:** What does random assignment do to confounders?

### ch12-hw-01-v1
- **Kind:** AI-written version of ch12-hw-01
- **Concepts:** Experiments vs observational studies
- **Type:** MC
- **Question:**

Why is a randomized experiment better than an observational study for inferring causation?

- **Options:**

  A) Random assignment makes treatment groups alike on average in everything except the treatment, so differences can be attributed to it (plus chance)
  B) Experiments have larger sample sizes
  C) Experiments never have sampling error
  D) Observational studies can't detect associations

- **Answer (tutor only):** A
- **Explanation (tutor only):** Random assignment breaks links between treatment and confounders.
- **Why the wrong options are wrong (tutor only):**
  B) Not necessarily.
  C) Sampling error is always present.
  D) They detect associations fine; they struggle with causation.
- **Hint:** What does random assignment balance?

### ch12-hw-01-v2
- **Kind:** AI-written version of ch12-hw-01
- **Concepts:** Experiments vs observational studies
- **Type:** MC
- **Question:**

When might researchers rely on observational studies to investigate causes?

- **Options:**

  A) When an experiment would be unethical or impossible (e.g., assigning people to smoke)
  B) When they want stronger causal evidence than an experiment provides
  C) Never
  D) Only when sample sizes are small

- **Answer (tutor only):** A
- **Explanation (tutor only):** Observational studies are essential when we can't manipulate the cause. Careful designs and multiple lines of evidence can still build a causal case.
- **Why the wrong options are wrong (tutor only):**
  B) Experiments give stronger causal evidence.
  C) Much important science is observational.
  D) Sample size isn't the reason.
- **Hint:** When can't you randomly assign a treatment?

### ch12-hw-02
- **Kind:** Course original
- **Concepts:** Experiments vs observational studies
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

### ch12-hw-02-v1
- **Kind:** AI-written version of ch12-hw-02
- **Concepts:** Experiments vs observational studies
- **Type:** MC
- **Question:**

In an observational study, people who sleep more report less anxiety. Which explanation is reverse causation?

- **Options:**

  A) Less anxious people find it easier to sleep
  B) More sleep reduces anxiety
  C) A third factor (e.g., stress at work) affects both
  D) The association is a chance result

- **Answer (tutor only):** A
- **Explanation (tutor only):** Reverse causation: the response is actually causing the explanatory variable.
- **Why the wrong options are wrong (tutor only):**
  B) That's the forward causal story.
  C) That's confounding.
  D) That's sampling error.
- **Hint:** Flip the arrow.

### ch12-hw-02-v2
- **Kind:** AI-written version of ch12-hw-02
- **Concepts:** Experiments vs observational studies
- **Type:** MC
- **Question:**

Ice cream sales and sunburns are positively correlated across days. What's the most likely explanation?

- **Options:**

  A) A confounder, sunny hot weather, increases both
  B) Ice cream causes sunburn
  C) Sunburns make people buy ice cream
  D) It must be sampling error

- **Answer (tutor only):** A
- **Explanation (tutor only):** Sunny days drive both. This is the classic common-cause pattern.
- **Why the wrong options are wrong (tutor only):**
  B) and C) No plausible mechanism.
  D) Possible, but a confounder is far more likely with an obvious common cause.
- **Hint:** What makes both go up?

### ch12-hw-03
- **Kind:** Course original
- **Concepts:** Experiments vs observational studies
- **Type:** select-all
- **Question:**

Potential explanations for a significant relationship between A and B in a well-designed EXPERIMENT in which we manipulate A are (select all correct):

- **Options:**

  A) A causes B
  B) B causes A
  C) Both A and B are caused by some other variable, C
  D) Sampling error

- **Answer (tutor only):** A, D
- **Explanation (tutor only):** We set A ourselves, so B can't have caused it, and random assignment means no other variable determined it. What's left: A causes B, or we got a chance result (a type I error).
- **Why the wrong options are wrong (tutor only):**
  B) and C) Manipulating A by random assignment rules these out.
- **Hint:** Who decided each subject's value of A?

### ch12-hw-03-v1
- **Kind:** AI-written version of ch12-hw-03
- **Concepts:** Experiments vs observational studies
- **Type:** MC
- **Question:**

In a well-designed experiment, researchers randomly assign plants to receive extra nitrogen and find they grow taller (p = 0.01). Why can't 'height causes nitrogen' explain this?

- **Options:**

  A) The researchers set nitrogen themselves before the plants grew, so height couldn't have determined it
  B) Because p < 0.05
  C) Because nitrogen is a chemical
  D) It could explain it

- **Answer (tutor only):** A
- **Explanation (tutor only):** Manipulating the explanatory variable rules out reverse causation; random assignment rules out confounders. What remains: a causal effect or chance.
- **Why the wrong options are wrong (tutor only):**
  B) Significance doesn't address direction.
  C) Irrelevant.
  D) Manipulation rules it out.
- **Hint:** Who decided which plants got nitrogen?

### ch12-hw-03-v2
- **Kind:** AI-written version of ch12-hw-03
- **Concepts:** Experiments vs observational studies
- **Type:** MC
- **Question:**

A well-designed randomized experiment finds a significant effect. Which alternative explanation is still possible?

- **Options:**

  A) Chance: a false positive (type I error)
  B) Confounding by an unmeasured variable that systematically differs between groups
  C) Reverse causation
  D) None; the effect is proven

- **Answer (tutor only):** A
- **Explanation (tutor only):** Random assignment handles confounding and reverse causation, but chance can still produce a significant result.
- **Why the wrong options are wrong (tutor only):**
  B) Randomization balances confounders on average.
  C) The researcher set the treatment.
  D) There's always some chance of a false positive.
- **Hint:** What can randomization not remove?

### ch12-hw-04
- **Kind:** Course original
- **Concepts:** Experiments vs observational studies
- **Type:** MC
- **Question:**

Across years, the number of films Nicolas Cage appeared in correlates with the number of people who drowned by falling into swimming pools (a famous 'spurious correlation'). What is the best explanation?

- **Options:**

  A) With enough variables, some will be correlated by chance or through shared time trends; the association isn't causal
  B) Watching Nicolas Cage movies makes people careless near pools
  C) Drownings inspire Nicolas Cage to make more movies
  D) The correlation must be real because it was statistically significant

- **Answer (tutor only):** A
- **Explanation (tutor only):** If you search through many pairs of variables, some will line up just by chance (and things that trend over time often correlate). Without a plausible mechanism or an experiment, this is not evidence of causation.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Causal stories with no mechanism.
  D) Significance doesn't rule out chance when you've searched many pairs, and it says nothing about causation.
- **Hint:** How many silly pairs of variables could you test?

### ch12-hw-04-v1
- **Kind:** AI-written version of ch12-hw-04
- **Concepts:** Experiments vs observational studies
- **Type:** MC
- **Question:**

A researcher checks correlations between 50 lifestyle variables and 20 health outcomes (1000 pairs) and reports the 50 that are 'significant' at α = 0.05. What's the main problem?

- **Options:**

  A) About 50 significant results are expected by chance alone even if nothing is related
  B) 50 is too many variables to measure
  C) Significance proves causation
  D) No problem

- **Answer (tutor only):** A
- **Explanation (tutor only):** 1000 tests × 0.05 ≈ 50 false positives when no real associations exist. Searching many pairs guarantees spurious hits.
- **Why the wrong options are wrong (tutor only):**
  B) Measuring many variables is fine; the problem is the search.
  C) It doesn't.
  D) These could all be false positives.
- **Hint:** How many false positives does α = 0.05 allow over 1000 tests?

### ch12-hw-04-v2
- **Kind:** AI-written version of ch12-hw-04
- **Concepts:** Experiments vs observational studies
- **Type:** MC
- **Question:**

Across 20 years, a country's internet use and its average life expectancy both rose and are strongly correlated. Why should we be cautious about a causal claim?

- **Options:**

  A) Both trend upward over time for many reasons, and things that trend over time tend to correlate even without a causal link
  B) The correlation is too strong to be real
  C) Life expectancy can't be measured
  D) Internet use certainly causes longer life

- **Answer (tutor only):** A
- **Explanation (tutor only):** Shared time trends create correlations. Without a mechanism or better design, this isn't causal evidence.
- **Why the wrong options are wrong (tutor only):**
  B) Strength doesn't rule out a spurious link.
  C) It can.
  D) Unjustified.
- **Hint:** What else changed over those 20 years?

### ch12-hw-05
- **Kind:** Course original
- **Concepts:** Experiments vs observational studies; The language of causation
- **Type:** select-all
- **Question:**

Which statistical terms prime us to incorrectly conflate correlation and causation? (Pick all that apply.)

- **Options:**

  A) Calling Y the 'response' variable
  B) Calling differences 'effect sizes'
  C) Null hypothesis significance testing
  D) Calling it the 'sampling distribution'

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** 'Response' implies Y responds to X, and 'effect size' implies an effect. Both suggest causation even in observational data, where we only have associations.
- **Why the wrong options are wrong (tutor only):**
  C) and D) These are about inference under uncertainty, not causal language.
- **Hint:** Which words imply that X does something to Y?

### ch12-hw-05-v1
- **Kind:** AI-written version of ch12-hw-05
- **Concepts:** Experiments vs observational studies; The language of causation
- **Type:** MC
- **Question:**

Why can calling Y the 'response' variable be misleading in an observational study?

- **Options:**

  A) It implies Y responds to (is caused by) X, when we've only observed an association
  B) Y should always be called the 'explanatory' variable
  C) It makes the p-value incorrect
  D) It isn't misleading

- **Answer (tutor only):** A
- **Explanation (tutor only):** Statistical vocabulary often carries causal assumptions that the design can't support.
- **Why the wrong options are wrong (tutor only):**
  B) The labels are conventions; the issue is what they imply.
  C) Words don't change the math.
  D) The word suggests causation.
- **Hint:** What does 'response' suggest?

### ch12-hw-05-v2
- **Kind:** AI-written version of ch12-hw-05
- **Concepts:** Experiments vs observational studies
- **Type:** select-all
- **Question:**

Which phrases in a report on an OBSERVATIONAL study wrongly imply causation? (Select all.)

- **Options:**

  A) 'Exercise reduces depression'
  B) 'The effect of income on lifespan'
  C) 'Exercise is associated with lower depression'
  D) 'People with higher incomes tended to live longer'

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** 'Reduces' and 'effect of' are causal language. 'Associated with' and 'tended to' describe the pattern without claiming a cause.
- **Why the wrong options are wrong (tutor only):**
  C) and D) These are appropriately non-causal.
- **Hint:** Which words claim a cause?

### ch12-hw-06
- **Kind:** Course original
- **Concepts:** Experiments vs observational studies
- **Type:** MC
- **Question:**

Why do statisticians sometimes describe the 'perfect experiment' as splitting the world in two?

- **Options:**

  A) In a perfect experiment, we'd see what happens to each individual both with and without the treatment, and compare the two worlds
  B) Computer simulations are the best way to infer causation
  C) Because you need two separate samples to calculate a p-value
  D) Because experiments should always be repeated twice

- **Answer (tutor only):** A
- **Explanation (tutor only):** The ideal comparison is the counterfactual: the same individual, treated and untreated. We can't observe both, so random assignment creates groups that are alike on average, the next best thing.
- **Why the wrong options are wrong (tutor only):**
  B) Simulations don't establish causation.
  C) and D) Not the point of the analogy.
- **Hint:** What would you ideally compare each individual to?

### ch12-hw-06-v1
- **Kind:** AI-written version of ch12-hw-06
- **Concepts:** Experiments vs observational studies
- **Type:** MC
- **Question:**

What is a counterfactual in the context of causal inference?

- **Options:**

  A) What would have happened to the same individual if they had received the other treatment
  B) A false fact in the data
  C) A control group that got nothing
  D) A statistical test

- **Answer (tutor only):** A
- **Explanation (tutor only):** Causal effects compare what happened with what would have happened otherwise. We can never observe both for one individual.
- **Why the wrong options are wrong (tutor only):**
  B) Not a data error.
  C) A control group approximates the counterfactual, but isn't the same thing.
  D) Not a test.
- **Hint:** Same individual, other treatment.

### ch12-hw-06-v2
- **Kind:** AI-written version of ch12-hw-06
- **Concepts:** Experiments vs observational studies
- **Type:** MC
- **Question:**

Since we can't observe the same individual both treated and untreated, how does a randomized experiment approximate the counterfactual?

- **Options:**

  A) Randomly assigned groups are alike on average, so the control group shows what would have happened to the treated group without treatment
  B) By measuring each individual twice
  C) By using a very large sample
  D) It can't

- **Answer (tutor only):** A
- **Explanation (tutor only):** Randomization makes the control group a stand-in for the treated group's 'other world.'
- **Why the wrong options are wrong (tutor only):**
  B) Repeated measures help in some designs, but time also changes.
  C) Size helps precision, not comparability.
  D) That's exactly what randomization does.
- **Hint:** Why is the control group a good stand-in?

### ch12-hw-07
- **Kind:** Course original
- **Concepts:** Controls & placebos
- **Type:** TF
- **Question:**

TRUE or FALSE: Doing nothing is usually the best control.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** A good control matches the treatment in every way except the factor of interest: a placebo pill, a sham surgery, handling the plants the same way. Doing nothing leaves differences (handling, expectation, placebo effects) that could explain the result.
- **Why the wrong options are wrong (tutor only):**
  A) 'Nothing' differs from the treatment in more than one way.
- **Hint:** Besides the active ingredient, what else does the treatment group experience?

### ch12-hw-07-v1
- **Kind:** AI-written version of ch12-hw-07
- **Concepts:** Controls & placebos
- **Type:** MC
- **Question:**

A study tests whether a new surgical procedure reduces knee pain. What is the best control?

- **Options:**

  A) A sham surgery (incisions but no actual repair), with patients unaware of which they got
  B) No surgery at all
  C) Patients who refused surgery
  D) The same patients before surgery

- **Answer (tutor only):** A
- **Explanation (tutor only):** A sham control matches everything except the active ingredient: anesthesia, recovery, expectation of improvement.
- **Why the wrong options are wrong (tutor only):**
  B) Differs in many ways besides the repair (including placebo effects).
  C) Self-selected, so confounded.
  D) Pain changes over time anyway.
- **Hint:** Match everything but the factor of interest.

### ch12-hw-07-v2
- **Kind:** AI-written version of ch12-hw-07
- **Concepts:** Controls & placebos
- **Type:** MC
- **Question:**

In a plant experiment, treated pots get a fertilizer dissolved in water. What should control pots get?

- **Options:**

  A) The same amount of plain water, applied the same way
  B) Nothing
  C) A different fertilizer
  D) Half the fertilizer

- **Answer (tutor only):** A
- **Explanation (tutor only):** The control should differ only in the fertilizer itself, so extra water or handling can't explain differences.
- **Why the wrong options are wrong (tutor only):**
  B) Treated pots also got extra water and handling.
  C) and D) Those are other treatments, not controls.
- **Hint:** What else does the treatment include besides fertilizer?

### ch12-hw-08
- **Kind:** Course original
- **Concepts:** Power & precision
- **Type:** select-all
- **Question:**

To estimate our power, we need to know (select all correct):

- **Options:**

  A) The sample size
  B) The minimal effect size that would be biologically meaningful
  C) The probability that the null is false
  D) The identity of the subjects in our study

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** Power depends on sample size, the effect size you want to detect, and the variability (plus α). You choose the smallest meaningful effect and ask how likely your design is to detect it.
- **Why the wrong options are wrong (tutor only):**
  C) That's unknowable and not part of a power calculation.
  D) Who the subjects are doesn't enter the calculation.
- **Hint:** What makes a real effect easier to detect?

### ch12-hw-08-v1
- **Kind:** AI-written version of ch12-hw-08
- **Concepts:** Power & precision
- **Type:** select-all
- **Question:**

Which of these would INCREASE the power of a study? (Select all.)

- **Options:**

  A) A larger sample size
  B) Reducing measurement noise
  C) A larger true effect
  D) Using α = 0.01 instead of 0.05

- **Answer (tutor only):** A, B, C
- **Explanation (tutor only):** Power rises with sample size, precision and effect size. A stricter α lowers power.
- **Why the wrong options are wrong (tutor only):**
  D) Harder to reject means lower power.
- **Hint:** What makes a real effect easier to detect?

### ch12-hw-08-v2
- **Kind:** AI-written version of ch12-hw-08
- **Concepts:** Power & precision
- **Type:** MC
- **Question:**

Why should a researcher estimate power BEFORE running an experiment?

- **Options:**

  A) To check whether the planned sample size is large enough to detect the smallest effect that would matter
  B) To guarantee a significant result
  C) To find out whether the null is true
  D) To calculate the p-value

- **Answer (tutor only):** A
- **Explanation (tutor only):** A power analysis helps avoid wasting effort on a study too small to detect meaningful effects.
- **Why the wrong options are wrong (tutor only):**
  B) Nothing guarantees significance.
  C) Power doesn't tell you that.
  D) p-values come from the data.
- **Hint:** Is the study big enough?
