from ai_helpers import V, r
import importlib.util, os
spec = importlib.util.spec_from_file_location('o21', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rows_ch21.py')); o = importlib.util.module_from_spec(spec); spec.loader.exec_module(o)
OLY, OADD, OINT, OSUM, GC, GC_ANOVA, PMASS, PADD, PINT, PSUM, PEMM = o.OLY, o.OADD, o.OINT, o.OSUM, o.GC, o.GC_ANOVA, o.PMASS, o.PADD, o.PINT, o.PSUM, o.PEMM
GCX = "To ask how petal area and anther-stigma distance (ASD) together predict hybridization in Clarkia RILs at GC, we fit:\n\nlm(prop_hybrid ~ petal_area_mm * asd_mm)\n(Intercept) = 0.300950; petal_area_mm = -0.004660; asd_mm = -0.448186; petal_area_mm:asd_mm = 0.009506"
FLIP = "Palmer penguins: we modeled body mass (g) as a function of flipper length (mm), species, and their interaction:\n\nlm(body_mass ~ flipper_len * species)\n(Intercept) = -2536.0; flipper_len = 32.80; speciesChinstrap = -501.0; speciesGentoo = -4251.0;\nflipper_len:speciesChinstrap = 1.74; flipper_len:speciesGentoo = 21.80"
PANOVA = 'car::Anova(penguin_interaction_model, type = "II")\n             Sum Sq  Df F value    Pr(>F)\nsex          37090262   1 387.460 < 2.2e-16\nspecies     143401584   2 749.016 < 2.2e-16\nsex:species   1676557   2   8.757 0.0001973\nResiduals    31302628 327'
add = lambda yr, male: 36.0528 - 0.01261*yr - 1.0928*male
itx = lambda yr, male: 44.3470 - 0.016822*yr - 12.5206*male + 0.005817*yr*male
gcx = lambda pa, asd: 0.300950 - 0.004660*pa - 0.448186*asd + 0.009506*pa*asd
ROWS = [
V("ch21-quiz-01", 1, image="ch21-quiz-olympics.png", question=OLY + "\n\nIn the plot, roughly how big is the gap between men's and women's winning times in recent Olympics?",
options="""A) About 1 second
B) About 0.1 seconds
C) About 3 seconds
D) There is no gap""", answer="A",
explanation="Recent women's times are around 10.8 to 10.9 s and men's around 9.85 s: about 1 s apart.",
why_wrong="""B) Too small.
C) Too large.
D) Men are clearly faster.""", hint="Compare the most recent points."),
V("ch21-quiz-01", 2, image="ch21-quiz-olympics.png", question=OLY + "\n\nIf straight lines were drawn through each group's points, would they be parallel?",
options="""A) Probably not: women's times seem to fall more steeply
B) Yes: both groups fall at exactly the same rate
C) Probably not: men's times seem to fall more steeply
D) Yes: neither group's times change over time""", answer="A",
explanation="The women's points drop from about 12.2 to 10.9 s since 1928; the men's drop less over the same period. Non-parallel lines suggest an interaction.",
why_wrong="""B) The slopes look different.
C) The women's fall is steeper.
D) Both fall.""", hint="Compare how steeply each set of points falls."),

V("ch21-quiz-02", 1, question=OLY + "\n\nA model with NO interaction:\n\n" + OADD + "\n\n(Gendermale is 1 for men and 0 for women.) What winning time does this model predict for the MEN'S 100 m in 1960? Round to two decimal places.",
answer=r(add(1960,1),2), explanation="36.0528 - 0.01261 × 1960 - 1.0928 = " + r(add(1960,1),2) + " s.", hint="Plug in Year = 1960 and Gendermale = 1."),
V("ch21-quiz-02", 2, question=OLY + "\n\nA model with NO interaction:\n\n" + OADD + "\n\nAccording to this model, how much faster (in seconds) are men than women in ANY given year?",
answer="1.0928", explanation="Without an interaction, the gap is the same every year: the Gendermale coefficient, 1.09 s.", hint="Additive model: parallel lines."),

V("ch21-quiz-03", 1, question=OLY + "\n\nA model with NO interaction:\n\n" + OADD + "\n\n(Gendermale is 1 for men and 0 for women.) What winning time does this model predict for the WOMEN'S 100 m in 1980? Round to two decimal places.",
answer=r(add(1980,0),2), explanation="36.0528 - 0.01261 × 1980 = " + r(add(1980,0),2) + " s.", hint="Gendermale = 0."),
V("ch21-quiz-03", 2, question=OLY + "\n\nA model with NO interaction:\n\n" + OADD + "\n\nBy how many seconds does this model predict winning times fall over 40 years (for either gender)? Round to two decimal places.",
answer=r(0.01261*40,2), explanation="0.01261 × 40 = 0.50 s. Without an interaction, both genders share this slope.", hint="Slope × 40."),

V("ch21-quiz-04", 1, question=OLY + "\n\nA model WITH an interaction:\n\n" + OINT + "\n\n(Gendermale is 1 for men and 0 for women.) What winning time does this model predict for the MEN'S 100 m in 1980? Round to two decimal places.",
answer=r(itx(1980,1),2), explanation="44.3470 - 0.016822 × 1980 - 12.5206 + 0.005817 × 1980 = " + r(itx(1980,1),2) + " s.", hint="Include every term when Gendermale = 1."),
V("ch21-quiz-04", 2, question=OLY + "\n\nA model WITH an interaction:\n\n" + OINT + "\n\nWhat is the slope for MEN (change in winning time per year)? Report it to four decimal places.",
answer=r(-0.016822+0.005817,4), explanation="Men's slope = Year + Year:Gendermale = -0.016822 + 0.005817 = -0.0110 s per year.", hint="Add the interaction to the reference slope."),

V("ch21-quiz-05", 1, question=OLY + "\n\nA model WITH an interaction:\n\n" + OINT + "\n\n(Gendermale is 1 for men and 0 for women.) What winning time does this model predict for the WOMEN'S 100 m in 1960? Round to two decimal places.",
answer=r(itx(1960,0),2), explanation="44.3470 - 0.016822 × 1960 = " + r(itx(1960,0),2) + " s.", hint="Gendermale = 0, so the gender terms drop out."),
V("ch21-quiz-05", 2, question=OLY + "\n\nA model WITH an interaction:\n\n" + OINT + "\n\nWhat is the slope for WOMEN (change in winning time per year)? Report it to four decimal places.",
answer="-0.0168", explanation="Women are the reference level, so their slope is just the Year coefficient: -0.0168 s per year.", hint="Which group is the reference?"),

V("ch21-quiz-06", 1, question=OLY + "\n\n" + OSUM + "\n\nWomen are the reference level. What does the Year:Gendermale coefficient (0.0058) measure?",
options="""A) How much less steeply men's times fall per year than women's
B) How much faster men are than women, averaged over every year
C) The change in women's winning times per year of the Olympics
D) The probability that men and women improve at the same rate""", answer="A",
explanation="It's the difference in slopes (men minus women). Positive means men's negative slope is less steep.",
why_wrong="""B) That's not an interaction.
C) That's the Year coefficient.
D) Coefficients aren't probabilities.""", hint="Difference in slopes."),
V("ch21-quiz-06", 2, question=OLY + "\n\n" + OSUM + "\n\nWhat null hypothesis does the Year:Gendermale p-value (0.008) test?",
options="""A) Men's and women's times change at the same rate
B) Men's and women's times are the same on average
C) Winning times are not changing over the years
D) Women's times are not changing over the years""", answer="A",
explanation="The interaction tests whether the slopes differ.",
why_wrong="""B) That's about the gap, not slopes.
C) and D) Those are about slopes themselves, not their difference.""", hint="Interaction = difference in slopes."),

V("ch21-quiz-07", 1, question=OLY + "\n\nTRUE or FALSE: Using the interaction model to predict the women's winning time in 1970 is an extrapolation.",
options="""A) TRUE
B) FALSE""", answer="B",
explanation="1970 is within the years of women's data (1928 to 2004), so it's interpolation.", why_wrong="TRUE: 1970 is inside the data range.", hint="Is 1970 within 1928 to 2004?"),
V("ch21-quiz-07", 2, question=OLY + "\n\nTRUE or FALSE: Using the interaction model to predict the women's winning time in 1904 is an extrapolation.",
options="""A) TRUE
B) FALSE""", answer="A",
explanation="Women's results start in 1928, so 1904 is outside their data.", why_wrong="FALSE: there are no women's data before 1928.", hint="When do women's results start?"),

V("ch21-quiz-08", 1, question=OLY + "\n\n" + OINT + "\n\nWomen are the reference level. What does the Year coefficient (-0.0168) represent?",
options="""A) The change in women's winning times per year
B) The change in men's winning times per year
C) The average change in winning times per year
D) The difference in slopes between men and women""", answer="A",
explanation="In an interaction model, Year is the slope for the reference group (women).",
why_wrong="""B) Men's slope adds the interaction.
C) Not an average.
D) That's the interaction.""", hint="Reference group's slope."),
V("ch21-quiz-08", 2, question=OLY + "\n\n" + OINT + "\n\nWhy is the Intercept (44.35 s) not a sensible winning time?",
options="""A) It's the women's prediction for year 0, far outside the data
B) It's the average winning time for men across all of the years
C) It's the predicted winning time for the first modern Olympics
D) It is sensible: early sprinters took about 44 s for 100 m""", answer="A",
explanation="The intercept is the prediction at Year = 0 for the reference group: a huge extrapolation.",
why_wrong="""B) Not an average.
C) The first Olympics was 1896, not year 0.
D) Nobody took 44 s.""", hint="What year does the intercept refer to?"),

V("ch21-quiz-09", 1, question=OLY + "\n\n" + OINT + "\n\nWe refit the interaction model using years_since_1928 = Year - 1928. Which of these stay the SAME? (Select all that apply.)",
options="""A) The slope for women
B) The interaction coefficient
C) The predicted times for 1960
D) The intercept""", answer="A, B, C",
explanation="Centering moves 'zero', changing the intercept and the gender coefficient, but not slopes or predictions.",
why_wrong="D) The intercept now describes women in 1928.", hint="What does shifting x change?"),
V("ch21-quiz-09", 2, question=OLY + "\n\n" + OINT + "\n\nAfter refitting with years_since_1928 = Year - 1928, the Gendermale coefficient is about -1.31. What does it now represent?",
options="""A) The predicted men-women gap in 1928
B) The predicted men-women gap in year 0
C) The average men-women gap over all years
D) The difference in slopes between men and women""", answer="A",
explanation="Gendermale is the gap where years_since_1928 = 0, i.e. in 1928.",
why_wrong="""B) That was before centering.
C) Not an average.
D) That's the interaction.""", hint="Where is the new zero?"),

V("ch21-hw-01", 1, question="A researcher includes an interaction between temperature and every one of 8 other variables, 'just in case'. What's the main problem?",
options="""A) Many interactions cost power and invite overfitting
B) R can't fit models with more than one interaction
C) Interactions can only involve categorical variables
D) There's no problem; more interactions are always better""", answer="A",
explanation="Include interactions that make biological sense; each one spends data.",
why_wrong="""B) R can.
C) Numeric variables can interact.
D) Not true.""", hint="Each term costs data."),
V("ch21-hw-01", 2, question="Which is the best reason to include an interaction between fertilizer and soil moisture in a model of plant growth?",
options="""A) There's reason to expect fertilizer to work differently in wet vs dry soil
B) Both variables are significant on their own in an additive model
C) The dataset has more than 100 plants in it
D) Soil moisture is a numeric variable rather than a category""", answer="A",
explanation="Interactions should be motivated by the biology: does the effect of one depend on the other?",
why_wrong="""B) Main effects don't imply interactions.
C) Sample size alone isn't a reason.
D) Variable type isn't a reason.""", hint="Start from the biology."),

V("ch21-hw-02", 1, question="In a study of fertilizer and two plant varieties, there's a significant interaction: fertilizer increases height in variety A but decreases it in variety B. Is it reasonable to report the main effect of fertilizer?",
options="""A) No: the effect reverses, so an average is misleading
B) Yes: main effects are always meaningful
C) Yes: if its p-value is below α
D) No: interactions make all main effects zero""", answer="A",
explanation="When the direction flips, an average effect describes neither variety.",
why_wrong="""B) and C) Not when effects reverse.
D) Main effects aren't zero; they're just hard to interpret.""", hint="Does the direction change?"),
V("ch21-hw-02", 2, question="Males are heavier than females in all three penguin species, but by different amounts (a significant interaction). Which summary is best?",
options="""A) Males are heavier in every species, but the gap varies by species
B) Sex doesn't matter, since there is a significant interaction
C) Males are heavier by exactly the same amount in every species
D) Nothing can be said about sex because of the interaction""", answer="A",
explanation="When direction is consistent, a main effect is meaningful; add that its size varies.",
why_wrong="""B) and D) Too strong.
C) The interaction says the gap varies.""", hint="Is the direction consistent?"),

V("ch21-hw-03", 1, image="ch21-hw-four-models.png", question=GC + "\n\nEach panel shows the same data with lines from a different model. Which panel's model has the most parameters?",
options="""A) Panel B: petal area × petal color
B) Panel A: petal area only
C) Panel C: petal area + petal color
D) Panel D: petal color only""", answer="A",
explanation="The interaction model estimates an intercept, an area slope, a color difference and a slope difference: 4 parameters.",
why_wrong="""B) and D) 2 parameters.
C) 3 parameters.""", hint="Count intercepts and slopes."),
V("ch21-hw-03", 2, image="ch21-hw-four-models.png", question=GC + "\n\nEach panel shows the same data with lines from a different model. In which panel are the lines flat?",
options="""A) Panel D: petal color only
B) Panel A: petal area only
C) Panel B: area × color
D) Panel C: area + color""", answer="A",
explanation="Without petal area in the model, predictions don't change with area: flat lines at each color's mean.",
why_wrong="B), C) and D) include petal area, so their lines slope.", hint="Which model ignores petal area?"),

V("ch21-hw-04", 1, image="ch21-hw-diag.png", question=GC + "\n\nDiagnostic plots for lm(prop_hybrid ~ petal_area_mm * petal_color) are shown. Which plot is best for judging normality of the residuals?",
options="""A) The QQ plot
B) Residuals vs leverage
C) Scale-location
D) None of them""", answer="A",
explanation="QQ plots compare residuals to a normal distribution.",
why_wrong="""B) For influence.
C) For equal variance.
D) The QQ plot is designed for this.""", hint="Quantiles."),
V("ch21-hw-04", 2, image="ch21-hw-diag.png", question=GC + "\n\nDiagnostic plots for lm(prop_hybrid ~ petal_area_mm * petal_color) are shown. Match each problem to its likely cause:\n\n1. Skewed residuals\n2. Spread of residuals growing with fitted values",
options="""A) Many RILs set no hybrid seed, with a long right tail
B) Proportions near zero can't vary much, but larger ones can
C) The RILs were not independent of one another
D) Petal area was measured in the wrong units""", answer="1-A, 2-B",
explanation="Pile-ups at zero skew the residuals; bounded proportions have smaller variance near zero.", why_wrong="C) and D) don't explain these patterns.", hint="Think about proportions near 0."),

V("ch21-hw-05", 1, question=GC + "\n\n" + GC_ANOVA + "\n\nWhy is the interaction's test the same with Type II and Type III?",
options="""A) It's the highest-order term, adjusted for all others in both types
B) Interactions are never affected by any type of sums of squares
C) Petal color and petal area are uncorrelated in these RILs
D) Type II and Type III are always the same for every term""", answer="A",
explanation="Both Type II and Type III test the highest-order term after all other terms.",
why_wrong="""B) Too general.
C) Not the reason.
D) The main effects differ here.""", hint="What is the interaction adjusted for?"),
V("ch21-hw-05", 2, question=GC + "\n\n" + GC_ANOVA + "\n\nWhy is petal color not significant with Type III (p = 0.17)?",
options="""A) Type III tests color at a petal area of 0, far outside the data
B) Petal color has no association with hybrid seed in these data
C) Type III always gives larger p-values than Type II does
D) The interaction removes all of petal color's effect""", answer="A",
explanation="With an interaction (and default contrasts), Type III tests each main effect where the other variable is 0.",
why_wrong="""B) Type II finds a strong color effect.
C) Not always.
D) Color still matters at real petal areas.""", hint="Where is the color effect evaluated?"),

V("ch21-hw-06", 1, question=GC + " The interaction between petal color and petal area is significant. What would a plot of the model look like?",
options="""A) Lines for pink and white with different slopes
B) Parallel lines for pink and white flowers
C) One single line for both colors of flower
D) Flat lines at each color's mean hybrid seed""", answer="A",
explanation="An interaction means different slopes for each color.",
why_wrong="""B) That's additive.
C) That's area only.
D) That's color only.""", hint="Interaction = non-parallel."),
V("ch21-hw-06", 2, question=GC + " The interaction between petal color and petal area is significant (p = 0.0049). Which statement is NOT supported by this result?",
options="""A) Petal color and petal area are strongly correlated with each other
B) The petal area slope differs between pink and white flowers
C) The effect of color depends on petal area
D) The model's lines for the two colors aren't parallel""", answer="A",
explanation="An interaction is about effects depending on each other, not about predictors being correlated.",
why_wrong="B), C) and D) are all what an interaction means.", hint="Interaction ≠ correlation."),

V("ch21-hw-07", 1, question=GCX + "\n\nPredict the proportion of hybrid seed for a RIL with an ASD of 1 mm and a petal area of 80 mm².",
answer=r(gcx(80,1),2), explanation="0.30095 - 0.00466 × 80 - 0.448186 × 1 + 0.009506 × 80 × 1 = " + r(gcx(80,1),3) + ".", hint="Include the product term."),
V("ch21-hw-07", 2, question=GCX + "\n\nWhat is the slope for petal area (change in proportion hybrid per mm²) for a RIL with an ASD of 2 mm? Report it to four decimals.",
answer=r(-0.004660+0.009506*2,4), explanation="Slope = -0.00466 + 0.009506 × 2 = 0.0144 per mm².", hint="petal_area_mm + interaction × ASD."),

V("ch21-chimein-01", 1, image="ch21-chimein-bill-sex-species.png", question="Palmer penguins: bill length of three Antarctic penguin species by sex. If you connected each species' female and male means with a line, what would you expect?",
options="""A) Roughly parallel lines, sloping up from female to male
B) Lines that cross, with the sex effect reversing
C) Flat lines, since sex has no effect on bill length
D) Lines with strongly different slopes for each species""", answer="A",
explanation="Males are longer-billed in every species by similar amounts: roughly parallel lines (no significant interaction).",
why_wrong="""B) The sex effect doesn't reverse.
C) There's a clear sex effect.
D) The gaps are similar.""", hint="Is the male-female gap similar across species?"),
V("ch21-chimein-01", 2, image="ch21-chimein-bill-sex-species.png", question="Palmer penguins: bill length of three Antarctic penguin species by sex. Which model best matches this plot? (Select all that apply.)",
options="""A) lm(bill_len ~ sex + species)
B) lm(bill_len ~ sex)
C) lm(bill_len ~ species)""", answer="A",
explanation="Both sex and species matter, and their effects look roughly additive.",
why_wrong="""B) Ignores big species differences.
C) Ignores the consistent sex difference.""", hint="Which effects are visible?"),

V("ch21-chimein-02", 1, image="ch21-chimein-iris-petal.png", question="Iris petal length vs petal width for three iris species, with a separate regression line for each species. Which feature of the plot shows the interaction? (Select all that apply.)",
options="""A) The lines have different slopes
B) The species are at different heights
C) Petal length rises with petal width""", answer="A",
explanation="An interaction is about slopes differing among groups.",
why_wrong="""B) That's a species main effect.
C) That's a petal width main effect.""", hint="Interaction = non-parallel."),
V("ch21-chimein-02", 2, image="ch21-chimein-iris-petal.png", question="Iris petal length vs petal width for three iris species, with a separate regression line for each species. Why should we be careful comparing the slopes? (Select all that apply.)",
options="""A) The species barely overlap in petal width
B) Each slope covers a different range of widths
C) The slopes are all exactly equal""", answer="A, B",
explanation="Each species' line covers a different range, so differences in slope partly reflect different parts of the width axis.",
why_wrong="C) They differ.", hint="Look at where each species falls on the x-axis."),

V("ch21-chimein-03", 1, image="ch21-chimein-iris-sepal.png", question="Iris sepal length vs sepal width for three iris species, with a separate regression line for each species. Which model best matches this plot? (Select all that apply.)",
options="""A) lm(Sepal.Length ~ Sepal.Width + Species)
B) lm(Sepal.Length ~ Sepal.Width * Species)
C) lm(Sepal.Length ~ Species)""", answer="A",
explanation="Roughly parallel lines at different heights: an additive model (the interaction isn't significant, p = 0.67).",
why_wrong="""B) Not needed: lines are parallel.
C) Ignores the clear width effect.""", hint="Parallel lines at different heights."),
V("ch21-chimein-03", 2, image="ch21-chimein-iris-sepal.png", question="Iris sepal length vs sepal width for three iris species, with a separate regression line for each species. What would you expect for the interaction's p-value?",
options="""A) Large (not significant)
B) Very small (p < 0.001)
C) Exactly 0.05
D) Impossible to guess""", answer="A",
explanation="Roughly parallel lines suggest no interaction (p = 0.67).",
why_wrong="""B) That would need clearly different slopes.
C) No reason.
D) The plot gives a strong hint.""", hint="Are the lines parallel?"),

V("ch21-chimein-04", 1, question=FLIP + "\n\nMatch each penguin (flipper length 210 mm) to its predicted body mass:\n\n1. Adelie\n2. Chinstrap\n3. Gentoo",
options="""A) """ + r(-2536+32.8*210,0) + """ g
B) """ + r(-2536-501+(32.8+1.74)*210,0) + """ g
C) """ + r(-2536-4251+(32.8+21.8)*210,0) + """ g
D) 6888 g""", answer="1-A, 2-B, 3-C",
explanation="Adelie: -2536 + 32.8 × 210. Chinstrap: -3037 + 34.54 × 210. Gentoo: -6787 + 54.6 × 210.",
why_wrong="D) is 32.8 × 210 without the intercept.", hint="Each species has its own intercept and slope."),
V("ch21-chimein-04", 2, question=FLIP + "\n\nMatch each species to its slope (g per mm of flipper length):\n\n1. Adelie\n2. Chinstrap\n3. Gentoo",
options="""A) 32.80
B) 34.54
C) 54.60
D) 21.80""", answer="1-A, 2-B, 3-C",
explanation="Adelie: 32.80. Chinstrap: 32.80 + 1.74. Gentoo: 32.80 + 21.80.",
why_wrong="D) is the Gentoo interaction term alone.", hint="Reference slope + interaction."),

V("ch21-chimein-05", 1, question=FLIP + "\n\nWhy is the Gentoo slope (54.6 g/mm) so different from Adelie's (32.8 g/mm)?",
options="""A) The flipper_len:speciesGentoo interaction adds 21.8 g/mm
B) speciesGentoo shifts the line down by 4251 g
C) Gentoos have more data, so their slope is larger
D) It isn't; they share one slope in this model""", answer="A",
explanation="With an interaction, each species' slope is the reference slope plus its interaction term.",
why_wrong="""B) That changes the intercept, not the slope.
C) Sample size doesn't set the slope.
D) The interaction gives separate slopes.""", hint="Which term changes slopes?"),
V("ch21-chimein-05", 2, question=FLIP + "\n\nWhat does speciesChinstrap = -501 represent?",
options="""A) The Chinstrap - Adelie difference at a flipper length of 0 mm
B) The average mass difference between Chinstraps and Adelies
C) How much lighter Chinstraps are at every flipper length
D) The difference in slopes between Chinstraps and Adelies""", answer="A",
explanation="With an interaction, a main effect is the difference where the other variable equals zero.",
why_wrong="""B) and C) The difference varies with flipper length.
D) That's the interaction (1.74).""", hint="Main effect in an interaction model."),

V("ch21-book-01", 1, question=PMASS + "\n\nWhich model forces the male-female difference to be the same in every species?",
options="""A) penguin_additive_model
B) penguin_interaction_model
C) Both of these models
D) Neither of these models""", answer="A",
explanation="Without an interaction, sexmale is one shared difference for all species.",
why_wrong="""B) Allows different differences.
C) and D) Only the additive model does.""", hint="Which has no sex:species term?"),
V("ch21-book-01", 2, question=PMASS + "\n\nWhat would it look like if there were NO sex:species interaction?",
options="""A) The male-female gap is the same in every species
B) Males and females have the same body mass
C) All of the species have the same body mass
D) Body mass doesn't vary within each species""", answer="A",
explanation="No interaction means the effect of sex doesn't depend on species.",
why_wrong="""B) That's no sex effect.
C) That's no species effect.
D) Unrelated.""", hint="Effect of one doesn't depend on the other."),

V("ch21-book-02", 1, question=PMASS + "\n\n" + PADD + "\n\nUsing the additive model, match each penguin to its predicted body mass:\n\n1. Female Chinstrap\n2. Male Chinstrap",
options="""A) 3399 g
B) 4067 g
C) 3527 g
D) 3939 g""", answer="1-A, 2-B",
explanation="Female Chinstrap: 3372 + 27 = 3399. Male Chinstrap: 3399 + 668 = 4067.", why_wrong="C) and D) come from the interaction model.", hint="Add the coefficients that apply."),
V("ch21-book-02", 2, question=PMASS + "\n\n" + PADD + "\n\nUsing the additive model, match each penguin to its predicted body mass:\n\n1. Female Adelie\n2. Male Adelie",
options="""A) 3372 g
B) 4040 g
C) 3369 g
D) 4044 g""", answer="1-A, 2-B",
explanation="Female Adelie is the reference: 3372. Male Adelie: 3372 + 668 = 4040.", why_wrong="C) and D) come from the interaction model.", hint="Adelie and female are the reference levels."),

V("ch21-book-03", 1, question=PMASS + "\n\n" + PINT + "\n\nUsing the interaction model, match each penguin to its predicted body mass:\n\n1. Female Chinstrap\n2. Male Chinstrap",
options="""A) 3399 g
B) 4067 g
C) 3527 g
D) 3939 g""", answer="1-C, 2-D",
explanation="Female Chinstrap: 3369 + 158 = 3527. Male Chinstrap: 3369 + 675 + 158 - 263 = 3939.", why_wrong="A) and B) come from the additive model.", hint="Include the interaction for males."),
V("ch21-book-03", 2, question=PMASS + "\n\n" + PINT + "\n\nAccording to the interaction model, how much heavier are male Chinstraps than female Chinstraps?",
options="""A) 412 g
B) 675 g
C) 938 g
D) 263 g""", answer="A",
explanation="675 - 263 = 412 g: the Adelie sex difference plus the Chinstrap interaction.",
why_wrong="""B) That's the Adelie sex difference.
C) Adds instead of subtracting.
D) That's the interaction alone.""", hint="sexmale + sexmale:speciesChinstrap."),

V("ch21-book-04", 1, image="ch21-book-mass-sex-species.png", question=PMASS + "\n\nThe plot shows body mass by sex and species; large points are group means. Which aspect shows a main effect of sex?",
options="""A) Males are heavier than females in every species
B) The lines for each species aren't parallel
C) Gentoos are heavier than the other species
D) Body mass varies a lot within each group""", answer="A",
explanation="A consistent male-female difference is the sex main effect.",
why_wrong="""B) That's an interaction.
C) That's a species effect.
D) That's within-group variation.""", hint="Female vs male."),
V("ch21-book-04", 2, image="ch21-book-mass-sex-species.png", question=PMASS + "\n\nThe plot shows body mass by sex and species; large points are group means. In which species is the male-female difference largest?",
options="""A) Gentoo
B) Adelie
C) Chinstrap
D) It is the same in all three species""", answer="A",
explanation="The Gentoo line is steepest (about 805 g vs 675 g for Adelie and 412 g for Chinstrap).",
why_wrong="""B) and C) Smaller gaps.
D) The interaction says they differ.""", hint="Which line is steepest?"),

V("ch21-book-05", 1, question=PMASS + "\n\n" + PANOVA + "\n\nWhat do we conclude about the sex:species interaction at α = 0.05?",
options="""A) Reject the null: the sex difference varies by species
B) Fail to reject: the sex difference is the same in each
C) Reject the null: males are heavier in every species
D) Fail to reject: species don't differ in their mass""", answer="A",
explanation="p = 0.0002 < 0.05, so the male-female difference differs among species.",
why_wrong="""B) p < α.
C) That's not what the interaction tests.
D) Wrong term.""", hint="What does the interaction test?"),
V("ch21-book-05", 2, question=PMASS + "\n\n" + PANOVA + "\n\nWhy does the sex:species term have 2 degrees of freedom?",
options="""A) (2 - 1) sexes × (3 - 1) species = 2
B) There are 2 sexes in the dataset
C) Interactions always have exactly 2 df
D) It is 327 - 325, from the residuals""", answer="A",
explanation="Interaction df = (levels of sex - 1) × (levels of species - 1) = 1 × 2.",
why_wrong="""B) Coincidence here.
C) Depends on the levels.
D) Not how df work.""", hint="Multiply the main effects' df."),

V("ch21-book-06", 1, question="Two students fit lm(y ~ a + b + a:b) and lm(y ~ b + a + a:b) and run base R's anova() on each. Why might their tables disagree for a and b?",
options="""A) anova() is sequential, so the first term isn't adjusted for later ones
B) The two models make different predictions for each observation
C) Base R picks a random reference level for each model it fits
D) They can't disagree; the models are identical""", answer="A",
explanation="Type I SS depend on order when predictors are correlated. car::Anova() avoids this.",
why_wrong="""B) Same model, same predictions.
C) Not random.
D) The tables can differ even though the model is the same.""", hint="Sequential sums of squares."),
V("ch21-book-06", 2, question="In car::Anova(model, type = 'II') for lm(y ~ a + b + a:b), what is the main effect of a adjusted for?",
options="""A) b (but not the a:b interaction)
B) Nothing; it's tested first
C) The a:b interaction only
D) Both b and the interaction""", answer="A",
explanation="Type II adjusts each main effect for the other main effects, not for interactions containing it.",
why_wrong="""B) That's Type I for the first term.
C) and D) That's closer to Type III.""", hint="Same-order terms."),

V("ch21-book-07", 1, question=PMASS + "\n\n" + PSUM + "\n\nWhat does the sexmale coefficient (674.66) describe in this interaction model?",
options="""A) The male - female difference in Adelies only
B) The male - female difference averaged over species
C) The male - female difference in every one of the species
D) The difference in average mass between Adelie and Gentoo""", answer="A",
explanation="With an interaction, sexmale is the sex difference at the reference species (Adelie).",
why_wrong="""B) That's from emmeans.
C) The interaction says it varies.
D) That's a species coefficient.""", hint="Reference species."),
V("ch21-book-07", 2, question=PMASS + "\n\n" + PSUM + "\n\nMatch each coefficient to the group comparison it describes:\n\n1. speciesGentoo\n2. sexmale:speciesGentoo",
options="""A) Female Gentoo minus female Adelie
B) How much larger the sex gap is in Gentoos than Adelies
C) Male Gentoo minus male Adelie
D) Gentoo minus Adelie, averaged over sexes""", answer="1-A, 2-B",
explanation="Main effects are at the reference sex (female); the interaction is the extra sex difference in Gentoos.", why_wrong="Reference levels matter.", hint="Female is the reference sex."),

V("ch21-book-08", 1, question=PMASS + "\n\n" + PSUM + "\n\nWhat does the sexmale:speciesGentoo p-value (0.089) test? (Select all that apply.)",
options="""A) Whether the sex difference differs between Gentoo and Adelie
B) Whether Gentoo males are heavier than Gentoo females
C) Whether Gentoos are heavier than Adelies overall""", answer="A",
explanation="It tests whether the Gentoo sex gap differs from the Adelie sex gap.",
why_wrong="""B) That's a different comparison.
C) That's a species comparison.""", hint="Interaction = difference of differences."),
V("ch21-book-08", 2, question=PMASS + "\n\n" + PSUM + "\n\nWhich is the best way to test whether species matters overall in this model? (Select all that apply.)",
options="""A) The Type II F test for species from car::Anova()
B) The p-value for speciesChinstrap in summary()
C) The p-value for the (Intercept) in summary()""", answer="A",
explanation="The F test asks about the species term as a whole.",
why_wrong="""B) One reference comparison, for females only.
C) Tests whether female Adelie mass is zero.""", hint="One test for the whole term."),

V("ch21-book-09", 1, question=PMASS + "\n\n" + PEMM + "\n\nWhy does emmeans warn that the sex contrast 'may be misleading'?",
options="""A) It averages a sex gap that differs among species
B) The emmeans sex contrast contains a calculation error
C) Males and females have identical average body mass
D) The species comparison is not statistically significant""", answer="A",
explanation="With an interaction, a single average sex difference hides variation among species.",
why_wrong="""B) No error.
C) They differ by 631 g on average.
D) Irrelevant.""", hint="Averaged over what?"),
V("ch21-book-09", 2, question=PMASS + "\n\n" + PEMM + "\n\nWhich statement about the female - male contrast (-631 g) is correct?",
options="""A) It averages the sex difference across the three species
B) It is the sex difference in Adelie penguins only
C) It is the sex difference in Gentoo penguins only
D) It is the size of the interaction between sex and species""", answer="A",
explanation="'Results are averaged over the levels of: species.'",
why_wrong="""B) That's sexmale from summary().
C) Gentoo's gap is larger.
D) Not an interaction.""", hint="Read the note under the contrast."),

V("ch21-book-10", 1, question=PMASS + "\n\n" + PSUM + "\n\n" + PEMM + "\n\nThe emmeans Adelie - Gentoo contrast is -1376 g, but speciesGentoo in summary() is 1311 g. Why do they differ in size? (Select all that apply.)",
options="""A) emmeans averages over both sexes
B) speciesGentoo compares females only
C) The Gentoo sex gap is larger than Adelie's""", answer="A, B, C",
explanation="speciesGentoo is the female-only difference (1311). Averaging over sexes adds half the extra male difference (130 / 2 ≈ 65), giving 1376.",
why_wrong="All three statements together explain the gap.", hint="Which sexes does each compare?"),
V("ch21-book-10", 2, question=PMASS + "\n\n" + PSUM + "\n\n" + PEMM + "\n\nWhich test asks whether Adelie and Chinstrap penguins differ in mass, averaged over sexes? (Select all that apply.)",
options="""A) The emmeans Adelie - Chinstrap contrast
B) The speciesChinstrap p-value in summary()
C) The sexmale:speciesChinstrap p-value""", answer="A",
explanation="emmeans averages over sex; speciesChinstrap is females only; the interaction compares sex gaps.",
why_wrong="""B) Females only.
C) A difference in sex gaps.""", hint="Averaged over sexes."),

V("ch21-book-11", 1, question="Which of the following are linear models?\n\n1. lm(height ~ fertilizer * soil_moisture)\n2. lm(growth ~ temperature + I(temperature^2))\n3. lm(log(mass) ~ log(length))\n4. lm(yield ~ variety)",
options="""A) All four of them
B) Only models 1 and 4
C) Only models 3 and 4
D) Only model 4""", answer="A",
explanation="Each prediction is a sum of coefficients times predictors, including interactions, polynomial terms and transformed variables.",
why_wrong="B), C) and D) leave out models that are still linear in their coefficients.", hint="Linear in the coefficients."),
V("ch21-book-11", 2, question="Why is lm(growth ~ temperature + I(temperature^2)) still a linear model, even though it fits a curve?",
options="""A) The prediction is still a sum of coefficients times predictors
B) The curve is approximately straight over the range of data
C) Polynomial terms are dropped automatically by R
D) It isn't a linear model; it's a nonlinear model""", answer="A",
explanation="Linear refers to the coefficients: temperature² is just another predictor.",
why_wrong="""B) It can be very curved.
C) They aren't dropped.
D) It is linear in its coefficients.""", hint="Linear in what?"),
]
