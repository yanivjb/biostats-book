from ai_helpers import V, r
HAM = "Orange juice increases tooth growth, so researchers asked whether vitamin C alone does the job: they gave hamsters vitamin C at Dose A (0.5 mg/day), Dose B (1 mg/day) or Dose C (2 mg/day), either in water (SuppVC) or as orange juice (OJ). The linear model is:\n\ntooth_length = 12.45 - 3.70 × SuppVC + 9.13 × DOSE_B + 15.50 × DOSE_C\n\n(SuppVC, DOSE_B and DOSE_C are 1 if true and 0 otherwise; orange juice and Dose A are the reference levels.)"
FISH = "To ask whether fishing makes fish populations more variable, a model compared the year-to-year coefficient of variation (cv) in larval abundance of exploited and unexploited fish species, adjusting for age at maturation: lm(cv ~ exploited + age)."
CHOC = "Messerli (2012) found that countries with higher chocolate consumption tend to have more Nobel Prize winners. nobel_prizes is Nobel laureates per 10 million people; chocolate_consumption is kg per person per year."
CHOC_FIT = "lm(nobel_prizes ~ chocolate_consumption, data = chocolate_data)\n\n          (Intercept)  chocolate_consumption\n               -3.396                  2.527"
IRIS = "The iris data contain flower measurements from three iris species (setosa, versicolor and virginica)."
IRIS_FIT = "lm(Sepal.Length ~ Species, data = iris)\n\n      (Intercept)  Speciesversicolor   Speciesvirginica\n            5.006              0.930              1.582"
PEN = "Palmer penguins data: bill and body measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo)."
PEN_SP = "lm(bill_length_mm ~ species, penguins)\n\n     (Intercept)  speciesChinstrap     speciesGentoo\n          38.791            10.042             8.713"

