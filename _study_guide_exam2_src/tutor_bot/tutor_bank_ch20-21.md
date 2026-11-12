# Applied Biostats tutor: question bank, chapters 20–21 (Exam 2, chapters 13–21, plus an Exam 1 review as chapter 0)

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

## Chapter 20: Multiple Predictors

### ch20-book-01
- **Kind:** Course original
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

How many explanatory variables does this model include?

- **Options:**

  A) One
  B) Two
  C) Three
  D) Four

- **Answer (tutor only):** B
- **Explanation (tutor only):** Sepal length and species. Species has three levels, so it gets two coefficients, but it's still one variable.
- **Why the wrong options are wrong (tutor only):**
  C) and D) Count coefficients, not variables.
- **Hint:** Variables vs coefficients.

### ch20-book-01-v1
- **Kind:** AI-written version of ch20-book-01
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

How many coefficients does this model estimate, including the intercept?

- **Options:**

  A) Four
  B) Five
  C) Three
  D) Two

- **Answer (tutor only):** A
- **Explanation (tutor only):** Intercept, Sepal.Length, Speciesversicolor and Speciesvirginica.
- **Why the wrong options are wrong (tutor only):**
  Count the coefficients in the output.
- **Hint:** Count them.

### ch20-book-01-v2
- **Kind:** AI-written version of ch20-book-01
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

Why does species get two coefficients?

- **Options:**

  A) It is the most important predictor
  B) Each species has two flowers sampled
  C) It has three levels: one is the reference
  D) Species interacts with sepal length

- **Answer (tutor only):** C
- **Explanation (tutor only):** A categorical variable with k levels gets k - 1 coefficients.
- **Why the wrong options are wrong (tutor only):**
  A) Importance doesn't set the count.
  B) Irrelevant.
  D) There's no interaction term.
- **Hint:** k - 1.

### ch20-book-02
- **Kind:** Course original
- **Concepts:** Coefficients & predictions; Adjusting vs controlling
- **Type:** MC
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

The Sepal.Length coefficient (0.63) is the expected change in petal length for a 1 cm increase in sepal length:

- **Options:**

  A) Without accounting for species
  B) After controlling for species
  C) After adjusting for species and petal width
  D) Only for setosa plants
  E) After adjusting for species

- **Answer (tutor only):** E
- **Explanation (tutor only):** It's the shared within-species slope, after statistically adjusting for species.
- **Why the wrong options are wrong (tutor only):**
  A) Species is in the model.
  B) 'Controlling' implies an experiment.
  C) Petal width isn't in the model.
  D) In an additive model the slope is the same for all species.
- **Hint:** What else is in the model, and how was it 'held constant'?

### ch20-book-02-v1
- **Kind:** AI-written version of ch20-book-02
- **Concepts:** Coefficients & predictions; Adjusting vs controlling
- **Type:** MC
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

Using the model, what is the predicted petal length of a setosa flower with a sepal length of 5 cm?

- **Options:**

  A) About 0.63 cm
  B) About 4.55 cm
  C) About 1.46 cm
  D) About 3.67 cm

- **Answer (tutor only):** C
- **Explanation (tutor only):** -1.7023 + 0.6321 × 5 = 1.458 cm (setosa is the reference).
- **Why the wrong options are wrong (tutor only):**
  A) That's the slope.
  B) Adds the virginica coefficient.
  D) Adds the versicolor coefficient.
- **Hint:** Setosa is the reference level.

### ch20-book-02-v2
- **Kind:** AI-written version of ch20-book-02
- **Concepts:** Coefficients & predictions; Adjusting vs controlling
- **Type:** MC
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

Two virginica flowers differ in sepal length by 2 cm. How much does their predicted petal length differ?

- **Options:**

  A) About 3.09 cm
  B) About 0.63 cm
  C) About 6.18 cm
  D) About 1.26 cm

- **Answer (tutor only):** D
- **Explanation (tutor only):** 0.6321 × 2 = 1.26 cm.
- **Why the wrong options are wrong (tutor only):**
  A) The virginica coefficient.
  B) For 1 cm.
  C) 2 × 3.09.
- **Hint:** Slope × difference.

### ch20-book-03
- **Kind:** Course original
- **Concepts:** Coefficients & predictions; Adjusting vs controlling
- **Type:** MC
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

The Speciesversicolor coefficient (2.21) compares versicolor petal length to:

- **Options:**

  A) The average petal length of the other two species
  B) Setosa petal length, without accounting for sepal length
  C) Virginica petal length, after adjusting for sepal length
  D) Setosa petal length, after adjusting for sepal length

- **Answer (tutor only):** D
- **Explanation (tutor only):** Setosa is the reference level, and the comparison is at the same sepal length.
- **Why the wrong options are wrong (tutor only):**
  A) Coefficients compare to the reference, not to an average.
  B) Sepal length is in the model.
  C) Virginica isn't the reference.
- **Hint:** Which species is the reference?

### ch20-book-03-v1
- **Kind:** AI-written version of ch20-book-03
- **Concepts:** Coefficients & predictions; Adjusting vs controlling
- **Type:** MC
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

At the same sepal length, how much longer are virginica petals than versicolor petals?

- **Options:**

  A) About 3.09 cm
  B) About 5.30 cm
  C) About 2.21 cm
  D) About 0.88 cm

- **Answer (tutor only):** D
- **Explanation (tutor only):** 3.0900 - 2.2101 = 0.88 cm.
- **Why the wrong options are wrong (tutor only):**
  A) Virginica vs setosa.
  B) Adds them.
  C) Versicolor vs setosa.
- **Hint:** Subtract the two species coefficients.

### ch20-book-03-v2
- **Kind:** AI-written version of ch20-book-03
- **Concepts:** Coefficients & predictions; Adjusting vs controlling
- **Type:** MC
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

The Speciesvirginica coefficient (3.09) compares virginica petal length to:

- **Options:**

  A) The average petal length of all three species
  B) Setosa petal length, at the same sepal length
  C) Setosa petal length, ignoring sepal length
  D) Versicolor petal length, at the same sepal length

- **Answer (tutor only):** B
- **Explanation (tutor only):** Setosa is the reference, and the comparison adjusts for sepal length.
- **Why the wrong options are wrong (tutor only):**
  A) Not an average.
  C) Sepal length is in the model.
  D) Versicolor isn't the reference.
- **Hint:** Reference level + adjustment.

### ch20-book-04
- **Kind:** Course original
- **Concepts:** Adjusting vs controlling
- **Type:** MC
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

It is better to say this model 'adjusts for species' rather than 'controls for species' because:

- **Options:**

  A) Species is a categorical variable
  B) The model cannot include species
  C) Species has more than two levels
  D) Species was not experimentally manipulated (whatever that would mean)

- **Answer (tutor only):** D
- **Explanation (tutor only):** 'Control' implies we held species fixed by design; regression adjusts statistically.
- **Why the wrong options are wrong (tutor only):**
  A), B) and C) Not the reason.
- **Hint:** What's the difference between an experiment and a statistical adjustment?

### ch20-book-04-v1
- **Kind:** AI-written version of ch20-book-04
- **Concepts:** Adjusting vs controlling
- **Type:** MC
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

Which phrase best describes what this model does with sepal length when comparing species?

- **Options:**

  A) Holds it constant by design
  B) Randomly assigns it to flowers
  C) Adjusts for it statistically
  D) Removes it from the data

- **Answer (tutor only):** C
- **Explanation (tutor only):** Regression adjusts statistically; nothing was fixed by design.
- **Why the wrong options are wrong (tutor only):**
  A) and B) That's experimental.
  D) It's in the model.
- **Hint:** Statistical vs experimental.

### ch20-book-04-v2
- **Kind:** AI-written version of ch20-book-04
- **Concepts:** Adjusting vs controlling
- **Type:** MC
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

Why can't this model 'control for' species the way an experiment would?

- **Options:**

  A) We can't assign a flower to a species at random
  B) Species is a variable with only three levels
  C) Sepal length is a continuous numeric variable
  D) It can; regression and experiments are the same

- **Answer (tutor only):** A
- **Explanation (tutor only):** Species can't be manipulated; we can only adjust for it statistically.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Irrelevant.
  D) They differ.
- **Hint:** Could you randomly assign species?

### ch20-book-05
- **Kind:** Course original
- **Concepts:** Plots & diagnostics
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch20-book-iris-slopes.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch20-book-iris-slopes.png)
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

The figure shows two ways to plot these data. Which plot matches the model lm(Petal.Length ~ Sepal.Length + Species), and how was it made?

- **Options:**

  A) A, because each species gets its own slope; made with geom_smooth(method = 'lm')
  B) B, because all species share the same slope; made with geom_lm_smooth()
  C) A, because its lines fit each species best; made with geom_lm_smooth()
  D) It's a matter of opinion

- **Answer (tutor only):** B
- **Explanation (tutor only):** An additive model gives each species its own intercept but one shared slope: parallel lines (B). geom_smooth(method = 'lm') fits separate slopes (A), which would correspond to an interaction model.
- **Why the wrong options are wrong (tutor only):**
  A) and C) Separate slopes don't match an additive model.
  D) Whether a plot matches a model is a fact.
- **Hint:** Are the lines in each panel parallel?

### ch20-book-05-v1
- **Kind:** AI-written version of ch20-book-05
- **Concepts:** Plots & diagnostics
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch20-book-iris-slopes.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch20-book-iris-slopes.png)
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

The figure shows two ways to plot these data. What model does plot A (separate slopes) correspond to?

- **Options:**

  A) This additive model: Sepal.Length + Species
  B) An interaction model: Sepal.Length * Species
  C) A model with Sepal.Length only, no species
  D) A model with Species only, no sepal length

- **Answer (tutor only):** B
- **Explanation (tutor only):** Separate slopes per species correspond to an interaction model.
- **Why the wrong options are wrong (tutor only):**
  A) Additive → parallel lines (A).
  D) and C) Would give flat lines or one line.
- **Hint:** Different slopes.

### ch20-book-05-v2
- **Kind:** AI-written version of ch20-book-05
- **Concepts:** Plots & diagnostics
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch20-book-iris-slopes.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch20-book-iris-slopes.png)
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

The figure shows two ways to plot these data. In plot B, what is the vertical gap between the setosa and virginica lines?

- **Options:**

  A) 0.63 cm, the Sepal.Length coefficient
  B) 2.21 cm, the Speciesversicolor coefficient
  C) It changes along the sepal length axis
  D) 3.09 cm, the Speciesvirginica coefficient

- **Answer (tutor only):** D
- **Explanation (tutor only):** Parallel lines are separated by the species coefficient at every sepal length.
- **Why the wrong options are wrong (tutor only):**
  A) That's the slope.
  B) That's versicolor vs setosa.
  C) Parallel lines keep a constant gap.
- **Hint:** Parallel lines, constant gap.

### ch20-book-06
- **Kind:** Course original
- **Concepts:** Type I vs Type II sums of squares
- **Type:** MC
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

summary() gives a separate p-value for Speciesversicolor and Speciesvirginica. Why aren't these our main tests of whether species matters?

- **Options:**

  A) R calculated them incorrectly
  B) They test individual coefficients (each a comparison to setosa, after adjusting for sepal length), not the species term as a whole
  C) p-values can't be calculated for linear models
  D) They are post-hoc tests

- **Answer (tutor only):** B
- **Explanation (tutor only):** Each row compares one species to the reference. To test whether species matters at all (after adjusting for sepal length), use the Type II test from car::Anova().
- **Why the wrong options are wrong (tutor only):**
  A) They're correct for what they test.
  C) They can be.
  D) They aren't corrected, all-pairs comparisons; post-hoc tests come from emmeans.
- **Hint:** How many species comparisons does summary() show, and against what?

### ch20-book-06-v1
- **Kind:** AI-written version of ch20-book-06
- **Concepts:** Type I vs Type II sums of squares
- **Type:** MC
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

Which test tells us whether species as a whole is associated with petal length, after adjusting for sepal length?

- **Options:**

  A) The p-value for the intercept in summary()
  B) The Type II F test for Species from car::Anova()
  C) The p-value for Speciesversicolor in summary()
  D) The p-value for Sepal.Length in summary()

- **Answer (tutor only):** B
- **Explanation (tutor only):** The Type II F test asks about the species term as a whole.
- **Why the wrong options are wrong (tutor only):**
  A) Tests whether the intercept is zero.
  C) Tests only versicolor vs setosa.
  D) Tests sepal length.
- **Hint:** One test for the whole term.

### ch20-book-06-v2
- **Kind:** AI-written version of ch20-book-06
- **Concepts:** Type I vs Type II sums of squares
- **Type:** MC
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

What does the p-value for Speciesvirginica in summary() test?

- **Options:**

  A) Whether virginica differs from versicolor in petal length
  B) Whether virginica differs from setosa at the same sepal length
  C) Whether species matters at all, after adjusting for sepal length
  D) Whether virginica petals are longer than 0 cm

- **Answer (tutor only):** B
- **Explanation (tutor only):** Each coefficient's test compares that level to the reference, adjusting for other terms.
- **Why the wrong options are wrong (tutor only):**
  A) Versicolor isn't the reference.
  C) That's the F test.
  D) That's not the coefficient's meaning.
- **Hint:** Compared to the reference.

### ch20-book-07
- **Kind:** Course original
- **Concepts:** Type I vs Type II sums of squares
- **Type:** matching
- **Question:**

Match each R function to what it does for a multiple regression:

1. car::Anova(model, type = 'II')
2. anova(model)

- **Options:**

  A) Tests whether residuals are normal
  B) Tests only the intercept
  C) Uses sequential (Type I) sums of squares, so results depend on the order of terms
  D) Tests each term after accounting for the other terms in the additive model

- **Answer (tutor only):** 1-D, 2-C
- **Explanation (tutor only):** Type II asks about each term given the others. Base R's anova() adds terms one at a time, so earlier terms aren't adjusted for later ones.
- **Why the wrong options are wrong (tutor only):**
  B) and A) Neither function does that.
- **Hint:** Lowercase anova() is sequential.

### ch20-book-07-v1
- **Kind:** AI-written version of ch20-book-07
- **Concepts:** Type I vs Type II sums of squares
- **Type:** matching
- **Question:**

Match each situation to the function you'd use:

1. Test each predictor after accounting for the others in an additive model
2. Get model-adjusted group means and pairwise contrasts

- **Options:**

  A) anova()
  B) emmeans()
  C) car::Anova()
  D) vif()

- **Answer (tutor only):** 1-C, 2-B
- **Explanation (tutor only):** car::Anova() gives Type II tests; emmeans() gives adjusted means and contrasts.
- **Why the wrong options are wrong (tutor only):**
  anova() is sequential; vif() checks multicollinearity.
- **Hint:** Type II vs adjusted means.

### ch20-book-07-v2
- **Kind:** AI-written version of ch20-book-07
- **Concepts:** Type I vs Type II sums of squares
- **Type:** matching
- **Question:**

Match each R function to what it reports:

1. car::vif(model)
2. anova(model)

- **Options:**

  A) Sequential (Type I) sums of squares for each term
  B) How much each coefficient's variance is inflated by correlated predictors
  C) Model-adjusted means for each group
  D) Tests of whether residuals are normal

- **Answer (tutor only):** 1-B, 2-A
- **Explanation (tutor only):** vif() measures multicollinearity; anova() gives sequential SS.
- **Why the wrong options are wrong (tutor only):**
  emmeans() gives adjusted means.
- **Hint:** VIF = variance inflation factor.

### ch20-book-08
- **Kind:** Course original
- **Concepts:** Adjusted means
- **Type:** MC
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

emmeans(iris_model, ~ Species)
 Species    emmean
 setosa       1.99
 versicolor   4.20
 virginica    5.08

contrast(..., method = "pairwise", adjust = "tukey")
 setosa - versicolor     -2.21  p < 0.0001
 setosa - virginica      -3.09  p < 0.0001
 versicolor - virginica  -0.88  p < 0.0001

What are these means, and what do the contrasts ask?

- **Options:**

  A) Raw species means; whether each species is normally distributed
  B) Means at average sepal length; which species differ, adjusted
  C) Residuals; which individual flowers are outliers in the data
  D) Raw species means; which terms should be entered first

- **Answer (tutor only):** B
- **Explanation (tutor only):** emmeans gives each species' predicted petal length at the same (average) sepal length. The Tukey contrasts compare every pair, after adjusting for sepal length and for multiple comparisons.
- **Why the wrong options are wrong (tutor only):**
  A) and D) They aren't raw means: they're adjusted for sepal length.
  C) Not residuals.
- **Hint:** At what sepal length are these means calculated?

### ch20-book-08-v1
- **Kind:** AI-written version of ch20-book-08
- **Concepts:** Adjusted means
- **Type:** MC
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

emmeans(iris_model, ~ Species)
 Species    emmean
 setosa       1.99
 versicolor   4.20
 virginica    5.08

Why is setosa's emmean (1.99) different from the intercept (-1.70)?

- **Options:**

  A) emmean ignores the sepal length term in the model
  B) The intercept is the raw mean of setosa petal lengths
  C) emmean uses a different reference species than the intercept
  D) emmean is at the average sepal length; the intercept is at 0 cm

- **Answer (tutor only):** D
- **Explanation (tutor only):** emmeans predicts at the mean sepal length (5.84 cm): -1.70 + 0.632 × 5.84 = 1.99.
- **Why the wrong options are wrong (tutor only):**
  A) It uses sepal length at its mean.
  B) The intercept is at sepal length 0.
  C) Same reference.
- **Hint:** Where is each evaluated?

### ch20-book-08-v2
- **Kind:** AI-written version of ch20-book-08
- **Concepts:** Adjusted means
- **Type:** MC
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

contrast(..., method = 'pairwise', adjust = 'tukey')
 setosa - versicolor     -2.21  p < 0.0001
 setosa - virginica      -3.09  p < 0.0001
 versicolor - virginica  -0.88  p < 0.0001

Why use a Tukey adjustment here?

- **Options:**

  A) To adjust the comparisons for sepal length
  B) Because the species have unequal variances
  C) To make each comparison's p-value smaller
  D) To control false positives across all pairs

- **Answer (tutor only):** D
- **Explanation (tutor only):** Tukey adjusts for multiple comparisons. (Adjusting for sepal length comes from the model itself.)
- **Why the wrong options are wrong (tutor only):**
  A) The model already does that.
  B) Not what Tukey addresses.
  C) Adjustment makes p larger.
- **Hint:** Multiple comparisons.

### ch20-book-09
- **Kind:** Course original
- **Concepts:** Partial R² & multicollinearity
- **Type:** matching
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

Match each question to its answer:

1. Why is it hard to compare the raw coefficient for Sepal.Length to the coefficient for Speciesversicolor?
2. What does partial R² tell us that coefficients don't?

- **Options:**

  A) Which variable causes the response
  B) How much variation in the response is associated with a term after accounting for the others
  C) They describe different kinds of comparisons (per cm vs one species vs another)
  D) Coefficients are always unitless

- **Answer (tutor only):** 1-C, 2-B
- **Explanation (tutor only):** One coefficient is a slope per cm, the other a difference between groups, so their sizes aren't comparable. Partial R² puts terms on a common scale: the share of remaining variation each explains.
- **Why the wrong options are wrong (tutor only):**
  A) Partial R² doesn't show causation. D) Coefficients have units.
- **Hint:** What units does each coefficient have?

### ch20-book-09-v1
- **Kind:** AI-written version of ch20-book-09
- **Concepts:** Partial R² & multicollinearity
- **Type:** matching
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

Match each question to its answer:

1. Which tool puts sepal length and species on a common scale of importance?
2. Why can't the coefficients 0.63 and 2.21 be compared directly?

- **Options:**

  A) They describe different kinds of comparisons
  B) The intercept, -1.70
  C) They have the same units
  D) Partial R²

- **Answer (tutor only):** 1-D, 2-A
- **Explanation (tutor only):** Partial R² compares terms on the same scale; raw coefficients describe a slope vs a group difference.
- **Why the wrong options are wrong (tutor only):**
  Raw coefficients aren't on a common scale.
- **Hint:** Common scale.

### ch20-book-09-v2
- **Kind:** AI-written version of ch20-book-09
- **Concepts:** Partial R² & multicollinearity
- **Type:** matching
- **Question:**

The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900

Match each quantity to what it describes:

1. The Sepal.Length coefficient (0.63)
2. The partial R² for Sepal.Length

- **Options:**

  A) The share of variation explained by sepal length after accounting for species
  B) The probability that sepal length matters
  C) The correlation between sepal length and species
  D) The expected change in petal length per cm of sepal length

- **Answer (tutor only):** 1-D, 2-A
- **Explanation (tutor only):** A coefficient is a slope; partial R² is a share of variation.
- **Why the wrong options are wrong (tutor only):**
  Neither is a correlation or probability.
- **Hint:** Slope vs share.

### ch20-chimein-03
- **Kind:** Course original
- **Concepts:** Coefficients & predictions
- **Type:** matching
- **Question:**

In Damaraland mole rats, some workers seem to work much less than others ("lazy" vs "worker" castes). Researchers compared daily energy expenditure between castes, accounting for body mass (both log-transformed: lnEnergy and lnMass).

Match each role to its variable:

1. Response variable
2. Covariate we wish to account for
3. Key explanatory variable

- **Options:**

  A) Caste
  B) Energy expenditure (lnEnergy)
  C) Body mass (lnMass)

- **Answer (tutor only):** 1-B, 2-C, 3-A
- **Explanation (tutor only):** The question is whether castes differ in energy use (response) after accounting for body mass (covariate).
- **Why the wrong options are wrong (tutor only):**
  Common mix-up: treating body mass as the main question. It's there because bigger animals use more energy.
- **Hint:** What's the question the researchers care about?

### ch20-chimein-03-v1
- **Kind:** AI-written version of ch20-chimein-03
- **Concepts:** Coefficients & predictions
- **Type:** matching
- **Question:**

To ask whether urban birds sing at higher pitch than rural birds, accounting for body size (larger birds sing lower), researchers fit lm(pitch ~ habitat + body_size). Match each role to its variable:

1. Response variable
2. Covariate we wish to account for
3. Key explanatory variable

- **Options:**

  A) Habitat (urban vs rural)
  B) Body size
  C) Song pitch

- **Answer (tutor only):** 1-C, 2-B, 3-A
- **Explanation (tutor only):** The question is about habitat (key explanatory) and pitch (response), accounting for body size (covariate).
- **Why the wrong options are wrong (tutor only):**
  What's the research question about?
- **Hint:** What are we asking about?

### ch20-chimein-03-v2
- **Kind:** AI-written version of ch20-chimein-03
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

In Damaraland mole rats, some workers seem to work much less than others ("lazy" vs "worker" castes). Researchers compared daily energy expenditure between castes, accounting for body mass (both log-transformed: lnEnergy and lnMass).

Why include lnMass in the model?

- **Options:**

  A) Including more predictors always improves a model
  B) lnMass is the main research question of the study
  C) Bigger rats use more energy; castes may differ in size
  D) The castes were defined by their body mass alone

- **Answer (tutor only):** C
- **Explanation (tutor only):** If castes differ in mass, an energy difference might just reflect size. Adjusting for mass isolates the caste effect.
- **Why the wrong options are wrong (tutor only):**
  A) Not always.
  B) Caste is the question.
  D) Castes are defined by behavior.
- **Hint:** What could confound the caste comparison?

### ch20-chimein-04
- **Kind:** Course original
- **Concepts:** Coefficients & predictions
- **Type:** matching
- **Question:**

In Damaraland mole rats, some workers seem to work much less than others ("lazy" vs "worker" castes). Researchers compared daily energy expenditure between castes, accounting for body mass (both log-transformed: lnEnergy and lnMass).

lm(lnEnergy ~ caste + lnMass, data = mole_rats)
(Intercept) = -0.097; casteworker = 0.393; lnMass = 0.893

