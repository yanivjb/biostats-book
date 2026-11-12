OLY = "Olympic sprinters keep getting faster. To ask whether winning times in the 100 m have fallen at different rates for men and women, we looked at gold-medal times (seconds) from 1900 to 2004 (women's results start in 1928)."
OADD = """lm(Time ~ Year + Gender)
(Intercept) = 36.0528; Year = -0.01261; Gendermale = -1.0928"""
OINT = """lm(Time ~ Year * Gender)
(Intercept) = 44.3470; Year = -0.016822; Gendermale = -12.5206; Year:Gendermale = 0.005817"""
OSUM = """lm(Time ~ Year * Gender) |> summary()
                  Estimate  Std. Error  t value  Pr(>|t|)
(Intercept)       44.3470    3.4760     12.76    < 0.001
Year              -0.0168    0.0018     -9.53    < 0.001
Gendermale       -12.5206    4.0760     -3.07     0.004
Year:Gendermale    0.0058    0.0021      2.80     0.008"""
GC = "To ask which floral traits predict hybridization, we modeled the proportion of hybrid seed on 93 parviflora RILs planted at the GC site as a function of petal area (mm²) and petal color (pink or white)."
GC_ANOVA = """lm(prop_hybrid ~ petal_area_mm * petal_color)

Type II (car::Anova(model, type = "II")):
                           F      p
petal_color            39.57  <0.0001
petal_area_mm          18.85  <0.0001
petal_area_mm:petal_color  8.33  0.0049

Type III (car::Anova(model, type = "III")):
                           F      p
petal_color             1.91  0.170
petal_area_mm          26.09  <0.0001
petal_area_mm:petal_color  8.33  0.0049"""
PMASS = "Palmer penguins: we modeled body mass (g) of three Antarctic penguin species as a function of sex and species, with and without an interaction:\n\npenguin_additive_model <- lm(body_mass ~ sex + species)\npenguin_interaction_model <- lm(body_mass ~ sex + species + sex:species)"
PADD = """lm(body_mass ~ sex + species)
(Intercept) = 3372; sexmale = 668; speciesChinstrap = 27; speciesGentoo = 1378"""
PINT = """lm(body_mass ~ sex + species + sex:species)
(Intercept) = 3369; sexmale = 675; speciesChinstrap = 158; speciesGentoo = 1311;
sexmale:speciesChinstrap = -263; sexmale:speciesGentoo = 130"""
PSUM = """summary(penguin_interaction_model)
                         Estimate Std. Error t value Pr(>|t|)
(Intercept)               3368.84      36.21  93.030  < 2e-16
sexmale                    674.66      51.21  13.174  < 2e-16
speciesChinstrap           158.37      64.24   2.465  0.01420
speciesGentoo             1310.91      54.42  24.088  < 2e-16
sexmale:speciesChinstrap  -262.89      90.85  -2.894  0.00406
sexmale:speciesGentoo      130.44      76.44   1.706  0.08886"""
PEMM = """emmeans(penguin_interaction_model, pairwise ~ sex)
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
Results are averaged over the levels of: sex"""
FLIP = """Palmer penguins: we modeled body mass (g) as a function of flipper length (mm), species, and their interaction:

lm(body_mass ~ flipper_len * species)
(Intercept) = -2536.0; flipper_len = 32.80; speciesChinstrap = -501.0; speciesGentoo = -4251.0;
flipper_len:speciesChinstrap = 1.74; flipper_len:speciesGentoo = 21.80"""

