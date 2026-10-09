# Applied Biostats tutor: question bank, chapters 7–9 (Exam 1, chapters 0–12)

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

## Chapter 7: Associations II

### ch07-book-01
- **Kind:** Course original
- **Concepts:** Correlation; Association vs causation
- **Type:** MC
- **Question:**

Correlations among Clarkia RIL traits (pairwise complete data, n ≈ 435–440 plants):

pair | correlation
petal_area & prop_hybrid | 0.224
lwc (leaf water content) & prop_hybrid | −0.202
petal_area & lwc | −0.168

Which variable, leaf water content (lwc) or petal area, is more plausibly interpreted as influencing proportion hybrid seed (prop_hybrid)?

- **Options:**

  A) Equally likely, because the absolute values of their correlations are similar
  B) Petal area, because it has the stronger correlation coefficient
  C) Neither: the correlations are both near zero
  D) Petal area: there's a substantial association, these are experimental RILs, and it's biologically plausible that pollinators are attracted to larger petals, not to low leaf water content
  E) There is no relevant information here; correlation does not imply causation

- **Answer (tutor only):** D
- **Explanation (tutor only):** The correlations are similar in size (0.22 vs −0.20), so the numbers alone can't decide. Biology plus design does: RILs shuffle traits, and a pollinator responding to petal size is a plausible mechanism, whereas pollinators sensing leaf water content is not.
- **Why the wrong options are wrong (tutor only):**
  A) Similar r doesn't mean similar plausibility as a cause.
  B) 0.224 vs 0.202 is barely different, so that's not the reason.
  C) About ±0.2 is modest but not zero.
  E) Correlation isn't proof, but combined with design and mechanism it is evidence.
- **Hint:** The numbers are nearly tied. What else can help you decide?

### ch07-book-01-v1
- **Kind:** AI-written version of ch07-book-01
- **Concepts:** Correlation; Association vs causation
- **Type:** MC
- **Question:**

In an experiment, Clarkia plants were randomly assigned to have their petals trimmed or left intact; intact plants set more hybrid seed. In a separate observational dataset, soil moisture correlates with hybrid seed at about the same strength. Which variable is more plausibly a cause of hybrid seed set?

- **Options:**

  A) Petal size, because it was manipulated with random assignment
  B) Soil moisture, because it's an environmental factor
  C) Both equally, since the associations are similar
  D) Neither; correlation never implies causation

- **Answer (tutor only):** A
- **Explanation (tutor only):** Random assignment rules out confounders, so the petal experiment supports a causal effect. The soil-moisture correlation could reflect confounding.
- **Why the wrong options are wrong (tutor only):**
  B) Being environmental doesn't make it causal.
  C) Similar strength doesn't mean similar evidence for causation.
  D) Experiments can support causal claims.
- **Hint:** Which result came from an experiment?

### ch07-book-01-v2
- **Kind:** AI-written version of ch07-book-01
- **Concepts:** Correlation; Association vs causation
- **Type:** MC
- **Question:**

Two traits correlate with seed set: flower color (r = 0.25) and leaf hairiness (r = 0.24). Pollinators are known to respond to flower color. Which is more plausibly causal, and why?

- **Options:**

  A) Flower color: the correlation plus a known mechanism make it more plausible
  B) Leaf hairiness, because both correlations are similar
  C) Both equally
  D) Neither; we can say nothing

- **Answer (tutor only):** A
- **Explanation (tutor only):** When correlations are similar, biological plausibility (and ideally experiments) helps decide what's likely causal.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Similar r doesn't mean similar plausibility.
  D) Mechanism provides evidence, though not proof.
- **Hint:** What do you know about how pollinators choose flowers?

### ch07-book-02
- **Kind:** Course original
- **Concepts:** Association vs causation
- **Type:** MC
- **Question:**

Correlations among Clarkia RIL traits (pairwise complete data, n ≈ 435–440 plants):

pair | correlation
petal_area & prop_hybrid | 0.224
lwc (leaf water content) & prop_hybrid | −0.202
petal_area & lwc | −0.168

Which explanation best accounts for the negative association between leaf water content and proportion hybrid seed?

- **Options:**

  A) Chance: strange associations sometimes appear randomly
  B) Reverse causation: pollinator visits might reduce leaf water content
  C) A direct causal link: pollinators are attracted to plants with dry leaves
  D) Confounding: low leaf water content may be linked (genetically or physiologically) with a trait that does influence pollinators, e.g., petal area

- **Answer (tutor only):** D
- **Explanation (tutor only):** lwc is negatively correlated with petal area (r = −0.17), and petal area is positively correlated with hybrid seed. So plants with low lwc tend to have bigger petals, which attract pollinators. That makes lwc and hybrid seed look related through petal area.
- **Why the wrong options are wrong (tutor only):**
  A) Possible, but the table shows a better explanation.
  B) and C) Neither has a plausible mechanism.
- **Hint:** Look at the third row of the table.

### ch07-book-02-v1
- **Kind:** AI-written version of ch07-book-02
- **Concepts:** Association vs causation
- **Type:** MC
- **Question:**

Across towns, the number of churches correlates positively with the number of crimes. What's the most likely explanation?

- **Options:**

  A) Confounding: bigger towns have more of both
  B) Churches cause crime
  C) Crime causes church building
  D) Pure chance

- **Answer (tutor only):** A
- **Explanation (tutor only):** Population size drives both counts. That's a classic confounder.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Causal stories ignoring an obvious third variable.
  D) A strong pattern across many towns isn't just chance.
- **Hint:** What makes both numbers go up?

### ch07-book-02-v2
- **Kind:** AI-written version of ch07-book-02
- **Concepts:** Association vs causation
- **Type:** MC
- **Question:**

Leaf water content correlates negatively with seed set, and leaf water content also correlates negatively with petal size. Petal size correlates positively with seed set. What might explain the first correlation?

- **Options:**

  A) Petal size may confound it: plants with bigger petals have drier leaves and more seed set
  B) Dry leaves attract pollinators
  C) Seed set dries out leaves
  D) Chance alone

- **Answer (tutor only):** A
- **Explanation (tutor only):** If petal size affects seed set and is linked to leaf water content, leaf water content will correlate with seed set even without a direct effect.
- **Why the wrong options are wrong (tutor only):**
  B) and C) No plausible mechanism.
  D) A better explanation exists.
- **Hint:** Look for a third variable linked to both.

### ch07-book-03
- **Kind:** Course original
- **Concepts:** Covariance
- **Type:** numeric
- **Question:**

We collected 131 Clarkia plants (74 parviflora, 57 xantiana) from a natural hybrid zone and genotyped a chloroplast marker.

species | parviflora chloroplast | xantiana chloroplast | total
parviflora | 74 | 0 | 74
xantiana | 8 | 49 | 57
total | 82 | 49 | 131

a) If species and chloroplast type were independent, what proportion of plants would you expect to be xantiana AND have a xantiana chloroplast?
b) How much does the observed proportion differ from that expectation (observed − expected)?

- **Answer (tutor only):** a) (57/131) × (49/131) ≈ 0.163
b) 49/131 − 0.163 = 0.374 − 0.163 ≈ 0.211
- **Explanation (tutor only):** a) P(xantiana) = 57/131 = 0.435; P(xan chloroplast) = 49/131 = 0.374; product = 0.163. b) Observed joint proportion = 49/131 = 0.374, which is much more than 0.163, so species and chloroplast are strongly associated.
- **Why the wrong options are wrong (tutor only):**
  Using 49/57 (a conditional proportion) instead of 49/131 (joint) is the most common slip.
- **Hint:** Expected joint = product of the two marginal proportions. Observed joint = count in that cell / total.

### ch07-book-03-v1
- **Kind:** AI-written version of ch07-book-03
- **Concepts:** Covariance
- **Type:** numeric
- **Question:**

We trapped 100 mice and recorded coat color and habitat:

coat | lava | sand | total
dark | 30 | 10 | 40
light | 5 | 55 | 60
total | 35 | 65 | 100

a) If coat color and habitat were independent, what proportion would be dark AND on lava?
b) How much does the observed proportion differ (observed − expected)?

- **Answer (tutor only):** a) 0.14
b) 0.16
- **Explanation (tutor only):** a) 0.40 × 0.35 = 0.14. b) Observed 30/100 = 0.30; 0.30 − 0.14 = 0.16.
- **Why the wrong options are wrong (tutor only):**
  Using a conditional proportion (30/35) instead of the joint (30/100).
- **Hint:** Expected = product of marginals; observed = cell count / total.

### ch07-book-03-v2
- **Kind:** AI-written version of ch07-book-03
- **Concepts:** Covariance
- **Type:** numeric
- **Question:**

Of 200 birds, 80 are migratory and 50 carry a parasite. 35 are migratory AND carry the parasite. What is observed − expected for the joint proportion of migratory birds with parasites?

- **Answer (tutor only):** 0.075
- **Explanation (tutor only):** Expected = (80/200) × (50/200) = 0.4 × 0.25 = 0.10. Observed = 35/200 = 0.175. Difference = 0.075.
- **Why the wrong options are wrong (tutor only):**
  Using 35/80 or 35/50 (conditional proportions).
- **Hint:** Joint proportions divide by 200.

### ch07-book-04
- **Kind:** Course original
- **Concepts:** Covariance
- **Type:** numeric
- **Question:**

We collected 131 Clarkia plants (74 parviflora, 57 xantiana) from a natural hybrid zone and genotyped a chloroplast marker.

species | parviflora chloroplast | xantiana chloroplast | total
parviflora | 74 | 0 | 74
xantiana | 8 | 49 | 57
total | 82 | 49 | 131

The observed joint proportion of xantiana plants with xantiana chloroplasts exceeds the expectation under independence by 0.2113. What is the covariance between being a xantiana plant and having a xantiana chloroplast, using Bessel's correction?

- **Answer (tutor only):** 0.2113 × 131/130 ≈ 0.213
- **Explanation (tutor only):** For 0/1 variables, (observed − expected joint proportion) is the covariance with n in the denominator. Bessel's correction switches to n − 1: multiply by n/(n − 1) = 131/130, giving 0.2129.
- **Why the wrong options are wrong (tutor only):**
  Forgetting Bessel's correction gives 0.2113. Multiplying by 130/131 goes the wrong way.
- **Hint:** Going from dividing by n to dividing by n − 1 means multiplying by n/(n − 1).

### ch07-book-04-v1
- **Kind:** AI-written version of ch07-book-04
- **Concepts:** Covariance
- **Type:** numeric
- **Question:**

We trapped 100 mice and recorded coat color and habitat:

coat | lava | sand | total
dark | 30 | 10 | 40
light | 5 | 55 | 60
total | 35 | 65 | 100

Observed minus expected joint proportion is 0.16. What is the covariance between being dark and being on lava, using Bessel's correction (n = 100)?

- **Answer (tutor only):** ≈ 0.162
- **Explanation (tutor only):** Multiply by n / (n − 1): 0.16 × 100/99 ≈ 0.1616.
- **Why the wrong options are wrong (tutor only):**
  Forgetting Bessel's correction gives 0.16.
- **Hint:** From dividing by n to dividing by n − 1: multiply by n/(n − 1).

### ch07-book-04-v2
- **Kind:** AI-written version of ch07-book-04
- **Concepts:** Covariance
- **Type:** numeric
- **Question:**

For 200 birds, observed − expected joint proportion of migratory birds with parasites is 0.075. What's the covariance with Bessel's correction?

- **Answer (tutor only):** ≈ 0.0754
- **Explanation (tutor only):** 0.075 × 200/199 ≈ 0.0754. With large n, Bessel's correction barely matters.
- **Why the wrong options are wrong (tutor only):**
  Multiplying by 199/200 goes the wrong way.
- **Hint:** Multiply by n/(n − 1).

### ch07-book-05
- **Kind:** Course original
- **Concepts:** Correlation
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch07-book-fourpanels.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch07-book-fourpanels.png)
- **Question:**

Consider the four scatterplots (a–d), each with a best-fit straight line. In which panel:

1. are x and y most tightly associated?
2. are x and y most tightly linearly associated?
3. do x and y have the most positive correlation coefficient?
4. does x do the worst job of predicting y?

- **Options:**

  A) a
  B) b
  C) c
  D) d

- **Answer (tutor only):** 1-A, 2-C, 3-B, 4-D
- **Explanation (tutor only):** 1. a: y is almost exactly determined by x, but along a U-shaped curve. 2. c: the points hug a straight line most closely (r ≈ −0.87). 3. b: r ≈ 0.77, the most positive. 4. d: almost no relationship (r ≈ 0.16). Note that a has r ≈ 0.05 even though the relationship is very tight, because r only measures linear association.
- **Why the wrong options are wrong (tutor only):**
  a for 'linear' or 'correlation': a U-shape has r near 0.
  c for 'most positive': its r is strongly negative.
- **Hint:** Correlation measures straight-line association only, and its sign matters.

### ch07-book-05-v1
- **Kind:** AI-written version of ch07-book-05
- **Concepts:** Correlation
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch07-var-fourpanels.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch07-var-fourpanels.png)
- **Question:**

In panel a, the points fall tightly along a downward line. Which describes its correlation?

- **Options:**

  A) Close to −1
  B) Close to 0
  C) Close to +1
  D) Exactly 0.5

- **Answer (tutor only):** A
- **Explanation (tutor only):** A tight negative linear relationship gives r near −1 (here about −0.96).
- **Why the wrong options are wrong (tutor only):**
  B) The relationship is strong.
  C) It slopes down.
  D) No reason for 0.5.
- **Hint:** Direction from the slope; strength from the tightness.

### ch07-book-05-v2
- **Kind:** AI-written version of ch07-book-05
- **Concepts:** Correlation
- **Type:** MC
- **Question:**

Which statement about the correlation coefficient is true?

- **Options:**

  A) A U-shaped or arch-shaped relationship can have r near 0
  B) r near 0 means x and y are unrelated
  C) A steeper line always means a larger r
  D) r can be greater than 1 for very strong relationships

- **Answer (tutor only):** A
- **Explanation (tutor only):** r measures only linear association; curved relationships can be strong yet have r ≈ 0.
- **Why the wrong options are wrong (tutor only):**
  B) Nonlinear relationships can hide behind r ≈ 0.
  C) r measures tightness around a line, not steepness.
  D) r is between −1 and 1.
- **Hint:** What kind of relationship does r measure?

### ch07-gquiz-01
- **Kind:** Course original
- **Concepts:** Covariance
- **Type:** MC
- **Question:**

Compare the equations for variance and covariance:

Var(X) = Σ(xᵢ − x̄)² / (n − 1)
Cov(X, Y) = Σ(xᵢ − x̄)(yᵢ − ȳ) / (n − 1)

Which statement is correct?

- **Options:**

  A) Both sum products of deviations from the mean and divide by n − 1; variance multiplies a variable's deviation by itself, while covariance multiplies deviations of two different variables, so covariance can be negative
  B) They are the same except that covariance divides by n
  C) Covariance is the square root of variance
  D) Both are always positive

- **Answer (tutor only):** A
- **Explanation (tutor only):** Variance is the covariance of a variable with itself: Cov(X, X) = Var(X). Because the deviations in covariance can have opposite signs, covariance can be negative (as X goes up, Y goes down), but variance never can.
- **Why the wrong options are wrong (tutor only):**
  B) Both use n − 1 for samples.
  C) That's the standard deviation.
  D) Variance is ≥ 0, but covariance can be negative.
- **Hint:** What would you get if you plugged X in for Y in the covariance formula?

### ch07-gquiz-01-v1
- **Kind:** AI-written version of ch07-gquiz-01
- **Concepts:** Covariance
- **Type:** MC
- **Question:**

Which statement about covariance is true?

- **Options:**

  A) Cov(X, X) equals Var(X)
  B) Covariance is always positive
  C) Covariance has no units
  D) Covariance is the same as correlation

- **Answer (tutor only):** A
- **Explanation (tutor only):** Covariance multiplies the deviations of X and Y. If Y is X itself, that's the squared deviation, i.e., the variance.
- **Why the wrong options are wrong (tutor only):**
  B) It's negative when one variable goes down as the other goes up.
  C) It has units (units of X × units of Y).
  D) Correlation is covariance standardized by both SDs.
- **Hint:** Plug X in for Y.

### ch07-gquiz-01-v2
- **Kind:** AI-written version of ch07-gquiz-01
- **Concepts:** Covariance
- **Type:** MC
- **Question:**

Big deviations above the mean in X tend to pair with big deviations below the mean in Y. The covariance will be:

- **Options:**

  A) Negative
  B) Positive
  C) Zero
  D) Undefined

- **Answer (tutor only):** A
- **Explanation (tutor only):** Each product (positive × negative) is negative, so their sum (and the covariance) is negative.
- **Why the wrong options are wrong (tutor only):**
  B) That would need deviations in the same direction.
  C) Zero would need no consistent pattern.
  D) It's defined.
- **Hint:** What's the sign of (positive) × (negative)?

### ch07-gquiz-03
- **Kind:** Course original
- **Concepts:** Covariance; Correlation
- **Type:** MC
- **Question:**

You want to compare how strongly fruit size is related to cost per pound in apples vs in oranges. Which statistic should you use?

- **Options:**

  A) Correlation, because it is standardized (unitless, between −1 and 1), so its strength can be compared across groups measured on different scales
  B) Covariance, because it keeps the original units
  C) Covariance, because it can be negative
  D) Either; they always give the same answer

- **Answer (tutor only):** A
- **Explanation (tutor only):** Covariance depends on the units and spread of each variable, so a bigger covariance in oranges could just mean oranges vary more in size or price. Correlation divides covariance by both SDs, so it measures the strength of the linear relationship on a common scale.
- **Why the wrong options are wrong (tutor only):**
  B) Keeping units is exactly the problem when comparing strength across groups.
  C) Correlation can be negative too.
  D) They agree in sign but not in magnitude.
- **Hint:** What does dividing by the two SDs do?

### ch07-gquiz-03-v1
- **Kind:** AI-written version of ch07-gquiz-03
- **Concepts:** Covariance; Correlation
- **Type:** MC
- **Question:**

Two studies relate body size to running speed: one in mice (grams, cm/s), one in horses (kg, m/s). Which statistic lets you compare the strength of the relationship?

- **Options:**

  A) Correlation
  B) Covariance
  C) Either one
  D) Neither

- **Answer (tutor only):** A
- **Explanation (tutor only):** Correlation is unitless and bounded by −1 and 1, so it compares strength across scales. Covariance depends on the units.
- **Why the wrong options are wrong (tutor only):**
  B) Covariance would differ just because of units.
  C) Only correlation is standardized.
  D) Correlation works.
- **Hint:** Which statistic doesn't care about units?

### ch07-gquiz-03-v2
- **Kind:** AI-written version of ch07-gquiz-03
- **Concepts:** Covariance; Correlation
- **Type:** MC
- **Question:**

If you convert mass from grams to kilograms, what happens to the covariance between mass and length, and to their correlation?

- **Options:**

  A) The covariance shrinks 1000-fold; the correlation is unchanged
  B) Both shrink 1000-fold
  C) Neither changes
  D) The correlation shrinks; the covariance doesn't

- **Answer (tutor only):** A
- **Explanation (tutor only):** Covariance carries the units of mass, so it shrinks when mass is in larger units. Correlation divides by the SDs, which shrink by the same factor, so it's unchanged.
- **Why the wrong options are wrong (tutor only):**
  B) Correlation is unitless.
  C) Covariance changes with units.
  D) Backwards.
- **Hint:** Which one has units?

### ch07-gquiz-04
- **Kind:** Course original
- **Concepts:** Covariance
- **Type:** numeric
- **Question:**

A store had a buy-one-get-one-free sale on apples and oranges. Half of all fruit sold were apples and half were oranges. Of the pairs of fruit sold, one third consisted of two oranges. Code each fruit as 1 = orange, 0 = apple. What is the covariance between the first and second fruit in a pair? (Ignore Bessel's correction.)

- **Answer (tutor only):** 1/12 ≈ 0.083
- **Explanation (tutor only):** Cov(X, Y) = E[XY] − E[X]E[Y]. XY = 1 only when both are oranges, so E[XY] = P(both orange) = 1/3. E[X] = E[Y] = 1/2. Cov = 1/3 − 1/4 = 1/12 ≈ 0.083. It's positive: people who pick one orange tend to pick another (if independent, P(two oranges) would be 1/4).
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: using 1/3 (the joint probability) as the answer, or forgetting to subtract E[X]E[Y] = 1/4.
- **Hint:** If the fruits were picked independently, what would P(two oranges) be? Compare to 1/3.

### ch07-gquiz-04-v1
- **Kind:** AI-written version of ch07-gquiz-04
- **Concepts:** Covariance
- **Type:** numeric
- **Question:**

Seed pods each contain two seeds. Code germinated = 1, not = 0. Each seed germinates with probability 0.6, but both seeds in a pod germinate 45% of the time. What is the covariance between the two seeds' outcomes (ignore Bessel's correction)?

- **Answer (tutor only):** 0.09
- **Explanation (tutor only):** Cov = P(both) − P(first) × P(second) = 0.45 − 0.6 × 0.6 = 0.45 − 0.36 = 0.09. Positive: seeds in the same pod tend to share fate.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: reporting 0.45 (the joint probability), or forgetting to subtract 0.36.
- **Hint:** If independent, how often would both germinate?

### ch07-gquiz-04-v2
- **Kind:** AI-written version of ch07-gquiz-04
- **Concepts:** Covariance
- **Type:** numeric
- **Question:**

Half of all fruit sold are oranges. If shoppers picked the two fruits in a pair independently, what would the covariance be between the first and second fruit (orange = 1)?

- **Answer (tutor only):** 0
- **Explanation (tutor only):** Under independence, P(both orange) = 0.5 × 0.5 = 0.25, so Cov = 0.25 − 0.25 = 0.
- **Why the wrong options are wrong (tutor only):**
  Covariance measures departure from independence; with independence there's none.
