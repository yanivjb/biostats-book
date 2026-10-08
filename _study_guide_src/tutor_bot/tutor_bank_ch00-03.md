# Applied Biostats tutor: question bank, chapters 0–3 (Exam 1, chapters 0–12)

Knowledge file for the course tutor. Each question has an ID, its concepts, the question, options, the answer, an explanation, why each wrong option is wrong, and a hint. Fields marked **tutor only** must never be shown to the student before they have answered.

- **Course originals** come from the instructor's homework, quizzes, Chime Ins and book.
- **AI-written versions** test the same idea with a new scenario or numbers. Their ID ends in -v1 or -v2 and names the original.
- 725 questions in all. 157 use a figure and are marked **Figure question (website only)**: students practice those on the study-guide website, where the figure is shown. Use one only when a student brings it to you; its figure link is included.

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

## Chapter 0: Types of variables

### ch00-book-01
- **Kind:** Course original
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

In a species with pink or white flowers, flower color is a special kind of categorical variable known as a ___ variable.

- **Options:**

  A) Nominal
  B) Binary
  C) Ordinal
  D) Bimodal

- **Answer (tutor only):** B
- **Explanation (tutor only):** Flower color here has only two possible values, so it is binary. It is also unordered (nominal), but binary is the more specific description.
- **Why the wrong options are wrong (tutor only):**
  A) Nominal: true that pink is not greater or less than white, but with only two values, binary is the better description.
  C) Ordinal: ordinal categories have a natural order (small, medium, large). Pink and white do not.
  D) Bimodal describes the shape of a numeric distribution with two peaks, not a type of variable.
- **Hint:** How many different values can flower color take in this species?

### ch00-book-01-v1
- **Kind:** AI-written version of ch00-book-01
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

Whether or not a seed germinated (yes/no) is a special kind of categorical variable known as a ___ variable.

- **Options:**

  A) Nominal
  B) Binary
  C) Ordinal
  D) Continuous

- **Answer (tutor only):** B
- **Explanation (tutor only):** A categorical variable with exactly two possible values (germinated or not) is binary.
- **Why the wrong options are wrong (tutor only):**
  A) Nominal variables can have many unordered categories; binary is the special two-category case.
  C) Yes/no has no natural ranking.
  D) Germination here is a category, not a measurement on a scale.
- **Hint:** How many possible values are there?

### ch00-book-01-v2
- **Kind:** AI-written version of ch00-book-01
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

A researcher records whether each lizard was caught in the sun or in the shade. This variable is best described as:

- **Options:**

  A) Binary
  B) Ordinal
  C) Discrete
  D) Continuous

- **Answer (tutor only):** A
- **Explanation (tutor only):** Two unordered categories (sun or shade) make a binary variable.
- **Why the wrong options are wrong (tutor only):**
  B) Sun and shade aren't ranked.
  C) Discrete variables are counts; this is a category.
  D) There's no measurement scale here.
- **Hint:** Count the categories.

### ch00-book-02
- **Kind:** Course original
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

Which of these variables is best described as continuous?

- **Options:**

  A) Flower color (pink, white)
  B) Petal length
  C) Number of flowers on a plant

- **Answer (tutor only):** B
- **Explanation (tutor only):** Petal length can take any value within a range (e.g., 12.37 mm), so it is continuous.
- **Why the wrong options are wrong (tutor only):**
  A) Flower color is categorical (binary here), not numeric.
  C) Number of flowers is a count. It can only take whole numbers, so it is discrete.
- **Hint:** Which of these could fall between two whole numbers?

### ch00-book-02-v1
- **Kind:** AI-written version of ch00-book-02
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

Which of these variables is best described as continuous?

- **Options:**

  A) Number of eggs in a nest
  B) Body temperature of a lizard
  C) Species of lizard
  D) Whether a nest was predated (yes/no)

- **Answer (tutor only):** B
- **Explanation (tutor only):** Temperature can take any value in a range (32.4, 32.41 …), so it's continuous.
- **Why the wrong options are wrong (tutor only):**
  A) Eggs are counted in whole numbers: discrete.
  C) Species is a category (nominal).
  D) Yes/no is binary.
- **Hint:** Could the value fall between any two values you can name?

### ch00-book-02-v2
- **Kind:** AI-written version of ch00-book-02
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

Which of these variables is best described as continuous?

- **Options:**

  A) Number of leaves on a seedling
  B) Leaf color (green, yellow, brown)
  C) Seedling height in mm
  D) Rank of the seedling in a size contest (1st, 2nd, 3rd)

- **Answer (tutor only):** C
- **Explanation (tutor only):** Height is measured on a scale and can take any value within a range, so it's continuous.
- **Why the wrong options are wrong (tutor only):**
  A) Leaves are counted: discrete.
  B) Color categories are nominal.
  D) Ranks are ordinal.
- **Hint:** Is it counted, ranked, named, or measured?

### ch00-book-03
- **Kind:** Course original
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

The number of offspring produced by a single animal in one breeding season is:

- **Options:**

  A) Binary
  B) Continuous
  C) Discrete

- **Answer (tutor only):** C
- **Explanation (tutor only):** Offspring are counted in whole numbers (0, 1, 2, ...), so this is a discrete numeric variable.
- **Why the wrong options are wrong (tutor only):**
  A) Binary variables have only two possible values. An animal can have many different numbers of offspring.
  B) Continuous variables can take any value in a range. An animal can't have 2.5 offspring.
- **Hint:** Can an animal have 2.5 offspring?

### ch00-book-03-v1
- **Kind:** AI-written version of ch00-book-03
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

The number of seeds in a single fruit is:

- **Options:**

  A) Binary
  B) Continuous
  C) Discrete

- **Answer (tutor only):** C
- **Explanation (tutor only):** Seeds are counted in whole numbers (0, 1, 2, …), so the variable is discrete.
- **Why the wrong options are wrong (tutor only):**
  A) There are more than two possible values.
  B) You can't have 12.6 seeds.
- **Hint:** Can the value be a fraction?

### ch00-book-03-v2
- **Kind:** AI-written version of ch00-book-03
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

The number of times a bird visits a feeder in an hour is:

- **Options:**

  A) Discrete
  B) Continuous
  C) Ordinal
  D) Binary

- **Answer (tutor only):** A
- **Explanation (tutor only):** Visits are counted in whole numbers, so this is a discrete numeric variable.
- **Why the wrong options are wrong (tutor only):**
  B) There's no such thing as 3.7 visits.
  C) Counts have equal steps between values; ordinal categories don't.
  D) There are more than two possible values.
- **Hint:** Is it a count or a measurement?

### ch00-book-04
- **Kind:** Course original
- **Concepts:** Variable types
- **Type:** TF
- **Question:**

TRUE or FALSE: Populations of Clarkia that we named 100 and 22 are numeric.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** These numbers are just names (labels). Doing math with them is meaningless: population 100 is not 'bigger' than population 22, and their average (61) means nothing. They are nominal categorical.
- **Why the wrong options are wrong (tutor only):**
  TRUE: a number used as a name is still a category. Ask whether arithmetic on the values would mean anything.
- **Hint:** Would it make sense to average the population names?

### ch00-book-04-v1
- **Kind:** AI-written version of ch00-book-04
- **Concepts:** Variable types
- **Type:** TF
- **Question:**

TRUE or FALSE: Field sites labeled 1, 2 and 3 on a map are numeric variables.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** The numbers are just labels for sites. Site 3 isn't 'more' than site 1, and averaging site labels is meaningless, so the variable is categorical.
- **Why the wrong options are wrong (tutor only):**
  A) Being written as numbers doesn't make a variable numeric.
- **Hint:** Would the average site number mean anything?

### ch00-book-04-v2
- **Kind:** AI-written version of ch00-book-04
- **Concepts:** Variable types
- **Type:** TF
- **Question:**

TRUE or FALSE: Lab mice identified by ear-tag numbers (e.g., 1042, 1187) have a numeric variable for 'mouse ID'.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** Tag numbers identify individuals; arithmetic on them is meaningless. Mouse ID is a categorical (nominal) variable.
- **Why the wrong options are wrong (tutor only):**
  A) A number used as a name is still a name.
- **Hint:** Does mouse 1187 have more of something than mouse 1042?

### ch00-book-05
- **Kind:** Course original
- **Concepts:** Variable types
- **Type:** TF
- **Question:**

TRUE or FALSE: A variable on a Likert scale is clearly numeric. (Example Likert scale: How do you feel about Clarkia? (1) Love it, (2) Like it, (3) Don't care, (4) Do not like, (5) Hate it.)

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** Likert values are written as numbers, but they label ordered categories, so the variable is ordinal. People sometimes analyze Likert data as if numeric (e.g., averaging), which can be a reasonable shortcut, but it is not 'clearly' numeric. 'Clearly' is the key word.
- **Why the wrong options are wrong (tutor only):**
  TRUE: the numbers 1 to 5 stand for ordered categories. The gap between 'Love it' and 'Like it' need not equal the gap between 'Don't care' and 'Do not like'.
- **Hint:** Do the numbers measure an amount, or just label ordered choices?

### ch00-book-05-v1
- **Kind:** AI-written version of ch00-book-05
- **Concepts:** Variable types
- **Type:** TF
- **Question:**

TRUE or FALSE: Pain reported on a scale of 'none, mild, moderate, severe' is clearly numeric.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** The categories are ordered, but the gaps between them aren't necessarily equal, so this is an ordinal categorical variable. Coding it 0–3 doesn't make it truly numeric.
- **Why the wrong options are wrong (tutor only):**
  A) Order alone doesn't make a variable numeric; the spacing between levels is unknown.
- **Hint:** Is the step from mild to moderate the same size as from moderate to severe?

### ch00-book-05-v2
- **Kind:** AI-written version of ch00-book-05
- **Concepts:** Variable types
- **Type:** TF
- **Question:**

TRUE or FALSE: A plant's age in days since germination is numeric.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** A
- **Explanation (tutor only):** Days are measured on a scale with equal intervals, so arithmetic (differences, averages) makes sense. It's numeric.
- **Why the wrong options are wrong (tutor only):**
  B) Unlike labels or ordered categories, days since germination are true quantities.
- **Hint:** Does the average age make sense?

### ch00-book-06
- **Kind:** Course original
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

The variable kingdom (corresponding to one of the six kingdoms of life) is a ___ variable.

- **Options:**

  A) Nominal
  B) Binary
  C) Ordinal
  D) Discrete

- **Answer (tutor only):** A
- **Explanation (tutor only):** Kingdom has several categories with no natural order, so it is nominal.
- **Why the wrong options are wrong (tutor only):**
  B) Binary would require exactly two categories. There are six kingdoms.
  C) Ordinal categories have a natural order. Animals are not 'more' or 'less' than plants.
  D) Discrete describes whole-number counts, a kind of numeric variable. Kingdom is not a number.
- **Hint:** Is there a natural order to the kingdoms of life?

### ch00-book-06-v1
- **Kind:** AI-written version of ch00-book-06
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

The variable 'blood type' (A, B, AB or O) is a ___ variable.

- **Options:**

  A) Nominal
  B) Binary
  C) Ordinal
  D) Discrete

- **Answer (tutor only):** A
- **Explanation (tutor only):** Blood types are unordered categories, and there are more than two, so it's nominal.
- **Why the wrong options are wrong (tutor only):**
  B) There are four categories, not two.
  C) No blood type ranks above another.
  D) Discrete variables are counts.
- **Hint:** Is there a natural order? How many categories?

### ch00-book-06-v2
- **Kind:** AI-written version of ch00-book-06
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

The variable 'habitat type' (forest, grassland, wetland, desert) is a ___ variable.

- **Options:**

  A) Ordinal
  B) Nominal
  C) Continuous
  D) Binary

- **Answer (tutor only):** B
- **Explanation (tutor only):** Several unordered categories: nominal.
- **Why the wrong options are wrong (tutor only):**
  A) The habitats aren't ranked.
  C) There's no measurement scale.
  D) There are more than two categories.
- **Hint:** Does the order of the categories matter?

### ch00-book-07
- **Kind:** Course original
- **Concepts:** Variable types; Explanatory & response variables
- **Type:** TF
- **Question:**

TRUE or FALSE: A continuous variable can never be modeled as discrete and vice versa.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** How we treat a variable is partly a modeling choice. Counts with many possible values (e.g., number of seeds) are often analyzed as if continuous, and continuous measurements are sometimes binned into categories (e.g., small vs. large petals).
- **Why the wrong options are wrong (tutor only):**
  TRUE: variable type guides analysis, but it is not a fixed rule. The best treatment depends on the question and the data.
- **Hint:** Can you think of a count that takes so many values it behaves almost like a measurement?

### ch00-book-07-v1
- **Kind:** AI-written version of ch00-book-07
- **Concepts:** Variable types; Explanatory & response variables
- **Type:** TF
- **Question:**

TRUE or FALSE: Although body mass is continuous, it's sometimes reasonable to analyze it as categories (e.g., small, medium, large).

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** A
- **Explanation (tutor only):** How we model a variable is a choice. Continuous variables are sometimes binned (with some loss of information), and counts are often modeled as continuous.
- **Why the wrong options are wrong (tutor only):**
  B) Variable type guides the analysis, but it isn't an unbreakable rule.
- **Hint:** Is the way we model a variable fixed forever?

### ch00-book-07-v2
- **Kind:** AI-written version of ch00-book-07
- **Concepts:** Variable types; Explanatory & response variables
- **Type:** TF
- **Question:**

TRUE or FALSE: The number of seeds per plant (a count) can never be analyzed with methods meant for continuous data.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** When counts are large and varied (e.g., 0–500 seeds), treating them as continuous is often a sensible modeling choice.
- **Why the wrong options are wrong (tutor only):**
  A) Discrete and continuous are descriptions, not strict rules about which models are allowed.
- **Hint:** With counts in the hundreds, does the gap between 213 and 214 matter much?

### ch00-canvas-01
- **Kind:** Course original
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

Some flowers are sweet, others are minty, some smell neutral, while others smell like rotting meat. In this description, flower fragrance is a special kind of categorical variable known as a ___ variable.

- **Options:**

  A) Binary
  B) Nominal
  C) Continuous
  D) Ordinal

- **Answer (tutor only):** B
- **Explanation (tutor only):** Fragrance has several categories (sweet, minty, neutral, rotting meat) with no natural order, so it is nominal.
- **Why the wrong options are wrong (tutor only):**
  A) Binary would need exactly two categories. There are four.
  C) Continuous variables are numeric measurements. Fragrance categories are not numbers.
  D) Ordinal categories have a natural order. 'Minty' is not more or less than 'sweet'.
- **Hint:** How many categories are there, and do they have a natural order?

### ch00-canvas-01-v1
- **Kind:** AI-written version of ch00-canvas-01
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

Bird song is recorded as 'trill', 'whistle', 'buzz' or 'chatter'. Song type is a special kind of categorical variable known as a ___ variable.

- **Options:**

  A) Binary
  B) Nominal
  C) Continuous
  D) Ordinal

- **Answer (tutor only):** B
- **Explanation (tutor only):** Several unordered categories: nominal.
- **Why the wrong options are wrong (tutor only):**
  A) There are four song types, not two.
  C) These are categories, not measurements.
  D) No song type ranks above another.
- **Hint:** Is there a natural order to the categories?

### ch00-canvas-01-v2
- **Kind:** AI-written version of ch00-canvas-01
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

Fruit ripeness is scored as 'unripe', 'ripe' or 'overripe'. This is a ___ variable.

- **Options:**

  A) Nominal
  B) Ordinal
  C) Binary
  D) Continuous

