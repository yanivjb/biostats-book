from ai_helpers import V, r
def R(orig, k, **kw):
    d = V(orig, k, **kw); d['chapter'] = '0'; return d
ROWS = [
R("rev-exam1-q06", 1, question="A student says, \"The standard error tells me how much the individuals in my sample differ from each other.\" Why are they wrong?",
options="""A) The SE describes how much estimates vary among samples, not individuals
B) The SE is only defined for categorical data, not for measurements
C) The SE is calculated before any data are collected in a study
D) They aren't wrong; that is what the standard error describes""", answer="A",
explanation="Variation among individuals is the SD. The SE describes uncertainty in an estimate across repeated samples.",
why_wrong="""B) and C) Not true.
D) That's the SD.""", hint="Individuals vs estimates."),
R("rev-exam1-q06", 2, question="Which describes the sampling distribution of a mean?",
options="""A) The distribution of means from many samples of the same size
B) The distribution of individual values within one sample
C) The distribution of individual values in the population
D) The distribution of p-values from many repeated studies""", answer="A",
explanation="A sampling distribution is the distribution of an estimate across repeated samples.",
why_wrong="""B) That's the sample distribution.
C) That's the population distribution.
D) Not what it means.""", hint="Distribution of estimates."),

R("rev-exam1-q08", 1, question="To estimate the average size of fish in a lake, you measure fish caught with a net whose holes let small fish escape. This sampling method likely introduces...",
options="""A) Sampling bias, because small fish are less likely to be measured
B) Sampling error, because estimates differ among samples by chance
C) Non-independence, because fish from one school are related
D) Measurement error, because rulers are imprecise for fish""", answer="A",
explanation="The net systematically misses small fish, so the estimate will be too large: bias.",
why_wrong="""B) Sampling error is random, not systematic.
C) and D) Not the main issue.""", hint="Is the error systematic?"),
R("rev-exam1-q08", 2, question="To estimate how much time people spend outdoors, a researcher surveys visitors at a national park. Which problem is this design most likely to have?",
options="""A) Sampling bias: park visitors likely spend more time outdoors
B) Sampling error: a larger sample would remove the problem
C) Non-independence: visitors were all asked the same questions
D) No problem: anyone could visit the park on any day""", answer="A",
explanation="Park visitors aren't representative of everyone; more data won't fix a biased sampling frame.",
why_wrong="""B) Larger samples don't fix bias.
C) Same questions don't cause non-independence.
D) The sample isn't representative.""", hint="Who gets sampled?"),

R("rev-exam1-q23", 1, question="A study reports a mean beak depth of 9.4 mm with a standard error of 0.1 mm. In plain words, the 0.1 mm roughly conveys:",
options="""A) How far the sample mean typically is from the true mean
B) How far a typical bird's beak is from the mean beak depth
C) The probability that the sample mean is wrong
D) The amount of bias introduced by the sampling method""", answer="A",
explanation="The SE describes uncertainty in the estimate due to sampling error.",
why_wrong="""B) That's the SD.
C) Not a probability.
D) The SE doesn't measure bias.""", hint="Uncertainty in the estimate."),
R("rev-exam1-q23", 2, question="Two studies measure the same trait with the same SD, but one has n = 25 and the other n = 100. How do their standard errors compare?",
options="""A) The n = 100 study's SE is half as large
B) The n = 100 study's SE is a quarter as large
C) Both studies have exactly the same SE
D) The n = 100 study's SE is twice as large""", answer="A",
explanation="SE = SD / √n; √100 / √25 = 2, so the SE halves.",
why_wrong="""B) SE scales with √n.
C) n differs.
D) Larger n means smaller SE.""", hint="SD / √n."),

R("rev-exam1-q04", 1, question="You conduct the same study twice, once with 20 individuals and once with 500. Which estimate(s) are most likely to be smaller in the study with 500? (Select all that apply.)",
options="""A) The standard error
B) The width of the 95% confidence interval
C) The standard deviation
D) The mean""", answer="A, B",
explanation="Uncertainty (SE, CI width) shrinks with n; the SD and mean estimate population values that don't depend on n.",
why_wrong="""C) and D) don't systematically change with n.""", hint="Uncertainty vs population values."),
R("rev-exam1-q04", 2, question="As sample size increases, which estimates are expected to stay about the same (but become more precise)? (Select all that apply.)",
options="""A) The mean
B) The standard deviation
C) The standard error
D) The width of the 95% CI""", answer="A, B",
explanation="The mean and SD estimate fixed population values. The SE and CI width shrink with n.",
why_wrong="""C) and D) shrink.""", hint="Which ones estimate population parameters?"),

R("rev-exam1-q21", 1, question="You put one bird feeder in each of two backyards (one with seed A, one with seed B) and count visits by 40 birds at each. What's the main problem?",
options="""A) Birds at each feeder share a backyard, so they aren't independent
B) A sample of 40 birds per feeder is far too small to say anything
C) The researcher should have been blinded to the type of seed
D) There's no problem with this design for comparing the seeds""", answer="A",
explanation="Seed type is confounded with backyard; the real replicates are feeders (n = 1 each).",
why_wrong="""B) Not the main problem.
C) Blinding doesn't fix pseudoreplication.
D) There's a big problem.""", hint="What's the unit of replication?"),
R("rev-exam1-q21", 2, question="A researcher compares two diets by giving each diet to one cage of 20 mice. How many independent replicates are there per diet?",
options="""A) 1
B) 20
C) 40
D) 10""", answer="A",
explanation="Diet was applied to whole cages, so each cage is one replicate; mice in a cage are not independent.",
why_wrong="""B) and C) Count mice, not cages.
D) No basis.""", hint="What received the treatment?"),

R("rev-exam1-q09", 1, question="A p-value of 0.30 means: (select all correct)",
options="""A) We fail to reject the null hypothesis (at α = 0.05)
B) 30% of samples from the null would be as or more extreme than ours
C) There is a 30% chance that the null is true
D) The null is true""", answer="A, B",
explanation="p > 0.05, so we fail to reject. B is the definition of a p-value.",
why_wrong="""C) p isn't P(null).
D) Failing to reject isn't proof.""", hint="Definition of p."),
R("rev-exam1-q09", 2, question="Which statements about a p-value are correct? (select all correct)",
options="""A) It is calculated assuming the null hypothesis is true
B) It's the probability of a result at least this extreme if the null were true
C) It is the probability that the null hypothesis is true
D) It measures how large the effect is""", answer="A, B",
explanation="p assumes the null and gives the probability of data at least this extreme.",
why_wrong="""C) Reversed conditional.
D) p mixes effect size and sample size.""", hint="P(data | null)."),

R("rev-exam1-q11", 1, question="What would happen if the field changed the custom from α = 0.05 to α = 0.10? (select all correct)",
options="""A) We would reject more true nulls (more type I errors)
B) We would reject fewer false nulls (less power)
C) We would reject more false nulls (more power)
D) We would use 90% confidence intervals, which are narrower""", answer="A, C, D",
explanation="A larger α makes rejecting easier: more false positives, more power, and narrower (90%) intervals.",
why_wrong="B) Power goes up.", hint="Easier to reject."),
R("rev-exam1-q11", 2, question="Lowering α from 0.05 to 0.01 makes which error MORE likely? (select all correct)",
options="""A) Failing to reject a false null (type II error)
B) Rejecting a true null (type I error)
C) Both type I and type II errors
D) Neither type I nor type II errors""", answer="A",
explanation="A stricter α reduces type I errors but increases type II errors (lower power).",
why_wrong="""B) Type I errors become less likely.
C) and D) There's a trade-off.""", hint="Harder to reject."),

R("rev-ch11-new-01", 1, image="ch11-lineup-null.png", question="Permutation eye-test: the plot shows 20 panels of Adelie penguin body mass on Biscoe vs Dream islands, with means and 95% CIs. One panel is the real data; the other 19 were made by shuffling the island labels.\n\nWhat do the 19 shuffled panels represent?",
options="""A) What data would look like if island had no effect on mass
B) What data would look like if Biscoe penguins were heavier
C) Repeated real samples taken from the two penguin islands
D) Bootstrap resamples used to build a confidence interval""", answer="A",
explanation="Shuffling labels breaks any link between island and mass, simulating the null.",
why_wrong="""B) That's an alternative.
C) They're not new samples.
D) Bootstrapping resamples with replacement within groups; this shuffles labels.""", hint="What does shuffling remove?"),
R("rev-ch11-new-01", 2, image="ch11-lineup-null.png", question="Permutation eye-test: the plot shows 20 panels of Adelie penguin body mass on Biscoe vs Dream islands, with means and 95% CIs. One panel is the real data; the other 19 were made by shuffling the island labels.\n\nIf the real panel clearly stood out from all 19 shuffled panels, what would that suggest?",
options="""A) The real difference is unusual under the null (p ≤ 1/20)
B) Shuffling was done incorrectly, so the test is invalid
C) The islands certainly have identical mean body masses
D) Nothing; line-ups can't tell us anything about the data""", answer="A",
explanation="If the real data stand out from 19 null panels, a pattern that strong would rarely arise by chance (like p ≤ 0.05).",
why_wrong="""B) Standing out is the point.
C) The opposite.
D) Line-ups are a visual permutation test.""", hint="1 real vs 19 null."),

R("rev-exam1-q24", 1, question="Which study is an experiment?",
options="""A) Randomly assigning plants to shade or full sun, then measuring growth
B) Comparing growth of plants that happen to grow in shade or sun
C) Measuring growth of plants along a natural light gradient
D) Surveying gardeners about where their plants grow best""", answer="A",
explanation="In an experiment the researcher assigns the explanatory variable (ideally at random).",
why_wrong="B), C) and D) observe existing conditions.", hint="Who sets the explanatory variable?"),
R("rev-exam1-q24", 2, question="Why does random assignment allow causal conclusions?",
options="""A) It balances confounders, measured or not, on average
B) It guarantees a large sample size for the study
C) It removes all sampling error from the results
D) It ensures every individual responds the same way""", answer="A",
explanation="Randomization breaks links between the treatment and other variables, so differences can be attributed to the treatment.",
why_wrong="""B) Unrelated.
C) Sampling error remains.
D) Individuals still vary.""", hint="What happens to confounders?"),
]
