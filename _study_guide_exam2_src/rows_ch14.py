POP = "A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4)."

ROWS = [
# ---------------- Quiz: Normal distribution (Oct 23) ----------------
dict(id="ch14-quiz-01", source="Normal distribution quiz (2026), Q1", topics="central limit theorem", type="MC",
question="If you sample from a distribution that is not normal, the sampling distribution of the mean becomes approximately normal when samples are large. What is this rule called?",
options="""A) The law of large numbers
B) Bayes' theorem
C) The normal rule
D) The central limit theorem""",
answer="D",
explanation="The central limit theorem says the sampling distribution of a mean (or sum) becomes approximately normal as sample size grows, whatever the shape of the original distribution.",
why_wrong="""A) The law of large numbers says an estimate gets closer to the true value as n grows. It says nothing about the shape of the sampling distribution.
B) Bayes' theorem is about updating probabilities with new information.
C) Not a real rule.""",
hint="Which rule is about the shape of a sampling distribution?"),

dict(id="ch14-quiz-02", source="Normal distribution quiz (2026), Q2", topics="Z-transform, standard normal", type="matching",
question=POP + """

Any normal value can be converted to the standard normal (mean 0, SD 1) with Z = (Y - μ) / σ. Match each value of Y to its Z score:

1. Y = 0
2. Y = 4
3. Y = 12
4. Y = 20""",
options="""A) Z = -2
B) Z = -1
C) Z = 1
D) Z = 3""",
answer="1-A, 2-B, 3-C, 4-D",
explanation="Subtract the mean (8) and divide by the SD (4): (0 - 8)/4 = -2, (4 - 8)/4 = -1, (12 - 8)/4 = 1, (20 - 8)/4 = 3.",
why_wrong="Common mistake: dividing by the variance (16) instead of the SD (4).",
hint="The formula needs σ, but you were given σ². What is σ?"),

dict(id="ch14-quiz-03", source="Normal distribution quiz (2026), Q3a", topics="normal probabilities", type="numeric",
question=POP + "\n\nWhat is the probability that a random draw from this population is less than 8?",
answer="0.5", explanation="8 is the mean, and a normal distribution is symmetric around its mean, so half of all values fall below it.",
why_wrong="Common mistake: thinking the probability of being below the mean depends on the SD. It's always 0.5 for a normal.",
hint="Where is 8 relative to the mean?"),

dict(id="ch14-quiz-04", source="Normal distribution quiz (2026), Q3b", topics="normal probabilities, 68-95 rule", type="numeric",
question=POP + "\n\nRoughly what is the probability that a random draw is more than 12 or less than 4?",
answer="0.32", explanation="4 and 12 are one SD below and above the mean. About 68% of a normal falls within one SD of the mean, so about 32% falls outside (exactly 0.317).",
why_wrong="Common mistake: answering 0.68, which is the probability of falling between 4 and 12.",
hint="How many SDs from the mean are 4 and 12? What fraction of a normal lies within that range?"),

dict(id="ch14-quiz-05", source="Normal distribution quiz (2026), Q3c", topics="normal probabilities, 68-95 rule", type="numeric",
question=POP + "\n\nRoughly what is the probability that a random draw is more than 16 or less than 0?",
answer="0.05", explanation="0 and 16 are two SDs from the mean. About 95% of a normal falls within two SDs, so about 5% falls outside (exactly 0.0455).",
why_wrong="Common mistake: answering 0.025, which counts only one tail.",
hint="How many SDs away are 0 and 16? Count both tails."),

dict(id="ch14-quiz-06", source="Normal distribution quiz (2026), Q4a", topics="sampling distribution", type="MC",
question=POP + "\n\nImagine you take many samples of size four from this population and record the mean of each sample. What is the distribution of these means called?",
options="""A) The population distribution
B) The sampling distribution (of the mean)
C) The null distribution
D) The standard normal distribution""",
answer="B",
explanation="The distribution of an estimate (here, the mean) across many samples is the sampling distribution.",
why_wrong="""A) The population distribution describes individual values, not sample means.
C) A null distribution is a sampling distribution under the null hypothesis, used for testing.
D) The standard normal has mean 0 and SD 1; these means are centered on 8.""",
hint="These are means of samples, not individual values."),

dict(id="ch14-quiz-07", source="Normal distribution quiz (2026), Q4b-c", topics="standard error, sampling distribution", type="numeric",
question=POP + "\n\nYou take many samples of size four and record each sample's mean. What is the standard deviation of this distribution of sample means (its standard error)?",
answer="2", explanation="SE = σ / √n = 4 / √4 = 4 / 2 = 2.",
why_wrong="Common mistakes: using the variance (16 / 2 = 8), or dividing by n instead of √n (4 / 4 = 1).",
hint="SE = σ / √n."),

dict(id="ch14-quiz-08", source="Normal distribution quiz (2026), Q4c", topics="standard error", type="MC",
question="The standard deviation of the sampling distribution of the mean has a special name. What is it?",
options="""A) The residual standard deviation
B) The standard error
C) The variance
D) The Z score""",
answer="B",
explanation="The standard error is the standard deviation of a sampling distribution. It describes how much an estimate varies from sample to sample.",
why_wrong="""A) The residual SD describes how far individual points fall from a model's predictions.
C) The variance is the square of an SD.
D) A Z score is a single value's distance from the mean in SD units.""",
hint="It describes the uncertainty in an estimate."),

dict(id="ch14-quiz-09", source="Normal distribution quiz (2026), Q5a", topics="p-values, Z test", type="numeric",
question=POP + "\n\nYou take one sample of size four and estimate a mean of 4. Testing the null hypothesis that μ = 8, roughly what is the two-tailed p-value?",
answer="0.05", explanation="The standard error is 4 / √4 = 2, so the sample mean is (4 - 8) / 2 = -2 standard errors from the null value. The probability of being at least 2 SEs away (in either direction) is about 0.05 (exactly 0.0455).",
why_wrong="Common mistake: using σ (4) instead of the SE (2). That puts the mean only 1 SD away and gives p ≈ 0.32.",
hint="How many standard errors (not SDs) is 4 from 8?"),

dict(id="ch14-quiz-10", source="Normal distribution quiz (2026), Q5b-c", topics="NHST, interpreting p-values", type="MC",
question=POP + """

You take one sample of size four and estimate a mean of 4. The two-tailed p-value for the null hypothesis that μ = 8 is 0.046. Using α = 0.05, what do we do, and what do we know about whether the null is true?""",
options="""A) Reject the null; the null is false
B) Reject the null; we don't know whether the null is true or false
C) Fail to reject the null; the null is true
D) Fail to reject the null; we don't know whether the null is true or false""",
answer="B",
explanation="0.046 < 0.05, so we reject the null. But a p-value never proves the null false (or true): either the null is false, or it's true and we got an unusual sample (a type I error).",
why_wrong="""A) Rejecting the null isn't proof it's false.
C) and D) 0.046 is less than 0.05, so we reject.""",
hint="Compare p to α first. Then ask: can a single p-value tell us the truth for certain?"),

dict(id="ch14-quiz-11", source="Normal distribution quiz (2026), Q6", topics="transformations", type="MC",
question="Transformations are one way to proceed when data are skewed and don't meet the assumptions of a statistical test. Which of the following statements is FALSE?",
options="""A) In many cases, an appropriate transformation can make data roughly normal
B) We must transform every individual in the same way
C) We must apply the same transformation to x and to y
D) We can compare a few transformations to see which best normalizes the data, as long as we choose before running our statistical test""",
answer="C",
explanation="We transform a variable to fix its own problem, so x and y can be transformed differently (or one not at all). But every value of a given variable must get the same transformation, and the choice should be made before looking at test results.",
why_wrong="""A) True: log or square-root transforms often normalize right-skewed data.
B) True: transforming some individuals differently would distort the data.
D) True: choosing a transformation is fine; choosing it based on which gives the smallest p-value is not.""",
hint="Does transforming y force you to transform x?"),

dict(id="ch14-quiz-12", source="Normal distribution quiz (2026), Q7", topics="transformations", type="MC",
question="What is a potential problem with log and square-root transformations?",
options="""A) They might remove the one-to-one correspondence with original values
B) They are undefined for some values
C) They don't preserve the order of the original values""",
answer="B",
explanation="You can't take the log of zero or a negative number, or the square root of a negative number. Data with zeros often get log(x + 1) instead.",
why_wrong="""A) For positive numbers, each original value has exactly one log and one square root.
C) Both are monotonic for positive values: bigger values stay bigger.""",
hint="Try taking log(0) or √(-4)."),

dict(id="ch14-quiz-13", source="Normal distribution quiz (2026), Q8", topics="transformations", type="select-all",
question="What are potential problems with square transformations (x²) when data include negative values? (Select all that apply.)",
options="""A) They might remove the one-to-one correspondence with original values
B) They are undefined for some values
C) They don't preserve the order of the original values (not monotonic)""",
answer="A, C",
explanation="Squaring makes -3 and 3 both equal 9, so different values become the same (no longer one-to-one), and order is scrambled (-3 < 2, but 9 > 4). Squaring is defined for every number, though.",
why_wrong="B) You can square any number.",
hint="What are (-3)² and 3²?"),

# ---------------- Homework ----------------
dict(id="ch14-hw-01", source="Normal distribution homework, Q1", topics="Z-transform", type="numeric",
question="Wing length helps determine flight performance in birds. Wing length of adult house sparrows is normally distributed with a mean of 76 mm and an SD of 2 mm. How many standard deviations from the mean is a sparrow with a wing length of 79.5 mm?",
answer="1.75", explanation="Z = (79.5 - 76) / 2 = 1.75.",
why_wrong="Common mistake: forgetting to divide by the SD (3.5).",
hint="Z = (value - mean) / SD."),

dict(id="ch14-hw-02", source="Normal distribution homework, Q2", topics="Z-transform", type="MC",
question="Converting a value into the number of standard deviations it is from the mean, as (Y - μ) / σ, is called:",
options="""A) The central limit theorem
B) The q-transform
C) The log-transform
D) The Z-transform""",
answer="D",
explanation="The Z-transform rescales a value into standard deviations from the mean, putting it on the standard normal scale.",
why_wrong="""A) The CLT is about the shape of sampling distributions.
B) Not a real transform; qnorm() finds quantiles.
C) A log transform changes the shape of data; it doesn't standardize.""",
hint="The result is called a Z score."),

dict(id="ch14-hw-03", source="Normal distribution homework, Q3", topics="probability density, _norm functions", type="MC",
question="Wing length of adult house sparrows is normal with mean 76 mm and SD 2 mm. Which R code gives the probability density at a wing length of 79.5 mm?",
options="""A) dnorm(79.5, mean = 76, sd = 2)
B) pnorm(79.5, mean = 76, sd = 2)
C) qnorm(79.5, mean = 76, sd = 2)
D) rnorm(79.5, mean = 76, sd = 2)""",
answer="A",
explanation="dnorm() returns the density: the height of the normal curve at a value. (Here it equals 0.043.)",
why_wrong="""B) pnorm() returns a probability: the area below the value.
C) qnorm() takes a probability and returns a value (a quantile).
D) rnorm() draws random numbers.""",
hint="d is for density."),

dict(id="ch14-hw-04", source="Normal distribution homework, Q4", topics="probability density", type="TF",
question="Wing length of adult house sparrows is normal with mean 76 mm and SD 2 mm, and dnorm(79.5, mean = 76, sd = 2) = 0.043. TRUE or FALSE: the probability that a sparrow's wing is exactly 79.5 mm long is 0.043.",
options="""A) TRUE
B) FALSE""",
answer="B",
explanation="For a continuous variable, a density is the height of the curve, not a probability. The probability of any exact value is zero; probabilities come from areas under the curve over a range (e.g. between 79.4 and 79.6 mm).",
why_wrong="TRUE: densities can even be bigger than 1, so they can't be probabilities.",
hint="Is the probability of an exact value a height or an area?"),

dict(id="ch14-hw-05", source="Normal distribution homework, Q5", topics="normal probabilities, _norm functions", type="numeric",
question="""Wing length of adult house sparrows is normal with mean 76 mm and SD 2 mm. In R:

pnorm(77, mean = 76, sd = 2)
[1] 0.691

What proportion of sparrows have wings longer than 77 mm?""",
answer="0.309", explanation="pnorm() gives the area below 77 (0.691). The area above is 1 - 0.691 = 0.309.",
why_wrong="Common mistake: answering 0.691, the proportion shorter than 77 mm.",
hint="pnorm() gives the lower tail by default."),

dict(id="ch14-hw-06", source="Normal distribution homework, Q6", topics="normal probabilities, _norm functions", type="numeric",
question="""Wing length of adult house sparrows is normal with mean 76 mm and SD 2 mm. In R:

pnorm(77, mean = 76, sd = 2)
[1] 0.691
pnorm(79, mean = 76, sd = 2)
[1] 0.933

What proportion of sparrows have wings between 77 and 79 mm long?""",
answer="0.242", explanation="Area below 79 minus area below 77: 0.933 - 0.691 = 0.242.",
why_wrong="Common mistake: adding the two numbers, or using 1 minus one of them.",
hint="Shade the region between 77 and 79. Which two areas can you subtract?"),

dict(id="ch14-hw-07", source="Normal distribution homework, Q7", topics="standard error, sampling distribution", type="numeric",
question="Wing length of adult house sparrows is normal with mean 76 mm and SD 2 mm. Imagine we caught nine sparrows, calculated their mean wing length, and repeated this many times. What would the standard deviation of this sampling distribution be?",
answer="0.667", explanation="SE = σ / √n = 2 / √9 = 2 / 3 = 0.667 mm.",
why_wrong="Common mistake: dividing by n (2 / 9 = 0.22) instead of √n.",
hint="SE = σ / √n."),

dict(id="ch14-hw-08", source="Normal distribution homework, Q8", topics="assessing normality", type="TF",
question="Chick mass shortly before fledging predicts survival in birds. TRUE or FALSE: The mass of these 3,720 blue tit chicks 14 days after hatching is roughly normally distributed.",
image="ch14-hw-bluetit.png",
options="""A) TRUE
B) FALSE""",
answer="B",
explanation="The histogram is clearly left-skewed: a long tail of small (probably undernourished) chicks stretches to the left of the main peak.",
why_wrong="TRUE: the main peak looks bell-shaped, but the long left tail is far too big for a normal distribution.",
hint="Is the histogram symmetric?"),

dict(id="ch14-hw-09", source="Normal distribution homework, Q9", topics="central limit theorem", type="MC",
question="The histogram shows the mass of 3,720 blue tit chicks 14 days after hatching. Imagine we repeatedly sample chicks and calculate the mean mass of each sample. Of the options below, what is the smallest sample size for which the sampling distribution of the mean would be roughly normal?",
image="ch14-hw-bluetit.png",
options="""A) A sample of size 1: it's already normal
B) Three
C) Fifty
D) Never: the data are simply not normal""",
answer="C",
explanation="By the central limit theorem, means of large enough samples are roughly normal even when the data aren't. With a skew this strong, samples of 3 aren't enough; 50 is.",
why_wrong="""A) A sample of size 1 has the same skewed shape as the population.
B) Three values averaged still inherit much of the skew.
D) The CLT works even when the data aren't normal.""",
hint="What does the central limit theorem say happens as sample size grows?"),

# ---------------- ChimeIn ----------------
dict(id="ch14-chimein-01", source="Chime In (normal)", topics="law of large numbers, central limit theorem", type="matching",
question="""Match each statement with its name:

1. An estimate approaches its true parameter value as sample size gets large
2. The sampling distribution of a mean becomes approximately normal as sample size gets large""",
options="""A) The law of large numbers
B) The central limit theorem""",
answer="1-A, 2-B",
explanation="The law of large numbers is about where an estimate ends up (close to the truth). The central limit theorem is about the shape of the sampling distribution (normal).",
why_wrong="These two are easy to mix up. 'Large numbers' gets you close to the truth; 'central limit' gives you a normal shape.",
hint="Which statement is about shape?"),

dict(id="ch14-chimein-02", source="Chime In (normal)", topics="normal probabilities, Z-transform", type="numeric",
question="""What is the probability that a value drawn from a normal distribution with μ = 8 and σ = 4 is greater than 10? In R:

pnorm(10, mean = 8, sd = 4)
[1] 0.691""",
answer="0.309", explanation="10 is half an SD above the mean. pnorm() gives the area below 10 (0.691), so the area above is 1 - 0.691 = 0.309.",
why_wrong="Common mistake: answering 0.691 (the area below 10).",
hint="Which tail does pnorm() give by default?"),

dict(id="ch14-chimein-03", source="Chime In (normal)", topics="_norm functions", type="matching",
question="""The figure shows a normal distribution, a value x, the height of the curve at x, and the area to the right of x. Match each R function to what it does:

1. dnorm()
2. pnorm(lower.tail = FALSE)
3. qnorm()
4. rnorm()""",
image="ch14-chimein-norm-functions.png",
options="""A) Returns the probability density: the height of the curve (y) at x
B) Returns the probability of a value greater than x: the shaded area from x to infinity
C) Returns the value of x for which the area to its left equals a given probability (e.g. the 0.025 quantile)
D) Draws random values from the distribution""",
answer="1-A, 2-B, 3-C, 4-D",
explanation="d = density (height), p = probability (area), q = quantile (the x value for a given area), r = random draws.",
why_wrong="Common mix-up: pnorm() and qnorm() are inverses. pnorm() goes from x to an area; qnorm() goes from an area to x.",
hint="d, p, q, r: density, probability, quantile, random."),

# ---------------- Book: Normal summary ----------------
dict(id="ch14-book-01", source="Book: Normal summary (Q1)", topics="Z-transform", type="numeric",
question="Birth weight is a key predictor of infant health. The weights of singleton babies born in the U.S. are roughly normal, with a mean of 3.339 kg and an SD of 0.573 kg. Roughly how many standard deviations from the mean is a 5 kg baby?",
answer="2.9", near_duplicate_of="ch14-hw-01",
explanation="Z = (5 - 3.339) / 0.573 = 1.661 / 0.573 = 2.9.",
why_wrong="Common mistake: forgetting to subtract the mean (5 / 0.573 = 8.7).",
hint="Z = (value - mean) / SD."),

dict(id="ch14-book-02", source="Book: Normal summary (Q3-4)", topics="probability density", type="TF",
question="""Birth weight of U.S. singleton babies is normal with mean 3.339 kg and SD 0.573 kg. In R:

dnorm(5, mean = 3.339, sd = 0.573)
[1] 0.0104

TRUE or FALSE: 1.04% of babies weigh exactly 5 kg at birth.""",
options="""A) TRUE
B) FALSE""",
answer="B", near_duplicate_of="ch14-hw-04",
explanation="dnorm() gives a density (the height of the curve), not a probability. For a continuous variable the probability of any exact value is zero; probabilities are areas over a range.",
why_wrong="TRUE: confuses density with probability.",
hint="Which _norm function gives probabilities?"),

dict(id="ch14-book-03", source="Book: Normal summary (Q5)", topics="normal probabilities, _norm functions", type="MC",
question="""Birth weight of U.S. singleton babies is normal with mean 3.339 kg and SD 0.573 kg. Which R code gives the probability that a baby weighs more than 5 kg?""",
options="""A) dnorm(5, mean = 3.339, sd = 0.573)
B) pnorm(5, mean = 3.339, sd = 0.573)
C) pnorm(5, mean = 3.339, sd = 0.573, lower.tail = FALSE)
D) qnorm(5, mean = 3.339, sd = 0.573, lower.tail = FALSE)""",
answer="C",
explanation="pnorm() gives the area below a value; lower.tail = FALSE gives the area above it. (The answer is 0.0019: about 2 in 1,000 babies.)",
why_wrong="""A) dnorm() gives a density, not a probability.
B) This gives the probability of weighing less than 5 kg.
D) qnorm() expects a probability, not a weight.""",
hint="You want an area, and the upper tail."),

dict(id="ch14-book-04", source="Book: Normal summary (Q6)", topics="normal probabilities", type="MC",
question="""Birth weight of U.S. singleton babies is normal with mean 3.339 kg and SD 0.573 kg. In R:

pnorm(3, mean = 3.339, sd = 0.573)
[1] 0.277
pnorm(4, mean = 3.339, sd = 0.573)
[1] 0.876

What percentage of babies weigh between 3 and 4 kg?""",
options="""A) 40%
B) 50%
C) 60%
D) 70%""",
answer="C",
explanation="0.876 - 0.277 = 0.599, about 60%.",
why_wrong="Common mistakes: using just one of the two numbers, or adding them.",
hint="Area below 4 minus area below 3."),

dict(id="ch14-book-05", source="Book: Normal summary (Q7)", topics="standard error", type="MC",
question="Birth weight of U.S. singleton babies is normal with SD 0.573 kg. Imagine we took five babies born in a hospital and calculated their mean weight, and repeated this many times. The standard deviation of this sampling distribution would be about:",
options="""A) 0.11
B) 0.15
C) 0.25""",
answer="C", near_duplicate_of="ch14-hw-07",
explanation="SE = 0.573 / √5 = 0.573 / 2.24 = 0.256.",
why_wrong="""A) 0.573 / 5: divides by n instead of √n.
B) Not a standard calculation here.""",
hint="SE = σ / √n."),

dict(id="ch14-book-06", source="Book: Normal summary (Q8)", topics="assessing normality", type="open", include="no",
question="Birth weight is a key predictor of infant health. The weights of singleton babies born in the U.S. are roughly normal (mean 3.339 kg, SD 0.573 kg). Do you think birth weights are actually perfectly normal? If not, how might they deviate?",
answer="Model answer: No. Real traits are never perfectly normal. Birth weight can't be negative and a normal distribution has infinite tails. More importantly, premature births create a longer left tail (more very light babies than a normal predicts), and there may be a slight right skew from very large babies. The normal is a useful approximation for typical babies, but it will misjudge the extremes.",
explanation="The normal is a model. It works well near the middle but is often wrong in the tails, which is where many biological questions (e.g. low birth weight) live.",
hint="Think about the tails: what processes could create unusually light or heavy babies?"),
]