- **Answer (tutor only):** B
- **Explanation (tutor only):** The categories have a natural order (unripe < ripe < overripe), so the variable is ordinal.
- **Why the wrong options are wrong (tutor only):**
  A) Nominal categories have no order; these do.
  C) There are three categories.
  D) There's no measurement scale.
- **Hint:** Can you put the categories in order?

### ch00-canvas-02
- **Kind:** Course original
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

Which of these variables is best described as continuous?

- **Options:**

  A) Total time visited by pollinator
  B) Number of pollinator visits
  C) Number of flowers

- **Answer (tutor only):** A
- **Explanation (tutor only):** Time can take any value in a range (e.g., 3.72 minutes), so total visit time is continuous.
- **Why the wrong options are wrong (tutor only):**
  B) Number of visits is a count of whole numbers, so it is discrete.
  C) Number of flowers is also a whole-number count, so it is discrete.
- **Hint:** Which of these could be measured with a stopwatch rather than counted?

### ch00-canvas-02-v1
- **Kind:** AI-written version of ch00-canvas-02
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

Which of these variables is best described as continuous?

- **Options:**

  A) Distance a seed travels from the parent plant
  B) Number of seeds dispersed
  C) Dispersal mode (wind, animal, water)

- **Answer (tutor only):** A
- **Explanation (tutor only):** Distance can take any value in a range, so it's continuous.
- **Why the wrong options are wrong (tutor only):**
  B) Seeds are counted: discrete.
  C) Dispersal mode is a category (nominal).
- **Hint:** Measured or counted?

### ch00-canvas-02-v2
- **Kind:** AI-written version of ch00-canvas-02
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

Which of these variables is best described as continuous?

- **Options:**

  A) Number of bees visiting a flower
  B) Nectar volume in a flower (µL)
  C) Flower color

- **Answer (tutor only):** B
- **Explanation (tutor only):** Nectar volume is measured on a continuous scale.
- **Why the wrong options are wrong (tutor only):**
  A) Bees are counted: discrete.
  C) Color is categorical.
- **Hint:** Which can take fractional values?

### ch00-canvas-03
- **Kind:** Course original
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

The number of pollinators that visit a plant in one day is a ____ variable.

- **Options:**

  A) Continuous
  B) Binary
  C) Discrete

- **Answer (tutor only):** C
- **Explanation (tutor only):** Pollinators are counted in whole numbers (0, 1, 2, ...), so this is a discrete numeric variable.
- **Why the wrong options are wrong (tutor only):**
  A) Continuous variables can take any value in a range. You can't have 2.5 pollinators.
  B) Binary variables have only two values. A plant can receive many different numbers of visitors.
- **Hint:** Can 2.5 pollinators visit a plant?

### ch00-canvas-03-v1
- **Kind:** AI-written version of ch00-canvas-03
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

The number of eggs a frog lays in one clutch is a ____ variable.

- **Options:**

  A) Continuous
  B) Binary
  C) Discrete

- **Answer (tutor only):** C
- **Explanation (tutor only):** Eggs are counted in whole numbers: discrete.
- **Why the wrong options are wrong (tutor only):**
  A) You can't lay 412.3 eggs.
  B) There are many possible values.
- **Hint:** Can the value be a fraction?

### ch00-canvas-03-v2
- **Kind:** AI-written version of ch00-canvas-03
- **Concepts:** Variable types
- **Type:** MC
- **Question:**

The number of aphids on a leaf is a ____ variable.

- **Options:**

  A) Discrete
  B) Continuous
  C) Nominal

- **Answer (tutor only):** A
- **Explanation (tutor only):** Aphids are counted, so the variable is discrete numeric.
- **Why the wrong options are wrong (tutor only):**
  B) Counts can't be fractional.
  C) It's a quantity, not a category.
- **Hint:** Counted or measured?

### ch00-canvas-04
- **Kind:** Course original
- **Concepts:** Variable types
- **Type:** TF
- **Question:**

TRUE or FALSE: Plant genotypes named 100 and 22 are numeric variables.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** The numbers are names (labels) for genotypes, so genotype is nominal categorical. Arithmetic on them is meaningless: genotype 100 is not 'more' than genotype 22.
- **Why the wrong options are wrong (tutor only):**
  TRUE: a number used as a name is still a category. Ask whether arithmetic on the values would mean anything.
- **Hint:** Would it make sense to average the genotype names?

### ch00-canvas-04-v1
- **Kind:** AI-written version of ch00-canvas-04
- **Concepts:** Variable types
- **Type:** TF
- **Question:**

TRUE or FALSE: Plots numbered 1 to 40 in a field experiment make 'plot number' a numeric variable.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** Plot numbers are labels. Plot 40 doesn't have 'more' of anything than plot 2, so plot number is categorical.
- **Why the wrong options are wrong (tutor only):**
  A) Numbers used as names don't make a variable numeric.
- **Hint:** Does arithmetic on plot numbers mean anything?

### ch00-canvas-04-v2
- **Kind:** AI-written version of ch00-canvas-04
- **Concepts:** Variable types
- **Type:** TF
- **Question:**

TRUE or FALSE: The number of fruits on each plant is a numeric variable.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** A
- **Explanation (tutor only):** Fruit number is a count: a discrete numeric variable where arithmetic makes sense (e.g., the mean number of fruits).
- **Why the wrong options are wrong (tutor only):**
  B) Unlike ID numbers, counts are real quantities.
- **Hint:** Is this a label or a quantity?

### ch00-canvas-05
- **Kind:** Course original
- **Concepts:** Variable types
- **Type:** TF
- **Question:**

TRUE or FALSE: We are nearing the end of the US Open tennis tournament. Tennis players' rankings are clearly numeric.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** Rankings are ordered categories (ordinal). The order is meaningful, but the gaps are not equal: the difference between #1 and #2 need not match the difference between #100 and #101.
- **Why the wrong options are wrong (tutor only):**
  TRUE: rankings look numeric, but they label positions in an order rather than measure an amount.
- **Hint:** Is the gap between #1 and #2 the same as the gap between #100 and #101?

### ch00-canvas-05-v1
- **Kind:** AI-written version of ch00-canvas-05
- **Concepts:** Variable types
- **Type:** TF
- **Question:**

TRUE or FALSE: Finishing place in a race (1st, 2nd, 3rd, …) is clearly numeric.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** Places are ordered, but the gaps aren't equal: 1st might win by a second and 2nd beat 3rd by a minute. That makes finishing place ordinal.
- **Why the wrong options are wrong (tutor only):**
  A) Order isn't the same as equal spacing.
- **Hint:** Is the gap between 1st and 2nd always the same as between 2nd and 3rd?

### ch00-canvas-05-v2
- **Kind:** AI-written version of ch00-canvas-05
- **Concepts:** Variable types
- **Type:** TF
- **Question:**

TRUE or FALSE: A runner's race time in seconds is numeric.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** A
- **Explanation (tutor only):** Time is measured on a scale with equal intervals, so it's numeric (continuous).
- **Why the wrong options are wrong (tutor only):**
  B) Unlike finishing place, time differences are meaningful.
- **Hint:** Does subtracting two times mean something?

### ch00-canvas-06
- **Kind:** Course original
- **Concepts:** Variable types; Explanatory & response variables
- **Type:** TF
- **Question:**

TRUE or FALSE: A discrete variable can never be modeled as continuous and vice versa.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** How we treat a variable is partly a modeling choice. Counts with many possible values are often analyzed as if continuous, and continuous measurements are sometimes binned into categories.
- **Why the wrong options are wrong (tutor only):**
  TRUE: variable type guides analysis, but it is not a fixed rule.
- **Hint:** Can you think of a count that takes so many values it behaves almost like a measurement?

### ch00-canvas-06-v1
- **Kind:** AI-written version of ch00-canvas-06
- **Concepts:** Variable types; Explanatory & response variables
- **Type:** TF
- **Question:**

TRUE or FALSE: The number of leaves on a plant (a count) can reasonably be modeled as continuous in some analyses.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** A
- **Explanation (tutor only):** Counts with many possible values are often treated as continuous. Modeling is a choice guided by, not dictated by, variable type.
- **Why the wrong options are wrong (tutor only):**
  B) Variable type isn't an unbreakable rule.
- **Hint:** If counts range from 0 to 300, how much does the 'whole number' part matter?

### ch00-canvas-06-v2
- **Kind:** AI-written version of ch00-canvas-06
- **Concepts:** Variable types; Explanatory & response variables
- **Type:** TF
- **Question:**

TRUE or FALSE: Once a variable is classified as continuous, it must always be analyzed as continuous.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** Analysts sometimes bin continuous variables or treat counts as continuous. Variable types describe data; they don't lock in the analysis.
- **Why the wrong options are wrong (tutor only):**
  A) That's too strict.
- **Hint:** Could there be good reasons to analyze body mass as small, medium or large?

## Chapter 1: Getting started with R

### ch01-book-01
- **Kind:** Course original
- **Concepts:** R basics; Errors & debugging
- **Type:** MC
- **Question:**

Entering "p"^2 into R produces which error?

- **Options:**

  A) What error? It works great?
  B) Error: object p not found
  C) Error: object of type closure is not subsettable
  D) Error in "p"^2 : non-numeric argument to binary operator

- **Answer (tutor only):** D
- **Explanation (tutor only):** The quotes make "p" a character string, and you can't do arithmetic (like ^2) on text. R says the argument is "non-numeric".
- **Why the wrong options are wrong (tutor only):**
  A) R cannot square a word, so it does throw an error.
  B) "object not found" happens when you type a name without quotes that doesn't exist (p^2). With quotes, R knows "p" is text, not an object.
  C) "closure is not subsettable" comes from treating a function like data (e.g., mean[1]). Not relevant here.
- **Hint:** What do the quotation marks around p tell R?

### ch01-book-01-v1
- **Kind:** AI-written version of ch01-book-01
- **Concepts:** R basics; Errors & debugging
- **Type:** MC
- **Question:**

Entering "10" + 5 into R produces:

- **Options:**

  A) 15
  B) "105"
  C) Error in "10" + 5 : non-numeric argument to binary operator
  D) Error: object 10 not found

- **Answer (tutor only):** C
- **Explanation (tutor only):** The quotes make "10" a character string, not a number, so R can't add it to 5.
- **Why the wrong options are wrong (tutor only):**
  A) R doesn't convert text to numbers automatically here.
  B) R's + doesn't paste strings together.
  D) Quotes make it a value, not an object name.
- **Hint:** What do quotation marks do in R?

### ch01-book-01-v2
- **Kind:** AI-written version of ch01-book-01
- **Concepts:** R basics; Errors & debugging
- **Type:** MC
- **Question:**

You type sqrt(x) but never created x. What does R say?

- **Options:**

  A) 0
  B) Error: object 'x' not found
  C) Error: non-numeric argument to mathematical function
  D) NA

- **Answer (tutor only):** B
- **Explanation (tutor only):** Without quotes, x is treated as the name of an object. Since nothing called x exists, R can't find it.
- **Why the wrong options are wrong (tutor only):**
  A) and D) R doesn't invent a value for a missing object.
  C) That error appears when x exists but holds text.
- **Hint:** Does an object named x exist yet?

### ch01-book-02
- **Kind:** Course original
- **Concepts:** R basics
- **Type:** MC
- **Question:**

Which logical question provides an unexpected answer?

- **Options:**

  A) (2.0 + 1.0) == 3.0
  B) (0.2 + 0.1) == 0.3
  C) 2^2 > 8
  D) (1/0) == (10 * 1/0)

- **Answer (tutor only):** B
- **Explanation (tutor only):** (0.2 + 0.1) == 0.3 returns FALSE because of floating-point precision: some decimals can't be stored exactly in binary, so 0.2 + 0.1 is very slightly different from 0.3. Use all.equal() or round() instead of == for decimals.
- **Why the wrong options are wrong (tutor only):**
  A) Whole-number arithmetic is exact, so this is TRUE, as expected.
  C) 2^2 is 4, which is not greater than 8, so FALSE, as expected.
  D) 1/0 is Inf in R, and 10 * Inf is also Inf, so this is TRUE. That surprises some people, but it follows from how R handles infinity.
- **Hint:** Try (0.2 + 0.1) - 0.3 in R. Is it exactly zero?

### ch01-book-02-v1
- **Kind:** AI-written version of ch01-book-02
- **Concepts:** R basics
- **Type:** MC
- **Question:**

Which logical comparison gives a surprising FALSE in R (and most programming languages)?

- **Options:**

  A) (1 + 1) == 2
  B) (0.1 * 3) == 0.3
  C) 5 > 3
  D) (4 / 2) == 2

- **Answer (tutor only):** B
- **Explanation (tutor only):** Computers store most decimals in binary only approximately, so 0.1 * 3 is 0.30000000000000004, not exactly 0.3. Use all.equal() or round() to compare decimals.
- **Why the wrong options are wrong (tutor only):**
  A), C) and D) Whole-number arithmetic is exact, so these behave as expected.
- **Hint:** Which comparison involves decimals that can't be stored exactly?

### ch01-book-02-v2
- **Kind:** AI-written version of ch01-book-02
- **Concepts:** R basics
- **Type:** MC
- **Question:**

Why can (0.2 + 0.1) == 0.3 return FALSE in R?

- **Options:**

  A) Decimals are stored with tiny rounding errors in binary
  B) R rounds all numbers to whole numbers
  C) == only works for text
  D) R has a bug that should be reported

- **Answer (tutor only):** A
- **Explanation (tutor only):** Many decimals (like 0.1) have no exact binary representation, so tiny errors creep in. Compare decimals with all.equal() or by rounding.
- **Why the wrong options are wrong (tutor only):**
  B) R keeps decimals.
  C) == compares numbers too.
  D) It's expected behavior in nearly all languages.
- **Hint:** How does a computer store 0.1?

### ch01-book-03
- **Kind:** Course original
- **Concepts:** R basics
- **Type:** MC
- **Question:**

You measured the length and width (in cm) of five wild grape (Vitis riparia) leaves and stored them in two vectors, leaf_length and leaf_width (in the same leaf order). Leaf area = 0.851 x leaf length x leaf width. Which code gives the mean leaf area?

- **Options:**

  A) mean(0.851 * leaf_length * leaf_width)
  B) 0.851 * mean(leaf_length) * mean(leaf_width)
  C) mean(leaf_length) * mean(leaf_width)
  D) sum(0.851 * leaf_length * leaf_width)

- **Answer (tutor only):** A
- **Explanation (tutor only):** R multiplies vectors element by element, so 0.851 * leaf_length * leaf_width gives the area of each leaf. Then mean() averages those five areas. (With the book's data this gives 16.9 cm².)
- **Why the wrong options are wrong (tutor only):**
  B) This multiplies the average length by the average width. The mean of products is not the same as the product of means, so this gives a (slightly) different number.
  C) Same problem as B, and it also forgets the 0.851.
  D) sum() gives the total area of all five leaves, not the average.
- **Hint:** First get one area per leaf, then summarize.

### ch01-book-03-v1
- **Kind:** AI-written version of ch01-book-03
- **Concepts:** R basics
- **Type:** MC
- **Question:**

You measured the length and width (cm) of six bean pods, stored in vectors pod_length and pod_width (same pod order). Pod area ≈ 0.7 × length × width. Which code gives the mean pod area?

- **Options:**

  A) mean(0.7 * pod_length * pod_width)
  B) 0.7 * mean(pod_length) * mean(pod_width)
  C) sum(0.7 * pod_length * pod_width)
  D) mean(pod_length * pod_width)

