PENG = """Palmer penguins data: measurements from three Antarctic penguin species (Adelie, Chinstrap and Gentoo). We modeled bill length (bill_len, mm) three ways:

Model 1: lm(bill_len ~ species): (Intercept) = 38.8; speciesChinstrap = 10.0; speciesGentoo = 8.7
Model 2: lm(bill_len ~ species + sex): (Intercept) = 37.0; speciesChinstrap = 10.0; speciesGentoo = 8.7; sexmale = 3.7
Model 3: lm(bill_len ~ bill_dep + body_mass): (Intercept) = 23.31; bill_dep = 0.163; body_mass = 0.00424
(bill_dep is bill depth in mm; body_mass is in g)"""
PENG3 = """Palmer penguins: we modeled bill length (mm) as a function of bill depth (mm) and body mass (g):

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
    1.29      1.29"""
SR = """To ask which floral traits attract pollinators, we modeled mean pollinator visits to 113 parviflora RILs at Sawmill Road as a function of petal area (mm²) and anther-stigma distance (ASD, mm)."""
SR_OUT = """lm(mean_visits ~ petal_area_mm + asd_mm)
(Intercept) = -1.098; petal_area_mm = 0.0302; asd_mm = 0.498

car::Anova(model)
               Sum Sq  Df F value  Pr(>F)
petal_area_mm  22.22   1   13.42  0.0004
asd_mm          3.88   1    2.35  0.129
Residuals     182.13 110

partial_r2(model)
term           partial_r2
petal_area_mm       0.109
asd_mm              0.021"""
MOLE = """In Damaraland mole rats, some workers seem to work much less than others ("lazy" vs "worker" castes). Researchers compared daily energy expenditure between castes, accounting for body mass (both log-transformed: lnEnergy and lnMass)."""
MOLE_OUT = """lm(lnEnergy ~ caste + lnMass, data = mole_rats)
(Intercept) = -0.097; casteworker = 0.393; lnMass = 0.893

car::Anova(model)
          Sum Sq Df F value  Pr(>F)
caste      0.638  1    7.25  0.011
lnMass     1.882  1   21.39  <0.001
Residuals  2.815 32"""
IRIS = """The iris data contain flower measurements from three iris species (setosa, versicolor and virginica). We modeled petal length as a function of sepal length and species:

lm(Petal.Length ~ Sepal.Length + Species, data = iris)

      (Intercept)  Sepal.Length  Speciesversicolor  Speciesvirginica
          -1.7023        0.6321             2.2101            3.0900"""