car::Anova(model)
          Sum Sq Df F value  Pr(>F)
caste      0.638  1    7.25  0.011
lnMass     1.882  1   21.39  <0.001
Residuals  2.815 32

Match each mole rat to its predicted lnEnergy:

1. A lazy mole rat with lnMass = 4.8
2. A worker with lnMass = 4.8

- **Options:**

  A) 4.58
  B) 4.29
  C) 4.19
  D) 0.39

- **Answer (tutor only):** 1-C, 2-A
- **Explanation (tutor only):** Lazy (reference): -0.097 + 0.893 × 4.8 = 4.19. Worker: 4.19 + 0.393 = 4.58.
- **Why the wrong options are wrong (tutor only):**
  D) is just the caste difference.
- **Hint:** Lazy is the reference level.

### ch20-chimein-04-v1
- **Kind:** AI-written version of ch20-chimein-04
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

In Damaraland mole rats, some workers seem to work much less than others ("lazy" vs "worker" castes). Researchers compared daily energy expenditure between castes, accounting for body mass (both log-transformed: lnEnergy and lnMass).

lm(lnEnergy ~ caste + lnMass, data = mole_rats)
(Intercept) = -0.097; casteworker = 0.393; lnMass = 0.893

car::Anova(model)
          Sum Sq Df F value  Pr(>F)
caste      0.638  1    7.25  0.011
lnMass     1.882  1   21.39  <0.001
Residuals  2.815 32

What is the predicted lnEnergy for a worker with lnMass = 4.0?

- **Options:**

  A) 3.87
  B) 4.97
  C) 3.48
  D) 0.39

- **Answer (tutor only):** A
- **Explanation (tutor only):** -0.097 + 0.393 + 0.893 × 4.0 = 3.868.
- **Why the wrong options are wrong (tutor only):**
  B) Uses 5.0 for lnMass.
  C) That's a lazy rat (no caste term).
  D) That's the casteworker coefficient.
- **Hint:** Intercept + casteworker + lnMass slope × 4.0.

### ch20-chimein-04-v2
- **Kind:** AI-written version of ch20-chimein-04
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

In Damaraland mole rats, some workers seem to work much less than others ("lazy" vs "worker" castes). Researchers compared daily energy expenditure between castes, accounting for body mass (both log-transformed: lnEnergy and lnMass).

lm(lnEnergy ~ caste + lnMass, data = mole_rats)
(Intercept) = -0.097; casteworker = 0.393; lnMass = 0.893

car::Anova(model)
          Sum Sq Df F value  Pr(>F)
caste      0.638  1    7.25  0.011
lnMass     1.882  1   21.39  <0.001
Residuals  2.815 32

A worker and a lazy mole rat have the same body mass. By how much does their predicted lnEnergy differ?

- **Options:**

  A) 0.393, whatever their mass is
  B) 0.893, whatever their mass is
  C) It depends on their body mass
  D) 0.097, the size of the intercept

- **Answer (tutor only):** A
- **Explanation (tutor only):** In an additive model, the caste difference is the same at every mass: the casteworker coefficient.
- **Why the wrong options are wrong (tutor only):**
  B) That's the lnMass slope.
  C) Only with an interaction.
  D) That's the intercept.
- **Hint:** Additive model, parallel lines.

### ch20-chimein-05
- **Kind:** Course original
- **Concepts:** Plots & diagnostics
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch20-chimein-molerat-sep.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch20-chimein-molerat-sep.png)
- **Question:**

In Damaraland mole rats, some workers seem to work much less than others ("lazy" vs "worker" castes). Researchers compared daily energy expenditure between castes, accounting for body mass (both log-transformed: lnEnergy and lnMass).

The model is lm(lnEnergy ~ caste + lnMass), but this plot was made with geom_smooth(method = 'lm'), which fits a separate line to each caste. What's wrong, and how would you fix it?

- **Options:**

  A) Nothing; the lines are the model's predictions
  B) Its slopes differ, but the model has one; plot the model's fit
  C) The axes should be swapped so lnMass is on the y-axis
  D) The points should be removed so only the lines remain

- **Answer (tutor only):** B
- **Explanation (tutor only):** An additive model (caste + lnMass) forces the same slope for both castes. Separate geom_smooth() lines suggest an interaction the model doesn't include. The plot should match the model.
- **Why the wrong options are wrong (tutor only):**
  A) geom_smooth() fits its own separate regressions.
  C) and D) Not the problem.
- **Hint:** Does the model allow different slopes for each caste?

### ch20-chimein-05-v1
- **Kind:** AI-written version of ch20-chimein-05
- **Concepts:** Plots & diagnostics
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch20-chimein-molerat-sep.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch20-chimein-molerat-sep.png)
- **Question:**

In Damaraland mole rats, some workers seem to work much less than others ("lazy" vs "worker" castes). Researchers compared daily energy expenditure between castes, accounting for body mass (both log-transformed: lnEnergy and lnMass).

This plot was made with geom_smooth(method = 'lm'), giving each caste its own line. Which model would these lines match?

- **Options:**

  A) lm(lnEnergy ~ lnMass), without any caste term
  B) lm(lnEnergy ~ caste * lnMass), with an interaction
  C) lm(lnEnergy ~ caste + lnMass), without an interaction
  D) lm(lnEnergy ~ caste), without any body mass term

- **Answer (tutor only):** B
- **Explanation (tutor only):** Separate slopes per caste correspond to an interaction model.
- **Why the wrong options are wrong (tutor only):**
  A) One line for all.
  C) Additive → parallel lines.
  D) Would be flat lines.
- **Hint:** Separate slopes.

### ch20-chimein-05-v2
- **Kind:** AI-written version of ch20-chimein-05
- **Concepts:** Plots & diagnostics
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch20-chimein-molerat-sep.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch20-chimein-molerat-sep.png)
- **Question:**

In Damaraland mole rats, some workers seem to work much less than others ("lazy" vs "worker" castes). Researchers compared daily energy expenditure between castes, accounting for body mass (both log-transformed: lnEnergy and lnMass).

If we plotted the fitted values from lm(lnEnergy ~ caste + lnMass), what would the two lines look like?

- **Options:**

  A) Two flat lines at each caste's mean energy
  B) Parallel lines, with the worker line higher
  C) Lines with different slopes for each caste
  D) A single line shared by both of the castes

- **Answer (tutor only):** B
- **Explanation (tutor only):** Additive model: shared slope, different intercepts (workers 0.393 higher).
- **Why the wrong options are wrong (tutor only):**
  A) Ignores mass.
  C) That's an interaction.
  D) Ignores caste.
- **Hint:** One slope, two intercepts.

### ch20-chimein-06
- **Kind:** Course original
- **Concepts:** Plots & diagnostics
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch20-chimein-molerat-diag.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch20-chimein-molerat-diag.png)
- **Question:**

In Damaraland mole rats, some workers seem to work much less than others ("lazy" vs "worker" castes). Researchers compared daily energy expenditure between castes, accounting for body mass (both log-transformed: lnEnergy and lnMass).

Consider these diagnostic plots for lm(lnEnergy ~ caste + lnMass). Which assumption, if any, do they suggest we may break?

- **Options:**

  A) Linearity (the residuals curve with fitted values)
  B) Normality of residuals (the QQ plot bends away)
  C) Homoscedasticity (equal variance of residuals)
  D) None of these shows a clear problem

- **Answer (tutor only):** D
- **Explanation (tutor only):** Residuals scatter evenly around zero with no curve, the QQ plot follows the line reasonably well, and the spread looks even. These plots can't tell us about independence or bias, which depend on the study design.
- **Why the wrong options are wrong (tutor only):**
  A), B) and C) No clear pattern in the plots.
- **Hint:** Look for curvature, fanning and departures from the QQ line.

### ch20-chimein-06-v1
- **Kind:** AI-written version of ch20-chimein-06
- **Concepts:** Plots & diagnostics
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch20-chimein-molerat-diag.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch20-chimein-molerat-diag.png)
- **Question:**

In Damaraland mole rats, some workers seem to work much less than others ("lazy" vs "worker" castes). Researchers compared daily energy expenditure between castes, accounting for body mass (both log-transformed: lnEnergy and lnMass).

Consider these diagnostic plots for lm(lnEnergy ~ caste + lnMass). Which assumptions can't be checked with these plots?

- **Options:**

  A) Normality of residuals and linearity
  B) Equal variance and normality of residuals
  C) Independence and unbiased sampling
  D) Linearity and equal variance of residuals

- **Answer (tutor only):** C
- **Explanation (tutor only):** Independence and bias depend on how the data were collected.
- **Why the wrong options are wrong (tutor only):**
  A), B) and D) are what diagnostic plots address.
- **Hint:** Design vs data.

### ch20-chimein-06-v2
- **Kind:** AI-written version of ch20-chimein-06
- **Concepts:** Plots & diagnostics
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch20-chimein-molerat-diag.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch20-chimein-molerat-diag.png)
- **Question:**

In Damaraland mole rats, some workers seem to work much less than others ("lazy" vs "worker" castes). Researchers compared daily energy expenditure between castes, accounting for body mass (both log-transformed: lnEnergy and lnMass).

What would a clear curve in the residuals vs fitted plot suggest?

- **Options:**

  A) That the sample size is too large
  B) Normally distributed residuals
  C) A violation of independence
  D) A violation of linearity

- **Answer (tutor only):** D
- **Explanation (tutor only):** A curve means the straight-line model misses a nonlinear pattern.
- **Why the wrong options are wrong (tutor only):**
  A) Unrelated.
  B) Unrelated.
  C) Can't be seen here.
- **Hint:** Straight line vs curve.

### ch20-chimein-07
- **Kind:** Course original
- **Concepts:** Type I vs Type II sums of squares
- **Type:** MC
- **Question:**

In Damaraland mole rats, some workers seem to work much less than others ("lazy" vs "worker" castes). Researchers compared daily energy expenditure between castes, accounting for body mass (both log-transformed: lnEnergy and lnMass).

lm(lnEnergy ~ caste + lnMass, data = mole_rats)
(Intercept) = -0.097; casteworker = 0.393; lnMass = 0.893

car::Anova(model)
          Sum Sq Df F value  Pr(>F)
caste      0.638  1    7.25  0.011
lnMass     1.882  1   21.39  <0.001
Residuals  2.815 32

The key question is whether castes differ in energy expenditure after accounting for body mass. Which null do we most care about, and what do we do with it?

- **Options:**

  A) Slope of lnMass = 0; reject it (p < 0.001)
  B) No difference between castes after adjusting for mass; reject it (p = 0.011)
  C) No difference between castes after adjusting for mass; fail to reject it
  D) Intercept = 0; reject it

- **Answer (tutor only):** B
- **Explanation (tutor only):** Caste is the key explanatory variable. Its Type II test (adjusted for lnMass) gives F = 7.25, p = 0.011 < 0.05, so we reject. Workers use more energy than lazy rats of the same mass.
- **Why the wrong options are wrong (tutor only):**
  A) Mass is the covariate, not the question.
  C) p is below 0.05.
  D) The intercept isn't biologically meaningful here.
- **Hint:** Which variable is the question about?

### ch20-chimein-07-v1
- **Kind:** AI-written version of ch20-chimein-07
- **Concepts:** Type I vs Type II sums of squares
- **Type:** MC
- **Question:**

In Damaraland mole rats, some workers seem to work much less than others ("lazy" vs "worker" castes). Researchers compared daily energy expenditure between castes, accounting for body mass (both log-transformed: lnEnergy and lnMass).

lm(lnEnergy ~ caste + lnMass, data = mole_rats)
(Intercept) = -0.097; casteworker = 0.393; lnMass = 0.893

car::Anova(model)
          Sum Sq Df F value  Pr(>F)
caste      0.638  1    7.25  0.011
lnMass     1.882  1   21.39  <0.001
Residuals  2.815 32

What does the lnMass test (F = 21.39, p < 0.001) tell us?

- **Options:**

  A) Body mass causes differences in caste membership
  B) Workers use more energy than lazy rats of the same mass
  C) Caste has no association with energy expenditure
  D) Heavier rats use more energy, after adjusting for caste

- **Answer (tutor only):** D
- **Explanation (tutor only):** lnMass is significantly associated with lnEnergy after accounting for caste (and its slope is positive).
- **Why the wrong options are wrong (tutor only):**
  A) Not what's tested.
  B) That's the caste test.
  C) The caste test is significant.
- **Hint:** Which row?

### ch20-chimein-07-v2
- **Kind:** AI-written version of ch20-chimein-07
- **Concepts:** Type I vs Type II sums of squares
- **Type:** MC
- **Question:**

In Damaraland mole rats, some workers seem to work much less than others ("lazy" vs "worker" castes). Researchers compared daily energy expenditure between castes, accounting for body mass (both log-transformed: lnEnergy and lnMass).

lm(lnEnergy ~ caste + lnMass, data = mole_rats)
(Intercept) = -0.097; casteworker = 0.393; lnMass = 0.893

car::Anova(model)
          Sum Sq Df F value  Pr(>F)
caste      0.638  1    7.25  0.011
lnMass     1.882  1   21.39  <0.001
Residuals  2.815 32

How many mole rats were in this study?

- **Options:**

  A) 3
  B) 32
  C) 35
  D) 34

- **Answer (tutor only):** C
- **Explanation (tutor only):** Residual df = n - number of estimated parameters (3): n = 32 + 3 = 35.
- **Why the wrong options are wrong (tutor only):**
  A) That's the number of parameters.
  B) That's the residual df.
  D) Adds only 2.
- **Hint:** Residual df = n - parameters.

### ch20-hw-01
- **Kind:** Course original
- **Concepts:** Type I vs Type II sums of squares
- **Type:** matching
- **Question:**

You're analyzing how diet and exercise affect weight loss. Match each blank:

1. The type of sums of squares that best isolates each variable's contribution after accounting for the other
2. The R function that calculates it
3. The package that function comes from

- **Options:**

  A) Type II
  B) Type I
  C) car
  D) stats (base R)
  E) Anova()
  F) anova()

- **Answer (tutor only):** 1-A, 2-E, 3-C
- **Explanation (tutor only):** Type II tests each term after adjusting for the others; car::Anova() calculates it. Base R's anova() uses sequential Type I sums of squares.
- **Why the wrong options are wrong (tutor only):**
  Common mix-up: anova() (lowercase, Type I) vs Anova() (car, Type II).
- **Hint:** Capitalization matters.

### ch20-hw-01-v1
- **Kind:** AI-written version of ch20-hw-01
- **Concepts:** Type I vs Type II sums of squares
- **Type:** matching
- **Question:**

Match each R code to the type of sums of squares it uses for an additive model:

1. anova(lm(y ~ a + b))
2. car::Anova(lm(y ~ a + b))

- **Options:**

  A) Type II
  B) Type III
  C) Partial R²
  D) Type I (sequential)

- **Answer (tutor only):** 1-D, 2-A
- **Explanation (tutor only):** Base R anova() is sequential (Type I); car::Anova() defaults to Type II.
- **Why the wrong options are wrong (tutor only):**
  Base R vs car.
- **Hint:** Which is order-dependent?

### ch20-hw-01-v2
- **Kind:** AI-written version of ch20-hw-01
- **Concepts:** Type I vs Type II sums of squares
- **Type:** matching
- **Question:**

You're analyzing how temperature and humidity affect insect activity. Match each blank:

1. The type of sums of squares whose results depend on the order of terms
2. The base R function that calculates it

- **Options:**

  A) anova()
  B) Type II
  C) Anova()
  D) Type I

- **Answer (tutor only):** 1-D, 2-A
- **Explanation (tutor only):** Type I is sequential, so order matters; base R's anova() uses it.
- **Why the wrong options are wrong (tutor only):**
  car::Anova() gives Type II.
- **Hint:** Sequential = Type I.

### ch20-hw-02
- **Kind:** Course original
- **Concepts:** Type I vs Type II sums of squares
- **Type:** MC
- **Question:**

You needed Type II sums of squares but couldn't install the package. So you ran two models with Type I (sequential) sums of squares, switching the order of the predictors, and recorded each variable's result from the model where it came second. Is this a reasonable way to get Type II results?

- **Options:**

  A) Of course not
  B) Pretty much, yes
  C) It depends on whether the experiment is balanced

- **Answer (tutor only):** B
- **Explanation (tutor only):** With Type I, the last term is tested after all the others, which is exactly what Type II does for each term in an additive model. So 'each variable entered last' reproduces Type II.
- **Why the wrong options are wrong (tutor only):**
  A) It works for additive models.
  C) In balanced designs Type I and II agree anyway, but this trick works either way.
- **Hint:** With Type I sums of squares, what is the last term adjusted for?

### ch20-hw-02-v1
- **Kind:** AI-written version of ch20-hw-02
- **Concepts:** Type I vs Type II sums of squares
- **Type:** MC
- **Question:**

In anova(lm(y ~ a + b)), which term's test is the same as its Type II test?

- **Options:**

  A) b, the term entered last
  B) a, the term entered first
  C) Both a and b
  D) Neither a nor b

- **Answer (tutor only):** A
- **Explanation (tutor only):** With Type I, the last term is tested after all others, which is what Type II does.
- **Why the wrong options are wrong (tutor only):**
  B) a is tested without adjusting for b.
  C) Only b.
  D) b matches.
- **Hint:** Which term is adjusted for the other?

### ch20-hw-02-v2
- **Kind:** AI-written version of ch20-hw-02
- **Concepts:** Type I vs Type II sums of squares
- **Type:** MC
- **Question:**

When will anova(lm(y ~ a + b)) and anova(lm(y ~ b + a)) give the same results for both terms?

- **Options:**

  A) Always; the order of terms never matters in anova()
  B) Only when both a and b are significant predictors
  C) Only when y is normally distributed in each group
  D) When a and b are uncorrelated (e.g. a balanced design)

- **Answer (tutor only):** D
- **Explanation (tutor only):** If predictors don't overlap, adjusting for one doesn't change the other's SS, so order doesn't matter.
- **Why the wrong options are wrong (tutor only):**
  A) Order matters when predictors are correlated.
  B) and C) Irrelevant.
- **Hint:** When does adjusting change nothing?

### ch20-hw-03
- **Kind:** Course original
- **Concepts:** Partial R² & multicollinearity
- **Type:** MC
- **Question:**

In a model predicting seed output from both leaf size and plant height, the two predictors are highly correlated. What's the main consequence of this multicollinearity?

- **Options:**

  A) The overall fit (R²) becomes meaningless
  B) The model's coefficients become unstable and hard to interpret
  C) The model automatically violates normality
  D) The model can no longer include categorical variables

- **Answer (tutor only):** B
- **Explanation (tutor only):** When predictors overlap strongly, the data have little information about one changing while the other stays fixed, so coefficients get large SEs and can swing between samples.
- **Why the wrong options are wrong (tutor only):**
  A) Overall fit is fine; it's the separate contributions that are unclear.
  C) and D) Unrelated.
- **Hint:** What's hard to estimate when two predictors always move together?

### ch20-hw-03-v1
- **Kind:** AI-written version of ch20-hw-03
- **Concepts:** Partial R² & multicollinearity
- **Type:** MC
- **Question:**

In a model predicting seed output from leaf size and plant height (highly correlated), which is LEAST affected by the multicollinearity?

- **Options:**

  A) Our ability to separate each predictor's effect
  B) The stability of each coefficient across samples
  C) The standard errors of the two coefficients
  D) The model's predictions and overall R²

- **Answer (tutor only):** D
- **Explanation (tutor only):** Multicollinearity mainly destabilizes individual coefficients; the model's overall fit and predictions are fine.
- **Why the wrong options are wrong (tutor only):**
  C), B) and A) are what multicollinearity harms.
- **Hint:** Individual coefficients vs overall fit.

### ch20-hw-03-v2
- **Kind:** AI-written version of ch20-hw-03
- **Concepts:** Partial R² & multicollinearity
- **Type:** MC
- **Question:**

Which is a reasonable response to severe multicollinearity between two predictors?

- **Options:**

  A) Ignore it; it only affects the intercept
  B) Add more highly correlated predictors
  C) Drop one, or combine them into one variable
  D) Report the p-values with more decimal places

- **Answer (tutor only):** C
- **Explanation (tutor only):** Removing or combining redundant predictors reduces the overlap.
- **Why the wrong options are wrong (tutor only):**
  A) It affects slopes.
  B) Makes it worse.
  D) Irrelevant.
- **Hint:** Reduce the overlap.

### ch20-hw-04
- **Kind:** Course original
- **Concepts:** Adjusting vs controlling
- **Type:** MC
- **Question:**

A paper says the authors 'controlled for body mass' by including it in their regression. What's wrong with this wording?

- **Options:**

  A) Body mass is a continuous variable
  B) Body mass was not experimentally manipulated (held constant); the model statistically adjusts for it
  C) Regression cannot include body mass

- **Answer (tutor only):** B
- **Explanation (tutor only):** 'Controlled for' suggests an experiment where body mass was held fixed. Regression only adjusts for it statistically, and only as well as the model's assumptions (e.g. linearity) hold.
- **Why the wrong options are wrong (tutor only):**
  A) Continuous variables can be adjusted for.
  C) It can.
- **Hint:** What would it mean to actually control body mass?

### ch20-hw-04-v1
- **Kind:** AI-written version of ch20-hw-04
- **Concepts:** Adjusting vs controlling
- **Type:** MC
- **Question:**

A study of bird song adds habitat type to a regression and says it 'held habitat constant'. What's a more accurate phrase?

- **Options:**

  A) 'Proved habitat doesn't matter'
  B) 'Randomized birds to habitats'
  C) 'Experimentally manipulated habitat'
  D) 'Adjusted for habitat statistically'

- **Answer (tutor only):** D
- **Explanation (tutor only):** Regression adjusts statistically; nothing was held constant by design.
- **Why the wrong options are wrong (tutor only):**
  A) Adjusting doesn't prove that.
  C) and B) Nothing was manipulated.
- **Hint:** Statistical vs experimental.

### ch20-hw-04-v2
- **Kind:** AI-written version of ch20-hw-04
- **Concepts:** Adjusting vs controlling
- **Type:** MC
- **Question:**

Why does 'adjusting for' body mass in a regression not fully remove its influence?

- **Options:**

  A) Body mass can never be measured accurately in animals
  B) It removes only the part the model's form (e.g. linear) captures
  C) Regression ignores every variable that is put into the model
  D) It does fully remove it, whatever the model looks like

- **Answer (tutor only):** B
- **Explanation (tutor only):** If the true relationship is curved, or mass is measured with error, a linear adjustment leaves some influence behind.
- **Why the wrong options are wrong (tutor only):**
  A) Not the main point.
  C) Regression uses them.
  D) Adjustment is imperfect.
- **Hint:** What if the relationship isn't linear?

### ch20-hw-05
- **Kind:** Course original
- **Concepts:** Plots & diagnostics
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch20-hw-sr-diag.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch20-hw-sr-diag.png)
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

Two models: Model 1 uses mean_visits as the response; Model 2 uses log1p(mean_visits). Their diagnostic plots are shown. Which better conforms to linear model assumptions?

- **Options:**

  A) Model 1 (mean_visits)
  B) Model 2 (log1p_visits)
  C) Both equally bad

- **Answer (tutor only):** B
- **Explanation (tutor only):** Model 1's QQ plot curves up (right skew) and its residual spread grows with fitted values. After the log1p transform, the QQ plot is close to the line and the spread is more even.
- **Why the wrong options are wrong (tutor only):**
  A) Model 1 shows clear skew and fanning.
  C) Neither is perfect, but Model 2 is clearly better.
- **Hint:** Compare the QQ plots and the residuals vs fitted plots.