- **Answer (tutor only):** A
- **Explanation (tutor only):** Multiplying vectors works element by element, giving one area per pod; mean() then averages those six areas.
- **Why the wrong options are wrong (tutor only):**
  B) The mean of products isn't the product of means (unless length and width are unrelated).
  C) That's the total, not the mean.
  D) Leaves out the 0.7 conversion.
- **Hint:** Compute each pod's area first, then average.

### ch01-book-03-v2
- **Kind:** AI-written version of ch01-book-03
- **Concepts:** R basics
- **Type:** MC
- **Question:**

temps_c holds five temperatures in °C. Which code converts them all to °F (F = 1.8 × C + 32) in one step?

- **Options:**

  A) 1.8 * temps_c + 32
  B) for each temps_c: 1.8 * temps_c + 32
  C) mean(1.8 * temps_c + 32)
  D) 1.8 * mean(temps_c) + 32

- **Answer (tutor only):** A
- **Explanation (tutor only):** R's arithmetic is vectorized: the formula is applied to every element, returning five Fahrenheit values.
- **Why the wrong options are wrong (tutor only):**
  B) Not valid R syntax.
  C) and D) Both return one number (the mean), not five conversions.
- **Hint:** R applies arithmetic to each element of a vector automatically.

### ch01-book-04
- **Kind:** Course original
- **Concepts:** R basics; Functions, pipes & packages; Scripts & reproducibility
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch01-book-wrongpraise.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch01-book-wrongpraise.png)
- **Question:**

A script has two lines, in this order:
Line 1: praise()
Line 2: library(praise)
How will running this script make you feel?

- **Options:**

  A) Amazing, I love being praised
  B) Not good, it won't work :(

- **Answer (tutor only):** B
- **Explanation (tutor only):** R runs a script from top to bottom. Line 1 calls praise() before the praise package is loaded on line 2, so R gives 'could not find function "praise"'. Load packages at the top of your script.
- **Why the wrong options are wrong (tutor only):**
  A) praise() would work only if the package were already loaded. Here it is loaded one line too late.
- **Hint:** In what order does R run the lines of a script?

### ch01-book-04-v1
- **Kind:** AI-written version of ch01-book-04
- **Concepts:** R basics; Functions, pipes & packages; Scripts & reproducibility
- **Type:** MC
- **Question:**

A script has two lines, in this order:
Line 1: ggplot(iris, aes(x = Sepal.Length)) + geom_histogram()
Line 2: library(ggplot2)
You restart R and run the script top to bottom. What happens?

- **Options:**

  A) A histogram appears
  B) Error: could not find function "ggplot"
  C) R installs ggplot2 automatically
  D) Nothing happens

- **Answer (tutor only):** B
- **Explanation (tutor only):** R runs lines in order. When line 1 runs, ggplot2 hasn't been loaded yet, so R can't find ggplot(). Load packages at the top.
- **Why the wrong options are wrong (tutor only):**
  A) It would only work if ggplot2 was already loaded from earlier in the session.
  C) R never installs packages automatically.
  D) R reports an error.
- **Hint:** Which line runs first?

### ch01-book-04-v2
- **Kind:** AI-written version of ch01-book-04
- **Concepts:** R basics; Functions, pipes & packages; Scripts & reproducibility
- **Type:** MC
- **Question:**

Where should library() calls go in an R script?

- **Options:**

  A) At the top, before any code that uses the package
  B) At the very end of the script
  C) Right after the first time you use a function from the package
  D) It doesn't matter

- **Answer (tutor only):** A
- **Explanation (tutor only):** A script runs top to bottom, so packages must be loaded before their functions are used. Putting them at the top also shows readers what the script needs.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Code that runs before library() will fail.
  D) Order matters in a script.
- **Hint:** Scripts run in order.

### ch01-book-05
- **Kind:** Course original
- **Concepts:** R basics; Assignment & the environment
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch01-book-badscript.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch01-book-badscript.png)
- **Question:**

A script contains two lines: x <- 3:5 and y <- 1. The Environment pane shows only x (int [1:3] 3 4 5); y is not listed. What happens if you enter x^2 in the console?

- **Options:**

  A) Error: object x not found
  B) 1 4 9
  C) 9 16 25

- **Answer (tutor only):** C
- **Explanation (tutor only):** x exists (it is in the Environment) and holds 3, 4, 5. Squaring each element gives 9, 16, 25.
- **Why the wrong options are wrong (tutor only):**
  A) x is in the Environment, so R can find it.
  B) 1 4 9 would be the squares of 1, 2, 3. But x is 3:5, which is 3, 4, 5.
- **Hint:** What values does 3:5 create?

### ch01-book-05-v1
- **Kind:** AI-written version of ch01-book-05
- **Concepts:** R basics; Assignment & the environment
- **Type:** MC
- **Question:**

Your script contains a <- c(2, 4, 6) and b <- 10, but the Environment pane shows only a (num [1:3] 2 4 6). What happens if you type a / 2 in the console?

- **Options:**

  A) Error: object 'a' not found
  B) 1 2 3
  C) 0.5 1 1.5

- **Answer (tutor only):** B
- **Explanation (tutor only):** a exists in the Environment (that line was run), so R divides each element by 2.
- **Why the wrong options are wrong (tutor only):**
  A) a is listed in the Environment.
  C) That would be dividing by 4; a / 2 halves each value.
- **Hint:** Is a in the Environment?

### ch01-book-05-v2
- **Kind:** AI-written version of ch01-book-05
- **Concepts:** R basics; Assignment & the environment
- **Type:** MC
- **Question:**

A script contains counts <- c(5, 8, 12). You ran that line. What does sum(counts) return?

- **Options:**

  A) 25
  B) Error: object 'counts' not found
  C) 5 8 12
  D) 3

- **Answer (tutor only):** A
- **Explanation (tutor only):** Running the line created counts in the Environment, so sum() adds 5 + 8 + 12.
- **Why the wrong options are wrong (tutor only):**
  B) The line was run, so counts exists.
  C) That would just print the vector.
  D) That's length(counts).
- **Hint:** Was the line that creates counts run?

### ch01-book-06
- **Kind:** Course original
- **Concepts:** R basics; Assignment & the environment
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch01-book-badscript.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch01-book-badscript.png)
- **Question:**

A script contains two lines: x <- 3:5 and y <- 1. The Environment pane shows only x (int [1:3] 3 4 5); y is not listed. What happens if you enter x * y in the console?

- **Options:**

  A) Error: object x not found
  B) Error: object y not found
  C) 1 2 3
  D) 3 4 5

- **Answer (tutor only):** B
- **Explanation (tutor only):** Writing y <- 1 in a script does nothing until you run that line. The Environment shows only x, so y was never created, and R stops with 'object y not found'.
- **Why the wrong options are wrong (tutor only):**
  A) x is in the Environment, so R can find it.
  C) and D) would require y to exist. D (3 4 5) is what you'd get if y were 1, which is the trap: the line exists in the script but was never run.
- **Hint:** Is y listed in the Environment pane?

### ch01-book-06-v1
- **Kind:** AI-written version of ch01-book-06
- **Concepts:** R basics; Assignment & the environment
- **Type:** MC
- **Question:**

Your script contains a <- c(2, 4, 6) and b <- 10, but the Environment pane shows only a. What happens if you type a + b in the console?

- **Options:**

  A) Error: object 'a' not found
  B) Error: object 'b' not found
  C) 12 14 16
  D) 2 4 6

- **Answer (tutor only):** B
- **Explanation (tutor only):** Writing a line in a script doesn't run it. b <- 10 was never run, so b doesn't exist yet.
- **Why the wrong options are wrong (tutor only):**
  A) a exists.
  C) That's what you'd get after running b <- 10.
  D) b isn't treated as 0.
- **Hint:** Which objects are actually in the Environment?

### ch01-book-06-v2
- **Kind:** AI-written version of ch01-book-06
- **Concepts:** R basics; Assignment & the environment
- **Type:** MC
- **Question:**

You wrote total <- 100 in your script but didn't run it. Then you type total / 4 in the console. What happens?

- **Options:**

  A) 25
  B) Error: object 'total' not found
  C) 0
  D) R runs the script line automatically

- **Answer (tutor only):** B
- **Explanation (tutor only):** Code in a script does nothing until it's run. Until then, total doesn't exist.
- **Why the wrong options are wrong (tutor only):**
  A) That's what you'd get after running the line.
  C) Missing objects aren't treated as zero.
  D) R never runs script lines on its own.
- **Hint:** Writing code isn't the same as running it.

### ch01-book-07
- **Kind:** Course original
- **Concepts:** Learning R
- **Type:** MC
- **Question:**

You spend 30 minutes debugging something, and at the end the mistake was so obvious. What is the most accurate interpretation?

- **Options:**

  A) You're bad at R
  B) You wasted time
  C) Good job! You learned something and solved a problem.
  D) R is stupid

- **Answer (tutor only):** C
- **Explanation (tutor only):** Debugging is how everyone learns R. Finding an 'obvious' mistake means you now recognize it, which makes the next one faster.
- **Why the wrong options are wrong (tutor only):**
  A), B) and D) all treat errors as failure. Errors are a normal part of coding, even for experts.

### ch01-book-07-v1
- **Kind:** AI-written version of ch01-book-07
- **Concepts:** Learning R
- **Type:** MC
- **Question:**

A classmate spends 45 minutes on an error that turns out to be a missing comma. What's the most useful way to see it?

- **Options:**

  A) They aren't cut out for coding
  B) Debugging is part of coding, and they now know to check for missing commas
  C) R is badly designed
  D) They should avoid writing code

- **Answer (tutor only):** B
- **Explanation (tutor only):** Everyone hits small, frustrating bugs. Finding them builds skill: next time, they'll spot the comma faster.
- **Why the wrong options are wrong (tutor only):**
  A), C) and D) These framings make learning harder and aren't accurate.
- **Hint:** Does an experienced coder never make typos?

### ch01-book-07-v2
- **Kind:** AI-written version of ch01-book-07
- **Concepts:** Learning R
- **Type:** MC
- **Question:**

After an hour of debugging, you realize you spelled a column name 'Petal.lenght'. What's the best takeaway?

- **Options:**

  A) You should give up on R
  B) Check spelling and capitalization early when you see 'object not found'
  C) Always ask someone else to write your code
  D) Never use long column names

- **Answer (tutor only):** B
- **Explanation (tutor only):** Typos are among the most common causes of errors. Building a habit of checking names first makes debugging faster.
- **Why the wrong options are wrong (tutor only):**
  A) and C) Unhelpful conclusions.
  D) Clear names are good; you just need to check them.
- **Hint:** What error message usually comes from a typo in a name?

### ch01-book-08
- **Kind:** Course original
- **Concepts:** R basics; Scripts & reproducibility
- **Type:** MC
- **Question:**

Script A:
a <- c(1,2,3)
b <- a*2

Script B:
leaf_length <- c(1,2,3)
double_length <- leaf_length * 2

While neither script is perfect, which is better?

- **Options:**

  A) They both work, so they are equally good
  B) It depends on who is reading it
  C) Script A, it's shorter
  D) Script B, it's easier to understand

- **Answer (tutor only):** D
- **Explanation (tutor only):** Both scripts do the same thing, but Script B's names say what the values are. Clear names make code easier to read, check and reuse, including by you in a few weeks.
- **Why the wrong options are wrong (tutor only):**
  A) Working is necessary but not enough. Code also has to be understandable.
  B) Descriptive names help every reader.
  C) Shorter is not better if the reader can't tell what a and b mean.
- **Hint:** Which script could you understand without any explanation?

### ch01-book-08-v1
- **Kind:** AI-written version of ch01-book-08
- **Concepts:** R basics; Scripts & reproducibility
- **Type:** MC
- **Question:**

Script A:
x <- c(12, 15, 9)
y <- x / 60

Script B:
minutes_foraging <- c(12, 15, 9)
hours_foraging <- minutes_foraging / 60

Which is better?

- **Options:**

  A) Script A, it's shorter
  B) Script B, the names say what the numbers are
  C) They both work, so they're equally good
  D) It depends on the computer

- **Answer (tutor only):** B
- **Explanation (tutor only):** Descriptive names make code readable for others and for future you. Shorter isn't better if no one can tell what x and y mean.
- **Why the wrong options are wrong (tutor only):**
  A) Brevity at the cost of clarity isn't a win.
  C) Working code can still be hard to read.
  D) Readability doesn't depend on the computer.
- **Hint:** Which would you understand six months from now?

### ch01-book-08-v2
- **Kind:** AI-written version of ch01-book-08
- **Concepts:** R basics; Scripts & reproducibility
- **Type:** MC
- **Question:**

Which object name is best for the mean beak depth of finches measured in 2024?

- **Options:**

  A) x
  B) mean_beak_depth_2024
  C) thing1
  D) m

- **Answer (tutor only):** B
- **Explanation (tutor only):** Descriptive, consistent names (snake_case) make code self-explaining.
- **Why the wrong options are wrong (tutor only):**
  A), C) and D) Short or vague names force readers to guess.
- **Hint:** Could someone guess what it holds from the name alone?

### ch01-book-09
- **Kind:** Course original
- **Concepts:** Functions, pipes & packages; Scripts & reproducibility
- **Type:** MC
- **Question:**

Consider these lines of code:
a) x <- 4
b) class(x)
c) install.packages("ggplot2")
d) library(ggplot2)
Which two are best to include in your saved R script (assuming you are using functions from ggplot2)?

- **Options:**

  A) a & b
  B) a & c
  C) a & d
  D) b & c
  E) b & d
  F) c & d

- **Answer (tutor only):** C
- **Explanation (tutor only):** a) and d) are needed for the code to work every time: x must be created and ggplot2 must be loaded. class(x) is a check you run while exploring, and install.packages() is a one-time setup step, not part of the analysis.
- **Why the wrong options are wrong (tutor only):**
  Options with b): class(x) only displays the type of x; the analysis doesn't need it.
  Options with c): installing a package every time the script runs is unnecessary and slow. Install once in the console.
  A) Includes b): class(x) only displays the type of x, which the analysis doesn't need.
  B) Includes c): installing a package every time the script runs is unnecessary; install once in the console. And without library(ggplot2), its functions won't load.
  D) Includes c), and leaves out both creating x and loading ggplot2.
  E) Includes b), and leaves out creating x.
  F) Includes c), and leaves out creating x.
- **Hint:** Which lines must run every time for the script to work, and which are one-time or exploratory?

### ch01-book-09-v1
- **Kind:** AI-written version of ch01-book-09
- **Concepts:** Functions, pipes & packages; Scripts & reproducibility
- **Type:** MC
- **Question:**

Consider these lines:
a) install.packages("dplyr")
b) library(dplyr)
c) View(my_data)
d) my_data <- read_csv("data/plants.csv")
Which two belong in a saved, shareable script (assuming you use dplyr functions)?

- **Options:**

  A) a & b
  B) b & d
  C) a & c
  D) c & d

- **Answer (tutor only):** B
- **Explanation (tutor only):** Load packages and read data in the script. Install packages once in the console (not every run), and leave interactive View() calls out.
- **Why the wrong options are wrong (tutor only):**
  A) Includes install.packages(), which reinstalls every run, and leaves out reading the data.
  C) Both are console-only actions.
  D) View() is interactive clutter, and dplyr is never loaded.
- **Hint:** Which lines does the analysis actually need every time it runs?

### ch01-book-09-v2
- **Kind:** AI-written version of ch01-book-09
- **Concepts:** Functions, pipes & packages; Scripts & reproducibility
- **Type:** MC
- **Question:**