ROWS = [
# ---------------- Quiz (penguins) ----------------
dict(id="ch20-quiz-01", source="Multiple regression quiz (2026), Q1", topics="intercept, categorical predictors", type="MC",
question=PENG + "\n\nWhat does the intercept (38.8) in Model 1 represent?",
options="""A) The average bill length across all penguins
B) The average bill length of Adelie penguins
C) The bill length of a penguin with a body mass of zero
D) The difference in bill length between Adelie and Gentoo penguins
E) The average bill length of male Adelie penguins""",
answer="B",
explanation="Adelie is the reference level (first alphabetically), so the intercept is the Adelie mean.",
why_wrong="""A) That would be an intercept-only model.
C) Body mass isn't in Model 1.
D) That's the speciesGentoo coefficient.
E) Sex isn't in Model 1.""",
hint="Which species has no coefficient of its own?"),

dict(id="ch20-quiz-02", source="Multiple regression quiz (2026), Q2", topics="categorical predictors, coefficients", type="MC",
question=PENG + "\n\nIn Model 1, what does speciesChinstrap = 10.0 mean?",
options="""A) Chinstrap penguins have bills 10 mm long, on average
B) Adelie penguins' bills are, on average, 10 mm longer than Chinstrap penguins' bills
C) Chinstrap penguins' bills are, on average, 10 mm longer than Adelie penguins' bills""",
answer="C",
explanation="Each species coefficient is that species' difference from the reference (Adelie).",
why_wrong="""A) 10 is a difference, not a mean.
B) The sign is positive: Chinstraps are longer.""",
hint="Coefficients for categories are differences from the reference level."),

dict(id="ch20-quiz-03", source="Multiple regression quiz (2026), Q3", topics="predictions", type="numeric",
question=PENG + "\n\nWhat is the predicted bill length of a Gentoo penguin from Model 1?",
answer="47.5", explanation="38.8 + 8.7 = 47.5 mm.",
why_wrong="Common mistake: answering 8.7 (the difference from Adelie).",
hint="Start at the intercept, then add the Gentoo coefficient."),

dict(id="ch20-quiz-04", source="Multiple regression quiz (2026), Q4", topics="intercept, multiple predictors", type="MC",
question=PENG + "\n\nIn Model 2, what does the intercept (37.0) represent?",
options="""A) The average bill length of Adelie penguins
B) The predicted bill length of a female Adelie penguin
C) The predicted bill length of a male Adelie penguin
D) The average bill length of all females""",
answer="B",
explanation="The intercept is the prediction when every indicator is 0: species = Adelie and sex = female (both reference levels).",
why_wrong="""A) Model 2 also includes sex.
C) Male would add 3.7.
D) It's specific to Adelie.""",
hint="What are the reference levels of species and sex?"),

dict(id="ch20-quiz-05", source="Multiple regression quiz (2026), Q5", topics="predictions, multiple predictors", type="numeric",
question=PENG + "\n\nWhat is the predicted bill length of a male Chinstrap from Model 2?",
answer="50.7", explanation="37.0 + 10.0 + 3.7 = 50.7 mm.",
why_wrong="Common mistake: using Model 1's intercept (38.8) instead of Model 2's.",
hint="Intercept + species + sex."),

dict(id="ch20-quiz-06", source="Multiple regression quiz (2026), Q6", topics="predictions, multiple predictors", type="numeric",
question=PENG + "\n\nUse Model 3 to predict the bill length of a penguin with a bill depth of 18 mm and a body mass of 4000 g.",
answer="43.2", explanation="23.31 + 0.163 × 18 + 0.00424 × 4000 = 23.31 + 2.93 + 16.96 = 43.2 mm.",
why_wrong="Common mistake: forgetting the intercept, or multiplying body mass by the bill depth coefficient.",
hint="Multiply each predictor by its own coefficient."),

dict(id="ch20-quiz-07", source="Multiple regression quiz (2026), Q7", topics="effect sizes, units", type="MC",
question=PENG + "\n\nIn Model 3, the bill_dep coefficient is about 40 times larger than the body_mass coefficient. Does this show that bill depth is more important than body mass for predicting bill length?",
options="""A) Yes, the larger coefficient means a stronger effect
B) No, body mass is more important because it is measured more precisely
C) No, the smaller coefficient means a stronger effect
D) We can't tell from these coefficients""",
answer="D",
explanation="Coefficients depend on units: bill depth is in mm and body mass in grams. A 1-gram change is tiny; a 1-mm change in depth is not. Compare effect sizes on a common scale (standardized coefficients or partial R²).",
why_wrong="""A) and C) Raw coefficients aren't comparable across units.
B) Precision isn't the issue.""",
hint="What would the body_mass coefficient be if mass were in kg?"),

dict(id="ch20-quiz-08", source="Multiple regression quiz (2026), Q8", topics="multicollinearity", type="TF",
question=PENG + "\n\nTRUE or FALSE: Because the two explanatory variables in Model 3 are significantly associated (r² = 0.22, F₁,₃₄₀ = 97.4, p < 2.2 × 10⁻¹⁶), multicollinearity is likely a big problem.",
options="""A) TRUE
B) FALSE""",
answer="B",
explanation="Significance isn't strength: with 342 penguins even modest correlations are highly significant. Here r² = 0.22, so the VIF = 1 / (1 - 0.22) ≈ 1.3, far below levels that worry us (about 5 to 10).",
why_wrong="TRUE: confuses a significant correlation with a strong one.",
hint="How much of each predictor's variation is shared (r²)? What VIF does that imply?"),

dict(id="ch20-quiz-09", source="Multiple regression quiz (2026), Q8 (explain)", topics="multicollinearity", type="open", include="no",
question=PENG + "\n\nThe two explanatory variables in Model 3 are significantly associated (r² = 0.22, F₁,₃₄₀ = 97.4, p < 2.2 × 10⁻¹⁶). Is multicollinearity likely a big problem? Explain.",
answer="Model answer: No. A significant association isn't a strong one; with 342 penguins even a modest correlation gives a tiny p-value. Multicollinearity depends on how strongly the predictors are related: r² = 0.22 means they share only about a fifth of their variation, and the VIF = 1 / (1 - r²) ≈ 1.3, well below the 5 to 10 range where we'd worry. Correlated predictors are expected; adjusting for them is the point of multiple regression.",
explanation="Key ideas: significance depends on sample size; multicollinearity depends on strength (r², VIF).",
hint="What would r² need to be for the VIF to reach 5?"),

dict(id="ch20-quiz-10", source="Multiple regression quiz (2026), Q9", topics="Type II sums of squares, NHST", type="MC",
question=PENG3 + "\n\nWhich explanatory variable(s) are significantly associated with bill length (α = 0.05), after accounting for the other?",
options="""A) Bill depth only
B) Body mass only
C) Neither
D) Both""",
answer="B",
explanation="In the Type II table, body mass is highly significant (F = 159, p < 2 × 10⁻¹⁶) and bill depth isn't (F = 1.4, p = 0.23).",
why_wrong="A), C) and D) Read the p-values in the Anova table.",
hint="Use the car::Anova() table."),

dict(id="ch20-quiz-11", source="Multiple regression quiz (2026), Q10", topics="effect sizes, partial R squared", type="MC",
question=PENG3 + "\n\nWhich variable explains more variation in bill length, and how can you tell?",
options="""A) Bill depth, because its coefficient is larger
B) Body mass: its partial R² is 0.32 vs 0.004 for bill depth
C) Bill depth, because its VIF is higher
D) They explain the same amount, because their VIFs are equal""",
answer="B",
explanation="Partial R² puts both terms on the same scale: after accounting for bill depth, body mass explains about 32% of the remaining variation in bill length; bill depth explains under 1%.",
why_wrong="""A) Coefficients depend on units.
C) and D) VIFs measure overlap between predictors, not how much each explains.""",
hint="Which output compares terms on a common scale?"),

dict(id="ch20-quiz-12", source="Multiple regression quiz (2026), Q11", topics="multicollinearity, VIF", type="MC",
question=PENG3 + "\n\nHow worried should we be about multicollinearity?",
options="""A) Not worried: VIFs of 1.3 are well below 5 to 10
B) Very worried: the two predictors are correlated
C) Very worried: any VIF above 1 is a problem
D) We can't tell without a p-value for the VIF""",
answer="A",
explanation="A VIF of 1.3 means the uncertainty in each coefficient is inflated only slightly by the overlap between predictors.",
why_wrong="""B) Some correlation is expected and fine.
C) VIF = 1 means no overlap at all; slightly above 1 is normal.
D) VIF is the measure; no p-value is needed.""",
hint="At roughly what VIF do people start to worry?"),

dict(id="ch20-quiz-13", source="Multiple regression quiz (2026), Q12", topics="adjusting for variables, confounding", type="MC",
question="""Palmer penguins: we modeled bill length (mm) two ways:

Model 3: lm(bill_len ~ bill_dep + body_mass)
bill_dep = 0.16 (p = 0.23); body_mass = 0.0042 (p < 0.001); R² = 0.36

Model 4: lm(bill_len ~ species + bill_dep + body_mass)
bill_dep = 0.71 (p < 0.001); body_mass = 0.0027 (p < 0.001); R² = 0.82

What changed, and why?""",
options="""A) Nothing important; adding species just raised R²
B) Bill depth turned positive: within species, deeper bills are longer
C) Bill depth became significant because species causes bill depth
D) Body mass stopped mattering once species was added to the model""",
answer="B",
explanation="Without species, between-species differences mask the within-species pattern. Each coefficient describes an association after adjusting for the other terms, so adding a variable can change it a lot. It's still a conditional association, not proof of cause.",
why_wrong="""A) The bill depth coefficient changed more than fourfold.
C) Adjusting doesn't establish causation.
D) Body mass is still significant.""",
hint="Compare the bill_dep coefficient and p-value between the models."),

# ---------------- Homework ----------------
dict(id="ch20-hw-01", source="Multiple regression homework, Q1", topics="Type II sums of squares, R", type="matching",
question="You're analyzing how diet and exercise affect weight loss. Match each blank:\n\n1. The type of sums of squares that best isolates each variable's contribution after accounting for the other\n2. The R function that calculates it\n3. The package that function comes from",
options="""A) Type II
B) Type I
C) Anova()
D) anova()
E) car
F) stats (base R)""",
answer="1-A, 2-C, 3-E",
explanation="Type II tests each term after adjusting for the others; car::Anova() calculates it. Base R's anova() uses sequential Type I sums of squares.",
why_wrong="Common mix-up: anova() (lowercase, Type I) vs Anova() (car, Type II).",
hint="Capitalization matters."),

dict(id="ch20-hw-02", source="Multiple regression homework, Q2", topics="Type I vs Type II sums of squares", type="MC",
question="You needed Type II sums of squares but couldn't install the package. So you ran two models with Type I (sequential) sums of squares, switching the order of the predictors, and recorded each variable's result from the model where it came second. Is this a reasonable way to get Type II results?",
options="""A) Of course not
B) Pretty much, yes
C) It depends on whether the experiment is balanced""",
answer="B",
explanation="With Type I, the last term is tested after all the others, which is exactly what Type II does for each term in an additive model. So 'each variable entered last' reproduces Type II.",
why_wrong="""A) It works for additive models.
C) In balanced designs Type I and II agree anyway, but this trick works either way.""",
hint="With Type I sums of squares, what is the last term adjusted for?"),

dict(id="ch20-hw-03", source="Multiple regression homework, Q3", topics="multicollinearity", type="MC",
question="In a model predicting seed output from both leaf size and plant height, the two predictors are highly correlated. What's the main consequence of this multicollinearity?",
options="""A) The overall fit (R²) becomes meaningless
B) The model's coefficients become unstable and hard to interpret
C) The model automatically violates normality
D) The model can no longer include categorical variables""",
answer="B",
explanation="When predictors overlap strongly, the data have little information about one changing while the other stays fixed, so coefficients get large SEs and can swing between samples.",
why_wrong="""A) Overall fit is fine; it's the separate contributions that are unclear.
C) and D) Unrelated.""",
hint="What's hard to estimate when two predictors always move together?"),

dict(id="ch20-hw-04", source="Multiple regression homework, Q4", topics="adjusting vs controlling", type="MC",
question="A paper says the authors 'controlled for body mass' by including it in their regression. What's wrong with this wording?",
options="""A) Body mass is a continuous variable
B) Body mass was not experimentally manipulated (held constant); the model statistically adjusts for it
C) Regression cannot include body mass""",
answer="B",
explanation="'Controlled for' suggests an experiment where body mass was held fixed. Regression only adjusts for it statistically, and only as well as the model's assumptions (e.g. linearity) hold.",
why_wrong="""A) Continuous variables can be adjusted for.
C) It can.""",
hint="What would it mean to actually control body mass?"),

dict(id="ch20-hw-05", source="Multiple regression homework, Q5", topics="transformations, diagnostics", type="MC",
question=SR + "\n\nTwo models: Model 1 uses mean_visits as the response; Model 2 uses log1p(mean_visits). Their diagnostic plots are shown. Which better conforms to linear model assumptions?",
image="ch20-hw-sr-diag.png",
options="""A) Model 1 (mean_visits)
B) Model 2 (log1p_visits)
C) Both equally bad""",
answer="B",
explanation="Model 1's QQ plot curves up (right skew) and its residual spread grows with fitted values. After the log1p transform, the QQ plot is close to the line and the spread is more even.",
why_wrong="""A) Model 1 shows clear skew and fanning.
C) Neither is perfect, but Model 2 is clearly better.""",
hint="Compare the QQ plots and the residuals vs fitted plots."),

dict(id="ch20-hw-06", source="Multiple regression homework, Q6", topics="multicollinearity, VIF", type="MC",
question=SR + """

vif(lm(log1p_visits ~ petal_area_mm + asd_mm))
petal_area_mm  asd_mm
      1.068     1.068

cor.test(asd_mm, petal_area_mm): r = 0.33, p = 4.5 × 10⁻⁶

How worried about multicollinearity should we be?""",
options="""A) Not very worried
B) Somewhat worried
C) Very worried""",
answer="A",
explanation="The predictors are significantly correlated, but weakly (r = 0.33). The VIF of 1.07 means barely any inflation of uncertainty.",
why_wrong="""B) and C) The small p-value reflects the sample size, not strong overlap.""",
hint="Look at the VIF, not the p-value."),

dict(id="ch20-hw-07", source="Multiple regression homework, Q7", topics="predictions, multiple predictors", type="numeric",
question=SR + "\n\n" + SR_OUT + "\n\nPredict mean_visits for a plant with an ASD of 2 mm and a petal area of 100 mm².",
answer="2.92", explanation="-1.098 + 0.0302 × 100 + 0.498 × 2 = -1.098 + 3.02 + 0.996 = 2.92 visits.",
why_wrong="Common mistake: swapping the coefficients (0.0302 × 2 + 0.498 × 100).",
hint="Each coefficient multiplies its own variable."),

dict(id="ch20-hw-08", source="Multiple regression homework, Q8", topics="interpreting coefficients, adjusting", type="MC",
question=SR + "\n\nThe asd_mm coefficient in lm(mean_visits ~ petal_area_mm + asd_mm) is 0.50. This means mean visits increase by about 0.5 for every 1 mm increase in ASD...",
options="""A) without accounting for petal area
B) only for plants with a petal area of 0
C) because longer ASD causes more visits
D) after adjusting for petal area""",
answer="D",
explanation="In a multiple regression each coefficient is the association with that predictor holding the others in the model constant (statistically).",
why_wrong="""A) That would be a model with ASD alone.
B) In an additive model the ASD slope is the same at every petal area.
C) An association, not proven causation.""",
hint="What else is in the model?"),

dict(id="ch20-hw-09", source="Multiple regression homework, Q9", topics="Type I vs Type II sums of squares", type="MC",
question=SR + "\n\nA tablemate ran anova(lm(mean_visits ~ asd_mm + petal_area_mm)) and found ASD significant (p = 0.013). You ran car::Anova() on the same model and found it isn't (p = 0.13). Which result should you report?",
options="""A) Your tablemate's: the smaller p-value reflects more statistical power
B) Either: both functions test the same null hypothesis
C) It depends on whether you expected ASD to matter
D) Neither: conflicting results mean the model is invalid
E) Yours: Type II tests each term after adjusting for the other""",
answer="E",
explanation="anova() is sequential: ASD came first, so it was tested without adjusting for petal area (which is correlated with ASD). Type II tests ASD after accounting for petal area, which is the question we care about.",
why_wrong="""A) It's a different (and inappropriate) test, not more power.
B) They test different nulls.
C) Choosing tests based on what you hoped for is p-hacking.
D) The model is fine; the tests differ.""",
hint="What does anova() adjust the first term for?"),

dict(id="ch20-hw-10", source="Multiple regression homework, Q10", topics="Type II sums of squares, NHST", type="matching",
question=SR + "\n\n" + SR_OUT + "\n\nAt α = 0.05, what do you do to each null?\n\n1. Petal area is not associated with visitation (after adjusting for ASD)\n2. ASD is not associated with visitation (after adjusting for petal area)",
options="""A) Reject it
B) Fail to reject it""",
answer="1-A, 2-B",
explanation="Petal area: p = 0.0004, reject. ASD: p = 0.13, fail to reject.",
why_wrong="Common mistake: using p-values from anova() or summary() instead of the Type II table.",
hint="Use the car::Anova() p-values."),

dict(id="ch20-hw-11", source="Multiple regression homework, Q11", topics="causation, observational studies", type="MC",
question=SR + "\n\nAssume that after adjusting for ASD, petal area is significantly associated with visitation, and that we know the null is false. Can we conclude that larger petals cause more visits?",
options="""A) Yes: adjusting for ASD rules out all other explanations
B) Yes: the p-value for petal area is very small
C) No: petal area wasn't manipulated; other traits could explain it
D) No: we would need a much larger sample size to say""",
answer="C",
explanation="Adjusting for one variable doesn't rule out others (e.g. flower number or scent might be correlated with petal area). Causal claims need manipulation, or a careful causal argument.",
why_wrong="""A) Only ASD was adjusted for.
B) A small p-value says nothing about causation.
D) More data wouldn't fix confounding.""",
hint="What else might differ between big- and small-petaled RILs?"),

dict(id="ch20-hw-12", source="Multiple regression homework, Q12", topics="partial R squared", type="MC",
question=SR + "\n\n" + SR_OUT + "\n\nIn this study, after adjusting for each other, which trait explains more of the variation in pollinator visitation?",
options="""A) Petal area
B) ASD
C) They explain the same amount
D) Partial R² can't be compared between variables""",
answer="A",
explanation="Petal area's partial R² (0.109) is about five times ASD's (0.021). Partial R² is on a common scale, so it can be compared.",
why_wrong="""B) ASD's partial R² is smaller.
D) Comparing terms is exactly what partial R² is for.""",
hint="Compare the two partial R² values."),

# ---------------- ChimeIn (mole rats) ----------------
dict(id="ch20-chimein-01", source="Chime In (multiple regression), Q1", topics="why multiple regression", type="open", include="no",
question="Why use one model with more than one predictor, rather than a separate model for each explanatory variable?",
answer="Model answer: (1) Explanatory variables are often associated with each other, so a one-predictor model can attribute to one variable an effect that really belongs to another; a multiple regression estimates each association while adjusting for the others. (2) Accounting for a variable that explains a lot of the response reduces unexplained variation, making other effects easier to detect (more precision). Example: lazy mole rats are bigger, so comparing castes without accounting for body mass hides the caste difference.",
explanation="Two key reasons: confounding among predictors (the estimate changes) and precision (the uncertainty shrinks).",
hint="What happens if two predictors are correlated and you only include one?"),

dict(id="ch20-chimein-02", source="Chime In (multiple regression), Q2", topics="model building", type="open", include="no",
question="Why not include every possible explanatory variable in a model?",
answer="Model answer: Each term costs a degree of freedom, reducing power; with many terms a model can overfit, describing noise that won't hold for new data. Highly correlated predictors make coefficients unstable. Some variables shouldn't be adjusted for at all (e.g. a consequence of the focal predictor can hide its effect). And very large models are hard to interpret. Variables should be included for biological reasons tied to the question.",
explanation="Key ideas: power and overfitting, multicollinearity, adjusting for the wrong variables, and interpretability.",
hint="What does each extra term cost?"),

dict(id="ch20-chimein-03", source="Chime In (multiple regression), Q3-5", topics="response, explanatory variables, covariates", type="matching",
question=MOLE + "\n\nMatch each role to its variable:\n\n1. Response variable\n2. Covariate we wish to account for\n3. Key explanatory variable",
options="""A) Energy expenditure (lnEnergy)
B) Body mass (lnMass)
C) Caste""",
answer="1-A, 2-B, 3-C",
explanation="The question is whether castes differ in energy use (response) after accounting for body mass (covariate).",
why_wrong="Common mix-up: treating body mass as the main question. It's there because bigger animals use more energy.",
hint="What's the question the researchers care about?"),

dict(id="ch20-chimein-04", source="Chime In (multiple regression), Q9-10", topics="predictions, multiple predictors", type="matching",
question=MOLE + "\n\n" + MOLE_OUT + "\n\nMatch each mole rat to its predicted lnEnergy:\n\n1. A lazy mole rat with lnMass = 4.8\n2. A worker with lnMass = 4.8",
options="""A) 4.19
B) 4.58
C) 4.29
D) 0.39""",
answer="1-A, 2-B",
explanation="Lazy (reference): -0.097 + 0.893 × 4.8 = 4.19. Worker: 4.19 + 0.393 = 4.58.",
why_wrong="D) is just the caste difference.",
hint="Lazy is the reference level."),

dict(id="ch20-chimein-05", source="Chime In (multiple regression), Q12", topics="plots should match models", type="MC",
question=MOLE + "\n\nThe model is lm(lnEnergy ~ caste + lnMass), but this plot was made with geom_smooth(method = 'lm'), which fits a separate line to each caste. What's wrong, and how would you fix it?",
image="ch20-chimein-molerat-sep.png",
options="""A) Nothing; the lines are the model's predictions
B) Its slopes differ, but the model has one; plot the model's fit
C) The axes should be swapped so lnMass is on the y-axis
D) The points should be removed so only the lines remain""",
answer="B",
explanation="An additive model (caste + lnMass) forces the same slope for both castes. Separate geom_smooth() lines suggest an interaction the model doesn't include. The plot should match the model.",
why_wrong="""A) geom_smooth() fits its own separate regressions.
C) and D) Not the problem.""",
hint="Does the model allow different slopes for each caste?"),

dict(id="ch20-chimein-06", source="Chime In (multiple regression), Q14", topics="regression assumptions, diagnostics", type="MC",
question=MOLE + "\n\nConsider these diagnostic plots for lm(lnEnergy ~ caste + lnMass). Which assumption, if any, do they suggest we may break?",
image="ch20-chimein-molerat-diag.png",
options="""A) Linearity (the residuals curve with fitted values)
B) Normality of residuals (the QQ plot bends away)
C) Homoscedasticity (equal variance of residuals)
D) None of these shows a clear problem""",
answer="D",
explanation="Residuals scatter evenly around zero with no curve, the QQ plot follows the line reasonably well, and the spread looks even. These plots can't tell us about independence or bias, which depend on the study design.",
why_wrong="A), B) and C) No clear pattern in the plots.",
hint="Look for curvature, fanning and departures from the QQ line."),

dict(id="ch20-chimein-07", source="Chime In (multiple regression), Q16-17", topics="Type II sums of squares, NHST", type="MC",
question=MOLE + "\n\n" + MOLE_OUT + "\n\nThe key question is whether castes differ in energy expenditure after accounting for body mass. Which null do we most care about, and what do we do with it?",
options="""A) Slope of lnMass = 0; reject it (p < 0.001)
B) No difference between castes after adjusting for mass; reject it (p = 0.011)
C) No difference between castes after adjusting for mass; fail to reject it
D) Intercept = 0; reject it""",
answer="B",
explanation="Caste is the key explanatory variable. Its Type II test (adjusted for lnMass) gives F = 7.25, p = 0.011 < 0.05, so we reject. Workers use more energy than lazy rats of the same mass.",
why_wrong="""A) Mass is the covariate, not the question.
C) p is below 0.05.
D) The intercept isn't biologically meaningful here.""",
hint="Which variable is the question about?"),

# ---------------- Book: Multiple regression summary (iris) ----------------
dict(id="ch20-book-01", source="Book: Multiple regression summary (Q1)", topics="explanatory variables", type="MC",
question=IRIS + "\n\nHow many explanatory variables does this model include?",
options="""A) One
B) Two
C) Three
D) Four""",
answer="B",
explanation="Sepal length and species. Species has three levels, so it gets two coefficients, but it's still one variable.",
why_wrong="C) and D) Count coefficients, not variables.",
hint="Variables vs coefficients."),

dict(id="ch20-book-02", source="Book: Multiple regression summary (Q2)", topics="interpreting coefficients, adjusting", type="MC",
question=IRIS + "\n\nThe Sepal.Length coefficient (0.63) is the expected change in petal length for a 1 cm increase in sepal length:",
options="""A) Without accounting for species
B) After controlling for species
C) After adjusting for species and petal width
D) Only for setosa plants
E) After adjusting for species""",
answer="E",
explanation="It's the shared within-species slope, after statistically adjusting for species.",
why_wrong="""A) Species is in the model.
B) 'Controlling' implies an experiment.
C) Petal width isn't in the model.
D) In an additive model the slope is the same for all species.""",
hint="What else is in the model, and how was it 'held constant'?"),

dict(id="ch20-book-03", source="Book: Multiple regression summary (Q3)", topics="categorical predictors, adjusting", type="MC",
question=IRIS + "\n\nThe Speciesversicolor coefficient (2.21) compares versicolor petal length to:",
options="""A) The average petal length of the other two species
B) Setosa petal length, without accounting for sepal length
C) Virginica petal length, after adjusting for sepal length
D) Setosa petal length, after adjusting for sepal length""",
answer="D",
explanation="Setosa is the reference level, and the comparison is at the same sepal length.",
why_wrong="""A) Coefficients compare to the reference, not to an average.
B) Sepal length is in the model.
C) Virginica isn't the reference.""",
hint="Which species is the reference?"),

dict(id="ch20-book-04", source="Book: Multiple regression summary (Q4)", topics="adjusting vs controlling", type="MC",
question=IRIS + "\n\nIt is better to say this model 'adjusts for species' rather than 'controls for species' because:",
options="""A) Species is a categorical variable
B) The model cannot include species
C) Species has more than two levels
D) Species was not experimentally manipulated (whatever that would mean)""",
answer="D", near_duplicate_of="ch20-hw-04",
explanation="'Control' implies we held species fixed by design; regression adjusts statistically.",
why_wrong="A), B) and C) Not the reason.",
hint="What's the difference between an experiment and a statistical adjustment?"),

dict(id="ch20-book-05", source="Book: Multiple regression summary (Q5-6)", topics="plots should match models", type="MC",
question=IRIS + "\n\nThe figure shows two ways to plot these data. Which plot matches the model lm(Petal.Length ~ Sepal.Length + Species), and how was it made?",
image="ch20-book-iris-slopes.png",
options="""A) A, because each species gets its own slope; made with geom_smooth(method = 'lm')
B) B, because all species share the same slope; made with geom_lm_smooth()
C) A, because its lines fit each species best; made with geom_lm_smooth()
D) It's a matter of opinion""",
answer="B",
explanation="An additive model gives each species its own intercept but one shared slope: parallel lines (B). geom_smooth(method = 'lm') fits separate slopes (A), which would correspond to an interaction model.",
why_wrong="""A) and C) Separate slopes don't match an additive model.
D) Whether a plot matches a model is a fact.""",
hint="Are the lines in each panel parallel?"),

dict(id="ch20-book-06", source="Book: Multiple regression summary (Q7-8)", topics="summary() output, coefficient p-values", type="MC",
question=IRIS + "\n\nsummary() gives a separate p-value for Speciesversicolor and Speciesvirginica. Why aren't these our main tests of whether species matters?",
options="""A) R calculated them incorrectly
B) They test individual coefficients (each a comparison to setosa, after adjusting for sepal length), not the species term as a whole
C) p-values can't be calculated for linear models
D) They are post-hoc tests""",
answer="B",
explanation="Each row compares one species to the reference. To test whether species matters at all (after adjusting for sepal length), use the Type II test from car::Anova().",
why_wrong="""A) They're correct for what they test.
C) They can be.
D) They aren't corrected, all-pairs comparisons; post-hoc tests come from emmeans.""",
hint="How many species comparisons does summary() show, and against what?"),

dict(id="ch20-book-07", source="Book: Multiple regression summary (Q9-10)", topics="Type I vs Type II sums of squares", type="matching",
question="Match each R function to what it does for a multiple regression:\n\n1. car::Anova(model, type = 'II')\n2. anova(model)",
options="""A) Tests each term after accounting for the other terms in the additive model
B) Uses sequential (Type I) sums of squares, so results depend on the order of terms
C) Tests only the intercept
D) Tests whether residuals are normal""",
answer="1-A, 2-B",
explanation="Type II asks about each term given the others. Base R's anova() adds terms one at a time, so earlier terms aren't adjusted for later ones.",
why_wrong="C) and D) Neither function does that.",
hint="Lowercase anova() is sequential."),

dict(id="ch20-book-08", source="Book: Multiple regression summary (Q11-13)", topics="post-hoc tests, adjusted means", type="MC",
question=IRIS + """

emmeans(iris_model, ~ Species)
 Species    emmean
 setosa       1.99
 versicolor   4.20
 virginica    5.08

contrast(..., method = "pairwise", adjust = "tukey")
 setosa - versicolor     -2.21  p < 0.0001
 setosa - virginica      -3.09  p < 0.0001
 versicolor - virginica  -0.88  p < 0.0001

What are these means, and what do the contrasts ask?""",
options="""A) Raw species means; whether each species is normally distributed
B) Means at average sepal length; which species differ, adjusted
C) Residuals; which individual flowers are outliers in the data
D) Raw species means; which terms should be entered first""",
answer="B",
explanation="emmeans gives each species' predicted petal length at the same (average) sepal length. The Tukey contrasts compare every pair, after adjusting for sepal length and for multiple comparisons.",
why_wrong="""A) and D) They aren't raw means: they're adjusted for sepal length.
C) Not residuals.""",
hint="At what sepal length are these means calculated?"),

dict(id="ch20-book-09", source="Book: Multiple regression summary (Q14-15)", topics="effect sizes, partial R squared", type="matching",
question=IRIS + "\n\nMatch each question to its answer:\n\n1. Why is it hard to compare the raw coefficient for Sepal.Length to the coefficient for Speciesversicolor?\n2. What does partial R² tell us that coefficients don't?",
options="""A) They describe different kinds of comparisons (per cm vs one species vs another)
B) How much variation in the response is associated with a term after accounting for the others
C) Which variable causes the response
D) Coefficients are always unitless""",
answer="1-A, 2-B",
explanation="One coefficient is a slope per cm, the other a difference between groups, so their sizes aren't comparable. Partial R² puts terms on a common scale: the share of remaining variation each explains.",
why_wrong="C) Partial R² doesn't show causation. D) Coefficients have units.",
hint="What units does each coefficient have?"),
]
