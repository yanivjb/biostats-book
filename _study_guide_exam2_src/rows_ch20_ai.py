from ai_helpers import V, r
import importlib.util, os
spec = importlib.util.spec_from_file_location('o20', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rows_ch20.py')); o = importlib.util.module_from_spec(spec); spec.loader.exec_module(o)
PENG, PENG3, SR, SR_OUT, MOLE, MOLE_OUT, IRIS = o.PENG, o.PENG3, o.SR, o.SR_OUT, o.MOLE, o.MOLE_OUT, o.IRIS
ROWS = [
V("ch20-quiz-01", 1, question=PENG + "\n\nWhat does the intercept (23.31) in Model 3 represent?",
options="""A) The predicted bill length for a bill depth of 0 and mass of 0
B) The average bill length of the penguins in this dataset
C) The average bill length of Adelie penguins in this dataset
D) The change in bill length per mm of bill depth, all else equal""", answer="A",
explanation="With two numeric predictors, the intercept is the prediction when both equal zero: far outside the data, so just an anchor.",
why_wrong="""B) That's an intercept-only model.
C) Species isn't in Model 3.
D) That's the bill_dep slope.""", hint="Set every predictor to zero."),
V("ch20-quiz-01", 2, question=PENG + "\n\nIn Model 1, which species' mean bill length is NOT shown directly by any single coefficient, but must be found by adding two?",
options="""A) Chinstrap and Gentoo
B) Adelie only
C) Gentoo only
D) None; every mean is one coefficient""", answer="A",
explanation="Adelie's mean is the intercept (38.8). Chinstrap = 38.8 + 10.0 and Gentoo = 38.8 + 8.7.",
why_wrong="""B) Adelie is the intercept.
C) Chinstrap also needs adding.
D) Only the reference mean is a single coefficient.""", hint="Which species is the reference?"),

V("ch20-quiz-02", 1, question=PENG + "\n\nIn Model 1, what does speciesGentoo = 8.7 mean?",
options="""A) Gentoo bills are 8.7 mm longer than Adelie bills, on average
B) Gentoo bills are 8.7 mm long, on average, in this dataset
C) Adelie bills are 8.7 mm longer than Gentoo bills, on average
D) Gentoo bills are 8.7 mm longer than Chinstrap bills, on average""", answer="A",
explanation="Each species coefficient is a difference from the reference (Adelie).",
why_wrong="""B) Coefficients are differences, not means.
C) Wrong direction.
D) Gentoo is 1.3 mm shorter than Chinstrap.""", hint="Compared to which species?"),
V("ch20-quiz-02", 2, question=PENG + "\n\nIn Model 2, what does sexmale = 3.7 mean?",
options="""A) Males' bills are 3.7 mm longer than females' of the same species
B) Males' bills are 3.7 mm long on average, across all of the species
C) Male Adelie penguins have bills that are 3.7 mm long, on average
D) Females' bills are 3.7 mm longer than males' of the same species""", answer="A",
explanation="sexmale is the male - female difference, adjusting for species.",
why_wrong="""B) and C) Coefficients are differences.
D) Wrong direction.""", hint="Female is the reference level."),

V("ch20-quiz-03", 1, question=PENG + "\n\nWhat is the predicted bill length of a Chinstrap penguin from Model 1?",
answer=r(38.8+10.0,1), explanation="38.8 + 10.0 = 48.8 mm.", hint="Intercept + Chinstrap coefficient."),
V("ch20-quiz-03", 2, question=PENG + "\n\nAccording to Model 1, how many mm longer are Chinstrap bills than Gentoo bills, on average?",
answer=r(10.0-8.7,1), explanation="10.0 - 8.7 = 1.3 mm.", hint="The intercept cancels."),

V("ch20-quiz-04", 1, question=PENG + "\n\nIn Model 2, what is the predicted bill length of a male Adelie penguin?",
options="""A) 40.7 mm
B) 37.0 mm
C) 38.8 mm
D) 47.0 mm""", answer="A",
explanation="37.0 + 3.7 = 40.7 mm (Adelie is the reference species).",
why_wrong="""B) That's a female Adelie.
C) That's the Model 1 intercept.
D) Adds the Chinstrap coefficient.""", hint="Intercept + sexmale."),
V("ch20-quiz-04", 2, question=PENG + "\n\nWhy does the intercept change from 38.8 (Model 1) to 37.0 (Model 2)?",
options="""A) In Model 2 it describes female Adelies, not all Adelies
B) Adding sex changed which species is the reference level
C) The data used to fit Model 2 were completely different
D) Intercepts always shrink when terms are added to a model""", answer="A",
explanation="Model 2's intercept is the prediction for the reference levels of both species and sex (female Adelie), which is below the all-Adelie mean.",
why_wrong="""B) Adelie is still the reference.
C) Same data.
D) Not a rule.""", hint="What are the reference levels in Model 2?"),

V("ch20-quiz-05", 1, question=PENG + "\n\nWhat is the predicted bill length of a female Gentoo from Model 2?",
answer=r(37.0+8.7,1), explanation="37.0 + 8.7 = 45.7 mm.", hint="Female is the reference sex."),
V("ch20-quiz-05", 2, question=PENG + "\n\nWhat is the predicted bill length of a male Gentoo from Model 2?",
answer=r(37.0+8.7+3.7,1), explanation="37.0 + 8.7 + 3.7 = 49.4 mm.", hint="Add every coefficient that applies."),

V("ch20-quiz-06", 1, question=PENG + "\n\nUse Model 3 to predict the bill length of a penguin with a bill depth of 15 mm and a body mass of 5000 g.",
answer=r(23.31+0.163*15+0.00424*5000,1), explanation="23.31 + 0.163 × 15 + 0.00424 × 5000 = 23.31 + 2.45 + 21.2 = 46.96 ≈ 47.0 mm.", hint="Intercept + each slope × its value."),
V("ch20-quiz-06", 2, question=PENG + "\n\nAccording to Model 3, how much longer is the bill of a penguin that is 1000 g heavier, with the same bill depth?",
answer=r(0.00424*1000,2), explanation="0.00424 × 1000 = 4.24 mm.", hint="Slope × change in mass."),

V("ch20-quiz-07", 1, question=PENG + "\n\nIf body mass in Model 3 were measured in kg instead of g, what would happen to its coefficient?",
options="""A) It would be 1,000 times larger (4.24 per kg)
B) It would be 1,000 times smaller
C) It would stay the same
D) It would become equal to the bill depth coefficient""", answer="A",
explanation="A 1-kg change is 1,000 g, so the change per kg is 1,000 × 0.00424 = 4.24 mm. The relationship itself is unchanged.",
why_wrong="""B) Wrong direction.
C) Coefficients depend on units.
D) No reason for that.""", hint="Per gram vs per kilogram."),
V("ch20-quiz-07", 2, question=PENG + "\n\nWhich would let you fairly compare the importance of bill depth and body mass in Model 3?",
options="""A) Partial R² or standardized coefficients
B) The raw coefficients, 0.163 vs 0.00424
C) The intercept of the model, 23.31
D) The number of penguins in the dataset""", answer="A",
explanation="Raw coefficients depend on units. Partial R² and standardized coefficients put terms on a common scale.",
why_wrong="""B) Units differ.
C) and D) Don't compare predictors.""", hint="Common scale."),

V("ch20-quiz-08", 1, question=PENG + "\n\nTRUE or FALSE: A VIF of 1.3 for bill depth and body mass means multicollinearity is a serious problem in Model 3.",
options="""A) TRUE
B) FALSE""", answer="B",
explanation="VIFs of 5 to 10 are concerning. A VIF of 1.3 means only slight inflation of uncertainty.", why_wrong="TRUE: 1.3 is low.", hint="Compare to 5 to 10."),
V("ch20-quiz-08", 2, question=PENG + "\n\nThe two predictors in Model 3 have r² = 0.22. TRUE or FALSE: Their VIF is about 1 / (1 - 0.22) ≈ 1.3.",
options="""A) TRUE
B) FALSE""", answer="A",
explanation="With two predictors, VIF = 1 / (1 - r²) = 1 / 0.78 = 1.28.", why_wrong="FALSE: that's exactly the formula.", hint="VIF = 1 / (1 - r²)."),

V("ch20-quiz-10", 1, question=PENG3 + "\n\nAt α = 0.05, what do we do with the null hypothesis that bill depth is not associated with bill length, after accounting for body mass?",
options="""A) Fail to reject it (p = 0.234)
B) Reject it (p = 0.234)
C) Reject it (p < 2e-16)
D) Fail to reject it (p < 2e-16)""", answer="A",
explanation="Bill depth's Type II p-value is 0.234 > 0.05.",
why_wrong="""B) p > α.
C) and D) That's body mass's p-value.""", hint="Find bill_dep's row."),
V("ch20-quiz-10", 2, question=PENG3 + "\n\nWhat does 'Type II' mean for the F test of body mass in this table?",
options="""A) It's tested after accounting for bill depth
B) It's tested before accounting for bill depth
C) It's tested only within the second species
D) It tests whether it's a type II error""", answer="A",
explanation="Type II tests each term after adjusting for the other terms in the additive model.",
why_wrong="""B) That would be Type I if mass came first.
C) and D) Not what Type II means.""", hint="After the others."),

V("ch20-quiz-11", 1, question=PENG3 + "\n\nWhat does a partial R² of 0.319 for body mass mean?",
options="""A) After accounting for bill depth, mass explains ~32% of the remaining variation
B) Body mass explains 31.9% of all variation in bill length, ignoring bill depth
C) Body mass and bill depth have a correlation of 0.319 in these penguins
D) There's a 31.9% chance that body mass is not associated with bill length""", answer="A",
explanation="Partial R² is the share of the variation left after other terms that this term explains.",
why_wrong="""B) That would be a simple R².
C) Not a correlation.
D) Not a probability.""", hint="After accounting for the other term."),
V("ch20-quiz-11", 2, question=PENG3 + "\n\nHow is the partial R² of body mass calculated from the ANOVA table?",
options="""A) 3065.6 / (3065.6 + 6537.1)
B) 3065.6 / (27.4 + 3065.6 + 6537.1)
C) 27.4 / (27.4 + 6537.1)
D) 6537.1 / (3065.6 + 6537.1)""", answer="A",
explanation="Partial R² = SS term / (SS term + SS residual) = 3065.6 / 9602.7 = 0.319.",
why_wrong="""B) Includes bill depth's SS in the denominator.
C) That's bill depth's.
D) That's residual / (term + residual).""", hint="SS term / (SS term + SS residual)."),

V("ch20-quiz-12", 1, question=PENG3 + "\n\nAt what VIF would you start to worry about multicollinearity?",
options="""A) Around 5 to 10
B) Anything above 1
C) Around 1.1
D) Only above 100""", answer="A",
explanation="Common rules of thumb flag VIFs around 5 to 10.",
why_wrong="""B) and C) Some correlation is normal.
D) Far too lenient.""", hint="Rule of thumb."),
V("ch20-quiz-12", 2, question=PENG3 + "\n\nWhy do both predictors have exactly the same VIF (1.29)?",
options="""A) With two predictors, both VIFs come from the same r²
B) Bill depth and body mass are measured in the same units
C) The VIF is always the same for every predictor in a model
D) Because body mass is significant and bill depth is not""", answer="A",
explanation="Each predictor's VIF is 1 / (1 - R²) from regressing it on the others; with only two predictors, both use the same r².",
why_wrong="""B) Units differ.
C) Not with three or more predictors.
D) Significance doesn't set VIF.""", hint="Regress each predictor on the other."),

V("ch20-quiz-13", 1, question="Palmer penguins: we modeled bill length (mm) two ways:\n\nModel 3: lm(bill_len ~ bill_dep + body_mass)\nbill_dep = 0.16 (p = 0.23); body_mass = 0.0042 (p < 0.001); R² = 0.36\n\nModel 4: lm(bill_len ~ species + bill_dep + body_mass)\nbill_dep = 0.71 (p < 0.001); body_mass = 0.0027 (p < 0.001); R² = 0.82\n\nWhat does the bill_dep coefficient of 0.71 in Model 4 describe?",
options="""A) Change in bill length per mm of depth, adjusting for species and mass
B) Change in bill length per mm of depth, ignoring the differences among species
C) The difference in bill depth between Gentoo and Adelie penguins
D) The proportion of variation in bill length explained by depth""", answer="A",
explanation="Each coefficient is adjusted for the other terms in the model: here species and body mass.",
why_wrong="""B) Species is in the model.
C) Not a species difference.
D) That's a partial R².""", hint="What else is in Model 4?"),
V("ch20-quiz-13", 2, question="Palmer penguins: we modeled bill length (mm) two ways:\n\nModel 3: lm(bill_len ~ bill_dep + body_mass)\nbill_dep = 0.16 (p = 0.23); body_mass = 0.0042 (p < 0.001); R² = 0.36\n\nModel 4: lm(bill_len ~ species + bill_dep + body_mass)\nbill_dep = 0.71 (p < 0.001); body_mass = 0.0027 (p < 0.001); R² = 0.82\n\nWhy did R² jump from 0.36 to 0.82?",
options="""A) Species explains a lot of bill length variation
B) Adding any variable always doubles R²
C) Bill depth became significant in Model 4
D) Species causes the change in bill depth""", answer="A",
explanation="Species differ a lot in bill length, so including species explains much more variation.",
why_wrong="""B) Not a rule.
C) A consequence, not the reason R² rose.
D) Causation isn't shown.""", hint="What was added?"),

V("ch20-hw-01", 1, question="Match each R code to the type of sums of squares it uses for an additive model:\n\n1. anova(lm(y ~ a + b))\n2. car::Anova(lm(y ~ a + b))",
options="""A) Type I (sequential)
B) Type II
C) Type III
D) Partial R²""", answer="1-A, 2-B",
explanation="Base R anova() is sequential (Type I); car::Anova() defaults to Type II.", why_wrong="Base R vs car.", hint="Which is order-dependent?"),
V("ch20-hw-01", 2, question="You're analyzing how temperature and humidity affect insect activity. Match each blank:\n\n1. The type of sums of squares whose results depend on the order of terms\n2. The base R function that calculates it",
options="""A) Type I
B) Type II
C) anova()
D) Anova()""", answer="1-A, 2-C",
explanation="Type I is sequential, so order matters; base R's anova() uses it.", why_wrong="car::Anova() gives Type II.", hint="Sequential = Type I."),

V("ch20-hw-02", 1, question="In anova(lm(y ~ a + b)), which term's test is the same as its Type II test?",
options="""A) b, the term entered last
B) a, the term entered first
C) Both a and b
D) Neither a nor b""", answer="A",
explanation="With Type I, the last term is tested after all others, which is what Type II does.",
why_wrong="""B) a is tested without adjusting for b.
C) Only b.
D) b matches.""", hint="Which term is adjusted for the other?"),
V("ch20-hw-02", 2, question="When will anova(lm(y ~ a + b)) and anova(lm(y ~ b + a)) give the same results for both terms?",
options="""A) When a and b are uncorrelated (e.g. a balanced design)
B) Always; the order of terms never matters in anova()
C) Only when both a and b are significant predictors
D) Only when y is normally distributed in each group""", answer="A",
explanation="If predictors don't overlap, adjusting for one doesn't change the other's SS, so order doesn't matter.",
why_wrong="""B) Order matters when predictors are correlated.
C) and D) Irrelevant.""", hint="When does adjusting change nothing?"),

V("ch20-hw-03", 1, question="In a model predicting seed output from leaf size and plant height (highly correlated), which is LEAST affected by the multicollinearity?",
options="""A) The model's predictions and overall R²
B) The standard errors of the two coefficients
C) The stability of each coefficient across samples
D) Our ability to separate each predictor's effect""", answer="A",
explanation="Multicollinearity mainly destabilizes individual coefficients; the model's overall fit and predictions are fine.",
why_wrong="B), C) and D) are what multicollinearity harms.", hint="Individual coefficients vs overall fit."),
V("ch20-hw-03", 2, question="Which is a reasonable response to severe multicollinearity between two predictors?",
options="""A) Drop one, or combine them into one variable
B) Add more highly correlated predictors
C) Ignore it; it only affects the intercept
D) Report the p-values with more decimal places""", answer="A",
explanation="Removing or combining redundant predictors reduces the overlap.",
why_wrong="""B) Makes it worse.
C) It affects slopes.
D) Irrelevant.""", hint="Reduce the overlap."),

V("ch20-hw-04", 1, question="A study of bird song adds habitat type to a regression and says it 'held habitat constant'. What's a more accurate phrase?",
options="""A) 'Adjusted for habitat statistically'
B) 'Experimentally manipulated habitat'
C) 'Proved habitat doesn't matter'
D) 'Randomized birds to habitats'""", answer="A",
explanation="Regression adjusts statistically; nothing was held constant by design.",
why_wrong="""B) and D) Nothing was manipulated.
C) Adjusting doesn't prove that.""", hint="Statistical vs experimental."),
V("ch20-hw-04", 2, question="Why does 'adjusting for' body mass in a regression not fully remove its influence?",
options="""A) It removes only the part the model's form (e.g. linear) captures
B) Regression ignores every variable that is put into the model
C) Body mass can never be measured accurately in animals
D) It does fully remove it, whatever the model looks like""", answer="A",
explanation="If the true relationship is curved, or mass is measured with error, a linear adjustment leaves some influence behind.",
why_wrong="""B) Regression uses them.
C) Not the main point.
D) Adjustment is imperfect.""", hint="What if the relationship isn't linear?"),

V("ch20-hw-05", 1, image="ch20-hw-sr-diag.png", question=SR + "\n\nTwo models: Model 1 uses mean_visits as the response; Model 2 uses log1p(mean_visits). Their diagnostic plots are shown. What problem does Model 1's QQ plot show?",
options="""A) Right-skewed residuals
B) Perfectly normal residuals
C) Non-independent residuals
D) Too few data points""", answer="A",
explanation="The points curve upward at the right: a long right tail.",
why_wrong="""B) They deviate.
C) QQ plots don't show independence.
D) There are 113 RILs.""", hint="Which way do the points bend?"),
V("ch20-hw-05", 2, image="ch20-hw-sr-diag.png", question=SR + "\n\nWhy use log1p(mean_visits) = log(mean_visits + 1) rather than log(mean_visits)?",
options="""A) Some RILs had zero visits, and log(0) is undefined
B) log1p() always gives a larger effect size than log()
C) log() is only defined for whole numbers of visits
D) log1p() makes the data perfectly normal""", answer="A",
explanation="Adding 1 lets zeros be transformed (log(1) = 0).",
why_wrong="""B) Not about effect size.
C) log() works on non-integers.
D) No transformation guarantees normality.""", hint="What is log(0)?"),

V("ch20-hw-06", 1, question=SR + "\n\nvif(lm(log1p_visits ~ petal_area_mm + asd_mm))\npetal_area_mm  asd_mm\n      1.068     1.068\n\nWhat does a VIF of 1.07 tell us?",
options="""A) Uncertainty in each coefficient is barely inflated by the overlap
B) The two predictors are perfectly correlated with each other
C) The model explains 1.07% of the variation in visits
D) Each coefficient's p-value should be multiplied by 1.07""", answer="A",
explanation="VIF is the inflation of each coefficient's variance due to correlation with other predictors; 1.07 is tiny.",
why_wrong="""B) That would give infinite VIF.
C) Not R².
D) Not how VIF is used.""", hint="Variance inflation."),
V("ch20-hw-06", 2, question=SR + "\n\ncor.test(asd_mm, petal_area_mm): r = 0.33, p = 4.5 × 10⁻⁶\n\nThe predictors are significantly correlated. Does that mean multicollinearity is a problem?",
options="""A) No: the correlation is weak (r = 0.33)
B) Yes: any significant correlation is a problem
C) Yes: p < 0.05 means VIF must be above 10
D) Can't tell without running a t-test""", answer="A",
explanation="With 113 RILs, even weak correlations are significant. What matters is strength: VIF = 1 / (1 - 0.33²) ≈ 1.12.",
why_wrong="""B) and C) Significance isn't strength.
D) We have what we need.""", hint="Significance vs strength."),

V("ch20-hw-07", 1, question=SR + "\n\n" + SR_OUT + "\n\nPredict mean_visits for a plant with an ASD of 1 mm and a petal area of 80 mm².",
answer=r(-1.098+0.0302*80+0.498*1,2), explanation="-1.098 + 0.0302 × 80 + 0.498 × 1 = -1.098 + 2.416 + 0.498 = 1.82 visits.", hint="Intercept + each slope × its value."),
V("ch20-hw-07", 2, question=SR + "\n\n" + SR_OUT + "\n\nTwo plants have the same ASD, but one has 20 mm² more petal area. How many more mean visits does the model predict for it?",
answer=r(0.0302*20,3), explanation="0.0302 × 20 = 0.604 visits.", hint="Slope × difference."),

V("ch20-hw-08", 1, question=SR + "\n\nThe petal_area_mm coefficient in lm(mean_visits ~ petal_area_mm + asd_mm) is 0.030. This means mean visits increase by about 0.03 per 1 mm² of petal area...",
options="""A) after adjusting for ASD
B) without accounting for ASD
C) only for plants with an ASD of 0
D) because larger petals cause visits""", answer="A",
explanation="Each coefficient in a multiple regression is adjusted for the other predictors.",
why_wrong="""B) ASD is in the model.
C) Not an interaction model.
D) Association, not causation.""", hint="What else is in the model?"),
V("ch20-hw-08", 2, question=SR + "\n\nA simple regression of mean_visits on asd_mm alone gives a slope of 1.1, but in lm(mean_visits ~ petal_area_mm + asd_mm) the asd_mm slope is 0.50. Why might it shrink?",
options="""A) ASD correlates with petal area, which takes over part of its effect
B) Adding a predictor always cuts every other slope in half
C) The simple regression must have been calculated incorrectly
D) ASD was measured in different units in the two models""", answer="A",
explanation="In the simple regression, ASD gets credit for some of petal area's association. Adjusting for petal area removes that.",
why_wrong="""B) Not a rule.
C) Both can be right; they answer different questions.
D) Same units.""", hint="Overlap between predictors."),

V("ch20-hw-09", 1, question=SR + "\n\nA tablemate ran anova(lm(mean_visits ~ petal_area_mm + asd_mm)), putting petal area first. For which term would anova() and car::Anova() agree?",
options="""A) ASD, the term entered last
B) Petal area, the term entered first
C) Both terms in the model
D) Neither term in the model""", answer="A",
explanation="With Type I, the last term is adjusted for all others, matching Type II.",
why_wrong="""B) Petal area isn't adjusted for ASD in Type I.
C) Only the last term matches.
D) The last term matches.""", hint="Which term is adjusted in both?"),
V("ch20-hw-09", 2, question=SR + "\n\nWhy did ASD look significant when entered FIRST in anova(), but not in car::Anova()?",
options="""A) Entered first, ASD takes credit for variation shared with petal area
B) car::Anova() uses a smaller sample than the base anova() does
C) anova() always gives smaller p-values than car::Anova()
D) The base anova() function contains a bug for numeric data""", answer="A",
explanation="Sequential SS give the first term all the variation it shares with later terms.",
why_wrong="""B) Same data.
C) Not always.
D) No bug; different question.""", hint="Shared variation."),

V("ch20-hw-10", 1, question=SR + "\n\n" + SR_OUT + "\n\nAt α = 0.01, what do you do to each null?\n\n1. Petal area is not associated with visitation (after adjusting for ASD)\n2. ASD is not associated with visitation (after adjusting for petal area)",
options="""A) Reject it
B) Fail to reject it""", answer="1-A, 2-B",
explanation="Petal area: p = 0.0004 < 0.01, reject. ASD: p = 0.13, fail to reject.", why_wrong="Compare each p with 0.01.", hint="α = 0.01."),
V("ch20-hw-10", 2, question=SR + "\n\n" + SR_OUT + "\n\nMatch each term to its F value's calculation:\n\n1. petal_area_mm\n2. asd_mm",
options="""A) (22.22 / 1) / (182.13 / 110)
B) (3.88 / 1) / (182.13 / 110)
C) 22.22 / 3.88
D) 182.13 / 110""", answer="1-A, 2-B",
explanation="F = (SS term / df term) / MS residual, with MS residual = 182.13 / 110 = 1.656.", why_wrong="Each F divides its own MS by MS residual.", hint="MS term / MS residual."),

V("ch20-hw-11", 1, question=SR + "\n\nPetal area is significantly associated with visitation after adjusting for ASD. Which study would best test whether larger petals CAUSE more visits?",
options="""A) Experimentally trim petals on random plants and count visits
B) Measure more RILs and refit the same regression model
C) Add more floral traits to the model as covariates
D) Use a smaller α so the result is more convincing""", answer="A",
explanation="Manipulating petal size at random breaks links with other traits, allowing causal inference.",
why_wrong="""B) and C) Still observational.
D) α doesn't establish causation.""", hint="Manipulation."),
V("ch20-hw-11", 2, question=SR + "\n\nWhy doesn't adjusting for ASD rule out all alternative explanations for the petal area association?",
options="""A) Other unmeasured traits may correlate with petal area
B) ASD was measured with too much precision to be useful
C) Adjusting for one variable removes every confounder
D) Petal area and ASD are uncorrelated in these RILs""", answer="A",
explanation="Only measured variables in the model are adjusted for; unmeasured confounders remain.",
why_wrong="""B) Irrelevant.
C) That's the misconception.
D) They are correlated (r = 0.33), and it doesn't matter here.""", hint="What about traits not in the model?"),

V("ch20-hw-12", 1, question=SR + "\n\n" + SR_OUT + "\n\nWhy can't we compare the raw coefficients (0.0302 for petal area, 0.498 for ASD) to judge importance?",
options="""A) They are in different units (per mm² vs per mm)
B) The intercept is negative, so the slopes are unreliable
C) Raw coefficients are always unitless numbers
D) Only one of them is statistically significant""", answer="A",
explanation="A slope's size depends on its predictor's units and spread. Partial R² is on a common scale.",
why_wrong="""B) Irrelevant.
C) They have units.
D) Significance doesn't fix units.""", hint="Units."),
V("ch20-hw-12", 2, question=SR + "\n\n" + SR_OUT + "\n\nHow many times more of the remaining variation does petal area explain than ASD?",
options="""A) About 5 times
B) About 16 times
C) About 0.06 times
D) The same amount""", answer="A",
explanation="0.109 / 0.021 ≈ 5.2.",
why_wrong="""B) That's 0.498 / 0.0302 (raw coefficients).
C) Upside down, roughly.
D) They differ.""", hint="Compare partial R²."),

V("ch20-chimein-03", 1, question="To ask whether urban birds sing at higher pitch than rural birds, accounting for body size (larger birds sing lower), researchers fit lm(pitch ~ habitat + body_size). Match each role to its variable:\n\n1. Response variable\n2. Covariate we wish to account for\n3. Key explanatory variable",
options="""A) Song pitch
B) Body size
C) Habitat (urban vs rural)""", answer="1-A, 2-B, 3-C",
explanation="The question is about habitat (key explanatory) and pitch (response), accounting for body size (covariate).", why_wrong="What's the research question about?", hint="What are we asking about?"),
V("ch20-chimein-03", 2, question=MOLE + "\n\nWhy include lnMass in the model?",
options="""A) Bigger rats use more energy; castes may differ in size
B) lnMass is the main research question of the study
C) Including more predictors always improves a model
D) The castes were defined by their body mass alone""", answer="A",
explanation="If castes differ in mass, an energy difference might just reflect size. Adjusting for mass isolates the caste effect.",
why_wrong="""B) Caste is the question.
C) Not always.
D) Castes are defined by behavior.""", hint="What could confound the caste comparison?"),

V("ch20-chimein-04", 1, question=MOLE + "\n\n" + MOLE_OUT + "\n\nWhat is the predicted lnEnergy for a worker with lnMass = 4.0?",
options="""A) 3.87
B) 3.48
C) 4.97
D) 0.39""", answer="A",
explanation="-0.097 + 0.393 + 0.893 × 4.0 = 3.868.",
why_wrong="""B) That's a lazy rat (no caste term).
C) Uses 5.0 for lnMass.
D) That's the casteworker coefficient.""", hint="Intercept + casteworker + lnMass slope × 4.0."),
V("ch20-chimein-04", 2, question=MOLE + "\n\n" + MOLE_OUT + "\n\nA worker and a lazy mole rat have the same body mass. By how much does their predicted lnEnergy differ?",
options="""A) 0.393, whatever their mass is
B) 0.893, whatever their mass is
C) It depends on their body mass
D) 0.097, the size of the intercept""", answer="A",
explanation="In an additive model, the caste difference is the same at every mass: the casteworker coefficient.",
why_wrong="""B) That's the lnMass slope.
C) Only with an interaction.
D) That's the intercept.""", hint="Additive model, parallel lines."),

V("ch20-chimein-05", 1, image="ch20-chimein-molerat-sep.png", question=MOLE + "\n\nThis plot was made with geom_smooth(method = 'lm'), giving each caste its own line. Which model would these lines match?",
options="""A) lm(lnEnergy ~ caste * lnMass), with an interaction
B) lm(lnEnergy ~ caste + lnMass), without an interaction
C) lm(lnEnergy ~ caste), without any body mass term
D) lm(lnEnergy ~ lnMass), without any caste term""", answer="A",
explanation="Separate slopes per caste correspond to an interaction model.",
why_wrong="""B) Additive → parallel lines.
C) Would be flat lines.
D) One line for all.""", hint="Separate slopes."),
V("ch20-chimein-05", 2, image="ch20-chimein-molerat-sep.png", question=MOLE + "\n\nIf we plotted the fitted values from lm(lnEnergy ~ caste + lnMass), what would the two lines look like?",
options="""A) Parallel lines, with the worker line higher
B) Lines with different slopes for each caste
C) A single line shared by both of the castes
D) Two flat lines at each caste's mean energy""", answer="A",
explanation="Additive model: shared slope, different intercepts (workers 0.393 higher).",
why_wrong="""B) That's an interaction.
C) Ignores caste.
D) Ignores mass.""", hint="One slope, two intercepts."),

V("ch20-chimein-06", 1, image="ch20-chimein-molerat-diag.png", question=MOLE + "\n\nConsider these diagnostic plots for lm(lnEnergy ~ caste + lnMass). Which assumptions can't be checked with these plots?",
options="""A) Independence and unbiased sampling
B) Normality of residuals and linearity
C) Equal variance and normality of residuals
D) Linearity and equal variance of residuals""", answer="A",
explanation="Independence and bias depend on how the data were collected.",
why_wrong="B), C) and D) are what diagnostic plots address.", hint="Design vs data."),
V("ch20-chimein-06", 2, image="ch20-chimein-molerat-diag.png", question=MOLE + "\n\nWhat would a clear curve in the residuals vs fitted plot suggest?",
options="""A) A violation of linearity
B) A violation of independence
C) Normally distributed residuals
D) That the sample size is too large""", answer="A",
explanation="A curve means the straight-line model misses a nonlinear pattern.",
why_wrong="""B) Can't be seen here.
C) Unrelated.
D) Unrelated.""", hint="Straight line vs curve."),

V("ch20-chimein-07", 1, question=MOLE + "\n\n" + MOLE_OUT + "\n\nWhat does the lnMass test (F = 21.39, p < 0.001) tell us?",
options="""A) Heavier rats use more energy, after adjusting for caste
B) Workers use more energy than lazy rats of the same mass
C) Caste has no association with energy expenditure
D) Body mass causes differences in caste membership""", answer="A",
explanation="lnMass is significantly associated with lnEnergy after accounting for caste (and its slope is positive).",
why_wrong="""B) That's the caste test.
C) The caste test is significant.
D) Not what's tested.""", hint="Which row?"),
V("ch20-chimein-07", 2, question=MOLE + "\n\n" + MOLE_OUT + "\n\nHow many mole rats were in this study?",
options="""A) 35
B) 32
C) 34
D) 3""", answer="A",
explanation="Residual df = n - number of estimated parameters (3): n = 32 + 3 = 35.",
why_wrong="""B) That's the residual df.
C) Adds only 2.
D) That's the number of parameters.""", hint="Residual df = n - parameters."),

V("ch20-book-01", 1, question=IRIS + "\n\nHow many coefficients does this model estimate, including the intercept?",
options="""A) Four
B) Three
C) Two
D) Five""", answer="A",
explanation="Intercept, Sepal.Length, Speciesversicolor and Speciesvirginica.",
why_wrong="Count the coefficients in the output.", hint="Count them."),
V("ch20-book-01", 2, question=IRIS + "\n\nWhy does species get two coefficients?",
options="""A) It has three levels: one is the reference
B) It is the most important predictor
C) Each species has two flowers sampled
D) Species interacts with sepal length""", answer="A",
explanation="A categorical variable with k levels gets k - 1 coefficients.",
why_wrong="""B) Importance doesn't set the count.
C) Irrelevant.
D) There's no interaction term.""", hint="k - 1."),

V("ch20-book-02", 1, question=IRIS + "\n\nUsing the model, what is the predicted petal length of a setosa flower with a sepal length of 5 cm?",
options="""A) About 1.46 cm
B) About 3.67 cm
C) About 4.55 cm
D) About 0.63 cm""", answer="A",
explanation="-1.7023 + 0.6321 × 5 = 1.458 cm (setosa is the reference).",
why_wrong="""B) Adds the versicolor coefficient.
C) Adds the virginica coefficient.
D) That's the slope.""", hint="Setosa is the reference level."),
V("ch20-book-02", 2, question=IRIS + "\n\nTwo virginica flowers differ in sepal length by 2 cm. How much does their predicted petal length differ?",
options="""A) About 1.26 cm
B) About 0.63 cm
C) About 3.09 cm
D) About 6.18 cm""", answer="A",
explanation="0.6321 × 2 = 1.26 cm.",
why_wrong="""B) For 1 cm.
C) The virginica coefficient.
D) 2 × 3.09.""", hint="Slope × difference."),

V("ch20-book-03", 1, question=IRIS + "\n\nAt the same sepal length, how much longer are virginica petals than versicolor petals?",
options="""A) About 0.88 cm
B) About 3.09 cm
C) About 2.21 cm
D) About 5.30 cm""", answer="A",
explanation="3.0900 - 2.2101 = 0.88 cm.",
why_wrong="""B) Virginica vs setosa.
C) Versicolor vs setosa.
D) Adds them.""", hint="Subtract the two species coefficients."),
V("ch20-book-03", 2, question=IRIS + "\n\nThe Speciesvirginica coefficient (3.09) compares virginica petal length to:",
options="""A) Setosa petal length, at the same sepal length
B) Setosa petal length, ignoring sepal length
C) Versicolor petal length, at the same sepal length
D) The average petal length of all three species""", answer="A",
explanation="Setosa is the reference, and the comparison adjusts for sepal length.",
why_wrong="""B) Sepal length is in the model.
C) Versicolor isn't the reference.
D) Not an average.""", hint="Reference level + adjustment."),

V("ch20-book-04", 1, question=IRIS + "\n\nWhich phrase best describes what this model does with sepal length when comparing species?",
options="""A) Adjusts for it statistically
B) Holds it constant by design
C) Randomly assigns it to flowers
D) Removes it from the data""", answer="A",
explanation="Regression adjusts statistically; nothing was fixed by design.",
why_wrong="""B) and C) That's experimental.
D) It's in the model.""", hint="Statistical vs experimental."),
V("ch20-book-04", 2, question=IRIS + "\n\nWhy can't this model 'control for' species the way an experiment would?",
options="""A) We can't assign a flower to a species at random
B) Species is a variable with only three levels
C) Sepal length is a continuous numeric variable
D) It can; regression and experiments are the same""", answer="A",
explanation="Species can't be manipulated; we can only adjust for it statistically.",
why_wrong="""B) and C) Irrelevant.
D) They differ.""", hint="Could you randomly assign species?"),

V("ch20-book-05", 1, image="ch20-book-iris-slopes.png", question=IRIS + "\n\nThe figure shows two ways to plot these data. What model does plot A (separate slopes) correspond to?",
options="""A) An interaction model: Sepal.Length * Species
B) This additive model: Sepal.Length + Species
C) A model with Species only, no sepal length
D) A model with Sepal.Length only, no species""", answer="A",
explanation="Separate slopes per species correspond to an interaction model.",
why_wrong="""B) Additive → parallel lines (B).
C) and D) Would give flat lines or one line.""", hint="Different slopes."),
V("ch20-book-05", 2, image="ch20-book-iris-slopes.png", question=IRIS + "\n\nThe figure shows two ways to plot these data. In plot B, what is the vertical gap between the setosa and virginica lines?",
options="""A) 3.09 cm, the Speciesvirginica coefficient
B) 0.63 cm, the Sepal.Length coefficient
C) 2.21 cm, the Speciesversicolor coefficient
D) It changes along the sepal length axis""", answer="A",
explanation="Parallel lines are separated by the species coefficient at every sepal length.",
why_wrong="""B) That's the slope.
C) That's versicolor vs setosa.
D) Parallel lines keep a constant gap.""", hint="Parallel lines, constant gap."),

V("ch20-book-06", 1, question=IRIS + "\n\nWhich test tells us whether species as a whole is associated with petal length, after adjusting for sepal length?",
options="""A) The Type II F test for Species from car::Anova()
B) The p-value for Speciesversicolor in summary()
C) The p-value for the intercept in summary()
D) The p-value for Sepal.Length in summary()""", answer="A",
explanation="The Type II F test asks about the species term as a whole.",
why_wrong="""B) Tests only versicolor vs setosa.
C) Tests whether the intercept is zero.
D) Tests sepal length.""", hint="One test for the whole term."),
V("ch20-book-06", 2, question=IRIS + "\n\nWhat does the p-value for Speciesvirginica in summary() test?",
options="""A) Whether virginica differs from setosa at the same sepal length
B) Whether species matters at all, after adjusting for sepal length
C) Whether virginica differs from versicolor in petal length
D) Whether virginica petals are longer than 0 cm""", answer="A",
explanation="Each coefficient's test compares that level to the reference, adjusting for other terms.",
why_wrong="""B) That's the F test.
C) Versicolor isn't the reference.
D) That's not the coefficient's meaning.""", hint="Compared to the reference."),

V("ch20-book-07", 1, question="Match each situation to the function you'd use:\n\n1. Test each predictor after accounting for the others in an additive model\n2. Get model-adjusted group means and pairwise contrasts",
options="""A) car::Anova()
B) emmeans()
C) anova()
D) vif()""", answer="1-A, 2-B",
explanation="car::Anova() gives Type II tests; emmeans() gives adjusted means and contrasts.", why_wrong="anova() is sequential; vif() checks multicollinearity.", hint="Type II vs adjusted means."),
V("ch20-book-07", 2, question="Match each R function to what it reports:\n\n1. car::vif(model)\n2. anova(model)",
options="""A) How much each coefficient's variance is inflated by correlated predictors
B) Sequential (Type I) sums of squares for each term
C) Model-adjusted means for each group
D) Tests of whether residuals are normal""", answer="1-A, 2-B",
explanation="vif() measures multicollinearity; anova() gives sequential SS.", why_wrong="emmeans() gives adjusted means.", hint="VIF = variance inflation factor."),

V("ch20-book-08", 1, question=IRIS + "\n\nemmeans(iris_model, ~ Species)\n Species    emmean\n setosa       1.99\n versicolor   4.20\n virginica    5.08\n\nWhy is setosa's emmean (1.99) different from the intercept (-1.70)?",
options="""A) emmean is at the average sepal length; the intercept is at 0 cm
B) emmean uses a different reference species than the intercept
C) The intercept is the raw mean of setosa petal lengths
D) emmean ignores the sepal length term in the model""", answer="A",
explanation="emmeans predicts at the mean sepal length (5.84 cm): -1.70 + 0.632 × 5.84 = 1.99.",
why_wrong="""B) Same reference.
C) The intercept is at sepal length 0.
D) It uses sepal length at its mean.""", hint="Where is each evaluated?"),
V("ch20-book-08", 2, question=IRIS + "\n\ncontrast(..., method = 'pairwise', adjust = 'tukey')\n setosa - versicolor     -2.21  p < 0.0001\n setosa - virginica      -3.09  p < 0.0001\n versicolor - virginica  -0.88  p < 0.0001\n\nWhy use a Tukey adjustment here?",
options="""A) To control false positives across all pairs
B) To make each comparison's p-value smaller
C) Because the species have unequal variances
D) To adjust the comparisons for sepal length""", answer="A",
explanation="Tukey adjusts for multiple comparisons. (Adjusting for sepal length comes from the model itself.)",
why_wrong="""B) Adjustment makes p larger.
C) Not what Tukey addresses.
D) The model already does that.""", hint="Multiple comparisons."),

V("ch20-book-09", 1, question=IRIS + "\n\nMatch each question to its answer:\n\n1. Which tool puts sepal length and species on a common scale of importance?\n2. Why can't the coefficients 0.63 and 2.21 be compared directly?",
options="""A) Partial R²
B) They describe different kinds of comparisons
C) The intercept, -1.70
D) They have the same units""", answer="1-A, 2-B",
explanation="Partial R² compares terms on the same scale; raw coefficients describe a slope vs a group difference.", why_wrong="Raw coefficients aren't on a common scale.", hint="Common scale."),
V("ch20-book-09", 2, question=IRIS + "\n\nMatch each quantity to what it describes:\n\n1. The Sepal.Length coefficient (0.63)\n2. The partial R² for Sepal.Length",
options="""A) The expected change in petal length per cm of sepal length
B) The share of variation explained by sepal length after accounting for species
C) The correlation between sepal length and species
D) The probability that sepal length matters""", answer="1-A, 2-B",
explanation="A coefficient is a slope; partial R² is a share of variation.", why_wrong="Neither is a correlation or probability.", hint="Slope vs share."),
]