Why shouldn't install.packages() usually be in your saved script?

- **Options:**

  A) You only need to install a package once; installing on every run is slow and unnecessary
  B) install.packages() doesn't work in scripts
  C) It deletes your data
  D) It loads the package twice

- **Answer (tutor only):** A
- **Explanation (tutor only):** Install once from the console; then use library() in the script to load it each session.
- **Why the wrong options are wrong (tutor only):**
  B) It works, it's just unnecessary.
  C) It doesn't touch your data.
  D) Installing isn't loading; library() loads.
- **Hint:** What's the difference between installing and loading a package?

### ch01-book-10
- **Kind:** Course original
- **Concepts:** Learning R
- **Type:** MC
- **Question:**

Which of the following is the best long-term strategy for improving in R?

- **Options:**

  A) Memorize as many functions as possible
  B) Avoid errors
  C) Write code regularly and reflect on mistakes
  D) Ask AI to solve all your R problems and copy and paste its answers

- **Answer (tutor only):** C
- **Explanation (tutor only):** Skill comes from practice and learning from errors. Look-up is easy; understanding comes from doing.
- **Why the wrong options are wrong (tutor only):**
  A) You can always look functions up. Knowing how to use them comes from practice.
  B) Errors are how you learn. Avoiding them means avoiding practice.
  D) Copying answers without understanding them doesn't build skill, and AI answers can be wrong.

### ch01-book-10-v1
- **Kind:** AI-written version of ch01-book-10
- **Concepts:** Learning R
- **Type:** MC
- **Question:**

Which habit will help you most in learning R over the semester?

- **Options:**

  A) Copying code from AI without reading it
  B) Practicing a little often and reading error messages carefully
  C) Memorizing every function's arguments
  D) Avoiding code that might give errors

- **Answer (tutor only):** B
- **Explanation (tutor only):** Frequent practice and learning from errors builds lasting skill.
- **Why the wrong options are wrong (tutor only):**
  A) You won't learn what the code does.
  C) You can look arguments up; understanding matters more.
  D) Errors are how you learn.
- **Hint:** What builds understanding rather than just output?

### ch01-book-10-v2
- **Kind:** AI-written version of ch01-book-10
- **Concepts:** Learning R
- **Type:** MC
- **Question:**

You're stuck on an R error. Which approach is most likely to help you learn?

- **Options:**

  A) Read the error, form a guess about the cause, test it, and ask for help if stuck
  B) Restart your computer until it works
  C) Delete the code and give up
  D) Paste the whole assignment into AI and submit the result

- **Answer (tutor only):** A
- **Explanation (tutor only):** Reading errors, forming hypotheses and testing them is how debugging skill develops. Asking for help after trying is great.
- **Why the wrong options are wrong (tutor only):**
  B) Rarely fixes a code error.
  C) You learn nothing.
  D) You skip the learning.
- **Hint:** Which option involves you thinking about the problem?

### ch01-quiz-01
- **Kind:** Course original
- **Concepts:** R basics; Assignment & the environment
- **Type:** MC
- **Question:**

Two students each typed x <- 5 in an R script.
Student A ran the line: it appears in the Console (> x<-5) and the Environment shows x = 5.
Student B did not run the line: the Console is empty and the Environment says 'Environment is empty'.
In which case does x equal 5?

- **Options:**

  A) A only
  B) B only
  C) Both
  D) Neither

- **Answer (tutor only):** A
- **Explanation (tutor only):** Typing code in a script doesn't do anything until you run it. Only Student A ran x <- 5, so only A has x in the Environment.
- **Why the wrong options are wrong (tutor only):**
  B) and C): Student B wrote the code but never ran it, so x doesn't exist for B.
  D) Student A did run the line, and the Environment confirms x = 5.
- **Hint:** Check the Environment pane. Does x exist there?

### ch01-quiz-01-v1
- **Kind:** AI-written version of ch01-quiz-01
- **Concepts:** R basics; Assignment & the environment
- **Type:** MC
- **Question:**

Two students each wrote y <- 12 in a script.
Student A ran the line: the Console shows > y <- 12 and the Environment lists y = 12.
Student B only typed it; the Environment is empty.
If each now types y * 2 in the console, who gets 24?

- **Options:**

  A) A only
  B) B only
  C) Both
  D) Neither

- **Answer (tutor only):** A
- **Explanation (tutor only):** Only running a line creates the object. Student B's y doesn't exist yet, so they'll get 'object not found'.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Typing without running does nothing.
  D) Student A ran the line.
- **Hint:** Whose Environment contains y?

### ch01-quiz-01-v2
- **Kind:** AI-written version of ch01-quiz-01
- **Concepts:** R basics; Assignment & the environment
- **Type:** MC
- **Question:**

You ran z <- 3 an hour ago. Since then you edited the script line to z <- 7 but didn't rerun it. What is z right now?

- **Options:**

  A) 3
  B) 7
  C) 10
  D) z doesn't exist

- **Answer (tutor only):** A
- **Explanation (tutor only):** The Environment holds whatever was last run. Editing a script line doesn't change the object until you run it again.
- **Why the wrong options are wrong (tutor only):**
  B) The edit hasn't been run.
  C) Assignment replaces, it doesn't add.
  D) z was created when you ran the first version.
- **Hint:** What was the last line that actually ran?

### ch01-quiz-02
- **Kind:** Course original
- **Concepts:** R basics; Assignment & the environment; Functions, pipes & packages
- **Type:** short answer
- **Question:**

When you open up R, the iris data set has column names Sepal.Length, Sepal.Width, Petal.Length, Petal.Width, and Species. I run this code:
library(janitor)
clean_names(iris)
The console prints the data with names sepal_length, sepal_width, and so on. If you now type View(iris), what is the first column name?

- **Answer (tutor only):** Sepal.Length
- **Explanation (tutor only):** clean_names(iris) returns a cleaned copy and prints it, but doesn't change iris itself, because the result wasn't saved. To keep it, you'd write iris <- clean_names(iris). So iris still has its original names.
- **Why the wrong options are wrong (tutor only):**
  Common wrong answer: sepal_length. That's what was printed, but printing a result is not the same as saving it.
- **Hint:** Did the code save the result anywhere with <- ?

### ch01-quiz-02-v1
- **Kind:** AI-written version of ch01-quiz-02
- **Concepts:** R basics; Assignment & the environment; Functions, pipes & packages
- **Type:** MC
- **Question:**

The iris data has a column called Species. You run:
iris |> rename(species = Species)
The console shows the renamed column. You then type View(iris). What is the column called?

- **Options:**

  A) Species
  B) species
  C) Both columns appear
  D) The column is gone

- **Answer (tutor only):** A
- **Explanation (tutor only):** rename() returned a modified copy and printed it, but nothing saved it: iris was never reassigned. To keep it: iris <- iris |> rename(species = Species).
- **Why the wrong options are wrong (tutor only):**
  B) That's only true after reassigning with <-.
  C) rename() renames; it doesn't duplicate.
  D) Nothing was deleted.
- **Hint:** Was the result saved back into iris?

### ch01-quiz-02-v2
- **Kind:** AI-written version of ch01-quiz-02
- **Concepts:** R basics; Assignment & the environment
- **Type:** MC
- **Question:**

You run sort(weights) and the console shows the values in increasing order. Then you type weights. What order are the values in?

- **Options:**

  A) Increasing order
  B) Their original order
  C) Decreasing order
  D) Error: object not found

- **Answer (tutor only):** B
- **Explanation (tutor only):** sort() returns a sorted copy without changing weights. To keep the sorted version: weights <- sort(weights).
- **Why the wrong options are wrong (tutor only):**
  A) Only if you reassigned.
  C) sort() defaults to increasing, and it didn't change weights anyway.
  D) weights still exists.
- **Hint:** Did anything assign the sorted result?

### ch01-quiz-03
- **Kind:** Course original
- **Concepts:** R basics; Functions, pipes & packages; Errors & debugging
- **Type:** MC
- **Question:**

You type glimpse(iris) and get:
Error in glimpse(iris) : could not find function "glimpse"
What went wrong?

- **Options:**

  A) glimpse is spelled wrong
  B) glimpse should be capitalized
  C) the dplyr package is not loaded
  D) iris does not exist

- **Answer (tutor only):** C
- **Explanation (tutor only):** glimpse() comes from the dplyr package. 'Could not find function' usually means the package that provides the function hasn't been loaded with library(dplyr).
- **Why the wrong options are wrong (tutor only):**
  A) glimpse is spelled correctly.
  B) R is case-sensitive, and the function is lowercase glimpse().
  D) iris is built into R. Also, if iris were missing, the error would say 'object not found', not 'could not find function'.
- **Hint:** Does the error say R can't find an object or a function?

### ch01-quiz-03-v1
- **Kind:** AI-written version of ch01-quiz-03
- **Concepts:** R basics; Functions, pipes & packages; Errors & debugging
- **Type:** MC
- **Question:**

You type ggplot(iris, aes(x = Sepal.Length)) + geom_histogram() and get:
Error in ggplot(iris, aes(x = Sepal.Length)) : could not find function "ggplot"
What went wrong?

- **Options:**

  A) ggplot2 isn't loaded
  B) iris doesn't exist
  C) Sepal.Length is misspelled
  D) geom_histogram() needs more arguments

- **Answer (tutor only):** A
- **Explanation (tutor only):** 'could not find function' means R doesn't know the function: usually the package isn't loaded (library(ggplot2)) or the name is misspelled.
- **Why the wrong options are wrong (tutor only):**
  B) A missing dataset gives 'object not found'.
  C) A wrong column name gives a different error.
  D) geom_histogram() works with defaults.
- **Hint:** What does 'could not find function' usually mean?

### ch01-quiz-03-v2
- **Kind:** AI-written version of ch01-quiz-03
- **Concepts:** R basics; Errors & debugging
- **Type:** MC
- **Question:**

You type Mean(c(1, 2, 3)) and get: could not find function "Mean". What's the fix?

- **Options:**

  A) Load a package for Mean
  B) Use lowercase: mean(c(1, 2, 3))
  C) Put quotes around the numbers
  D) Reinstall R

- **Answer (tutor only):** B
- **Explanation (tutor only):** R is case-sensitive: the base function is mean(), not Mean(). 'could not find function' can mean a typo, including capitalization.
- **Why the wrong options are wrong (tutor only):**
  A) mean() is built in; no package is needed.
  C) Quotes would make the numbers text.
  D) Unnecessary.
- **Hint:** R cares about capital letters.

## Chapter 2: ggplot

### ch02-chimein-02
- **Kind:** Course original
- **Concepts:** Plot design principles
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch02-chimein-02.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch02-chimein-02.png)
- **Question:**

You want to compare sepal width among three iris species using 'small multiples' (one histogram per species). Layout A stacks the three panels vertically so they share one x-axis. Layout B puts them side by side; each panel uses the same x-axis scale, but the panels sit next to each other rather than lined up above one another. Which layout makes it easier to compare where each species' values fall, and why?

- **Options:**

  A) Layout A, because stacking the panels on a shared x-axis lines up the values, so you can compare positions directly
  B) Layout B, because side-by-side panels are always easier to read
  C) There is no difference

- **Answer (tutor only):** A
- **Explanation (tutor only):** To compare where values fall (the centers and spreads), the x-axes should line up. Stacking panels vertically does that. Side-by-side panels line up the y-axes instead, which is better for comparing counts.
- **Why the wrong options are wrong (tutor only):**
  B) Side-by-side is not always better. It lines up the y-axis (counts), not the values we want to compare.
  C) The layout changes which comparison is easy, so it does matter.
- **Hint:** Which axis do you need to line up to compare where the values fall?

### ch02-chimein-02-v1
- **Kind:** AI-written version of ch02-chimein-02
- **Concepts:** Plot design principles
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch02-var-penguin-smallmult.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch02-var-penguin-smallmult.png)
- **Question:**

Both layouts show flipper length for three penguin species as small multiples. In A the panels are stacked and share one x-axis; in B they sit side by side. Which layout makes it easier to compare where each species' values fall?

- **Options:**

  A) A, because stacking on a shared x-axis lines up the values, so positions can be compared directly
  B) B, because side-by-side panels are always easier to read
  C) There is no difference

- **Answer (tutor only):** A
- **Explanation (tutor only):** When panels are stacked on a common x-axis, the same flipper length sits at the same horizontal position in every panel, so you can see at a glance that Gentoo flippers are longer.
- **Why the wrong options are wrong (tutor only):**
  B) Side-by-side panels put the x-axes next to each other, so the eye has to jump between different axes to compare positions.
  C) The layout changes which comparison is easy.
- **Hint:** Which layout puts 200 mm at the same spot for every species?

### ch02-chimein-02-v2
- **Kind:** AI-written version of ch02-chimein-02
- **Concepts:** Plot design principles
- **Type:** MC
- **Question:**

You want readers to compare body mass (on the y-axis) across four treatment groups shown as small multiples. Which arrangement makes that comparison easiest?

- **Options:**

  A) Panels side by side in one row, sharing the same y-axis
  B) Panels stacked in one column, each with its own y-axis
  C) Panels in a 2 × 2 grid, each with its own y-axis
  D) Arrangement doesn't matter

- **Answer (tutor only):** A
- **Explanation (tutor only):** To compare values on the y-axis, line the panels up horizontally with a shared y-axis, so the same body mass sits at the same height in every panel.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Separate y-axes break the comparison.
  D) Arrangement determines which comparisons are easy.
- **Hint:** Compare along x → stack vertically. Compare along y → place side by side.

### ch02-chimein-03
- **Kind:** Course original
- **Concepts:** Plot design principles
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch02-chimein-03.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch02-chimein-03.png)
- **Question:**

Two density plots show sepal width for three iris species. In plot A, the curves are filled with solid colors, so some curves hide behind others. In plot B, the same curves are semi-transparent, so all three remain visible where they overlap. Which plot is superior?

- **Options:**

  A) A, because the colors are bolder
  B) B, because you can see the distribution of values for all species
  C) It depends...

- **Answer (tutor only):** B
- **Explanation (tutor only):** In plot A, the curves drawn last cover the ones underneath, hiding parts of the data. Transparency (alpha) in plot B lets you see every distribution, including where they overlap.
- **Why the wrong options are wrong (tutor only):**
  A) Bold colors don't help if they hide data.
  C) Here the purpose (comparing all three species) is clear, and B serves it better.
- **Hint:** In plot A, can you see the full shape of every species' curve?

### ch02-chimein-03-v1
- **Kind:** AI-written version of ch02-chimein-03
- **Concepts:** Plot design principles
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch02-var-penguin-density.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch02-var-penguin-density.png)
- **Question:**

Two density plots show bill length for three penguin species. In A the curves are solid; in B they're semi-transparent. Which plot is better?

- **Options:**

  A) A, because solid colors stand out more
  B) B, because you can see every species' distribution, even where they overlap
  C) They're equally good

- **Answer (tutor only):** B
- **Explanation (tutor only):** With solid fills, curves drawn later cover earlier ones, hiding parts of the distributions (look at how Chinstrap and Gentoo cover each other in A). Transparency keeps all three visible.
- **Why the wrong options are wrong (tutor only):**
  A) Bold colors don't help if they hide data.
  C) A hides information that B shows.
- **Hint:** In plot A, can you see the whole Chinstrap curve?

### ch02-chimein-03-v2
- **Kind:** AI-written version of ch02-chimein-03
- **Concepts:** Plot design principles
- **Type:** MC
- **Question:**