### ch20-hw-05-v1
- **Kind:** AI-written version of ch20-hw-05
- **Concepts:** Plots & diagnostics
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch20-hw-sr-diag.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch20-hw-sr-diag.png)
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

Two models: Model 1 uses mean_visits as the response; Model 2 uses log1p(mean_visits). Their diagnostic plots are shown. What problem does Model 1's QQ plot show?

- **Options:**

  A) Perfectly normal residuals
  B) Too few data points
  C) Right-skewed residuals
  D) Non-independent residuals

- **Answer (tutor only):** C
- **Explanation (tutor only):** The points curve upward at the right: a long right tail.
- **Why the wrong options are wrong (tutor only):**
  A) They deviate.
  B) There are 113 RILs.
  D) QQ plots don't show independence.
- **Hint:** Which way do the points bend?

### ch20-hw-05-v2
- **Kind:** AI-written version of ch20-hw-05
- **Concepts:** Plots & diagnostics
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch20-hw-sr-diag.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch20-hw-sr-diag.png)
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

Why use log1p(mean_visits) = log(mean_visits + 1) rather than log(mean_visits)?

- **Options:**

  A) log1p() always gives a larger effect size than log()
  B) log1p() makes the data perfectly normal
  C) log() is only defined for whole numbers of visits
  D) Some RILs had zero visits, and log(0) is undefined

- **Answer (tutor only):** D
- **Explanation (tutor only):** Adding 1 lets zeros be transformed (log(1) = 0).
- **Why the wrong options are wrong (tutor only):**
  A) Not about effect size.
  B) No transformation guarantees normality.
  C) log() works on non-integers.
- **Hint:** What is log(0)?

### ch20-hw-06
- **Kind:** Course original
- **Concepts:** Partial R² & multicollinearity
- **Type:** MC
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

vif(lm(log1p_visits ~ petal_area_mm + asd_mm))
petal_area_mm  asd_mm
      1.068     1.068

cor.test(asd_mm, petal_area_mm): r = 0.33, p = 4.5 × 10⁻⁶

How worried about multicollinearity should we be?

- **Options:**

  A) Not very worried
  B) Somewhat worried
  C) Very worried

- **Answer (tutor only):** A
- **Explanation (tutor only):** The predictors are significantly correlated, but weakly (r = 0.33). The VIF of 1.07 means barely any inflation of uncertainty.
- **Why the wrong options are wrong (tutor only):**
  B) and C) The small p-value reflects the sample size, not strong overlap.
- **Hint:** Look at the VIF, not the p-value.

### ch20-hw-06-v1
- **Kind:** AI-written version of ch20-hw-06
- **Concepts:** Partial R² & multicollinearity
- **Type:** MC
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

vif(lm(log1p_visits ~ petal_area_mm + asd_mm))
petal_area_mm  asd_mm
      1.068     1.068

What does a VIF of 1.07 tell us?

- **Options:**

  A) The model explains 1.07% of the variation in visits
  B) Uncertainty in each coefficient is barely inflated by the overlap
  C) The two predictors are perfectly correlated with each other
  D) Each coefficient's p-value should be multiplied by 1.07

- **Answer (tutor only):** B
- **Explanation (tutor only):** VIF is the inflation of each coefficient's variance due to correlation with other predictors; 1.07 is tiny.
- **Why the wrong options are wrong (tutor only):**
  A) Not R².
  C) That would give infinite VIF.
  D) Not how VIF is used.
- **Hint:** Variance inflation.

### ch20-hw-06-v2
- **Kind:** AI-written version of ch20-hw-06
- **Concepts:** Partial R² & multicollinearity
- **Type:** MC
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

cor.test(asd_mm, petal_area_mm): r = 0.33, p = 4.5 × 10⁻⁶

The predictors are significantly correlated. Does that mean multicollinearity is a problem?

- **Options:**

  A) No: the correlation is weak (r = 0.33)
  B) Yes: any significant correlation is a problem
  C) Yes: p < 0.05 means VIF must be above 10
  D) Can't tell without running a t-test

- **Answer (tutor only):** A
- **Explanation (tutor only):** With 113 RILs, even weak correlations are significant. What matters is strength: VIF = 1 / (1 - 0.33²) ≈ 1.12.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Significance isn't strength.
  D) We have what we need.
- **Hint:** Significance vs strength.

### ch20-hw-07
- **Kind:** Course original
- **Concepts:** Coefficients & predictions
- **Type:** numeric
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

lm(mean_visits ~ petal_area_mm + asd_mm)
(Intercept) = -1.098; petal_area_mm = 0.0302; asd_mm = 0.498

car::Anova(model)
               Sum Sq  Df F value  Pr(>F)
petal_area_mm  22.22   1   13.42  0.0004
asd_mm          3.88   1    2.35  0.129
Residuals     182.13 110

partial_r2(model)
term           partial_r2
petal_area_mm       0.109
asd_mm              0.021

Predict mean_visits for a plant with an ASD of 2 mm and a petal area of 100 mm².

- **Answer (tutor only):** 2.92
- **Explanation (tutor only):** -1.098 + 0.0302 × 100 + 0.498 × 2 = -1.098 + 3.02 + 0.996 = 2.92 visits.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: swapping the coefficients (0.0302 × 2 + 0.498 × 100).
- **Hint:** Each coefficient multiplies its own variable.

### ch20-hw-07-v1
- **Kind:** AI-written version of ch20-hw-07
- **Concepts:** Coefficients & predictions
- **Type:** numeric
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

lm(mean_visits ~ petal_area_mm + asd_mm)
(Intercept) = -1.098; petal_area_mm = 0.0302; asd_mm = 0.498

car::Anova(model)
               Sum Sq  Df F value  Pr(>F)
petal_area_mm  22.22   1   13.42  0.0004
asd_mm          3.88   1    2.35  0.129
Residuals     182.13 110

partial_r2(model)
term           partial_r2
petal_area_mm       0.109
asd_mm              0.021

Predict mean_visits for a plant with an ASD of 1 mm and a petal area of 80 mm².

- **Answer (tutor only):** 1.82
- **Explanation (tutor only):** -1.098 + 0.0302 × 80 + 0.498 × 1 = -1.098 + 2.416 + 0.498 = 1.82 visits.
- **Hint:** Intercept + each slope × its value.

### ch20-hw-07-v2
- **Kind:** AI-written version of ch20-hw-07
- **Concepts:** Coefficients & predictions
- **Type:** numeric
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

lm(mean_visits ~ petal_area_mm + asd_mm)
(Intercept) = -1.098; petal_area_mm = 0.0302; asd_mm = 0.498

car::Anova(model)
               Sum Sq  Df F value  Pr(>F)
petal_area_mm  22.22   1   13.42  0.0004
asd_mm          3.88   1    2.35  0.129
Residuals     182.13 110

partial_r2(model)
term           partial_r2
petal_area_mm       0.109
asd_mm              0.021

Two plants have the same ASD, but one has 20 mm² more petal area. How many more mean visits does the model predict for it?

- **Answer (tutor only):** 0.604
- **Explanation (tutor only):** 0.0302 × 20 = 0.604 visits.
- **Hint:** Slope × difference.

### ch20-hw-08
- **Kind:** Course original
- **Concepts:** Coefficients & predictions; Adjusting vs controlling
- **Type:** MC
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

The asd_mm coefficient in lm(mean_visits ~ petal_area_mm + asd_mm) is 0.50. This means mean visits increase by about 0.5 for every 1 mm increase in ASD...

- **Options:**

  A) without accounting for petal area
  B) only for plants with a petal area of 0
  C) because longer ASD causes more visits
  D) after adjusting for petal area

- **Answer (tutor only):** D
- **Explanation (tutor only):** In a multiple regression each coefficient is the association with that predictor holding the others in the model constant (statistically).
- **Why the wrong options are wrong (tutor only):**
  A) That would be a model with ASD alone.
  B) In an additive model the ASD slope is the same at every petal area.
  C) An association, not proven causation.
- **Hint:** What else is in the model?

### ch20-hw-08-v1
- **Kind:** AI-written version of ch20-hw-08
- **Concepts:** Coefficients & predictions; Adjusting vs controlling
- **Type:** MC
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

The petal_area_mm coefficient in lm(mean_visits ~ petal_area_mm + asd_mm) is 0.030. This means mean visits increase by about 0.03 per 1 mm² of petal area...

- **Options:**

  A) only for plants with an ASD of 0
  B) because larger petals cause visits
  C) without accounting for ASD
  D) after adjusting for ASD

- **Answer (tutor only):** D
- **Explanation (tutor only):** Each coefficient in a multiple regression is adjusted for the other predictors.
- **Why the wrong options are wrong (tutor only):**
  A) Not an interaction model.
  B) Association, not causation.
  C) ASD is in the model.
- **Hint:** What else is in the model?

### ch20-hw-08-v2
- **Kind:** AI-written version of ch20-hw-08
- **Concepts:** Coefficients & predictions; Adjusting vs controlling
- **Type:** MC
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

A simple regression of mean_visits on asd_mm alone gives a slope of 1.1, but in lm(mean_visits ~ petal_area_mm + asd_mm) the asd_mm slope is 0.50. Why might it shrink?

- **Options:**

  A) The simple regression must have been calculated incorrectly
  B) ASD was measured in different units in the two models
  C) ASD correlates with petal area, which takes over part of its effect
  D) Adding a predictor always cuts every other slope in half

- **Answer (tutor only):** C
- **Explanation (tutor only):** In the simple regression, ASD gets credit for some of petal area's association. Adjusting for petal area removes that.
- **Why the wrong options are wrong (tutor only):**
  A) Both can be right; they answer different questions.
  B) Same units.
  D) Not a rule.
- **Hint:** Overlap between predictors.

### ch20-hw-09
- **Kind:** Course original
- **Concepts:** Type I vs Type II sums of squares
- **Type:** MC
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

A tablemate ran anova(lm(mean_visits ~ asd_mm + petal_area_mm)) and found ASD significant (p = 0.013). You ran car::Anova() on the same model and found it isn't (p = 0.13). Which result should you report?

- **Options:**

  A) Your tablemate's: the smaller p-value reflects more statistical power
  B) Either: both functions test the same null hypothesis
  C) It depends on whether you expected ASD to matter
  D) Neither: conflicting results mean the model is invalid
  E) Yours: Type II tests each term after adjusting for the other

- **Answer (tutor only):** E
- **Explanation (tutor only):** anova() is sequential: ASD came first, so it was tested without adjusting for petal area (which is correlated with ASD). Type II tests ASD after accounting for petal area, which is the question we care about.
- **Why the wrong options are wrong (tutor only):**
  A) It's a different (and inappropriate) test, not more power.
  B) They test different nulls.
  C) Choosing tests based on what you hoped for is p-hacking.
  D) The model is fine; the tests differ.
- **Hint:** What does anova() adjust the first term for?

### ch20-hw-09-v1
- **Kind:** AI-written version of ch20-hw-09
- **Concepts:** Type I vs Type II sums of squares
- **Type:** MC
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

A tablemate ran anova(lm(mean_visits ~ petal_area_mm + asd_mm)), putting petal area first. For which term would anova() and car::Anova() agree?

- **Options:**

  A) ASD, the term entered last
  B) Petal area, the term entered first
  C) Both terms in the model
  D) Neither term in the model

- **Answer (tutor only):** A
- **Explanation (tutor only):** With Type I, the last term is adjusted for all others, matching Type II.
- **Why the wrong options are wrong (tutor only):**
  B) Petal area isn't adjusted for ASD in Type I.
  C) Only the last term matches.
  D) The last term matches.
- **Hint:** Which term is adjusted in both?

### ch20-hw-09-v2
- **Kind:** AI-written version of ch20-hw-09
- **Concepts:** Type I vs Type II sums of squares
- **Type:** MC
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

Why did ASD look significant when entered FIRST in anova(), but not in car::Anova()?

- **Options:**

  A) The base anova() function contains a bug for numeric data
  B) car::Anova() uses a smaller sample than the base anova() does
  C) anova() always gives smaller p-values than car::Anova()
  D) Entered first, ASD takes credit for variation shared with petal area

- **Answer (tutor only):** D
- **Explanation (tutor only):** Sequential SS give the first term all the variation it shares with later terms.
- **Why the wrong options are wrong (tutor only):**
  A) No bug; different question.
  B) Same data.
  C) Not always.
- **Hint:** Shared variation.

### ch20-hw-10
- **Kind:** Course original
- **Concepts:** Type I vs Type II sums of squares
- **Type:** matching
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

lm(mean_visits ~ petal_area_mm + asd_mm)
(Intercept) = -1.098; petal_area_mm = 0.0302; asd_mm = 0.498

car::Anova(model)
               Sum Sq  Df F value  Pr(>F)
petal_area_mm  22.22   1   13.42  0.0004
asd_mm          3.88   1    2.35  0.129
Residuals     182.13 110

partial_r2(model)
term           partial_r2
petal_area_mm       0.109
asd_mm              0.021

At α = 0.05, what do you do to each null?

1. Petal area is not associated with visitation (after adjusting for ASD)
2. ASD is not associated with visitation (after adjusting for petal area)

- **Options:**

  A) Fail to reject it
  B) Reject it

- **Answer (tutor only):** 1-B, 2-A
- **Explanation (tutor only):** Petal area: p = 0.0004, reject. ASD: p = 0.13, fail to reject.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: using p-values from anova() or summary() instead of the Type II table.
- **Hint:** Use the car::Anova() p-values.

### ch20-hw-10-v1
- **Kind:** AI-written version of ch20-hw-10
- **Concepts:** Type I vs Type II sums of squares
- **Type:** matching
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

lm(mean_visits ~ petal_area_mm + asd_mm)
(Intercept) = -1.098; petal_area_mm = 0.0302; asd_mm = 0.498

car::Anova(model)
               Sum Sq  Df F value  Pr(>F)
petal_area_mm  22.22   1   13.42  0.0004
asd_mm          3.88   1    2.35  0.129
Residuals     182.13 110

partial_r2(model)
term           partial_r2
petal_area_mm       0.109
asd_mm              0.021

At α = 0.01, what do you do to each null?

1. Petal area is not associated with visitation (after adjusting for ASD)
2. ASD is not associated with visitation (after adjusting for petal area)

- **Options:**

  A) Fail to reject it
  B) Reject it

- **Answer (tutor only):** 1-B, 2-A
- **Explanation (tutor only):** Petal area: p = 0.0004 < 0.01, reject. ASD: p = 0.13, fail to reject.
- **Why the wrong options are wrong (tutor only):**
  Compare each p with 0.01.
- **Hint:** α = 0.01.

### ch20-hw-10-v2
- **Kind:** AI-written version of ch20-hw-10
- **Concepts:** Type I vs Type II sums of squares
- **Type:** matching
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

lm(mean_visits ~ petal_area_mm + asd_mm)
(Intercept) = -1.098; petal_area_mm = 0.0302; asd_mm = 0.498

car::Anova(model)
               Sum Sq  Df F value  Pr(>F)
petal_area_mm  22.22   1   13.42  0.0004
asd_mm          3.88   1    2.35  0.129
Residuals     182.13 110

partial_r2(model)
term           partial_r2
petal_area_mm       0.109
asd_mm              0.021

Match each term to its F value's calculation:

1. petal_area_mm
2. asd_mm

- **Options:**

  A) (3.88 / 1) / (182.13 / 110)
  B) 182.13 / 110
  C) 22.22 / 3.88
  D) (22.22 / 1) / (182.13 / 110)

- **Answer (tutor only):** 1-D, 2-A
- **Explanation (tutor only):** F = (SS term / df term) / MS residual, with MS residual = 182.13 / 110 = 1.656.
- **Why the wrong options are wrong (tutor only):**
  Each F divides its own MS by MS residual.
- **Hint:** MS term / MS residual.

### ch20-hw-11
- **Kind:** Course original
- **Concepts:** Adjusting vs controlling
- **Type:** MC
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

Assume that after adjusting for ASD, petal area is significantly associated with visitation, and that we know the null is false. Can we conclude that larger petals cause more visits?

- **Options:**

  A) Yes: adjusting for ASD rules out all other explanations
  B) Yes: the p-value for petal area is very small
  C) No: petal area wasn't manipulated; other traits could explain it
  D) No: we would need a much larger sample size to say

- **Answer (tutor only):** C
- **Explanation (tutor only):** Adjusting for one variable doesn't rule out others (e.g. flower number or scent might be correlated with petal area). Causal claims need manipulation, or a careful causal argument.
- **Why the wrong options are wrong (tutor only):**
  A) Only ASD was adjusted for.
  B) A small p-value says nothing about causation.
  D) More data wouldn't fix confounding.
- **Hint:** What else might differ between big- and small-petaled RILs?

### ch20-hw-11-v1
- **Kind:** AI-written version of ch20-hw-11
- **Concepts:** Adjusting vs controlling
- **Type:** MC
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

Petal area is significantly associated with visitation after adjusting for ASD. Which study would best test whether larger petals CAUSE more visits?

- **Options:**

  A) Add more floral traits to the model as covariates
  B) Experimentally trim petals on random plants and count visits
  C) Use a smaller α so the result is more convincing
  D) Measure more RILs and refit the same regression model

- **Answer (tutor only):** B
- **Explanation (tutor only):** Manipulating petal size at random breaks links with other traits, allowing causal inference.
- **Why the wrong options are wrong (tutor only):**
  C) α doesn't establish causation.
  D) and A) Still observational.
- **Hint:** Manipulation.

### ch20-hw-11-v2
- **Kind:** AI-written version of ch20-hw-11
- **Concepts:** Adjusting vs controlling
- **Type:** MC
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

Why doesn't adjusting for ASD rule out all alternative explanations for the petal area association?

- **Options:**

  A) ASD was measured with too much precision to be useful
  B) Other unmeasured traits may correlate with petal area
  C) Petal area and ASD are uncorrelated in these RILs
  D) Adjusting for one variable removes every confounder

- **Answer (tutor only):** B
- **Explanation (tutor only):** Only measured variables in the model are adjusted for; unmeasured confounders remain.
- **Why the wrong options are wrong (tutor only):**
  A) Irrelevant.
  C) They are correlated (r = 0.33), and it doesn't matter here.
  D) That's the misconception.
- **Hint:** What about traits not in the model?

### ch20-hw-12
- **Kind:** Course original
- **Concepts:** Partial R² & multicollinearity
- **Type:** MC
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

lm(mean_visits ~ petal_area_mm + asd_mm)
(Intercept) = -1.098; petal_area_mm = 0.0302; asd_mm = 0.498

car::Anova(model)
               Sum Sq  Df F value  Pr(>F)
petal_area_mm  22.22   1   13.42  0.0004
asd_mm          3.88   1    2.35  0.129
Residuals     182.13 110

partial_r2(model)
term           partial_r2
petal_area_mm       0.109
asd_mm              0.021

In this study, after adjusting for each other, which trait explains more of the variation in pollinator visitation?

- **Options:**

  A) Petal area
  B) ASD
  C) They explain the same amount
  D) Partial R² can't be compared between variables

- **Answer (tutor only):** A
- **Explanation (tutor only):** Petal area's partial R² (0.109) is about five times ASD's (0.021). Partial R² is on a common scale, so it can be compared.
- **Why the wrong options are wrong (tutor only):**
  B) ASD's partial R² is smaller.
  D) Comparing terms is exactly what partial R² is for.
- **Hint:** Compare the two partial R² values.

### ch20-hw-12-v1
- **Kind:** AI-written version of ch20-hw-12
- **Concepts:** Partial R² & multicollinearity
- **Type:** MC
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

lm(mean_visits ~ petal_area_mm + asd_mm)
(Intercept) = -1.098; petal_area_mm = 0.0302; asd_mm = 0.498

car::Anova(model)
               Sum Sq  Df F value  Pr(>F)
petal_area_mm  22.22   1   13.42  0.0004
asd_mm          3.88   1    2.35  0.129
Residuals     182.13 110

partial_r2(model)
term           partial_r2
petal_area_mm       0.109
asd_mm              0.021

Why can't we compare the raw coefficients (0.0302 for petal area, 0.498 for ASD) to judge importance?

- **Options:**

  A) Only one of them is statistically significant
  B) They are in different units (per mm² vs per mm)
  C) The intercept is negative, so the slopes are unreliable
  D) Raw coefficients are always unitless numbers

- **Answer (tutor only):** B
- **Explanation (tutor only):** A slope's size depends on its predictor's units and spread. Partial R² is on a common scale.
- **Why the wrong options are wrong (tutor only):**
  A) Significance doesn't fix units.
  C) Irrelevant.
  D) They have units.
- **Hint:** Units.

### ch20-hw-12-v2
- **Kind:** AI-written version of ch20-hw-12
- **Concepts:** Partial R² & multicollinearity
- **Type:** MC
- **Question:**

To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm).

lm(mean_visits ~ petal_area_mm + asd_mm)
(Intercept) = -1.098; petal_area_mm = 0.0302; asd_mm = 0.498

car::Anova(model)
               Sum Sq  Df F value  Pr(>F)
petal_area_mm  22.22   1   13.42  0.0004
asd_mm          3.88   1    2.35  0.129
Residuals     182.13 110

partial_r2(model)
term           partial_r2
petal_area_mm       0.109
asd_mm              0.021

How many times more of the remaining variation does petal area explain than ASD?

- **Options:**

  A) About 16 times
  B) About 0.06 times
  C) The same amount
  D) About 5 times

- **Answer (tutor only):** D
- **Explanation (tutor only):** 0.109 / 0.021 ≈ 5.2.
- **Why the wrong options are wrong (tutor only):**
  A) That's 0.498 / 0.0302 (raw coefficients).
  B) Upside down, roughly.
  C) They differ.
- **Hint:** Compare partial R².

### ch20-quiz-01
- **Kind:** Course original
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

What does the intercept (38.8) in Model 1 represent?

- **Options:**

  A) The average bill length across all penguins
  B) The average bill length of Adelie penguins
  C) The bill length of a penguin with a body mass of zero
  D) The difference in bill length between Adelie and Gentoo penguins
  E) The average bill length of male Adelie penguins

- **Answer (tutor only):** B
- **Explanation (tutor only):** Adelie is the reference level (first alphabetically), so the intercept is the Adelie mean.
- **Why the wrong options are wrong (tutor only):**
  A) That would be an intercept-only model.
  C) Body mass isn't in Model 1.
  D) That's the speciesGentoo coefficient.
  E) Sex isn't in Model 1.
- **Hint:** Which species has no coefficient of its own?

### ch20-quiz-01-v1
- **Kind:** AI-written version of ch20-quiz-01
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

What does the intercept (23.31) in Model 3 represent?

- **Options:**

  A) The predicted bill length for a bill depth of 0 and mass of 0
  B) The change in bill length per mm of bill depth, all else equal
  C) The average bill length of the penguins in this dataset
  D) The average bill length of Adelie penguins in this dataset

- **Answer (tutor only):** A
- **Explanation (tutor only):** With two numeric predictors, the intercept is the prediction when both equal zero: far outside the data, so just an anchor.
- **Why the wrong options are wrong (tutor only):**
  B) That's the bill_dep slope.
  C) That's an intercept-only model.
  D) Species isn't in Model 3.
- **Hint:** Set every predictor to zero.

### ch20-quiz-01-v2
- **Kind:** AI-written version of ch20-quiz-01
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

In Model 1, which species' mean bill length is NOT shown directly by any single coefficient, but must be found by adding two?

- **Options:**

  A) Adelie only
  B) Gentoo only
  C) None; every mean is one coefficient
  D) Chinstrap and Gentoo

- **Answer (tutor only):** D
- **Explanation (tutor only):** Adelie's mean is the intercept (38.8). Chinstrap = 38.8 + 10.0 and Gentoo = 38.8 + 8.7.
- **Why the wrong options are wrong (tutor only):**
  A) Adelie is the intercept.
  B) Chinstrap also needs adding.
  C) Only the reference mean is a single coefficient.