- **Hint:** Covariance = observed joint − expected joint.

### ch07-gquiz-06
- **Kind:** Course original
- **Concepts:** Covariance; Correlation
- **Type:** MC
- **Question:**

If we measure the heights of people in inches and in feet, the two variables are perfectly linearly related (inches = 12 × feet). What are the covariance and the correlation between height in inches and height in feet?

- **Options:**

  A) Covariance = 12 × Var(height in feet), which depends on the data and the units; correlation = 1
  B) Covariance = 1; correlation = 1
  C) Covariance = 12; correlation = 12
  D) Covariance = 1; correlation = 1/12

- **Answer (tutor only):** A
- **Explanation (tutor only):** Cov(12F, F) = 12·Cov(F, F) = 12·Var(F), so there's no fixed number: it depends on how variable heights are. Correlation = Cov / (SD_inches × SD_feet) = 12·Var(F) / (12·SD_F × SD_F) = 1. A perfect positive linear relationship always has r = 1, whatever the units.
- **Why the wrong options are wrong (tutor only):**
  B) Covariance isn't standardized, so it's not automatically 1.
  C) Correlation can never exceed 1.
  D) Changing units doesn't change correlation.
- **Hint:** Covariance has units; correlation doesn't. What is Cov(F, F)?

### ch07-gquiz-06-v1
- **Kind:** AI-written version of ch07-gquiz-06
- **Concepts:** Covariance; Correlation
- **Type:** MC
- **Question:**

Temperature in °C and the same temperatures in °F (F = 1.8 × C + 32) are perfectly linearly related. What is their correlation?

- **Options:**

  A) 1
  B) 1.8
  C) 32
  D) It depends on the temperatures

- **Answer (tutor only):** A
- **Explanation (tutor only):** Any perfect positive linear relationship has r = 1, no matter the slope or intercept.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Correlation can't exceed 1.
  D) Perfect linear relationships always give r = 1.
- **Hint:** What does a perfect straight-line relationship give?

### ch07-gquiz-06-v2
- **Kind:** AI-written version of ch07-gquiz-06
- **Concepts:** Covariance; Correlation
- **Type:** MC
- **Question:**

y = −2x exactly, for a set of x values. What is the correlation between x and y?

- **Options:**

  A) −1
  B) −2
  C) 0
  D) 1

- **Answer (tutor only):** A
- **Explanation (tutor only):** A perfect negative linear relationship gives r = −1, whatever the slope.
- **Why the wrong options are wrong (tutor only):**
  B) Correlation is bounded by −1 and 1.
  C) There's a perfect relationship.
  D) The relationship is negative.
- **Hint:** Direction and perfection, not slope.

### ch07-hw-01
- **Kind:** Course original
- **Concepts:** Covariance
- **Type:** numeric
- **Question:**

A taste of brilliance. These data (Prinz 2020) give national chocolate consumption, coffee consumption, and number of Nobel laureates for different countries.

Of the 24 countries with coffee consumption data:
• 10 (0.417) drink more than the average amount of coffee
• 15 (0.625) have more than ten Nobel laureates

If coffee drinking and Nobel success were independent, what proportion would you expect to BOTH drink more than average coffee AND have more than ten Nobel laureates?

- **Answer (tutor only):** 0.417 × 0.625 ≈ 0.260
- **Explanation (tutor only):** Under independence, P(A and B) = P(A) × P(B) = 0.4167 × 0.625 = 0.2604. That's about 6.25 of 24 countries.
- **Why the wrong options are wrong (tutor only):**
  Adding the proportions (1.04) gives an impossible value above 1. Using a conditional proportion (e.g., 6/10) answers a different question.
- **Hint:** Multiplication rule for independent events.

### ch07-hw-01-v1
- **Kind:** AI-written version of ch07-hw-01
- **Concepts:** Covariance
- **Type:** numeric
- **Question:**

In a forest, 40% of trees are oaks and 50% of trees have a fungal infection. If species and infection were independent, what proportion of trees would be infected oaks?

- **Answer (tutor only):** 0.20
- **Explanation (tutor only):** Under independence, P(oak and infected) = 0.4 × 0.5 = 0.20.
- **Why the wrong options are wrong (tutor only):**
  Adding (0.9) gives an impossible joint proportion.
- **Hint:** Multiplication rule.

### ch07-hw-01-v2
- **Kind:** AI-written version of ch07-hw-01
- **Concepts:** Covariance
- **Type:** numeric
- **Question:**

We trapped 100 mice and recorded coat color and habitat:

coat | lava | sand | total
dark | 30 | 10 | 40
light | 5 | 55 | 60
total | 35 | 65 | 100

If coat color and habitat were independent, what proportion of mice would you expect to be dark AND on lava?

- **Answer (tutor only):** 0.14
- **Explanation (tutor only):** P(dark) × P(lava) = 0.40 × 0.35 = 0.14 (14 of 100 mice).
- **Why the wrong options are wrong (tutor only):**
  Using the observed 0.30 answers a different question.
- **Hint:** Multiply the two marginal proportions.

### ch07-hw-02
- **Kind:** Course original
- **Concepts:** Covariance
- **Type:** numeric
- **Question:**

A taste of brilliance. These data (Prinz 2020) give national chocolate consumption, coffee consumption, and number of Nobel laureates for different countries.

Of the 24 countries with coffee consumption data:
• 10 (0.417) drink more than the average amount of coffee
• 15 (0.625) have more than ten Nobel laureates

We actually find that 6 of 24 countries (0.25) both drink more coffee than average AND have more than ten Nobel laureates. Find the covariance between these two binary variables (ignore Bessel's correction).

- **Answer (tutor only):** 0.25 − 0.2604 ≈ −0.0104
- **Explanation (tutor only):** For binary (0/1) variables, the covariance is observed joint proportion − expected joint proportion under independence: 0.25 − 0.417 × 0.625 = 0.25 − 0.2604 = −0.0104. It's tiny and slightly negative: high-coffee countries are very slightly *less* likely to have many Nobels than independence predicts.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: reporting 0.25 (the joint proportion) or flipping the sign (expected − observed).
- **Hint:** Covariance = P(A and B) − P(A)·P(B).

### ch07-hw-02-v1
- **Kind:** AI-written version of ch07-hw-02
- **Concepts:** Covariance
- **Type:** numeric
- **Question:**

40% of trees are oaks, 50% are infected, and 30% are infected oaks. What is the covariance between being an oak and being infected (ignore Bessel's correction)?

- **Answer (tutor only):** 0.10
- **Explanation (tutor only):** Cov = observed joint − expected joint = 0.30 − 0.40 × 0.50 = 0.10. Positive: oaks are infected more often than independence predicts.
- **Why the wrong options are wrong (tutor only):**
  Reporting 0.30 (the joint) or flipping the sign.
- **Hint:** Observed minus expected.

### ch07-hw-02-v2
- **Kind:** AI-written version of ch07-hw-02
- **Concepts:** Covariance
- **Type:** numeric
- **Question:**

We trapped 100 mice and recorded coat color and habitat:

coat | lava | sand | total
dark | 30 | 10 | 40
light | 5 | 55 | 60
total | 35 | 65 | 100

What is the covariance between being dark and being on lava (ignore Bessel's correction)?

- **Answer (tutor only):** 0.16
- **Explanation (tutor only):** Observed joint = 0.30; expected = 0.40 × 0.35 = 0.14. Cov = 0.30 − 0.14 = 0.16.
- **Why the wrong options are wrong (tutor only):**
  Forgetting to subtract the expectation, or using conditional proportions.
- **Hint:** Observed joint − product of marginals.

### ch07-hw-03
- **Kind:** Course original
- **Concepts:** Covariance; Correlation
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch07-hw-choc-nobel-scatter.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch07-hw-choc-nobel-scatter.png)
- **Question:**

A taste of brilliance. These data (Prinz 2020) give national chocolate consumption, coffee consumption, and number of Nobel laureates for different countries.

The scatterplot shows chocolate consumption vs number of Nobel laureates for 27 countries.

Cov(chocolate, laureates) = 81.3
SD(chocolate) = 2.99 kg/capita
SD(laureates) = 76.1

What is the correlation?

- **Answer (tutor only):** ≈ 0.36
- **Explanation (tutor only):** r = Cov / (SD_x × SD_y) = 81.3 / (2.99 × 76.1) = 81.3 / 227.5 ≈ 0.36. A moderate positive correlation. Note in the plot that a few countries (USA especially) have far more laureates than the rest, so this correlation is driven largely by a handful of points.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: reporting the covariance (81.3), which has units and isn't bounded by ±1; or dividing by only one SD.
- **Hint:** Correlation = covariance divided by the product of the two SDs.

### ch07-hw-03-v1
- **Kind:** AI-written version of ch07-hw-03
- **Concepts:** Covariance; Correlation
- **Type:** numeric
- **Question:**

For a sample of lizards, Cov(body length, sprint speed) = 12, SD(length) = 4 and SD(speed) = 5. What is the correlation?

- **Answer (tutor only):** 0.6
- **Explanation (tutor only):** r = 12 / (4 × 5) = 0.6.
- **Why the wrong options are wrong (tutor only):**
  Reporting the covariance, or dividing by only one SD.
- **Hint:** r = Cov / (SD_x × SD_y).

### ch07-hw-03-v2
- **Kind:** AI-written version of ch07-hw-03
- **Concepts:** Covariance; Correlation
- **Type:** numeric
- **Question:**

Cov(x, y) = −18, SD(x) = 3 and SD(y) = 10. What is the correlation?

- **Answer (tutor only):** -0.6
- **Explanation (tutor only):** r = −18 / (3 × 10) = −0.6: a moderately strong negative association.
- **Why the wrong options are wrong (tutor only):**
  Dropping the sign, or forgetting to divide by both SDs.
- **Hint:** Keep the sign of the covariance.

### ch07-hw-04
- **Kind:** Course original
- **Concepts:** Association vs causation
- **Type:** MC
- **Question:**

A taste of brilliance. These data (Prinz 2020) give national chocolate consumption, coffee consumption, and number of Nobel laureates for different countries.

The correlation between per-capita chocolate consumption and number of Nobel laureates is about 0.36. What can we safely conclude?

- **Options:**

  A) There is a positive association between chocolate consumption and Nobel prizes (ignoring 'significance')
  B) There is a negative association between chocolate consumption and Nobel prizes
  C) Chocolate makes you smart
  D) Smartness makes chocolate

- **Answer (tutor only):** A
- **Explanation (tutor only):** A positive correlation means countries that eat more chocolate tend to have more laureates. That's all we can say: country wealth (and population) could drive both.
- **Why the wrong options are wrong (tutor only):**
  B) r > 0 means a positive association.
  C) and D) Causal claims (in opposite directions) that correlational data can't distinguish, and a confounder like wealth is a likely explanation.
- **Hint:** Which answer only describes the pattern?

### ch07-hw-04-v1
- **Kind:** AI-written version of ch07-hw-04
- **Concepts:** Association vs causation
- **Type:** MC
- **Question:**

Across cities, ice-cream sales and drowning deaths have a correlation of 0.7. What can we safely conclude?

- **Options:**

  A) There's a positive association between ice-cream sales and drownings
  B) Ice cream causes drowning
  C) Drowning causes ice-cream sales
  D) There's no relationship

- **Answer (tutor only):** A
- **Explanation (tutor only):** The data show an association. Hot weather plausibly drives both (a confounder).
- **Why the wrong options are wrong (tutor only):**
  B) and C) Causal claims from correlation.
  D) r = 0.7 is a clear association.
- **Hint:** What else rises in summer?

### ch07-hw-04-v2
- **Kind:** AI-written version of ch07-hw-04
- **Concepts:** Association vs causation
- **Type:** MC
- **Question:**

A correlation of −0.5 between hours of screen time and sleep quality means:

- **Options:**

  A) People with more screen time tend to report worse sleep
  B) Screen time causes bad sleep
  C) Half of people sleep badly
  D) There's no relationship

- **Answer (tutor only):** A
- **Explanation (tutor only):** A negative correlation means that as one goes up, the other tends to go down. It doesn't establish cause.
- **Why the wrong options are wrong (tutor only):**
  B) Causal.
  C) r isn't a proportion of people.
  D) −0.5 is a moderate association.
- **Hint:** What does the sign mean?

### ch07-hw-05
- **Kind:** Course original
- **Concepts:** Correlation
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch07-hw-fourpanels.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch07-hw-fourpanels.png)
- **Question:**

Consider the four scatterplots (a–d). In which panel:

1. are x and y most tightly associated?
2. are x and y most tightly linearly associated?
3. do x and y have the most positive correlation coefficient?
4. do x and y have the largest correlation in absolute value (|r|)?
5. does x do the worst job of predicting y?

- **Options:**

  A) a
  B) b
  C) c
  D) d

- **Answer (tutor only):** 1-B, 2-C, 3-D, 4-C, 5-A
- **Explanation (tutor only):** 1. b: y is a perfect (but wavy, nonlinear) function of x, so knowing x tells you y exactly. 2. c: the points hug a straight line most closely. 3. d: the only clearly positive relationship. 4. c: its r is strongly negative (about −0.9), so it has the largest magnitude even though it's the smallest number. b's r is near zero despite the perfect relationship, because r only measures linear association. 5. a: a cloud of points with no pattern.
- **Why the wrong options are wrong (tutor only):**
  b for any correlation question: r only captures straight-line relationships, so a sine wave has r near 0.
  Mixing up 3 and 4: the sign of r gives the direction, and |r| gives the strength of the linear association.
- **Hint:** Correlation measures linear association only, and its sign matters for 'largest.'

### ch07-hw-05-v1
- **Kind:** AI-written version of ch07-hw-05
- **Concepts:** Correlation
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch07-var-fourpanels.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch07-var-fourpanels.png)
- **Question:**

Consider the four scatterplots (a–d). In which panel:

1. is there a strong but clearly nonlinear relationship?
2. are x and y most tightly linearly associated?
3. is the correlation the most positive?
4. does x do the worst job of predicting y?

- **Options:**

  A) a
  B) b
  C) c
  D) d

- **Answer (tutor only):** 1-B, 2-A, 3-C, 4-D
- **Explanation (tutor only):** b is an arch: y depends strongly on x, but r ≈ 0.07. a hugs a falling line (r ≈ −0.96, the largest |r|). c has the most positive r (≈ 0.68). d is a weak cloud (r ≈ 0.28).
- **Why the wrong options are wrong (tutor only):**
  r only measures straight-line association, and its sign matters for 'most positive'.
- **Hint:** Look at shape, tightness and direction separately.

### ch07-hw-05-v2
- **Kind:** AI-written version of ch07-hw-05
- **Concepts:** Correlation
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch07-var-fourpanels.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch07-var-fourpanels.png)
- **Question:**

In panel b, y is closely predicted by x (an arch shape), but r ≈ 0.07. Why?

- **Options:**

  A) Correlation only measures linear association; the rising and falling halves cancel out
  B) The data must be wrong
  C) There's no relationship between x and y
  D) The sample is too small

- **Answer (tutor only):** A
- **Explanation (tutor only):** A straight line can't describe an arch, so r is near zero even though the relationship is strong.
- **Why the wrong options are wrong (tutor only):**
  B) The data are fine.
  C) There's a strong (nonlinear) relationship.
  D) Sample size isn't the issue.
- **Hint:** Can a straight line fit an arch?

### ch07-hw-06
- **Kind:** Course original
- **Concepts:** Correlation; Association vs causation
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch07-hw-choc-nobel-scatter.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch07-hw-choc-nobel-scatter.png)
- **Question:**

Across 27 countries, the correlation between chocolate consumption and number of Nobel laureates is r ≈ 0.36 (see the scatterplot). If we remove just three countries (the USA, the UK and Germany), the correlation among the remaining 24 drops to r ≈ −0.06. What does this tell us?

- **Options:**

  A) The association is driven by a few extreme countries; for most countries there is essentially no linear association
  B) Removing data always lowers the correlation, so this tells us nothing
  C) Those three countries are errors and should be deleted
  D) Chocolate causes Nobel prizes only in large countries

- **Answer (tutor only):** A
- **Explanation (tutor only):** Correlation is sensitive to extreme points: three countries with huge laureate counts (which also eat a lot of chocolate) create the whole pattern. Among the other 24, r is about 0. Also note these are raw counts, not per capita, so big, rich countries dominate. Always look at the plot before trusting an r.
- **Why the wrong options are wrong (tutor only):**
  B) Removing points can raise, lower or not change r. Here it changed it a lot, which is informative.
  C) They're real data; you can report results with and without them, but you don't delete them for being inconvenient.
  D) A causal claim the data can't support.
- **Hint:** Look at the scatterplot. Where would the line go without the three labeled points?

### ch07-hw-06-v1
- **Kind:** AI-written version of ch07-hw-06
- **Concepts:** Correlation
- **Type:** MC
- **Question:**

Across 30 lakes, fish species richness and lake area have r = 0.55. Removing the single largest lake drops r to 0.05. What does this tell you?

- **Options:**

  A) One extreme lake drives the correlation; among the other lakes there's little linear association
  B) Removing data always lowers r
  C) The largest lake must be a data error and should be deleted
  D) Big lakes cause more species only above a certain size

- **Answer (tutor only):** A
- **Explanation (tutor only):** Correlation is sensitive to extreme points. Report results with and without the influential point, and look at the plot.
- **Why the wrong options are wrong (tutor only):**
  B) Removing points can raise or lower r.
  C) Real data shouldn't be deleted just for being influential.
  D) One point can't establish that.
- **Hint:** How much is one point doing?

### ch07-hw-06-v2
- **Kind:** AI-written version of ch07-hw-06
- **Concepts:** Correlation
- **Type:** MC
- **Question:**

Why should you always plot data before trusting a correlation coefficient?

- **Options:**

  A) One or two extreme points, or a curved pattern, can make r misleading
  B) Plots are required for r to be calculated
  C) r is always wrong
  D) Plots make r larger

- **Answer (tutor only):** A
- **Explanation (tutor only):** Very different patterns can share the same r (e.g., Anscombe's quartet). The plot shows whether r describes the data well.
- **Why the wrong options are wrong (tutor only):**
  B) R calculates r without a plot.
  C) r is correct as a number; it just may not describe the pattern well.
  D) Plotting doesn't change r.
- **Hint:** Can very different scatterplots have the same r?

## Chapter 8: Sampling

### ch08-book-01
- **Kind:** Course original
- **Concepts:** SD vs SE
- **Type:** matching
- **Question:**

1. The ____ describes the variability among individual observations in a sample (or population). It quantifies how far we expect individuals to deviate from the sample estimate.
2. The ____ describes the variability among estimates (of a fixed sample size) from a population. It quantifies how far we expect sample estimates to deviate from the population parameter.

- **Options:**

  A) standard error
  B) standard deviation
  C) error function

- **Answer (tutor only):** 1-B, 2-A
- **Explanation (tutor only):** SD: spread of individuals. SE: spread of estimates (the SD of the sampling distribution).
- **Why the wrong options are wrong (tutor only):**
  C) isn't a term we use here.
- **Hint:** Individuals → SD. Estimates → SE.

### ch08-book-01-v1
- **Kind:** AI-written version of ch08-book-01
- **Concepts:** SD vs SE
- **Type:** matching
- **Question:**

1. If you measured more and more individuals, which would settle near a fixed value (not shrink)?
2. Which would keep getting smaller as you added more individuals to your sample?

- **Options:**

  A) standard error of the mean
  B) standard deviation

- **Answer (tutor only):** 1-B, 2-A
- **Explanation (tutor only):** The SD estimates a property of the population (how variable individuals are), so it settles down. The SE ≈ SD/√n keeps shrinking as n grows.
- **Why the wrong options are wrong (tutor only):**
  Bigger samples make the SD more precise, not smaller.
- **Hint:** Would individuals become more similar if you measured more of them?

### ch08-book-01-v2
- **Kind:** AI-written version of ch08-book-01
- **Concepts:** SD vs SE
- **Type:** MC
- **Question:**

Which statement is correct?

- **Options:**

  A) The SE describes how much sample means vary; the SD describes how much individuals vary
  B) The SE and SD are two names for the same thing
  C) The SE is always larger than the SD
  D) The SD shrinks as sample size increases; the SE doesn't

- **Answer (tutor only):** A
- **Explanation (tutor only):** SD: spread among individuals. SE: spread among estimates (for a given n). Since SE ≈ SD/√n, the SE is smaller than the SD whenever n > 1.
- **Why the wrong options are wrong (tutor only):**
  B) They measure different things.
  C) It's smaller, not larger.
  D) That's backwards.
- **Hint:** Individuals or estimates?

### ch08-book-02
- **Kind:** Course original
- **Concepts:** Samples, populations & estimates; Shape of distributions
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-book-gene-lengths.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-book-gene-lengths.png)
- **Question:**

The histogram shows the lengths of all ~20,000 human genes (the whole population). The mean is 2.62 kb, the median is 2.23 kb, and the SD is 2.04 kb.

Which statements are correct? (Select all that apply.)

- **Options:**

  A) The distribution is unimodal
  B) The distribution is bimodal
  C) The distribution is symmetric
  D) The distribution is right skewed
  E) The histogram displays the population distribution
  F) The histogram displays a sampling distribution

- **Answer (tutor only):** A, D, E
- **Explanation (tutor only):** One peak near 1–2 kb with a long tail of very long genes: unimodal and right skewed (that's why the mean, 2.62, is above the median, 2.23). It shows every gene, i.e., individuals in the whole population, so it's the population distribution.
- **Why the wrong options are wrong (tutor only):**
  B) One peak.
  C) The right tail is much longer.
  F) A sampling distribution would show estimates (e.g., means of many samples), not individual genes.
- **Hint:** Individuals or estimates? And which way does the long tail go?

### ch08-book-02-v1
- **Kind:** AI-written version of ch08-book-02
- **Concepts:** Samples, populations & estimates; Shape of distributions
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-ripen-pop.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-ripen-pop.png)
- **Question:**