You make overlapping density plots of leaf size for four plant populations, and the curves hide one another. What's the best fix?

- **Options:**

  A) Make the fills semi-transparent (e.g., alpha = 0.4), or facet by population
  B) Use brighter colors
  C) Remove the legend
  D) Make the plot bigger

- **Answer (tutor only):** A
- **Explanation (tutor only):** Transparency lets overlapping curves show through; faceting gives each population its own panel. Both keep every distribution visible.
- **Why the wrong options are wrong (tutor only):**
  B) Brighter opaque colors still hide each other.
  C) Removing the legend makes it harder to read.
  D) Size doesn't fix overlap.
- **Hint:** What would let you see through the front curve?

### ch02-chimein-04
- **Kind:** Course original
- **Concepts:** Plot design principles
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch02-chimein-04.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch02-chimein-04.png)
- **Question:**

Two sets of faceted histograms show sepal width for three iris species. In plot A, all three panels share the same x-axis (2 to 4.5). In plot B, each panel has its own x-axis range (setosa about 2.2 to 4.5, versicolor 2.0 to 3.5, virginica about 2.2 to 3.8). What feature of plot B makes it dangerously misleading?

- **Options:**

  A) The width of bins varies by panel
  B) The y-axis (count) is rescaled in each panel
  C) Because the meaning of the x-axis differs across panels, we can't visually compare

- **Answer (tutor only):** C
- **Explanation (tutor only):** A reader assumes the same spot on the x-axis means the same value in every panel. In plot B, it doesn't, so species look more similar than they are. Facets meant for comparison should share axes.
- **Why the wrong options are wrong (tutor only):**
  A) Bin widths do differ, as a side effect of the different x ranges, but the main danger is that the axes themselves differ.
  B) All three panels in plot B share the same y-axis (0 to 15); it is the x-axes that change from panel to panel.
- **Hint:** Look at the x-axis labels in each panel of plot B. Do they match?

### ch02-chimein-04-v1
- **Kind:** AI-written version of ch02-chimein-04
- **Concepts:** Plot design principles
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch02-var-penguin-facets.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch02-var-penguin-facets.png)
- **Question:**

Two sets of faceted histograms show body mass for three penguin species. In A all panels share the x-axis (2700–6300 g). In B each panel has its own x-axis range. What makes plot B misleading?

- **Options:**

  A) The bins are different widths
  B) The y-axis counts differ
  C) The same horizontal position means a different body mass in each panel, so the eye compares the wrong things

- **Answer (tutor only):** C
- **Explanation (tutor only):** In B, Gentoo's panel starts near 4000 g while Adelie's starts near 2900 g, so the three species look similar in size. Plot A, with a shared axis, shows Gentoo are clearly heavier.
- **Why the wrong options are wrong (tutor only):**
  A) Bin widths differ a little, but that's minor.
  B) Different y-ranges are less of a problem here; the x-axis is what misleads.
- **Hint:** In plot B, compare the left edges of the three panels.

### ch02-chimein-04-v2
- **Kind:** AI-written version of ch02-chimein-04
- **Concepts:** Plot design principles
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [fix-truncated-bars.png](https://yanivjb.github.io/biostats-book/study_guide/images/fix-truncated-bars.png)
- **Question:**

This bar chart compares mean nest temperature in two habitats. What's the problem with it?

- **Options:**

  A) The axis choice exaggerates a small difference, so readers think it's huge
  B) Temperatures can't be shown in bar charts
  C) The colors are misleading
  D) Nothing; truncated axes are always fine

- **Answer (tutor only):** A
- **Explanation (tutor only):** Look at the y-axis: it starts at 30 °C, so the meadow bar looks about three times as tall as the forest bar even though the means differ by only 0.5 °C. Bar length should be proportional to the value. Use points (where a non-zero axis is fine) or start bars at zero.
- **Why the wrong options are wrong (tutor only):**
  B) Bar charts can show temperatures, honestly.
  C) Color isn't the issue.
  D) Truncation is especially misleading for bars.
- **Hint:** Check where the y-axis starts. Does bar height still match the size of the values?

### ch02-hw-01
- **Kind:** Course original
- **Concepts:** Plot design principles; Visualizing associations
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch02-hw-01.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch02-hw-01.png)
- **Question:**

This scatterplot shows petal width (y-axis) against petal length (x-axis) for the 150 flowers in the iris data, with a straight trendline added. The points run from the lower left (petal length about 1 to 2, width about 0.1 to 0.6) up to the upper right (length about 5 to 7, width about 1.5 to 2.5), and the trendline slopes upward. What do you see?

- **Options:**

  A) Petal width tends to increase with petal length
  B) Petal width tends to decrease with petal length
  C) Petal width shows no clear relationship with petal length

- **Answer (tutor only):** A
- **Explanation (tutor only):** The points and the trendline both rise from lower left to upper right: flowers with longer petals tend to have wider petals, a strong positive association. Also worth noticing: the points form a separate cluster at the lower left (these turn out to be one species, setosa), a reminder that a single trendline can hide group structure.
- **Why the wrong options are wrong (tutor only):**
  B) A decrease would show points falling from upper left to lower right.
  C) The points follow the trendline closely, so the relationship is clear.
- **Hint:** Follow the points from left to right. Do they go up or down?

### ch02-hw-01-v1
- **Kind:** AI-written version of ch02-hw-01
- **Concepts:** Plot design principles; Visualizing associations
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch02-var-penguin-flipper-mass.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch02-var-penguin-flipper-mass.png)
- **Question:**

The scatterplot shows body mass against flipper length for 342 penguins, with a straight trendline. What do you see?

- **Options:**

  A) Body mass tends to increase with flipper length
  B) Body mass tends to decrease with flipper length
  C) There is no clear relationship

- **Answer (tutor only):** A
- **Explanation (tutor only):** Points rise from lower left to upper right and the trendline slopes up: penguins with longer flippers tend to be heavier (r ≈ 0.87).
- **Why the wrong options are wrong (tutor only):**
  B) The trend goes up, not down.
  C) The pattern is strong and clear.
- **Hint:** Which way does the line slope?

### ch02-hw-01-v2
- **Kind:** AI-written version of ch02-hw-01
- **Concepts:** Plot design principles; Visualizing associations
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch02-var-penguin-depth-mass.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch02-var-penguin-depth-mass.png)
- **Question:**

The scatterplot shows body mass against bill depth for 342 penguins (all species together), with a straight trendline. What do you see overall?

- **Options:**

  A) Body mass tends to increase with bill depth
  B) Body mass tends to decrease with bill depth
  C) There is no clear relationship

- **Answer (tutor only):** B
- **Explanation (tutor only):** Overall, the trendline slopes down (r ≈ −0.47): heavier penguins tend to have shallower bills. (Coloring by species would show why: heavy Gentoo have shallow bills.)
- **Why the wrong options are wrong (tutor only):**
  A) The line slopes down.
  C) There's a clear negative trend.
- **Hint:** Which way does the line slope?

### ch02-quiz-01
- **Kind:** Course original
- **Concepts:** Plot design principles; Aesthetics & ggplot layers
- **Type:** short answer
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch02-quiz-iris-aesthetics.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch02-quiz-iris-aesthetics.png)
- **Question:**

A plot of iris data maps four variables onto aesthetics: x position, y position, color, and point size. Which aesthetic mappings make it easiest for a reader to compare values, and which make it hardest? Explain.

- **Answer (tutor only):** Easiest: x and y position. Hardest: size, and color when it shows a continuous variable (color is fine for a few categories, like species).
- **Explanation (tutor only):** People judge positions along a common axis very accurately, but are poor at judging differences in area or shade. Put the comparisons that matter most on the x and y axes.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: saying color is easiest because it stands out. Color is great for telling groups apart, but poor for reading amounts.
- **Hint:** Try reading an exact value from a point's size. How about from its position on the y-axis?

### ch02-quiz-01-v1
- **Kind:** AI-written version of ch02-quiz-01
- **Concepts:** Plot design principles; Aesthetics & ggplot layers
- **Type:** MC
- **Question:**

Which aesthetic makes it easiest for readers to compare exact values of a continuous variable?

- **Options:**

  A) Position along an axis (x or y)
  B) Point size
  C) Color shade
  D) Transparency

- **Answer (tutor only):** A
- **Explanation (tutor only):** People judge positions along a common scale most accurately. Size, shade and transparency are much harder to read precisely.
- **Why the wrong options are wrong (tutor only):**
  B) Area is hard to judge (twice the size doesn't look twice as big).
  C) Shades are hard to decode precisely.
  D) Transparency is very hard to read as a value.
- **Hint:** Which is easiest to read off a ruler?

### ch02-quiz-01-v2
- **Kind:** AI-written version of ch02-quiz-01
- **Concepts:** Plot design principles; Aesthetics & ggplot layers
- **Type:** MC
- **Question:**

You need to show five variables in one plot. The most important comparison is between mass and bill length. Where should those two go?

- **Options:**

  A) On the x and y axes
  B) In color and point size
  C) In facets
  D) It doesn't matter

- **Answer (tutor only):** A
- **Explanation (tutor only):** Put the most important comparison on position (x and y), the aesthetics people read most accurately, and use color, size or facets for secondary variables.
- **Why the wrong options are wrong (tutor only):**
  B) Size and color are harder to compare precisely.
  C) Facets are great for groups, not for a continuous comparison.
  D) Mapping choices determine what's easy to see.
- **Hint:** Which aesthetics do people read most accurately?

### ch02-quiz-02
- **Kind:** Course original
- **Concepts:** Plot design principles; Aesthetics & ggplot layers
- **Type:** MC
- **Question:**

Which code will best reveal the raw data?
a) ggplot(iris, aes(x = Species, y = Petal.Length)) + geom_boxplot()
b) ggplot(iris, aes(x = Species, y = Petal.Length)) + geom_boxplot() + geom_jitter(width = .2, alpha = .4)
c) ggplot(iris, aes(x = Species, y = Petal.Length)) + geom_jitter(width = .2, alpha = .4) + geom_boxplot()

- **Options:**

  A) a
  B) b
  C) c

- **Answer (tutor only):** B
- **Explanation (tutor only):** A boxplot alone summarizes the data and hides the individual points. Adding jittered points shows them. ggplot draws layers in order, so in b) the points sit on top of the boxplot, while in c) the boxplot is drawn last and covers points inside the box.
- **Why the wrong options are wrong (tutor only):**
  A) A boxplot shows a summary (median, quartiles), not the individual data points.
  C) This includes the points, but the boxplot is drawn on top and hides the ones inside the box.
- **Hint:** ggplot draws layers in the order you add them. Which layer ends up on top?

### ch02-quiz-02-v1
- **Kind:** AI-written version of ch02-quiz-02
- **Concepts:** Plot design principles; Aesthetics & ggplot layers
- **Type:** MC
- **Question:**

Which code best shows both a summary and every individual penguin?
a) ggplot(penguins, aes(x = species, y = body_mass)) + geom_jitter(width = .2, alpha = .4) + geom_boxplot()
b) ggplot(penguins, aes(x = species, y = body_mass)) + geom_boxplot()
c) ggplot(penguins, aes(x = species, y = body_mass)) + geom_boxplot() + geom_jitter(width = .2, alpha = .4)

- **Options:**

  A) a
  B) b
  C) c

- **Answer (tutor only):** C
- **Explanation (tutor only):** Layers are drawn in order. In c the points are drawn last, on top of the boxes, so you see the summary and every penguin.
- **Why the wrong options are wrong (tutor only):**
  A) The boxes are drawn over the points and hide many of them.
  B) No raw data at all.
- **Hint:** Later layers are drawn on top.

### ch02-quiz-02-v2
- **Kind:** AI-written version of ch02-quiz-02
- **Concepts:** Plot design principles; Aesthetics & ggplot layers
- **Type:** MC
- **Question:**

In ggplot, if you add geom_boxplot() and then geom_point(), which appears on top?

- **Options:**

  A) The points, because later layers are drawn on top
  B) The boxplot, because it's bigger
  C) Whichever has more data
  D) They're blended together

- **Answer (tutor only):** A
- **Explanation (tutor only):** ggplot draws layers in the order you add them, so the last layer sits on top.
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) Order, not size or data, determines what's on top.
- **Hint:** Think of stacking transparencies in order.

### ch02-quiz-03
- **Kind:** Course original
- **Concepts:** Plot design principles
- **Type:** short answer
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [fix-iris-geomcol.png](https://yanivjb.github.io/biostats-book/study_guide/images/fix-iris-geomcol.png)
- **Question:**

I plotted sepal width by species with this code and got the plot below:
ggplot(iris, aes(x = Species, y = Sepal.Width)) + geom_col() + geom_jitter(width = .2, alpha = .4)
As the black points (individual flowers) near zero show, iris sepals are only a few centimeters wide. Explain what went wrong. Bonus: how would you fix it?

- **Answer (tutor only):** geom_col() makes each bar's height the SUM of all the y values in that group (about 50 flowers per species x ~3 cm), not the mean. So the bars show totals that have no useful meaning here, and the raw points get squashed at the bottom. Fix: show the mean instead (e.g., stat_summary(fun = mean, geom = 'bar')), or use a boxplot with jittered points.
- **Explanation (tutor only):** Bar heights should show a meaningful summary. Bars of summed widths make the groups look like they differ in something they don't, and hide the real data.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: assuming bars always show the mean. In ggplot, geom_col() adds up the values.
- **Hint:** If each species has about 50 flowers with sepals about 3 cm wide, what do you get if you add them all up?

### ch02-quiz-03-v1
- **Kind:** AI-written version of ch02-quiz-03
- **Concepts:** Plot design principles
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [fix-penguin-geomcol.png](https://yanivjb.github.io/biostats-book/study_guide/images/fix-penguin-geomcol.png)
- **Question:**

I plotted bill length (mm) by species with ggplot(penguins, aes(x = species, y = bill_length)) + geom_col() and got the plot below. No penguin has a bill longer than 60 mm. What went wrong?

- **Options:**

  A) geom_col() stacks (sums) all the values in each group, so the bar shows a total, not a typical bill
  B) The data have a typo
  C) The y-axis is in the wrong units
  D) geom_col() shows the maximum

- **Answer (tutor only):** A
- **Explanation (tutor only):** geom_col() adds up the y values within each group. With about 150 Adelie penguins of ~39 mm each, the bar reaches ~5,900. Show means (stat_summary) or the raw data (boxplot + jitter) instead.
- **Why the wrong options are wrong (tutor only):**
  B) The data are fine; the geom is summing them.
  C) The units are mm; the issue is summing.
  D) geom_col() shows the sum, not the maximum.
- **Hint:** About how many penguins × about how long a bill?

### ch02-quiz-03-v2
- **Kind:** AI-written version of ch02-quiz-03
- **Concepts:** Plot design principles
- **Type:** MC
- **Question:**

Which plot best shows how leaf length differs among three tree species?

- **Options:**

  A) A bar of the total leaf length per species
  B) Jittered points for every leaf plus a boxplot or mean for each species
  C) A pie chart of total leaf length by species
  D) A single number: the mean leaf length across all species

- **Answer (tutor only):** B
- **Explanation (tutor only):** Showing every leaf plus a summary reveals both typical values and variation. Totals depend on how many leaves were measured, not on how long they are.
- **Why the wrong options are wrong (tutor only):**
  A) and C) Totals mix up sample size with leaf length.
  D) Ignores the species comparison.
- **Hint:** What would change the 'total' even if leaves were the same length?