ROWS = [
# ---------------- Quiz: Olympic 100 m ----------------
dict(id="ch21-quiz-01", source="Interactions quiz (2026), Q1", topics="plotting, interactions", type="MC",
question=OLY + "\n\nWhat trend does the plot suggest?",
image="ch21-quiz-olympics.png",
options="""A) Both are getting faster, with women's times falling more steeply
B) Both men and women are getting faster at exactly the same rate
C) Men are getting faster, but women's times are not changing
D) Women are now faster than men in the most recent Olympics""",
answer="A",
explanation="Times drop over the years for both groups (lower time = faster). Women's times fall from about 12.2 s in 1928 to about 10.9 s, a steeper drop than men's over the same years, so the gap seems to be narrowing. Whether that difference in slopes is real is what the interaction tests.",
why_wrong="""B) The women's points fall more steeply than the men's.
C) Women's times clearly fall.
D) Women's times are still about 1 s slower.""",
hint="Lower times mean faster runners. Compare how steeply each set of points falls."),

dict(id="ch21-quiz-02", source="Interactions quiz (2026), Q2", topics="additive models, predictions", type="numeric",
question=OLY + "\n\nA model with NO interaction:\n\n" + OADD + "\n\n(Gendermale is 1 for men and 0 for women.) What winning time does this model predict for the MEN'S 100 m in 1940? Round to two decimal places.",
answer="10.50",
explanation="36.0528 - 0.01261 × 1940 - 1.0928 = 36.0528 - 24.463 - 1.0928 ≈ 10.50 s. (There were no Olympics in 1940; the model still gives a prediction because 1940 is within the range of the data.)",
hint="Plug in Year = 1940 and Gendermale = 1."),

dict(id="ch21-quiz-03", source="Interactions quiz (2026), Q2", topics="additive models, predictions", type="numeric",
question=OLY + "\n\nA model with NO interaction:\n\n" + OADD + "\n\n(Gendermale is 1 for men and 0 for women.) What winning time does this model predict for the WOMEN'S 100 m in 1940? Round to two decimal places.",
answer="11.59",
explanation="Women are the reference level, so Gendermale = 0: 36.0528 - 0.01261 × 1940 = 36.0528 - 24.463 ≈ 11.59 s.",
hint="Plug in Year = 1940 and Gendermale = 0."),

dict(id="ch21-quiz-04", source="Interactions quiz (2026), Q3", topics="interactions, predictions", type="numeric",
question=OLY + "\n\nA model WITH an interaction:\n\n" + OINT + "\n\n(Gendermale is 1 for men and 0 for women.) What winning time does this model predict for the MEN'S 100 m in 1940? Round to two decimal places.",
answer="10.48",
explanation="44.3470 - 0.016822 × 1940 - 12.5206 + 0.005817 × 1940 = 44.3470 - 32.635 - 12.5206 + 11.285 ≈ 10.48 s. For men, the slope is -0.016822 + 0.005817 = -0.011005 s per year.",
hint="With Gendermale = 1, every term is in play, including Year × Gendermale."),

dict(id="ch21-quiz-05", source="Interactions quiz (2026), Q3", topics="interactions, predictions", type="numeric",
question=OLY + "\n\nA model WITH an interaction:\n\n" + OINT + "\n\n(Gendermale is 1 for men and 0 for women.) What winning time does this model predict for the WOMEN'S 100 m in 1940? Round to two decimal places.",
answer="11.71",
explanation="With Gendermale = 0, both gender terms drop out: 44.3470 - 0.016822 × 1940 = 44.3470 - 32.635 ≈ 11.71 s.",
hint="With Gendermale = 0, which terms drop out?"),

dict(id="ch21-quiz-06", source="Interactions quiz (2026), Q4", topics="interpreting interactions", type="MC",
question=OLY + "\n\n" + OSUM + "\n\nWomen are the reference level. The interaction term suggests that over the past 100 or so years, male gold medalists have been getting faster at:",
options="""A) A rate not significantly different from women's
B) A significantly slower rate than women
C) A significantly faster rate than women""",
answer="B",
explanation="Women's times fall by 0.0168 s per year. The positive Year:Gendermale term (0.0058, p = 0.008) means men's slope is less steep: -0.0168 + 0.0058 = -0.0110 s per year. Men are improving more slowly than women, and the difference in slopes is significant.",
why_wrong="""A) p = 0.008 for the interaction, so the slopes differ significantly.
C) A positive interaction makes men's negative slope closer to zero, so men are improving more slowly.""",
hint="The men's slope is Year + Year:Gendermale. Is that more or less negative than the women's slope?"),

dict(id="ch21-quiz-07", source="Interactions quiz (2026), Q5", topics="extrapolation, interactions", type="TF",
question=OLY + "\n\nTRUE or FALSE: We can find the year when women's winning 100 m times will be faster than men's by following the lines from the interaction model into the future until they cross.",
options="""A) TRUE
B) FALSE""",
answer="B",
explanation="That's an extreme extrapolation: the lines would cross around 2150, far beyond the data. Straight lines can't continue forever (they'd eventually predict negative times), and improvement slows as athletes approach physical limits. The model describes the years we have data for.",
why_wrong="TRUE: the arithmetic gives a year, but the prediction lies far outside the data.",
hint="Would a straight line still describe winning times 150 years from now?"),

dict(id="ch21-quiz-08", source="Interactions quiz (2026), follow-up", topics="interactions, interpreting coefficients", type="MC",
question=OLY + "\n\n" + OINT + "\n\nWomen are the reference level. What does the Gendermale coefficient (-12.52) represent?",
options="""A) The average difference between men's and women's winning times across all years
B) How much faster men's times have improved per year compared with women's
C) The predicted difference between men's and women's winning times in the year 0
D) The men's winning time in the first Olympics""",
answer="C",
explanation="In an interaction model, a main-effect coefficient is the difference when the other variable equals zero: here, the year 0. That's almost 2,000 years before the first modern Olympics, so the coefficient is huge and meaningless on its own (the real gap is about 1 s).",
why_wrong="""A) In an interaction model the gap changes with year.
B) That's the Year:Gendermale interaction coefficient.
D) Coefficients for categories are differences, not times.""",
hint="What is the value of Year when the gender coefficient applies?"),

dict(id="ch21-quiz-09", source="Interactions quiz (2026), follow-up", topics="centering, interactions", type="select-all",
question=OLY + "\n\n" + OINT + "\n\nWe make a new variable, years_since_1928 = Year - 1928, and refit the interaction model with it in place of Year. Which of these change? (Select all that apply.)",
options="""A) The Gendermale coefficient
B) The slope for women
C) The interaction coefficient
D) The predicted winning times for 1960""",
answer="A",
explanation="Shifting Year only moves where 'zero' is. The Gendermale coefficient now gives the men-women gap in 1928 (the first Olympics with a women's 100 m): about -1.31 s instead of -12.52. Slopes, the interaction and all predictions stay the same.",
why_wrong="B), C) and D) Subtracting a constant from x doesn't change slopes or predictions.",
hint="What does subtracting 1928 from every year change about the lines themselves?"),

# ---------------- Homework (GC RILs) ----------------
dict(id="ch21-hw-01", source="Interactions homework, Q1", topics="when to include interactions", type="MC",
question="When should you include an interaction in your model? (Choose the best answer.)",
options="""A) When you have enough degrees of freedom to evaluate it
B) When your sample size is greater than 100
C) When an interaction is scientifically meaningful for your question
D) Whenever you have two variables
E) When one of the variables is not numeric""",
answer="C",
explanation="Include an interaction when there's a biological reason to expect the effect of one variable to depend on another, and when you have the data to estimate it.",
why_wrong="""A) and B) Enough data is necessary but not a reason by itself.
D) Adding every possible interaction wastes power and invites overfitting.
E) Variable type doesn't matter.""",
hint="Start from the biology."),

dict(id="ch21-hw-02", source="Interactions homework, Q2", topics="main effects, interactions", type="MC",
question="When is it reasonable to interpret main effects even when there is a significant interaction?",
options="""A) Never
B) Whenever the p-value is less than α
C) When the direction of the effect is consistent across all values of the other variable
D) When the main effect's p-value is smaller than the interaction's""",
answer="C",
explanation="If, say, males are heavier in every species but by different amounts, it's fair to say 'males are heavier' while noting that the size of the difference varies.",
why_wrong="""A) Too strict: consistent effects are still meaningful.
B) and D) p-values don't decide this.""",
hint="Does the effect ever flip direction?"),

dict(id="ch21-hw-03", source="Interactions homework, Q3", topics="plots should match models", type="matching",
question=GC + "\n\nEach panel shows the same data with lines from a different model. Match each panel to its explanatory variables:\n\n1. Panel A\n2. Panel B\n3. Panel C\n4. Panel D",
image="ch21-hw-four-models.png",
options="""A) Petal area only
B) Petal area, petal color, and their interaction
C) Petal area and petal color (additive)
D) Petal color only""",
answer="1-A, 2-B, 3-C, 4-D",
explanation="A: one line for everyone (petal area only). B: different slopes for each color (interaction). C: parallel lines (additive). D: flat lines at each color's mean (color only).",
why_wrong="Look for: one line vs two; parallel vs not; sloped vs flat.",
hint="Are there two lines? Are they parallel? Are they flat?"),

dict(id="ch21-hw-04", source="Interactions homework, Q4", topics="diagnostics, assumptions", type="matching",
question=GC + "\n\nDiagnostic plots for lm(prop_hybrid ~ petal_area_mm * petal_color) are shown. Fill in: The residuals are (1) ____, and the variance in residuals is (2) ____.",
image="ch21-hw-diag.png",
options="""A) not normally distributed
B) normally distributed
C) heteroscedastic
D) homoscedastic""",
answer="1-A, 2-C",
explanation="The QQ plot curves away from the line (many zeros and a long right tail), and the spread of residuals grows with the fitted values.",
why_wrong="Proportions with many zeros rarely give normal, equal-variance residuals.",
hint="Look at the QQ plot and the scale-location plot."),

dict(id="ch21-hw-05", source="Interactions homework, Q5", topics="Type II vs Type III sums of squares", type="select-all",
question=GC + "\n\n" + GC_ANOVA + "\n\nWhich terms are significantly associated with proportion hybrid seed with BOTH Type II and Type III sums of squares? (Select all that apply.)",
options="""A) Petal area
B) The interaction between petal color and petal area
C) Petal color""",
answer="A, B",
explanation="Petal area and the interaction are significant either way. Petal color is significant with Type II but not Type III, because Type III tests color at a petal area of zero (with R's default contrasts), far outside the data.",
why_wrong="C) Not significant with Type III.",
hint="Check each term in both tables."),

dict(id="ch21-hw-06", source="Interactions homework, Q6", topics="interpreting interactions", type="MC",
question=GC + "\n\nThe interaction between petal color and petal area is significant. With the usual caveats about NHST, this means:",
options="""A) The predicted effect of petal area on proportion hybrid seed depends on petal color
B) Petal color and petal area are significantly correlated
C) Both petal color and petal area have significant main effects
D) The relationship between petal area and hybrid proportion is the same for both colors""",
answer="A",
explanation="An interaction means the slope for one variable differs across values of the other: here, hybrid seed rises more steeply with petal area in pink than in white flowers.",
why_wrong="""B) Correlation between predictors is a different issue (multicollinearity).
C) An interaction says nothing about main effects.
D) That's the null hypothesis we rejected.""",
hint="What does 'interaction' mean in words?"),

dict(id="ch21-hw-07", source="Interactions homework, Q7", topics="predictions, interactions", type="numeric",
question="""To ask how petal area and anther-stigma distance (ASD) together predict hybridization in Clarkia RILs at GC, we fit:

lm(prop_hybrid ~ petal_area_mm * asd_mm)
(Intercept) = 0.300950; petal_area_mm = -0.004660; asd_mm = -0.448186; petal_area_mm:asd_mm = 0.009506

Predict the proportion (not percent) of hybrid seed for a RIL with an ASD of 2 mm and a petal area of 100 mm².""",
answer="0.84", explanation="0.30095 + (-0.00466 × 100) + (-0.448186 × 2) + (0.009506 × 100 × 2) = 0.301 - 0.466 - 0.896 + 1.901 = 0.84.",
why_wrong="Common mistake: forgetting that the interaction term multiplies petal area by ASD (100 × 2 = 200).",
hint="The interaction coefficient multiplies the product of the two predictors."),

# ---------------- ChimeIn ----------------
dict(id="ch21-chimein-01", source="Chime In (interactions), Q1", topics="main effects, interactions, visualizing", type="select-all",
question="Palmer penguins: bill length of three Antarctic penguin species by sex. What does this plot show? (Select all that apply.)",
image="ch21-chimein-bill-sex-species.png",
options="""A) A main effect of sex
B) A main effect of species
C) An interaction between sex and species""",
answer="A, B",
explanation="Males have longer bills than females in every species (sex effect), and species differ (species effect). The male-female gap is similar across species; a formal test finds no significant interaction (p = 0.10).",
why_wrong="C) The gaps differ a little (largest in Chinstraps), but not by more than we'd expect from noise.",
hint="Is the male-female gap about the same size in each species?"),

dict(id="ch21-chimein-02", source="Chime In (interactions), Q2", topics="main effects, interactions, visualizing", type="select-all",
question="Iris petal length vs petal width for three iris species, with a separate regression line for each species. What does this plot show? (Select all that apply.)",
image="ch21-chimein-iris-petal.png",
options="""A) A main effect of petal width
B) A main effect of species
C) An interaction between petal width and species""",
answer="A, B, C",
explanation="Petal length rises with width, species differ, and the slopes differ clearly among species (interaction p < 0.001). Note that the species barely overlap in petal width, so each slope covers a different range.",
why_wrong="All three are present.",
hint="Are the slopes similar across species?"),

dict(id="ch21-chimein-03", source="Chime In (interactions), Q3", topics="main effects, interactions, visualizing", type="select-all",
question="Iris sepal length vs sepal width for three iris species, with a separate regression line for each species. What does this plot show? (Select all that apply.)",
image="ch21-chimein-iris-sepal.png",
options="""A) A main effect of sepal width
B) A main effect of species
C) An interaction between sepal width and species""",
answer="A, B",
explanation="Sepal length rises with sepal width, and species differ, but the lines are roughly parallel (interaction p = 0.67).",
why_wrong="C) The slopes are similar.",
hint="Are the lines roughly parallel?"),

dict(id="ch21-chimein-04", source="Chime In (interactions), Q4-6", topics="predictions, interactions", type="matching",
question=FLIP + "\n\nMatch each penguin (flipper length 200 mm) to its predicted body mass:\n\n1. Adelie\n2. Chinstrap\n3. Gentoo",
options="""A) 4024 g
B) 3871 g
C) 4133 g
D) 6560 g""",
answer="1-A, 2-B, 3-C",
explanation="Adelie: -2536 + 32.8 × 200 = 4024. Chinstrap: -2536 - 501 + (32.8 + 1.74) × 200 = 3871. Gentoo: -2536 - 4251 + (32.8 + 21.8) × 200 = 4133.",
why_wrong="Common mistake: forgetting to add the interaction to the slope for Chinstrap or Gentoo.",
hint="Each species gets its own intercept and its own slope."),

dict(id="ch21-chimein-05", source="Chime In (interactions), follow-up", topics="interactions, interpreting coefficients", type="MC",
question=FLIP + "\n\nGentoo are the heaviest penguins, yet speciesGentoo = -4251. Why?",
options="""A) The model is wrong and should be refit
B) It's the difference at 0 mm flipper length, far outside the data
C) Gentoos are actually lighter than Adelies of the same size
D) Negative coefficients mean the variable isn't significant""",
answer="B",
explanation="With an interaction, a species coefficient is the difference when flipper length = 0. Because the Gentoo slope is much steeper (54.6 vs 32.8 g/mm), the lines cross well below real flipper lengths. At realistic lengths, Gentoos are predicted to be heavier.",
why_wrong="""A) The model fits fine.
C) They aren't.
D) Sign and significance are unrelated.""",
hint="At what flipper length does the species coefficient apply?"),

# ---------------- Book: Interactions summary (penguin body mass) ----------------
dict(id="ch21-book-01", source="Book: Interactions summary (Q1)", topics="interactions", type="MC",
question=PMASS + "\n\nThe sex:species interaction asks whether:",
options="""A) Male penguins are heavier than female penguins
B) Penguin species differ in average body mass
C) The male-female difference in body mass differs among species
D) The proportion of males and females differs among species""",
answer="C",
explanation="An interaction asks whether the effect of one variable (sex) depends on the other (species).",
why_wrong="""A) That's the main effect of sex.
B) That's the main effect of species.
D) Not a question about body mass.""",
hint="'The effect of A depends on B.'"),

dict(id="ch21-book-02", source="Book: Interactions summary (Q2-3)", topics="predictions, additive models", type="matching",
question=PMASS + "\n\n" + PADD + "\n\nUsing the additive model, match each penguin to its predicted body mass:\n\n1. Female Gentoo\n2. Male Gentoo",
options="""A) 4750 g
B) 5418 g
C) 4680 g
D) 5485 g""",
answer="1-A, 2-B",
explanation="Female Gentoo: 3372 + 1378 = 4750. Male Gentoo: 4750 + 668 = 5418.",
why_wrong="C) and D) come from the interaction model.",
hint="Female is the reference sex."),

dict(id="ch21-book-03", source="Book: Interactions summary (Q4-5)", topics="predictions, interaction models", type="matching",
question=PMASS + "\n\n" + PINT + "\n\nUsing the interaction model, match each penguin to its predicted body mass:\n\n1. Female Gentoo\n2. Male Gentoo",
options="""A) 4750 g
B) 5418 g
C) 4680 g
D) 5485 g""",
answer="1-C, 2-D",
explanation="Female Gentoo: 3369 + 1311 = 4680. Male Gentoo: 3369 + 675 + 1311 + 130 = 5485. These equal the observed group means.",
why_wrong="A) and B) come from the additive model. Common mistake: forgetting the sexmale:speciesGentoo term for males.",
hint="For a male Gentoo, add every coefficient whose indicator is 1."),

dict(id="ch21-book-04", source="Book: Interactions summary (Q6)", topics="visualizing interactions", type="MC",
question=PMASS + "\n\nThe plot shows body mass by sex and species; large points are group means. Which aspect suggests an interaction between sex and species?",
image="ch21-book-mass-sex-species.png",
options="""A) That body mass differs by species
B) That body mass differs by sex (the lines connecting female and male means slope upward)
C) That the line connecting male and female means is steeper for Gentoo than for Adelie and Chinstrap (the lines aren't parallel)
D) Such plots don't convey information about interactions""",
answer="C",
explanation="Non-parallel lines mean the sex difference depends on species: an interaction.",
why_wrong="""A) and B) Those are main effects.
D) Interaction plots are exactly for this.""",
hint="What would the lines look like with no interaction?"),

dict(id="ch21-book-05", source="Book: Interactions summary (Q7-8)", topics="Type II sums of squares, interactions", type="MC",
question=PMASS + """

car::Anova(penguin_interaction_model, type = "II")
             Sum Sq  Df F value    Pr(>F)
sex          37090262   1 387.460 < 2.2e-16
species     143401584   2 749.016 < 2.2e-16
sex:species   1676557   2   8.757 0.0001973
Residuals    31302628 327

The small p-value for sex:species means we reject the null that:""",
options="""A) Male and female penguins have the same average body mass
B) All penguin species have the same average body mass
C) Sex and species are independent
D) The sex difference in body mass is identical across species""",
answer="D",
explanation="The interaction tests whether the male-female difference is the same in every species.",
why_wrong="""A) and B) Those are the main-effect nulls.
C) That's about the composition of the sample, not body mass.""",
hint="What does the interaction term model?"),

dict(id="ch21-book-06", source="Book: Interactions summary (Q7)", topics="Type I vs Type II sums of squares", type="MC",
question="Why use car::Anova() rather than base R's anova() to test terms in an interaction model?",
options="""A) Base R's anova() is sequential, so term order can matter
B) Base R can't fit models that include interactions
C) anova() assumes the residuals are normally distributed
D) car::Anova() proves that the interaction is causal""",
answer="A",
explanation="Type II tests each term after adjusting for others of the same order, so results don't depend on the order we typed the terms.",
why_wrong="""B) It can.
C) Both rely on the same assumptions.
D) No test proves causation.""",
hint="What's different about how anova() handles the first term?"),

dict(id="ch21-book-07", source="Book: Interactions summary (Q9)", topics="summary() output, intercept", type="matching",
question=PMASS + "\n\n" + PSUM + "\n\nConsider the (Intercept) p-value.\n\n1. It tests the null hypothesis that...\n2. This test is silly because...",
options="""A) the mean body mass of female Adelie penguins is zero
B) we already know penguins don't have an average body mass of zero grams
C) the mean body mass of all penguins is zero
D) intercepts can't be estimated in models with interactions""",
answer="1-A, 2-B",
explanation="The intercept is the prediction for the reference levels (female, Adelie). Its p-value tests whether that mean is zero, which is obviously false.",
why_wrong="C) The intercept is for the reference group, not all penguins. D) They can.",
hint="Which penguins does the intercept describe?"),

dict(id="ch21-book-08", source="Book: Interactions summary (Q10)", topics="summary() output, main effects", type="select-all",
question=PMASS + "\n\n" + PSUM + "\n\nWhy should we be cautious about interpreting the speciesChinstrap p-value (0.014)? (Select all that apply.)",
options="""A) It's only one reference-level comparison, not a test of the whole species term
B) Main effects require extra care when interactions are in the model (this compares female Chinstraps to female Adelies only)
C) It doesn't account for the multiple species comparisons we might make
D) Chinstrap penguins were randomly assigned to species""",
answer="A, B, C",
explanation="speciesChinstrap compares female Chinstrap to female Adelie (the reference sex), isn't a test of species overall, and isn't corrected for multiple comparisons.",
why_wrong="D) Nonsense: species can't be assigned.",
hint="What exactly does this coefficient compare?"),

dict(id="ch21-book-09", source="Book: Interactions summary (Q11-13)", topics="emmeans, main effects with interactions", type="MC",
question=PMASS + "\n\n" + PEMM + "\n\nemmeans warns that the sex comparison 'may be misleading due to involvement in interactions.' What does the female - male contrast estimate, and is it reasonable to say males are heavier?",
options="""A) The sex difference in Adelies only; no, because interactions make main effects meaningless
B) The sex difference averaged over species; yes, but we should add that the size of the difference varies among species
C) The sex:species interaction; yes, and the difference is identical in every species
D) The sex difference averaged over species; no, because female Gentoos outweigh male Chinstraps""",
answer="B",
explanation="emmeans averages the sex difference over species, hence the warning. Males are heavier in every species, so 'males are heavier' is fair, as long as we note that the gap varies.",
why_wrong="""A) It's averaged over species, and main effects aren't meaningless when consistent.
C) The interaction says the difference is NOT identical.
D) Comparing across species doesn't address the sex difference within species.""",
hint="Is the male-female difference in the same direction in every species?"),

dict(id="ch21-book-10", source="Book: Interactions summary (Q14)", topics="emmeans vs summary(), contrasts", type="select-all",
question=PMASS + "\n\n" + PSUM + "\n\n" + PEMM + "\n\nWhy is the Adelie - Chinstrap contrast from emmeans not significant (p = 0.82), while speciesChinstrap in summary() is (p = 0.014)? (Select the two correct answers.)",
options="""A) The emmeans contrast compares Adelie and Chinstrap averaged over sex, while speciesChinstrap compares female Chinstraps to female Adelies
B) The emmeans contrast tests sex, while speciesChinstrap tests body mass
C) The emmeans p-value is adjusted with Tukey's method, while the speciesChinstrap p-value is not
D) They are the same test, so one of them must be wrong""",
answer="A, C",
explanation="They answer different questions: females only vs averaged over sexes (and male Chinstraps are relatively light, so the average difference nearly vanishes). The emmeans p-value is also corrected for multiple comparisons.",
why_wrong="""B) Both are about species differences in body mass.
D) They're different tests.""",
hint="Which penguins does each comparison use?"),

dict(id="ch21-book-11", source="Book: Interactions summary (Q15)", topics="linear models", type="MC",
question="Which of the following are linear models?\n\n1. Modeling blood glucose in lizards kept at warm vs cool temperatures\n2. Modeling algal growth as a function of nutrient concentration, allowing for a hump or trough (a polynomial)\n3. Modeling tadpole growth as a function of pond, adjusting for initial body size\n4. Modeling the different effect of fertilizer on plant height in wet and dry soil\n5. Modeling log-transformed metabolic rate as a function of log-transformed body mass",
options="""A) Only 1, 3 and 4
B) Only 1, 3, 4 and 5
C) All of them (1-5)
D) Only model 1""",
answer="C",
explanation="All are linear models: predictions are sums of coefficients times predictors. That includes categorical predictors (1), polynomials (2: x and x² are both just predictors), covariates (3), interactions (4) and transformed variables (5).",
why_wrong="Common mistake: thinking curved relationships (2) can't be linear models. 'Linear' refers to the coefficients, not the shape.",
hint="'Linear' means we add up coefficient × predictor terms."),
]