ROWS = [
V("ch13-quiz-01", 1,
question=HAM + "\n\nIf dose had instead been entered as a number (0.5, 1, 2), what would the model assume that the categorical version does not?",
options="""A) That tooth length changes by the same amount for every extra mg of vitamin C
B) That orange juice and water have the same effect at every dose of vitamin C
C) That every hamster in a dose group has exactly the same tooth length
D) That the dose effects must be estimated separately for OJ and for water""",
answer="A", explanation="A numeric dose gets one slope: the same change in tooth length per mg everywhere. As a category, each dose gets its own mean, so the dose-response can have any shape.",
why_wrong="""B) Both versions are additive, so both assume the supplement effect is the same at every dose.
C) Neither version assumes no variation within groups.
D) Neither version has a dose × supplement interaction.""",
hint="What does a single slope imply about going from 0.5 to 1 mg versus 1 to 2 mg?"),
V("ch13-quiz-01", 2,
question="A plant biologist grows seedlings at three fertilizer levels (low, medium, high) and fits lm(height ~ fertilizer), with fertilizer as a categorical variable. Compared with treating fertilizer as a number (1, 2, 3), what does this choice allow?",
options="""A) Each fertilizer level gets its own mean, so height need not change by equal steps
B) The model estimates a single slope for the change in height per fertilizer level
C) The model no longer needs a reference level or an intercept to make predictions
D) The predictions are guaranteed to be identical to those from the numeric version""",
answer="A", explanation="A categorical predictor gives each level its own coefficient (relative to the reference), so the model doesn't assume a straight-line, equal-step response.",
why_wrong="""B) That's what the numeric version does.
C) Categorical predictors still use a reference level and intercept.
D) Predictions match only if the true means happen to fall on a straight line.""",
hint="One slope, or one mean per level?"),

V("ch13-quiz-02", 1, question=HAM + "\n\nWhat is the predicted mean tooth length for a hamster given Dose B (1 mg/day) of orange juice?",
answer=r(12.45+9.13), explanation="OJ is the reference (SuppVC = 0) and DOSE_B = 1: 12.45 + 9.13 = 21.58.", hint="Which indicator variables equal 1 for OJ at Dose B?"),
V("ch13-quiz-02", 2, question=HAM + "\n\nWhat is the predicted mean tooth length for a hamster given Dose A (0.5 mg/day) of vitamin C in water (SuppVC)?",
answer=r(12.45-3.70), explanation="SuppVC = 1 and Dose A is the reference (DOSE_B = DOSE_C = 0): 12.45 - 3.70 = 8.75.", hint="Dose A is a reference level; SuppVC is not."),

V("ch13-quiz-03", 1, question=HAM + "\n\nWhat is the predicted mean tooth length for a hamster given Dose B (1 mg/day) of vitamin C in water (SuppVC)?",
answer=r(12.45-3.70+9.13), explanation="SuppVC = 1 and DOSE_B = 1: 12.45 - 3.70 + 9.13 = 17.88.", hint="Add every coefficient whose indicator is 1."),
V("ch13-quiz-03", 2, question=HAM + "\n\nWhat is the predicted mean tooth length for a hamster given Dose C (2 mg/day) of orange juice?",
answer=r(12.45+15.50), explanation="OJ is the reference (SuppVC = 0) and DOSE_C = 1: 12.45 + 15.50 = 27.95.", hint="Which indicators are 1 for OJ at Dose C?"),

V("ch13-quiz-04", 1, question=HAM + "\n\nA hamster given Dose B (1 mg/day) of orange juice had a tooth length of 23.00. What is its residual?",
answer=r(23-(12.45+9.13)), explanation="Prediction = 12.45 + 9.13 = 21.58. Residual = observed - predicted = 23.00 - 21.58 = 1.42.", hint="Residual = observed - predicted."),
V("ch13-quiz-04", 2, question=HAM + "\n\nA hamster given Dose C (2 mg/day) of vitamin C in water (SuppVC) had a tooth length of 22.50. What is its residual?",
answer=r(22.5-(12.45-3.70+15.50)), explanation="Prediction = 12.45 - 3.70 + 15.50 = 24.25. Residual = 22.50 - 24.25 = -1.75. Negative: shorter than predicted.", hint="Residual = observed - predicted."),

V("ch13-quiz-05", 1,
question="Researchers ask whether fishing changes the year-to-year coefficient of variation (cv) in larval abundance. They compare exploited and unexploited species, and they want to adjust for body size at maturation (size), which also affects cv. Which model matches this design?",
options="""A) lm(cv ~ exploited + size)
B) lm(size ~ cv + exploited)
C) lm(exploited ~ cv + size)
D) lm(cv ~ size)""",
answer="A", explanation="cv is the response, so it goes on the left. Exploitation status (the question of interest) and size (the variable we adjust for) both go on the right.",
why_wrong="""B) and C) put the wrong variable as the response.
D) leaves out exploitation, the variable we care about.""", hint="Which variable is being explained?"),
V("ch13-quiz-05", 2,
question="A study asks whether exploited fish species have more variable larval populations (cv) than unexploited ones, after adjusting for age at maturation (age). A student fits lm(cv ~ exploited). What is wrong with this model for the study's question?",
options="""A) It leaves out age, so it does not adjust for age at maturation
B) It puts cv as the response when exploited should be the response
C) It should include age instead of exploited as the only predictor
D) Nothing; the adjustment happens automatically in lm()""",
answer="A", explanation="To adjust for age at maturation, age must be in the model: lm(cv ~ exploited + age).",
why_wrong="""B) cv is the response in this design.
C) Dropping exploited removes the variable of interest.
D) lm() only adjusts for variables you include.""", hint="Which variable from the design is missing?"),

V("ch13-quiz-06", 1,
question=FISH + " Fill in the blanks:\n\n1. The ____ is found by squaring each residual and adding them up.\n2. Dividing that by the residual degrees of freedom gives the ____.\n3. Taking the square root of that gives the ____.",
options="""A) residual standard deviation
B) residual sum of squares
C) mean square residual""",
answer="1-B, 2-C, 3-A", explanation="Sum of squares → divide by df → mean square (the residual variance) → square root → residual standard deviation.",
why_wrong="Follow the order: square and sum, then average, then take the root.", hint="Which one is in the original units of cv?"),
V("ch13-quiz-06", 2,
question=FISH + " The model's residual sum of squares is 2.45, with 25 degrees of freedom. Match each value to what it is:\n\n1. 2.45\n2. 0.098\n3. 0.313",
options="""A) The residual standard deviation (√0.098)
B) The residual sum of squares
C) The mean square residual (2.45 / 25)""",
answer="1-B, 2-C, 3-A", explanation="2.45 is the sum of squared residuals; 2.45 / 25 = 0.098 is the mean square; √0.098 = 0.313 is the residual SD.",
why_wrong="Each value is calculated from the one before it.", hint="Start from the sum of squares."),

V("ch13-quiz-07", 1, question=FISH + " The model has a residual sum of squares of 2.45 and 25 residual degrees of freedom. What is the mean square residual?",
answer=r(2.45/25,3), explanation="Mean square = sum of squares / df = 2.45 / 25 = 0.098.", hint="Divide the sum of squares by its degrees of freedom."),
V("ch13-quiz-07", 2, question=FISH + " The model has a mean square residual of 0.098 with 25 residual degrees of freedom. What is the residual sum of squares?",
answer=r(0.098*25,2), explanation="Sum of squares = mean square × df = 0.098 × 25 = 2.45.", hint="Mean square = SS / df, so SS = mean square × df."),

V("ch13-quiz-08", 1, image="ch13-quiz-fish.png",
question="The plot shows the coefficient of variation (cv) in larval abundance for exploited and unexploited fish species, against age at maturation. The model is lm(cv ~ exploited + age), where exploited is \"yes\" or \"no\" (\"no\" is the reference level). What sign should the exploitedyes and age coefficients have?",
options="""A) exploitedyes positive; age negative
B) exploitedyes negative; age negative
C) exploitedyes positive; age positive
D) exploitedyes negative; age positive""",
answer="A", explanation="At any given age, exploited species sit higher (positive exploitedyes). Within each group cv falls as age at maturation increases (negative age slope).",
why_wrong="Compare the groups at the same age, then look at the trend within a group.", hint="Which group is higher? Which way does each cloud slope?"),
V("ch13-quiz-08", 2, image="ch13-quiz-fish.png",
question="The plot shows the coefficient of variation (cv) in larval abundance for exploited and unexploited fish species, against age at maturation, with lines from lm(cv ~ exploited + age). What feature of the model makes the two lines parallel?",
options="""A) The model is additive: one age slope is shared by both groups
B) The exploited coefficient is positive, so the lines never cross
C) Age at maturation was measured the same way in both groups
D) The residual standard deviation is the same for both groups""",
answer="A", explanation="With no interaction, both groups share one age slope; exploited only shifts the line up or down.",
why_wrong="""B) A positive shift alone doesn't make lines parallel; a shared slope does.
C) Measurement method doesn't determine the slope.
D) Equal residual spread doesn't make lines parallel.""", hint="How many age slopes does lm(cv ~ exploited + age) estimate?"),

V("ch13-quiz-09", 1, question=FISH + " The fitted model is (exploitedyes = 1 for exploited species, 0 otherwise):\n\ncv = 1.25 + 0.45 × exploitedyes - 0.04 × age\n\nWhat is the predicted cv for an unexploited species that matures at 5 years?",
answer=r(1.25-0.04*5), explanation="1.25 + 0.45 × 0 - 0.04 × 5 = 1.25 - 0.20 = 1.05.", hint="exploitedyes = 0 for unexploited species."),
V("ch13-quiz-09", 2, question=FISH + " The fitted model is (exploitedyes = 1 for exploited species, 0 otherwise):\n\ncv = 1.25 + 0.45 × exploitedyes - 0.04 × age\n\nWhat is the predicted cv for an exploited species that matures at 10 years?",
answer=r(1.25+0.45-0.04*10), explanation="1.25 + 0.45 - 0.04 × 10 = 1.70 - 0.40 = 1.30.", hint="Plug in exploitedyes = 1 and age = 10."),

V("ch13-hw-01", 1,
question=CHOC + " Which of the following are statistical (not scientific) models? (Select all that apply.)",
options="""A) A regression of Nobel laureates per 10 million people on chocolate consumption
B) An idea that flavonoids in chocolate improve memory, boosting scientific output
C) A correlation coefficient describing how chocolate and Nobel prizes covary
D) An idea that wealthy countries both fund science and buy more luxuries like chocolate""",
answer="A, C", explanation="Regressions and correlations describe patterns in data. Ideas about flavonoids or wealth propose mechanisms, so they are scientific models.",
why_wrong="""B) and D) propose processes: scientific models.""", hint="Does it describe a pattern, or propose a process?"),
V("ch13-hw-01", 2,
question=CHOC + " Which of the following are scientific models? (Select all that apply. A scientific model need not be correct.)",
options="""A) Chocolate makes people happier, and happier scientists do more creative work
B) A scatterplot with a best-fit line through the country-level data points
C) Richer countries spend more on both research and luxury foods like chocolate""",
answer="A, C", explanation="A and C propose processes (happiness; wealth). A best-fit line describes a pattern, so it's a statistical model.",
why_wrong="B) A fitted line describes a pattern; it says nothing about why.", hint="Which ones explain why?"),

V("ch13-hw-02", 1,
question=CHOC + "\n\nlm(chocolate_consumption ~ 1, data = chocolate_data)\n\nCoefficients:\n(Intercept)\n      4.63\n\nWhat does the (Intercept) of 4.63 represent?",
options="""A) The expected chocolate consumption in a country with no Nobel laureates
B) The average chocolate consumption (kg/person/year) across countries
C) The average number of Nobel laureates per 10 million people
D) The increase in chocolate consumption per extra Nobel laureate""",
answer="B", explanation="A model with only an intercept predicts the mean of the response for everyone. Here the response is chocolate consumption.",
why_wrong="""A) There's no predictor here, so nothing is set to zero.
C) Nobel prizes aren't in this model.
D) There's no slope in an intercept-only model.""", hint="What does ~ 1 predict for every country?"),
V("ch13-hw-02", 2,
question=CHOC + " Which code produces a model whose only coefficient is the mean number of Nobel laureates per 10 million people across countries?",
options="""A) lm(nobel_prizes ~ 1, data = chocolate_data)
B) lm(nobel_prizes ~ chocolate_consumption, data = chocolate_data)
C) lm(chocolate_consumption ~ 1, data = chocolate_data)
D) lm(1 ~ nobel_prizes, data = chocolate_data)""",
answer="A", explanation="~ 1 fits an intercept only, and the intercept-only model's estimate is the mean of the response.",
why_wrong="""B) That also fits a slope.
C) That gives mean chocolate consumption.
D) The response must be on the left.""", hint="Response on the left; ~ 1 means 'intercept only'."),

V("ch13-hw-03", 1,
question=CHOC + "\n\n" + CHOC_FIT + "\n\nWhy is the intercept (-3.396) negative, even though a country can't have negative Nobel laureates?",
options="""A) It's the prediction at 0 kg of chocolate, far outside the data
B) Countries with no chocolate truly lose Nobel laureates on average
C) The model must have been fit to the data incorrectly
D) Intercepts are always negative when the slope is positive""",
answer="A", explanation="The intercept is where the line crosses chocolate = 0. No country in the data eats 0 kg, so this is an extrapolation and needn't make biological sense.",
why_wrong="""B) Laureate counts can't be negative.
C) The fit can be correct; it's just extrapolated.
D) Sign of the intercept doesn't depend on the slope's sign.""", hint="What value of chocolate consumption does the intercept correspond to?"),
V("ch13-hw-03", 2,
question=CHOC + "\n\n" + CHOC_FIT + "\n\nWhat does the model predict for a country with 0 kg of chocolate consumption per person per year?",
options="""A) 2.527 laureates per 10 million people
B) -3.396 laureates per 10 million people
C) The mean number of laureates across countries
D) 0 laureates per 10 million people""",
answer="B", explanation="At chocolate = 0, the prediction is just the intercept: -3.396. Impossible in reality, showing the danger of predicting outside the data.",
why_wrong="""A) That's the slope.
C) That's what an intercept-only model would give.
D) The line doesn't pass through the origin.""", hint="Set chocolate_consumption to 0."),

V("ch13-hw-04", 1,
question=CHOC + "\n\n" + CHOC_FIT + "\n\nAccording to the model, how do two countries that differ by 2 kg of chocolate per person per year differ in Nobel laureates?",
options="""A) By about 2.53 laureates per 10 million people
B) By about 5.05 laureates per 10 million people
C) By about 1.65 laureates per 10 million people
D) By about 6.79 laureates per 10 million people""",
answer="B", explanation="The slope is 2.527 laureates per kg, so 2 kg → 2 × 2.527 = 5.05.",
why_wrong="""A) That's the difference for 1 kg.
C) That adds the intercept to the slope.
D) That's 2 × 3.396, the intercept, not the slope.""", hint="Slope × difference in x."),
V("ch13-hw-04", 2,
question=CHOC + "\n\n" + CHOC_FIT + "\n\nWhich statement correctly interprets the slope of 2.527?",
options="""A) Eating 1 kg more chocolate causes 2.527 more Nobel laureates per 10 million
B) Countries eating 1 kg more chocolate have about 2.527 more laureates per 10 million
C) 2.527 is the correlation between chocolate consumption and Nobel laureates
D) 2.527 is the number of Nobel laureates in a country that eats no chocolate""",
answer="B", explanation="The slope describes the expected difference in the response per one-unit difference in the explanatory variable. These are observational data, so it says nothing about cause.",
why_wrong="""A) A regression of observational data can't show causation.
C) A slope is not a correlation (it has units).
D) That's the intercept.""", hint="Slopes describe associations, in the units of the data."),

V("ch13-hw-05", 1, question=CHOC + "\n\n" + CHOC_FIT + "\n\nWhat is the predicted number of Nobel laureates (per 10 million people) for a country that eats 5 kg of chocolate per person per year?",
answer=r(-3.396+2.527*5,2), explanation="-3.396 + 2.527 × 5 = -3.396 + 12.635 = 9.24.", hint="Intercept + slope × 5."),
V("ch13-hw-05", 2, question=CHOC + "\n\n" + CHOC_FIT + "\n\nWhat is the predicted number of Nobel laureates (per 10 million people) for a country that eats 10 kg of chocolate per person per year?",
answer=r(-3.396+2.527*10,2), explanation="-3.396 + 2.527 × 10 = -3.396 + 25.27 = 21.87.", hint="Intercept + slope × 10."),

V("ch13-hw-06", 1, question=CHOC + " Use these summaries to find the slope of the regression of Nobel prizes (response) on chocolate consumption (explanatory):\n\nvar_nobel | var_chocolate | cov_chocolate_nobel\n104 | 10.3 | 25.9",
answer=r(25.9/10.3,2), explanation="Slope = cov(x, y) / var(x) = 25.9 / 10.3 = 2.51 laureates per kg (close to the fitted 2.527, which used unrounded values).", hint="Divide the covariance by the variance of the explanatory variable."),
V("ch13-hw-06", 2, question="For 20 lakes, the variance of water temperature is 16, the variance of algal density is 25, and their covariance is 12. What is the correlation between temperature and algal density?",
answer=r(12/(4*5),2), explanation="r = cov / (sd_x × sd_y) = 12 / (√16 × √25) = 12 / (4 × 5) = 0.60.", hint="Take square roots of the variances first."),

V("ch13-hw-07", 1, question=CHOC + "\n\n" + CHOC_FIT + "\n\nCalculate the residual for Switzerland (chocolate consumption = 12.0 kg/person/year; Nobel laureates = 31.5 per 10 million people).",
answer=r(31.5-(-3.396+2.527*12),2), explanation="Prediction = -3.396 + 2.527 × 12 = 26.93. Residual = 31.5 - 26.93 = 4.58.", hint="Residual = observed - predicted."),
V("ch13-hw-07", 2, question=CHOC + "\n\n" + CHOC_FIT + "\n\nCalculate the residual for a country that eats 4.0 kg of chocolate per person per year and has 2.0 Nobel laureates per 10 million people.",
answer=r(2.0-(-3.396+2.527*4),2), explanation="Prediction = -3.396 + 2.527 × 4 = 6.71. Residual = 2.0 - 6.71 = -4.71: fewer laureates than predicted.", hint="Residual = observed - predicted."),

V("ch13-hw-08", 1,
question=CHOC + " Two models of Nobel prizes:\n\nmodel_A <- lm(nobel_prizes ~ 1, data = chocolate_data)\nmodel_B <- lm(nobel_prizes ~ chocolate_consumption, data = chocolate_data)\n\nmodel_A has a residual standard deviation of 10.2 and model_B of 6.1. What does this tell us?",
options="""A) Data points fall closer, on average, to model B's predictions
B) Data points fall closer, on average, to model A's predictions
C) Chocolate consumption causes differences in Nobel prizes
D) Model A is statistically significant, while model B is not""",
answer="A", explanation="Smaller residual SD = observations closer to the predictions.",
why_wrong="""B) Larger residual SD means farther.
C) Fit doesn't show causation.
D) Residual SD isn't a significance test.""", hint="What does the residual SD measure?"),
V("ch13-hw-08", 2,
question=CHOC + " For lm(nobel_prizes ~ chocolate_consumption), the residual standard deviation is 6.1 laureates per 10 million. What does this mean?",
options="""A) A country's laureate count is typically about 6 away from the model's prediction
B) Each extra kg of chocolate predicts about 6.1 more laureates per 10 million
C) The model explains about 61% of the variation in Nobel laureates
D) The standard deviation of chocolate consumption across countries is 6.1""",
answer="A", explanation="The residual SD is roughly the typical distance between observations and the model's predictions, in units of the response.",
why_wrong="""B) That's a slope.
C) That's R², not the residual SD.
D) The residual SD is about the response, not the explanatory variable.""", hint="Residuals are observed minus predicted."),

V("ch13-chimein-01", 1, question=IRIS + "\n\n" + IRIS_FIT + "\n\nWhat is the predicted (mean) sepal length of versicolor flowers?",
answer=r(5.006+0.930,3), explanation="setosa is the reference (intercept 5.006). versicolor: 5.006 + 0.930 = 5.936.", hint="Intercept + the versicolor coefficient."),
V("ch13-chimein-01", 2, question=IRIS + "\n\n" + IRIS_FIT + "\n\nHow much longer are virginica sepals than versicolor sepals, on average?",
answer=r(1.582-0.930,3), explanation="Both coefficients are differences from setosa, so virginica - versicolor = 1.582 - 0.930 = 0.652.", hint="The intercept cancels out."),

V("ch13-chimein-02", 1, image="ch13-chimein-iris-AB.png",
question=IRIS + "\n\nThe plot shows iris sepal lengths by species. Black lines are the species means from:\n\n" + IRIS_FIT + "\n\nWhat is the model's predicted value (fitted value) for data point B?",
answer=r(5.006+1.582,3), explanation="Point B is a virginica flower, so its prediction is the virginica mean: 5.006 + 1.582 = 6.588.", hint="Every flower of a species gets the same prediction."),
V("ch13-chimein-02", 2, image="ch13-chimein-iris-AB.png",
question=IRIS + "\n\nThe plot shows iris sepal lengths by species. Black lines are the species means from:\n\n" + IRIS_FIT + "\n\nData point B has a sepal length of 5.8 cm. Is its residual positive or negative, and how big is it?",
answer=r(5.8-6.588,3), explanation="B is virginica: predicted 6.588. Residual = 5.8 - 6.588 = -0.788. Negative, because B is below its species' line.", hint="Residual = observed - the virginica mean."),

V("ch13-chimein-03", 1, image="ch13-chimein-iris-AB.png",
question=IRIS + " The plot shows iris sepal lengths by species; black lines are the species means from lm(Sepal.Length ~ Species):\n\n      (Intercept)  Speciesversicolor   Speciesvirginica\n            5.006              0.930              1.582\n\nWhat is the model's predicted value for data point A?",
answer="5.006", explanation="Point A is a setosa flower. Setosa is the reference level, so its prediction is the intercept, 5.006.", hint="Which species is the reference level?"),
V("ch13-chimein-03", 2, image="ch13-chimein-iris-AB.png",
question=IRIS + " The plot shows iris sepal lengths by species; black lines are the species means from lm(Sepal.Length ~ Species):\n\n      (Intercept)  Speciesversicolor   Speciesvirginica\n            5.006              0.930              1.582\n\nPoint A has a sepal length of 5.7 cm. What would its residual be if it were a versicolor flower instead of setosa?",
answer=r(5.7-5.936,3), explanation="The versicolor prediction is 5.006 + 0.930 = 5.936, so the residual would be 5.7 - 5.936 = -0.236.", hint="Use the versicolor mean as the prediction."),

V("ch13-book-01", 1,
question="A researcher says, \"Warmer water speeds up fish metabolism, so fish in warm lakes grow faster.\" Another fits lm(growth ~ temperature). Which is the scientific model and which is the statistical model?",
options="""A) The metabolism idea is scientific; the lm() is statistical
B) The lm() is scientific; the metabolism idea is statistical
C) Both are statistical models of the same pattern
D) Both are scientific models of the same process""",
answer="A", explanation="The metabolism idea proposes a process. The regression describes a pattern in the data.",
why_wrong="Scientific models explain how; statistical models describe what the data look like.", hint="Which one proposes a mechanism?"),
V("ch13-book-01", 2,
question="Which statement about scientific and statistical models is true?",
options="""A) Statistical models describe patterns; scientific models propose processes
B) Scientific models are always correct; statistical models can be wrong
C) Only statistical models can be used to make predictions about data
D) Only scientific models make assumptions about the world""",
answer="A", explanation="Statistical models summarize patterns in data; scientific models are built on ideas about the processes that generate them. Both can be wrong, make predictions and rest on assumptions.",
why_wrong="""B) Both can be wrong.
C) Scientific models make predictions too.
D) Statistical models have assumptions too.""", hint="Pattern vs process."),

V("ch13-book-02", 1,
question=PEN + "\n\nlm(flipper_length_mm ~ 1, penguins)\n\nCoefficients:\n(Intercept)\n      200.9\n\nThe (Intercept) describes:",
options="""A) The mean flipper length of the penguins in this dataset
B) The mean flipper length of all penguins in the world
C) The mean flipper length of the reference-level species
D) The expected flipper length when body mass is zero""",
answer="A", explanation="An intercept-only model predicts the sample mean of the response.",
why_wrong="""B) It's an estimate from a sample, not the population value.
C) No species term is in the model.
D) No body mass term is in the model.""", hint="What does ~ 1 estimate?"),
V("ch13-book-02", 2,
question=PEN + "\n\nlm(bill_depth_mm ~ 1, penguins) gives an intercept of 17.15. What would the model predict for the bill depth of a Gentoo penguin with a 50 mm bill?",
options="""A) 17.15 mm, the same prediction as for any penguin
B) It can't predict, since species isn't in the model
C) 17.15 mm plus the Gentoo species coefficient
D) 17.15 mm plus 50 times the bill length slope""",
answer="A", explanation="With no predictors, every penguin gets the same prediction: the sample mean, 17.15 mm.",
why_wrong="""B) It can predict; it just ignores species.
C) and D) There are no species or bill length terms in this model.""", hint="How many different predictions can an intercept-only model make?"),

V("ch13-book-03", 1,
question=PEN + "\n\nWithout running it, which species will be the reference level in lm(bill_length_mm ~ species, penguins)? The species are Adelie, Chinstrap and Gentoo.",
options="""A) Adelie
B) Chinstrap
C) Gentoo
D) Whichever species has the most penguins""",
answer="A", explanation="By default R uses the first level alphabetically. Adelie comes first.",
why_wrong="Sample size and means don't set the default reference.", hint="Alphabetical order."),
V("ch13-book-03", 2,
question=PEN + "\n\nPenguins were sampled on three islands: Biscoe, Dream and Torgersen. Without running it, which island will be the reference level in lm(body_mass_g ~ island, penguins)?",
options="""A) Biscoe
B) Dream
C) Torgersen
D) Whichever island has the lightest penguins""",
answer="A", explanation="R uses the first level alphabetically as the reference: Biscoe.",
why_wrong="Means don't set the default reference level.", hint="Alphabetical order."),

V("ch13-book-04", 1, question=PEN + "\n\n" + PEN_SP + "\n\nWhat is the mean bill length of Gentoo penguins in the dataset?",
answer=r(38.791+8.713,3), explanation="Adelie is the reference (38.791). Gentoo = 38.791 + 8.713 = 47.504.", hint="Intercept + the Gentoo coefficient."),
V("ch13-book-04", 2, question=PEN + "\n\n" + PEN_SP + "\n\nWhat is the mean bill length of Adelie penguins in the dataset?",
answer="38.791", explanation="Adelie is the reference level, so its mean is the intercept: 38.791.", hint="Which species has no coefficient of its own?"),

V("ch13-book-05", 1, question=PEN + "\n\n" + PEN_SP + "\n\nHow many mm longer are Gentoo bills than Adelie bills, on average, in this dataset?",
answer="8.713", explanation="Adelie is the reference, so the Gentoo coefficient (8.713) is exactly the Gentoo - Adelie difference.", hint="What does a coefficient for a non-reference level measure?"),
V("ch13-book-05", 2, question=PEN + "\n\n" + PEN_SP + "\n\nHow many mm shorter are Gentoo bills than Chinstrap bills, on average, in this dataset?",
answer=r(10.042-8.713,3), explanation="Chinstrap - Gentoo = 10.042 - 8.713 = 1.329 mm. The intercept cancels.", hint="Subtract the two coefficients."),

V("ch13-book-06", 1,
question=PEN + "\n\n" + PEN_SP + "\n\nThe dataset has 151 Adelie, 68 Chinstrap and 123 Gentoo penguins. Why isn't the overall mean bill length simply the average of the three species means?",
options="""A) The species have different sample sizes, so their means need weighting
B) The intercept is already the mean bill length of all the penguins
C) Species means can't be combined because they come from a model
D) It is; the overall mean always equals the average of group means""",
answer="A", explanation="The overall mean weights each species by its number of penguins. Adelie (151) counts more than Chinstrap (68).",
why_wrong="""B) The intercept is the Adelie mean.
C) Model-based group means are just the sample means here.
D) Only true when groups are the same size.""", hint="Each penguin counts once."),
V("ch13-book-06", 2,
question=PEN + "\n\n" + PEN_SP + "\n\nWhich of these can you calculate using ONLY this output?",
options="""A) The mean bill length of Gentoo penguins
B) The mean bill length of all penguins
C) The number of Chinstrap penguins sampled
D) The standard deviation of Adelie bills""",
answer="A", explanation="Gentoo mean = 38.791 + 8.713. The overall mean needs sample sizes; counts and SDs aren't in the coefficients.",
why_wrong="""B) Needs the sample size of each species.
C) and D) Coefficients don't report counts or spread.""", hint="Coefficients give group means, nothing more."),

V("ch13-book-07", 1, question=PEN + "\n\nFor 34 penguins:\n\nmean_depth | mean_length | cov | sd_depth | sd_length\n17.59 | 46.57 | 0.62 | 0.78 | 3.11\n\nWhat is the variance of bill length?",
answer=r(3.11**2,2), explanation="Variance = SD² = 3.11² = 9.67.", hint="Square the SD."),
V("ch13-book-07", 2, question="For 40 lizards, the covariance between body length and sprint speed is 1.2, the SD of body length is 2.0 and the SD of sprint speed is 1.5. What is the correlation between body length and sprint speed?",
answer=r(1.2/(2*1.5),2), explanation="r = cov / (sd_x × sd_y) = 1.2 / (2.0 × 1.5) = 0.40.", hint="Divide the covariance by the product of the SDs."),

V("ch13-book-08", 1, question=PEN + "\n\nFor 34 penguins, we model bill length (response) as a function of bill depth (explanatory):\n\nmean_depth | mean_length | cov | sd_depth | sd_length\n17.59 | 46.57 | 0.62 | 0.78 | 3.11\n\nWhat is the slope of the regression of bill LENGTH on bill DEPTH?",
answer=r(0.62/0.78**2,2), explanation="b = cov / var(x). Now depth is x: 0.62 / 0.78² = 0.62 / 0.608 = 1.02 mm of length per mm of depth.", hint="Divide by the variance of the explanatory variable (depth)."),
V("ch13-book-08", 2, question="For 40 lizards, the covariance between body length (explanatory) and sprint speed (response) is 1.2, and the SD of body length is 2.0. What is the slope of the regression of sprint speed on body length?",
answer=r(1.2/4,2), explanation="b = cov / var(x) = 1.2 / 2.0² = 1.2 / 4 = 0.30.", hint="var(x) = SD²."),

V("ch13-book-09", 1, question=PEN + "\n\nFor 34 penguins, mean bill depth = 17.59 mm and mean bill length = 46.57 mm. The regression of bill depth on bill length has slope 0.0641. What does the model predict for a penguin with an average bill length (46.57 mm)?",
answer="17.59", explanation="A regression line always passes through (mean x, mean y), so the prediction at mean length is mean depth: 17.59 mm.", hint="Where does every regression line pass?"),
V("ch13-book-09", 2, question="For 40 lizards, mean body length is 10 cm and mean sprint speed is 5 m/s. The regression of sprint speed on body length has slope 0.30. What is the intercept?",
answer=r(5-0.3*10,2), explanation="a = mean(y) - b × mean(x) = 5 - 0.30 × 10 = 2.0.", hint="The line passes through (mean x, mean y)."),

V("ch13-book-10", 1, question=PEN + "\n\nFor 34 penguins, the regression of bill depth on bill length has intercept 14.6 and slope 0.0641. A penguin has a bill 45 mm long and 16.5 mm deep. What is its residual (in mm)?",
answer=r(16.5-(14.6+0.0641*45),2), explanation="Prediction = 14.6 + 0.0641 × 45 = 17.48. Residual = 16.5 - 17.48 = -0.98.", hint="Residual = observed - predicted."),
V("ch13-book-10", 2, question=PEN + "\n\nFor 34 penguins, the regression of bill depth on bill length has intercept 14.6 and slope 0.0641. What bill depth does the model predict for a penguin with a 55 mm bill?",
answer=r(14.6+0.0641*55,2), explanation="14.6 + 0.0641 × 55 = 14.6 + 3.53 = 18.13 mm.", hint="Intercept + slope × length."),

V("ch13-book-11", 1,
question=PEN + "\n\nThe regression of bill depth on bill length (intercept 14.6, slope 0.0641) was fit to penguins with bill lengths from 40.9 to 58 mm. Which prediction is most trustworthy?",
options="""A) The prediction for a bill 50 mm long
B) The prediction for a bill 5 mm long
C) The prediction for a bill 100 mm long
D) They are all equally trustworthy""",
answer="A", explanation="50 mm lies within the data (40.9 to 58 mm). The others are extrapolations.",
why_wrong="""B) and C) are far outside the data.
D) Predictions outside the data range are not trustworthy.""", hint="Which one is inside the range of the data?"),
V("ch13-book-11", 2,
question=PEN + "\n\nThe regression of bill depth on bill length (intercept 14.6, slope 0.0641) was fit to penguins with bill lengths from 40.9 to 58 mm. Why shouldn't we interpret the intercept (14.6 mm) as the bill depth of a penguin with no bill?",
options="""A) A bill length of 0 mm is far outside the data, so it's an extrapolation
B) The intercept is the mean bill depth, not a prediction for any penguin
C) The intercept is only meaningful when the slope is negative
D) We should; 14.6 mm is the expected depth of a bill 0 mm long""",
answer="A", explanation="The intercept is the prediction at x = 0, which is far outside the observed bill lengths, so it has no biological meaning here.",
why_wrong="""B) The mean depth is 17.59, not 14.6.
C) The slope's sign doesn't matter.
D) The math gives a number, but it's an extrapolation.""", hint="Is 0 mm within the range of the data?"),

V("ch13-book-12", 1, image="ch13-book-gentoo-resid.png",
question=PEN + "\n\nThe figure shows bill depth vs bill length for Gentoo penguins. Solid lines are predictions from lm(bill_depth_mm ~ bill_length_mm + sex); dashed lines are separate fits for each sex.\n\nThe model's solid male line predicts a bill depth of about 16.3 mm at 56 mm. A male with a 56 mm bill has a residual of 0.7 mm. What is its actual bill depth?",
answer=r(16.3+0.7,1), explanation="Observed = predicted + residual = 16.3 + 0.7 = 17.0 mm.", hint="Residual = observed - predicted."),
V("ch13-book-12", 2, image="ch13-book-gentoo-resid.png",
question=PEN + "\n\nThe figure shows bill depth vs bill length for Gentoo penguins. Solid lines are predictions from lm(bill_depth_mm ~ bill_length_mm + sex); dashed lines are separate fits for each sex.\n\nA female Gentoo has a bill 46 mm long and 13.6 mm deep. The solid female line predicts about 14.3 mm at that length. What is her residual?",
answer=r(13.6-14.3,1), explanation="Residual = 13.6 - 14.3 = -0.7 mm. She sits below her line.", hint="Residual = observed - predicted."),

V("ch13-book-13", 1, image="ch13-book-gentoo-resid.png",
question=PEN + "\n\nThe figure shows Gentoo bill depth vs bill length, with solid lines from lm(bill_depth_mm ~ bill_length_mm + sex) and dashed lines from separate fits for each sex. Which of the following differ clearly between male and female Gentoo penguins? (Select all that apply.)",
options="""A) Mean bill lengths
B) Mean bill depths
C) Slopes
D) Intercepts""",
answer="A, B, D", explanation="Males have longer and deeper bills (different means) and their line sits higher (different intercept), but the slopes are nearly the same (parallel dashed lines).",
why_wrong="C) The dashed lines are nearly parallel.", hint="Look at where the clouds sit, and whether the dashed lines are parallel."),
V("ch13-book-13", 2, image="ch13-book-gentoo-resid.png",
question=PEN + "\n\nThe figure shows Gentoo bill depth vs bill length, with solid lines from lm(bill_depth_mm ~ bill_length_mm + sex) and dashed lines from separate fits for each sex. Why are the solid lines from the model exactly parallel?",
options="""A) The additive model gives both sexes one shared slope
B) Males and females have exactly the same mean bill length
C) The dashed separate fits are also exactly parallel
D) Bill depth was measured more precisely for one sex""",
answer="A", explanation="Without an interaction, the model estimates one bill length slope for both sexes; sex only shifts the line up or down.",
why_wrong="""B) The means differ.
C) The dashed lines are close but not exactly parallel.
D) Measurement precision doesn't set the slope.""", hint="How many slopes does bill_length_mm + sex estimate?"),

V("ch13-book-14", 1, question=PEN + "\n\nFor Chinstrap penguins, lm(flipper_length_mm ~ body_mass_g + sex) has a sum of squared residuals of 1748 on 65 degrees of freedom. What is the residual standard error?",
answer=r((1748/65)**0.5,2), explanation="Residual SE = √(SS / df) = √(1748 / 65) = √26.89 = 5.19.", hint="Divide by df, then take the square root."),
V("ch13-book-14", 2, question=PEN + "\n\nFor Chinstrap penguins, lm(flipper_length_mm ~ body_mass_g + sex) has a residual standard error of 5.186 on 65 degrees of freedom. What is the mean square residual (the residual variance)?",
answer=r(5.186**2,2), explanation="Mean square = residual SE² = 5.186² = 26.89.", hint="Square the residual SE."),
]