The histogram shows the day of the year that fruit ripened on each of 5,000 plants in a population (all of them were measured). Which statements are correct? (Select all that apply.)

- **Options:**

  A) The distribution is unimodal
  B) The distribution is bimodal
  C) The distribution is left skewed
  D) The distribution is right skewed
  E) The histogram displays the population distribution
  F) The histogram displays a sampling distribution

- **Answer (tutor only):** A, C, E
- **Explanation (tutor only):** One peak near day 114 with a long tail toward earlier days: unimodal and left skewed (so the mean, 108, is below the median, 110). It shows every individual plant, so it's the population distribution.
- **Why the wrong options are wrong (tutor only):**
  B) One peak.
  D) The long tail is on the left.
  F) A sampling distribution would show estimates from many samples, not individual plants.
- **Hint:** Which way does the long tail point? And is each value a plant or an estimate?

### ch08-book-02-v2
- **Kind:** AI-written version of ch08-book-02
- **Concepts:** Sampling distribution; Shape of distributions
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-ripen-means.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-ripen-means.png)
- **Question:**

From the same population of 5,000 plants (whose ripening days are left skewed), I drew 1,000 random samples of 40 plants and recorded the mean ripening day of each. The histogram shows those 1,000 means. Which statements are correct? (Select all that apply.)

- **Options:**

  A) The distribution is unimodal and roughly symmetric
  B) The distribution is strongly left skewed, like the population
  C) The histogram displays a sampling distribution
  D) The histogram displays the population distribution
  E) It is much narrower than the population distribution

- **Answer (tutor only):** A, C, E
- **Explanation (tutor only):** Means of 40 plants smooth out the skew of individuals, so the sampling distribution is roughly symmetric (a preview of the central limit theorem). It's a distribution of estimates, and it's far narrower: means range from about 104 to 112, while individuals range from about 55 to 120.
- **Why the wrong options are wrong (tutor only):**
  B) Averaging removes most of the skew.
  D) Each value is a mean of 40 plants, not one plant.
- **Hint:** Is each value one plant, or a mean of 40?

### ch08-book-03
- **Kind:** Course original
- **Concepts:** Sampling error vs bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-book-biased-sampdist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-book-biased-sampdist.png)
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

### ch08-book-03-v1
- **Kind:** AI-written version of ch08-book-03
- **Concepts:** Sampling error vs bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-family-biased.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-family-biased.png)
- **Question:**

To estimate the mean number of children per family in a town, I asked 40 randomly chosen high-school students how many children are in their family (counting themselves), and averaged their answers. I repeated this 1000 times. The plot shows my 1000 estimates; the red line is the true mean number of children per family with children (2.56).

The difference between the true mean and my estimates is most likely explained by:

- **Options:**

  A) Sampling bias
  B) Non-independence
  C) Sampling error
  D) Too few repetitions

- **Answer (tutor only):** A
- **Explanation (tutor only):** Nearly all 1000 estimates are above 2.56: a systematic shift. Families with more children have more students to be asked, so big families are oversampled (size-biased sampling). Sampling error would scatter estimates on both sides of the truth.
- **Why the wrong options are wrong (tutor only):**
  B) Non-independence would widen the spread, not shift it.
  C) Chance would put estimates on both sides of the line.
  D) More repetitions would show the same shift.
- **Hint:** Are the estimates scattered around the truth, or all off in one direction?

### ch08-book-03-v2
- **Kind:** AI-written version of ch08-book-03
- **Concepts:** Sampling error vs bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-trout-unbiased.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-trout-unbiased.png)
- **Question:**

A hatchery pond holds thousands of trout with a true mean length of 31.0 cm. A technician nets 25 fish at random, measures them, and returns them, and does this 1000 times. The plot shows the 1000 estimated means (red line = true mean).

The individual estimates range from about 27 to 34.5 cm. This spread is best explained by:

- **Options:**

  A) Sampling error
  B) Sampling bias
  C) Non-independence
  D) Measurement error

- **Answer (tutor only):** A
- **Explanation (tutor only):** The estimates are scattered evenly on both sides of the true mean, as expected from chance differences among random samples. There's no systematic shift, so no bias.
- **Why the wrong options are wrong (tutor only):**
  B) Bias would shift the whole histogram away from the red line.
  C) Nothing suggests related fish.
  D) Even perfect measurements would give this spread, because each net catches different fish.
- **Hint:** Is the histogram centered on the red line?

### ch08-book-04
- **Kind:** Course original
- **Concepts:** Sampling error vs bias
- **Type:** MC
- **Question:**

I estimated mean human gene length by randomly choosing nucleotides from the genome and recording the length of the gene each one fell in. My estimates (about 4 kb) were far above the true mean (2.62 kb). Why, and how could I fix it?

- **Options:**

  A) Long genes contain more nucleotides, so they were more likely to be hit. Fix: randomly sample genes from a list of all genes, giving each gene an equal chance
  B) My sample of 50 was too small. Fix: sample 5000 genes the same way
  C) Nucleotides near each other are non-independent. Fix: sample nucleotides farther apart
  D) Bad luck. Fix: repeat the experiment

- **Answer (tutor only):** A
- **Explanation (tutor only):** Picking random nucleotides is size-biased sampling: a 20 kb gene is ten times as likely to be picked as a 2 kb gene. Each gene needs an equal chance of being chosen. It's the same issue as picking random times of day for Old Faithful.
- **Why the wrong options are wrong (tutor only):**
  B) A bigger biased sample is still biased, just more precisely wrong.
  C) Spacing doesn't change the length-based selection.
  D) 1000 repeats were all too high; that's not luck.
- **Hint:** Does every gene have the same chance of being in the sample?

### ch08-book-04-v1
- **Kind:** AI-written version of ch08-book-04
- **Concepts:** Sampling error vs bias
- **Type:** MC
- **Question:**

I estimated the mean number of children per family by surveying random high-school students about their own families. My estimate (3.2) was well above the true mean (2.6). Why, and how could I fix it?

- **Options:**

  A) Families with more children have more students who could be picked, so big families were oversampled. Fix: randomly sample families (e.g., households), not students
  B) My sample was too small. Fix: survey more students the same way
  C) Students are bad at counting siblings. Fix: check birth records
  D) Bad luck. Fix: repeat the survey

- **Answer (tutor only):** A
- **Explanation (tutor only):** Sampling students gives each family a chance proportional to its number of children: size-biased sampling, like random nucleotides oversampling long genes. Each family needs an equal chance.
- **Why the wrong options are wrong (tutor only):**
  B) A bigger biased sample is still biased.
  C) Even perfect counting gives the same bias.
  D) Repeating gives the same systematic error.
- **Hint:** Does every family have the same chance of being in the sample?

### ch08-book-04-v2
- **Kind:** AI-written version of ch08-book-04
- **Concepts:** Sampling error vs bias
- **Type:** MC
- **Question:**

To estimate mean group size of wild horses, researchers flew over the range and photographed a random spot, recording the size of the group closest to that spot. Estimates were consistently larger than the true mean group size. Why?

- **Options:**

  A) Large groups cover more ground, so they're more likely to be nearest a random spot: big groups are oversampled
  B) Horses move, so photos are blurry
  C) The flights were too short
  D) The researchers made arithmetic errors

- **Answer (tutor only):** A
- **Explanation (tutor only):** Like random nucleotides landing in long genes, random spots are more likely to land near big groups. That's size-biased sampling. Fix: sample groups with equal probability, e.g., list all groups and pick at random.
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) None of these would push estimates consistently upward.
- **Hint:** Which groups are easiest to 'hit' with a random spot?

### ch08-book-05
- **Kind:** Course original
- **Concepts:** Samples, populations & estimates; Sampling distribution
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-book-gene-lengths.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-book-gene-lengths.png), [ch08-book-biased-sampdist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-book-biased-sampdist.png)
- **Question:**

Gene lengths in the human genome range from under 1 kb to over 20 kb, but the 1000 sample means (n = 50 each) all fall between about 3 and 7 kb. Why is the range of the sample means so much smaller than the range of individual gene lengths?

- **Options:**

  A) Sampling bias
  B) Non-independence
  C) Sampling error
  D) Parameter estimates usually have a tighter distribution than individual observed values

- **Answer (tutor only):** D
- **Explanation (tutor only):** Averaging 50 genes cancels out extremes: one huge gene gets diluted by 49 others. So means vary much less than individuals (SE = SD/√n).
- **Why the wrong options are wrong (tutor only):**
  A) Bias shifts the center; it doesn't explain narrowness.
  B) Non-independence would widen, not narrow.
  C) Sampling error is the spread we're looking at, not its cause.
- **Hint:** What happens to an extreme value when you average it with 49 others?

### ch08-book-05-v1
- **Kind:** AI-written version of ch08-book-05
- **Concepts:** Samples, populations & estimates; Sampling distribution
- **Type:** MC
- **Question:**

Individual oak heights range from about 6 to 30 m, but means of random samples of 64 oaks all fall between about 16.5 and 19.5 m. Why is the range of the means so much smaller?

- **Options:**

  A) Averaging many trees cancels out extremes, so estimates vary much less than individuals
  B) Sampling bias
  C) Non-independence
  D) The samples of 64 must have excluded the tallest and shortest trees

- **Answer (tutor only):** A
- **Explanation (tutor only):** One very tall tree in a sample of 64 is diluted by 63 others. That's why SE = SD/√n is much smaller than the SD.
- **Why the wrong options are wrong (tutor only):**
  B) Bias would shift the center, not narrow the spread.
  C) Non-independence would widen, not narrow.
  D) Random samples include extreme trees; they just don't dominate the mean.
- **Hint:** What happens to one extreme value when averaged with 63 others?

### ch08-book-05-v2
- **Kind:** AI-written version of ch08-book-05
- **Concepts:** Samples, populations & estimates; Sampling distribution
- **Type:** MC
- **Question:**

Which will be more spread out?

- **Options:**

  A) Heights of 1,000 individual students
  B) Mean heights of 1,000 random samples of 25 students
  C) They'll be equally spread out
  D) It depends on whether the population is skewed

- **Answer (tutor only):** A
- **Explanation (tutor only):** Individuals vary the most. Means of 25 vary about 1/√25 = 1/5 as much (SE = SD/√n), whatever the shape of the population.
- **Why the wrong options are wrong (tutor only):**
  B) Means are less variable than individuals.
  C) and D) Averaging always reduces spread.
- **Hint:** Do means vary more or less than individuals?

### ch08-book-06
- **Kind:** Course original
- **Concepts:** SD vs SE; Sampling error vs bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-book-sampdist-n.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-book-sampdist-n.png)
- **Question:**

The plot shows sampling distributions of mean human gene length from 1000 random samples each of n = 5, 30 and 500 genes (red line = true mean). What explains the difference between the panels, and which n has the smallest standard error?

- **Options:**

  A) Less sampling error in larger samples; n = 500 has the smallest SE
  B) Less sampling bias in larger samples; n = 500 has the smallest SE
  C) Less non-independence in larger samples; n = 5 has the smallest SE
  D) Less sampling error in larger samples; they all have about the same SE

- **Answer (tutor only):** A
- **Explanation (tutor only):** All three are centered on the truth (no bias). They get narrower as n increases. The SEs computed from the data are about 1.04 kb (n = 5), 0.37 (n = 30) and 0.09 (n = 500).
- **Why the wrong options are wrong (tutor only):**
  B) None of the three is biased; they're all centered on the red line.
  C) Sample size doesn't change independence.
  D) The widths clearly differ.
- **Hint:** Center = bias; width = sampling error / SE.

### ch08-book-06-v1
- **Kind:** AI-written version of ch08-book-06
- **Concepts:** SD vs SE; Sampling error vs bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-pink-sampdist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-pink-sampdist.png)
- **Question:**

In a large Clarkia population, 30% of plants have pink flowers. The plot shows the sampling distributions of the proportion of pink plants in random samples of n = 10, 40 and 160 plants (red line = true proportion, 0.30).

What explains the difference between the panels, and which n has the smallest standard error?

- **Options:**

  A) Less sampling error in larger samples; n = 160 has the smallest SE
  B) Less sampling bias in larger samples; n = 160 has the smallest SE
  C) Less non-independence in larger samples; n = 10 has the smallest SE
  D) Less sampling error in larger samples; they all have about the same SE

- **Answer (tutor only):** A
- **Explanation (tutor only):** All three are centered on 0.30 (no bias) and get narrower as n increases. SE = √(0.3 × 0.7 / n): about 0.145, 0.072 and 0.036.
- **Why the wrong options are wrong (tutor only):**
  B) None is biased.
  C) Sample size doesn't change independence; n = 10 has the largest SE.
  D) The widths clearly differ.
- **Hint:** Center = bias; width = sampling error / SE.

### ch08-book-06-v2
- **Kind:** AI-written version of ch08-book-06
- **Concepts:** SD vs SE; Sampling error vs bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-oak-sampdist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-oak-sampdist.png)
- **Question:**

Imagine we could measure every one of the 8,000 red oaks in a forest: their mean height is 18.0 m and the SD is 4.0 m. The plot shows sampling distributions of the mean height for random samples of n = 4, 16 and 64 trees (each panel is a histogram of 10,000 sample means; red line = true mean).

Going from n = 16 to n = 64 (four times as many trees), what happens to the standard error?

- **Options:**

  A) It halves (from about 1 m to about 0.5 m)
  B) It shrinks to a quarter
  C) It stays the same
  D) It doubles

- **Answer (tutor only):** A
- **Explanation (tutor only):** SE = SD/√n. Quadrupling n doubles √n, so the SE halves: 4/√16 = 1 m, 4/√64 = 0.5 m. You can see the n = 64 panel is about half as wide as n = 16.
- **Why the wrong options are wrong (tutor only):**
  B) That would need 16 times the sample.
  C) The SE depends on n.
  D) Larger samples reduce the SE.
- **Hint:** SE = SD / √n. What happens to √n when n quadruples?

### ch08-book-07
- **Kind:** Course original
- **Concepts:** Sampling distribution; SD vs SE
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-book-sampdist-n.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-book-sampdist-n.png)
- **Question:**

The plot shows sampling distributions of mean gene length (n = 5 and n = 500; true mean 2.62 kb). Approximately what proportion of sample means are:

1. greater than the population mean, for n = 5?
2. greater than the population mean, for n = 500?
3. greater than 3.8 kb, for n = 5?
4. greater than 3.8 kb, for n = 500?

- **Options:**

  A) way less than 0.01
  B) about 0.10
  C) about 0.50

- **Answer (tutor only):** 1-C, 2-C, 3-B, 4-A
- **Explanation (tutor only):** Both distributions are centered on the truth, so about half fall above it (from the data: 0.44 for n = 5 and 0.46 for n = 500; a bit under half because the right-skewed population makes small-sample means slightly right skewed). Only the wide n = 5 distribution reaches 3.8 kb: 8% of n = 5 means vs 0% of n = 500 means.
- **Why the wrong options are wrong (tutor only):**
  Being centered on the truth doesn't depend on n; reaching far from the truth does.
- **Hint:** Find the red line, then find 3.8 on the x-axis.

### ch08-book-07-v1
- **Kind:** AI-written version of ch08-book-07
- **Concepts:** Sampling distribution; SD vs SE
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-oak-sampdist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-oak-sampdist.png)
- **Question:**

Imagine we could measure every one of the 8,000 red oaks in a forest: their mean height is 18.0 m and the SD is 4.0 m. The plot shows sampling distributions of the mean height for random samples of n = 4, 16 and 64 trees (each panel is a histogram of 10,000 sample means; red line = true mean).

Approximately what proportion of sample means are:

1. greater than 18 m, for n = 4?
2. greater than 18 m, for n = 64?
3. greater than 20 m, for n = 4?
4. greater than 20 m, for n = 64?

- **Options:**

  A) way less than 0.01
  B) about 0.16
  C) about 0.50

- **Answer (tutor only):** 1-C, 2-C, 3-B, 4-A
- **Explanation (tutor only):** Both are centered on 18 m, so about half are above it regardless of n. Only the wide n = 4 distribution reaches 20 m often (about 16%); for n = 64 a mean of 20 m is 4 SEs away and essentially never happens.
- **Why the wrong options are wrong (tutor only):**
  Being centered on the truth doesn't depend on n; reaching far from it does.
- **Hint:** Find the red line, then find 20 m in each panel.

### ch08-book-07-v2
- **Kind:** AI-written version of ch08-book-07
- **Concepts:** Sampling distribution; SD vs SE
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-trout-unbiased.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-trout-unbiased.png)
- **Question:**

A hatchery pond holds thousands of trout with a true mean length of 31.0 cm. A technician nets 25 fish at random, measures them, and returns them, and does this 1000 times. The plot shows the 1000 estimated means (red line = true mean).

If the technician had netted 100 fish each time instead of 25, how would the histogram change?

- **Options:**

  A) Still centered on 31 cm, but about half as wide
  B) Shifted closer to 31 cm
  C) Centered on 31 cm and the same width
  D) About a quarter as wide

- **Answer (tutor only):** A
- **Explanation (tutor only):** Random samples stay centered on the truth. The SE scales with 1/√n, so 4 times the fish makes it 1/2 as wide.
- **Why the wrong options are wrong (tutor only):**
  B) It's already centered on 31 cm.
  C) Larger samples reduce the spread.
  D) That would take 16 times the fish.
- **Hint:** SE = SD / √n.

### ch08-book-08
- **Kind:** Course original
- **Concepts:** Samples, populations & estimates; SD vs SE
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-book-gene-lengths.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-book-gene-lengths.png)
- **Question:**

The histogram shows the lengths of all ~20,000 human genes (the whole population). The mean is 2.62 kb, the median is 2.23 kb, and the SD is 2.04 kb.

What is the standard error of the mean gene length here?

- **Options:**

  A) There is none: this is the entire population, so 2.62 kb is the parameter itself, known without sampling error
  B) 2.04 kb, the SD
  C) 2.04 / √20,290 ≈ 0.014 kb
  D) 2.62 / √20,290

- **Answer (tutor only):** A
- **Explanation (tutor only):** An SE describes how much an estimate would vary across samples. We measured every gene, so there's no sample, no sampling error, and no SE: the mean is the parameter.
- **Why the wrong options are wrong (tutor only):**
  B) That's the SD among genes.
  C) That's what you'd compute if these 20,290 genes were a sample from a larger population, which they aren't.
  D) Wrong formula, and it doesn't apply here anyway.
- **Hint:** Is this a sample or the whole population?

### ch08-book-08-v1
- **Kind:** AI-written version of ch08-book-08
- **Concepts:** Samples, populations & estimates; SD vs SE
- **Type:** MC
- **Question:**

A national park counts every one of its 412 bighorn sheep from the air and finds the mean group size is 7.3. What is the standard error of this mean?

- **Options:**

  A) There is none: every sheep in the population was counted, so 7.3 is the parameter
  B) The SD of group sizes
  C) The SD of group sizes divided by √412
  D) 7.3 / √412

- **Answer (tutor only):** A
- **Explanation (tutor only):** An SE describes how much an estimate would vary across samples. A complete census has no sampling, so no sampling error and no SE (though counting mistakes are still possible).
- **Why the wrong options are wrong (tutor only):**
  B) That's the spread among groups.
  C) That would apply if these 412 were a sample from a larger population.
  D) The wrong formula, and it doesn't apply anyway.
- **Hint:** Is this a sample or the whole population?

### ch08-book-08-v2
- **Kind:** AI-written version of ch08-book-08
- **Concepts:** Samples, populations & estimates; SD vs SE
- **Type:** MC
- **Question:**

A teacher calculates the mean exam score of all 28 students in her class: 81.5. She only cares about this class. Should she report a standard error?

- **Options:**

  A) No: she measured the whole population she cares about, so 81.5 is the parameter
  B) Yes: every mean needs a standard error
  C) Yes, because 28 is a small number
  D) Only if the scores are normally distributed

- **Answer (tutor only):** A
- **Explanation (tutor only):** Whether something is a population depends on the question. If the class is the population of interest, the mean is known exactly. If she wanted to generalize to future classes, then this class would be a sample and an SE would make sense.
- **Why the wrong options are wrong (tutor only):**
  B) SEs describe sampling error; no sampling, no SE.
  C) Small populations are still populations.
  D) Shape doesn't matter here.
- **Hint:** Is she sampling, or did she measure everyone she cares about?

### ch08-gquiz-01
- **Kind:** Course original
- **Concepts:** SD vs SE; Sampling error vs bias
- **Type:** MC
- **Question:**

In class, students sampled 10 crayons (without replacement) from a bin and reported the number that were red, using a Google form.

Because it would take too long, only one person per group sampled crayons. (Logistics often limit sample size.) This practice:

- **Options:**

  A) Increases sampling bias
  B) Increases sampling error
  C) Had no real impact on the outcome of sampling

- **Answer (tutor only):** B
- **Explanation (tutor only):** Fewer samples means fewer estimates and a smaller total sample, so there's more chance variation. Bias isn't affected, because each sample is still random.
- **Why the wrong options are wrong (tutor only):**
  A) Bias comes from how we sample, not how many.
  C) A smaller sample makes estimates noisier.
- **Hint:** Does sample size affect the center or the spread of the sampling distribution?

### ch08-gquiz-01-v1
- **Kind:** AI-written version of ch08-gquiz-01
- **Concepts:** SD vs SE; Sampling error vs bias
- **Type:** MC
- **Question:**

To save time, a field crew measures 5 randomly chosen lizards per site instead of 25. This practice:

- **Options:**

  A) Increases sampling bias
  B) Increases sampling error
  C) Has no real impact on the estimates

- **Answer (tutor only):** B
- **Explanation (tutor only):** Smaller random samples give noisier estimates (larger SE), but each sample is still random, so the estimate isn't systematically shifted.
- **Why the wrong options are wrong (tutor only):**
  A) Bias comes from how we sample, not how many.
  C) Fewer lizards means less precise means.