### ch02-quiz-04
- **Kind:** Course original
- **Concepts:** Aesthetics & ggplot layers
- **Type:** short answer
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch02-quiz-iris-aesthetics.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch02-quiz-iris-aesthetics.png)
- **Question:**

Plot setup (iris data, cleaned names): three panels, one per species (setosa, versicolor, virginica). Each point is a flower. The x-axis is sepal_length (about 4.3 to 7.9) and the y-axis is sepal_width (about 2 to 4.4). Point color shows petal_length (dark purple = short, about 1; yellow = long, about 7), and point size shows petal_width (small = narrow, large = wide). Each panel has a straight trendline from geom_smooth(method = "lm"). Setosa points sit to the upper left (short, wide sepals), are small and dark purple, and have a steep trendline. Versicolor points are in the middle, medium-sized and teal. Virginica points sit furthest right, are the largest and green to yellow, with the shallowest trendline.

The plot uses four aesthetics. Map each variable onto its aesthetic: aes(x = ___, y = ___, color = ___, size = ___)

- **Answer (tutor only):** aes(x = sepal_length, y = sepal_width, color = petal_length, size = petal_width)
- **Explanation (tutor only):** Read each mapping from the plot: the axis titles give x and y, and the two legends give color (petal_length) and size (petal_width). Species is not an aesthetic here; it splits the plot into panels (facets).
- **Why the wrong options are wrong (tutor only):**
  Common mistake: putting species as color. Species defines the panels, not the colors; color shows petal length.
- **Hint:** Look at the axis titles and the two legends.

### ch02-quiz-04-v1
- **Kind:** AI-written version of ch02-quiz-04
- **Concepts:** Aesthetics & ggplot layers
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch02-var-penguin-aes.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch02-var-penguin-aes.png)
- **Question:**

Penguins are shown in three panels, one per species. The x-axis is bill length, the y-axis is bill depth, point color shows flipper length, and point size shows body mass. Match each aesthetic in aes() to its variable:

1. x
2. y
3. color
4. size

- **Options:**

  A) bill_depth
  B) body_mass
  C) bill_length
  D) flipper_length

- **Answer (tutor only):** 1-C, 2-A, 3-D, 4-B
- **Explanation (tutor only):** aes(x = bill_length, y = bill_depth, color = flipper_length, size = body_mass). Each aesthetic maps one variable onto one visual property.
- **Why the wrong options are wrong (tutor only):**
  Swapping x and y flips the plot; swapping color and size changes what the reader decodes from each.
- **Hint:** Read the axis labels first, then the legends.

### ch02-quiz-04-v2
- **Kind:** AI-written version of ch02-quiz-04
- **Concepts:** Aesthetics & ggplot layers
- **Type:** MC
- **Question:**

Which code makes a scatterplot of flipper length (x) against body mass (y), with points colored by species?

- **Options:**

  A) ggplot(penguins, aes(x = flipper_length, y = body_mass, color = species)) + geom_point()
  B) ggplot(penguins, aes(x = body_mass, y = flipper_length, color = species)) + geom_point()
  C) ggplot(penguins, aes(x = flipper_length, y = body_mass)) + geom_point(color = species)
  D) ggplot(penguins, aes(x = flipper_length, y = body_mass, fill = species)) + geom_line()

- **Answer (tutor only):** A
- **Explanation (tutor only):** Variables that should change the look of the plot go inside aes(). Here x, y and color are all mapped to variables.
- **Why the wrong options are wrong (tutor only):**
  B) x and y are swapped.
  C) color = species outside aes() looks for an object named species, not the column.
  D) geom_line() connects points, and fill doesn't color points.
- **Hint:** Mappings to variables go inside aes().

### ch02-quiz-05
- **Kind:** Course original
- **Concepts:** Aesthetics & ggplot layers; Visualizing associations
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch02-quiz-iris-aesthetics.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch02-quiz-iris-aesthetics.png)
- **Question:**

Plot setup (iris data, cleaned names): three panels, one per species (setosa, versicolor, virginica). Each point is a flower. The x-axis is sepal_length (about 4.3 to 7.9) and the y-axis is sepal_width (about 2 to 4.4). Point color shows petal_length (dark purple = short, about 1; yellow = long, about 7), and point size shows petal_width (small = narrow, large = wide). Each panel has a straight trendline from geom_smooth(method = "lm"). Setosa points sit to the upper left (short, wide sepals), are small and dark purple, and have a steep trendline. Versicolor points are in the middle, medium-sized and teal. Virginica points sit furthest right, are the largest and green to yellow, with the shallowest trendline.

Visually guess: which species shows the steepest increase in sepal width with sepal length?

- **Options:**

  A) setosa
  B) versicolor
  C) virginica

- **Answer (tutor only):** A
- **Explanation (tutor only):** Setosa's trendline rises the most for each unit of sepal length (roughly 0.8 cm of width per cm of length, versus about 0.3 for versicolor and 0.2 for virginica).
- **Why the wrong options are wrong (tutor only):**
  B) Versicolor's line rises, but more gently than setosa's.
  C) Virginica has the shallowest line of the three.
- **Hint:** Compare how much each trendline rises over the same distance along the x-axis.

### ch02-quiz-05-v1
- **Kind:** AI-written version of ch02-quiz-05
- **Concepts:** Aesthetics & ggplot layers; Visualizing associations
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch02-var-seedling-slopes.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch02-var-seedling-slopes.png)
- **Question:**

Each panel shows seedling height over time at one site, with a straight trendline. Which site shows the steepest increase in height?

- **Options:**

  A) North
  B) Ridge
  C) Valley

- **Answer (tutor only):** B
- **Explanation (tutor only):** Ridge's line climbs about 30 cm over 30 days (slope ≈ 1 cm/day), Valley's about half that, and North's barely rises.
- **Why the wrong options are wrong (tutor only):**
  A) North's line is the flattest.
  C) Valley rises, but less steeply than Ridge.
- **Hint:** Compare how much each line rises from day 0 to day 30.

### ch02-quiz-05-v2
- **Kind:** AI-written version of ch02-quiz-05
- **Concepts:** Aesthetics & ggplot layers; Visualizing associations
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [fix-facet-slopes.png](https://yanivjb.github.io/biostats-book/study_guide/images/fix-facet-slopes.png)
- **Question:**

These faceted scatterplots share the same axes. Which panel shows the steepest positive relationship between x and y?

- **Options:**

  A) A
  B) B
  C) C

- **Answer (tutor only):** B
- **Explanation (tutor only):** With shared axes, compare how much each trendline rises over the same x-range: B rises about 10 units, A only about 3, and C falls.
- **Why the wrong options are wrong (tutor only):**
  A) Positive, but it rises much less than B.
  C) It falls: a negative relationship.
- **Hint:** Steepest positive = rises the most.

### ch02-quiz-06
- **Kind:** Course original
- **Concepts:** Plot design principles; Aesthetics & ggplot layers
- **Type:** short answer
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch02-quiz-iris-aesthetics.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch02-quiz-iris-aesthetics.png)
- **Question:**

Plot setup (iris data, cleaned names): three panels, one per species (setosa, versicolor, virginica). Each point is a flower. The x-axis is sepal_length (about 4.3 to 7.9) and the y-axis is sepal_width (about 2 to 4.4). Point color shows petal_length (dark purple = short, about 1; yellow = long, about 7), and point size shows petal_width (small = narrow, large = wide). Each panel has a straight trendline from geom_smooth(method = "lm"). Setosa points sit to the upper left (short, wide sepals), are small and dark purple, and have a steep trendline. Versicolor points are in the middle, medium-sized and teal. Virginica points sit furthest right, are the largest and green to yellow, with the shallowest trendline.

From the plot, visually estimate which species has the: widest sepals? widest petals? longest sepals? longest petals?

- **Answer (tutor only):** Widest sepals: setosa. Widest petals: virginica. Longest sepals: virginica. Longest petals: virginica.
- **Explanation (tutor only):** Sepal width and length are read from position (y and x), so they're easy to judge. Petal width and length are read from point size and color, which is much harder, which is the point of the follow-up question on which aesthetics are easiest to compare (ch02-quiz-01).
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: guessing petal width from color or petal length from size (they're swapped), or picking versicolor for longest sepals because its points sit in the middle.
- **Hint:** Sepals: use the axes. Petals: use the legends for color and size.

### ch02-quiz-06-v1
- **Kind:** AI-written version of ch02-quiz-06
- **Concepts:** Plot design principles; Aesthetics & ggplot layers
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch02-var-penguin-aes.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch02-var-penguin-aes.png)
- **Question:**

Penguins are shown in three panels by species: x = bill length, y = bill depth, color = flipper length (yellow = long), size = body mass. Visually estimate which species has the:

1. shortest bills
2. shallowest bills
3. longest flippers
4. heaviest bodies

- **Options:**

  A) Adelie
  B) Chinstrap
  C) Gentoo

- **Answer (tutor only):** 1-A, 2-C, 3-C, 4-C
- **Explanation (tutor only):** Adelie points sit furthest left (bills ~39 mm vs ~48 mm). Gentoo sit lowest (depth ~15 mm vs ~18 mm), are the most yellow (flippers ~217 mm) and have the biggest points (~5,100 g).
- **Why the wrong options are wrong (tutor only):**
  Read each aesthetic separately: position for bills, color for flippers, size for mass.
- **Hint:** x and y position first, then color, then size.

### ch02-quiz-06-v2
- **Kind:** AI-written version of ch02-quiz-06
- **Concepts:** Plot design principles; Aesthetics & ggplot layers
- **Type:** MC
- **Question:**

In a scatterplot, point size shows body mass. Why is it hard to tell whether one penguin is twice as heavy as another from point size?

- **Options:**

  A) People judge area poorly, so differences in size are hard to read precisely
  B) Point size can't represent numbers
  C) Bigger points always hide smaller ones
  D) Size only works for categorical variables

- **Answer (tutor only):** A
- **Explanation (tutor only):** Size is one of the least precise aesthetics. Use it for a secondary variable, and put key comparisons on x and y.
- **Why the wrong options are wrong (tutor only):**
  B) It can; it's just imprecise.
  C) Overlap can happen, but isn't the main problem.
  D) Size can show continuous variables.
- **Hint:** Is twice the area easy to spot?

## Chapter 3: Reproducible science

### ch03-book-01
- **Kind:** Course original
- **Concepts:** Reproducible workflows; Data entry & data dictionaries
- **Type:** MC
- **Question:**

What is the biggest mistake in this table?

ID | weight | date_collected_empty_means_same_as_above
1-A1 | 104 | 2024-03-01
1-1B | 210 | (blank)
3-7 | 150 | (blank)
2-B | 176 | 2024-03-15
1-A5 | 110 | (blank)

- **Options:**

  A) ID should be lower case
  B) It's perfect, change nothing
  C) The column name weight is not sufficiently descriptive; it should include the units
  D) date_collected_empty_means_same_as_above is too wordy; replace with date
  E) Values for date_collected_empty_means_same_as_above are implied
  F) Date is in Year-Month-Day format, while Month-Day-Year format is preferred

- **Answer (tutor only):** E
- **Explanation (tutor only):** Spreadsheets should never leave values implied. Blank cells that 'mean the same as above' are easily broken by sorting or filtering, and anyone reading the data later can mistake them for missing data. Fill in every value.
- **Why the wrong options are wrong (tutor only):**
  A) Capitalization of a column name isn't a problem.
  B) The implied values are a real problem.
  C) Units matter, but they can go in the data dictionary. This is a smaller issue than implied data.
  D) The long name is clumsy, but it's not the biggest problem.
  F) Year-Month-Day is actually the recommended format, because it sorts correctly.
- **Hint:** What happens to the blank dates if someone sorts the table by weight?

### ch03-book-01-v1
- **Kind:** AI-written version of ch03-book-01
- **Concepts:** Reproducible workflows; Data entry & data dictionaries
- **Type:** MC
- **Question:**

What is the biggest problem with this table?

plant | height | site
P1 | 12.1 | North
P2 | 10.4 | "
P3 | 15.0 | "
P4 | 9.8 | South

- **Options:**

  A) Plant IDs should be numbers
  B) Ditto marks (") mean the site is implied rather than recorded
  C) height should be called h
  D) North and South should be abbreviated

- **Answer (tutor only):** B
- **Explanation (tutor only):** Every cell should hold its own value. Ditto marks rely on row order and break when data are sorted or filtered.
- **Why the wrong options are wrong (tutor only):**
  A) Text IDs are fine.
  C) A shorter name is less descriptive.
  D) Full words are clearer.
- **Hint:** What happens to the ditto marks if you sort by height?

### ch03-book-01-v2
- **Kind:** AI-written version of ch03-book-01
- **Concepts:** Reproducible workflows; Data entry & data dictionaries
- **Type:** MC
- **Question:**

Which is the best way to record the collection date in a spreadsheet?

- **Options:**

  A) Write the date in every row, as YYYY-MM-DD
  B) Write the date in the first row of each day and leave the rest blank
  C) Color rows by date
  D) Put the date in the file name only

- **Answer (tutor only):** A
- **Explanation (tutor only):** Every row should contain its own values in a consistent, unambiguous format. ISO dates (2024-03-01) sort correctly and can't be misread.
- **Why the wrong options are wrong (tutor only):**
  B) Blank cells imply values and break when sorted.
  C) Colors aren't data.
  D) The date gets lost once data are combined.
- **Hint:** Could each row stand on its own?

### ch03-book-02
- **Kind:** Course original
- **Concepts:** Reproducible workflows; Data entry & data dictionaries
- **Type:** select-all
- **Question:**

What would you expect in a data dictionary accompanying this table? (select all correct)

ID | weight | date_collected_empty_means_same_as_above
1-A1 | 104 | 2024-03-01
1-1B | 210 | (blank)
3-7 | 150 | (blank)
2-B | 176 | 2024-03-15
1-A5 | 110 | (blank)

- **Options:**

  A) The units for weight
  B) A statement that date is in Year-Month-Day format
  C) A statement explaining that in the date collected column, empty means same as above

- **Answer (tutor only):** A, B, C
- **Explanation (tutor only):** A data dictionary should say what each variable means, its units, and its format. Given the table as it is, documenting the 'empty means same as above' rule is better than leaving it unexplained, although the better fix is to fill in the dates.
- **Why the wrong options are wrong (tutor only):**
  Leaving any of these out forces a reader to guess.
- **Hint:** Imagine handing this table to someone who has never seen your study. What would they need to know?

### ch03-book-02-v1
- **Kind:** AI-written version of ch03-book-02
- **Concepts:** Reproducible workflows; Data entry & data dictionaries
- **Type:** select-all
- **Question:**

A table has columns: frog_id, svl, mass, capture_date. What should a data dictionary include? (Select all correct.)

- **Options:**

  A) What 'svl' means (snout–vent length) and its units
  B) The units for mass
  C) The date format used for capture_date
  D) The sample mean of mass

- **Answer (tutor only):** A, B, C
- **Explanation (tutor only):** A dictionary defines each variable, its units and its format. Summary statistics belong in the analysis.
- **Why the wrong options are wrong (tutor only):**
  D) That's a result, not a description of the data.
- **Hint:** What would a stranger need to interpret each column?

### ch03-book-02-v2
- **Kind:** AI-written version of ch03-book-02
- **Concepts:** Reproducible workflows; Data entry & data dictionaries
- **Type:** MC
- **Question:**

Why is a data dictionary important?

- **Options:**

  A) It lets others (and future you) correctly interpret every variable, its units and its codes
  B) It makes the file smaller
  C) It replaces the need for a script
  D) It's only needed for very large datasets