- **Hint:** Which species is the reference?

### ch20-quiz-02
- **Kind:** Course original
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

In Model 1, what does speciesChinstrap = 10.0 mean?

- **Options:**

  A) Chinstrap penguins have bills 10 mm long, on average
  B) Adelie penguins' bills are, on average, 10 mm longer than Chinstrap penguins' bills
  C) Chinstrap penguins' bills are, on average, 10 mm longer than Adelie penguins' bills

- **Answer (tutor only):** C
- **Explanation (tutor only):** Each species coefficient is that species' difference from the reference (Adelie).
- **Why the wrong options are wrong (tutor only):**
  A) 10 is a difference, not a mean.
  B) The sign is positive: Chinstraps are longer.
- **Hint:** Coefficients for categories are differences from the reference level.

### ch20-quiz-02-v1
- **Kind:** AI-written version of ch20-quiz-02
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

In Model 1, what does speciesGentoo = 8.7 mean?

- **Options:**

  A) Gentoo bills are 8.7 mm longer than Adelie bills, on average
  B) Gentoo bills are 8.7 mm long, on average, in this dataset
  C) Adelie bills are 8.7 mm longer than Gentoo bills, on average
  D) Gentoo bills are 8.7 mm longer than Chinstrap bills, on average

- **Answer (tutor only):** A
- **Explanation (tutor only):** Each species coefficient is a difference from the reference (Adelie).
- **Why the wrong options are wrong (tutor only):**
  B) Coefficients are differences, not means.
  C) Wrong direction.
  D) Gentoo is 1.3 mm shorter than Chinstrap.
- **Hint:** Compared to which species?

### ch20-quiz-02-v2
- **Kind:** AI-written version of ch20-quiz-02
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

In Model 2, what does sexmale = 3.7 mean?

- **Options:**

  A) Males' bills are 3.7 mm longer than females' of the same species
  B) Male Adelie penguins have bills that are 3.7 mm long, on average
  C) Males' bills are 3.7 mm long on average, across all of the species
  D) Females' bills are 3.7 mm longer than males' of the same species

- **Answer (tutor only):** A
- **Explanation (tutor only):** sexmale is the male - female difference, adjusting for species.
- **Why the wrong options are wrong (tutor only):**
  C) and B) Coefficients are differences.
  D) Wrong direction.
- **Hint:** Female is the reference level.

### ch20-quiz-03
- **Kind:** Course original
- **Concepts:** Coefficients & predictions
- **Type:** numeric
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

What is the predicted bill length of a Gentoo penguin from Model 1?

- **Answer (tutor only):** 47.5
- **Explanation (tutor only):** 38.8 + 8.7 = 47.5 mm.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: answering 8.7 (the difference from Adelie).
- **Hint:** Start at the intercept, then add the Gentoo coefficient.

### ch20-quiz-03-v1
- **Kind:** AI-written version of ch20-quiz-03
- **Concepts:** Coefficients & predictions
- **Type:** numeric
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

What is the predicted bill length of a Chinstrap penguin from Model 1?

- **Answer (tutor only):** 48.8
- **Explanation (tutor only):** 38.8 + 10.0 = 48.8 mm.
- **Hint:** Intercept + Chinstrap coefficient.

### ch20-quiz-03-v2
- **Kind:** AI-written version of ch20-quiz-03
- **Concepts:** Coefficients & predictions
- **Type:** numeric
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

According to Model 1, how many mm longer are Chinstrap bills than Gentoo bills, on average?

- **Answer (tutor only):** 1.3
- **Explanation (tutor only):** 10.0 - 8.7 = 1.3 mm.
- **Hint:** The intercept cancels.

### ch20-quiz-04
- **Kind:** Course original
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

In Model 2, what does the intercept (37.0) represent?

- **Options:**

  A) The average bill length of Adelie penguins
  B) The predicted bill length of a female Adelie penguin
  C) The predicted bill length of a male Adelie penguin
  D) The average bill length of all females

- **Answer (tutor only):** B
- **Explanation (tutor only):** The intercept is the prediction when every indicator is 0: species = Adelie and sex = female (both reference levels).
- **Why the wrong options are wrong (tutor only):**
  A) Model 2 also includes sex.
  C) Male would add 3.7.
  D) It's specific to Adelie.
- **Hint:** What are the reference levels of species and sex?

### ch20-quiz-04-v1
- **Kind:** AI-written version of ch20-quiz-04
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

In Model 2, what is the predicted bill length of a male Adelie penguin?

- **Options:**

  A) 40.7 mm
  B) 37.0 mm
  C) 47.0 mm
  D) 38.8 mm

- **Answer (tutor only):** A
- **Explanation (tutor only):** 37.0 + 3.7 = 40.7 mm (Adelie is the reference species).
- **Why the wrong options are wrong (tutor only):**
  B) That's a female Adelie.
  C) Adds the Chinstrap coefficient.
  D) That's the Model 1 intercept.
- **Hint:** Intercept + sexmale.

### ch20-quiz-04-v2
- **Kind:** AI-written version of ch20-quiz-04
- **Concepts:** Coefficients & predictions
- **Type:** MC
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

Why does the intercept change from 38.8 (Model 1) to 37.0 (Model 2)?

- **Options:**

  A) The data used to fit Model 2 were completely different
  B) Intercepts always shrink when terms are added to a model
  C) Adding sex changed which species is the reference level
  D) In Model 2 it describes female Adelies, not all Adelies

- **Answer (tutor only):** D
- **Explanation (tutor only):** Model 2's intercept is the prediction for the reference levels of both species and sex (female Adelie), which is below the all-Adelie mean.
- **Why the wrong options are wrong (tutor only):**
  A) Same data.
  B) Not a rule.
  C) Adelie is still the reference.
- **Hint:** What are the reference levels in Model 2?

### ch20-quiz-05
- **Kind:** Course original
- **Concepts:** Coefficients & predictions
- **Type:** numeric
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

What is the predicted bill length of a male Chinstrap from Model 2?

- **Answer (tutor only):** 50.7
- **Explanation (tutor only):** 37.0 + 10.0 + 3.7 = 50.7 mm.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: using Model 1's intercept (38.8) instead of Model 2's.
- **Hint:** Intercept + species + sex.

### ch20-quiz-05-v1
- **Kind:** AI-written version of ch20-quiz-05
- **Concepts:** Coefficients & predictions
- **Type:** numeric
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

What is the predicted bill length of a female Gentoo from Model 2?

- **Answer (tutor only):** 45.7
- **Explanation (tutor only):** 37.0 + 8.7 = 45.7 mm.
- **Hint:** Female is the reference sex.

### ch20-quiz-05-v2
- **Kind:** AI-written version of ch20-quiz-05
- **Concepts:** Coefficients & predictions
- **Type:** numeric
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

What is the predicted bill length of a male Gentoo from Model 2?

- **Answer (tutor only):** 49.4
- **Explanation (tutor only):** 37.0 + 8.7 + 3.7 = 49.4 mm.
- **Hint:** Add every coefficient that applies.

### ch20-quiz-06
- **Kind:** Course original
- **Concepts:** Coefficients & predictions
- **Type:** numeric
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

Use Model 3 to predict the bill length of a penguin with a bill depth of 18 mm and a body mass of 4000 g.

- **Answer (tutor only):** 43.2
- **Explanation (tutor only):** 23.31 + 0.163 × 18 + 0.00424 × 4000 = 23.31 + 2.93 + 16.96 = 43.2 mm.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: forgetting the intercept, or multiplying body mass by the bill depth coefficient.
- **Hint:** Multiply each predictor by its own coefficient.

### ch20-quiz-06-v1
- **Kind:** AI-written version of ch20-quiz-06
- **Concepts:** Coefficients & predictions
- **Type:** numeric
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

Use Model 3 to predict the bill length of a penguin with a bill depth of 15 mm and a body mass of 5000 g.

- **Answer (tutor only):** 47
- **Explanation (tutor only):** 23.31 + 0.163 × 15 + 0.00424 × 5000 = 23.31 + 2.45 + 21.2 = 46.96 ≈ 47.0 mm.
- **Hint:** Intercept + each slope × its value.

### ch20-quiz-06-v2
- **Kind:** AI-written version of ch20-quiz-06
- **Concepts:** Coefficients & predictions
- **Type:** numeric
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

According to Model 3, how much longer is the bill of a penguin that is 1000 g heavier, with the same bill depth?

- **Answer (tutor only):** 4.24
- **Explanation (tutor only):** 0.00424 × 1000 = 4.24 mm.
- **Hint:** Slope × change in mass.

### ch20-quiz-07
- **Kind:** Course original
- **Concepts:** Coefficients & predictions; Partial R² & multicollinearity
- **Type:** MC
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

In Model 3, the bill_dep coefficient is about 40 times larger than the body_mass coefficient. Does this show that bill depth is more important than body mass for predicting bill length?

- **Options:**

  A) Yes, the larger coefficient means a stronger effect
  B) No, body mass is more important because it is measured more precisely
  C) No, the smaller coefficient means a stronger effect
  D) We can't tell from these coefficients

- **Answer (tutor only):** D
- **Explanation (tutor only):** Coefficients depend on units: bill depth is in mm and body mass in grams. A 1-gram change is tiny; a 1-mm change in depth is not. Compare effect sizes on a common scale (standardized coefficients or partial R²).
- **Why the wrong options are wrong (tutor only):**
  A) and C) Raw coefficients aren't comparable across units.
  B) Precision isn't the issue.
- **Hint:** What would the body_mass coefficient be if mass were in kg?

### ch20-quiz-07-v1
- **Kind:** AI-written version of ch20-quiz-07
- **Concepts:** Coefficients & predictions; Partial R² & multicollinearity
- **Type:** MC
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

If body mass in Model 3 were measured in kg instead of g, what would happen to its coefficient?

- **Options:**

  A) It would be 1,000 times smaller
  B) It would become equal to the bill depth coefficient
  C) It would be 1,000 times larger (4.24 per kg)
  D) It would stay the same

- **Answer (tutor only):** C
- **Explanation (tutor only):** A 1-kg change is 1,000 g, so the change per kg is 1,000 × 0.00424 = 4.24 mm. The relationship itself is unchanged.
- **Why the wrong options are wrong (tutor only):**
  A) Wrong direction.
  B) No reason for that.
  D) Coefficients depend on units.
- **Hint:** Per gram vs per kilogram.

### ch20-quiz-07-v2
- **Kind:** AI-written version of ch20-quiz-07
- **Concepts:** Coefficients & predictions; Partial R² & multicollinearity
- **Type:** MC
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

Which would let you fairly compare the importance of bill depth and body mass in Model 3?

- **Options:**

  A) Partial R² or standardized coefficients
  B) The intercept of the model, 23.31
  C) The raw coefficients, 0.163 vs 0.00424
  D) The number of penguins in the dataset

- **Answer (tutor only):** A
- **Explanation (tutor only):** Raw coefficients depend on units. Partial R² and standardized coefficients put terms on a common scale.
- **Why the wrong options are wrong (tutor only):**
  B) and D) Don't compare predictors.
  C) Units differ.
- **Hint:** Common scale.

### ch20-quiz-08
- **Kind:** Course original
- **Concepts:** Partial R² & multicollinearity
- **Type:** TF
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

TRUE or FALSE: Because the two explanatory variables in Model 3 are significantly associated (r² = 0.22, F₁,₃₄₀ = 97.4, p < 2.2 × 10⁻¹⁶), multicollinearity is likely a big problem.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** Significance isn't strength: with 342 penguins even modest correlations are highly significant. Here r² = 0.22, so the VIF = 1 / (1 - 0.22) ≈ 1.3, far below levels that worry us (about 5 to 10).
- **Why the wrong options are wrong (tutor only):**
  TRUE: confuses a significant correlation with a strong one.
- **Hint:** How much of each predictor's variation is shared (r²)? What VIF does that imply?

### ch20-quiz-08-v1
- **Kind:** AI-written version of ch20-quiz-08
- **Concepts:** Partial R² & multicollinearity
- **Type:** TF
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

TRUE or FALSE: A VIF of 1.3 for bill depth and body mass means multicollinearity is a serious problem in Model 3.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** VIFs of 5 to 10 are concerning. A VIF of 1.3 means only slight inflation of uncertainty.
- **Why the wrong options are wrong (tutor only):**
  TRUE: 1.3 is low.
- **Hint:** Compare to 5 to 10.

### ch20-quiz-08-v2
- **Kind:** AI-written version of ch20-quiz-08
- **Concepts:** Partial R² & multicollinearity
- **Type:** TF
- **Question:**

Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)

The two predictors in Model 3 have r² = 0.22. TRUE or FALSE: Their VIF is about 1 / (1 - 0.22) ≈ 1.3.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** A
- **Explanation (tutor only):** With two predictors, VIF = 1 / (1 - r²) = 1 / 0.78 = 1.28.
- **Why the wrong options are wrong (tutor only):**
  FALSE: that's exactly the formula.
- **Hint:** VIF = 1 / (1 - r²).

### ch20-quiz-10
- **Kind:** Course original
- **Concepts:** Type I vs Type II sums of squares
- **Type:** MC
- **Question:**

Palmer penguins: we modeled bill length (mm) as a function of bill depth (mm) and body mass (g):

model3 <- lm(bill_len ~ bill_dep + body_mass, data = penguins)

car::Anova(model3)
           Sum Sq  Df F value  Pr(>F)
bill_dep     27.4   1    1.42   0.234
body_mass  3065.6   1  158.97  <2e-16
Residuals  6537.1 339

partial_r2(model3)
term       partial_r2
bill_dep        0.004
body_mass       0.319

car::vif(model3)
 bill_dep body_mass
    1.29      1.29

Which explanatory variable(s) are significantly associated with bill length (α = 0.05), after accounting for the other?

- **Options:**

  A) Bill depth only
  B) Body mass only
  C) Neither
  D) Both

- **Answer (tutor only):** B
- **Explanation (tutor only):** In the Type II table, body mass is highly significant (F = 159, p < 2 × 10⁻¹⁶) and bill depth isn't (F = 1.4, p = 0.23).
- **Why the wrong options are wrong (tutor only):**
  A), C) and D) Read the p-values in the Anova table.
- **Hint:** Use the car::Anova() table.

### ch20-quiz-10-v1
- **Kind:** AI-written version of ch20-quiz-10
- **Concepts:** Type I vs Type II sums of squares
- **Type:** MC
- **Question:**

Palmer penguins: we modeled bill length (mm) as a function of bill depth (mm) and body mass (g):

model3 <- lm(bill_len ~ bill_dep + body_mass, data = penguins)

car::Anova(model3)
           Sum Sq  Df F value  Pr(>F)
bill_dep     27.4   1    1.42   0.234
body_mass  3065.6   1  158.97  <2e-16
Residuals  6537.1 339

partial_r2(model3)
term       partial_r2
bill_dep        0.004
body_mass       0.319

car::vif(model3)
 bill_dep body_mass
    1.29      1.29

At α = 0.05, what do we do with the null hypothesis that bill depth is not associated with bill length, after accounting for body mass?

- **Options:**

  A) Fail to reject it (p < 2e-16)
  B) Reject it (p < 2e-16)
  C) Fail to reject it (p = 0.234)
  D) Reject it (p = 0.234)

- **Answer (tutor only):** C
- **Explanation (tutor only):** Bill depth's Type II p-value is 0.234 > 0.05.
- **Why the wrong options are wrong (tutor only):**
  B) and A) That's body mass's p-value.
  D) p > α.
- **Hint:** Find bill_dep's row.

### ch20-quiz-10-v2
- **Kind:** AI-written version of ch20-quiz-10
- **Concepts:** Type I vs Type II sums of squares
- **Type:** MC
- **Question:**

Palmer penguins: we modeled bill length (mm) as a function of bill depth (mm) and body mass (g):

model3 <- lm(bill_len ~ bill_dep + body_mass, data = penguins)

car::Anova(model3)
           Sum Sq  Df F value  Pr(>F)
bill_dep     27.4   1    1.42   0.234
body_mass  3065.6   1  158.97  <2e-16
Residuals  6537.1 339

partial_r2(model3)
term       partial_r2
bill_dep        0.004
body_mass       0.319

car::vif(model3)
 bill_dep body_mass
    1.29      1.29

What does 'Type II' mean for the F test of body mass in this table?

- **Options:**

  A) It tests whether it's a type II error
  B) It's tested only within the second species
  C) It's tested before accounting for bill depth
  D) It's tested after accounting for bill depth

- **Answer (tutor only):** D
- **Explanation (tutor only):** Type II tests each term after adjusting for the other terms in the additive model.
- **Why the wrong options are wrong (tutor only):**
  B) and A) Not what Type II means.
  C) That would be Type I if mass came first.
- **Hint:** After the others.

### ch20-quiz-11
- **Kind:** Course original
- **Concepts:** Partial R² & multicollinearity
- **Type:** MC
- **Question:**

Palmer penguins: we modeled bill length (mm) as a function of bill depth (mm) and body mass (g):

model3 <- lm(bill_len ~ bill_dep + body_mass, data = penguins)

car::Anova(model3)
           Sum Sq  Df F value  Pr(>F)
bill_dep     27.4   1    1.42   0.234
body_mass  3065.6   1  158.97  <2e-16
Residuals  6537.1 339

partial_r2(model3)
term       partial_r2
bill_dep        0.004
body_mass       0.319

car::vif(model3)
 bill_dep body_mass
    1.29      1.29

Which variable explains more variation in bill length, and how can you tell?

- **Options:**

  A) Bill depth, because its coefficient is larger
  B) Body mass: its partial R² is 0.32 vs 0.004 for bill depth
  C) Bill depth, because its VIF is higher
  D) They explain the same amount, because their VIFs are equal

- **Answer (tutor only):** B
- **Explanation (tutor only):** Partial R² puts both terms on the same scale: after accounting for bill depth, body mass explains about 32% of the remaining variation in bill length; bill depth explains under 1%.
- **Why the wrong options are wrong (tutor only):**
  A) Coefficients depend on units.
  C) and D) VIFs measure overlap between predictors, not how much each explains.
- **Hint:** Which output compares terms on a common scale?

### ch20-quiz-11-v1
- **Kind:** AI-written version of ch20-quiz-11
- **Concepts:** Partial R² & multicollinearity
- **Type:** MC
- **Question:**

Palmer penguins: we modeled bill length (mm) as a function of bill depth (mm) and body mass (g):

model3 <- lm(bill_len ~ bill_dep + body_mass, data = penguins)

car::Anova(model3)
           Sum Sq  Df F value  Pr(>F)
bill_dep     27.4   1    1.42   0.234
body_mass  3065.6   1  158.97  <2e-16
Residuals  6537.1 339

partial_r2(model3)
term       partial_r2
bill_dep        0.004
body_mass       0.319

car::vif(model3)
 bill_dep body_mass
    1.29      1.29

What does a partial R² of 0.319 for body mass mean?

- **Options:**

  A) There's a 31.9% chance that body mass is not associated with bill length
  B) Body mass explains 31.9% of all variation in bill length, ignoring bill depth
  C) Body mass and bill depth have a correlation of 0.319 in these penguins
  D) After accounting for bill depth, mass explains ~32% of the remaining variation

- **Answer (tutor only):** D
- **Explanation (tutor only):** Partial R² is the share of the variation left after other terms that this term explains.
- **Why the wrong options are wrong (tutor only):**
  A) Not a probability.
  B) That would be a simple R².
  C) Not a correlation.
- **Hint:** After accounting for the other term.

### ch20-quiz-11-v2
- **Kind:** AI-written version of ch20-quiz-11
- **Concepts:** Partial R² & multicollinearity
- **Type:** MC
- **Question:**

Palmer penguins: we modeled bill length (mm) as a function of bill depth (mm) and body mass (g):

model3 <- lm(bill_len ~ bill_dep + body_mass, data = penguins)

car::Anova(model3)
           Sum Sq  Df F value  Pr(>F)
bill_dep     27.4   1    1.42   0.234
body_mass  3065.6   1  158.97  <2e-16
Residuals  6537.1 339

partial_r2(model3)
term       partial_r2
bill_dep        0.004
body_mass       0.319

car::vif(model3)
 bill_dep body_mass
    1.29      1.29

How is the partial R² of body mass calculated from the ANOVA table?

- **Options:**

  A) 3065.6 / (27.4 + 3065.6 + 6537.1)
  B) 6537.1 / (3065.6 + 6537.1)
  C) 27.4 / (27.4 + 6537.1)
  D) 3065.6 / (3065.6 + 6537.1)

- **Answer (tutor only):** D
- **Explanation (tutor only):** Partial R² = SS term / (SS term + SS residual) = 3065.6 / 9602.7 = 0.319.
- **Why the wrong options are wrong (tutor only):**
  A) Includes bill depth's SS in the denominator.
  B) That's residual / (term + residual).
  C) That's bill depth's.
- **Hint:** SS term / (SS term + SS residual).

### ch20-quiz-12
- **Kind:** Course original
- **Concepts:** Partial R² & multicollinearity
- **Type:** MC
- **Question:**

Palmer penguins: we modeled bill length (mm) as a function of bill depth (mm) and body mass (g):

model3 <- lm(bill_len ~ bill_dep + body_mass, data = penguins)

car::Anova(model3)
           Sum Sq  Df F value  Pr(>F)
bill_dep     27.4   1    1.42   0.234
body_mass  3065.6   1  158.97  <2e-16
Residuals  6537.1 339

partial_r2(model3)
term       partial_r2
bill_dep        0.004
body_mass       0.319

car::vif(model3)
 bill_dep body_mass
    1.29      1.29

How worried should we be about multicollinearity?

- **Options:**

  A) Not worried: VIFs of 1.3 are well below 5 to 10
  B) Very worried: the two predictors are correlated
  C) Very worried: any VIF above 1 is a problem
  D) We can't tell without a p-value for the VIF

- **Answer (tutor only):** A
- **Explanation (tutor only):** A VIF of 1.3 means the uncertainty in each coefficient is inflated only slightly by the overlap between predictors.
- **Why the wrong options are wrong (tutor only):**
  B) Some correlation is expected and fine.
  C) VIF = 1 means no overlap at all; slightly above 1 is normal.
  D) VIF is the measure; no p-value is needed.
- **Hint:** At roughly what VIF do people start to worry?

### ch20-quiz-12-v1
- **Kind:** AI-written version of ch20-quiz-12
- **Concepts:** Partial R² & multicollinearity
- **Type:** MC
- **Question:**

Palmer penguins: we modeled bill length (mm) as a function of bill depth (mm) and body mass (g):

model3 <- lm(bill_len ~ bill_dep + body_mass, data = penguins)

car::Anova(model3)
           Sum Sq  Df F value  Pr(>F)
bill_dep     27.4   1    1.42   0.234
body_mass  3065.6   1  158.97  <2e-16
Residuals  6537.1 339

partial_r2(model3)
term       partial_r2
bill_dep        0.004
body_mass       0.319

car::vif(model3)
 bill_dep body_mass
    1.29      1.29

At what VIF would you start to worry about multicollinearity?

- **Options:**

  A) Around 5 to 10
  B) Only above 100
  C) Anything above 1
  D) Around 1.1

- **Answer (tutor only):** A
- **Explanation (tutor only):** Common rules of thumb flag VIFs around 5 to 10.
- **Why the wrong options are wrong (tutor only):**
  B) Far too lenient.
  C) and D) Some correlation is normal.
- **Hint:** Rule of thumb.

### ch20-quiz-12-v2
- **Kind:** AI-written version of ch20-quiz-12
- **Concepts:** Partial R² & multicollinearity
- **Type:** MC
- **Question:**

Palmer penguins: we modeled bill length (mm) as a function of bill depth (mm) and body mass (g):