- **Hint:** Does sample size change the center or the spread of the sampling distribution?

### ch08-gquiz-01-v2
- **Kind:** AI-written version of ch08-gquiz-01
- **Concepts:** SD vs SE; Sampling error vs bias
- **Type:** MC
- **Question:**

Two students estimate the proportion of red crayons in the same bin. Ana draws 5 crayons at random; Ben draws 50 at random. Whose estimate is more likely to be far from the true proportion, and why?

- **Options:**

  A) Ana's, because small samples have more sampling error
  B) Ben's, because more crayons means more chances for mistakes
  C) Ana's, because small samples are biased
  D) Neither; both are random

- **Answer (tutor only):** A
- **Explanation (tutor only):** Both samples are random, so neither is biased. But Ana's 5 crayons can easily be all red or all blue by chance; Ben's 50 average out more of that luck.
- **Why the wrong options are wrong (tutor only):**
  B) More data reduces, not increases, chance error.
  C) Small random samples are noisy, not biased.
  D) Both are random, but they differ in precision.
- **Hint:** With 5 crayons, how likely is a very lopsided sample?

### ch08-gquiz-02
- **Kind:** Course original
- **Concepts:** Non-independence
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

### ch08-gquiz-02-v1
- **Kind:** AI-written version of ch08-gquiz-02
- **Concepts:** Non-independence
- **Type:** MC
- **Question:**

For a class survey of sleep hours, a teacher asks only one person per household to respond. Why?

- **Options:**

  A) To minimize sampling bias
  B) To minimize sampling error
  C) To minimize non-independence
  D) To reduce the number of responses

- **Answer (tutor only):** C
- **Explanation (tutor only):** People in the same household share routines (and noise!), so their sleep is more alike. Counting several per household would treat related observations as independent.
- **Why the wrong options are wrong (tutor only):**
  A) It doesn't systematically shift the estimate.
  B) Fewer responses would increase, not reduce, sampling error.
  D) That's a side effect, not the reason.
- **Hint:** Would two people from the same household be more alike than two random students?

### ch08-gquiz-02-v2
- **Kind:** AI-written version of ch08-gquiz-02
- **Concepts:** Non-independence
- **Type:** MC
- **Question:**

In a class activity, each table drew one sample of 10 crayons, but everyone at the table entered that same sample into the form, so 30 entries came from 6 samples. What's the problem?

- **Options:**

  A) The 30 entries aren't independent: the class really has only 6 independent samples
  B) The estimates are biased toward red
  C) There's no problem; more entries is always better
  D) The sample size per draw was too small

- **Answer (tutor only):** A
- **Explanation (tutor only):** Duplicate entries of one draw aren't new information. Treating them as 30 independent samples overstates how much data we have, making results look more precise than they are.
- **Why the wrong options are wrong (tutor only):**
  B) Duplicating samples doesn't shift the center.
  C) More entries only help if they're independent.
  D) That's a separate issue.
- **Hint:** How many independent draws were there?

### ch08-gquiz-04
- **Kind:** Course original
- **Concepts:** Samples, populations & estimates
- **Type:** matching
- **Question:**

In class, students sampled 10 crayons (without replacement) from a bin and reported the number that were red, using a Google form.

The number of red crayons in a sample of 10 is an (1) ____ of the true population (2) ____.

- **Options:**

  A) estimate
  B) parameter

- **Answer (tutor only):** 1-A, 2-B
- **Explanation (tutor only):** The count (or proportion) in your sample estimates the true proportion of red crayons in the whole bin, which is the parameter.
- **Why the wrong options are wrong (tutor only):**
  Parameters describe populations; estimates come from samples.
- **Hint:** Which one did you calculate?

### ch08-gquiz-04-v1
- **Kind:** AI-written version of ch08-gquiz-04
- **Concepts:** Samples, populations & estimates
- **Type:** matching
- **Question:**

A lake has thousands of perch. You catch 25 at random and 8 have parasites.

8/25 = 0.32 is our (1) ____ of the (2) ____: the true proportion of all perch in the lake with parasites.

- **Options:**

  A) estimate
  B) parameter

- **Answer (tutor only):** 1-A, 2-B
- **Explanation (tutor only):** 0.32 comes from the sample of 25, so it's an estimate. The true proportion for all perch in the lake is the parameter.
- **Why the wrong options are wrong (tutor only):**
  Parameters describe populations; estimates come from samples.
- **Hint:** Which one did you calculate?

### ch08-gquiz-04-v2
- **Kind:** AI-written version of ch08-gquiz-04
- **Concepts:** Samples, populations & estimates
- **Type:** MC
- **Question:**

Which of these is a parameter?

- **Options:**

  A) The mean height of all 1,204 students enrolled in a school
  B) The mean height of 30 randomly chosen students from that school
  C) The SD of heights among those 30 students
  D) The proportion of the 30 students taller than 170 cm

- **Answer (tutor only):** A
- **Explanation (tutor only):** A parameter describes the whole population. If the population is all 1,204 students, their true mean height is a parameter. Everything calculated from the 30 is an estimate.
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) All are calculated from a sample, so they're estimates.
- **Hint:** Which number describes everyone?

### ch08-gquiz-05
- **Kind:** Course original
- **Concepts:** Sampling distribution
- **Type:** MC
- **Question:**

In class, students sampled 10 crayons (without replacement) from a bin and reported the number that were red, using a Google form.

The distribution of sample estimates from this exercise (if we repeated it an infinite number of times) is the:

- **Options:**

  A) sampling distribution
  B) population distribution
  C) standard error
  D) sampling bias

- **Answer (tutor only):** A
- **Explanation (tutor only):** Many repeated samples → many estimates → their distribution is the sampling distribution.
- **Why the wrong options are wrong (tutor only):**
  B) The population distribution is the colors of all crayons in the bin.
  C) The SE is the spread (SD) of the sampling distribution, not the distribution itself.
  D) Bias would be a shift in its center.
- **Hint:** Distribution of estimates.

### ch08-gquiz-05-v1
- **Kind:** AI-written version of ch08-gquiz-05
- **Concepts:** Sampling distribution
- **Type:** MC
- **Question:**

Each of 200 students flips a coin 20 times and reports the proportion of heads. The distribution of those 200 proportions approximates the:

- **Options:**

  A) sampling distribution of the proportion
  B) population distribution
  C) standard error
  D) sampling bias

- **Answer (tutor only):** A
- **Explanation (tutor only):** Many samples of the same size (20 flips) → many estimates → their distribution approximates the sampling distribution.
- **Why the wrong options are wrong (tutor only):**
  B) The population distribution would be the outcomes of individual flips.
  C) The SE is the SD of this distribution, not the distribution itself.
  D) Bias would be a shift of its center away from the truth.
- **Hint:** Distribution of estimates.

### ch08-gquiz-05-v2
- **Kind:** AI-written version of ch08-gquiz-05
- **Concepts:** Sampling distribution; SD vs SE
- **Type:** MC
- **Question:**

In class, each student drew 10 crayons (without replacement) from a big bin of mixed colors and reported how many were red. We pooled everyone's results to estimate the proportion of red crayons in the bin. If we repeated this activity an enormous number of times and plotted the proportion red each time, what would the SD of that histogram be?

- **Options:**

  A) The standard error of the proportion red for samples of 10
  B) The standard deviation of crayon colors in the bin
  C) The sampling bias
  D) The true proportion of red crayons

- **Answer (tutor only):** A
- **Explanation (tutor only):** The histogram is the sampling distribution, and the SD of a sampling distribution is the standard error.
- **Why the wrong options are wrong (tutor only):**
  B) That describes individual crayons, not estimates.
  C) Bias is about the center, not the spread.
  D) The true proportion is where the histogram is centered.
- **Hint:** SE = the SD of what?

### ch08-gquiz-07
- **Kind:** Course original
- **Concepts:** Sampling distribution; SD vs SE
- **Type:** MC
- **Question:**

In class, students sampled 10 crayons (without replacement) from a bin and reported the number that were red, using a Google form.

How could you find the standard error of the proportion of red crayons in a sample of size ten from the bin?

- **Options:**

  A) Repeatedly draw samples of 10 crayons (returning them between samples), calculate the proportion red in each sample, and take the standard deviation of those proportions
  B) Draw one sample of 10 and calculate the standard deviation of crayon colors in it
  C) Count all the crayons in the bin and calculate the proportion red
  D) Draw one sample of 100 crayons instead of 10

- **Answer (tutor only):** A
- **Explanation (tutor only):** The SE is the SD of the sampling distribution, so build the sampling distribution: many samples of the same size (10), one estimate per sample, then the SD of the estimates.
- **Why the wrong options are wrong (tutor only):**
  B) That's (roughly) an SD among individuals, not among estimates.
  C) That gives the parameter, with no uncertainty to describe.
  D) That gives one estimate from a different sample size, not the SE for n = 10.
- **Hint:** SE = the SD of what?

### ch08-gquiz-07-v1
- **Kind:** AI-written version of ch08-gquiz-07
- **Concepts:** Sampling distribution; SD vs SE
- **Type:** MC
- **Question:**

A biologist wants the standard error of mean beak length for samples of 15 finches, and can catch as many finches as she likes. How could she find it directly?

- **Options:**

  A) Catch many separate samples of 15 finches, compute the mean of each, and take the SD of those means
  B) Catch one sample of 15 and compute the SD of beak lengths
  C) Catch one sample of 150 and compute its mean
  D) Measure every finch on the island

- **Answer (tutor only):** A
- **Explanation (tutor only):** The SE is the SD of the sampling distribution. Building it means many samples of the same size, one mean each, then the SD of those means.
- **Why the wrong options are wrong (tutor only):**
  B) That's the SD among individuals (though SD/√15 would approximate the SE).
  C) One mean, from a different n, says nothing about variation among means.
  D) That gives the parameter, with no sampling error to describe.
- **Hint:** SE = SD of many what?

### ch08-gquiz-07-v2
- **Kind:** AI-written version of ch08-gquiz-07
- **Concepts:** Sampling distribution; SD vs SE
- **Type:** MC
- **Question:**

You have one sample of 40 plants and can't go back for more. What's the best way to estimate the standard error of the mean?

- **Options:**

  A) Use the sample SD divided by √40 (or bootstrap the sample)
  B) Use the sample SD itself
  C) It's impossible without more samples
  D) Use the sample mean divided by √40

- **Answer (tutor only):** A
- **Explanation (tutor only):** With only one sample, we approximate the sampling distribution: either with the formula SE ≈ SD/√n or by resampling the data (bootstrap).
- **Why the wrong options are wrong (tutor only):**
  B) The SD describes individuals, not means.
  C) We can estimate it; we just can't observe it directly.
  D) The mean isn't a measure of spread.
- **Hint:** Means vary less than individuals by how much?

### ch08-hw-01
- **Kind:** Course original
- **Concepts:** Samples, populations & estimates
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

### ch08-hw-01-v1
- **Kind:** AI-written version of ch08-hw-01
- **Concepts:** Samples, populations & estimates
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

### ch08-hw-01-v2
- **Kind:** AI-written version of ch08-hw-01
- **Concepts:** Samples, populations & estimates
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

### ch08-hw-02
- **Kind:** Course original
- **Concepts:** Sampling distribution
- **Type:** MC
- **Question:**

The ____ describes the expected distribution of estimates we would get if we took estimates from many different samples of our population.

- **Options:**

  A) Sampling distribution
  B) Histogram
  C) Population distribution
  D) Sampling error

- **Answer (tutor only):** A
- **Explanation (tutor only):** A sampling distribution is a distribution of estimates (e.g., sample means), one from each of many hypothetical samples of the same size.
- **Why the wrong options are wrong (tutor only):**
  B) A histogram is a type of plot, not a concept.
  C) The population distribution is of individuals, not estimates.
  D) Sampling error is the chance difference between an estimate and the parameter; the sampling distribution shows its spread.
- **Hint:** Is this a distribution of individuals or of estimates?

### ch08-hw-02-v1
- **Kind:** AI-written version of ch08-hw-02
- **Concepts:** Sampling distribution
- **Type:** MC
- **Question:**

Many labs each measure 30 randomly chosen zebrafish and report the mean swimming speed. A histogram of all those reported means shows the:

- **Options:**

  A) Sampling distribution of the mean
  B) Population distribution of swimming speeds
  C) Standard deviation of swimming speed
  D) Sampling bias

- **Answer (tutor only):** A
- **Explanation (tutor only):** Each lab produced one estimate (a mean of 30 fish). A distribution of estimates from many samples of the same size is a sampling distribution.
- **Why the wrong options are wrong (tutor only):**
  B) The population distribution would show individual fish, not means of 30.
  C) The SD is a single number describing spread among individuals.
  D) Bias would be a shift of the means away from the truth, not the distribution itself.
- **Hint:** Is each value in the histogram an individual fish, or an estimate?

### ch08-hw-02-v2
- **Kind:** AI-written version of ch08-hw-02
- **Concepts:** Samples, populations & estimates; Sampling distribution
- **Type:** MC
- **Question:**

Which of these is a sampling distribution?

- **Options:**

  A) A histogram of the heights of all 600 trees in a forest plot
  B) A histogram of the means of 1,000 random samples of 10 trees each
  C) A histogram of the heights of 10 trees in one sample
  D) A bar chart of the number of trees of each species

- **Answer (tutor only):** B
- **Explanation (tutor only):** A sampling distribution is a distribution of estimates (here, means), one from each of many samples of the same size.
- **Why the wrong options are wrong (tutor only):**
  A) That's the population distribution of individual trees.
  C) That's the distribution of one sample.
  D) That summarizes a categorical variable for individuals.
- **Hint:** Look for a histogram of estimates, not of individuals.

### ch08-hw-03
- **Kind:** Course original
- **Concepts:** Sampling distribution
- **Type:** MC
- **Question:**

Understanding the sampling distribution is important for understanding statistics because…

- **Options:**

  A) It helps us think about other estimates we might have gotten from sampling
  B) It shows how individuals in the population are distributed
  C) It removes uncertainty from our estimates
  D) We often calculate it directly from a single dataset

- **Answer (tutor only):** A
- **Explanation (tutor only):** We only get one sample, but the sampling distribution shows the range of estimates we could have gotten. That is the basis for standard errors, confidence intervals and p-values.
- **Why the wrong options are wrong (tutor only):**
  B) That's the population distribution.
  C) It describes uncertainty; it doesn't remove it.
  D) We usually can't observe it directly; we estimate or approximate it (by resampling or math).
- **Hint:** It's about the estimates we didn't get.

### ch08-hw-03-v1
- **Kind:** AI-written version of ch08-hw-03
- **Concepts:** Sampling distribution
- **Type:** MC
- **Question:**

You measured one sample of 50 frogs and found a mean jump distance of 82 cm. Why should you care about the sampling distribution of the mean?

- **Options:**

  A) It tells you how much your 82 cm might differ from the truth, because a different sample of 50 would give a different mean
  B) It tells you how far an individual frog can jump
  C) It makes your 82 cm exactly correct
  D) You can read it directly off your one sample of 50 frogs

- **Answer (tutor only):** A
- **Explanation (tutor only):** The sampling distribution describes the other estimates you might have gotten. That's what lets us say how uncertain our one estimate is (SE, CI).
- **Why the wrong options are wrong (tutor only):**
  B) Individual variation is the population distribution.
  C) Nothing removes sampling error.
  D) We can approximate it (bootstrap, formulas), but one sample doesn't show it directly.
- **Hint:** Think about the estimates you didn't get.

### ch08-hw-03-v2
- **Kind:** AI-written version of ch08-hw-03
- **Concepts:** Sampling distribution
- **Type:** MC
- **Question:**

Two students each estimate the mean caffeine content of a coffee shop's lattes from separate random samples of 8 drinks. They get 142 mg and 155 mg. Which idea explains why they differ, and how much difference to expect?

- **Options:**

  A) The sampling distribution: estimates vary from sample to sample, and its spread tells us how much
  B) One of them must have made a measurement mistake
  C) The population distribution changed between their visits
  D) Sampling bias: one sample must be non-random

- **Answer (tutor only):** A
- **Explanation (tutor only):** Even with perfect measurements and random samples, different samples give different estimates. The sampling distribution describes that variation.
- **Why the wrong options are wrong (tutor only):**
  B) A difference doesn't require a mistake; chance alone produces it.
  C) Nothing suggests the lattes changed.
  D) Random samples still differ by chance; that's sampling error, not bias.
- **Hint:** Would two perfectly random samples give the same mean?

### ch08-hw-04
- **Kind:** Course original
- **Concepts:** SD vs SE
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

### ch08-hw-04-v1
- **Kind:** AI-written version of ch08-hw-04
- **Concepts:** SD vs SE
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

### ch08-hw-04-v2
- **Kind:** AI-written version of ch08-hw-04
- **Concepts:** SD vs SE
- **Type:** MC
- **Question:**

A paper reports: "mean body mass = 24.1 g (± 0.3 g, SE), n = 100 mice." What does the 0.3 g tell you?

- **Options:**

  A) How far a typical sample mean of 100 mice would be from the true mean
  B) How far a typical mouse is from the mean
  C) The difference between the heaviest and lightest mouse
  D) The measurement error of the scale

- **Answer (tutor only):** A
- **Explanation (tutor only):** A standard error describes the variability of an estimate (the mean of 100 mice). Individual mice vary much more: the SD here would be about 0.3 × √100 = 3 g.
- **Why the wrong options are wrong (tutor only):**
  B) That's the SD.
  C) That's the range.
  D) Measurement error is a different thing; the SE comes from sampling.
- **Hint:** SE = spread of what?

### ch08-hw-05
- **Kind:** Course original
- **Concepts:** SD vs SE; Sampling error vs bias
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

### ch08-hw-05-v1
- **Kind:** AI-written version of ch08-hw-05
- **Concepts:** SD vs SE; Sampling error vs bias
- **Type:** MC
- **Question:**

A lab estimates the mean seed mass of a weed from 15 randomly chosen plants. The estimate seems imprecise. What change would most reduce sampling error?

- **Options:**

  A) Weigh the seeds on a more precise scale
  B) Measure 150 randomly chosen plants instead of 15
  C) Choose the 15 healthiest-looking plants
  D) Nothing; sampling error can't be reduced

- **Answer (tutor only):** B
- **Explanation (tutor only):** Sampling error comes from which individuals happen to be in the sample. Larger random samples average over more individuals, so the SE shrinks (with √n).
- **Why the wrong options are wrong (tutor only):**
  A) Reduces measurement error, a different source of error.
  C) Non-random selection adds bias.
  D) It can't be eliminated, but it can be reduced.
- **Hint:** What makes a sampling distribution narrower?

### ch08-hw-05-v2
- **Kind:** AI-written version of ch08-hw-05
- **Concepts:** SD vs SE; Sampling error vs bias
- **Type:** MC
- **Question:**

A researcher doubles her sample size but keeps sampling only from plants near the road. What happens?

- **Options:**

  A) Sampling error decreases, but any bias from sampling only near the road remains
  B) Both sampling error and bias decrease
  C) Bias decreases, but sampling error stays the same
  D) Nothing changes

- **Answer (tutor only):** A
- **Explanation (tutor only):** A larger sample makes the estimate more precise (less sampling error), but if roadside plants differ from the rest, the estimate is still systematically off. A bigger biased sample is precisely wrong.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Sample size doesn't fix bias.
  D) Precision does improve.
- **Hint:** Does sampling more from the same place fix who's being sampled?

### ch08-hw-06
- **Kind:** Course original
- **Concepts:** Shape of distributions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-hw-faithful-eruptions.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-hw-faithful-eruptions.png)
- **Question:**

The histogram shows the lengths of eruptions of the Old Faithful geyser.

The distribution of eruption lengths is:

- **Options:**

  A) Unimodal & right skewed
  B) Unimodal & left skewed
  C) Unimodal & symmetric
  D) Bimodal

- **Answer (tutor only):** D
- **Explanation (tutor only):** Two clear peaks (around 2 and 4.5 minutes) with a valley between them: short and long eruptions.
- **Why the wrong options are wrong (tutor only):**
  A)–C) There are two humps, not one.
- **Hint:** Count the peaks.

### ch08-hw-06-v1
- **Kind:** AI-written version of ch08-hw-06
- **Concepts:** Shape of distributions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-visits-hist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-visits-hist.png)
- **Question:**

The histogram shows the number of pollinator visits to each of 400 plants. The distribution is:

- **Options:**

  A) Unimodal & right skewed
  B) Unimodal & left skewed
  C) Unimodal & symmetric
  D) Bimodal

- **Answer (tutor only):** A
- **Explanation (tutor only):** One peak at 0–2 visits, with a long tail stretching to the right (a few plants get 10+ visits). That's unimodal and right skewed, common for counts.
- **Why the wrong options are wrong (tutor only):**
  B) The long tail goes to the right, not the left.
  C) The two sides aren't mirror images.
  D) There's only one peak.
- **Hint:** Which side has the long tail?

### ch08-hw-06-v2
- **Kind:** AI-written version of ch08-hw-06
- **Concepts:** Shape of distributions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-oak-hist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-oak-hist.png)
- **Question:**

The histogram shows the heights of 600 trees. The distribution is:

- **Options:**

  A) Unimodal & right skewed
  B) Unimodal & left skewed
  C) Unimodal & symmetric
  D) Bimodal

- **Answer (tutor only):** C
- **Explanation (tutor only):** One peak near 18 m, falling off about equally on both sides: unimodal and roughly symmetric.
- **Why the wrong options are wrong (tutor only):**
  A) and B) Neither tail is clearly longer.
  D) There's one peak; small bumps are just noise.
- **Hint:** Would it look about the same flipped left to right?

### ch08-hw-07
- **Kind:** Course original
- **Concepts:** Sampling error vs bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-hw-faithful-eruptions.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-hw-faithful-eruptions.png)
- **Question:**