- **Answer (tutor only):** A
- **Explanation (tutor only):** Without definitions, units and codes, data can't be reused or checked.
- **Why the wrong options are wrong (tutor only):**
  B) It adds a file; it doesn't shrink anything.
  C) Scripts are still needed.
  D) Even small datasets need clear definitions.
- **Hint:** What happens if you open the data in five years?

### ch03-book-03
- **Kind:** Course original
- **Concepts:** Reproducible workflows
- **Type:** MC
- **Question:**

What should you do to make code reproducible? (pick the best answer)

- **Options:**

  A) Specify the working directory with setwd()
  B) Show the packages installed with install.packages()
  C) Restart R once you're done, and rerun your script to see if it works

- **Answer (tutor only):** C
- **Explanation (tutor only):** Restarting R clears everything you did by hand. If the script still runs top to bottom in a fresh session, it contains everything it needs.
- **Why the wrong options are wrong (tutor only):**
  A) setwd() points to a folder on your computer, so the script breaks on anyone else's computer. Use an R project instead.
  B) Installing is a one-time setup step; it shouldn't run every time the script does.
- **Hint:** How can you be sure your script doesn't depend on something you did by hand in the console?

### ch03-book-03-v1
- **Kind:** AI-written version of ch03-book-03
- **Concepts:** Reproducible workflows
- **Type:** MC
- **Question:**

What's the best quick check that your script is reproducible?

- **Options:**

  A) Restart R and run the whole script from top to bottom
  B) Check that the plots look nice
  C) Run just the last few lines
  D) Save the script with a new name

- **Answer (tutor only):** A
- **Explanation (tutor only):** A fresh session has no leftover objects, so if the script runs top to bottom, it doesn't depend on anything you did by hand.
- **Why the wrong options are wrong (tutor only):**
  B) Nice plots don't mean the code runs.
  C) Earlier lines may be broken or out of order.
  D) Renaming doesn't test anything.
- **Hint:** What does a fresh session reveal?

### ch03-book-03-v2
- **Kind:** AI-written version of ch03-book-03
- **Concepts:** Reproducible workflows
- **Type:** MC
- **Question:**

Your script works, but only if you first run a line you typed into the console last week. What should you do?

- **Options:**

  A) Add that line to the script, in the right place
  B) Remember to type it each time
  C) Email the line to collaborators
  D) Nothing; it works

- **Answer (tutor only):** A
- **Explanation (tutor only):** Everything the analysis needs should be in the script, in order, so it runs from scratch.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Fragile: easy to forget or lose.
  D) It only works by accident on your machine.
- **Hint:** Could a classmate run your script without that line?

### ch03-book-04
- **Kind:** Course original
- **Concepts:** Data entry & data dictionaries
- **Type:** MC
- **Question:**

R has a built-in dataset called iris. Which variable type is Species in the iris dataset?

- **Options:**

  A) numeric <dbl>
  B) logical <lgl>
  C) character <chr>
  D) factor <fct>

- **Answer (tutor only):** D
- **Explanation (tutor only):** Species is a categorical variable, and in iris it is stored as a factor: a category with a fixed set of levels (setosa, versicolor, virginica).
- **Why the wrong options are wrong (tutor only):**
  A) Numeric is for measurements.
  B) Logical is for TRUE/FALSE.
  C) Character also stores text, so this is a reasonable guess, but iris stores Species as a factor (with defined levels).
- **Hint:** Species has exactly three possible values. Which type is built for categories with set levels?

### ch03-book-04-v1
- **Kind:** AI-written version of ch03-book-04
- **Concepts:** Data entry & data dictionaries
- **Type:** MC
- **Question:**

In the penguins dataset, island has three values (Biscoe, Dream, Torgersen) stored with levels. What type is it?

- **Options:**

  A) numeric <dbl>
  B) logical <lgl>
  C) character <chr>
  D) factor <fct>

- **Answer (tutor only):** D
- **Explanation (tutor only):** A categorical variable stored with a fixed set of levels is a factor.
- **Why the wrong options are wrong (tutor only):**
  A) Island names aren't numbers.
  B) Not TRUE/FALSE.
  C) Character would be plain text without levels.
- **Hint:** What does <fct> stand for?

### ch03-book-04-v2
- **Kind:** AI-written version of ch03-book-04
- **Concepts:** Data entry & data dictionaries
- **Type:** MC
- **Question:**

What does a factor in R represent?

- **Options:**

  A) A categorical variable with a defined set of levels
  B) A number with decimals
  C) TRUE/FALSE values
  D) A date

- **Answer (tutor only):** A
- **Explanation (tutor only):** Factors store categories (e.g., species, treatment) along with their allowed levels and order.
- **Why the wrong options are wrong (tutor only):**
  B) That's double (numeric).
  C) That's logical.
  D) Dates have their own type.
- **Hint:** Think: categories with levels.

### ch03-book-05
- **Kind:** Course original
- **Concepts:** Reproducible workflows
- **Type:** MC
- **Question:**

Consider this R script:

# My R script
setwd("~/ybrandva/Desktop/silphium_project")

#### load data
silphium_data <- read_csv("mydata.csv")
View(silphium_data)

ggplot(silphium_data, aes(x = location, y = yield))+
  geom_point()

The script worked fine on my computer yesterday, but today I opened a new R session on the very same computer and it failed. What went wrong?

- **Options:**

  A) I set my working directory
  B) I loaded data from an absolute path, not a relative path
  C) I did not load the libraries in my script
  D) I used the View function

- **Answer (tutor only):** C
- **Explanation (tutor only):** read_csv() and ggplot() come from packages (readr and ggplot2). Yesterday they were probably loaded earlier in the session; in a fresh session, nothing is loaded, and the script never loads them itself.
- **Why the wrong options are wrong (tutor only):**
  A) setwd() is a problem for other people's computers, but it works on yours.
  B) The data are read with a relative path ("mydata.csv").
  D) View() is annoying in a script, but it doesn't make it fail.
- **Hint:** What is different about a brand new R session?

### ch03-book-05-v1
- **Kind:** AI-written version of ch03-book-05
- **Concepts:** Reproducible workflows
- **Type:** MC
- **Question:**

# Script
library(readr)
setwd("C:/Users/sam/Documents/frogs")
frogs <- read_csv("frog_data.csv")
View(frogs)
ggplot(frogs, aes(x = site, y = mass)) + geom_boxplot()

Sam opens a new R session on the same computer and runs this script. It fails at the last line. Why?

- **Options:**

  A) ggplot2 is never loaded
  B) setwd() is used
  C) View() is used
  D) The data file is a CSV

- **Answer (tutor only):** A
- **Explanation (tutor only):** Only readr is loaded. In a new session, ggplot() isn't available until library(ggplot2) runs. It worked before only because ggplot2 was loaded earlier by hand.
- **Why the wrong options are wrong (tutor only):**
  B) setwd() works on Sam's own computer.
  C) View() is annoying but doesn't cause errors.
  D) CSV is fine.
- **Hint:** Which package does ggplot() come from?

### ch03-book-05-v2
- **Kind:** AI-written version of ch03-book-05
- **Concepts:** Reproducible workflows
- **Type:** MC
- **Question:**

A script worked yesterday but fails in a fresh R session today with 'could not find function "filter"'. What's most likely?

- **Options:**

  A) The script never loads dplyr; it only worked because dplyr was loaded earlier by hand
  B) The data changed overnight
  C) R needs reinstalling
  D) filter() was removed from R

- **Answer (tutor only):** A
- **Explanation (tutor only):** A fresh session only has what the script itself loads. Put library(dplyr) at the top.
- **Why the wrong options are wrong (tutor only):**
  B) Data changes cause different errors.
  C) and D) Unnecessary explanations.
- **Hint:** What's different about a fresh session?

### ch03-book-06
- **Kind:** Course original
- **Concepts:** Reproducible workflows
- **Type:** MC
- **Question:**

Consider this R script:

# My R script
setwd("~/ybrandva/Desktop/silphium_project")

#### load data
silphium_data <- read_csv("mydata.csv")
View(silphium_data)

ggplot(silphium_data, aes(x = location, y = yield))+
  geom_point()

What about this script would prevent it from working on someone else's computer but allow it to work on mine?

- **Options:**

  A) Setting this working directory
  B) Loading data from an absolute path, not a relative path
  C) Neglecting to load libraries
  D) Using the View function

- **Answer (tutor only):** A
- **Explanation (tutor only):** setwd() points to a folder that exists only on my computer (~/ybrandva/Desktop/...). On anyone else's computer, that folder doesn't exist. Using an R project and relative paths avoids this.
- **Why the wrong options are wrong (tutor only):**
  B) The data path ("mydata.csv") is relative, so it isn't the problem.
  C) Missing libraries would break the script on my computer too.
  D) View() doesn't stop the script from working.
- **Hint:** Which line names a location that only exists on my computer?

### ch03-book-06-v1
- **Kind:** AI-written version of ch03-book-06
- **Concepts:** Reproducible workflows
- **Type:** MC
- **Question:**

# Script
library(readr)
setwd("C:/Users/sam/Documents/frogs")
frogs <- read_csv("frog_data.csv")
View(frogs)
ggplot(frogs, aes(x = site, y = mass)) + geom_boxplot()

Which part will make this script fail on a classmate's computer (but not Sam's)?

- **Options:**

  A) setwd("C:/Users/sam/Documents/frogs")
  B) library(readr)
  C) View(frogs)
  D) geom_boxplot()

- **Answer (tutor only):** A
- **Explanation (tutor only):** That folder only exists on Sam's computer. Use an R project with relative paths instead.
- **Why the wrong options are wrong (tutor only):**
  B) readr loads anywhere it's installed.
  C) View() doesn't depend on the computer.
  D) Unrelated to the computer.
- **Hint:** Which line names a specific person's folder?

### ch03-book-06-v2
- **Kind:** AI-written version of ch03-book-06
- **Concepts:** Reproducible workflows
- **Type:** MC
- **Question:**

Why are relative paths (e.g., "data/frog_data.csv") better than absolute paths in a shared project?

- **Options:**

  A) They work wherever the project folder is placed, on any computer
  B) They load data faster
  C) They're required by readr
  D) They encrypt the data

- **Answer (tutor only):** A
- **Explanation (tutor only):** A relative path starts from the project folder, so it works for anyone who has the project.
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) None of these is true.
- **Hint:** Does the path depend on whose computer it is?

### ch03-book-07
- **Kind:** Course original
- **Concepts:** Reproducible workflows
- **Type:** MC
- **Question:**

Consider this R script:

# My R script
setwd("~/ybrandva/Desktop/silphium_project")

#### load data
silphium_data <- read_csv("mydata.csv")
View(silphium_data)

ggplot(silphium_data, aes(x = location, y = yield))+
  geom_point()

What about the script is annoying for someone using this code (once it works) and should be removed, but doesn't stop the code from working?

- **Options:**

  A) I set my working directory
  B) I loaded data from an absolute path, not a relative path
  C) I did not load the libraries in my script
  D) I used the View function

- **Answer (tutor only):** D
- **Explanation (tutor only):** View() opens a new window every time the script runs. It's useful for exploring in the console, but it doesn't belong in a saved script.
- **Why the wrong options are wrong (tutor only):**
  A) and C) actually stop the script from working (on others' computers, or in a new session).
  B) The data path is relative, so this isn't an issue here.
- **Hint:** Which line is for you to look at the data, rather than part of the analysis?

### ch03-book-07-v1
- **Kind:** AI-written version of ch03-book-07
- **Concepts:** Reproducible workflows
- **Type:** MC
- **Question:**

# Script
library(readr)
setwd("C:/Users/sam/Documents/frogs")
frogs <- read_csv("frog_data.csv")
View(frogs)
ggplot(frogs, aes(x = site, y = mass)) + geom_boxplot()

Which line is unnecessary clutter in a shared script (annoying to others) but doesn't stop the code from working?

- **Options:**

  A) setwd(...)
  B) library(readr)
  C) View(frogs)
  D) frogs <- read_csv("frog_data.csv")

- **Answer (tutor only):** C
- **Explanation (tutor only):** View() opens a window every time the script runs. It's useful interactively but shouldn't be in a shared script.
- **Why the wrong options are wrong (tutor only):**
  A) setwd() actually breaks the script on other computers.
  B) and D) Needed.
- **Hint:** Which line only matters while you're exploring?

### ch03-book-07-v2
- **Kind:** AI-written version of ch03-book-07
- **Concepts:** Reproducible workflows
- **Type:** MC
- **Question:**

Which of these belongs in your console, not in a saved analysis script?

- **Options:**

  A) install.packages("dplyr")
  B) library(dplyr)
  C) my_data <- read_csv("data/plants.csv")
  D) summary_table <- my_data |> summarize(mean_h = mean(height))

- **Answer (tutor only):** A
- **Explanation (tutor only):** Install once from the console. The script should load packages, read data and do the analysis.
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) These are part of the analysis and should run every time.
- **Hint:** Which line only needs to run once, ever?

### ch03-chimein-01
- **Kind:** Course original
- **Concepts:** Reproducible workflows; Data entry & data dictionaries
- **Type:** MC
- **Question:**

You are entering measurements of tree diameters into a spreadsheet. One of the trees had something odd about it that made you wonder whether its data should be included. What should you do? (choose the best answer)

- **Options:**

  A) Do not enter it
  B) Enter it and move on
  C) Include a * in the column
  D) Highlight the column in the spreadsheet
  E) Add a brief note in the notes column explaining your concern

- **Answer (tutor only):** E
- **Explanation (tutor only):** Record the data and record your concern in a notes column. That keeps the raw data complete and lets you (or anyone else) decide later, with full information, whether to exclude it, and report that decision honestly.
- **Why the wrong options are wrong (tutor only):**
  A) Leaving it out throws away data and hides a decision nobody can check.
  B) Entering it without comment loses what you noticed.
  C) A * inside a data column turns numbers into text and breaks the analysis.
  D) Highlighting is lost when the file is read into R or saved as CSV, and color doesn't say what the concern was.
- **Hint:** Which option keeps the data intact and records what you noticed in a way that survives being read into R?

### ch03-chimein-01-v1
- **Kind:** AI-written version of ch03-chimein-01
- **Concepts:** Reproducible workflows; Data entry & data dictionaries
- **Type:** MC
- **Question:**

While measuring fish, you notice one had a damaged fin that may have affected its swimming speed. What should you do when entering its data?

- **Options:**

  A) Leave it out without telling anyone
  B) Enter it, and write the concern in a notes column
  C) Change its speed to match the others
  D) Color the cell red

- **Answer (tutor only):** B
- **Explanation (tutor only):** Record all the data, and document anything unusual in a notes column. Then decisions about exclusion can be made transparently later.
- **Why the wrong options are wrong (tutor only):**
  A) Silent exclusion is undocumented and irreproducible.
  C) That's fabricating data.
  D) Colors aren't read by R and are easily lost.
- **Hint:** How would someone else know about the concern?

### ch03-chimein-01-v2
- **Kind:** AI-written version of ch03-chimein-01
- **Concepts:** Reproducible workflows; Data entry & data dictionaries
- **Type:** MC
- **Question:**

Why is highlighting cells in a spreadsheet a poor way to flag questionable data?

- **Options:**

  A) Formatting isn't data: it's lost when the file is read into R or saved as CSV
  B) Highlighting is too colorful
  C) Spreadsheets can't highlight
  D) It's fine; highlighting is the best method

- **Answer (tutor only):** A
- **Explanation (tutor only):** Put flags and notes in their own column so they travel with the data.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Not the reason.
  D) Highlights disappear in most analysis pipelines.
