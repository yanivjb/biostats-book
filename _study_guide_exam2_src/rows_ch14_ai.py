from ai_helpers import V, r
from scipy.stats import norm
POP = "A population is normally distributed with mean μ = 8 and variance σ² = 16 (so σ = 4)."
POP2 = "A population is normally distributed with mean μ = 50 and variance σ² = 100 (so σ = 10)."
SPAR = "Wing length helps determine flight performance in birds. Wing length of adult house sparrows is normally distributed with a mean of 76 mm and an SD of 2 mm."
BABY = "Birth weight is a key predictor of infant health. Birth weight of U.S. singleton babies is roughly normal, with mean 3.339 kg and SD 0.573 kg."
ROWS = [
V("ch14-quiz-01", 1,
question="Seed mass in a wildflower is strongly right-skewed. A botanist repeatedly takes samples of 100 seeds and calculates each sample's mean mass. Why is the distribution of these means roughly normal?",
options="""A) The central limit theorem
B) The law of large numbers
C) Bayes' theorem
D) The seeds themselves are normally distributed""",
answer="A", explanation="The central limit theorem says means of large samples are approximately normal, whatever the shape of the data.",
why_wrong="""B) The law of large numbers says the estimate approaches the truth, not that it becomes normal.
C) Bayes' theorem is about conditional probability.
D) The seed masses are skewed.""", hint="Which rule is about the shape of the sampling distribution?"),
V("ch14-quiz-01", 2,
question="Which statement describes the central limit theorem?",
options="""A) Sample means become approximately normal as sample size gets large
B) Sample estimates get closer to the true value as sample size gets large
C) Every biological variable is normal if we measure enough individuals
D) The data in a large sample always become approximately normal""",
answer="A", explanation="The CLT is about the sampling distribution of means (or sums): it becomes approximately normal with large samples, even when the data aren't.",
why_wrong="""B) That's the law of large numbers.
C) and D) The data keep their own shape; only the sampling distribution of the mean becomes normal.""", hint="Is it about the data or about the means?"),

V("ch14-quiz-02", 1, question=POP2 + "\n\nAny normal value can be converted to the standard normal (mean 0, SD 1) with Z = (Y - μ) / σ. Match each value of Y to its Z score:\n\n1. Y = 30\n2. Y = 45\n3. Y = 60\n4. Y = 75",
options="""A) Z = -2
B) Z = -0.5
C) Z = 1
D) Z = 2.5""", answer="1-A, 2-B, 3-C, 4-D",
explanation="(30 - 50)/10 = -2; (45 - 50)/10 = -0.5; (60 - 50)/10 = 1; (75 - 50)/10 = 2.5.", why_wrong="Subtract the mean, then divide by the SD.", hint="Z = (Y - 50) / 10."),
V("ch14-quiz-02", 2, question=POP + "\n\nAny normal value can be converted to the standard normal (mean 0, SD 1) with Z = (Y - μ) / σ. Match each Z score to its value of Y:\n\n1. Z = -1.5\n2. Z = 0\n3. Z = 0.5\n4. Z = 2",
options="""A) Y = 2
B) Y = 8
C) Y = 10
D) Y = 16""", answer="1-A, 2-B, 3-C, 4-D",
explanation="Y = μ + Z × σ: 8 - 1.5 × 4 = 2; 8 + 0 = 8; 8 + 0.5 × 4 = 10; 8 + 2 × 4 = 16.", why_wrong="Work backwards: Y = 8 + 4Z.", hint="Y = μ + Z × σ."),

V("ch14-quiz-03", 1, question=POP + "\n\nWhat is the probability that a random draw from this population is greater than 8?",
answer="0.5", explanation="8 is the mean, and the normal is symmetric around its mean, so half the values are above it.", hint="Where is 8 relative to the center?"),
V("ch14-quiz-03", 2, question=POP2 + "\n\nWhat is the probability that a random draw from this population is less than 50?",
answer="0.5", explanation="50 is the mean of a symmetric distribution, so half of all values fall below it.", hint="Where is 50 relative to the center?"),

V("ch14-quiz-04", 1, question=POP2 + "\n\nRoughly what is the probability that a random draw is more than 60 or less than 40?",
answer="0.32", explanation="40 and 60 are one SD from the mean. About 68% falls within one SD, so about 32% falls outside (exactly 0.317).", hint="How many SDs from the mean are 40 and 60?"),
V("ch14-quiz-04", 2, question=POP + "\n\nRoughly what is the probability that a random draw is between 4 and 12?",
answer="0.68", explanation="4 and 12 are one SD below and above the mean, and about 68% of a normal falls within one SD (exactly 0.683).", hint="How many SDs from the mean are 4 and 12?"),

V("ch14-quiz-05", 1, question=POP2 + "\n\nRoughly what is the probability that a random draw is more than 70 or less than 30?",
answer="0.05", explanation="30 and 70 are two SDs from the mean; about 95% falls within two SDs, so about 5% is outside (exactly 0.0455).", hint="How many SDs from the mean?"),
V("ch14-quiz-05", 2, question=POP + "\n\nRoughly what is the probability that a random draw is between 0 and 16?",
answer="0.95", explanation="0 and 16 are two SDs from the mean; about 95% of a normal falls within two SDs (exactly 0.954).", hint="How many SDs from the mean are 0 and 16?"),

V("ch14-quiz-06", 1,
question=POP + "\n\nYou take many samples of size 10 from this population and record the mean of each. The standard deviation of these means is called the standard error. What is the distribution of the means itself called?",
options="""A) The sampling distribution of the mean
B) The population distribution
C) The standard normal distribution
D) The null distribution""",
answer="A", explanation="The distribution of an estimate across repeated samples is its sampling distribution.",
why_wrong="""B) That's the distribution of individual values.
C) That's the normal with mean 0 and SD 1.
D) A null distribution is a sampling distribution assuming the null is true.""", hint="Distribution of estimates from many samples."),
V("ch14-quiz-06", 2,
question=POP + "\n\nWhich of these describes the distribution of individual values in the population, rather than the distribution of sample means?",
options="""A) The population distribution: mean 8 and SD 4
B) The sampling distribution: mean 8 and SD 4 / √n
C) The null distribution: mean 0 and SD 1
D) The standard normal: mean 8 and SD 1""",
answer="A", explanation="Individual values follow the population distribution (SD = σ = 4). Sample means follow the sampling distribution, whose SD (the SE) is σ / √n.",
why_wrong="""B) That's for sample means.
C) and D) These aren't this population's distribution of individuals.""", hint="Individuals vs means."),

V("ch14-quiz-07", 1, question=POP + "\n\nYou take many samples of size 16 and record each sample's mean. What is the standard error of the mean?",
answer=r(4/16**0.5,2), explanation="SE = σ / √n = 4 / √16 = 4 / 4 = 1.", hint="σ / √n."),
V("ch14-quiz-07", 2, question=POP2 + "\n\nYou take many samples of size 25 and record each sample's mean. What is the standard error of the mean?",
answer=r(10/5,2), explanation="SE = σ / √n = 10 / √25 = 10 / 5 = 2.", hint="σ / √n."),

V("ch14-quiz-08", 1,
question="A researcher repeatedly samples 20 mice, calculates the mean body mass of each sample, and finds the standard deviation of those means. What is this quantity called?",
options="""A) The standard error of the mean
B) The residual standard deviation
C) The population variance
D) The Z score""", answer="A",
explanation="The SD of a sampling distribution is the standard error.", why_wrong="""B) That's about residuals from a model.
C) That's the spread of individuals, squared.
D) A Z score is a single standardized value.""", hint="SD of the sampling distribution."),
V("ch14-quiz-08", 2,
question="What does the standard error of a mean describe?",
options="""A) How much the sample mean varies from sample to sample
B) How much individual values vary around the mean
C) The probability that the null hypothesis is true
D) How far the sample is from a normal distribution""", answer="A",
explanation="The standard error is the SD of the sampling distribution: how much estimates vary among samples.",
why_wrong="""B) That's the standard deviation.
C) Neither SE nor p-values give that.
D) That's about the shape, not the SE.""", hint="Variation among estimates, not individuals."),

V("ch14-quiz-09", 1, question=POP + "\n\nYou take one sample of size 16 and estimate a mean of 10. Testing the null hypothesis that μ = 8, roughly what is the two-tailed p-value?",
answer="0.05", explanation="SE = 4 / √16 = 1, so the mean is (10 - 8) / 1 = 2 SEs from the null value. About 5% of a normal is at least 2 SDs away (exactly 0.0455).", hint="First find the SE, then the Z."),
V("ch14-quiz-09", 2, question=POP + "\n\nYou take one sample of size four and estimate a mean of 10. Testing the null hypothesis that μ = 8, roughly what is the two-tailed p-value?",
answer="0.32", explanation="SE = 4 / √4 = 2, so the mean is (10 - 8) / 2 = 1 SE from the null value. About 32% of a normal is at least 1 SD away (exactly 0.317).", hint="First find the SE, then the Z."),

V("ch14-quiz-10", 1,
question=POP + "\n\nYou take one sample of size four and estimate a mean of 10. The two-tailed p-value for the null hypothesis that μ = 8 is 0.32. Using α = 0.05, what do we do, and what do we know about whether the null is true?",
options="""A) Reject the null; the null is false
B) Reject the null; we don't know whether the null is true
C) Fail to reject the null; the null is true
D) Fail to reject the null; we don't know whether the null is true""", answer="D",
explanation="0.32 > 0.05, so we fail to reject. But failing to reject doesn't show the null is true: we may simply lack power.",
why_wrong="""A) and B) p > α, so we don't reject.
C) Failing to reject isn't evidence the null is true.""", hint="Compare p to α, then remember what p can't tell you."),
V("ch14-quiz-10", 2,
question="A study tests whether a fertilizer changes plant height and gets p = 0.01. Using α = 0.05, which statement is correct?",
options="""A) We reject the null, and we know the fertilizer changes height
B) We reject the null, but we don't know for sure that the null is false
C) We fail to reject the null, so the fertilizer has no effect
D) We fail to reject the null, but we don't know if it is true""", answer="B",
explanation="p < α, so we reject. But rejecting doesn't prove the null false: a true null still gives p < 0.05 in 5% of studies (a type I error).",
why_wrong="""A) Rejection isn't proof.
C) and D) p < α, so we reject.""", hint="Can a true null give p = 0.01?"),

V("ch14-quiz-11", 1,
question="Body masses of shrews are right-skewed, and a researcher considers transforming them before a statistical test. Which of the following is TRUE?",
options="""A) Every shrew's mass must be transformed in the same way
B) If mass is transformed, the explanatory variable must be too
C) Try many transformations and keep the one with the smallest p
D) Transforming the data is never appropriate in statistics""", answer="A",
explanation="All values of a variable get the same transformation. Different variables can be transformed differently, and the choice is made before testing.",
why_wrong="""B) Each variable is transformed (or not) on its own merits.
C) Choosing by p-value is p-hacking.
D) Transformations are often appropriate.""", hint="What must be consistent within one variable?"),
V("ch14-quiz-11", 2,
question="Which of these is a legitimate way to choose a transformation for skewed data?",
options="""A) Compare a few transformations' normality before running the test
B) Run the test on several transformations; keep the significant one
C) Transform the large values only, leaving the small values alone
D) Transform the response only in the group that looks most skewed""", answer="A",
explanation="It's fine to compare transformations by how well they normalize the data, as long as you decide before seeing test results and apply it to all values.",
why_wrong="""B) That's p-hacking.
C) and D) All values of a variable must get the same transformation.""", hint="When should the choice be made?"),

V("ch14-quiz-12", 1,
question="A dataset of parasite counts includes many zeros. Why can't we simply log-transform the counts?",
options="""A) The log of zero is undefined
B) The log changes the order of the values
C) Logs only work on normally distributed data
D) Logs turn different counts into the same value""", answer="A",
explanation="log(0) is undefined (negative infinity). A common fix is log(x + 1).",
why_wrong="""B) The log keeps the order.
C) Logs are often used to make skewed data more normal.
D) The log is one-to-one.""", hint="What is log(0)?"),
V("ch14-quiz-12", 2,
question="A variable has values ranging from -5 to 20. Which transformation could NOT be applied to all of these values?",
options="""A) The square root
B) Adding a constant of 10
C) Multiplying by 2
D) Squaring""", answer="A",
explanation="The square root of a negative number is undefined (and so is the log).",
why_wrong="B), C) and D) are defined for every number.", hint="Which one fails for negative numbers?"),

V("ch14-quiz-13", 1,
question="Data on temperature change include negative and positive values (e.g. -3 and 3). What happens if we square them? (Select all that apply.)",
options="""A) -3 and 3 both become 9, so different values become the same
B) The order of values is no longer preserved
C) The transformation is undefined for negative values
D) The transformation is undefined when the value is zero""", answer="A, B",
explanation="Squaring maps -3 and 3 to 9 (not one-to-one), and it scrambles order (-3 < 2, but 9 > 4). Squaring is defined for every number.",
why_wrong="""C) and D) Every number, including negatives and zero, can be squared.""", hint="Try squaring -3, 2 and 3."),
V("ch14-quiz-13", 2,
question="Which transformations keep the order of values (a larger value stays larger) when ALL data are positive? (Select all that apply.)",
options="""A) The log
B) The square root
C) Squaring
D) Taking 1 / x""", answer="A, B, C",
explanation="For positive numbers, log, square root and squaring are all increasing. 1/x reverses the order (2 < 4, but 1/2 > 1/4).",
why_wrong="D) 1/x reverses the order.", hint="Try each on the values 2 and 4."),

V("ch14-hw-01", 1, question=SPAR + " How many standard deviations from the mean is a sparrow with a wing length of 73 mm?",
answer=r((73-76)/2,2), explanation="Z = (73 - 76) / 2 = -1.5.", hint="(Y - μ) / σ."),
V("ch14-hw-01", 2, question=SPAR + " What wing length is 2.5 standard deviations above the mean?",
answer=r(76+2.5*2,1), explanation="Y = μ + Z × σ = 76 + 2.5 × 2 = 81 mm.", hint="Y = μ + Z × σ."),

V("ch14-hw-02", 1,
question="A biologist rescales tail lengths by subtracting the population mean and dividing by the population SD. What is this called, and what is the mean of the rescaled values?",
options="""A) The Z-transform; mean 0
B) The Z-transform; mean 1
C) The log-transform; mean 0
D) The central limit theorem; mean 1""", answer="A",
explanation="(Y - μ) / σ is the Z-transform. The rescaled values have mean 0 and SD 1.",
why_wrong="""B) The SD is 1; the mean is 0.
C) No logs are taken.
D) The CLT is about sampling distributions.""", hint="What happens to the mean after subtracting it?"),
V("ch14-hw-02", 2,
question="After a Z-transform, (Y - μ) / σ, a value of Z = -1 means the original value was:",
options="""A) One standard deviation below the mean
B) One unit below the mean, in the original units
C) One standard error below the mean
D) Smaller than every other value in the data""", answer="A",
explanation="Z counts standard deviations from the mean; negative means below.",
why_wrong="""B) Z is in SD units, not original units.
C) Z uses σ, not the SE.
D) It's one SD below the mean, not the minimum.""", hint="What units is Z in?"),

V("ch14-hw-03", 1,
question=SPAR + " Which R code gives the proportion of sparrows with wings shorter than 74 mm?",
options="""A) dnorm(74, mean = 76, sd = 2)
B) pnorm(74, mean = 76, sd = 2)
C) qnorm(74, mean = 76, sd = 2)
D) rnorm(74, mean = 76, sd = 2)""", answer="B",
explanation="pnorm() gives the area below a value (here 0.159).",
why_wrong="""A) dnorm() gives the curve's height.
C) qnorm() takes a probability and returns a value.
D) rnorm() draws random values.""", hint="p for probability (area)."),
V("ch14-hw-03", 2,
question=SPAR + " Which R code gives the wing length below which 2.5% of sparrows fall?",
options="""A) dnorm(0.025, mean = 76, sd = 2)
B) pnorm(0.025, mean = 76, sd = 2)
C) qnorm(0.025, mean = 76, sd = 2)
D) rnorm(0.025, mean = 76, sd = 2)""", answer="C",
explanation="qnorm() takes a probability and returns the value (quantile) with that area to its left: about 72.1 mm.",
why_wrong="""A) dnorm() gives a height.
B) pnorm() takes a value and returns an area.
D) rnorm() draws random values.""", hint="q for quantile."),

V("ch14-hw-04", 1,
question=SPAR + " TRUE or FALSE: dnorm(76, mean = 76, sd = 2) = 0.199 means that 19.9% of sparrows have wings exactly 76 mm long.",
options="""A) TRUE
B) FALSE""", answer="B",
explanation="dnorm() gives the height of the curve (a density). For a continuous variable, the probability of any exact value is zero; probabilities are areas.",
why_wrong="TRUE: a density is not a probability.", hint="Height or area?"),
V("ch14-hw-04", 2,
question=SPAR + " TRUE or FALSE: To find the probability a sparrow's wing is between 75 and 77 mm, we calculate pnorm(77, 76, 2) - pnorm(75, 76, 2).",
options="""A) TRUE
B) FALSE""", answer="A",
explanation="Probabilities are areas. The area below 77 minus the area below 75 is the area between them (0.383).",
why_wrong="FALSE: subtracting the two pnorm() areas gives exactly the area between.", hint="Area below 77 minus area below 75."),

V("ch14-hw-05", 1, question=SPAR + " In R:\n\npnorm(73, mean = 76, sd = 2)\n[1] 0.0668\n\nWhat proportion of sparrows have wings longer than 73 mm?",
answer=r(1-0.0668,4), explanation="1 - 0.0668 = 0.9332.", hint="pnorm() gives the area below."),
V("ch14-hw-05", 2, question=SPAR + " In R:\n\npnorm(78, mean = 76, sd = 2, lower.tail = FALSE)\n[1] 0.159\n\nWhat proportion of sparrows have wings shorter than 78 mm?",
answer=r(1-0.159,3), explanation="lower.tail = FALSE gives the area above 78 (0.159), so the area below is 1 - 0.159 = 0.841.", hint="The two areas add to 1."),

V("ch14-hw-06", 1, question=SPAR + " In R:\n\npnorm(74, mean = 76, sd = 2)\n[1] 0.159\npnorm(78, mean = 76, sd = 2)\n[1] 0.841\n\nWhat proportion of sparrows have wings between 74 and 78 mm long?",
answer=r(0.841-0.159,3), explanation="0.841 - 0.159 = 0.682 (within one SD of the mean, as expected).", hint="Area below 78 minus area below 74."),
V("ch14-hw-06", 2, question=SPAR + " In R:\n\npnorm(72, mean = 76, sd = 2)\n[1] 0.0228\npnorm(75, mean = 76, sd = 2)\n[1] 0.309\n\nWhat proportion of sparrows have wings between 72 and 75 mm long?",
answer=r(0.309-0.0228,3), explanation="0.309 - 0.0228 = 0.286.", hint="Area below 75 minus area below 72."),

V("ch14-hw-07", 1, question=SPAR + " Imagine we caught 16 sparrows, calculated their mean wing length, and repeated this many times. What would the standard deviation of this sampling distribution be?",
answer=r(2/4,2), explanation="SE = σ / √n = 2 / √16 = 0.5 mm.", hint="σ / √n."),
V("ch14-hw-07", 2, question=SPAR + " Imagine we caught four sparrows, calculated their mean wing length, and repeated this many times. What would the standard deviation of this sampling distribution be?",
answer=r(2/2,2), explanation="SE = σ / √n = 2 / √4 = 1 mm.", hint="σ / √n."),

V("ch14-hw-08", 1, image="ch14-hw-bluetit.png",
question="Chick mass shortly before fledging predicts survival in birds. The histogram shows the mass of 3,720 blue tit chicks 14 days after hatching. TRUE or FALSE: The distribution of chick mass is left-skewed (a long tail toward small values).",
options="""A) TRUE
B) FALSE""", answer="A",
explanation="Most chicks cluster near the peak, with a long tail of lighter chicks stretching to the left.",
why_wrong="FALSE: look at which side has the long tail.", hint="Which side has the long tail?"),
V("ch14-hw-08", 2, image="ch14-hw-bluetit.png",
question="Chick mass shortly before fledging predicts survival in birds. The histogram shows the mass of 3,720 blue tit chicks 14 days after hatching. TRUE or FALSE: Because there are 3,720 chicks, the central limit theorem makes these individual masses normally distributed.",
options="""A) TRUE
B) FALSE""", answer="B",
explanation="The CLT is about sample means, not individual values. The masses themselves stay left-skewed however many chicks we measure.",
why_wrong="TRUE: the CLT applies to the sampling distribution of the mean, not to the data.", hint="Does the CLT describe data or means?"),

V("ch14-hw-09", 1, image="ch14-hw-bluetit.png",
question="The histogram shows the mass of 3,720 blue tit chicks 14 days after hatching. We repeatedly sample chicks and calculate each sample's mean mass. How does the sampling distribution of the mean change as sample size grows from 2 to 100?",
options="""A) It becomes more normal and narrower
B) It becomes more skewed and wider
C) It becomes more normal, but no narrower
D) It stays the shape of the data""", answer="A",
explanation="By the CLT, the sampling distribution becomes more normal, and its spread (the SE) shrinks with √n.",
why_wrong="""B) Larger samples make it less skewed and narrower.
C) The SE shrinks as n grows.
D) Means of large samples become normal.""", hint="Think about both the CLT and σ / √n."),
V("ch14-hw-09", 2, image="ch14-hw-bluetit.png",
question="The histogram shows the mass of 3,720 blue tit chicks 14 days after hatching. Imagine taking many samples of size 2 and calculating each sample's mean mass. What shape would the sampling distribution most likely have?",
options="""A) Somewhat left-skewed, like the data
B) Perfectly normal, by the CLT
C) Right-skewed, the opposite of the data
D) Uniform, with all means equally likely""", answer="A",
explanation="With n = 2, means still carry much of the data's skew. The CLT only kicks in with larger samples.",
why_wrong="""B) The CLT needs large samples, especially for skewed data.
C) Averaging doesn't flip the skew.
D) There's no reason for a uniform shape.""", hint="Is n = 2 large?"),

V("ch14-chimein-01", 1,
question="Match each example to the idea it illustrates:\n\n1. As a field crew measures more and more trees, their mean height gets closer to the forest's true mean\n2. Means of many samples of 50 skewed seed masses form a bell-shaped histogram",
options="""A) The law of large numbers
B) The central limit theorem""", answer="1-A, 2-B",
explanation="Approaching the truth is the law of large numbers; the bell shape of the sampling distribution is the central limit theorem.",
why_wrong="One is about where the estimate ends up; the other is about the shape.", hint="Accuracy vs shape."),
V("ch14-chimein-01", 2,
question="Match each statement with its name:\n\n1. Describes the shape of the sampling distribution of a mean in large samples\n2. Describes how close a large sample's estimate gets to the true parameter",
options="""A) The law of large numbers
B) The central limit theorem""", answer="1-B, 2-A",
explanation="The CLT is about shape (normal); the law of large numbers is about estimates approaching the truth.",
why_wrong="Shape → CLT; closeness to truth → law of large numbers.", hint="Which one is about shape?"),

V("ch14-chimein-02", 1, question="What is the probability that a value drawn from a normal distribution with μ = 8 and σ = 4 is less than 6? In R:\n\npnorm(6, mean = 8, sd = 4)\n[1] 0.309",
answer="0.309", explanation="pnorm() gives the area below 6 directly: 0.309.", hint="pnorm() gives the area below the value."),
V("ch14-chimein-02", 2, question="What is the probability that a value drawn from a normal distribution with μ = 8 and σ = 4 is greater than 14? In R:\n\npnorm(14, mean = 8, sd = 4)\n[1] 0.933",
answer=r(1-0.933,3), explanation="pnorm() gives the area below 14 (0.933), so the area above is 1 - 0.933 = 0.067.", hint="Area above = 1 - area below."),

V("ch14-chimein-03", 1, image="ch14-chimein-norm-functions.png",
question="The figure shows a normal distribution, a value x, the height of the curve at x, and the area to the right of x. Match each task to the R function you'd use:\n\n1. Simulate 100 values from the distribution\n2. Find the height of the curve at x\n3. Find the value of x with 2.5% of the area to its left\n4. Find the area to the right of x",
options="""A) dnorm()
B) pnorm(lower.tail = FALSE)
C) qnorm()
D) rnorm()""", answer="1-D, 2-A, 3-C, 4-B",
explanation="r = random draws; d = density (height); q = quantile; p = probability (area).", why_wrong="Match the first letter: d, p, q, r.", hint="d = density, p = probability, q = quantile, r = random."),
V("ch14-chimein-03", 2, image="ch14-chimein-norm-functions.png",
question="The figure shows a normal distribution, a value x, the height of the curve at x, and the area to the right of x. Match each R function to what it takes as its main input:\n\n1. pnorm()\n2. qnorm()\n3. rnorm()",
options="""A) A value of x
B) A probability (an area)
C) The number of random values to draw""", answer="1-A, 2-B, 3-C",
explanation="pnorm(x) returns an area; qnorm(p) returns a value; rnorm(n) returns n random draws.", why_wrong="pnorm and qnorm are inverses.", hint="pnorm and qnorm undo each other."),

V("ch14-book-01", 1, question=BABY + " Roughly how many standard deviations from the mean is a 2 kg baby?",
answer=r((2-3.339)/0.573,1), explanation="Z = (2 - 3.339) / 0.573 = -1.339 / 0.573 = -2.3.", hint="(Y - μ) / σ."),
V("ch14-book-01", 2, question=BABY + " What birth weight (in kg) is two standard deviations above the mean?",
answer=r(3.339+2*0.573,2), explanation="3.339 + 2 × 0.573 = 4.485 kg.", hint="μ + 2σ."),

V("ch14-book-02", 1,
question=BABY + " In R:\n\ndnorm(3.339, mean = 3.339, sd = 0.573)\n[1] 0.696\n\nTRUE or FALSE: 69.6% of babies weigh exactly 3.339 kg.",
options="""A) TRUE
B) FALSE""", answer="B",
explanation="dnorm() is the height of the curve, not a probability. The probability of any exact weight is zero.", why_wrong="TRUE: densities aren't probabilities.", hint="Height or area?"),
V("ch14-book-02", 2,
question=BABY + " TRUE or FALSE: pnorm(3, mean = 3.339, sd = 0.573) gives the probability that a baby weighs less than 3 kg.",
options="""A) TRUE
B) FALSE""", answer="A",
explanation="pnorm() returns the area to the left of a value: the probability of a smaller value (here 0.277).", why_wrong="FALSE: pnorm() is exactly the area below.", hint="What does pnorm() return?"),

V("ch14-book-03", 1,
question=BABY + " Which R code gives the probability that a baby weighs less than 2.5 kg?",
options="""A) dnorm(2.5, mean = 3.339, sd = 0.573)
B) pnorm(2.5, mean = 3.339, sd = 0.573)
C) pnorm(2.5, mean = 3.339, sd = 0.573, lower.tail = FALSE)
D) qnorm(2.5, mean = 3.339, sd = 0.573)""", answer="B",
explanation="pnorm() gives the area below 2.5 (about 0.07).",
why_wrong="""A) dnorm() gives a height.
C) That's the area above 2.5.
D) qnorm() takes a probability.""", hint="Area below a value."),
V("ch14-book-03", 2,
question=BABY + " Which R code gives the birth weight that only 1% of babies exceed?",
options="""A) qnorm(0.99, mean = 3.339, sd = 0.573)
B) pnorm(0.99, mean = 3.339, sd = 0.573)
C) dnorm(0.99, mean = 3.339, sd = 0.573)
D) qnorm(0.01, mean = 3.339, sd = 0.573)""", answer="A",
explanation="99% of babies fall below the 0.99 quantile, so only 1% exceed it (about 4.67 kg).",
why_wrong="""B) and C) take a weight, not a probability.
D) That's the weight 1% fall BELOW.""", hint="Which quantile has 1% above it?"),

V("ch14-book-04", 1,
question=BABY + " In R:\n\npnorm(2.5, mean = 3.339, sd = 0.573)\n[1] 0.072\npnorm(4.5, mean = 3.339, sd = 0.573)\n[1] 0.979\n\nWhat percentage of babies weigh between 2.5 and 4.5 kg?",
options="""A) About 7%
B) About 21%
C) About 91%
D) About 98%""", answer="C",
explanation="0.979 - 0.072 = 0.907, about 91%.",
why_wrong="""A) That's the share below 2.5 kg.
B) That's not an area from this output.
D) That's the share below 4.5 kg.""", hint="Subtract the two areas."),
V("ch14-book-04", 2,
question=BABY + " In R:\n\npnorm(4, mean = 3.339, sd = 0.573)\n[1] 0.876\n\nWhat percentage of babies weigh more than 4 kg?",
options="""A) About 12%
B) About 24%
C) About 50%
D) About 88%""", answer="A",
explanation="1 - 0.876 = 0.124, about 12%.",
why_wrong="""B) Doubles the tail.
C) 4 kg is above the mean, so fewer than half are heavier.
D) That's the share below 4 kg.""", hint="Area above = 1 - area below."),

V("ch14-book-05", 1,
question="Birth weight of U.S. singleton babies has SD 0.573 kg. Imagine we took 25 babies, calculated their mean weight, and repeated this many times. The standard deviation of this sampling distribution would be about:",
options="""A) 0.023
B) 0.115
C) 0.573""", answer="B",
explanation="SE = 0.573 / √25 = 0.573 / 5 = 0.115.",
why_wrong="""A) Divides by 25 instead of √25.
C) That's the SD of individuals.""", hint="σ / √n."),
V("ch14-book-05", 2,
question="Birth weight of U.S. singleton babies has SD 0.573 kg. If we increase the number of babies in each sample from 5 to 20, what happens to the standard error of the mean?",
options="""A) It is cut in half
B) It is cut to a quarter
C) It stays the same""", answer="A",
explanation="SE = σ / √n. Quadrupling n doubles √n, so the SE halves (0.256 → 0.128).",
why_wrong="""B) The SE scales with √n, not n.
C) The SE shrinks as n grows.""", hint="How does √n change when n is multiplied by 4?"),
]