The histogram shows the lengths of eruptions of the Old Faithful geyser.

Which method would give an unbiased estimate of the mean eruption length per eruption (if we didn't already have the data)? (Hint: eruption length and time between eruptions are positively correlated.)

- **Options:**

  A) Randomly select eruptions, measure their lengths, and calculate the mean
  B) Randomly select eruptions, measure their lengths, and calculate the median
  C) Randomly select times of day, measure the length of the current or next eruption, and calculate the mean
  D) Randomly select times of day, measure the length of the current or next eruption, and calculate the median

- **Answer (tutor only):** A
- **Explanation (tutor only):** Every eruption should have an equal chance of being picked. If you pick random times of day, you are more likely to land in a long gap between eruptions, and long gaps go with long eruptions. That oversamples long eruptions: a size-biased sample. And the mean, not the median, estimates the mean.
- **Why the wrong options are wrong (tutor only):**
  B) and D) The median estimates the median, not the mean.
  C) Random times oversample eruptions that follow long gaps, which tend to be long eruptions.
- **Hint:** Does every eruption have the same chance of being chosen under each method?

### ch08-hw-07-v1
- **Kind:** AI-written version of ch08-hw-07
- **Concepts:** Sampling error vs bias
- **Type:** MC
- **Question:**

You want the mean length of time patients stay in a hospital. Which method gives an unbiased estimate?

- **Options:**

  A) Pick a random sample of patients from the year's admission records and average their stays
  B) Visit the wards on a random day and average the stays of the patients who are there
  C) Ask the first 50 patients discharged in January
  D) Visit the wards on several random days and average the stays of the patients there

- **Answer (tutor only):** A
- **Explanation (tutor only):** Every admission should have an equal chance of being picked. On any given day, the wards are full of long-stay patients (they're there for many days), so sampling whoever is present oversamples long stays: size-biased sampling.
- **Why the wrong options are wrong (tutor only):**
  B) and D) Long stays are more likely to be 'caught' on a random day, so the mean is biased upward; more days doesn't fix it.
  C) January discharges may not represent the whole year.
- **Hint:** Does every patient have the same chance of being included?

### ch08-hw-07-v2
- **Kind:** AI-written version of ch08-hw-07
- **Concepts:** Sampling error vs bias
- **Type:** MC
- **Question:**

To estimate the mean size of fish schools in a bay, a diver picks random fish and records the size of the school each fish belongs to. Why will this overestimate the mean school size?

- **Options:**

  A) Fish in big schools are more likely to be picked, so big schools are oversampled
  B) The diver's sample is too small
  C) Fish in the same school are non-independent, which increases sampling error but doesn't shift the mean
  D) It won't; picking random fish is random sampling of schools

- **Answer (tutor only):** A
- **Explanation (tutor only):** A school of 200 fish has 200 chances to be picked; a school of 5 has only 5. Sampling individuals gives schools probability proportional to their size, so the estimate is biased upward. Fix: sample schools, not fish.
- **Why the wrong options are wrong (tutor only):**
  B) More fish chosen the same way gives the same bias.
  C) True that they're related, but the main problem is the shift in the mean.
  D) Random fish ≠ random schools.
- **Hint:** Does every school have the same chance of being included?

### ch08-hw-08
- **Kind:** Course original
- **Concepts:** Non-independence
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-hw-faithful-eruptions.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-hw-faithful-eruptions.png)
- **Question:**

The histogram shows the lengths of eruptions of the Old Faithful geyser.

Which sampling technique would best minimize non-independence among observations? (Ignore any link between eruption length and waiting time.)

- **Options:**

  A) Sampling randomly across the day
  B) Sampling during a fixed block of time each day (e.g., 8 a.m.–noon)
  C) Sampling at regular, highly coordinated intervals (e.g., every hour on the hour)

- **Answer (tutor only):** A
- **Explanation (tutor only):** Eruptions close in time may be more similar to each other (and to conditions at that time of day). Random times spread observations out so that no shared timing links them.
- **Why the wrong options are wrong (tutor only):**
  B) Observations within the same block share conditions.
  C) Regular schedules can line up with cycles in the geyser (or the day), so observations aren't independent of each other.
- **Hint:** Which method keeps observations from sharing a common time-related cause?

### ch08-hw-08-v1
- **Kind:** AI-written version of ch08-hw-08
- **Concepts:** Non-independence
- **Type:** MC
- **Question:**

You want to estimate the average song rate of male wrens across a forest. Which sampling plan minimizes non-independence?

- **Options:**

  A) Record 30 males, each from a different randomly chosen territory spread across the forest
  B) Record one male 30 times
  C) Record 30 males that all sing from the same clearing
  D) Record 30 males on the same morning in the same weather

- **Answer (tutor only):** A
- **Explanation (tutor only):** Independent observations don't share anything that would make them more alike. Randomly chosen, spread-out territories avoid shared individuals, locations and conditions.
- **Why the wrong options are wrong (tutor only):**
  B) Repeated measures of one bird tell you about that bird, not the population.
  C) Birds in one clearing share habitat and may influence each other.
  D) Shared weather and time of day can make songs alike.
- **Hint:** What could make two of your observations more similar than two random birds?

### ch08-hw-08-v2
- **Kind:** AI-written version of ch08-hw-08
- **Concepts:** Non-independence
- **Type:** MC
- **Question:**

A student measures leaf toughness on 60 leaves. Which design gives the most independent observations?

- **Options:**

  A) 1 leaf from each of 60 randomly chosen plants
  B) 60 leaves from one plant
  C) 10 leaves from each of 6 plants
  D) 60 leaves from one branch of one plant

- **Answer (tutor only):** A
- **Explanation (tutor only):** Leaves on the same plant share genes and growing conditions, so they're more alike than leaves from different plants. One leaf per plant gives 60 independent observations.
- **Why the wrong options are wrong (tutor only):**
  B) and D) Effectively a sample size of one plant.
  C) Only 6 independent plants; the 10 leaves within each are related.
- **Hint:** How many truly independent units does each design give?

### ch08-hw-09
- **Kind:** Course original
- **Concepts:** Sampling distribution; Sampling error vs bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-hw-sampdist-n.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-hw-sampdist-n.png)
- **Question:**

The plot shows sampling distributions of the mean eruption length of Old Faithful for samples of size n = 10, 25, 50 and 100 (each panel is a histogram of many sample means). The true population mean is about 3.49 minutes and the population SD is 1.14 minutes.

Which sampling distribution has the greatest proportion of estimates above the true population mean?

- **Options:**

  A) n: 10
  B) n: 25
  C) n: 50
  D) n: 100
  E) They all have basically half greater than the true mean

- **Answer (tutor only):** E
- **Explanation (tutor only):** All four are centered on the true mean (random samples give unbiased estimates), so about half of the estimates fall above it regardless of n. Bigger n changes the spread, not the center.
- **Why the wrong options are wrong (tutor only):**
  A)–D) Sample size affects how far estimates stray, not which side they're on.
- **Hint:** Where is each histogram centered?

### ch08-hw-09-v1
- **Kind:** AI-written version of ch08-hw-09
- **Concepts:** Sampling distribution; Sampling error vs bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-oak-sampdist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-oak-sampdist.png)
- **Question:**

Imagine we could measure every one of the 8,000 red oaks in a forest: their mean height is 18.0 m and the SD is 4.0 m. The plot shows sampling distributions of the mean height for random samples of n = 4, 16 and 64 trees (each panel is a histogram of 10,000 sample means; red line = true mean).

Which sampling distribution has the greatest proportion of sample means above the true mean (18.0 m)?

- **Options:**

  A) n: 4
  B) n: 16
  C) n: 64
  D) They all have about half above the true mean

- **Answer (tutor only):** D
- **Explanation (tutor only):** All three are centered on the true mean (random samples give unbiased estimates), so about half of the means fall above it whatever n is. Larger n changes the spread, not the center.
- **Why the wrong options are wrong (tutor only):**
  A)–C) Sample size affects how far estimates stray, not which side they're on.
- **Hint:** Where is each histogram centered?

### ch08-hw-09-v2
- **Kind:** AI-written version of ch08-hw-09
- **Concepts:** Sampling distribution; Sampling error vs bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-trout-unbiased.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-trout-unbiased.png)
- **Question:**

A hatchery pond holds thousands of trout with a true mean length of 31.0 cm. A technician nets 25 fish at random, measures them, and returns them, and does this 1000 times. The plot shows the 1000 estimated means (red line = true mean).

About what proportion of the 1000 estimates are above the true mean?

- **Options:**

  A) About 0.10
  B) About 0.25
  C) About 0.50
  D) About 0.95

- **Answer (tutor only):** C
- **Explanation (tutor only):** The estimates are centered on the true mean, as expected from random sampling (no bias), so about half fall above it (here 0.49).
- **Why the wrong options are wrong (tutor only):**
  A), B) and D) Those would mean the estimates are shifted, i.e., biased.
- **Hint:** Where is the histogram centered relative to the red line?

### ch08-hw-10
- **Kind:** Course original
- **Concepts:** SD vs SE; Sampling error vs bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-hw-sampdist-n.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-hw-sampdist-n.png)
- **Question:**

The plot shows sampling distributions of the mean eruption length of Old Faithful for samples of size n = 10, 25, 50 and 100 (each panel is a histogram of many sample means). The true population mean is about 3.49 minutes and the population SD is 1.14 minutes.

Which statement about sampling bias is correct?

- **Options:**

  A) Sampling bias is greatest with n: 10
  B) Sampling bias is greatest with n: 25
  C) Sampling bias is greatest with n: 50
  D) Sampling bias is greatest with n: 100
  E) There is no difference in sampling bias, only sampling error

- **Answer (tutor only):** E
- **Explanation (tutor only):** Bias is a systematic shift of the whole sampling distribution away from the truth. All four distributions are centered on the true mean, so there's no bias. They differ only in spread (sampling error).
- **Why the wrong options are wrong (tutor only):**
  A)–D) A larger sample doesn't fix bias, and a smaller one doesn't create it.
- **Hint:** Bias moves the center; error widens the spread.

### ch08-hw-10-v1
- **Kind:** AI-written version of ch08-hw-10
- **Concepts:** SD vs SE; Sampling error vs bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-oak-sampdist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-oak-sampdist.png)
- **Question:**

Imagine we could measure every one of the 8,000 red oaks in a forest: their mean height is 18.0 m and the SD is 4.0 m. The plot shows sampling distributions of the mean height for random samples of n = 4, 16 and 64 trees (each panel is a histogram of 10,000 sample means; red line = true mean).

Which statement about sampling bias is correct?

- **Options:**

  A) Sampling bias is greatest with n = 4
  B) Sampling bias is greatest with n = 64
  C) There is no difference in sampling bias between them, only in sampling error

- **Answer (tutor only):** C
- **Explanation (tutor only):** All three distributions are centered on the true mean, so none is biased. They differ only in spread (sampling error).
- **Why the wrong options are wrong (tutor only):**
  A) and B) A small sample is noisier, not biased; a large one is more precise, not less biased.
- **Hint:** Bias moves the center; error widens the spread.

### ch08-hw-10-v2
- **Kind:** AI-written version of ch08-hw-10
- **Concepts:** SD vs SE; Sampling error vs bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-pink-sampdist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-pink-sampdist.png)
- **Question:**

In a large Clarkia population, 30% of plants have pink flowers. The plot shows the sampling distributions of the proportion of pink plants in random samples of n = 10, 40 and 160 plants (red line = true proportion, 0.30).

Which statement about sampling bias is correct?

- **Options:**

  A) Sampling bias is greatest with n = 10
  B) Sampling bias is greatest with n = 160
  C) None of these is biased; they differ in sampling error

- **Answer (tutor only):** C
- **Explanation (tutor only):** Each distribution is centered on 0.30, so random samples of any size give unbiased estimates. The n = 10 distribution is just much wider.
- **Why the wrong options are wrong (tutor only):**
  A) Wide is not the same as biased.
  B) Larger random samples don't add bias.
- **Hint:** Where is each distribution centered?

### ch08-hw-11
- **Kind:** Course original
- **Concepts:** SD vs SE; Sampling error vs bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-hw-sampdist-n.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-hw-sampdist-n.png)
- **Question:**

The plot shows sampling distributions of the mean eruption length of Old Faithful for samples of size n = 10, 25, 50 and 100 (each panel is a histogram of many sample means). The true population mean is about 3.49 minutes and the population SD is 1.14 minutes.

Which statement about sampling error is correct?

- **Options:**

  A) Sampling error is greatest with n: 10
  B) Sampling error is greatest with n: 25
  C) Sampling error is greatest with n: 50
  D) Sampling error is greatest with n: 100
  E) There is no difference in sampling error, only sampling bias

- **Answer (tutor only):** A
- **Explanation (tutor only):** The n = 10 distribution is the widest, so its estimates stray furthest from the truth by chance.
- **Why the wrong options are wrong (tutor only):**
  D) n = 100 is the narrowest, with the least sampling error.
  E) The widths clearly differ.
  B) and C) The middle sample sizes are narrower than n = 10.
- **Hint:** Which histogram is widest?

### ch08-hw-11-v1
- **Kind:** AI-written version of ch08-hw-11
- **Concepts:** SD vs SE; Sampling error vs bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-oak-sampdist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-oak-sampdist.png)
- **Question:**

Imagine we could measure every one of the 8,000 red oaks in a forest: their mean height is 18.0 m and the SD is 4.0 m. The plot shows sampling distributions of the mean height for random samples of n = 4, 16 and 64 trees (each panel is a histogram of 10,000 sample means; red line = true mean).

Which statement about sampling error is correct?

- **Options:**

  A) Sampling error is greatest with n = 4
  B) Sampling error is greatest with n = 64
  C) There is no difference in sampling error between them

- **Answer (tutor only):** A
- **Explanation (tutor only):** The n = 4 distribution is the widest, so its sample means stray furthest from the truth by chance.
- **Why the wrong options are wrong (tutor only):**
  B) n = 64 is the narrowest, with the least sampling error.
  C) The widths clearly differ.
- **Hint:** Which histogram is widest?

### ch08-hw-11-v2
- **Kind:** AI-written version of ch08-hw-11
- **Concepts:** SD vs SE; Sampling error vs bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-pink-sampdist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-pink-sampdist.png)
- **Question:**

In a large Clarkia population, 30% of plants have pink flowers. The plot shows the sampling distributions of the proportion of pink plants in random samples of n = 10, 40 and 160 plants (red line = true proportion, 0.30).

If you took one random sample of each size, which estimate is most likely to be far from 0.30?

- **Options:**

  A) The n = 10 estimate
  B) The n = 40 estimate
  C) The n = 160 estimate
  D) All are equally likely to be far off

- **Answer (tutor only):** A
- **Explanation (tutor only):** The n = 10 distribution spreads from 0 to 0.7, so a single small sample can easily miss by 0.2 or more. Larger samples cluster tightly around 0.30.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Their distributions are narrower.
  D) Spread depends strongly on n.
- **Hint:** Which distribution reaches furthest from the red line?

### ch08-hw-12
- **Kind:** Course original
- **Concepts:** SD vs SE; Sampling error vs bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-hw-sampdist-n.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-hw-sampdist-n.png)
- **Question:**

The plot shows sampling distributions of the mean eruption length of Old Faithful for samples of size n = 10, 25, 50 and 100 (each panel is a histogram of many sample means). The true population mean is about 3.49 minutes and the population SD is 1.14 minutes.

Which sampling distribution has the greatest proportion of sample means more than half a population SD away from the true mean (i.e., below 2.92 or above 4.06)?

- **Options:**

  A) n: 10
  B) n: 25
  C) n: 50
  D) n: 100
  E) They all have basically 60% more than 0.5 SD away from the true mean

- **Answer (tutor only):** A
- **Explanation (tutor only):** Look at the tails beyond 2.92 and 4.06. Only the wide n = 10 distribution has much there (roughly 10%). Larger samples are almost never that far off. 'About 60%' would be true for individual eruptions, not for means.
- **Why the wrong options are wrong (tutor only):**
  E) That describes individuals (the population distribution), not sample means.
  B)–D) Narrower distributions put less in the tails.
- **Hint:** Mark 2.92 and 4.06 on each panel. Which has bars outside them?

### ch08-hw-12-v1
- **Kind:** AI-written version of ch08-hw-12
- **Concepts:** SD vs SE; Sampling error vs bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-oak-sampdist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-oak-sampdist.png)
- **Question:**

Imagine we could measure every one of the 8,000 red oaks in a forest: their mean height is 18.0 m and the SD is 4.0 m. The plot shows sampling distributions of the mean height for random samples of n = 4, 16 and 64 trees (each panel is a histogram of 10,000 sample means; red line = true mean).

Which sampling distribution has the greatest proportion of sample means more than half a population SD (2 m) from the true mean, i.e., below 16 m or above 20 m?

- **Options:**

  A) n: 4
  B) n: 16
  C) n: 64
  D) They all have about 62% more than 2 m away

- **Answer (tutor only):** A
- **Explanation (tutor only):** Only the wide n = 4 distribution has much beyond 16 and 20 m (about 32% of means). For n = 16 it's about 5%, and for n = 64 almost none. 'About 62%' describes individual trees, not means.
- **Why the wrong options are wrong (tutor only):**
  D) About 62% of individual trees are more than 0.5 SD from the mean; means are much less spread out.
  B) and C) Narrower distributions have less in their tails.
- **Hint:** Mark 16 and 20 m on each panel. Which has bars outside them?

### ch08-hw-12-v2
- **Kind:** AI-written version of ch08-hw-12
- **Concepts:** SD vs SE; Sampling error vs bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-pink-sampdist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-pink-sampdist.png)
- **Question:**

In a large Clarkia population, 30% of plants have pink flowers. The plot shows the sampling distributions of the proportion of pink plants in random samples of n = 10, 40 and 160 plants (red line = true proportion, 0.30).

For which sample size is a sample proportion of 0.45 or higher (half again as large as the truth) most likely?

- **Options:**

  A) n = 10
  B) n = 40
  C) n = 160
  D) It's equally likely for all three

- **Answer (tutor only):** A
- **Explanation (tutor only):** With n = 10, about 15% of samples give 0.45 or more (exact binomial). With n = 40 it's about 3%, and with n = 160 essentially never. Small samples are much more likely to be far off.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Larger samples rarely stray that far.
  D) The spread shrinks as n grows.
- **Hint:** Find 0.45 on the x-axis in each panel.

### ch08-hw-13
- **Kind:** Course original
- **Concepts:** SD vs SE
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-hw-sampdist-n.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-hw-sampdist-n.png)
- **Question:**

The plot shows sampling distributions of the mean eruption length of Old Faithful for samples of size n = 10, 25, 50 and 100 (each panel is a histogram of many sample means). The true population mean is about 3.49 minutes and the population SD is 1.14 minutes.

Which has the smallest standard error?

- **Options:**

  A) n: 10
  B) n: 25
  C) n: 50
  D) n: 100
  E) They all have the same standard error

- **Answer (tutor only):** D
- **Explanation (tutor only):** The standard error is the SD of the sampling distribution, and n = 100 has the narrowest. SE ≈ SD/√n: 1.14/√100 ≈ 0.11 versus 1.14/√10 ≈ 0.36.
- **Why the wrong options are wrong (tutor only):**
  A) n = 10 has the largest SE.
  E) The SE shrinks as n grows.
  B) and C) These are narrower than n = 10 but wider than n = 100.
- **Hint:** Narrowest histogram = smallest SE.

### ch08-hw-13-v1
- **Kind:** AI-written version of ch08-hw-13
- **Concepts:** SD vs SE
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-oak-sampdist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-oak-sampdist.png)
- **Question:**

Imagine we could measure every one of the 8,000 red oaks in a forest: their mean height is 18.0 m and the SD is 4.0 m. The plot shows sampling distributions of the mean height for random samples of n = 4, 16 and 64 trees (each panel is a histogram of 10,000 sample means; red line = true mean).

Which sample size has the smallest standard error?

- **Options:**

  A) n: 4
  B) n: 16
  C) n: 64
  D) They all have the same standard error

- **Answer (tutor only):** C
- **Explanation (tutor only):** The SE is the SD of the sampling distribution; n = 64 is the narrowest. SE ≈ SD/√n: 4/√64 = 0.5 m vs 4/√4 = 2 m.
- **Why the wrong options are wrong (tutor only):**
  A) n = 4 has the largest SE.
  B) Narrower than n = 4 but wider than n = 64.
  D) The SE shrinks as n grows.
- **Hint:** Narrowest histogram = smallest SE.

### ch08-hw-13-v2
- **Kind:** AI-written version of ch08-hw-13
- **Concepts:** SD vs SE
- **Type:** MC
- **Question:**

The SD of seed mass in a population is 0.8 mg. Which sample size gives a standard error of the mean of about 0.1 mg?

- **Options:**

  A) n = 8
  B) n = 16
  C) n = 64
  D) n = 800

- **Answer (tutor only):** C
- **Explanation (tutor only):** SE = SD/√n. For SE = 0.1, √n = 0.8/0.1 = 8, so n = 64. To halve the SE you need four times the sample size.
- **Why the wrong options are wrong (tutor only):**
  A) and B) Too small: SE ≈ 0.28 and 0.2 mg.
  D) Gives SE ≈ 0.028 mg, much smaller than needed.
- **Hint:** Set 0.8/√n = 0.1 and solve for n.

## Chapter 9: Uncertainty

### ch09-book-01
- **Kind:** Course original
- **Concepts:** Sampling distribution & SE
- **Type:** MC
- **Question:**

The ___ is the key idea we use to think about uncertainty due to sampling error.

- **Options:**

  A) Standard error
  B) Standard deviation
  C) Sampling distribution
  D) Error function
  E) Bootstrap distribution

