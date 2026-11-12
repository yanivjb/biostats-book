ROWS = [
# ---------------- Quiz: Linear models group quiz (Oct 21) ----------------
dict(id="ch13-quiz-01", source="Linear models group quiz (2026), Q1", topics="categorical predictors, linear model coefficients", type="MC",
question="""Orange juice increases tooth growth, so researchers asked whether vitamin C alone does the job: they gave hamsters vitamin C at three doses: Dose A (0.5 mg/day), Dose B (1 mg/day) or Dose C (2 mg/day), either in water (SuppVC) or as orange juice (OJ). They fit this linear model:

tooth_length = 12.45 - 3.70 × SuppVC + 9.13 × DOSE_B + 15.50 × DOSE_C

Dose was modeled as a categorical variable, not as a number (0.5, 1, 2). What does this choice mean?""",
options="""A) Each dose gets its own mean, so no constant change per mg is assumed
B) The model fits a single slope: the change in tooth length per mg
C) It makes no difference; the predictions are identical either way
D) Categorical predictors are required whenever there are 3+ values""",
answer="A",
explanation="As a category, each dose level gets its own coefficient (compared to the reference, Dose A). The model makes no assumption about the shape of the dose-response, e.g. that going from 0.5 to 1 mg has half the effect of going from 1 to 2 mg. Treating dose as a number would fit one straight-line slope.",
why_wrong="""B) That's what you get when dose is a number: one slope for 'per mg'.
C) The predictions differ unless tooth length happens to change perfectly linearly with dose.
D) Numbers with three or more values can be modeled either way. It's a choice about what we want to assume.""",
hint="How many coefficients does dose get in this model? How many would it get as a number?",
drafted_by_claude="question (made MC), options, explanation, why_wrong, hint", flags="Original was open ('What is the difference? Why would I?')."),

dict(id="ch13-quiz-02", source="Linear models group quiz (2026), Q2", topics="categorical predictors, predictions", type="numeric",
question="""Orange juice increases tooth growth, so researchers asked whether vitamin C alone does the job: they gave hamsters vitamin C at Dose A (0.5 mg/day), Dose B (1 mg/day) or Dose C (2 mg/day), either in water (SuppVC) or as orange juice (OJ). The linear model is:

tooth_length = 12.45 - 3.70 × SuppVC + 9.13 × DOSE_B + 15.50 × DOSE_C

(SuppVC, DOSE_B and DOSE_C are 1 if true and 0 otherwise.)

What is the predicted mean tooth length for a hamster given Dose A of orange juice?""",
answer="12.45", explanation="OJ and Dose A are both reference levels, so SuppVC = 0, DOSE_B = 0 and DOSE_C = 0. The prediction is just the intercept: 12.45.",
why_wrong="Common mistake: subtracting 3.70. That coefficient applies only to the vitamin C in water (SuppVC) group.",
hint="Which of the indicator variables equal 1 for an OJ, Dose A hamster?",
drafted_by_claude="question (made self-contained), explanation, why_wrong, hint"),

dict(id="ch13-quiz-03", source="Linear models group quiz (2026), Q3", topics="categorical predictors, predictions", type="numeric",
question="""Hamster tooth growth with vitamin C in water (SuppVC) or orange juice, at three doses:

tooth_length = 12.45 - 3.70 × SuppVC + 9.13 × DOSE_B + 15.50 × DOSE_C

(SuppVC, DOSE_B and DOSE_C are 1 if true and 0 otherwise; orange juice and Dose A are the reference levels.)

What is the predicted mean tooth length for a hamster given Dose C (2 mg/day) of vitamin C in water (SuppVC)?""",
answer="24.25", explanation="SuppVC = 1 and DOSE_C = 1 (DOSE_B = 0): 12.45 - 3.70 + 15.50 = 24.25.",
why_wrong="Common mistakes: forgetting the -3.70 for SuppVC (gives 27.95), or adding the Dose B coefficient too.",
hint="Start at the intercept, then add each coefficient whose indicator equals 1.",
drafted_by_claude="question (made self-contained), explanation, why_wrong, hint"),

dict(id="ch13-quiz-04", source="Linear models group quiz (2026), Q4", topics="residuals, predictions", type="numeric",
question="""Hamster tooth growth with vitamin C in water (SuppVC) or orange juice, at three doses:

tooth_length = 12.45 - 3.70 × SuppVC + 9.13 × DOSE_B + 15.50 × DOSE_C

(SuppVC, DOSE_B and DOSE_C are 1 if true and 0 otherwise; orange juice and Dose A are the reference levels.)

A hamster given Dose A (0.5 mg/day) of vitamin C in water (SuppVC) had a tooth length of 8.00. What is its residual?""",
answer="-0.75", explanation="Prediction = 12.45 - 3.70 = 8.75. Residual = observed - predicted = 8.00 - 8.75 = -0.75. The negative sign means this hamster's teeth were shorter than the model predicted.",
why_wrong="Common mistake: predicted - observed (+0.75). Residuals are observed minus predicted.",
hint="First find the prediction, then subtract it from the observed value.",
drafted_by_claude="question (made self-contained), explanation, why_wrong, hint"),

dict(id="ch13-quiz-05", source="Linear models group quiz (2026), Q6", topics="linear model formulas, covariates", type="MC",
question="""Hsieh et al. (2006) compared the year-to-year coefficient of variation (cv) in larval population size between exploited and unexploited fish species. Their model adjusted for age at maturation (age), which also seemed to influence cv. Which linear model matches this design?""",
options="""A) lm(cv ~ exploited + age)
B) lm(exploited ~ cv + age)
C) lm(age ~ cv + exploited)
D) lm(cv ~ exploited)""",
answer="A",
explanation="The response (cv) goes on the left. The key explanatory variable (exploited or not) and the variable we adjust for (age at maturation) both go on the right.",
why_wrong="""B) and C) put an explanatory variable on the left as the response.
D) leaves out age at maturation, so it doesn't adjust for it.""",
hint="What is the response variable? Which variables are we using to predict it?",
drafted_by_claude="question (made MC), options, explanation, why_wrong, hint", flags="Original was 'write down the model'."),

dict(id="ch13-quiz-06", source="Linear models group quiz (2026), Q8", topics="residuals, sums of squares, residual standard deviation", type="matching",
question="""To ask whether fishing makes fish populations more variable, a model compared the year-to-year coefficient of variation (cv) in larval abundance of exploited and unexploited fish species, adjusting for age at maturation: lm(cv ~ exploited + age). The model gives three summaries of its residuals. Match each to how it is calculated:

1. Residual sum of squares = 2.45
2. Mean square residual = 0.098
3. Residual standard deviation = 0.313""",
options="""A) Square root of the mean square residual
B) Sum of the squared residuals
C) Residual sum of squares divided by its degrees of freedom""",
answer="1-B, 2-C, 3-A",
explanation="Square each residual and add them up to get the residual sum of squares (2.45). Divide by the residual degrees of freedom to get the mean square, an estimate of the residual variance (0.098). Its square root (0.313) is the residual standard deviation: roughly how far a typical point falls from its prediction, in the units of cv.",
why_wrong="Common mix-up: the mean square and the standard deviation. The mean square is a variance (squared units); the SD is its square root.",
hint="Which of these three is in the same units as the response?",
drafted_by_claude="question (made matching), options, explanation, why_wrong, hint", flags="Original asked 'what do these mean, how were they calculated' (open)."),

dict(id="ch13-quiz-07", source="Linear models group quiz (2026), Q8 (follow-up)", topics="residuals, degrees of freedom", type="numeric",
question="""To ask whether fishing makes fish populations more variable, a model compared the year-to-year coefficient of variation (cv) in larval abundance of exploited and unexploited fish species, adjusting for age at maturation: lm(cv ~ exploited + age). The model has a residual sum of squares of 2.45 and a mean square residual of 0.098. How many residual degrees of freedom does the model have?""",
answer="25", explanation="Mean square = sum of squares / df, so df = 2.45 / 0.098 = 25.",
why_wrong="Common mistake: multiplying instead of dividing (2.45 × 0.098 = 0.24).",
hint="How do you get from a sum of squares to a mean square?",
drafted_by_claude="all (new question)", flags="New follow-up built from the numbers in Q8."),

dict(id="ch13-quiz-01-open", source="Linear models group quiz (2026), Q1", topics="categorical predictors, linear model coefficients", type="open", include="no",
question="""Orange juice increases tooth growth, so researchers asked whether vitamin C alone does the job: they gave hamsters vitamin C at three doses (0.5, 1 or 2 mg/day), in water or as orange juice, and modeled tooth length with dose as a categorical variable rather than a number. What is the difference between these two choices, and why might you choose the categorical one?""",
answer="""Model answer: As a category, each dose gets its own mean (two coefficients, compared to the reference dose), so the model doesn't assume any particular shape for the dose-response. As a number, dose gets a single slope, which assumes each extra mg changes tooth length by the same amount (a straight line). With only three doses, often unevenly spaced, a categorical model avoids assuming linearity; the cost is an extra parameter and no way to predict between doses.""",
explanation="This is the trade-off between flexibility (categorical) and a simpler, more assumption-laden model (numeric).",
hint="How many coefficients does dose get each way? What does a single slope assume?"),

dict(id="ch13-quiz-08", source="Linear models group quiz (2026), Q7", topics="linear model coefficients, multiple predictors", type="MC",
question="""The plot shows the coefficient of variation (cv) in larval abundance for exploited and unexploited fish species, against age at maturation. The model is lm(cv ~ exploited + age), where exploited is "yes" or "no" ("no" is the reference level).

Which set of estimates best matches the plot?""",
image="ch13-quiz-fish.png",
options="""A) (Intercept) = 1.25, exploitedyes = 0.45, age = -0.04
B) (Intercept) = 1.25, exploitedyes = -0.45, age = -0.04
C) (Intercept) = 0.98, exploitedyes = 0.53, age = 0
D) (Intercept) = 1.50, exploitedyes = 0.45, age = 0.04""",
answer="A",
explanation="Exploited species (orange) sit higher than unexploited species of the same age, so exploitedyes is positive. Within each group, cv tends to fall with age at maturation, so the age slope is negative. The intercept is the predicted cv of an unexploited species at age 0: extend the blue cloud back to age 0, about 1.25.",
why_wrong="""B) Gets the direction of the exploited effect backwards.
C) An age slope of 0 ignores the downward trend; these numbers are close to the simple group means.
D) A positive age slope doesn't match the downward trend.""",
hint="Check the signs first: are exploited species higher or lower? Does cv go up or down with age?"),

dict(id="ch13-quiz-09", source="Linear models group quiz (2026), Q7 (follow-up)", topics="predictions, multiple predictors", type="numeric",
question="""To ask whether fishing makes fish populations more variable, a model compared the year-to-year coefficient of variation (cv) in larval abundance of exploited and unexploited fish species, adjusting for age at maturation: lm(cv ~ exploited + age). The fitted model is (exploitedyes = 1 for exploited species, 0 otherwise):

cv = 1.25 + 0.45 × exploitedyes - 0.04 × age

What is the predicted cv for an exploited species that matures at 5 years?""",
answer="1.5", explanation="1.25 + 0.45 × 1 - 0.04 × 5 = 1.25 + 0.45 - 0.20 = 1.50.",
why_wrong="Common mistakes: leaving out the exploited coefficient (1.05), or adding the age term instead of subtracting it (1.90).",
hint="exploitedyes = 1 for an exploited species."),

dict(id="ch13-quiz-10", source="Linear models group quiz (2026), Q9", topics="interpreting linear models, writing results", type="open", include="no",
image="ch13-quiz-fish.png",
question="""To ask whether fishing makes fish populations more variable, a model compared the year-to-year coefficient of variation (cv) in larval abundance of exploited and unexploited fish species, adjusting for age at maturation: lm(cv ~ exploited + age). Fit to 28 fish species, it gives:

(Intercept) = 1.25, exploitedyes = 0.45, age = -0.04
Residual standard deviation = 0.313 (25 df)

Summarize these results in a short paragraph for a biologist.""",
answer="""Model answer: After adjusting for age at maturation, exploited fish species had more variable larval populations than unexploited species: their year-to-year CV was about 0.45 higher. Within each group, species that mature later had slightly less variable larval abundance (about 0.04 lower CV per year of maturation age). Individual species typically deviate from the model's predictions by about 0.3. This is an observational comparison, so it shows an association with exploitation, not that fishing caused the higher variability.""",
explanation="A good summary states the key comparison in biological terms, gives effect sizes in the units of the response, mentions the covariate, and avoids causal language for observational data.",
hint="Start with the comparison the study was about (exploited vs unexploited). How big is the difference, and what was adjusted for?"),

# ---------------- Homework ----------------
dict(id="ch13-hw-01", source="Linear models homework, Q1", topics="scientific vs statistical models", type="select-all",
question="""Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. Which of the following are scientific models? (Select all that apply. A scientific model need not be correct.)""",
options="""A) A theory that compounds in chocolate improve brain function, leading to more Nobel-worthy discoveries
B) A model describing how research funding, education systems, cultural values, and a society's wealth to spend on luxuries like chocolate interact to shape Nobel Prize rates
C) A regression showing that for every additional 0.5 kg of chocolate consumed per person per year, the number of Nobel laureates per 10 million people increases by 2""",
answer="A, B",
explanation="Scientific models propose mechanisms (brain chemistry; funding, education and wealth). A regression describes a pattern in data and knows nothing about brains or funding, so it is a statistical model.",
why_wrong="C) A regression is a statistical model: it summarizes the pattern without explaining what causes it.",
hint="Which options propose a process that could produce the pattern?",
drafted_by_claude="explanation, why_wrong, hint"),

dict(id="ch13-hw-02", source="Linear models homework, Q2", topics="linear model coefficients, intercept", type="MC",
question="""I ran this code and got the output below:

lm(nobel_prizes ~ 1, data = chocolate_data)

Coefficients:
(Intercept)
     11.061

nobel_prizes is the number of Nobel laureates per 10 million people. What does the (Intercept) of 11.061 represent?""",
options="""A) The expected number of Nobel laureates per 10 million people in a country with no chocolate consumption
B) The expected chocolate consumption in a country with no Nobel laureates
C) The average chocolate consumption across countries
D) The average number of Nobel laureates per 10 million people across countries
E) The expected increase in Nobel laureates per 10 million people for each 1 kg/person increase in chocolate consumption""",
answer="D",
explanation="A model with only an intercept (~ 1) predicts the same value for everyone: the mean of the response. So 11.061 is the mean number of laureates per 10 million people across the countries in the data.",
why_wrong="""A) Chocolate isn't in this model, so the intercept can't be about 'no chocolate'.
B) and C) Chocolate consumption isn't the response.
E) That would be a slope, and this model has none.""",
hint="With nothing on the right side of ~, what is the best single prediction?",
drafted_by_claude="question (rewritten), options, explanation, why_wrong, hint", flags="Original variable name mixed 'per 100 million' with 'per 10 million' in the text; standardized to per 10 million. Dropped option F (strength of association)."),

dict(id="ch13-hw-03", source="Linear models homework, Q3", topics="linear model coefficients, intercept", type="MC",
question="""I ran this code and got the output below:

lm(nobel_prizes ~ chocolate_consumption, data = chocolate_data)

Coefficients:
          (Intercept)  chocolate_consumption
               -3.396                  2.527

nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year. According to the model, what does the (Intercept) of -3.396 represent?""",
options="""A) The expected number of Nobel laureates per 10 million people in a country with no chocolate consumption
B) The expected chocolate consumption in a country with no Nobel laureates
C) The average number of Nobel laureates per 10 million people across countries
D) The expected increase in Nobel laureates per 10 million people for each 1 kg/person increase in chocolate consumption
E) The strength of the association between chocolate consumption and Nobel laureates""",
answer="A",
explanation="The intercept is the prediction when every explanatory variable equals zero: a country eating 0 kg of chocolate. A negative number of laureates is impossible, a reminder that 0 kg is outside the data and the intercept is just where the line crosses x = 0.",
why_wrong="""B) Reverses the roles of the variables.
C) That would be the intercept of a model with no predictors.
D) That's the slope (2.527).
E) Coefficients aren't measures of strength; that's what r or R² describe.""",
hint="What value of chocolate consumption does the intercept correspond to?",
drafted_by_claude="explanation, why_wrong, hint", flags="Dropped two options to keep five."),

dict(id="ch13-hw-04", source="Linear models homework, Q4", topics="linear model coefficients, slope", type="MC",
question="""Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. I ran:

lm(nobel_prizes ~ chocolate_consumption, data = chocolate_data)

          (Intercept)  chocolate_consumption
               -3.396                  2.527

nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year. According to the model, what does the chocolate_consumption coefficient of 2.527 represent?""",
options="""A) The expected number of Nobel laureates per 10 million people in a country with no chocolate consumption
B) The average chocolate consumption across countries
C) The expected increase in Nobel laureates per 10 million people for each 1 kg/person increase in chocolate consumption
D) The strength of the association between chocolate consumption and Nobel laureates""",
answer="C",
explanation="A slope is the expected change in the response for a one-unit increase in the explanatory variable: about 2.5 more laureates per 10 million people for each extra kg of chocolate per person per year.",
why_wrong="""A) That's the intercept.
B) Not something this model estimates.
D) A slope depends on units, so it isn't a measure of strength. r or R² measure strength.""",
hint="What happens to the prediction if chocolate consumption goes up by 1?",
drafted_by_claude="options, explanation, why_wrong, hint"),

dict(id="ch13-hw-05", source="Linear models homework, Q5", topics="predictions, regression", type="numeric",
question="""Using lm(nobel_prizes ~ chocolate_consumption) with intercept -3.396 and slope 2.527, what is the predicted number of Nobel laureates (per 10 million people) for a country that eats 8 kg of chocolate per person per year?""",
answer="16.82", explanation="-3.396 + 2.527 × 8 = -3.396 + 20.216 = 16.82.",
why_wrong="Common mistake: forgetting the intercept (20.22).",
hint="Prediction = intercept + slope × x.",
drafted_by_claude="question (made self-contained), explanation, why_wrong, hint"),

dict(id="ch13-hw-06", source="Linear models homework, Q6", topics="correlation, covariance", type="numeric",
question="""Use these summaries of the chocolate data to estimate the correlation between Nobel prizes and chocolate consumption:

var_nobel | var_chocolate | cov_chocolate_nobel
104 | 10.3 | 25.9""",
answer="0.792", explanation="r = cov(x, y) / (sd(x) × sd(y)). The SDs are the square roots of the variances: √104 = 10.2 and √10.3 = 3.21. So r = 25.9 / (10.2 × 3.21) = 0.79.",
why_wrong="Common mistake: dividing by the variances instead of the SDs (25.9 / (104 × 10.3) = 0.024).",
hint="The formula needs standard deviations, but you were given variances.",
drafted_by_claude="explanation, why_wrong, hint"),

dict(id="ch13-hw-07", source="Linear models homework, Q7", topics="residuals, predictions", type="numeric",
question="""Using lm(nobel_prizes ~ chocolate_consumption) with intercept -3.396 and slope 2.527, calculate the residual for Sweden (chocolate consumption = 6.4 kg/person/year; Nobel laureates = 31.9 per 10 million people).""",
answer="19.1", explanation="Prediction = -3.396 + 2.527 × 6.4 = 12.78. Residual = observed - predicted = 31.9 - 12.78 = 19.1. Sweden has many more laureates than its chocolate consumption predicts.",
why_wrong="Common mistake: predicted - observed (-19.1).",
hint="Find Sweden's prediction first, then subtract it from what was observed.",
drafted_by_claude="question (made self-contained), explanation, why_wrong, hint", flags="Original offered a figure as an alternative; numbers are enough."),

dict(id="ch13-hw-08", source="Linear models homework, Q8", topics="residual standard deviation, model fit", type="MC",
question="""Consider two models of the same response:

model_A <- lm(nobel_prizes ~ 1, data = chocolate_data)
model_B <- lm(nobel_prizes ~ chocolate_consumption, data = chocolate_data)

model_A has a residual standard deviation of 10.2, and model_B has a residual standard deviation of 1.4. Which statement must be true?""",
options="""A) Observations fall closer to model A's predictions, on average
B) Observations fall closer to model B's predictions, on average
C) Model B is statistically significant, while model A is not
D) None of these: the residual SD can't be compared across models of the same response""",
answer="B",
explanation="The residual SD describes how far observations typically fall from the model's predictions. Smaller is closer, so model B's predictions are closer.",
why_wrong="""A) Backwards: a larger residual SD means points are farther from the predictions.
C) The residual SD alone says nothing about statistical significance.
D) Comparing residual SDs is meaningful for models of the same response (same units).""",
hint="What does a residual SD measure, in words?",
drafted_by_claude="explanation, why_wrong, hint"),

# ---------------- ChimeIn ----------------
dict(id="ch13-chimein-01", source="Chime In (linear models), Q1-3", topics="categorical predictors, predictions", type="numeric",
question="""The iris data contain flower measurements from three iris species (setosa, versicolor and virginica).

Consider this model of iris sepal length as a function of species:

lm(Sepal.Length ~ Species, data = iris)

Coefficients:
      (Intercept)  Speciesversicolor   Speciesvirginica
            5.006              0.930              1.582

What is the predicted (mean) sepal length of virginica flowers?""",
answer="6.588", explanation="setosa is the reference level, so the intercept (5.006) is the setosa mean. Add the virginica coefficient: 5.006 + 1.582 = 6.588.",
why_wrong="Common mistake: answering 1.582. That's the difference between virginica and setosa, not the virginica mean.",
hint="Which species is the reference level (it has no coefficient of its own)?",
drafted_by_claude="question (merged, stats given), explanation, why_wrong, hint", flags="Merged three ChimeIn questions (setosa, versicolor, virginica means); output added from the iris data."),

dict(id="ch13-chimein-02", source="Chime In (linear models), Q4", topics="residuals, categorical predictors", type="numeric",
question="""The iris data contain flower measurements from three iris species (setosa, versicolor and virginica).

The plot shows iris sepal lengths by species. Black lines are the species means from:

lm(Sepal.Length ~ Species, data = iris)

      (Intercept)  Speciesversicolor   Speciesvirginica
            5.006              0.930              1.582

What is the residual for data point B?""",
image="ch13-chimein-iris-AB.png",
answer="-0.788", explanation="Point B is a virginica flower with a sepal length of 5.8 cm. The model predicts the virginica mean for it: 5.006 + 1.582 = 6.588. Residual = 5.8 - 6.588 = -0.788. B sits below its species' line, so its residual is negative.",
why_wrong="Common mistakes: using the setosa mean (5.006) as B's prediction, or subtracting in the wrong order (+0.788).",
hint="Which species is B? What does the model predict for every flower of that species?"),

dict(id="ch13-chimein-03", source="Chime In (linear models), slide example (point A)", topics="residuals, categorical predictors", type="numeric",
question="""The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). The plot shows iris sepal lengths by species; black lines are the species means from lm(Sepal.Length ~ Species):

      (Intercept)  Speciesversicolor   Speciesvirginica
            5.006              0.930              1.582

What is the residual for data point A?""",
image="ch13-chimein-iris-AB.png",
answer="0.694", explanation="Point A is a setosa flower with a sepal length of 5.7 cm. Setosa is the reference level, so its prediction is the intercept, 5.006. Residual = 5.7 - 5.006 = 0.694.",
why_wrong="Common mistake: reading A's value off the wrong gridline. Each faint line is 0.1 cm.",
hint="Setosa has no coefficient of its own. What does that tell you about its prediction?"),

# ---------------- Book: Linear model summary ----------------
dict(id="ch13-book-01", source="Book: Linear model summary (Q1)", topics="scientific vs statistical models", type="MC",
question="What is the key difference between a scientific and a statistical model?",
options="""A) Statistical models make predictions, scientific models do not
B) Statistical models can be wrong, scientific models cannot
C) Statistical models describe patterns, scientific models are built on understanding processes
D) Statistical models make assumptions, scientific models do not
E) There are no differences between scientific and statistical models""",
answer="C", near_duplicate_of="ch13-hw-01",
explanation="A statistical model describes patterns in data. A scientific model proposes the process or mechanism that produces them.",
why_wrong="""A) Both kinds of models can make predictions.
B) Both can be wrong.
D) Both make assumptions.
E) The distinction is real and useful.""",
hint="Which kind of model tries to explain why the pattern exists?",
drafted_by_claude="explanation, why_wrong, hint"),

dict(id="ch13-book-02", source="Book: Linear model summary (Q2)", topics="linear model coefficients, intercept", type="MC",
question="""Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

Consider this code and output:

lm(bill_depth_mm ~ 1, penguins)

Coefficients:
(Intercept)
      17.15

The (Intercept) describes:""",
options="""A) The mean bill depth of penguins in this dataset
B) The mean bill depth of all penguins
C) The mean bill depth of penguins of the "reference level" species
D) The expected bill depth if all the predictors are set to zero""",
answer="A", near_duplicate_of="ch13-hw-02",
explanation="With only an intercept, the model's single prediction is the sample mean: the mean bill depth of the penguins in this dataset.",
why_wrong="""B) It's an estimate from this sample, not the true mean of all penguins (a parameter).
C) Species isn't in this model.
D) There are no predictors here, so there's nothing to set to zero.""",
hint="Is 17.15 calculated from a sample or from every penguin?",
drafted_by_claude="explanation, why_wrong, hint"),

dict(id="ch13-book-03", source="Book: Linear model summary (Q3)", topics="categorical predictors, reference level", type="MC",
question="Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).\n\nWithout running it, which sex will be the reference level in lm(bill_length_mm ~ sex, penguins)? The two values of sex are \"female\" and \"male\".",
options="""A) male
B) female
C) whichever has the smaller mean
D) impossible to predict""",
answer="B",
explanation="By default, R uses the first level in alphabetical order as the reference. \"female\" comes before \"male\".",
why_wrong="""A) "male" comes second alphabetically.
C) R doesn't look at the means when choosing the reference.
D) The default rule (alphabetical) makes it predictable.""",
hint="How does R order the levels of a categorical variable by default?",
drafted_by_claude="question (values added), explanation, why_wrong, hint"),

dict(id="ch13-book-04", source="Book: Linear model summary (Q4-5)", topics="categorical predictors, predictions", type="numeric",
question="""Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

Consider this output:

lm(bill_length_mm ~ species, penguins)

Coefficients:
     (Intercept)  speciesChinstrap     speciesGentoo
          38.791            10.042             8.713

What is the mean bill length of Chinstrap penguins in the dataset?""",
answer="48.833", explanation="Adelie is the reference, so 38.791 is the Adelie mean. Chinstrap mean = 38.791 + 10.042 = 48.833.",
why_wrong="Common mistake: answering 10.042, which is the Chinstrap minus Adelie difference.",
hint="Which species does the intercept describe?",
drafted_by_claude="question (merged), explanation, why_wrong, hint", flags="Merged Q4 (Adelie mean = intercept) and Q5 (Chinstrap mean)."),

dict(id="ch13-book-05", source="Book: Linear model summary (Q6)", topics="categorical predictors, coefficients", type="numeric",
question="""Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

lm(bill_length_mm ~ species, penguins)

     (Intercept)  speciesChinstrap     speciesGentoo
          38.791            10.042             8.713

How many mm longer are Chinstrap bills than Gentoo bills, on average, in this dataset?""",
answer="1.329", explanation="Both coefficients are differences from Adelie, so the Chinstrap minus Gentoo difference is 10.042 - 8.713 = 1.329. The intercept cancels out.",
why_wrong="Common mistake: answering 10.042 or 8.713. Each of those compares a species to Adelie, not to each other.",
hint="Both coefficients are measured from the same starting point.",
drafted_by_claude="question (made numeric), explanation, why_wrong, hint"),

dict(id="ch13-book-06", source="Book: Linear model summary (Q7)", topics="categorical predictors, means", type="MC",
question="""Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

Using only this output:

lm(bill_length_mm ~ species, penguins)

     (Intercept)  speciesChinstrap     speciesGentoo
          38.791            10.042             8.713

What is the mean bill length of all penguins in this dataset?""",
options="""A) 38.791
B) 19.182
C) 45.042 (the average of the three species means)
D) Not enough information""",
answer="D",
explanation="The overall mean depends on how many penguins of each species there are. The output gives the three species means but not the sample sizes, so we can't weight them.",
why_wrong="""A) That's the Adelie (reference) mean.
B) That's just the sum of the two coefficients.
C) Averaging the species means is only right if every species has the same sample size.""",
hint="Would the overall mean change if there were many more Adelie penguins than Chinstraps?",
drafted_by_claude="options, explanation, why_wrong, hint"),

dict(id="ch13-book-07", source="Book: Linear model summary (Q8)", topics="correlation, covariance", type="numeric",
question="""Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

Use these summaries to model bill depth (response) as a function of bill length (explanatory):

mean_depth | mean_length | cov | sd_depth | sd_length
17.59 | 46.57 | 0.62 | 0.78 | 3.11

(Bill depth ranges from 16.4 to 19.4 mm, bill length from 40.9 to 58 mm, n = 34.)

What is the correlation between bill depth and bill length?""",
answer="0.256", explanation="r = cov / (sd_x × sd_y) = 0.62 / (3.11 × 0.78) = 0.256.",
why_wrong="Common mistake: dividing by the variance of x (that gives the slope, 0.064).",
hint="r = cov(x, y) / (sd(x) × sd(y)).",
drafted_by_claude="explanation, why_wrong, hint"),

dict(id="ch13-book-08", source="Book: Linear model summary (Q9)", topics="regression slope, covariance", type="numeric",
question="""Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

For 34 penguins, we model bill depth (response) as a function of bill length (explanatory) using these summaries:

mean_depth | mean_length | cov | sd_depth | sd_length
17.59 | 46.57 | 0.62 | 0.78 | 3.11

What is the slope of the regression of bill depth (response) on bill length (explanatory)?""",
answer="0.0641", explanation="b = cov(x, y) / var(x) = 0.62 / 3.11² = 0.62 / 9.67 = 0.0641 mm of depth per mm of length.",
why_wrong="Common mistakes: dividing by sd(x) instead of var(x) (0.199), or using the response's variance.",
hint="b = cov(x, y) / var(x), and var(x) = sd(x)².",
drafted_by_claude="explanation, why_wrong, hint"),

dict(id="ch13-book-09", source="Book: Linear model summary (Q10)", topics="regression intercept", type="numeric",
question="""Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

For 34 penguins, mean bill depth = 17.59 mm and mean bill length = 46.57 mm. Given a slope of 0.0641, what is the intercept of the regression of bill depth on bill length?""",
answer="14.6", explanation="a = mean(y) - b × mean(x) = 17.59 - 0.0641 × 46.57 = 17.59 - 2.99 = 14.6. A regression line always passes through the point (mean x, mean y).",
why_wrong="Common mistake: using mean(x) in place of mean(y).",
hint="The line passes through (mean bill length, mean bill depth).",
drafted_by_claude="question (stats given), explanation, why_wrong, hint"),

dict(id="ch13-book-10", source="Book: Linear model summary (Q11-12)", topics="residuals, predictions", type="numeric",
question="""Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

For 34 penguins, the regression of bill depth on bill length has intercept 14.6 and slope 0.0641. A penguin has a bill 50 mm long and 20 mm deep. What is its residual (in mm)?""",
answer="2.19", explanation="Prediction = 14.6 + 0.0641 × 50 = 17.81 mm. Residual = 20 - 17.81 = 2.19 mm.",
why_wrong="Common mistake: predicted - observed (-2.19).",
hint="Predict first, then subtract the prediction from the observed depth.",
drafted_by_claude="question (merged), explanation, why_wrong, hint", flags="Merged Q11 (prediction, 17.81) and Q12 (residual)."),

dict(id="ch13-book-11", source="Book: Linear model summary (Q13)", topics="extrapolation, predictions", type="MC",
question="""Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

The regression of bill depth on bill length (intercept 14.6, slope 0.0641) was fit to penguins with bill lengths from 40.9 to 58 mm. What should we make of its prediction for a penguin with a 500 mm long bill?""",
options="""A) It's about 46.7 mm, and we can trust it because the formula gives an answer
B) It's not trustworthy: 500 mm is far outside the range of the data, so this is an extrapolation
C) The model can't produce a number for x = 500
D) It's trustworthy because the correlation is positive""",
answer="B",
explanation="The formula will happily give 14.6 + 0.0641 × 500 = 46.7 mm, but the model only describes bill lengths between about 41 and 58 mm. Nothing tells us the relationship stays a straight line (or that such a penguin could exist) far outside that range.",
why_wrong="""A) Getting a number is not the same as getting a sensible prediction.
C) The equation works for any x; the problem is whether to believe it.
D) A positive correlation within the data says nothing about values far beyond it.""",
hint="What range of bill lengths was the model built on?",
drafted_by_claude="question (made MC), options, explanation, why_wrong, hint", flags="Original numeric question used a sentinel key (any answer); turned into an extrapolation MC."),

dict(id="ch13-book-12", source="Book: Linear model summary (Q14)", topics="residuals, multiple predictors", type="numeric",
question="""Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

The figure shows bill depth vs bill length for Gentoo penguins. Solid lines are predictions from lm(bill_depth_mm ~ bill_length_mm + sex); dashed lines are separate fits for each sex.

The male penguin with a bill about 56 mm long (the second point from the right) has a bill depth of 17.0 mm. Using the solid male line, approximate its residual.""",
answer="0.68", image="ch13-book-gentoo-resid.png",
explanation="Read the solid male line at 56 mm: about 16.3 mm. Residual = 17.0 - 16.3 ≈ 0.7 mm (the model gives 16.32, so 0.68). The point sits a bit above its line.",
why_wrong="Common mistakes: using the female line, or the dashed (separate fit) line instead of the model's solid line.",
hint="Find the solid male line at 56 mm, then compare it to the point.",
drafted_by_claude="question (plot regenerated), explanation, why_wrong, hint", flags="Figure regenerated from palmerpenguins; check it against the book's version. Accept roughly 0.5 to 0.85."),

dict(id="ch13-book-13", source="Book: Linear model summary (Q15)", topics="multiple predictors, slopes", type="select-all",
question="""Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

The figure shows Gentoo bill depth vs bill length, with solid lines from lm(bill_depth_mm ~ bill_length_mm + sex) and dashed lines from separate fits for each sex. Which of the following are nearly identical for male and female Gentoo penguins? (Select all that apply.)""",
image="ch13-book-gentoo-resid.png",
options="""A) Mean bill lengths
B) Mean bill depths
C) Slopes
D) Intercepts""",
answer="C",
explanation="The separate (dashed) lines for males and females are nearly parallel, so the slopes are similar. Males sit higher (deeper bills) and to the right (longer bills), so means and intercepts differ.",
why_wrong="""A) and B) The male points are shifted right and up: males have longer and deeper bills.
D) The lines are parallel but offset vertically, so their intercepts differ.""",
hint="Compare the dashed lines: are they parallel? Are they on top of each other?",
drafted_by_claude="explanation, why_wrong, hint", flags="Dropped option E ('nearly nothing is identical')."),

dict(id="ch13-book-14", source="Book: Linear model summary (Q16)", topics="residuals, sums of squares, residual standard deviation", type="numeric",
question="""Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo).

For Chinstrap penguins, lm(flipper_length_mm ~ body_mass_g + sex) has a residual standard error of 5.186 on 65 degrees of freedom. What is the sum of squared residuals?""",
answer="1748", explanation="Residual SE = √(sum of squares / df). So sum of squares = SE² × df = 5.186² × 65 = 26.89 × 65 = 1748.",
why_wrong="Common mistake: SE × df (337), forgetting to square.",
hint="Undo the square root, then undo the division by df.",
drafted_by_claude="question (stats given), explanation, why_wrong, hint", flags="Original required running the model in R; now gives the residual SE and df."),
]