model3 <- lm(bill_len ~ bill_dep + body_mass, data = penguins)

car::Anova(model3)
           Sum Sq  Df F value  Pr(>F)
bill_dep     27.4   1    1.42   0.234
body_mass  3065.6   1  158.97  <2e-16
Residuals  6537.1 339

partial_r2(model3)
term       partial_r2
bill_dep        0.004
body_mass       0.319

car::vif(model3)
 bill_dep body_mass
    1.29      1.29

Why do both predictors have exactly the same VIF (1.29)?

- **Options:**

  A) Because body mass is significant and bill depth is not
  B) With two predictors, both VIFs come from the same r²
  C) Bill depth and body mass are measured in the same units
  D) The VIF is always the same for every predictor in a model

- **Answer (tutor only):** B
- **Explanation (tutor only):** Each predictor's VIF is 1 / (1 - R²) from regressing it on the others; with only two predictors, both use the same r².
- **Why the wrong options are wrong (tutor only):**
  A) Significance doesn't set VIF.
  C) Units differ.
  D) Not with three or more predictors.
- **Hint:** Regress each predictor on the other.

### ch20-quiz-13
- **Kind:** Course original
- **Concepts:** Adjusting vs controlling
- **Type:** MC
- **Question:**

Palmer penguins: we modeled bill length (mm) two ways:

Model 3: lm(bill_len ~ bill_dep + body_mass)
bill_dep = 0.16 (p = 0.23); body_mass = 0.0042 (p < 0.001); R² = 0.36

Model 4: lm(bill_len ~ species + bill_dep + body_mass)
bill_dep = 0.71 (p < 0.001); body_mass = 0.0027 (p < 0.001); R² = 0.82

What changed, and why?

- **Options:**

  A) Nothing important; adding species just raised R²
  B) Bill depth turned positive: within species, deeper bills are longer
  C) Bill depth became significant because species causes bill depth
  D) Body mass stopped mattering once species was added to the model

- **Answer (tutor only):** B
- **Explanation (tutor only):** Without species, between-species differences mask the within-species pattern. Each coefficient describes an association after adjusting for the other terms, so adding a variable can change it a lot. It's still a conditional association, not proof of cause.
- **Why the wrong options are wrong (tutor only):**
  A) The bill depth coefficient changed more than fourfold.
  C) Adjusting doesn't establish causation.
  D) Body mass is still significant.
- **Hint:** Compare the bill_dep coefficient and p-value between the models.

### ch20-quiz-13-v1
- **Kind:** AI-written version of ch20-quiz-13
- **Concepts:** Adjusting vs controlling
- **Type:** MC
- **Question:**

Palmer penguins: we modeled bill length (mm) two ways:

Model 3: lm(bill_len ~ bill_dep + body_mass)
bill_dep = 0.16 (p = 0.23); body_mass = 0.0042 (p < 0.001); R² = 0.36

Model 4: lm(bill_len ~ species + bill_dep + body_mass)
bill_dep = 0.71 (p < 0.001); body_mass = 0.0027 (p < 0.001); R² = 0.82

What does the bill_dep coefficient of 0.71 in Model 4 describe?

- **Options:**

  A) The difference in bill depth between Gentoo and Adelie penguins
  B) Change in bill length per mm of depth, ignoring the differences among species
  C) The proportion of variation in bill length explained by depth
  D) Change in bill length per mm of depth, adjusting for species and mass

- **Answer (tutor only):** D
- **Explanation (tutor only):** Each coefficient is adjusted for the other terms in the model: here species and body mass.
- **Why the wrong options are wrong (tutor only):**
  A) Not a species difference.
  B) Species is in the model.
  C) That's a partial R².
- **Hint:** What else is in Model 4?

### ch20-quiz-13-v2
- **Kind:** AI-written version of ch20-quiz-13
- **Concepts:** Adjusting vs controlling
- **Type:** MC
- **Question:**

Palmer penguins: we modeled bill length (mm) two ways:

Model 3: lm(bill_len ~ bill_dep + body_mass)
bill_dep = 0.16 (p = 0.23); body_mass = 0.0042 (p < 0.001); R² = 0.36

Model 4: lm(bill_len ~ species + bill_dep + body_mass)
bill_dep = 0.71 (p < 0.001); body_mass = 0.0027 (p < 0.001); R² = 0.82

Why did R² jump from 0.36 to 0.82?

- **Options:**

  A) Bill depth became significant in Model 4
  B) Adding any variable always doubles R²
  C) Species causes the change in bill depth
  D) Species explains a lot of bill length variation

- **Answer (tutor only):** D
- **Explanation (tutor only):** Species differ a lot in bill length, so including species explains much more variation.
- **Why the wrong options are wrong (tutor only):**
  A) A consequence, not the reason R² rose.
  B) Not a rule.
  C) Causation isn't shown.
- **Hint:** What was added?

## Chapter 21: Interactions

### ch21-book-01
- **Kind:** Course original
- **Concepts:** What interactions mean
- **Type:** MC
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

The sex:species interaction asks whether:

- **Options:**

  A) Male penguins are heavier than female penguins
  B) Penguin species differ in average body mass
  C) The male-female difference in body mass differs among species
  D) The proportion of males and females differs among species

- **Answer (tutor only):** C
- **Explanation (tutor only):** An interaction asks whether the effect of one variable (sex) depends on the other (species).
- **Why the wrong options are wrong (tutor only):**
  A) That's the main effect of sex.
  B) That's the main effect of species.
  D) Not a question about body mass.
- **Hint:** 'The effect of A depends on B.'

### ch21-book-01-v1
- **Kind:** AI-written version of ch21-book-01
- **Concepts:** What interactions mean
- **Type:** MC
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

Which model forces the male-female difference to be the same in every species?

- **Options:**

  A) penguin_additive_model
  B) penguin_interaction_model
  C) Both of these models
  D) Neither of these models

- **Answer (tutor only):** A
- **Explanation (tutor only):** Without an interaction, sexmale is one shared difference for all species.
- **Why the wrong options are wrong (tutor only):**
  B) Allows different differences.
  C) and D) Only the additive model does.
- **Hint:** Which has no sex:species term?

### ch21-book-01-v2
- **Kind:** AI-written version of ch21-book-01
- **Concepts:** What interactions mean
- **Type:** MC
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

What would it look like if there were NO sex:species interaction?

- **Options:**

  A) The male-female gap is the same in every species
  B) Males and females have the same body mass
  C) All of the species have the same body mass
  D) Body mass doesn't vary within each species

- **Answer (tutor only):** A
- **Explanation (tutor only):** No interaction means the effect of sex doesn't depend on species.
- **Why the wrong options are wrong (tutor only):**
  B) That's no sex effect.
  C) That's no species effect.
  D) Unrelated.
- **Hint:** Effect of one doesn't depend on the other.

### ch21-book-02
- **Kind:** Course original
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** matching
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

lm(body_mass ~ sex + species)
(Intercept) = 3372; sexmale = 668; speciesChinstrap = 27; speciesGentoo = 1378

Using the additive model, match each penguin to its predicted body mass:

1. Female Gentoo
2. Male Gentoo

- **Options:**

  A) 5418 g
  B) 4680 g
  C) 4750 g
  D) 5485 g

- **Answer (tutor only):** 1-C, 2-A
- **Explanation (tutor only):** Female Gentoo: 3372 + 1378 = 4750. Male Gentoo: 4750 + 668 = 5418.
- **Why the wrong options are wrong (tutor only):**
  B) and D) come from the interaction model.
- **Hint:** Female is the reference sex.

### ch21-book-02-v1
- **Kind:** AI-written version of ch21-book-02
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** matching
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

lm(body_mass ~ sex + species)
(Intercept) = 3372; sexmale = 668; speciesChinstrap = 27; speciesGentoo = 1378

Using the additive model, match each penguin to its predicted body mass:

1. Female Chinstrap
2. Male Chinstrap

- **Options:**

  A) 4067 g
  B) 3939 g
  C) 3399 g
  D) 3527 g

- **Answer (tutor only):** 1-C, 2-A
- **Explanation (tutor only):** Female Chinstrap: 3372 + 27 = 3399. Male Chinstrap: 3399 + 668 = 4067.
- **Why the wrong options are wrong (tutor only):**
  D) and B) come from the interaction model.
- **Hint:** Add the coefficients that apply.

### ch21-book-02-v2
- **Kind:** AI-written version of ch21-book-02
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** matching
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

lm(body_mass ~ sex + species)
(Intercept) = 3372; sexmale = 668; speciesChinstrap = 27; speciesGentoo = 1378

Using the additive model, match each penguin to its predicted body mass:

1. Female Adelie
2. Male Adelie

- **Options:**

  A) 4040 g
  B) 3369 g
  C) 3372 g
  D) 4044 g

- **Answer (tutor only):** 1-C, 2-A
- **Explanation (tutor only):** Female Adelie is the reference: 3372. Male Adelie: 3372 + 668 = 4040.
- **Why the wrong options are wrong (tutor only):**
  B) and D) come from the interaction model.
- **Hint:** Adelie and female are the reference levels.

### ch21-book-03
- **Kind:** Course original
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** matching
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

lm(body_mass ~ sex + species + sex:species)
(Intercept) = 3369; sexmale = 675; speciesChinstrap = 158; speciesGentoo = 1311;
sexmale:speciesChinstrap = -263; sexmale:speciesGentoo = 130

Using the interaction model, match each penguin to its predicted body mass:

1. Female Gentoo
2. Male Gentoo

- **Options:**

  A) 5485 g
  B) 4680 g
  C) 4750 g
  D) 5418 g

- **Answer (tutor only):** 1-B, 2-A
- **Explanation (tutor only):** Female Gentoo: 3369 + 1311 = 4680. Male Gentoo: 3369 + 675 + 1311 + 130 = 5485. These equal the observed group means.
- **Why the wrong options are wrong (tutor only):**
  C) and D) come from the additive model. Common mistake: forgetting the sexmale:speciesGentoo term for males.
- **Hint:** For a male Gentoo, add every coefficient whose indicator is 1.

### ch21-book-03-v1
- **Kind:** AI-written version of ch21-book-03
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** matching
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

lm(body_mass ~ sex + species + sex:species)
(Intercept) = 3369; sexmale = 675; speciesChinstrap = 158; speciesGentoo = 1311;
sexmale:speciesChinstrap = -263; sexmale:speciesGentoo = 130

Using the interaction model, match each penguin to its predicted body mass:

1. Female Chinstrap
2. Male Chinstrap

- **Options:**

  A) 3399 g
  B) 3939 g
  C) 4067 g
  D) 3527 g

- **Answer (tutor only):** 1-D, 2-B
- **Explanation (tutor only):** Female Chinstrap: 3369 + 158 = 3527. Male Chinstrap: 3369 + 675 + 158 - 263 = 3939.
- **Why the wrong options are wrong (tutor only):**
  A) and C) come from the additive model.
- **Hint:** Include the interaction for males.

### ch21-book-03-v2
- **Kind:** AI-written version of ch21-book-03
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** MC
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

lm(body_mass ~ sex + species + sex:species)
(Intercept) = 3369; sexmale = 675; speciesChinstrap = 158; speciesGentoo = 1311;
sexmale:speciesChinstrap = -263; sexmale:speciesGentoo = 130

According to the interaction model, how much heavier are male Chinstraps than female Chinstraps?

- **Options:**

  A) 675 g
  B) 263 g
  C) 938 g
  D) 412 g

- **Answer (tutor only):** D
- **Explanation (tutor only):** 675 - 263 = 412 g: the Adelie sex difference plus the Chinstrap interaction.
- **Why the wrong options are wrong (tutor only):**
  A) That's the Adelie sex difference.
  B) That's the interaction alone.
  C) Adds instead of subtracting.
- **Hint:** sexmale + sexmale:speciesChinstrap.

### ch21-book-04
- **Kind:** Course original
- **Concepts:** Visualizing interactions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-book-mass-sex-species.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-book-mass-sex-species.png)
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

The plot shows body mass by sex and species; large points are group means. Which aspect suggests an interaction between sex and species?

- **Options:**

  A) That body mass differs by species
  B) That body mass differs by sex (the lines connecting female and male means slope upward)
  C) That the line connecting male and female means is steeper for Gentoo than for Adelie and Chinstrap (the lines aren't parallel)
  D) Such plots don't convey information about interactions

- **Answer (tutor only):** C
- **Explanation (tutor only):** Non-parallel lines mean the sex difference depends on species: an interaction.
- **Why the wrong options are wrong (tutor only):**
  A) and B) Those are main effects.
  D) Interaction plots are exactly for this.
- **Hint:** What would the lines look like with no interaction?

### ch21-book-04-v1
- **Kind:** AI-written version of ch21-book-04
- **Concepts:** Visualizing interactions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-book-mass-sex-species.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-book-mass-sex-species.png)
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

The plot shows body mass by sex and species; large points are group means. Which aspect shows a main effect of sex?

- **Options:**

  A) Body mass varies a lot within each group
  B) Gentoos are heavier than the other species
  C) The lines for each species aren't parallel
  D) Males are heavier than females in every species

- **Answer (tutor only):** D
- **Explanation (tutor only):** A consistent male-female difference is the sex main effect.
- **Why the wrong options are wrong (tutor only):**
  A) That's within-group variation.
  B) That's a species effect.
  C) That's an interaction.
- **Hint:** Female vs male.

### ch21-book-04-v2
- **Kind:** AI-written version of ch21-book-04
- **Concepts:** Visualizing interactions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-book-mass-sex-species.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-book-mass-sex-species.png)
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

The plot shows body mass by sex and species; large points are group means. In which species is the male-female difference largest?

- **Options:**

  A) Gentoo
  B) Adelie
  C) Chinstrap
  D) It is the same in all three species

- **Answer (tutor only):** A
- **Explanation (tutor only):** The Gentoo line is steepest (about 805 g vs 675 g for Adelie and 412 g for Chinstrap).
- **Why the wrong options are wrong (tutor only):**
  B) and C) Smaller gaps.
  D) The interaction says they differ.
- **Hint:** Which line is steepest?

### ch21-book-05
- **Kind:** Course original
- **Concepts:** What interactions mean; Testing interactions
- **Type:** MC
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

car::Anova(penguin_interaction_model, type = "II")
             Sum Sq  Df F value    Pr(>F)
sex          37090262   1 387.460 < 2.2e-16
species     143401584   2 749.016 < 2.2e-16
sex:species   1676557   2   8.757 0.0001973
Residuals    31302628 327

The small p-value for sex:species means we reject the null that:

- **Options:**

  A) Male and female penguins have the same average body mass
  B) All penguin species have the same average body mass
  C) Sex and species are independent
  D) The sex difference in body mass is identical across species

- **Answer (tutor only):** D
- **Explanation (tutor only):** The interaction tests whether the male-female difference is the same in every species.
- **Why the wrong options are wrong (tutor only):**
  A) and B) Those are the main-effect nulls.
  C) That's about the composition of the sample, not body mass.
- **Hint:** What does the interaction term model?

### ch21-book-05-v1
- **Kind:** AI-written version of ch21-book-05
- **Concepts:** What interactions mean; Testing interactions
- **Type:** MC
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

car::Anova(penguin_interaction_model, type = "II")
             Sum Sq  Df F value    Pr(>F)
sex          37090262   1 387.460 < 2.2e-16
species     143401584   2 749.016 < 2.2e-16
sex:species   1676557   2   8.757 0.0001973
Residuals    31302628 327

What do we conclude about the sex:species interaction at α = 0.05?

- **Options:**

  A) Reject the null: males are heavier in every species
  B) Fail to reject: species don't differ in their mass
  C) Fail to reject: the sex difference is the same in each
  D) Reject the null: the sex difference varies by species

- **Answer (tutor only):** D
- **Explanation (tutor only):** p = 0.0002 < 0.05, so the male-female difference differs among species.
- **Why the wrong options are wrong (tutor only):**
  A) That's not what the interaction tests.
  B) Wrong term.
  C) p < α.
- **Hint:** What does the interaction test?

### ch21-book-05-v2
- **Kind:** AI-written version of ch21-book-05
- **Concepts:** What interactions mean; Testing interactions
- **Type:** MC
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

car::Anova(penguin_interaction_model, type = "II")
             Sum Sq  Df F value    Pr(>F)
sex          37090262   1 387.460 < 2.2e-16
species     143401584   2 749.016 < 2.2e-16
sex:species   1676557   2   8.757 0.0001973
Residuals    31302628 327

Why does the sex:species term have 2 degrees of freedom?

- **Options:**

  A) It is 327 - 325, from the residuals
  B) Interactions always have exactly 2 df
  C) (2 - 1) sexes × (3 - 1) species = 2
  D) There are 2 sexes in the dataset

- **Answer (tutor only):** C
- **Explanation (tutor only):** Interaction df = (levels of sex - 1) × (levels of species - 1) = 1 × 2.
- **Why the wrong options are wrong (tutor only):**
  A) Not how df work.
  B) Depends on the levels.
  D) Coincidence here.
- **Hint:** Multiply the main effects' df.

### ch21-book-06
- **Kind:** Course original
- **Concepts:** Testing interactions
- **Type:** MC
- **Question:**

Why use car::Anova() rather than base R's anova() to test terms in an interaction model?

- **Options:**

  A) Base R's anova() is sequential, so term order can matter
  B) Base R can't fit models that include interactions
  C) anova() assumes the residuals are normally distributed
  D) car::Anova() proves that the interaction is causal

- **Answer (tutor only):** A
- **Explanation (tutor only):** Type II tests each term after adjusting for others of the same order, so results don't depend on the order we typed the terms.
- **Why the wrong options are wrong (tutor only):**
  B) It can.
  C) Both rely on the same assumptions.
  D) No test proves causation.
- **Hint:** What's different about how anova() handles the first term?

### ch21-book-06-v1
- **Kind:** AI-written version of ch21-book-06
- **Concepts:** Testing interactions
- **Type:** MC
- **Question:**

Two students fit lm(y ~ a + b + a:b) and lm(y ~ b + a + a:b) and run base R's anova() on each. Why might their tables disagree for a and b?

- **Options:**

  A) The two models make different predictions for each observation
  B) anova() is sequential, so the first term isn't adjusted for later ones
  C) Base R picks a random reference level for each model it fits
  D) They can't disagree; the models are identical

- **Answer (tutor only):** B
- **Explanation (tutor only):** Type I SS depend on order when predictors are correlated. car::Anova() avoids this.
- **Why the wrong options are wrong (tutor only):**
  A) Same model, same predictions.
  C) Not random.
  D) The tables can differ even though the model is the same.
- **Hint:** Sequential sums of squares.

### ch21-book-06-v2
- **Kind:** AI-written version of ch21-book-06
- **Concepts:** Testing interactions
- **Type:** MC
- **Question:**

In car::Anova(model, type = 'II') for lm(y ~ a + b + a:b), what is the main effect of a adjusted for?

- **Options:**

  A) b (but not the a:b interaction)
  B) Nothing; it's tested first
  C) The a:b interaction only
  D) Both b and the interaction

- **Answer (tutor only):** A
- **Explanation (tutor only):** Type II adjusts each main effect for the other main effects, not for interactions containing it.
- **Why the wrong options are wrong (tutor only):**
  B) That's Type I for the first term.
  C) and D) That's closer to Type III.
- **Hint:** Same-order terms.

### ch21-book-07
- **Kind:** Course original
- **Concepts:** Predictions & coefficients
- **Type:** matching
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

summary(penguin_interaction_model)
                         Estimate Std. Error t value Pr(>|t|)
(Intercept)               3368.84      36.21  93.030  < 2e-16
sexmale                    674.66      51.21  13.174  < 2e-16
speciesChinstrap           158.37      64.24   2.465  0.01420
speciesGentoo             1310.91      54.42  24.088  < 2e-16
sexmale:speciesChinstrap  -262.89      90.85  -2.894  0.00406
sexmale:speciesGentoo      130.44      76.44   1.706  0.08886

Consider the (Intercept) p-value.

1. It tests the null hypothesis that...
2. This test is silly because...

- **Options:**

  A) we already know penguins don't have an average body mass of zero grams
  B) the mean body mass of female Adelie penguins is zero
  C) the mean body mass of all penguins is zero
  D) intercepts can't be estimated in models with interactions

- **Answer (tutor only):** 1-B, 2-A
- **Explanation (tutor only):** The intercept is the prediction for the reference levels (female, Adelie). Its p-value tests whether that mean is zero, which is obviously false.
- **Why the wrong options are wrong (tutor only):**
  C) The intercept is for the reference group, not all penguins. D) They can.
- **Hint:** Which penguins does the intercept describe?

### ch21-book-07-v1
- **Kind:** AI-written version of ch21-book-07
- **Concepts:** Predictions & coefficients
- **Type:** MC
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

summary(penguin_interaction_model)
                         Estimate Std. Error t value Pr(>|t|)
(Intercept)               3368.84      36.21  93.030  < 2e-16
sexmale                    674.66      51.21  13.174  < 2e-16
speciesChinstrap           158.37      64.24   2.465  0.01420
speciesGentoo             1310.91      54.42  24.088  < 2e-16
sexmale:speciesChinstrap  -262.89      90.85  -2.894  0.00406
sexmale:speciesGentoo      130.44      76.44   1.706  0.08886

What does the sexmale coefficient (674.66) describe in this interaction model?

- **Options:**

  A) The male - female difference in Adelies only
  B) The male - female difference averaged over species
  C) The difference in average mass between Adelie and Gentoo
  D) The male - female difference in every one of the species

- **Answer (tutor only):** A
- **Explanation (tutor only):** With an interaction, sexmale is the sex difference at the reference species (Adelie).
- **Why the wrong options are wrong (tutor only):**
  B) That's from emmeans.
  C) That's a species coefficient.
  D) The interaction says it varies.
- **Hint:** Reference species.

### ch21-book-07-v2
- **Kind:** AI-written version of ch21-book-07
- **Concepts:** Predictions & coefficients
- **Type:** matching
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

summary(penguin_interaction_model)
                         Estimate Std. Error t value Pr(>|t|)
(Intercept)               3368.84      36.21  93.030  < 2e-16
sexmale                    674.66      51.21  13.174  < 2e-16
speciesChinstrap           158.37      64.24   2.465  0.01420
speciesGentoo             1310.91      54.42  24.088  < 2e-16
sexmale:speciesChinstrap  -262.89      90.85  -2.894  0.00406
sexmale:speciesGentoo      130.44      76.44   1.706  0.08886

Match each coefficient to the group comparison it describes:

1. speciesGentoo
2. sexmale:speciesGentoo

- **Options:**

  A) How much larger the sex gap is in Gentoos than Adelies
  B) Male Gentoo minus male Adelie
  C) Gentoo minus Adelie, averaged over sexes
  D) Female Gentoo minus female Adelie

- **Answer (tutor only):** 1-D, 2-A
- **Explanation (tutor only):** Main effects are at the reference sex (female); the interaction is the extra sex difference in Gentoos.
- **Why the wrong options are wrong (tutor only):**
  Reference levels matter.
- **Hint:** Female is the reference sex.

### ch21-book-08
- **Kind:** Course original
- **Concepts:** Predictions & coefficients; Main effects with interactions
- **Type:** select-all
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

summary(penguin_interaction_model)
                         Estimate Std. Error t value Pr(>|t|)
(Intercept)               3368.84      36.21  93.030  < 2e-16
sexmale                    674.66      51.21  13.174  < 2e-16
speciesChinstrap           158.37      64.24   2.465  0.01420
speciesGentoo             1310.91      54.42  24.088  < 2e-16
sexmale:speciesChinstrap  -262.89      90.85  -2.894  0.00406
sexmale:speciesGentoo      130.44      76.44   1.706  0.08886

Why should we be cautious about interpreting the speciesChinstrap p-value (0.014)? (Select all that apply.)