- **Answer (tutor only):** C
- **Explanation (tutor only):** The sampling distribution (the distribution of estimates across samples) is the foundational idea. The SE measures its spread, and the bootstrap approximates it.
- **Why the wrong options are wrong (tutor only):**
  A) Close: the SE quantifies uncertainty, but it comes from the sampling distribution.
  B) The SD describes individuals.
  D) Not a thing here.
  E) A tool to approximate the sampling distribution, not the idea itself.
- **Hint:** Idea vs measure vs tool.

### ch09-book-01-v1
- **Kind:** AI-written version of ch09-book-01
- **Concepts:** Sampling distribution & SE
- **Type:** MC
- **Question:**

The ___ summarizes the spread of the sampling distribution in one number.

- **Options:**

  A) Standard error
  B) Standard deviation of the sample
  C) Bootstrap
  D) Sample mean
  E) Confidence level

- **Answer (tutor only):** A
- **Explanation (tutor only):** The SE is the standard deviation of the sampling distribution: the typical size of sampling error.
- **Why the wrong options are wrong (tutor only):**
  B) That's spread of individuals.
  C) The bootstrap is a method for approximating the sampling distribution.
  D) That's an estimate, not a spread.
  E) That's a chosen percentage, like 95%.
- **Hint:** Spread of estimates.

### ch09-book-01-v2
- **Kind:** AI-written version of ch09-book-01
- **Concepts:** Sampling distribution & SE; Bootstrap
- **Type:** MC
- **Question:**

The bootstrap distribution is best described as:

- **Options:**

  A) An approximation of the sampling distribution, made by resampling our one sample with replacement
  B) The exact sampling distribution
  C) The distribution of values in our sample
  D) The population distribution

- **Answer (tutor only):** A
- **Explanation (tutor only):** We can't observe the true sampling distribution, so we approximate it by treating our sample as the population and resampling.
- **Why the wrong options are wrong (tutor only):**
  B) It's an approximation; its quality depends on the sample.
  C) Its values are estimates, not individual observations.
  D) It describes estimates, not individuals.
- **Hint:** What do we resample, and what does that approximate?

### ch09-book-02
- **Kind:** Course original
- **Concepts:** Bootstrap
- **Type:** MC
- **Question:**

For real data, we can use the ___, which we make by sampling ___ replacement, to estimate uncertainty.

- **Options:**

  A) Bootstrap distribution, with
  B) Bootstrap distribution, without
  C) Sampling distribution, without
  D) Sampling distribution, with

- **Answer (tutor only):** A
- **Explanation (tutor only):** We can't make the true sampling distribution from one dataset, but we can bootstrap: resample our data with replacement.
- **Why the wrong options are wrong (tutor only):**
  B) Without replacement, every resample equals the original data.
  C) and D) The sampling distribution needs new samples from the population.
- **Hint:** Which one can you make from a single dataset?

### ch09-book-02-v1
- **Kind:** AI-written version of ch09-book-02
- **Concepts:** Bootstrap
- **Type:** MC
- **Question:**

To make a bootstrap replicate from a sample of size n, we draw ___ observations ___ replacement.

- **Options:**

  A) n, with
  B) n, without
  C) n/2, with
  D) 2n, without

- **Answer (tutor only):** A
- **Explanation (tutor only):** Same size, with replacement: that mimics drawing a new sample of size n from a population shaped like our data.
- **Why the wrong options are wrong (tutor only):**
  B) Without replacement just reshuffles the data.
  C) Smaller resamples exaggerate uncertainty.
  D) You can't draw 2n without replacement from n values.
- **Hint:** Same size as the original?

### ch09-book-02-v2
- **Kind:** AI-written version of ch09-book-02
- **Concepts:** Sampling distribution & SE
- **Type:** MC
- **Question:**

The true sampling distribution is made by drawing many ___ from the ___.

- **Options:**

  A) new samples, population
  B) resamples, sample
  C) individuals, sample
  D) estimates, bootstrap

- **Answer (tutor only):** A
- **Explanation (tutor only):** The sampling distribution comes from repeated independent samples of the population; the bootstrap approximates it with resamples of our one sample.
- **Why the wrong options are wrong (tutor only):**
  B) That's the bootstrap.
  C) That just gives the sample distribution.
  D) Backwards: the bootstrap approximates the sampling distribution.
- **Hint:** Where do truly new samples come from?

### ch09-book-03
- **Kind:** Course original
- **Concepts:** Sampling distribution & SE; Confidence intervals
- **Type:** select-all
- **Question:**

Which of these tend to get bigger as sample sizes get smaller? (Select all that apply.)

- **Options:**

  A) Standard error
  B) Standard deviation
  C) Mean
  D) Confidence interval width

- **Answer (tutor only):** A, D
- **Explanation (tutor only):** Uncertainty grows as n shrinks. The mean and SD get less precise with small samples, but they aren't systematically larger.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Noisier, not bigger.
- **Hint:** Which describe uncertainty, and which describe the data?

### ch09-book-03-v1
- **Kind:** AI-written version of ch09-book-03
- **Concepts:** Sampling distribution & SE; Confidence intervals
- **Type:** select-all
- **Question:**

Which of these tend to get SMALLER as sample size gets larger? (Select all that apply.)

- **Options:**

  A) Standard error
  B) Width of a 95% CI
  C) Standard deviation
  D) Median

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** Uncertainty shrinks with more data. The SD and median describe the population; they're estimated more precisely but don't trend smaller.
- **Why the wrong options are wrong (tutor only):**
  C) and D) These describe individuals, not precision.
- **Hint:** Precision vs description.

### ch09-book-03-v2
- **Kind:** AI-written version of ch09-book-03
- **Concepts:** Sampling distribution & SE; Confidence intervals
- **Type:** MC
- **Question:**

Study 1 (n = 20) and Study 2 (n = 200) sample the same population. Which is most likely?

- **Options:**

  A) Study 2's 95% CI will be narrower, but both have the same coverage
  B) Study 2's CI is more likely to contain the true mean
  C) Study 1's CI will be narrower
  D) Both CIs will be about the same width

- **Answer (tutor only):** A
- **Explanation (tutor only):** Larger n → smaller SE → narrower CI. A correctly made 95% CI catches the truth 95% of the time regardless of n.
- **Why the wrong options are wrong (tutor only):**
  B) Coverage stays 95%; only width changes.
  C) Smaller samples give wider CIs.
  D) Ten times the data makes a big difference.
- **Hint:** Width and coverage are different things.

### ch09-book-04
- **Kind:** Course original
- **Concepts:** Confidence intervals
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

### ch09-book-04-v1
- **Kind:** AI-written version of ch09-book-04
- **Concepts:** Confidence intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-gquiz-ringtoss.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-gquiz-ringtoss.png)
- **Question:**

A 95% CI for the proportion of infected ticks is 0.21 to 0.34. Which statement is correct?

- **Options:**

  A) Whether the true proportion lies in 0.21–0.34 is settled; it either does or doesn't
  B) There's a 95% chance the true proportion is between 0.21 and 0.34
  C) 95% of ticks have infection proportions between 0.21 and 0.34
  D) The true proportion is 0.275

- **Answer (tutor only):** A
- **Explanation (tutor only):** After calculation, the interval and the parameter are fixed. The 95% refers to the method.
- **Why the wrong options are wrong (tutor only):**
  B) Attaches the method's rate to this one interval.
  C) Individual ticks are infected or not; the CI is about the population proportion.
  D) 0.275 is the midpoint, an estimate, not the truth.
- **Hint:** Is anything random left once the interval is computed?

### ch09-book-04-v2
- **Kind:** AI-written version of ch09-book-04
- **Concepts:** Confidence intervals
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

### ch09-book-05
- **Kind:** Course original
- **Concepts:** Confidence intervals
- **Type:** MC
- **Question:**

You know the population parameter. A bunch of friends sample randomly from this population and calculate 95% confidence intervals. What proportion of these intervals will catch the true parameter?

- **Options:**

  A) There is no probability about this
  B) 95%
  C) It depends on the sample size
  D) It depends on the sample standard deviation

- **Answer (tutor only):** B
- **Explanation (tutor only):** Across many intervals, about 95% catch the parameter. That's what 95% confidence means.
- **Why the wrong options are wrong (tutor only):**
  A) That applies to one finished interval, not the proportion of many.
  C) and D) These change width, not coverage.
- **Hint:** Many intervals, not one.

### ch09-book-05-v1
- **Kind:** AI-written version of ch09-book-05
- **Concepts:** Confidence intervals
- **Type:** MC
- **Question:**

In a simulation you know the true mean is 50. You draw 1000 samples and compute a 90% CI from each. About how many contain 50?

- **Options:**

  A) About 900
  B) About 950
  C) About 100
  D) All 1000

- **Answer (tutor only):** A
- **Explanation (tutor only):** 90% coverage: about 900 of 1000 intervals catch the true mean.
- **Why the wrong options are wrong (tutor only):**
  B) That's 95% coverage.
  C) That's how many miss.
  D) Some always miss.
- **Hint:** Confidence level × number of intervals.

### ch09-book-05-v2
- **Kind:** AI-written version of ch09-book-05
- **Concepts:** Confidence intervals
- **Type:** MC
- **Question:**

In a simulation, only 80% of supposedly 95% CIs contain the true parameter. What does this suggest?

- **Options:**

  A) The CI method isn't working as advertised for these data (e.g., the sample is too small for the bootstrap, or assumptions are violated)
  B) That's expected: coverage varies with the sample mean
  C) The true parameter changed during the simulation
  D) Nothing; 80% is close to 95%

- **Answer (tutor only):** A
- **Explanation (tutor only):** Simulations check coverage. A 95% method should catch the truth about 95% of the time; 80% means the intervals are too narrow.
- **Why the wrong options are wrong (tutor only):**
  B) Coverage should hold across samples.
  C) The parameter is fixed in a simulation.
  D) Missing 20% vs 5% is a big difference.
- **Hint:** What should coverage be?

### ch09-book-06
- **Kind:** Course original
- **Concepts:** Bootstrap
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-book-faithful-waiting.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-book-faithful-waiting.png)
- **Question:**

The Old Faithful data have 272 eruptions. The mean waiting time until the next eruption is 70.9 minutes (SD = 13.6).

The histogram shows waiting times. The distribution is:

- **Options:**

  A) Unimodal
  B) Bimodal
  C) Symmetric

- **Answer (tutor only):** B
- **Explanation (tutor only):** Two peaks (around 55 and 80 minutes): short waits follow short eruptions, long waits follow long ones.
- **Why the wrong options are wrong (tutor only):**
  A) and C) There are two clear humps.
- **Hint:** Count the peaks.

### ch09-book-06-v1
- **Kind:** AI-written version of ch09-book-06
- **Concepts:** Bootstrap
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-var-flipper-hist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-var-flipper-hist.png)
- **Question:**

Palmer penguins: 342 birds with flipper lengths. Mean flipper length = 200.9 mm (SD = 14.1).

The histogram shows flipper lengths of all three species together. The distribution is:

- **Options:**

  A) Bimodal
  B) Unimodal and symmetric
  C) Uniform

- **Answer (tutor only):** A
- **Explanation (tutor only):** There are two humps (around 190 mm and 215 mm): Adelie and Chinstrap have shorter flippers, Gentoo longer ones.
- **Why the wrong options are wrong (tutor only):**
  B) There's a clear dip near 205 mm between two peaks.
  C) Counts are far from flat.
- **Hint:** Count the humps.

### ch09-book-06-v2
- **Kind:** AI-written version of ch09-book-06
- **Concepts:** Bootstrap
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-var-bee-hist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-var-bee-hist.png)
- **Question:**

We timed 150 bee visits to flowers. Mean time at a flower = 14.9 s (median 10.2 s, SD = 13.8 s).

The histogram shows the visit times. The distribution is:

- **Options:**

  A) Right-skewed
  B) Left-skewed
  C) Symmetric
  D) Bimodal

- **Answer (tutor only):** A
- **Explanation (tutor only):** Most visits are short, with a long tail of a few long visits. The mean (14.9) above the median (10.2) is another sign of right skew.
- **Why the wrong options are wrong (tutor only):**
  B) The long tail is to the right.
  C) The tail is lopsided, and mean ≠ median.
  D) There's one peak.
- **Hint:** Which side has the long tail?

### ch09-book-07
- **Kind:** Course original
- **Concepts:** Sampling distribution & SE; Bootstrap
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-book-faithful-boot.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-book-faithful-boot.png)
- **Question:**

The Old Faithful data have 272 eruptions. The mean waiting time until the next eruption is 70.9 minutes (SD = 13.6).

The plot shows 5000 bootstrap replicates of the mean waiting time. Even though the data are bimodal, the bootstrap distribution is roughly: (select all that apply)

- **Options:**

  A) Unimodal
  B) Bimodal
  C) Symmetric

- **Answer (tutor only):** A, C
- **Explanation (tutor only):** Averaging smooths out extremes: each resample mixes short and long waits, so the means cluster in one roughly symmetric peak. This previews the central limit theorem. (Picking only 'unimodal' is fine too.)
- **Why the wrong options are wrong (tutor only):**
  B) The bimodality of individuals doesn't carry over to means.
- **Hint:** Is this plot of individual waits, or of means?

### ch09-book-07-v1
- **Kind:** AI-written version of ch09-book-07
- **Concepts:** Sampling distribution & SE; Bootstrap
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-var-flipper-boot.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-var-flipper-boot.png)
- **Question:**

Palmer penguins: 342 birds with flipper lengths. Mean flipper length = 200.9 mm (SD = 14.1).

The plot shows 5000 bootstrap replicates of mean flipper length. Even though flipper lengths are bimodal, the bootstrap distribution is roughly: (select all that apply)

- **Options:**

  A) Unimodal
  B) Bimodal
  C) Symmetric

- **Answer (tutor only):** A, C
- **Explanation (tutor only):** Each resample mixes short- and long-flippered birds, so the means pile up in one roughly symmetric peak. This previews the central limit theorem.
- **Why the wrong options are wrong (tutor only):**
  B) Bimodal individuals don't make bimodal means.
- **Hint:** Does averaging keep the two humps?

### ch09-book-07-v2
- **Kind:** AI-written version of ch09-book-07
- **Concepts:** Sampling distribution & SE; Bootstrap
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-var-bee-boot.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-var-bee-boot.png)
- **Question:**

We timed 150 bee visits to flowers. Mean time at a flower = 14.9 s (median 10.2 s, SD = 13.8 s).

The plot shows 5000 bootstrap means. Compared with the raw data (strongly right-skewed), the bootstrap distribution of the mean is:

- **Options:**

  A) Much closer to symmetric, with only a slight right tail
  B) Just as right-skewed as the data
  C) Left-skewed
  D) Bimodal

- **Answer (tutor only):** A
- **Explanation (tutor only):** Averaging 150 visits smooths out the skew a lot, though a little remains with skewed data. The bootstrap distribution is single-peaked and nearly symmetric.
- **Why the wrong options are wrong (tutor only):**
  B) Means are much less skewed than individuals.
  C) Averaging doesn't flip skew.
  D) There's one peak.
- **Hint:** What does averaging do to a long tail?

### ch09-book-08
- **Kind:** Course original
- **Concepts:** Sampling distribution & SE; Bootstrap; Confidence intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-book-faithful-boot.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-book-faithful-boot.png)
- **Question:**

The Old Faithful data have 272 eruptions. The mean waiting time until the next eruption is 70.9 minutes (SD = 13.6).

In the plot of 5000 bootstrap means, the red dashed lines mark the 0.5th and 99.5th percentiles (about 68.8 and 73.0 minutes). Which statement is correct?

- **Options:**

  A) The 99% CI for mean waiting time is about 68.8 to 73.0 minutes, and the bootstrap SE is the standard deviation of the 5000 bootstrap means (about 0.82 min)
  B) The 95% CI is about 68.8 to 73.0 minutes, and the SE is the mean of the bootstrap distribution
  C) The 99% CI is about 68.8 to 73.0 minutes, and the SE is the SD of the original data (13.6 min)
  D) 99% of individual waiting times fall between 68.8 and 73.0 minutes

- **Answer (tutor only):** A
- **Explanation (tutor only):** The middle 99% of bootstrap estimates (0.5th to 99.5th percentiles) gives the 99% CI. The SE is the spread (SD) of the bootstrap distribution. A 99% CI is wider than a 95% CI (69.3–72.5) from the same data: more confidence costs precision.
- **Why the wrong options are wrong (tutor only):**
  B) The 0.5th–99.5th percentiles give 99%, not 95%, and the SE is an SD, not a mean.
  C) 13.6 is the SD among individual waits.
  D) The CI is for the mean, not for individuals (which range from about 43 to 96 minutes).
- **Hint:** Which percentiles leave 0.5% in each tail? And SE = SD of what?

### ch09-book-08-v1
- **Kind:** AI-written version of ch09-book-08
- **Concepts:** Sampling distribution & SE; Bootstrap; Confidence intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-var-flipper-boot.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-var-flipper-boot.png)
- **Question:**

Palmer penguins: 342 birds with flipper lengths. Mean flipper length = 200.9 mm (SD = 14.1).

In the plot of 5000 bootstrap means, the red dashed lines mark the 2.5th and 97.5th percentiles (about 199.5 and 202.4 mm). The SD of the bootstrap means is 0.75 mm. Which is correct?

- **Options:**

  A) The 95% CI for mean flipper length is about 199.5 to 202.4 mm, and the bootstrap SE is about 0.75 mm
  B) The 99% CI is about 199.5 to 202.4 mm, and the SE is 14.1 mm
  C) 95% of penguins have flippers between 199.5 and 202.4 mm
  D) The SE is 200.9 mm, the mean of the bootstrap distribution

- **Answer (tutor only):** A
- **Explanation (tutor only):** The middle 95% of bootstrap means gives the 95% CI. The SE is the SD of the bootstrap means (≈ 14.1/√342 ≈ 0.76).
- **Why the wrong options are wrong (tutor only):**
  B) 2.5th–97.5th percentiles give 95%, and 14.1 is the SD of individual birds.
  C) Individual flippers range from about 172 to 231 mm; the CI is for the mean.
  D) The mean of the bootstrap means is the estimate, not its SE.
- **Hint:** Which percentiles, and what does the SD of bootstrap means measure?

### ch09-book-08-v2
- **Kind:** AI-written version of ch09-book-08
- **Concepts:** Bootstrap; Confidence intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-var-bee-boot.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-var-bee-boot.png)
- **Question:**

We timed 150 bee visits to flowers. Mean time at a flower = 14.9 s (median 10.2 s, SD = 13.8 s).

In the plot of 5000 bootstrap means, the red dashed lines mark the 5th and 95th percentiles (about 13.2 and 16.8 s). Which is correct?

- **Options:**

  A) This is a 90% CI for the mean visit time: about 13.2 to 16.8 s
  B) This is a 95% CI for the mean visit time
  C) 90% of visits last 13.2 to 16.8 s
  D) This is a 90% CI for the median visit time

- **Answer (tutor only):** A
- **Explanation (tutor only):** 5th to 95th percentiles leaves 5% in each tail: a 90% interval. It's for the mean, because the replicates are means.
- **Why the wrong options are wrong (tutor only):**
  B) 95% would use the 2.5th and 97.5th percentiles.
  C) Individual visits range from about 1 s to over 90 s; the CI is for the mean.
  D) The replicates are means, not medians.
- **Hint:** How much is cut from each tail?

### ch09-chime-01
- **Kind:** Course original
- **Concepts:** Sampling distribution & SE
- **Type:** MC
- **Question:**

True or false: the sampling distribution is the distribution of values in your sample.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** The sampling distribution is the distribution of estimates (e.g., means) across many hypothetical samples. The values in your one sample form the sample distribution.
- **Why the wrong options are wrong (tutor only):**
  A) That's the most common mix-up: sample distribution ≠ sampling distribution.
- **Hint:** Values of individuals, or of estimates?

### ch09-chime-01-v1
- **Kind:** AI-written version of ch09-chime-01
- **Concepts:** Sampling distribution & SE
- **Type:** TF
- **Question:**

True or false: the standard error is the standard deviation of the values in your sample.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** The SE is the SD of the sampling distribution (spread of estimates across samples). The SD of the values in your sample describes individuals.
- **Why the wrong options are wrong (tutor only):**
  A) This mixes up the sample's spread with the spread of estimates.
- **Hint:** Spread of individuals or of estimates?

### ch09-chime-01-v2
- **Kind:** AI-written version of ch09-chime-01
- **Concepts:** Sampling distribution & SE
- **Type:** TF
- **Question:**

True or false: the sampling distribution describes how estimates (e.g., means) would vary across many samples of the same size.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** A
- **Explanation (tutor only):** That's exactly the definition: each value is an estimate from a different hypothetical sample.
- **Why the wrong options are wrong (tutor only):**
  B) It is not the distribution of values in one sample (that's the sample distribution).
- **Hint:** Each point in a sampling distribution is a ___.

### ch09-chime-02
- **Kind:** Course original
- **Concepts:** Sampling distribution & SE
- **Type:** select-all
- **Question:**

Which of the following will tend to decrease the sampling error in estimates of the mean? (Select all that apply.)

- **Options:**

  A) A smaller variance
  B) A smaller mean (with an equal variance)
  C) A larger sample size
  D) Unbiased sampling
  E) None of these will tend to decrease sampling error

- **Answer (tutor only):** A, C
- **Explanation (tutor only):** SE = SD/√n: less variable populations and larger samples both shrink sampling error.
- **Why the wrong options are wrong (tutor only):**
  B) The mean doesn't enter the SE.
  D) Unbiased sampling fixes the center, not the spread.
  E) Two of these do help: a smaller variance and a larger sample.
- **Hint:** Think SE = SD / √n.

### ch09-chime-02-v1
- **Kind:** AI-written version of ch09-chime-02
- **Concepts:** Sampling distribution & SE
- **Type:** select-all
- **Question:**

Which of the following will tend to INCREASE the standard error of a mean? (Select all that apply.)