- **Hint:** What happens to cell colors in a CSV?

### ch03-chimein-02
- **Kind:** Course original
- **Concepts:** Missing data & bias
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch03-chimein-02.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch03-chimein-02.png)
- **Question:**

Consider this glucose and insulin dataset from glucose tolerance tests (GTT). Some insulin values are NA with the note 'insulin below curve', meaning the insulin level was too low for the assay to measure.

GTT time | glucose mg/dl | insulin ng/ml | note
0 | 99.2 | NA | insulin below curve
5 | 349.3 | 0.205 |
15 | 286.1 | 0.129 |
30 | 312 | 0.175 |
60 | 99.9 | 0.122 |
120 | 217.9 | NA | insulin below curve
0 | 185.8 | 0.251 |
5 | 297.4 | 2.228 |
15 | 439 | 2.078 |
30 | 362.3 | 0.775 |
60 | 232.7 | 0.5 |
120 | 260.7 | 0.523 |
0 | 198.5 | 0.151 |
5 | 530.6 | NA | insulin below curve

What is the most serious concern with fully ignoring the NA data?

- **Options:**

  A) Nothing. It's fine. Missing data happens
  B) We would just have a smaller sample size, which is a bummer
  C) We would systematically overestimate insulin levels
  D) We would systematically underestimate insulin levels

- **Answer (tutor only):** C
- **Explanation (tutor only):** These values are missing for a reason: insulin was too LOW to measure. Dropping them removes exactly the lowest values, so the remaining data are biased upward and we'd overestimate insulin. Missing data that aren't random introduce bias, not just a smaller sample.
- **Why the wrong options are wrong (tutor only):**
  A) Missing data do happen, but here they are missing for a systematic reason.
  B) A smaller sample is a cost, but the bigger problem is bias.
  D) Dropping the lowest values pushes estimates up, not down.
- **Hint:** What do the missing insulin values have in common? If you drop them, what happens to the average of what's left?

### ch03-chimein-02-v1
- **Kind:** AI-written version of ch03-chimein-02
- **Concepts:** Missing data & bias
- **Type:** MC
- **Question:**

A water-quality probe reports 'NA' whenever lead concentration is below its detection limit. If you calculate mean lead concentration ignoring the NAs, you would:

- **Options:**

  A) Get an unbiased estimate
  B) Overestimate mean lead
  C) Underestimate mean lead
  D) Just have a smaller sample, with no bias

- **Answer (tutor only):** B
- **Explanation (tutor only):** The missing values are the lowest ones. Dropping them leaves only the higher readings, so the mean is pushed up.
- **Why the wrong options are wrong (tutor only):**
  A) and D) Missingness depends on the value, so it isn't harmless.
  C) The dropped values are low, not high.
- **Hint:** Are the missing values random, or a particular kind of value?

### ch03-chimein-02-v2
- **Kind:** AI-written version of ch03-chimein-02
- **Concepts:** Missing data & bias
- **Type:** MC
- **Question:**

In a survey of plant heights, the tallest plants were too tall to reach, so their heights were left blank. Ignoring the blanks would make your estimate of mean height:

- **Options:**

  A) Too low
  B) Too high
  C) Unbiased
  D) Impossible to calculate

- **Answer (tutor only):** A
- **Explanation (tutor only):** The missing plants are the tallest, so averaging only the measured ones underestimates the mean.
- **Why the wrong options are wrong (tutor only):**
  B) The dropped values are high, so the mean goes down.
  C) Missingness depends on height.
  D) You can calculate it; it's just biased.
- **Hint:** Which plants are missing?

### ch03-chimein-03
- **Kind:** Course original
- **Concepts:** Reproducible workflows; Data entry & data dictionaries
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch03-chimein-03.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch03-chimein-03.png)
- **Question:**

Consider this data set:

id | date | glucose
101 | 2015-06-14 | 149.3
102 | (blank) | 95.3
103 | 2015-06-18 | 97.5
104 | (blank) | 117.0
105 | (blank) | 108.0
106 | 2015-06-20 | 149.0
107 | (blank) | 169.4

What is the biggest problem with this data set?

- **Options:**

  A) Date does not follow Month-Day-Year convention
  B) We don't know the units for glucose
  C) Date is implied
  D) id should not be a number because it is not numeric
  E) It is not tidy

- **Answer (tutor only):** C
- **Explanation (tutor only):** Blank dates that 'mean the same as above' leave values implied. They break when the data are sorted or filtered and look like missing data to anyone else. Every cell should be filled in.
- **Why the wrong options are wrong (tutor only):**
  A) Year-Month-Day is the recommended format (it sorts correctly).
  B) Units do matter, but they belong in the data dictionary. This is a smaller problem than implied values.
  D) IDs can be written as numbers; they just shouldn't be treated as numeric in analysis.
  E) The data are tidy: each row is one observation and each column one variable.
- **Hint:** What would happen to the blank dates if someone sorted the table by glucose?

### ch03-chimein-03-v1
- **Kind:** AI-written version of ch03-chimein-03
- **Concepts:** Reproducible workflows; Data entry & data dictionaries
- **Type:** MC
- **Question:**

What is the biggest problem with this dataset?

tree | species | dbh_cm
T1 | oak | 34.2
T2 | | 28.9
T3 | | 41.0
T4 | maple | 22.5

- **Options:**

  A) dbh_cm should not include units in its name
  B) Species is implied (left blank for 'same as above')
  C) Tree IDs should be numbers
  D) The data aren't sorted

- **Answer (tutor only):** B
- **Explanation (tutor only):** Blank cells meant as 'same as above' are implied values. They break when data are sorted, filtered or read into R (they become NA).
- **Why the wrong options are wrong (tutor only):**
  A) Units in the name are helpful.
  C) Text IDs are fine.
  D) Sorting order doesn't matter if every row is complete.
- **Hint:** What would R put in those blank cells?

### ch03-chimein-03-v2
- **Kind:** AI-written version of ch03-chimein-03
- **Concepts:** Reproducible workflows; Data entry & data dictionaries
- **Type:** MC
- **Question:**

A spreadsheet leaves the 'site' cell blank whenever it's the same as the row above. When read into R, those cells become:

- **Options:**

  A) NA (missing)
  B) Automatically filled with the value above
  C) Zero
  D) An error that stops R from reading the file

- **Answer (tutor only):** A
- **Explanation (tutor only):** R has no idea a blank means 'same as above'; it records NA. Fill every cell explicitly.
- **Why the wrong options are wrong (tutor only):**
  B) R doesn't fill values down.
  C) Blanks aren't zeros.
  D) R reads the file; it just records NA.
- **Hint:** Does R know your shorthand?

### ch03-hw-01
- **Kind:** Course original
- **Concepts:** Reproducible workflows; Data entry & data dictionaries
- **Type:** select-all
- **Question:**

What would you expect in a data dictionary describing the following data table? (select all correct)

Date | Tree_ID | Diameter
2025-06-01 | 1A | 8
2025-06-01 | 2A | 12
2025-06-01 | 1B | 3
2025-06-01 | 2B | 9

- **Options:**

  A) An explanation of what Tree_ID represents
  B) The units for the Diameter variable
  C) A statement that date is in Year-Month-Day format

- **Answer (tutor only):** A, B, C
- **Explanation (tutor only):** A data dictionary explains everything a stranger needs to use the data: what each variable means (what is a Tree_ID? what do 1 and A stand for?), its units (cm? inches?), and its format (YYYY-MM-DD).
- **Why the wrong options are wrong (tutor only):**
  All three belong in the dictionary. Leaving any out forces a future reader (including future you) to guess.
- **Hint:** Imagine handing this table to someone who has never seen your study. What would they need to ask you?

### ch03-hw-01-v1
- **Kind:** AI-written version of ch03-hw-01
- **Concepts:** Reproducible workflows; Data entry & data dictionaries
- **Type:** select-all
- **Question:**

What would you expect in a data dictionary describing this table? (Select all correct.)

site | plot | cover
N1 | 3 | 45
N1 | 4 | 60
S2 | 1 | 15

- **Options:**

  A) What 'site' codes like N1 and S2 mean
  B) The units of cover (e.g., % of the plot)
  C) How plot numbers were assigned
  D) The analysis results

- **Answer (tutor only):** A, B, C
- **Explanation (tutor only):** A data dictionary explains every variable: what codes mean, the units, and how values were recorded. Results belong in the analysis, not the dictionary.
- **Why the wrong options are wrong (tutor only):**
  D) The dictionary describes the data, not what you found.
- **Hint:** Could a stranger interpret every column?

### ch03-hw-01-v2
- **Kind:** AI-written version of ch03-hw-01
- **Concepts:** Reproducible workflows; Data entry & data dictionaries
- **Type:** MC
- **Question:**

A collaborator sends you a spreadsheet with a column 'temp' containing values like 22, 31 and 18. What's the most important missing information a data dictionary should provide?

- **Options:**

  A) The units (°C or °F?) and what was measured (air, water, soil?)
  B) The font used in the spreadsheet
  C) The collaborator's favorite temperature
  D) Nothing; the numbers speak for themselves

- **Answer (tutor only):** A
- **Explanation (tutor only):** Without units and a definition, 22 could be 22 °C water or 22 °F air: completely different meanings.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Irrelevant.
  D) Numbers without units can't be interpreted.
- **Hint:** Could you interpret 22 without knowing more?

### ch03-hw-03
- **Kind:** Course original
- **Concepts:** Reproducible workflows
- **Type:** MC
- **Question:**

How should you make your code more reproducible? (choose the best answer)

- **Options:**

  A) Annotate code with comments to indicate the purpose of each section
  B) Read in your data BEFORE loading in the required packages
  C) Use absolute file paths rather than relative paths

- **Answer (tutor only):** A
- **Explanation (tutor only):** Comments explain what each part of the code is for, so others (and future you) can follow, check, and rerun it.
- **Why the wrong options are wrong (tutor only):**
  B) Packages should be loaded first, at the top of the script; functions like read_csv() won't exist until they are.
  C) Absolute paths (like C:/Users/yaniv/...) only work on your computer. Relative paths inside an R project work for anyone.
- **Hint:** Which option would still help a stranger running your script on their own computer?

### ch03-hw-03-v1
- **Kind:** AI-written version of ch03-hw-03
- **Concepts:** Reproducible workflows
- **Type:** MC
- **Question:**

Which practice most helps someone else (or future you) understand and rerun your analysis?

- **Options:**

  A) Comments explaining what each section does and why
  B) Running code by typing it into the console instead of saving a script
  C) Using absolute file paths
  D) Loading packages after you use them

- **Answer (tutor only):** A
- **Explanation (tutor only):** Comments make the logic clear. Scripts (not console typing), relative paths and loading packages first all help too.
- **Why the wrong options are wrong (tutor only):**
  B) Console-only code isn't saved or shareable.
  C) Absolute paths break on other computers.
  D) Code would fail when run in order.
- **Hint:** What would a stranger reading your script need?

### ch03-hw-03-v2
- **Kind:** AI-written version of ch03-hw-03
- **Concepts:** Reproducible workflows
- **Type:** MC
- **Question:**

Which change makes this line more reproducible?
read_csv("/Users/maria/Desktop/thesis/data.csv")

- **Options:**

  A) Use a project with a relative path: read_csv("data/data.csv")
  B) Add more folders to the path
  C) Move the file to the Desktop
  D) Use setwd("/Users/maria/Desktop") first

- **Answer (tutor only):** A
- **Explanation (tutor only):** Absolute paths only exist on one computer. A relative path inside an R project works anywhere the project folder is copied.
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) All still depend on Maria's computer.
- **Hint:** Will /Users/maria exist on a classmate's laptop?

### ch03-hw-04
- **Kind:** Course original
- **Concepts:** Data entry & data dictionaries
- **Type:** MC
- **Question:**

R has a built-in dataset called iris, with measurements of flowers. What type of variable is Petal.Length?

- **Options:**

  A) character
  B) logical
  C) factor
  D) numeric

- **Answer (tutor only):** D
- **Explanation (tutor only):** Petal length is a measurement (in cm, with decimals like 1.4), so R stores it as a number (numeric, shown as <dbl>).
- **Why the wrong options are wrong (tutor only):**
  A) Character is for text.
  B) Logical is for TRUE/FALSE.
  C) Factor is for categories, like Species.
- **Hint:** Is petal length a measurement or a category?

### ch03-hw-04-v1
- **Kind:** AI-written version of ch03-hw-04
- **Concepts:** Data entry & data dictionaries
- **Type:** MC
- **Question:**

In the penguins dataset, what type of variable is body_mass (values like 3750, 3800, 3250)?

- **Options:**

  A) character
  B) logical
  C) factor
  D) numeric

- **Answer (tutor only):** D
- **Explanation (tutor only):** Body mass is a measured quantity, stored as numbers (integer or double), so it's numeric.
- **Why the wrong options are wrong (tutor only):**
  A) Character is text.
  B) Logical is TRUE/FALSE.
  C) Factors are categories.
- **Hint:** Is it a quantity or a category?

### ch03-hw-04-v2
- **Kind:** AI-written version of ch03-hw-04
- **Concepts:** Data entry & data dictionaries
- **Type:** MC
- **Question:**

A column called is_flowering contains only TRUE and FALSE. What type is it in R?

- **Options:**

  A) numeric
  B) logical
  C) character
  D) factor

- **Answer (tutor only):** B
- **Explanation (tutor only):** R stores TRUE/FALSE values as a logical variable.
- **Why the wrong options are wrong (tutor only):**
  A) They're not numbers (though R can count TRUEs).
  C) Not text.
  D) Not a factor unless converted.
- **Hint:** Which type holds TRUE/FALSE?

### ch03-hw-05
- **Kind:** Course original
- **Concepts:** Data entry & data dictionaries
- **Type:** TF
- **Question:**

TRUE or FALSE: A variable whose values have decimals (e.g., 4.31, 5.67, 7.82) is stored as a double. It could be converted to an integer without losing information relevant to our analyses.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** Integers are whole numbers. Converting 4.31 to an integer gives 4, throwing away the decimal part, which is real information about the measurement.
- **Why the wrong options are wrong (tutor only):**
  TRUE: converting to integer rounds off (truncates) the decimals, so information is lost.
- **Hint:** What happens to 4.31 if it can only be a whole number?

### ch03-hw-05-v1
- **Kind:** AI-written version of ch03-hw-05
- **Concepts:** Data entry & data dictionaries
- **Type:** TF
- **Question:**

TRUE or FALSE: Leaf lengths like 4.31, 5.67 and 7.82 cm can be converted to integers without losing information we care about.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** B
- **Explanation (tutor only):** Converting to integer drops the decimals (4.31 → 4), throwing away real measurement detail.
- **Why the wrong options are wrong (tutor only):**
  A) The decimals carry meaningful differences between leaves.
- **Hint:** What happens to 4.31 if you store it as a whole number?

### ch03-hw-05-v2
- **Kind:** AI-written version of ch03-hw-05
- **Concepts:** Data entry & data dictionaries
- **Type:** TF
- **Question:**

TRUE or FALSE: Counts of eggs per nest (3, 5, 2, 4) can be stored as integers without losing information.

- **Options:**

  A) TRUE
  B) FALSE

- **Answer (tutor only):** A
- **Explanation (tutor only):** Counts are already whole numbers, so storing them as integers loses nothing.
- **Why the wrong options are wrong (tutor only):**
  B) There are no decimals to lose.
- **Hint:** Do counts ever have decimals?