- **Options:**

  A) It's only one reference-level comparison, not a test of the whole species term
  B) Main effects require extra care when interactions are in the model (this compares female Chinstraps to female Adelies only)
  C) It doesn't account for the multiple species comparisons we might make
  D) Chinstrap penguins were randomly assigned to species

- **Answer (tutor only):** A, B, C
- **Explanation (tutor only):** speciesChinstrap compares female Chinstrap to female Adelie (the reference sex), isn't a test of species overall, and isn't corrected for multiple comparisons.
- **Why the wrong options are wrong (tutor only):**
  D) Nonsense: species can't be assigned.
- **Hint:** What exactly does this coefficient compare?

### ch21-book-08-v1
- **Kind:** AI-written version of ch21-book-08
- **Concepts:** Predictions & coefficients; Main effects with interactions
- **Type:** select-all
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

summary(penguin_interaction_model)
                         Estimate Std. Error t value Pr(>|t|)
(Intercept)               3368.84      36.21  93.030  < 2e-16
sexmale                    674.66      51.21  13.174  < 2e-16
speciesChinstrap           158.37      64.24   2.465  0.01420
speciesGentoo             1310.91      54.42  24.088  < 2e-16
sexmale:speciesChinstrap  -262.89      90.85  -2.894  0.00406
sexmale:speciesGentoo      130.44      76.44   1.706  0.08886

What does the sexmale:speciesGentoo p-value (0.089) test? (Select all that apply.)

- **Options:**

  A) Whether Gentoo males are heavier than Gentoo females
  B) Whether the sex difference differs between Gentoo and Adelie
  C) Whether Gentoos are heavier than Adelies overall

- **Answer (tutor only):** B
- **Explanation (tutor only):** It tests whether the Gentoo sex gap differs from the Adelie sex gap.
- **Why the wrong options are wrong (tutor only):**
  A) That's a different comparison.
  C) That's a species comparison.
- **Hint:** Interaction = difference of differences.

### ch21-book-08-v2
- **Kind:** AI-written version of ch21-book-08
- **Concepts:** Predictions & coefficients; Main effects with interactions
- **Type:** select-all
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

summary(penguin_interaction_model)
                         Estimate Std. Error t value Pr(>|t|)
(Intercept)               3368.84      36.21  93.030  < 2e-16
sexmale                    674.66      51.21  13.174  < 2e-16
speciesChinstrap           158.37      64.24   2.465  0.01420
speciesGentoo             1310.91      54.42  24.088  < 2e-16
sexmale:speciesChinstrap  -262.89      90.85  -2.894  0.00406
sexmale:speciesGentoo      130.44      76.44   1.706  0.08886

Which is the best way to test whether species matters overall in this model? (Select all that apply.)

- **Options:**

  A) The p-value for the (Intercept) in summary()
  B) The Type II F test for species from car::Anova()
  C) The p-value for speciesChinstrap in summary()

- **Answer (tutor only):** B
- **Explanation (tutor only):** The F test asks about the species term as a whole.
- **Why the wrong options are wrong (tutor only):**
  A) Tests whether female Adelie mass is zero.
  C) One reference comparison, for females only.
- **Hint:** One test for the whole term.

### ch21-book-09
- **Kind:** Course original
- **Concepts:** Main effects with interactions
- **Type:** MC
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

emmeans(penguin_interaction_model, pairwise ~ sex)
NOTE: Results may be misleading due to involvement in interactions
 contrast      estimate   SE  df t.ratio p.value
 female - male     -631 35.7 327 -17.659 <0.0001
Results are averaged over the levels of: species

emmeans(penguin_interaction_model, pairwise ~ species)
NOTE: Results may be misleading due to involvement in interactions
 contrast           estimate   SE  df t.ratio p.value
 Adelie - Chinstrap    -26.9 45.4 327  -0.593  0.8241
 Adelie - Gentoo     -1376.1 38.2 327 -36.007 <0.0001
 Chinstrap - Gentoo  -1349.2 47.0 327 -28.682 <0.0001
Results are averaged over the levels of: sex

emmeans warns that the sex comparison 'may be misleading due to involvement in interactions.' What does the female - male contrast estimate, and is it reasonable to say males are heavier?

- **Options:**

  A) The sex difference in Adelies only; no, because interactions make main effects meaningless
  B) The sex difference averaged over species; yes, but we should add that the size of the difference varies among species
  C) The sex:species interaction; yes, and the difference is identical in every species
  D) The sex difference averaged over species; no, because female Gentoos outweigh male Chinstraps

- **Answer (tutor only):** B
- **Explanation (tutor only):** emmeans averages the sex difference over species, hence the warning. Males are heavier in every species, so 'males are heavier' is fair, as long as we note that the gap varies.
- **Why the wrong options are wrong (tutor only):**
  A) It's averaged over species, and main effects aren't meaningless when consistent.
  C) The interaction says the difference is NOT identical.
  D) Comparing across species doesn't address the sex difference within species.
- **Hint:** Is the male-female difference in the same direction in every species?

### ch21-book-09-v1
- **Kind:** AI-written version of ch21-book-09
- **Concepts:** Main effects with interactions
- **Type:** MC
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

emmeans(penguin_interaction_model, pairwise ~ sex)
NOTE: Results may be misleading due to involvement in interactions
 contrast      estimate   SE  df t.ratio p.value
 female - male     -631 35.7 327 -17.659 <0.0001
Results are averaged over the levels of: species

emmeans(penguin_interaction_model, pairwise ~ species)
NOTE: Results may be misleading due to involvement in interactions
 contrast           estimate   SE  df t.ratio p.value
 Adelie - Chinstrap    -26.9 45.4 327  -0.593  0.8241
 Adelie - Gentoo     -1376.1 38.2 327 -36.007 <0.0001
 Chinstrap - Gentoo  -1349.2 47.0 327 -28.682 <0.0001
Results are averaged over the levels of: sex

Why does emmeans warn that the sex contrast 'may be misleading'?

- **Options:**

  A) Males and females have identical average body mass
  B) It averages a sex gap that differs among species
  C) The species comparison is not statistically significant
  D) The emmeans sex contrast contains a calculation error

- **Answer (tutor only):** B
- **Explanation (tutor only):** With an interaction, a single average sex difference hides variation among species.
- **Why the wrong options are wrong (tutor only):**
  A) They differ by 631 g on average.
  C) Irrelevant.
  D) No error.
- **Hint:** Averaged over what?

### ch21-book-09-v2
- **Kind:** AI-written version of ch21-book-09
- **Concepts:** Main effects with interactions
- **Type:** MC
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

emmeans(penguin_interaction_model, pairwise ~ sex)
NOTE: Results may be misleading due to involvement in interactions
 contrast      estimate   SE  df t.ratio p.value
 female - male     -631 35.7 327 -17.659 <0.0001
Results are averaged over the levels of: species

emmeans(penguin_interaction_model, pairwise ~ species)
NOTE: Results may be misleading due to involvement in interactions
 contrast           estimate   SE  df t.ratio p.value
 Adelie - Chinstrap    -26.9 45.4 327  -0.593  0.8241
 Adelie - Gentoo     -1376.1 38.2 327 -36.007 <0.0001
 Chinstrap - Gentoo  -1349.2 47.0 327 -28.682 <0.0001
Results are averaged over the levels of: sex

Which statement about the female - male contrast (-631 g) is correct?

- **Options:**

  A) It is the sex difference in Adelie penguins only
  B) It is the sex difference in Gentoo penguins only
  C) It averages the sex difference across the three species
  D) It is the size of the interaction between sex and species

- **Answer (tutor only):** C
- **Explanation (tutor only):** 'Results are averaged over the levels of: species.'
- **Why the wrong options are wrong (tutor only):**
  A) That's sexmale from summary().
  B) Gentoo's gap is larger.
  D) Not an interaction.
- **Hint:** Read the note under the contrast.

### ch21-book-10
- **Kind:** Course original
- **Concepts:** Main effects with interactions
- **Type:** select-all
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

summary(penguin_interaction_model)
                         Estimate Std. Error t value Pr(>|t|)
(Intercept)               3368.84      36.21  93.030  < 2e-16
sexmale                    674.66      51.21  13.174  < 2e-16
speciesChinstrap           158.37      64.24   2.465  0.01420
speciesGentoo             1310.91      54.42  24.088  < 2e-16
sexmale:speciesChinstrap  -262.89      90.85  -2.894  0.00406
sexmale:speciesGentoo      130.44      76.44   1.706  0.08886

emmeans(penguin_interaction_model, pairwise ~ sex)
NOTE: Results may be misleading due to involvement in interactions
 contrast      estimate   SE  df t.ratio p.value
 female - male     -631 35.7 327 -17.659 <0.0001
Results are averaged over the levels of: species

emmeans(penguin_interaction_model, pairwise ~ species)
NOTE: Results may be misleading due to involvement in interactions
 contrast           estimate   SE  df t.ratio p.value
 Adelie - Chinstrap    -26.9 45.4 327  -0.593  0.8241
 Adelie - Gentoo     -1376.1 38.2 327 -36.007 <0.0001
 Chinstrap - Gentoo  -1349.2 47.0 327 -28.682 <0.0001
Results are averaged over the levels of: sex

Why is the Adelie - Chinstrap contrast from emmeans not significant (p = 0.82), while speciesChinstrap in summary() is (p = 0.014)? (Select the two correct answers.)

- **Options:**

  A) The emmeans contrast compares Adelie and Chinstrap averaged over sex, while speciesChinstrap compares female Chinstraps to female Adelies
  B) The emmeans contrast tests sex, while speciesChinstrap tests body mass
  C) The emmeans p-value is adjusted with Tukey's method, while the speciesChinstrap p-value is not
  D) They are the same test, so one of them must be wrong

- **Answer (tutor only):** A, C
- **Explanation (tutor only):** They answer different questions: females only vs averaged over sexes (and male Chinstraps are relatively light, so the average difference nearly vanishes). The emmeans p-value is also corrected for multiple comparisons.
- **Why the wrong options are wrong (tutor only):**
  B) Both are about species differences in body mass.
  D) They're different tests.
- **Hint:** Which penguins does each comparison use?

### ch21-book-10-v1
- **Kind:** AI-written version of ch21-book-10
- **Concepts:** Main effects with interactions
- **Type:** select-all
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

summary(penguin_interaction_model)
                         Estimate Std. Error t value Pr(>|t|)
(Intercept)               3368.84      36.21  93.030  < 2e-16
sexmale                    674.66      51.21  13.174  < 2e-16
speciesChinstrap           158.37      64.24   2.465  0.01420
speciesGentoo             1310.91      54.42  24.088  < 2e-16
sexmale:speciesChinstrap  -262.89      90.85  -2.894  0.00406
sexmale:speciesGentoo      130.44      76.44   1.706  0.08886

emmeans(penguin_interaction_model, pairwise ~ sex)
NOTE: Results may be misleading due to involvement in interactions
 contrast      estimate   SE  df t.ratio p.value
 female - male     -631 35.7 327 -17.659 <0.0001
Results are averaged over the levels of: species

emmeans(penguin_interaction_model, pairwise ~ species)
NOTE: Results may be misleading due to involvement in interactions
 contrast           estimate   SE  df t.ratio p.value
 Adelie - Chinstrap    -26.9 45.4 327  -0.593  0.8241
 Adelie - Gentoo     -1376.1 38.2 327 -36.007 <0.0001
 Chinstrap - Gentoo  -1349.2 47.0 327 -28.682 <0.0001
Results are averaged over the levels of: sex

The emmeans Adelie - Gentoo contrast is -1376 g, but speciesGentoo in summary() is 1311 g. Why do they differ in size? (Select all that apply.)

- **Options:**

  A) speciesGentoo compares females only
  B) emmeans averages over both sexes
  C) The Gentoo sex gap is larger than Adelie's

- **Answer (tutor only):** A, B, C
- **Explanation (tutor only):** speciesGentoo is the female-only difference (1311). Averaging over sexes adds half the extra male difference (130 / 2 ≈ 65), giving 1376.
- **Why the wrong options are wrong (tutor only):**
  All three statements together explain the gap.
- **Hint:** Which sexes does each compare?

### ch21-book-10-v2
- **Kind:** AI-written version of ch21-book-10
- **Concepts:** Main effects with interactions
- **Type:** select-all
- **Question:**

Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:

penguin_additive_model <- lm(body_mass ~ sex + species)
penguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)

summary(penguin_interaction_model)
                         Estimate Std. Error t value Pr(>|t|)
(Intercept)               3368.84      36.21  93.030  < 2e-16
sexmale                    674.66      51.21  13.174  < 2e-16
speciesChinstrap           158.37      64.24   2.465  0.01420
speciesGentoo             1310.91      54.42  24.088  < 2e-16
sexmale:speciesChinstrap  -262.89      90.85  -2.894  0.00406
sexmale:speciesGentoo      130.44      76.44   1.706  0.08886

emmeans(penguin_interaction_model, pairwise ~ sex)
NOTE: Results may be misleading due to involvement in interactions
 contrast      estimate   SE  df t.ratio p.value
 female - male     -631 35.7 327 -17.659 <0.0001
Results are averaged over the levels of: species

emmeans(penguin_interaction_model, pairwise ~ species)
NOTE: Results may be misleading due to involvement in interactions
 contrast           estimate   SE  df t.ratio p.value
 Adelie - Chinstrap    -26.9 45.4 327  -0.593  0.8241
 Adelie - Gentoo     -1376.1 38.2 327 -36.007 <0.0001
 Chinstrap - Gentoo  -1349.2 47.0 327 -28.682 <0.0001
Results are averaged over the levels of: sex

Which test asks whether Adelie and Chinstrap penguins differ in mass, averaged over sexes? (Select all that apply.)

- **Options:**

  A) The sexmale:speciesChinstrap p-value
  B) The emmeans Adelie - Chinstrap contrast
  C) The speciesChinstrap p-value in summary()

- **Answer (tutor only):** B
- **Explanation (tutor only):** emmeans averages over sex; speciesChinstrap is females only; the interaction compares sex gaps.
- **Why the wrong options are wrong (tutor only):**
  A) A difference in sex gaps.
  C) Females only.
- **Hint:** Averaged over sexes.

### ch21-book-11
- **Kind:** Course original
- **Concepts:** What interactions mean
- **Type:** MC
- **Question:**

Which of the following are linear models?

1. Modeling blood glucose in lizards kept at warm vs cool temperatures
2. Modeling algal growth as a function of nutrient concentration, allowing for a hump or trough (a polynomial)
3. Modeling tadpole growth as a function of pond, adjusting for initial body size
4. Modeling the different effect of fertilizer on plant height in wet and dry soil
5. Modeling log-transformed metabolic rate as a function of log-transformed body mass

- **Options:**

  A) Only 1, 3 and 4
  B) Only 1, 3, 4 and 5
  C) All of them (1-5)
  D) Only model 1

- **Answer (tutor only):** C
- **Explanation (tutor only):** All are linear models: predictions are sums of coefficients times predictors. That includes categorical predictors (1), polynomials (2: x and x² are both just predictors), covariates (3), interactions (4) and transformed variables (5).
- **Why the wrong options are wrong (tutor only):**
  Common mistake: thinking curved relationships (2) can't be linear models. 'Linear' refers to the coefficients, not the shape.
- **Hint:** 'Linear' means we add up coefficient × predictor terms.

### ch21-book-11-v1
- **Kind:** AI-written version of ch21-book-11
- **Concepts:** What interactions mean
- **Type:** MC
- **Question:**

Which of the following are linear models?

1. lm(height ~ fertilizer * soil_moisture)
2. lm(growth ~ temperature + I(temperature^2))
3. lm(log(mass) ~ log(length))
4. lm(yield ~ variety)

- **Options:**

  A) All four of them
  B) Only models 1 and 4
  C) Only models 3 and 4
  D) Only model 4

- **Answer (tutor only):** A
- **Explanation (tutor only):** Each prediction is a sum of coefficients times predictors, including interactions, polynomial terms and transformed variables.
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) leave out models that are still linear in their coefficients.
- **Hint:** Linear in the coefficients.

### ch21-book-11-v2
- **Kind:** AI-written version of ch21-book-11
- **Concepts:** What interactions mean
- **Type:** MC
- **Question:**

Why is lm(growth ~ temperature + I(temperature^2)) still a linear model, even though it fits a curve?

- **Options:**

  A) Polynomial terms are dropped automatically by R
  B) It isn't a linear model; it's a nonlinear model
  C) The curve is approximately straight over the range of data
  D) The prediction is still a sum of coefficients times predictors

- **Answer (tutor only):** D
- **Explanation (tutor only):** Linear refers to the coefficients: temperature² is just another predictor.
- **Why the wrong options are wrong (tutor only):**
  A) They aren't dropped.
  B) It is linear in its coefficients.
  C) It can be very curved.
- **Hint:** Linear in what?

### ch21-chimein-01
- **Kind:** Course original
- **Concepts:** What interactions mean; Main effects with interactions; Visualizing interactions
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-chimein-bill-sex-species.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-chimein-bill-sex-species.png)
- **Question:**

Palmer penguins: bill length of three Antarctic penguin species by sex. What does this plot show? (Select all that apply.)

- **Options:**

  A) A main effect of sex
  B) A main effect of species
  C) An interaction between sex and species

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** Males have longer bills than females in every species (sex effect), and species differ (species effect). The male-female gap is similar across species; a formal test finds no significant interaction (p = 0.10).
- **Why the wrong options are wrong (tutor only):**
  C) The gaps differ a little (largest in Chinstraps), but not by more than we'd expect from noise.
- **Hint:** Is the male-female gap about the same size in each species?

### ch21-chimein-01-v1
- **Kind:** AI-written version of ch21-chimein-01
- **Concepts:** What interactions mean; Main effects with interactions; Visualizing interactions
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-chimein-bill-sex-species.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-chimein-bill-sex-species.png)
- **Question:**

Palmer penguins: bill length of three Antarctic penguin species by sex. If you connected each species' female and male means with a line, what would you expect?

- **Options:**

  A) Lines that cross, with the sex effect reversing
  B) Lines with strongly different slopes for each species
  C) Roughly parallel lines, sloping up from female to male
  D) Flat lines, since sex has no effect on bill length

- **Answer (tutor only):** C
- **Explanation (tutor only):** Males are longer-billed in every species by similar amounts: roughly parallel lines (no significant interaction).
- **Why the wrong options are wrong (tutor only):**
  A) The sex effect doesn't reverse.
  B) The gaps are similar.
  D) There's a clear sex effect.
- **Hint:** Is the male-female gap similar across species?

### ch21-chimein-01-v2
- **Kind:** AI-written version of ch21-chimein-01
- **Concepts:** What interactions mean; Main effects with interactions; Visualizing interactions
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-chimein-bill-sex-species.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-chimein-bill-sex-species.png)
- **Question:**

Palmer penguins: bill length of three Antarctic penguin species by sex. Which model best matches this plot? (Select all that apply.)

- **Options:**

  A) lm(bill_len ~ species)
  B) lm(bill_len ~ sex + species)
  C) lm(bill_len ~ sex)

- **Answer (tutor only):** B
- **Explanation (tutor only):** Both sex and species matter, and their effects look roughly additive.
- **Why the wrong options are wrong (tutor only):**
  A) Ignores the consistent sex difference.
  C) Ignores big species differences.
- **Hint:** Which effects are visible?

### ch21-chimein-02
- **Kind:** Course original
- **Concepts:** What interactions mean; Main effects with interactions; Visualizing interactions
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-chimein-iris-petal.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-chimein-iris-petal.png)
- **Question:**

Iris petal length vs petal width for three iris species, with a separate regression line for each species. What does this plot show? (Select all that apply.)

- **Options:**

  A) A main effect of petal width
  B) A main effect of species
  C) An interaction between petal width and species

- **Answer (tutor only):** A, B, C
- **Explanation (tutor only):** Petal length rises with width, species differ, and the slopes differ clearly among species (interaction p < 0.001). Note that the species barely overlap in petal width, so each slope covers a different range.
- **Why the wrong options are wrong (tutor only):**
  All three are present.
- **Hint:** Are the slopes similar across species?

### ch21-chimein-02-v1
- **Kind:** AI-written version of ch21-chimein-02
- **Concepts:** What interactions mean; Main effects with interactions; Visualizing interactions
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-chimein-iris-petal.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-chimein-iris-petal.png)
- **Question:**

Iris petal length vs petal width for three iris species, with a separate regression line for each species. Which feature of the plot shows the interaction? (Select all that apply.)

- **Options:**

  A) The lines have different slopes
  B) The species are at different heights
  C) Petal length rises with petal width

- **Answer (tutor only):** A
- **Explanation (tutor only):** An interaction is about slopes differing among groups.
- **Why the wrong options are wrong (tutor only):**
  B) That's a species main effect.
  C) That's a petal width main effect.
- **Hint:** Interaction = non-parallel.

### ch21-chimein-02-v2
- **Kind:** AI-written version of ch21-chimein-02
- **Concepts:** What interactions mean; Main effects with interactions; Visualizing interactions
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-chimein-iris-petal.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-chimein-iris-petal.png)
- **Question:**

Iris petal length vs petal width for three iris species, with a separate regression line for each species. Why should we be careful comparing the slopes? (Select all that apply.)

- **Options:**

  A) The slopes are all exactly equal
  B) Each slope covers a different range of widths
  C) The species barely overlap in petal width

- **Answer (tutor only):** B, C
- **Explanation (tutor only):** Each species' line covers a different range, so differences in slope partly reflect different parts of the width axis.
- **Why the wrong options are wrong (tutor only):**
  A) They differ.
- **Hint:** Look at where each species falls on the x-axis.

### ch21-chimein-03
- **Kind:** Course original
- **Concepts:** What interactions mean; Main effects with interactions; Visualizing interactions
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-chimein-iris-sepal.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-chimein-iris-sepal.png)
- **Question:**

Iris sepal length vs sepal width for three iris species, with a separate regression line for each species. What does this plot show? (Select all that apply.)

- **Options:**

  A) A main effect of sepal width
  B) A main effect of species
  C) An interaction between sepal width and species

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** Sepal length rises with sepal width, and species differ, but the lines are roughly parallel (interaction p = 0.67).
- **Why the wrong options are wrong (tutor only):**
  C) The slopes are similar.
- **Hint:** Are the lines roughly parallel?

### ch21-chimein-03-v1
- **Kind:** AI-written version of ch21-chimein-03
- **Concepts:** What interactions mean; Main effects with interactions; Visualizing interactions
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-chimein-iris-sepal.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-chimein-iris-sepal.png)
- **Question:**

Iris sepal length vs sepal width for three iris species, with a separate regression line for each species. Which model best matches this plot? (Select all that apply.)

- **Options:**

  A) lm(Sepal.Length ~ Sepal.Width + Species)
  B) lm(Sepal.Length ~ Species)
  C) lm(Sepal.Length ~ Sepal.Width * Species)

- **Answer (tutor only):** A
- **Explanation (tutor only):** Roughly parallel lines at different heights: an additive model (the interaction isn't significant, p = 0.67).
- **Why the wrong options are wrong (tutor only):**
  B) Ignores the clear width effect.
  C) Not needed: lines are parallel.
- **Hint:** Parallel lines at different heights.

### ch21-chimein-03-v2
- **Kind:** AI-written version of ch21-chimein-03
- **Concepts:** What interactions mean; Main effects with interactions; Visualizing interactions
- **Type:** select-all
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-chimein-iris-sepal.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-chimein-iris-sepal.png)
- **Question:**

Iris sepal length vs sepal width for three iris species, with a separate regression line for each species. What would you expect for the interaction's p-value?

- **Options:**

  A) Impossible to guess
  B) Very small (p < 0.001)
  C) Large (not significant)
  D) Exactly 0.05