- **Options:**

  A) A smaller sample size
  B) A more variable population
  C) A larger population mean (same variance)
  D) Biased sampling
  E) None of these

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** SE = SD/√n: fewer observations or more variable individuals both increase it.
- **Why the wrong options are wrong (tutor only):**
  C) The mean doesn't enter the SE.
  D) Bias shifts the center; it isn't measured by the SE.
  E) Two of these do increase it.
- **Hint:** Look at SE = SD/√n.

### ch09-chime-02-v2
- **Kind:** AI-written version of ch09-chime-02
- **Concepts:** Sampling distribution & SE
- **Type:** MC
- **Question:**

A researcher measures 2000 birds, but only at feeders (which attract bolder birds). What does the huge sample do and not do?

- **Options:**

  A) It makes sampling error small, but doesn't fix the bias: the estimate is precise but may be precisely wrong
  B) It removes both sampling error and bias
  C) It increases sampling error
  D) It fixes the bias but not sampling error

- **Answer (tutor only):** A
- **Explanation (tutor only):** Larger n shrinks sampling error (SE ∝ 1/√n), but a biased sampling method stays biased no matter how many birds you measure.
- **Why the wrong options are wrong (tutor only):**
  B) and D) Sample size doesn't fix bias.
  C) More data reduces sampling error.
- **Hint:** Sampling error vs sampling bias: which one does n fix?

### ch09-chime-03
- **Kind:** Course original
- **Concepts:** Sampling distribution & SE
- **Type:** MC
- **Question:**

The sampling distribution is a key idea in statistics because we use it to think about (choose the best answer):

- **Options:**

  A) Sampling error
  B) Sampling bias
  C) Non-independence

- **Answer (tutor only):** A
- **Explanation (tutor only):** The sampling distribution shows how estimates vary by chance from sample to sample: sampling error.
- **Why the wrong options are wrong (tutor only):**
  B) Bias would shift the sampling distribution, but we can't see bias from it (we don't know the truth).
  C) Non-independence is a design problem, not what the sampling distribution describes.
- **Hint:** Chance variation among estimates is called…

### ch09-chime-03-v1
- **Kind:** AI-written version of ch09-chime-03
- **Concepts:** Sampling distribution & SE
- **Type:** MC
- **Question:**

Why can't a sampling distribution reveal sampling bias in a real study?

- **Options:**

  A) Bias shifts the whole distribution away from the truth, but in a real study we don't know the truth, so we can't see the shift
  B) Sampling distributions don't exist for biased samples
  C) Bias makes the sampling distribution wider
  D) It can; bias shows up as bimodality

- **Answer (tutor only):** A
- **Explanation (tutor only):** The sampling distribution shows chance spread around wherever the method is centered. Detecting a shifted center would require knowing the true parameter.
- **Why the wrong options are wrong (tutor only):**
  B) They exist; they're just centered in the wrong place.
  C) Bias is about the center, not the spread.
  D) Bias doesn't create extra peaks.
- **Hint:** Bias moves the center. Do we know where the center should be?

### ch09-chime-03-v2
- **Kind:** AI-written version of ch09-chime-03
- **Concepts:** Sampling distribution & SE
- **Type:** MC
- **Question:**

Which summary of the sampling distribution do we use to quantify sampling error?

- **Options:**

  A) Its standard deviation (the standard error)
  B) Its mean
  C) Its maximum
  D) Its sample size

- **Answer (tutor only):** A
- **Explanation (tutor only):** Sampling error is about how much estimates scatter; the SD of the sampling distribution (the SE) measures that.
- **Why the wrong options are wrong (tutor only):**
  B) The mean is near the estimate itself (or the truth), not the error.
  C) A single extreme isn't a typical error.
  D) Sample size affects the SE but isn't a summary of the distribution.
- **Hint:** Error = scatter. Which summary measures scatter?

### ch09-chime-04
- **Kind:** Course original
- **Concepts:** Sampling distribution & SE; Confidence intervals
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

### ch09-chime-04-v1
- **Kind:** AI-written version of ch09-chime-04
- **Concepts:** Sampling distribution & SE
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

### ch09-chime-04-v2
- **Kind:** AI-written version of ch09-chime-04
- **Concepts:** Sampling distribution & SE
- **Type:** MC
- **Question:**

If the SD stays the same, by how much does the standard error of the mean change when n goes from 25 to 100?

- **Options:**

  A) It is cut in half
  B) It is cut to a quarter
  C) It stays the same
  D) It doubles

- **Answer (tutor only):** A
- **Explanation (tutor only):** SE = SD/√n. √25 = 5 and √100 = 10, so the SE is halved.
- **Why the wrong options are wrong (tutor only):**
  B) The SE scales with 1/√n, not 1/n.
  C) More data reduces the SE.
  D) More data reduces, not increases, the SE.
- **Hint:** Compare √25 and √100.

### ch09-chime-05
- **Kind:** Course original
- **Concepts:** Sampling distribution & SE; Bootstrap
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

### ch09-chime-05-v1
- **Kind:** AI-written version of ch09-chime-05
- **Concepts:** Sampling distribution & SE; Bootstrap
- **Type:** MC
- **Question:**

In a computer simulation where we invent the population, which can we generate?

- **Options:**

  A) Only the sampling distribution
  B) Only the bootstrap distribution
  C) Both
  D) Neither

- **Answer (tutor only):** C
- **Explanation (tutor only):** In a simulation we can draw as many new samples as we want (sampling distribution), and we can also bootstrap any one sample. That's how we check that the bootstrap works.
- **Why the wrong options are wrong (tutor only):**
  A) We can also bootstrap any one simulated sample.
  B) Simulation lets us sample the population repeatedly too.
  D) Simulation makes both possible.
- **Hint:** What does knowing the population let you do?

### ch09-chime-05-v2
- **Kind:** AI-written version of ch09-chime-05
- **Concepts:** Sampling distribution & SE; Bootstrap
- **Type:** MC
- **Question:**

Why do we bootstrap in real studies instead of building the true sampling distribution?

- **Options:**

  A) Building the sampling distribution would require many new samples from the population, but we usually only have one
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

### ch09-chime-06
- **Kind:** Course original
- **Concepts:** Sampling distribution & SE; Bootstrap
- **Type:** MC
- **Question:**

The bootstrap standard error is the _____ of estimates from many bootstrap replicates.

- **Options:**

  A) Mean
  B) Standard deviation
  C) Upper and lower quantiles
  D) Covariance

- **Answer (tutor only):** B
- **Explanation (tutor only):** The SE is the SD of the sampling distribution, and the bootstrap distribution approximates it, so the bootstrap SE is the SD of the bootstrap estimates.
- **Why the wrong options are wrong (tutor only):**
  A) The mean of the replicates is close to the original estimate.
  C) Quantiles give a confidence interval, not the SE.
  D) Covariance involves two variables.
- **Hint:** SE = the SD of what?

### ch09-chime-06-v1
- **Kind:** AI-written version of ch09-chime-06
- **Concepts:** Bootstrap; Confidence intervals
- **Type:** MC
- **Question:**

The 95% bootstrap confidence interval is found from the _____ of the bootstrap estimates.

- **Options:**

  A) 2.5th and 97.5th percentiles
  B) Mean
  C) Standard deviation
  D) Minimum and maximum

- **Answer (tutor only):** A
- **Explanation (tutor only):** The middle 95% of bootstrap estimates (between the 2.5th and 97.5th percentiles) gives the percentile 95% CI.
- **Why the wrong options are wrong (tutor only):**
  B) The mean is a single center value.
  C) The SD gives the SE, not the interval.
  D) The min–max isn't 95%.
- **Hint:** Cut off 2.5% in each tail.

### ch09-chime-06-v2
- **Kind:** AI-written version of ch09-chime-06
- **Concepts:** Sampling distribution & SE; Bootstrap
- **Type:** MC
- **Question:**

1000 bootstrap means have mean 70.9 and SD 0.82. The original data have SD 13.6. Which is the bootstrap SE?

- **Options:**

  A) 0.82
  B) 13.6
  C) 70.9
  D) 13.6 / 1000

- **Answer (tutor only):** A
- **Explanation (tutor only):** The bootstrap SE is the SD of the bootstrap estimates.
- **Why the wrong options are wrong (tutor only):**
  B) That's the SD of individual observations.
  C) That's the center of the bootstrap distribution.
  D) The number of replicates isn't the sample size.
- **Hint:** SE = spread of estimates.

### ch09-chime-07
- **Kind:** Course original
- **Concepts:** Sampling distribution & SE; Bootstrap
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

### ch09-chime-07-v1
- **Kind:** AI-written version of ch09-chime-07
- **Concepts:** Sampling distribution & SE
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

### ch09-chime-07-v2
- **Kind:** AI-written version of ch09-chime-07
- **Concepts:** Sampling distribution & SE
- **Type:** MC
- **Question:**

For a sample of size n = 1, how would the standard error of the mean compare to the standard deviation?

- **Options:**

  A) They'd be the same (SD/√1 = SD), because the 'mean' of one observation is just that observation
  B) The SE would be smaller
  C) The SE would be larger
  D) The SE would be zero

- **Answer (tutor only):** A
- **Explanation (tutor only):** With one observation, its mean varies exactly as much as individuals do. Averaging only reduces spread when n > 1. (In practice you can't estimate an SD from one value, but the idea holds.)
- **Why the wrong options are wrong (tutor only):**
  B) Only with n > 1.
  C) The SE is never larger than the SD.
  D) Different samples of one would give different values.
- **Hint:** Plug n = 1 into SD/√n.

### ch09-chime-08
- **Kind:** Course original
- **Concepts:** Sampling distribution & SE; Bootstrap
- **Type:** MC
- **Question:**

True or false: the bootstrap is the only way to approximate a sampling distribution.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** Mathematical approaches (e.g., SE = SD/√n with the normal or t distribution) also approximate it. We'll use those later in the course.
- **Why the wrong options are wrong (tutor only):**
  A) The bootstrap is one tool among several.
- **Hint:** Have you seen a formula for the standard error?

### ch09-chime-08-v1
- **Kind:** AI-written version of ch09-chime-08
- **Concepts:** Sampling distribution & SE; Bootstrap
- **Type:** MC
- **Question:**

Which is a non-bootstrap way to estimate the standard error of a mean?

- **Options:**

  A) SE = SD/√n
  B) SE = the mean/√n
  C) SE = the range/2
  D) There is none

- **Answer (tutor only):** A
- **Explanation (tutor only):** The mathematical formula SE = SD/√n approximates the spread of the sampling distribution of the mean without any resampling.
- **Why the wrong options are wrong (tutor only):**
  B) The mean doesn't determine the spread.
  C) Half the range isn't an SE.
  D) Math-based approaches exist (and we'll use them later).
- **Hint:** The formula with √n.

### ch09-chime-08-v2
- **Kind:** AI-written version of ch09-chime-08
- **Concepts:** Bootstrap
- **Type:** TF
- **Question:**

True or false: the bootstrap requires the data to be normally distributed.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** The bootstrap just resamples your data; it makes no normality assumption. (It does need a reasonably large, representative sample.)
- **Why the wrong options are wrong (tutor only):**
  A) Many formula-based methods lean on normality; the bootstrap doesn't.
- **Hint:** What does the bootstrap actually do with your data?

### ch09-chime-09
- **Kind:** Course original
- **Concepts:** Confidence intervals
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-gquiz-ringtoss.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-gquiz-ringtoss.png)
- **Question:**

You have correctly calculated a 95% confidence interval from a sample. What is the probability it contains the true population parameter? (Select all correct.)

- **Options:**

  A) 95%
  B) Depends on sample size
  C) Depends on standard deviation
  D) There is no probability about this; it either did or it didn't

- **Answer (tutor only):** D
- **Explanation (tutor only):** Once the interval is calculated, both it and the parameter are fixed. It caught the parameter or it didn't.
- **Why the wrong options are wrong (tutor only):**
  A) 95% is the long-run rate of the method, not the chance for this interval.
  B) and C) These affect width, not interpretation.
- **Hint:** Before or after the sample was taken?

### ch09-chime-09-v1
- **Kind:** AI-written version of ch09-chime-09
- **Concepts:** Confidence intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-gquiz-ringtoss.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-gquiz-ringtoss.png)
- **Question:**

You calculated a 90% CI for mean wing length: 41.2 to 43.0 mm. Which statement is correct?

- **Options:**

  A) This interval either contains the true mean or it doesn't; 90% of intervals made this way capture the truth
  B) There's a 90% chance the true mean is in 41.2–43.0
  C) 90% of birds have wings 41.2–43.0 mm
  D) There's a 10% chance the true mean is outside this interval

- **Answer (tutor only):** A
- **Explanation (tutor only):** Once calculated, the interval is fixed and the mean is fixed. The 90% describes the long-run success rate of the procedure.
- **Why the wrong options are wrong (tutor only):**
  B) and D) These attach probability to this one finished interval.
  C) The CI is about the mean, not individuals.
- **Hint:** Before vs after calculating.

### ch09-chime-09-v2
- **Kind:** AI-written version of ch09-chime-09
- **Concepts:** Confidence intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-gquiz-ringtoss.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-gquiz-ringtoss.png)
- **Question:**

Two researchers each compute a correct 95% CI from different samples. Researcher 1's is narrower. Which is true?

- **Options:**

  A) Researcher 1's estimate is more precise, but neither interval has a 'probability' of containing the truth once calculated
  B) Researcher 1's interval has a higher probability of containing the truth
  C) Researcher 1's interval is less likely to contain the truth
  D) The narrower interval must be biased

- **Answer (tutor only):** A
- **Explanation (tutor only):** Width reflects precision (sample size, variability). Both come from 95% methods; after calculation each one simply did or didn't capture the parameter.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Width doesn't change the interpretation for a finished interval.
  D) Narrow means precise, not biased.
- **Hint:** What does width tell you?

### ch09-chime-10
- **Kind:** Course original
- **Concepts:** Confidence intervals
- **Type:** MC
- **Question:**

You will conduct 100 experiments in your life. What proportion of their 95% confidence intervals do you expect to contain the true parameter being estimated?

- **Options:**

  A) 0.95
  B) Depends on sample size
  C) Depends on standard deviation
  D) There is no probability about this; they will or they won't

- **Answer (tutor only):** A
- **Explanation (tutor only):** Looking ahead at many future intervals, the method's 95% success rate applies: expect about 95 of 100 to catch their parameters.
- **Why the wrong options are wrong (tutor only):**
  B) and C) These affect width, not coverage.
  D) That's true of each finished interval, but this question is about the long-run proportion before they're made.
- **Hint:** Are you being asked about one finished interval, or about the long-run proportion of many future intervals?

### ch09-chime-10-v1
- **Kind:** AI-written version of ch09-chime-10
- **Concepts:** Confidence intervals
- **Type:** MC
- **Question:**

Over your career you will compute 40 independent 95% confidence intervals. About how many do you expect to MISS their true parameter?

- **Options:**

  A) About 2
  B) 0
  C) About 5
  D) About 38

- **Answer (tutor only):** A
- **Explanation (tutor only):** 5% of 40 is 2, so expect about 2 misses (and you won't know which ones).
- **Why the wrong options are wrong (tutor only):**
  B) 95% isn't 100%.
  C) That's 5 of 100, not 5% of 40.
  D) That's how many succeed.
- **Hint:** 5% of 40.

### ch09-chime-10-v2
- **Kind:** AI-written version of ch09-chime-10
- **Concepts:** Confidence intervals
- **Type:** MC
- **Question:**

Before collecting any data, what is the probability that the 99% CI you're about to compute will contain the true parameter?

- **Options:**

  A) 0.99
  B) 0.01
  C) It either will or won't, so there's no probability
  D) It depends on the sample mean

- **Answer (tutor only):** A
- **Explanation (tutor only):** Before sampling, the outcome is still random, so the method's 99% success rate applies. Only after calculation does it become 'did or didn't'.
- **Why the wrong options are wrong (tutor only):**
  B) That's the chance of missing.
  C) That applies after the interval is calculated.
  D) The sample mean doesn't exist yet.
- **Hint:** Has the randomness happened yet?

### ch09-gquiz-01
- **Kind:** Course original
- **Concepts:** Sampling distribution & SE
- **Type:** MC
- **Question:**

Which statement best describes the sampling distribution and how it relates to sampling error and uncertainty?

- **Options:**

  A) It's the distribution of estimates we would get from many samples of the same size; its spread reflects sampling error, so it tells us how uncertain any single estimate is
  B) It's the distribution of values in our sample; its spread is the standard deviation
  C) It's the distribution of individuals in the population; it shows sampling bias
  D) It's what we get after removing sampling error from our data

- **Answer (tutor only):** A
- **Explanation (tutor only):** Each sample gives a slightly different estimate by chance (sampling error). The sampling distribution collects all those possible estimates; its SD is the standard error, our measure of uncertainty.
- **Why the wrong options are wrong (tutor only):**
  B) That's the sample distribution.
  C) That's the population distribution, and bias is about the center, not this idea.
  D) Sampling error can't be removed, only described.
- **Hint:** Distribution of what: individuals or estimates?

### ch09-gquiz-01-v1
- **Kind:** AI-written version of ch09-gquiz-01
- **Concepts:** Sampling distribution & SE
- **Type:** MC
- **Question:**

If we could draw 10,000 samples of 25 penguins and compute each sample's mean body mass, the histogram of those 10,000 means would be:

- **Options:**

  A) The sampling distribution of the mean; its spread is the standard error
  B) The population distribution of body mass
  C) The sample distribution; its spread is the standard deviation
  D) A bootstrap distribution

- **Answer (tutor only):** A
- **Explanation (tutor only):** A distribution of estimates from many independent samples of the same size is the sampling distribution. Its SD is the standard error.
- **Why the wrong options are wrong (tutor only):**
  B) The population distribution describes individual penguins.
  C) A sample distribution is the values in one sample.
  D) A bootstrap resamples one sample; here we drew new samples from the population.
- **Hint:** Is each value in the histogram an individual or an estimate?

### ch09-gquiz-01-v2
- **Kind:** AI-written version of ch09-gquiz-01
- **Concepts:** Sampling distribution & SE
- **Type:** MC
- **Question:**

Two sampling distributions of a mean are centered on the true value. One is narrow, the other wide. What does the wide one tell you?

- **Options:**

  A) Any single estimate from that design is likely to land farther from the truth (more sampling error, more uncertainty)
  B) That design is biased
  C) The population is more variable than the sample
  D) The estimate is wrong

- **Answer (tutor only):** A
- **Explanation (tutor only):** A wider sampling distribution means estimates scatter more from sample to sample, so one estimate is less precise. Both are centered on the truth, so neither is biased.
- **Why the wrong options are wrong (tutor only):**
  B) Both are centered on the truth, so neither is biased.
  C) Spread here is spread of estimates, not individuals.
  D) It's imprecise, not wrong.
- **Hint:** Spread of a sampling distribution = ?

### ch09-gquiz-02
- **Kind:** Course original
- **Concepts:** Bootstrap
- **Type:** MC
- **Question:**

How does the bootstrap approximate the sampling distribution?

- **Options:**

  A) Resample the data WITH replacement, making each resample the same size as the original sample; calculate the estimate (e.g., the mean) for each resample; repeat many times
  B) Resample the data WITHOUT replacement, same size as the original; calculate the estimate; repeat
  C) Take new samples from the population many times and calculate the estimate for each
  D) Resample WITH replacement, but make each resample much larger than the original sample to reduce error

- **Answer (tutor only):** A
- **Explanation (tutor only):** With replacement and the same n means each resample is a plausible alternative sample: some observations show up twice, some not at all. The spread of the estimates across resamples approximates the sampling distribution.
- **Why the wrong options are wrong (tutor only):**
  B) Without replacement, every resample is just the original data shuffled, so every estimate is identical.
  C) That's the true sampling distribution; in real studies we can't keep resampling the population.
  D) Uncertainty depends on n; bigger resamples would understate it.
- **Hint:** What happens if you resample n values from n values without replacement?

### ch09-gquiz-02-v1
- **Kind:** AI-written version of ch09-gquiz-02
- **Concepts:** Bootstrap
- **Type:** MC
- **Question:**

Your sample has 30 seed masses. Which describes ONE bootstrap replicate?

- **Options:**

  A) Draw 30 values from your 30 with replacement, then compute the mean
  B) Draw 30 values from your 30 without replacement, then compute the mean
  C) Draw 10 values with replacement, then compute the mean
  D) Collect 30 new seeds from the field, then compute the mean

- **Answer (tutor only):** A
- **Explanation (tutor only):** Same size (30), with replacement: some seeds appear twice, some not at all. Computing the estimate on that resample gives one bootstrap replicate.
- **Why the wrong options are wrong (tutor only):**
  B) Without replacement you just reshuffle the same 30, so every mean is identical.
  C) Smaller resamples overstate uncertainty.
  D) That's a new sample from the population, not a bootstrap.
- **Hint:** Same n, and with or without replacement?

### ch09-gquiz-02-v2
- **Kind:** AI-written version of ch09-gquiz-02
- **Concepts:** Bootstrap
- **Type:** MC
- **Question:**

A student bootstraps by sampling WITHOUT replacement (same size as the data). What happens?

- **Options:**

  A) Every resample contains exactly the original data, so every bootstrap mean is identical and the SE looks like 0
  B) The bootstrap SE is slightly too large
  C) It works the same as sampling with replacement
  D) The bootstrap distribution becomes bimodal

- **Answer (tutor only):** A
- **Explanation (tutor only):** Drawing all n values without replacement just reorders the data, and the mean doesn't depend on order, so there's no variation.
- **Why the wrong options are wrong (tutor only):**
  B) There is no variation at all, not a little extra.
  C) Replacement is what creates variation among resamples.
  D) There's no spread at all.
- **Hint:** What's in a 'resample' if no value can be drawn twice?

### ch09-gquiz-03
- **Kind:** Course original
- **Concepts:** Sampling distribution & SE; Bootstrap
- **Type:** MC
- **Question:**

Why does bootstrapping do a poor job of approximating the sampling distribution when the sample size is very small?

- **Options:**

  A) The bootstrap can only resample the few values we observed, so a tiny sample poorly represents the population's spread and shape; bootstrap distributions are then lumpy and tend to understate uncertainty
  B) Small samples are always biased
  C) The bootstrap needs at least 1000 observations to run
  D) With small samples you must resample without replacement

- **Answer (tutor only):** A
- **Explanation (tutor only):** The bootstrap treats your sample as a stand-in for the population. With, say, 5 values, that stand-in is crude: there are few distinct resamples, extremes are missing, and the bootstrap spread is often too narrow.
- **Why the wrong options are wrong (tutor only):**
  B) Small random samples are noisy, not biased.
  C) It runs fine; it just approximates poorly.
  D) Without replacement, every resample is identical.
- **Hint:** What does the bootstrap use as its 'population'?

### ch09-gquiz-03-v1
- **Kind:** AI-written version of ch09-gquiz-03
- **Concepts:** Sampling distribution & SE; Bootstrap
- **Type:** MC
- **Question:**

A researcher has only 4 measurements: 2.1, 2.3, 2.4, 9.8. Why should they be cautious about a bootstrap CI?

- **Options:**

  A) The bootstrap can only reshuffle these 4 values, so it poorly reflects the population and its uncertainty; the resulting distribution is lumpy and often too narrow
  B) The bootstrap requires normal data
  C) The bootstrap needs at least 100 values to run
  D) With 4 values, sampling with replacement is impossible

- **Answer (tutor only):** A
- **Explanation (tutor only):** With tiny samples the bootstrap's stand-in population is crude: few distinct resamples, and one odd value (9.8) dominates. Bootstrap intervals tend to understate uncertainty.
- **Why the wrong options are wrong (tutor only):**
  B) The bootstrap doesn't assume normality.
  C) It runs; it just approximates poorly.
  D) You can resample with replacement from any sample.
- **Hint:** The bootstrap treats your sample as the population. How good is a 4-value population?

### ch09-gquiz-03-v2
- **Kind:** AI-written version of ch09-gquiz-03
- **Concepts:** Sampling distribution & SE; Bootstrap
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

### ch09-gquiz-04
- **Kind:** Course original
- **Concepts:** Difference in means & Cohen's d; Confidence intervals
- **Type:** MC
- **Question:**

A study compared the proportion of correct predictions made by professional astrologers vs random guessers (prop_correct). Cohen's d (astrologers − guessers) = 0.27, 95% CI [0.05, 0.48]. Benchmarks: tiny 0.01–0.20, small 0.20–0.50, medium 0.50–0.80, large 0.80–1.20. What does this mean?

- **Options:**

  A) Astrologers did slightly better than guessers (a small effect); the plausible range runs from tiny to almost medium, and it excludes zero
  B) Astrologers did much better than guessers; a large effect
  C) There's a 95% chance the true d is exactly 0.27
  D) Because the CI includes small values, there is no difference

- **Answer (tutor only):** A
- **Explanation (tutor only):** d = 0.27 is 'small' by convention. The CI [0.05, 0.48] says effects from tiny (0.05) to nearly medium (0.48) are consistent with the data. The CI doesn't include 0, but the plausible effect is modest at best.
- **Why the wrong options are wrong (tutor only):**
  B) 0.27 is small, not large.
  C) The CI gives a range; 0.27 is our best estimate, not the truth.
  D) The CI excludes 0, so 'no difference' isn't supported.
- **Hint:** Read the point estimate first, then the range.

### ch09-gquiz-04-v1
- **Kind:** AI-written version of ch09-gquiz-04
- **Concepts:** Difference in means & Cohen's d; Confidence intervals
- **Type:** MC
- **Question:**

A study compared plant height with vs without fertilizer. Cohen's d (fertilized − control) = 0.95, 95% CI [0.60, 1.30]. Benchmarks: tiny 0.01–0.20, small 0.20–0.50, medium 0.50–0.80, large 0.80–1.20, very large > 1.20. What does this mean?

- **Options:**

  A) Fertilized plants were taller, a large effect; plausible values run from medium to very large, and zero is not plausible
  B) A small effect that could be zero
  C) There's a 95% chance the true d is 0.95
  D) Because the CI is wide, we can't say anything

- **Answer (tutor only):** A
- **Explanation (tutor only):** 0.95 is a large effect. The CI [0.60, 1.30] spans medium to very large and excludes 0, so the data support a substantial positive effect.
- **Why the wrong options are wrong (tutor only):**
  B) 0.95 is large, and the CI excludes 0.
  C) 0.95 is the best estimate; the CI gives a plausible range.
  D) Even the low end (0.60) is a medium effect.
- **Hint:** Place both the estimate and the CI ends on the benchmark scale.

### ch09-gquiz-04-v2
- **Kind:** AI-written version of ch09-gquiz-04
- **Concepts:** Difference in means & Cohen's d; Confidence intervals
- **Type:** MC
- **Question:**

Caffeinated vs decaf students' quiz scores: Cohen's d (caffeine − decaf) = 0.12, 95% CI [−0.15, 0.39]. Benchmarks: tiny 0.01–0.20, small 0.20–0.50, medium 0.50–0.80. What's the best summary?

- **Options:**

  A) The estimated effect is tiny; plausible values range from a slight disadvantage to a small advantage, including zero, so the data don't establish an effect either way
  B) Caffeine has a small positive effect
  C) Caffeine has no effect
  D) There's a 95% chance d is between −0.15 and 0.39

- **Answer (tutor only):** A
- **Explanation (tutor only):** The CI includes 0 and spans small negative to small positive effects. We can't conclude there's an effect, nor that it's exactly zero; any effect is likely small.
- **Why the wrong options are wrong (tutor only):**
  B) The CI includes 0 and negative values.
  C) Failing to show an effect isn't showing no effect.
  D) The 95% belongs to the method, not to this interval.
- **Hint:** Does the CI include 0? How big are the plausible effects?

### ch09-gquiz-05
- **Kind:** Course original
- **Concepts:** Sampling distribution & SE; Bootstrap; Confidence intervals
- **Type:** MC
- **Question:**

We bootstrapped the slope of sepal length on sepal width for Iris versicolor (1000 bootstrap replicates; each replicate's slope is called stat). How would we get the bootstrap standard error and the 95% confidence interval from these 1000 slopes?

- **Options:**

  A) SE = standard deviation of the 1000 slopes; 95% CI = their 2.5th and 97.5th percentiles
  B) SE = mean of the 1000 slopes; 95% CI = their 5th and 95th percentiles
  C) SE = standard deviation of the 1000 slopes; 95% CI = their 5th and 95th percentiles
  D) SE = the original slope / √1000; 95% CI = their minimum and maximum

- **Answer (tutor only):** A
- **Explanation (tutor only):** The bootstrap distribution approximates the sampling distribution, so its SD is the SE. A 95% CI leaves 2.5% in each tail, so use the 2.5th and 97.5th percentiles (quantile(stat, 0.025) and quantile(stat, 0.975)).
- **Why the wrong options are wrong (tutor only):**
  B) The mean of the replicates is near the estimate itself, not its uncertainty.
  C) 5th to 95th percentiles is a 90% interval.
  D) The number of replicates isn't the sample size, and min–max isn't a 95% interval.
- **Hint:** 95% in the middle leaves how much in each tail?

### ch09-gquiz-05-v1
- **Kind:** AI-written version of ch09-gquiz-05
- **Concepts:** Bootstrap; Confidence intervals
- **Type:** MC
- **Question:**

You have 2000 bootstrap replicates of a correlation coefficient. How do you get a 90% bootstrap confidence interval?

- **Options:**

  A) The 5th and 95th percentiles of the 2000 replicates
  B) The 2.5th and 97.5th percentiles
  C) The mean ± the standard deviation of the replicates
  D) The minimum and maximum of the replicates

- **Answer (tutor only):** A
- **Explanation (tutor only):** A 90% interval leaves 5% in each tail, so use the 5th and 95th percentiles.
- **Why the wrong options are wrong (tutor only):**
  B) That's a 95% interval.
  C) Mean ± 1 SD covers roughly 68%.
  D) The min–max covers essentially 100%, and depends on the number of replicates.
- **Hint:** How much goes in each tail for 90%?

### ch09-gquiz-05-v2
- **Kind:** AI-written version of ch09-gquiz-05
- **Concepts:** Sampling distribution & SE; Bootstrap
- **Type:** MC
- **Question:**

Bootstrapping a median gives 1000 replicate medians with mean 12.4 and standard deviation 0.9. The original sample median was 12.3. What's the bootstrap SE of the median?

- **Options:**

  A) 0.9
  B) 12.4
  C) 0.9 / √1000
  D) 12.3 / √1000

- **Answer (tutor only):** A
- **Explanation (tutor only):** The bootstrap SE is the SD of the bootstrap replicates: 0.9.
- **Why the wrong options are wrong (tutor only):**
  B) That's the center of the bootstrap distribution, close to the estimate itself.
  C) and D) The number of replicates isn't the sample size; don't divide by √1000.
- **Hint:** SE = spread of the estimates.

### ch09-gquiz-06
- **Kind:** Course original
- **Concepts:** Visualizing uncertainty
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-gquiz-astrology-plots.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-gquiz-astrology-plots.png)
- **Question:**

A study compared the proportion of correct predictions made by professional astrologers vs random guessers (prop_correct).

Two plots show the same data. Plot A: raw points plus each group's mean with error bars. Plot B: raw points plus boxplots.

1. Which plot highlights variability among individuals?
2. Which plot highlights uncertainty in the estimated means?

- **Options:**

  A) Plot A
  B) Plot B

- **Answer (tutor only):** 1-B, 2-A
- **Explanation (tutor only):** Boxplots summarize the spread of individuals (quartiles, range). Error bars around the means show uncertainty in the estimated means (SE or CI), which is much narrower than the spread of the data.
- **Why the wrong options are wrong (tutor only):**
  Error bars are not the spread of the data: they shrink with n, but individual variability doesn't.
- **Hint:** What would happen to each summary with 10× as much data?

### ch09-gquiz-06-v1
- **Kind:** AI-written version of ch09-gquiz-06
- **Concepts:** Visualizing uncertainty
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-var-penguin-twoplots.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-var-penguin-twoplots.png)
- **Question:**

Two plots show the same penguin body masses. Plot A: raw points plus boxplots. Plot B: raw points plus each species' mean with 95% CI error bars.

1. Which plot shows how much individual penguins differ?
2. Which plot shows how precisely we've estimated each species' mean?

- **Options:**

  A) Plot A
  B) Plot B

- **Answer (tutor only):** 1-A, 2-B
- **Explanation (tutor only):** Boxplots summarize individuals (quartiles, whiskers). Error bars around the means show uncertainty in the mean, which is much narrower than the spread of birds.
- **Why the wrong options are wrong (tutor only):**
  Error bars ≠ spread of the data: they shrink as n grows, but individual variation doesn't.
- **Hint:** Which plot's summary is about individuals?

### ch09-gquiz-06-v2
- **Kind:** AI-written version of ch09-gquiz-06
- **Concepts:** Visualizing uncertainty
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-var-penguin-twoplots.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-var-penguin-twoplots.png)
- **Question:**

In Plot B, the 95% CI error bars for Adelie and Chinstrap mean body mass overlap heavily, yet the raw points span about 2700–4800 g. Why are the error bars so much shorter than the spread of points?

- **Options:**

  A) Error bars show uncertainty in the mean (≈ SD/√n), which is much smaller than the variation among individual penguins
  B) The error bars hide the outliers
  C) The error bars show the interquartile range
  D) Error bars are drawn at a different scale

- **Answer (tutor only):** A
- **Explanation (tutor only):** A mean of about 70–150 birds is far more stable than any single bird, so the CI for the mean is narrow even though individuals vary a lot.
- **Why the wrong options are wrong (tutor only):**
  B) Error bars aren't about outliers.
  C) That's what a boxplot's box shows.
  D) Same y-axis.
- **Hint:** What does dividing by √n do?

### ch09-gquiz-07
- **Kind:** Course original
- **Concepts:** Confidence intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-gquiz-ringtoss.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-gquiz-ringtoss.png)
- **Question:**

People often say a 95% CI is 'the interval with a 95% chance of capturing the true parameter.' Statisticians prefer: '95% of confidence intervals from samples of a population will include the true parameter.' The cartoon contrasts archery (target fixed, arrow might hit) with ring toss (true value fixed, ring might land around it). What's the key difference?

- **Options:**

  A) The probability belongs to the process of making intervals (tossing rings); the true value is fixed, and any single interval either caught it or didn't
  B) The true parameter moves around, and the interval might catch it
  C) There is no difference; it's just wording
  D) 95% CIs are wrong 95% of the time

- **Answer (tutor only):** A
- **Explanation (tutor only):** Like a coin already flipped under a cup: it's heads or tails, not '50% heads.' Before sampling, the method has a 95% chance of catching the parameter. After, your interval is right or wrong. (Whether to police this in everyday speech is a fair debate.)
- **Why the wrong options are wrong (tutor only):**
  B) The parameter is fixed (the post in ring toss).
  C) It's a real conceptual difference about where the randomness lives.
  D) They miss about 5% of the time.
- **Hint:** In ring toss, what moves: the post or the ring?

### ch09-gquiz-07-v1
- **Kind:** AI-written version of ch09-gquiz-07
- **Concepts:** Confidence intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-gquiz-ringtoss.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-gquiz-ringtoss.png)
- **Question:**

A coin is flipped and hidden under a cup. A friend says 'there's a 50% chance it's heads.' How does this relate to a calculated 95% CI?

- **Options:**

  A) Like the coin, the interval's outcome is already settled: it caught the parameter or it didn't; the 95% describes the procedure before it's run
  B) The 95% CI has a 95% chance of containing the parameter, just as the coin is 50% heads
  C) The parameter moves like a flipping coin
  D) The analogy shows CIs are useless

- **Answer (tutor only):** A
- **Explanation (tutor only):** Before flipping, P(heads) = 0.5. After, it's heads or tails. Likewise, before sampling the method has a 95% chance to succeed; after, the interval is right or wrong. (Many people still talk loosely here.)
- **Why the wrong options are wrong (tutor only):**
  B) That's the loose reading statisticians object to.
  C) The parameter is fixed.
  D) CIs are useful; the analogy is about interpretation.
- **Hint:** Before vs after the randomness happens.

### ch09-gquiz-07-v2
- **Kind:** AI-written version of ch09-gquiz-07
- **Concepts:** Confidence intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-gquiz-ringtoss.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-gquiz-ringtoss.png)
- **Question:**

In the ring toss analogy for confidence intervals, what are the post and the ring?

- **Options:**

  A) Post = the true parameter (fixed); ring = the interval (random, changes with each sample)
  B) Post = the interval; ring = the parameter
  C) Post = the sample mean; ring = the population
  D) Both move each time

- **Answer (tutor only):** A
- **Explanation (tutor only):** The truth stays put; each sample produces a new interval that may or may not land around it. 95% CIs are a ring-toss method that rings the post 95% of the time.
- **Why the wrong options are wrong (tutor only):**
  B) The interval is what varies across samples.
  C) The sample mean changes; the post doesn't.
  D) The parameter is fixed.
- **Hint:** Which thing changes from sample to sample?

### ch09-hw-01
- **Kind:** Course original
- **Concepts:** Sampling distribution & SE; Bootstrap
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

### ch09-hw-01-v1
- **Kind:** AI-written version of ch09-hw-01
- **Concepts:** Sampling distribution & SE; Bootstrap
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

### ch09-hw-01-v2
- **Kind:** AI-written version of ch09-hw-01
- **Concepts:** Sampling distribution & SE
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

### ch09-hw-02
- **Kind:** Course original
- **Concepts:** Sampling distribution & SE; Confidence intervals
- **Type:** select-all
- **Question:**

Which of the following quantities typically increase when the sample size gets smaller? (Select all that apply.)

- **Options:**

  A) Standard error
  B) Sample median
  C) Width of a 99% confidence interval
  D) The variance

- **Answer (tutor only):** A, C
- **Explanation (tutor only):** Smaller samples mean more sampling error, so the SE and CI width grow. Estimates of the median and variance get less precise with small n, but they don't systematically get bigger.
- **Why the wrong options are wrong (tutor only):**
  B) and D) They become noisier, not larger. (Without Bessel's correction the variance would actually be underestimated.)
- **Hint:** Which of these measure uncertainty in an estimate, rather than describing the data?

### ch09-hw-02-v1
- **Kind:** AI-written version of ch09-hw-02
- **Concepts:** Sampling distribution & SE; Confidence intervals
- **Type:** select-all
- **Question:**

A team doubles its sample size from 40 to 80 plants. Which quantities would you expect to get smaller? (Select all that apply.)

- **Options:**

  A) The standard error of the mean
  B) The standard deviation of plant height
  C) The width of a 95% confidence interval for the mean
  D) The mean plant height

- **Answer (tutor only):** A, C
- **Explanation (tutor only):** More data means less uncertainty: the SE (≈ SD/√n) and the CI width shrink. The SD and mean describe the plants themselves; they get estimated more precisely but don't trend smaller.
- **Why the wrong options are wrong (tutor only):**
  B) The SD describes how much plants differ; adding plants doesn't make them more alike.
  D) The mean doesn't depend on how many plants you measure.
- **Hint:** Which of these describe uncertainty in an estimate, and which describe the plants?

### ch09-hw-02-v2
- **Kind:** AI-written version of ch09-hw-02
- **Concepts:** Sampling distribution & SE; Confidence intervals
- **Type:** select-all
- **Question:**

Researcher 1 samples 15 fish; Researcher 2 samples 150 fish from the same lake. Which will tend to be LARGER for Researcher 1? (Select all that apply.)

- **Options:**

  A) The standard error of mean fish length
  B) The width of a 90% confidence interval for mean length
  C) The sample mean length
  D) The sample standard deviation of length

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** Smaller samples give less precise estimates, so the SE and CI width are larger. The mean and SD are just noisier with n = 15, not systematically bigger.
- **Why the wrong options are wrong (tutor only):**
  C) and D) These vary more from sample to sample with small n, but they don't trend upward.
- **Hint:** Which quantities measure precision?

### ch09-hw-03
- **Kind:** Course original
- **Concepts:** Confidence intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-gquiz-ringtoss.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-gquiz-ringtoss.png)
- **Question:**

You calculate a 95% confidence interval from one random sample. Which statement is correct about this CI?

- **Options:**

  A) There's a 95% chance the true value is inside this interval
  B) Either the interval contains the true value or it doesn't; there's no probability anymore
  C) Larger samples make the interval more likely to contain the parameter
  D) The population parameter changes depending on the sample

- **Answer (tutor only):** B
- **Explanation (tutor only):** The parameter is fixed and, once calculated, so is your interval. The 95% describes the method: 95% of intervals made this way catch the truth. Any one interval simply did or didn't.
- **Why the wrong options are wrong (tutor only):**
  A) The common misreading: the probability applies to the process, not to this interval.
  C) Larger samples make intervals narrower, but still 95% of them catch the parameter.
  D) The parameter is fixed; it's the estimate that changes.
- **Hint:** Is anything random left once the interval is calculated?

### ch09-hw-03-v1
- **Kind:** AI-written version of ch09-hw-03
- **Concepts:** Confidence intervals
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-gquiz-ringtoss.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-gquiz-ringtoss.png)
- **Question:**

From one random sample of lakes you calculate a 95% CI for mean phosphorus: 12.1 to 15.8 µg/L. Which statement is correct?

- **Options:**

  A) There is a 95% probability the true mean is between 12.1 and 15.8
  B) If we repeated the study many times, about 95% of intervals made this way would contain the true mean; this interval either does or doesn't
  C) 95% of lakes have phosphorus between 12.1 and 15.8
  D) The true mean changes depending on which lakes we sampled

- **Answer (tutor only):** B
- **Explanation (tutor only):** The 95% is about the method. The true mean is fixed, and so is this interval once calculated, so it simply did or didn't catch the truth.
- **Why the wrong options are wrong (tutor only):**
  A) The common misreading: the probability belongs to the process.
  C) The CI is for the mean, not for individual lakes.
  D) The parameter is fixed; estimates change.
- **Hint:** Where does the randomness live: in the parameter or the procedure?

### ch09-hw-03-v2
- **Kind:** AI-written version of ch09-hw-03
- **Concepts:** Confidence intervals
- **Type:** TF
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch09-gquiz-ringtoss.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch09-gquiz-ringtoss.png)
- **Question:**

True or false: after you calculate a 95% CI of 4.2 to 6.8, the probability that the true mean lies in that range is 0.95.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** Once calculated, the interval and the parameter are both fixed numbers, so it did or didn't capture it. The 0.95 describes how often the procedure works across many samples.
- **Why the wrong options are wrong (tutor only):**
  A) This is the tempting misreading: 95% is a property of the method, not of this one interval.
- **Hint:** Think of a ring already tossed at a post.

### ch09-hw-04
- **Kind:** Course original
- **Concepts:** Confidence intervals
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

### ch09-hw-04-v1
- **Kind:** AI-written version of ch09-hw-04
- **Concepts:** Confidence intervals
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

### ch09-hw-04-v2
- **Kind:** AI-written version of ch09-hw-04
- **Concepts:** Confidence intervals
- **Type:** MC
- **Question:**

50 labs each compute a 99% confidence interval for the same parameter. About how many intervals would you expect to contain the true parameter?

- **Options:**

  A) All 50, guaranteed
  B) About 49 or 50
  C) About 45
  D) It depends on each lab's sample mean

- **Answer (tutor only):** B
- **Explanation (tutor only):** 99% of 50 is 49.5, so expect almost all of them, with perhaps one miss.
- **Why the wrong options are wrong (tutor only):**
  A) Even 99% intervals miss sometimes.
  C) That's 90% coverage.
  D) Coverage is a property of the method, not of any one sample.
- **Hint:** Multiply the number of intervals by the confidence level.