- **Answer (tutor only):** C
- **Explanation (tutor only):** Roughly parallel lines suggest no interaction (p = 0.67).
- **Why the wrong options are wrong (tutor only):**
  A) The plot gives a strong hint.
  B) That would need clearly different slopes.
  D) No reason.
- **Hint:** Are the lines parallel?

### ch21-chimein-04
- **Kind:** Course original
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** matching
- **Question:**

Palmer penguins: we modeled body mass (g) as a function of flipper length (mm), species, and their interaction:

lm(body_mass ~ flipper_len * species)
(Intercept) = -2536.0; flipper_len = 32.80; speciesChinstrap = -501.0; speciesGentoo = -4251.0;
flipper_len:speciesChinstrap = 1.74; flipper_len:speciesGentoo = 21.80

Match each penguin (flipper length 200 mm) to its predicted body mass:

1. Adelie
2. Chinstrap
3. Gentoo

- **Options:**

  A) 3871 g
  B) 4133 g
  C) 4024 g
  D) 6560 g

- **Answer (tutor only):** 1-C, 2-A, 3-B
- **Explanation (tutor only):** Adelie: -2536 + 32.8 × 200 = 4024. Chinstrap: -2536 - 501 + (32.8 + 1.74) × 200 = 3871. Gentoo: -2536 - 4251 + (32.8 + 21.8) × 200 = 4133.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: forgetting to add the interaction to the slope for Chinstrap or Gentoo.
- **Hint:** Each species gets its own intercept and its own slope.

### ch21-chimein-04-v1
- **Kind:** AI-written version of ch21-chimein-04
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** matching
- **Question:**

Palmer penguins: we modeled body mass (g) as a function of flipper length (mm), species, and their interaction:

lm(body_mass ~ flipper_len * species)
(Intercept) = -2536.0; flipper_len = 32.80; speciesChinstrap = -501.0; speciesGentoo = -4251.0;
flipper_len:speciesChinstrap = 1.74; flipper_len:speciesGentoo = 21.80

Match each penguin (flipper length 210 mm) to its predicted body mass:

1. Adelie
2. Chinstrap
3. Gentoo

- **Options:**

  A) 4352 g
  B) 4679 g
  C) 6888 g
  D) 4216 g

- **Answer (tutor only):** 1-A, 2-D, 3-B
- **Explanation (tutor only):** Adelie: -2536 + 32.8 × 210. Chinstrap: -3037 + 34.54 × 210. Gentoo: -6787 + 54.6 × 210.
- **Why the wrong options are wrong (tutor only):**
  C) is 32.8 × 210 without the intercept.
- **Hint:** Each species has its own intercept and slope.

### ch21-chimein-04-v2
- **Kind:** AI-written version of ch21-chimein-04
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** matching
- **Question:**

Palmer penguins: we modeled body mass (g) as a function of flipper length (mm), species, and their interaction:

lm(body_mass ~ flipper_len * species)
(Intercept) = -2536.0; flipper_len = 32.80; speciesChinstrap = -501.0; speciesGentoo = -4251.0;
flipper_len:speciesChinstrap = 1.74; flipper_len:speciesGentoo = 21.80

Match each species to its slope (g per mm of flipper length):

1. Adelie
2. Chinstrap
3. Gentoo

- **Options:**

  A) 54.60
  B) 34.54
  C) 32.80
  D) 21.80

- **Answer (tutor only):** 1-C, 2-B, 3-A
- **Explanation (tutor only):** Adelie: 32.80. Chinstrap: 32.80 + 1.74. Gentoo: 32.80 + 21.80.
- **Why the wrong options are wrong (tutor only):**
  D) is the Gentoo interaction term alone.
- **Hint:** Reference slope + interaction.

### ch21-chimein-05
- **Kind:** Course original
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** MC
- **Question:**

Palmer penguins: we modeled body mass (g) as a function of flipper length (mm), species, and their interaction:

lm(body_mass ~ flipper_len * species)
(Intercept) = -2536.0; flipper_len = 32.80; speciesChinstrap = -501.0; speciesGentoo = -4251.0;
flipper_len:speciesChinstrap = 1.74; flipper_len:speciesGentoo = 21.80

Gentoo are the heaviest penguins, yet speciesGentoo = -4251. Why?

- **Options:**

  A) The model is wrong and should be refit
  B) It's the difference at 0 mm flipper length, far outside the data
  C) Gentoos are actually lighter than Adelies of the same size
  D) Negative coefficients mean the variable isn't significant

- **Answer (tutor only):** B
- **Explanation (tutor only):** With an interaction, a species coefficient is the difference when flipper length = 0. Because the Gentoo slope is much steeper (54.6 vs 32.8 g/mm), the lines cross well below real flipper lengths. At realistic lengths, Gentoos are predicted to be heavier.
- **Why the wrong options are wrong (tutor only):**
  A) The model fits fine.
  C) They aren't.
  D) Sign and significance are unrelated.
- **Hint:** At what flipper length does the species coefficient apply?

### ch21-chimein-05-v1
- **Kind:** AI-written version of ch21-chimein-05
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** MC
- **Question:**

Palmer penguins: we modeled body mass (g) as a function of flipper length (mm), species, and their interaction:

lm(body_mass ~ flipper_len * species)
(Intercept) = -2536.0; flipper_len = 32.80; speciesChinstrap = -501.0; speciesGentoo = -4251.0;
flipper_len:speciesChinstrap = 1.74; flipper_len:speciesGentoo = 21.80

Why is the Gentoo slope (54.6 g/mm) so different from Adelie's (32.8 g/mm)?

- **Options:**

  A) speciesGentoo shifts the line down by 4251 g
  B) Gentoos have more data, so their slope is larger
  C) The flipper_len:speciesGentoo interaction adds 21.8 g/mm
  D) It isn't; they share one slope in this model

- **Answer (tutor only):** C
- **Explanation (tutor only):** With an interaction, each species' slope is the reference slope plus its interaction term.
- **Why the wrong options are wrong (tutor only):**
  A) That changes the intercept, not the slope.
  B) Sample size doesn't set the slope.
  D) The interaction gives separate slopes.
- **Hint:** Which term changes slopes?

### ch21-chimein-05-v2
- **Kind:** AI-written version of ch21-chimein-05
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** MC
- **Question:**

Palmer penguins: we modeled body mass (g) as a function of flipper length (mm), species, and their interaction:

lm(body_mass ~ flipper_len * species)
(Intercept) = -2536.0; flipper_len = 32.80; speciesChinstrap = -501.0; speciesGentoo = -4251.0;
flipper_len:speciesChinstrap = 1.74; flipper_len:speciesGentoo = 21.80

What does speciesChinstrap = -501 represent?

- **Options:**

  A) The difference in slopes between Chinstraps and Adelies
  B) The average mass difference between Chinstraps and Adelies
  C) The Chinstrap - Adelie difference at a flipper length of 0 mm
  D) How much lighter Chinstraps are at every flipper length

- **Answer (tutor only):** C
- **Explanation (tutor only):** With an interaction, a main effect is the difference where the other variable equals zero.
- **Why the wrong options are wrong (tutor only):**
  A) That's the interaction (1.74).
  B) and D) The difference varies with flipper length.
- **Hint:** Main effect in an interaction model.

### ch21-hw-01
- **Kind:** Course original
- **Concepts:** What interactions mean
- **Type:** MC
- **Question:**

When should you include an interaction in your model? (Choose the best answer.)

- **Options:**

  A) When you have enough degrees of freedom to evaluate it
  B) When your sample size is greater than 100
  C) When an interaction is scientifically meaningful for your question
  D) Whenever you have two variables
  E) When one of the variables is not numeric

- **Answer (tutor only):** C
- **Explanation (tutor only):** Include an interaction when there's a biological reason to expect the effect of one variable to depend on another, and when you have the data to estimate it.
- **Why the wrong options are wrong (tutor only):**
  A) and B) Enough data is necessary but not a reason by itself.
  D) Adding every possible interaction wastes power and invites overfitting.
  E) Variable type doesn't matter.
- **Hint:** Start from the biology.

### ch21-hw-01-v1
- **Kind:** AI-written version of ch21-hw-01
- **Concepts:** What interactions mean
- **Type:** MC
- **Question:**

A researcher includes an interaction between temperature and every one of 8 other variables, 'just in case'. What's the main problem?

- **Options:**

  A) R can't fit models with more than one interaction
  B) Interactions can only involve categorical variables
  C) Many interactions cost power and invite overfitting
  D) There's no problem; more interactions are always better

- **Answer (tutor only):** C
- **Explanation (tutor only):** Include interactions that make biological sense; each one spends data.
- **Why the wrong options are wrong (tutor only):**
  A) R can.
  B) Numeric variables can interact.
  D) Not true.
- **Hint:** Each term costs data.

### ch21-hw-01-v2
- **Kind:** AI-written version of ch21-hw-01
- **Concepts:** What interactions mean
- **Type:** MC
- **Question:**

Which is the best reason to include an interaction between fertilizer and soil moisture in a model of plant growth?

- **Options:**

  A) There's reason to expect fertilizer to work differently in wet vs dry soil
  B) Soil moisture is a numeric variable rather than a category
  C) Both variables are significant on their own in an additive model
  D) The dataset has more than 100 plants in it

- **Answer (tutor only):** A
- **Explanation (tutor only):** Interactions should be motivated by the biology: does the effect of one depend on the other?
- **Why the wrong options are wrong (tutor only):**
  B) Variable type isn't a reason.
  C) Main effects don't imply interactions.
  D) Sample size alone isn't a reason.
- **Hint:** Start from the biology.

### ch21-hw-02
- **Kind:** Course original
- **Concepts:** What interactions mean; Main effects with interactions
- **Type:** MC
- **Question:**

When is it reasonable to interpret main effects even when there is a significant interaction?

- **Options:**

  A) Never
  B) Whenever the p-value is less than α
  C) When the direction of the effect is consistent across all values of the other variable
  D) When the main effect's p-value is smaller than the interaction's

- **Answer (tutor only):** C
- **Explanation (tutor only):** If, say, males are heavier in every species but by different amounts, it's fair to say 'males are heavier' while noting that the size of the difference varies.
- **Why the wrong options are wrong (tutor only):**
  A) Too strict: consistent effects are still meaningful.
  B) and D) p-values don't decide this.
- **Hint:** Does the effect ever flip direction?

### ch21-hw-02-v1
- **Kind:** AI-written version of ch21-hw-02
- **Concepts:** What interactions mean; Main effects with interactions
- **Type:** MC
- **Question:**

In a study of fertilizer and two plant varieties, there's a significant interaction: fertilizer increases height in variety A but decreases it in variety B. Is it reasonable to report the main effect of fertilizer?

- **Options:**

  A) Yes: if its p-value is below α
  B) Yes: main effects are always meaningful
  C) No: interactions make all main effects zero
  D) No: the effect reverses, so an average is misleading

- **Answer (tutor only):** D
- **Explanation (tutor only):** When the direction flips, an average effect describes neither variety.
- **Why the wrong options are wrong (tutor only):**
  B) and A) Not when effects reverse.
  C) Main effects aren't zero; they're just hard to interpret.
- **Hint:** Does the direction change?

### ch21-hw-02-v2
- **Kind:** AI-written version of ch21-hw-02
- **Concepts:** What interactions mean; Main effects with interactions
- **Type:** MC
- **Question:**

Males are heavier than females in all three penguin species, but by different amounts (a significant interaction). Which summary is best?

- **Options:**

  A) Males are heavier by exactly the same amount in every species
  B) Nothing can be said about sex because of the interaction
  C) Sex doesn't matter, since there is a significant interaction
  D) Males are heavier in every species, but the gap varies by species

- **Answer (tutor only):** D
- **Explanation (tutor only):** When direction is consistent, a main effect is meaningful; add that its size varies.
- **Why the wrong options are wrong (tutor only):**
  A) The interaction says the gap varies.
  C) and B) Too strong.
- **Hint:** Is the direction consistent?

### ch21-hw-03
- **Kind:** Course original
- **Concepts:** Visualizing interactions
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-hw-four-models.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-hw-four-models.png)
- **Question:**

To ask which floral traits predict hybridization, we modeled the proportion of hybrid seed on 93 parviflora RILs planted at the GC site as a function of petal area (mm²) and petal color (pink or white).

Each panel shows the same data with lines from a different model. Match each panel to its explanatory variables:

1. Panel A
2. Panel B
3. Panel C
4. Panel D

- **Options:**

  A) Petal area, petal color, and their interaction
  B) Petal color only
  C) Petal area and petal color (additive)
  D) Petal area only

- **Answer (tutor only):** 1-D, 2-A, 3-C, 4-B
- **Explanation (tutor only):** A: one line for everyone (petal area only). B: different slopes for each color (interaction). C: parallel lines (additive). D: flat lines at each color's mean (color only).
- **Why the wrong options are wrong (tutor only):**
  Look for: one line vs two; parallel vs not; sloped vs flat.
- **Hint:** Are there two lines? Are they parallel? Are they flat?

### ch21-hw-03-v1
- **Kind:** AI-written version of ch21-hw-03
- **Concepts:** Visualizing interactions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-hw-four-models.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-hw-four-models.png)
- **Question:**

To ask which floral traits predict hybridization, we modeled the proportion of hybrid seed on 93 parviflora RILs planted at the GC site as a function of petal area (mm²) and petal color (pink or white).

Each panel shows the same data with lines from a different model. Which panel's model has the most parameters?

- **Options:**

  A) Panel B: petal area × petal color
  B) Panel D: petal color only
  C) Panel C: petal area + petal color
  D) Panel A: petal area only

- **Answer (tutor only):** A
- **Explanation (tutor only):** The interaction model estimates an intercept, an area slope, a color difference and a slope difference: 4 parameters.
- **Why the wrong options are wrong (tutor only):**
  C) 3 parameters.
  D) and B) 2 parameters.
- **Hint:** Count intercepts and slopes.

### ch21-hw-03-v2
- **Kind:** AI-written version of ch21-hw-03
- **Concepts:** Visualizing interactions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-hw-four-models.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-hw-four-models.png)
- **Question:**

To ask which floral traits predict hybridization, we modeled the proportion of hybrid seed on 93 parviflora RILs planted at the GC site as a function of petal area (mm²) and petal color (pink or white).

Each panel shows the same data with lines from a different model. In which panel are the lines flat?

- **Options:**

  A) Panel A: petal area only
  B) Panel B: area × color
  C) Panel D: petal color only
  D) Panel C: area + color

- **Answer (tutor only):** C
- **Explanation (tutor only):** Without petal area in the model, predictions don't change with area: flat lines at each color's mean.
- **Why the wrong options are wrong (tutor only):**
  A), B) and D) include petal area, so their lines slope.
- **Hint:** Which model ignores petal area?

### ch21-hw-04
- **Kind:** Course original
- **Concepts:** Testing interactions
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-hw-diag.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-hw-diag.png)
- **Question:**

To ask which floral traits predict hybridization, we modeled the proportion of hybrid seed on 93 parviflora RILs planted at the GC site as a function of petal area (mm²) and petal color (pink or white).

Diagnostic plots for lm(prop_hybrid ~ petal_area_mm * petal_color) are shown. Fill in: The residuals are (1) ____, and the variance in residuals is (2) ____.

- **Options:**

  A) normally distributed
  B) homoscedastic
  C) heteroscedastic
  D) not normally distributed

- **Answer (tutor only):** 1-D, 2-C
- **Explanation (tutor only):** The QQ plot curves away from the line (many zeros and a long right tail), and the spread of residuals grows with the fitted values.
- **Why the wrong options are wrong (tutor only):**
  Proportions with many zeros rarely give normal, equal-variance residuals.
- **Hint:** Look at the QQ plot and the scale-location plot.

### ch21-hw-04-v1
- **Kind:** AI-written version of ch21-hw-04
- **Concepts:** Testing interactions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-hw-diag.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-hw-diag.png)
- **Question:**

To ask which floral traits predict hybridization, we modeled the proportion of hybrid seed on 93 parviflora RILs planted at the GC site as a function of petal area (mm²) and petal color (pink or white).

Diagnostic plots for lm(prop_hybrid ~ petal_area_mm * petal_color) are shown. Which plot is best for judging normality of the residuals?

- **Options:**

  A) The QQ plot
  B) Residuals vs leverage
  C) Scale-location
  D) None of them

- **Answer (tutor only):** A
- **Explanation (tutor only):** QQ plots compare residuals to a normal distribution.
- **Why the wrong options are wrong (tutor only):**
  B) For influence.
  C) For equal variance.
  D) The QQ plot is designed for this.
- **Hint:** Quantiles.

### ch21-hw-04-v2
- **Kind:** AI-written version of ch21-hw-04
- **Concepts:** Testing interactions
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-hw-diag.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-hw-diag.png)
- **Question:**

To ask which floral traits predict hybridization, we modeled the proportion of hybrid seed on 93 parviflora RILs planted at the GC site as a function of petal area (mm²) and petal color (pink or white).

Diagnostic plots for lm(prop_hybrid ~ petal_area_mm * petal_color) are shown. Match each problem to its likely cause:

1. Skewed residuals
2. Spread of residuals growing with fitted values

- **Options:**

  A) Proportions near zero can't vary much, but larger ones can
  B) Many RILs set no hybrid seed, with a long right tail
  C) The RILs were not independent of one another
  D) Petal area was measured in the wrong units

- **Answer (tutor only):** 1-B, 2-A
- **Explanation (tutor only):** Pile-ups at zero skew the residuals; bounded proportions have smaller variance near zero.
- **Why the wrong options are wrong (tutor only):**
  C) and D) don't explain these patterns.
- **Hint:** Think about proportions near 0.

### ch21-hw-05
- **Kind:** Course original
- **Concepts:** Testing interactions
- **Type:** select-all
- **Question:**

To ask which floral traits predict hybridization, we modeled the proportion of hybrid seed on 93 parviflora RILs planted at the GC site as a function of petal area (mm²) and petal color (pink or white).

lm(prop_hybrid ~ petal_area_mm * petal_color)

Type II (car::Anova(model, type = "II")):
                           F      p
petal_color            39.57  <0.0001
petal_area_mm          18.85  <0.0001
petal_area_mm:petal_color  8.33  0.0049

Type III (car::Anova(model, type = "III")):
                           F      p
petal_color             1.91  0.170
petal_area_mm          26.09  <0.0001
petal_area_mm:petal_color  8.33  0.0049

Which terms are significantly associated with proportion hybrid seed with BOTH Type II and Type III sums of squares? (Select all that apply.)

- **Options:**

  A) Petal area
  B) The interaction between petal color and petal area
  C) Petal color

- **Answer (tutor only):** A, B
- **Explanation (tutor only):** Petal area and the interaction are significant either way. Petal color is significant with Type II but not Type III, because Type III tests color at a petal area of zero (with R's default contrasts), far outside the data.
- **Why the wrong options are wrong (tutor only):**
  C) Not significant with Type III.
- **Hint:** Check each term in both tables.

### ch21-hw-05-v1
- **Kind:** AI-written version of ch21-hw-05
- **Concepts:** Testing interactions
- **Type:** select-all
- **Question:**

To ask which floral traits predict hybridization, we modeled the proportion of hybrid seed on 93 parviflora RILs planted at the GC site as a function of petal area (mm²) and petal color (pink or white).

lm(prop_hybrid ~ petal_area_mm * petal_color)

Type II (car::Anova(model, type = "II")):
                           F      p
petal_color            39.57  <0.0001
petal_area_mm          18.85  <0.0001
petal_area_mm:petal_color  8.33  0.0049

Type III (car::Anova(model, type = "III")):
                           F      p
petal_color             1.91  0.170
petal_area_mm          26.09  <0.0001
petal_area_mm:petal_color  8.33  0.0049

Why is the interaction's test the same with Type II and Type III?

- **Options:**

  A) It's the highest-order term, adjusted for all others in both types
  B) Petal color and petal area are uncorrelated in these RILs
  C) Interactions are never affected by any type of sums of squares
  D) Type II and Type III are always the same for every term

- **Answer (tutor only):** A
- **Explanation (tutor only):** Both Type II and Type III test the highest-order term after all other terms.
- **Why the wrong options are wrong (tutor only):**
  B) Not the reason.
  C) Too general.
  D) The main effects differ here.
- **Hint:** What is the interaction adjusted for?

### ch21-hw-05-v2
- **Kind:** AI-written version of ch21-hw-05
- **Concepts:** Testing interactions
- **Type:** select-all
- **Question:**

To ask which floral traits predict hybridization, we modeled the proportion of hybrid seed on 93 parviflora RILs planted at the GC site as a function of petal area (mm²) and petal color (pink or white).

lm(prop_hybrid ~ petal_area_mm * petal_color)

Type II (car::Anova(model, type = "II")):
                           F      p
petal_color            39.57  <0.0001
petal_area_mm          18.85  <0.0001
petal_area_mm:petal_color  8.33  0.0049

Type III (car::Anova(model, type = "III")):
                           F      p
petal_color             1.91  0.170
petal_area_mm          26.09  <0.0001
petal_area_mm:petal_color  8.33  0.0049

Why is petal color not significant with Type III (p = 0.17)?

- **Options:**

  A) The interaction removes all of petal color's effect
  B) Petal color has no association with hybrid seed in these data
  C) Type III tests color at a petal area of 0, far outside the data
  D) Type III always gives larger p-values than Type II does

- **Answer (tutor only):** C
- **Explanation (tutor only):** With an interaction (and default contrasts), Type III tests each main effect where the other variable is 0.
- **Why the wrong options are wrong (tutor only):**
  A) Color still matters at real petal areas.
  B) Type II finds a strong color effect.
  D) Not always.
- **Hint:** Where is the color effect evaluated?

### ch21-hw-06
- **Kind:** Course original
- **Concepts:** Main effects with interactions
- **Type:** MC
- **Question:**

To ask which floral traits predict hybridization, we modeled the proportion of hybrid seed on 93 parviflora RILs planted at the GC site as a function of petal area (mm²) and petal color (pink or white).

The interaction between petal color and petal area is significant. With the usual caveats about NHST, this means:

- **Options:**

  A) The predicted effect of petal area on proportion hybrid seed depends on petal color
  B) Petal color and petal area are significantly correlated
  C) Both petal color and petal area have significant main effects
  D) The relationship between petal area and hybrid proportion is the same for both colors

- **Answer (tutor only):** A
- **Explanation (tutor only):** An interaction means the slope for one variable differs across values of the other: here, hybrid seed rises more steeply with petal area in pink than in white flowers.
- **Why the wrong options are wrong (tutor only):**
  B) Correlation between predictors is a different issue (multicollinearity).
  C) An interaction says nothing about main effects.
  D) That's the null hypothesis we rejected.
- **Hint:** What does 'interaction' mean in words?

### ch21-hw-06-v1
- **Kind:** AI-written version of ch21-hw-06
- **Concepts:** Main effects with interactions
- **Type:** MC
- **Question:**

To ask which floral traits predict hybridization, we modeled the proportion of hybrid seed on 93 parviflora RILs planted at the GC site as a function of petal area (mm²) and petal color (pink or white). The interaction between petal color and petal area is significant. What would a plot of the model look like?

- **Options:**

  A) Flat lines at each color's mean hybrid seed
  B) Parallel lines for pink and white flowers
  C) One single line for both colors of flower
  D) Lines for pink and white with different slopes

- **Answer (tutor only):** D
- **Explanation (tutor only):** An interaction means different slopes for each color.
- **Why the wrong options are wrong (tutor only):**
  A) That's color only.
  B) That's additive.
  C) That's area only.
- **Hint:** Interaction = non-parallel.

### ch21-hw-06-v2
- **Kind:** AI-written version of ch21-hw-06
- **Concepts:** Main effects with interactions
- **Type:** MC
- **Question:**

To ask which floral traits predict hybridization, we modeled the proportion of hybrid seed on 93 parviflora RILs planted at the GC site as a function of petal area (mm²) and petal color (pink or white). The interaction between petal color and petal area is significant (p = 0.0049). Which statement is NOT supported by this result?

- **Options:**

  A) Petal color and petal area are strongly correlated with each other
  B) The petal area slope differs between pink and white flowers
  C) The model's lines for the two colors aren't parallel
  D) The effect of color depends on petal area

- **Answer (tutor only):** A
- **Explanation (tutor only):** An interaction is about effects depending on each other, not about predictors being correlated.
- **Why the wrong options are wrong (tutor only):**
  B), D) and C) are all what an interaction means.
- **Hint:** Interaction ≠ correlation.

### ch21-hw-07
- **Kind:** Course original
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** numeric
- **Question:**

To ask how petal area and anther-stigma distance (ASD) together predict hybridization in Clarkia RILs at GC, we fit:

lm(prop_hybrid ~ petal_area_mm * asd_mm)
(Intercept) = 0.300950; petal_area_mm = -0.004660; asd_mm = -0.448186; petal_area_mm:asd_mm = 0.009506

Predict the proportion (not percent) of hybrid seed for a RIL with an ASD of 2 mm and a petal area of 100 mm².

- **Answer (tutor only):** 0.84
- **Explanation (tutor only):** 0.30095 + (-0.00466 × 100) + (-0.448186 × 2) + (0.009506 × 100 × 2) = 0.301 - 0.466 - 0.896 + 1.901 = 0.84.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: forgetting that the interaction term multiplies petal area by ASD (100 × 2 = 200).
- **Hint:** The interaction coefficient multiplies the product of the two predictors.

### ch21-hw-07-v1
- **Kind:** AI-written version of ch21-hw-07
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** numeric
- **Question:**

To ask how petal area and anther-stigma distance (ASD) together predict hybridization in Clarkia RILs at GC, we fit:

lm(prop_hybrid ~ petal_area_mm * asd_mm)
(Intercept) = 0.300950; petal_area_mm = -0.004660; asd_mm = -0.448186; petal_area_mm:asd_mm = 0.009506

Predict the proportion of hybrid seed for a RIL with an ASD of 1 mm and a petal area of 80 mm².

- **Answer (tutor only):** 0.24
- **Explanation (tutor only):** 0.30095 - 0.00466 × 80 - 0.448186 × 1 + 0.009506 × 80 × 1 = 0.24.
- **Hint:** Include the product term.

### ch21-hw-07-v2
- **Kind:** AI-written version of ch21-hw-07
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** numeric
- **Question:**

To ask how petal area and anther-stigma distance (ASD) together predict hybridization in Clarkia RILs at GC, we fit:

lm(prop_hybrid ~ petal_area_mm * asd_mm)
(Intercept) = 0.300950; petal_area_mm = -0.004660; asd_mm = -0.448186; petal_area_mm:asd_mm = 0.009506

What is the slope for petal area (change in proportion hybrid per mm²) for a RIL with an ASD of 2 mm? Report it to four decimals.

- **Answer (tutor only):** 0.0144
- **Explanation (tutor only):** Slope = -0.00466 + 0.009506 × 2 = 0.0144 per mm².
- **Hint:** petal_area_mm + interaction × ASD.

### ch21-quiz-01
- **Kind:** Course original
- **Concepts:** What interactions mean; Visualizing interactions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-quiz-olympics.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-quiz-olympics.png)
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

What trend does the plot suggest?

- **Options:**

  A) Both are getting faster, with women's times falling more steeply
  B) Both men and women are getting faster at exactly the same rate
  C) Men are getting faster, but women's times are not changing
  D) Women are now faster than men in the most recent Olympics

- **Answer (tutor only):** A
- **Explanation (tutor only):** Times drop over the years for both groups (lower time = faster). Women's times fall from about 12.2 s in 1928 to about 10.9 s, a steeper drop than men's over the same years, so the gap seems to be narrowing. Whether that difference in slopes is real is what the interaction tests.
- **Why the wrong options are wrong (tutor only):**
  B) The women's points fall more steeply than the men's.
  C) Women's times clearly fall.
  D) Women's times are still about 1 s slower.
- **Hint:** Lower times mean faster runners. Compare how steeply each set of points falls.

### ch21-quiz-01-v1
- **Kind:** AI-written version of ch21-quiz-01
- **Concepts:** What interactions mean; Visualizing interactions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-quiz-olympics.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-quiz-olympics.png)
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

In the plot, roughly how big is the gap between men's and women's winning times in recent Olympics?

- **Options:**

  A) About 3 seconds
  B) About 1 second
  C) About 0.1 seconds
  D) There is no gap

- **Answer (tutor only):** B
- **Explanation (tutor only):** Recent women's times are around 10.8 to 10.9 s and men's around 9.85 s: about 1 s apart.
- **Why the wrong options are wrong (tutor only):**
  A) Too large.
  C) Too small.
  D) Men are clearly faster.
- **Hint:** Compare the most recent points.

### ch21-quiz-01-v2
- **Kind:** AI-written version of ch21-quiz-01
- **Concepts:** What interactions mean; Visualizing interactions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch21-quiz-olympics.png](https://yanivjb.github.io/biostats-book/study_guide_exam2/images/ch21-quiz-olympics.png)
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

If straight lines were drawn through each group's points, would they be parallel?

- **Options:**

  A) Probably not: men's times seem to fall more steeply
  B) Yes: both groups fall at exactly the same rate
  C) Yes: neither group's times change over time
  D) Probably not: women's times seem to fall more steeply

- **Answer (tutor only):** D
- **Explanation (tutor only):** The women's points drop from about 12.2 to 10.9 s since 1928; the men's drop less over the same period. Non-parallel lines suggest an interaction.
- **Why the wrong options are wrong (tutor only):**
  A) The women's fall is steeper.
  B) The slopes look different.
  C) Both fall.
- **Hint:** Compare how steeply each set of points falls.

### ch21-quiz-02
- **Kind:** Course original
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** numeric
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

A model with NO interaction:

lm(Time ~ Year + Gender)
(Intercept) = 36.0528; Year = -0.01261; Gendermale = -1.0928

(Gendermale is 1 for men and 0 for women.) What winning time does this model predict for the MEN'S 100 m in 1940? Round to two decimal places.

- **Answer (tutor only):** 10.50
- **Explanation (tutor only):** 36.0528 - 0.01261 × 1940 - 1.0928 = 36.0528 - 24.463 - 1.0928 ≈ 10.50 s. (There were no Olympics in 1940; the model still gives a prediction because 1940 is within the range of the data.)
- **Hint:** Plug in Year = 1940 and Gendermale = 1.

### ch21-quiz-02-v1
- **Kind:** AI-written version of ch21-quiz-02
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** numeric
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

A model with NO interaction:

lm(Time ~ Year + Gender)
(Intercept) = 36.0528; Year = -0.01261; Gendermale = -1.0928

(Gendermale is 1 for men and 0 for women.) What winning time does this model predict for the MEN'S 100 m in 1960? Round to two decimal places.

- **Answer (tutor only):** 10.24
- **Explanation (tutor only):** 36.0528 - 0.01261 × 1960 - 1.0928 = 10.24 s.
- **Hint:** Plug in Year = 1960 and Gendermale = 1.

### ch21-quiz-02-v2
- **Kind:** AI-written version of ch21-quiz-02
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** numeric
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

A model with NO interaction:

lm(Time ~ Year + Gender)
(Intercept) = 36.0528; Year = -0.01261; Gendermale = -1.0928

According to this model, how much faster (in seconds) are men than women in ANY given year?

- **Answer (tutor only):** 1.0928
- **Explanation (tutor only):** Without an interaction, the gap is the same every year: the Gendermale coefficient, 1.09 s.
- **Hint:** Additive model: parallel lines.

### ch21-quiz-03
- **Kind:** Course original
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** numeric
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

A model with NO interaction:

lm(Time ~ Year + Gender)
(Intercept) = 36.0528; Year = -0.01261; Gendermale = -1.0928

(Gendermale is 1 for men and 0 for women.) What winning time does this model predict for the WOMEN'S 100 m in 1940? Round to two decimal places.

- **Answer (tutor only):** 11.59
- **Explanation (tutor only):** Women are the reference level, so Gendermale = 0: 36.0528 - 0.01261 × 1940 = 36.0528 - 24.463 ≈ 11.59 s.
- **Hint:** Plug in Year = 1940 and Gendermale = 0.

### ch21-quiz-03-v1
- **Kind:** AI-written version of ch21-quiz-03
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** numeric
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

A model with NO interaction:

lm(Time ~ Year + Gender)
(Intercept) = 36.0528; Year = -0.01261; Gendermale = -1.0928

(Gendermale is 1 for men and 0 for women.) What winning time does this model predict for the WOMEN'S 100 m in 1980? Round to two decimal places.

- **Answer (tutor only):** 11.08
- **Explanation (tutor only):** 36.0528 - 0.01261 × 1980 = 11.08 s.
- **Hint:** Gendermale = 0.

### ch21-quiz-03-v2
- **Kind:** AI-written version of ch21-quiz-03
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** numeric
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

A model with NO interaction:

lm(Time ~ Year + Gender)
(Intercept) = 36.0528; Year = -0.01261; Gendermale = -1.0928

By how many seconds does this model predict winning times fall over 40 years (for either gender)? Round to two decimal places.

- **Answer (tutor only):** 0.5
- **Explanation (tutor only):** 0.01261 × 40 = 0.50 s. Without an interaction, both genders share this slope.
- **Hint:** Slope × 40.

### ch21-quiz-04
- **Kind:** Course original
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** numeric
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

A model WITH an interaction:

lm(Time ~ Year * Gender)
(Intercept) = 44.3470; Year = -0.016822; Gendermale = -12.5206; Year:Gendermale = 0.005817

(Gendermale is 1 for men and 0 for women.) What winning time does this model predict for the MEN'S 100 m in 1940? Round to two decimal places.

- **Answer (tutor only):** 10.48
- **Explanation (tutor only):** 44.3470 - 0.016822 × 1940 - 12.5206 + 0.005817 × 1940 = 44.3470 - 32.635 - 12.5206 + 11.285 ≈ 10.48 s. For men, the slope is -0.016822 + 0.005817 = -0.011005 s per year.
- **Hint:** With Gendermale = 1, every term is in play, including Year × Gendermale.

### ch21-quiz-04-v1
- **Kind:** AI-written version of ch21-quiz-04
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** numeric
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

A model WITH an interaction:

lm(Time ~ Year * Gender)
(Intercept) = 44.3470; Year = -0.016822; Gendermale = -12.5206; Year:Gendermale = 0.005817

(Gendermale is 1 for men and 0 for women.) What winning time does this model predict for the MEN'S 100 m in 1980? Round to two decimal places.

- **Answer (tutor only):** 10.04
- **Explanation (tutor only):** 44.3470 - 0.016822 × 1980 - 12.5206 + 0.005817 × 1980 = 10.04 s.
- **Hint:** Include every term when Gendermale = 1.

### ch21-quiz-04-v2
- **Kind:** AI-written version of ch21-quiz-04
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** numeric
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

A model WITH an interaction:

lm(Time ~ Year * Gender)
(Intercept) = 44.3470; Year = -0.016822; Gendermale = -12.5206; Year:Gendermale = 0.005817

What is the slope for MEN (change in winning time per year)? Report it to four decimal places.

- **Answer (tutor only):** -0.011
- **Explanation (tutor only):** Men's slope = Year + Year:Gendermale = -0.016822 + 0.005817 = -0.0110 s per year.
- **Hint:** Add the interaction to the reference slope.

### ch21-quiz-05
- **Kind:** Course original
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** numeric
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

A model WITH an interaction:

lm(Time ~ Year * Gender)
(Intercept) = 44.3470; Year = -0.016822; Gendermale = -12.5206; Year:Gendermale = 0.005817

(Gendermale is 1 for men and 0 for women.) What winning time does this model predict for the WOMEN'S 100 m in 1940? Round to two decimal places.

- **Answer (tutor only):** 11.71
- **Explanation (tutor only):** With Gendermale = 0, both gender terms drop out: 44.3470 - 0.016822 × 1940 = 44.3470 - 32.635 ≈ 11.71 s.
- **Hint:** With Gendermale = 0, which terms drop out?

### ch21-quiz-05-v1
- **Kind:** AI-written version of ch21-quiz-05
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** numeric
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

A model WITH an interaction:

lm(Time ~ Year * Gender)
(Intercept) = 44.3470; Year = -0.016822; Gendermale = -12.5206; Year:Gendermale = 0.005817

(Gendermale is 1 for men and 0 for women.) What winning time does this model predict for the WOMEN'S 100 m in 1960? Round to two decimal places.

- **Answer (tutor only):** 11.38
- **Explanation (tutor only):** 44.3470 - 0.016822 × 1960 = 11.38 s.
- **Hint:** Gendermale = 0, so the gender terms drop out.

### ch21-quiz-05-v2
- **Kind:** AI-written version of ch21-quiz-05
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** numeric
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

A model WITH an interaction:

lm(Time ~ Year * Gender)
(Intercept) = 44.3470; Year = -0.016822; Gendermale = -12.5206; Year:Gendermale = 0.005817

What is the slope for WOMEN (change in winning time per year)? Report it to four decimal places.

- **Answer (tutor only):** -0.0168
- **Explanation (tutor only):** Women are the reference level, so their slope is just the Year coefficient: -0.0168 s per year.
- **Hint:** Which group is the reference?

### ch21-quiz-06
- **Kind:** Course original
- **Concepts:** Main effects with interactions
- **Type:** MC
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

lm(Time ~ Year * Gender) |> summary()
                  Estimate  Std. Error  t value  Pr(>|t|)
(Intercept)       44.3470    3.4760     12.76    < 0.001
Year              -0.0168    0.0018     -9.53    < 0.001
Gendermale       -12.5206    4.0760     -3.07     0.004
Year:Gendermale    0.0058    0.0021      2.80     0.008

Women are the reference level. The interaction term suggests that over the past 100 or so years, male gold medalists have been getting faster at:

- **Options:**

  A) A rate not significantly different from women's
  B) A significantly slower rate than women
  C) A significantly faster rate than women

- **Answer (tutor only):** B
- **Explanation (tutor only):** Women's times fall by 0.0168 s per year. The positive Year:Gendermale term (0.0058, p = 0.008) means men's slope is less steep: -0.0168 + 0.0058 = -0.0110 s per year. Men are improving more slowly than women, and the difference in slopes is significant.
- **Why the wrong options are wrong (tutor only):**
  A) p = 0.008 for the interaction, so the slopes differ significantly.
  C) A positive interaction makes men's negative slope closer to zero, so men are improving more slowly.
- **Hint:** The men's slope is Year + Year:Gendermale. Is that more or less negative than the women's slope?

### ch21-quiz-06-v1
- **Kind:** AI-written version of ch21-quiz-06
- **Concepts:** Main effects with interactions
- **Type:** MC
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

lm(Time ~ Year * Gender) |> summary()
                  Estimate  Std. Error  t value  Pr(>|t|)
(Intercept)       44.3470    3.4760     12.76    < 0.001
Year              -0.0168    0.0018     -9.53    < 0.001
Gendermale       -12.5206    4.0760     -3.07     0.004
Year:Gendermale    0.0058    0.0021      2.80     0.008

Women are the reference level. What does the Year:Gendermale coefficient (0.0058) measure?

- **Options:**

  A) The change in women's winning times per year of the Olympics
  B) How much less steeply men's times fall per year than women's
  C) How much faster men are than women, averaged over every year
  D) The probability that men and women improve at the same rate

- **Answer (tutor only):** B
- **Explanation (tutor only):** It's the difference in slopes (men minus women). Positive means men's negative slope is less steep.
- **Why the wrong options are wrong (tutor only):**
  A) That's the Year coefficient.
  C) That's not an interaction.
  D) Coefficients aren't probabilities.
- **Hint:** Difference in slopes.

### ch21-quiz-06-v2
- **Kind:** AI-written version of ch21-quiz-06
- **Concepts:** Main effects with interactions
- **Type:** MC
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

lm(Time ~ Year * Gender) |> summary()
                  Estimate  Std. Error  t value  Pr(>|t|)
(Intercept)       44.3470    3.4760     12.76    < 0.001
Year              -0.0168    0.0018     -9.53    < 0.001
Gendermale       -12.5206    4.0760     -3.07     0.004
Year:Gendermale    0.0058    0.0021      2.80     0.008

What null hypothesis does the Year:Gendermale p-value (0.008) test?

- **Options:**

  A) Winning times are not changing over the years
  B) Women's times are not changing over the years
  C) Men's and women's times change at the same rate
  D) Men's and women's times are the same on average

- **Answer (tutor only):** C
- **Explanation (tutor only):** The interaction tests whether the slopes differ.
- **Why the wrong options are wrong (tutor only):**
  A) and B) Those are about slopes themselves, not their difference.
  D) That's about the gap, not slopes.
- **Hint:** Interaction = difference in slopes.

### ch21-quiz-07
- **Kind:** Course original
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** TF
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

TRUE or FALSE: We can find the year when women's winning 100 m times will be faster than men's by following the lines from the interaction model into the future until they cross.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** That's an extreme extrapolation: the lines would cross around 2150, far beyond the data. Straight lines can't continue forever (they'd eventually predict negative times), and improvement slows as athletes approach physical limits. The model describes the years we have data for.
- **Why the wrong options are wrong (tutor only):**
  TRUE: the arithmetic gives a year, but the prediction lies far outside the data.
- **Hint:** Would a straight line still describe winning times 150 years from now?

### ch21-quiz-07-v1
- **Kind:** AI-written version of ch21-quiz-07
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** TF
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

TRUE or FALSE: Using the interaction model to predict the women's winning time in 1970 is an extrapolation.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** 1970 is within the years of women's data (1928 to 2004), so it's interpolation.
- **Why the wrong options are wrong (tutor only):**
  TRUE: 1970 is inside the data range.
- **Hint:** Is 1970 within 1928 to 2004?

### ch21-quiz-07-v2
- **Kind:** AI-written version of ch21-quiz-07
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** TF
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

TRUE or FALSE: Using the interaction model to predict the women's winning time in 1904 is an extrapolation.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** A
- **Explanation (tutor only):** Women's results start in 1928, so 1904 is outside their data.
- **Why the wrong options are wrong (tutor only):**
  FALSE: there are no women's data before 1928.
- **Hint:** When do women's results start?

### ch21-quiz-08
- **Kind:** Course original
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** MC
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

lm(Time ~ Year * Gender)
(Intercept) = 44.3470; Year = -0.016822; Gendermale = -12.5206; Year:Gendermale = 0.005817

Women are the reference level. What does the Gendermale coefficient (-12.52) represent?

- **Options:**

  A) The average difference between men's and women's winning times across all years
  B) How much faster men's times have improved per year compared with women's
  C) The predicted difference between men's and women's winning times in the year 0
  D) The men's winning time in the first Olympics

- **Answer (tutor only):** C
- **Explanation (tutor only):** In an interaction model, a main-effect coefficient is the difference when the other variable equals zero: here, the year 0. That's almost 2,000 years before the first modern Olympics, so the coefficient is huge and meaningless on its own (the real gap is about 1 s).
- **Why the wrong options are wrong (tutor only):**
  A) In an interaction model the gap changes with year.
  B) That's the Year:Gendermale interaction coefficient.
  D) Coefficients for categories are differences, not times.
- **Hint:** What is the value of Year when the gender coefficient applies?

### ch21-quiz-08-v1
- **Kind:** AI-written version of ch21-quiz-08
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** MC
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

lm(Time ~ Year * Gender)
(Intercept) = 44.3470; Year = -0.016822; Gendermale = -12.5206; Year:Gendermale = 0.005817

Women are the reference level. What does the Year coefficient (-0.0168) represent?

- **Options:**

  A) The change in women's winning times per year
  B) The change in men's winning times per year
  C) The average change in winning times per year
  D) The difference in slopes between men and women

- **Answer (tutor only):** A
- **Explanation (tutor only):** In an interaction model, Year is the slope for the reference group (women).
- **Why the wrong options are wrong (tutor only):**
  B) Men's slope adds the interaction.
  C) Not an average.
  D) That's the interaction.
- **Hint:** Reference group's slope.

### ch21-quiz-08-v2
- **Kind:** AI-written version of ch21-quiz-08
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** MC
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

lm(Time ~ Year * Gender)
(Intercept) = 44.3470; Year = -0.016822; Gendermale = -12.5206; Year:Gendermale = 0.005817

Why is the Intercept (44.35 s) not a sensible winning time?

- **Options:**

  A) It's the average winning time for men across all of the years
  B) It is sensible: early sprinters took about 44 s for 100 m
  C) It's the predicted winning time for the first modern Olympics
  D) It's the women's prediction for year 0, far outside the data

- **Answer (tutor only):** D
- **Explanation (tutor only):** The intercept is the prediction at Year = 0 for the reference group: a huge extrapolation.
- **Why the wrong options are wrong (tutor only):**
  A) Not an average.
  B) Nobody took 44 s.
  C) The first Olympics was 1896, not year 0.
- **Hint:** What year does the intercept refer to?

### ch21-quiz-09
- **Kind:** Course original
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** select-all
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

lm(Time ~ Year * Gender)
(Intercept) = 44.3470; Year = -0.016822; Gendermale = -12.5206; Year:Gendermale = 0.005817

We make a new variable, years_since_1928 = Year - 1928, and refit the interaction model with it in place of Year. Which of these change? (Select all that apply.)

- **Options:**

  A) The Gendermale coefficient
  B) The slope for women
  C) The interaction coefficient
  D) The predicted winning times for 1960

- **Answer (tutor only):** A
- **Explanation (tutor only):** Shifting Year only moves where 'zero' is. The Gendermale coefficient now gives the men-women gap in 1928 (the first Olympics with a women's 100 m): about -1.31 s instead of -12.52. Slopes, the interaction and all predictions stay the same.
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) Subtracting a constant from x doesn't change slopes or predictions.
- **Hint:** What does subtracting 1928 from every year change about the lines themselves?

### ch21-quiz-09-v1
- **Kind:** AI-written version of ch21-quiz-09
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** select-all
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

lm(Time ~ Year * Gender)
(Intercept) = 44.3470; Year = -0.016822; Gendermale = -12.5206; Year:Gendermale = 0.005817

We refit the interaction model using years_since_1928 = Year - 1928. Which of these stay the SAME? (Select all that apply.)

- **Options:**

  A) The interaction coefficient
  B) The intercept
  C) The slope for women
  D) The predicted times for 1960

- **Answer (tutor only):** A, C, D
- **Explanation (tutor only):** Centering moves 'zero', changing the intercept and the gender coefficient, but not slopes or predictions.
- **Why the wrong options are wrong (tutor only):**
  B) The intercept now describes women in 1928.
- **Hint:** What does shifting x change?

### ch21-quiz-09-v2
- **Kind:** AI-written version of ch21-quiz-09
- **Concepts:** What interactions mean; Predictions & coefficients
- **Type:** select-all
- **Question:**

Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928).

lm(Time ~ Year * Gender)
(Intercept) = 44.3470; Year = -0.016822; Gendermale = -12.5206; Year:Gendermale = 0.005817

After refitting with years_since_1928 = Year - 1928, the Gendermale coefficient is about -1.31. What does it now represent?

- **Options:**

  A) The difference in slopes between men and women
  B) The average men-women gap over all years
  C) The predicted men-women gap in year 0
  D) The predicted men-women gap in 1928

- **Answer (tutor only):** D
- **Explanation (tutor only):** Gendermale is the gap where years_since_1928 = 0, i.e. in 1928.
- **Why the wrong options are wrong (tutor only):**
  A) That's the interaction.
  B) Not an average.
  C) That was before centering.
- **Hint:** Where is the new zero?
