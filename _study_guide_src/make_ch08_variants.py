"""AI-written variants of the chapter 8 questions ("Try a similar question").

Each variant tests the same idea and the same misconception as its original, with a new
scenario, new numbers, or a new plot. Numbers and plots come from plots/ch08_variant_plots.py.
"""
import csv

D = "all (AI variant)"
V = []


def add(orig, n, type_, topics, question, options, answer, explanation, why_wrong, hint, image="", flags=""):
    V.append({"id": f"{orig}-v{n}", "source": f"AI variant of {orig}", "chapter": "8", "topics": topics,
              "type": type_, "question": question, "options": options, "answer": answer,
              "explanation": explanation, "why_wrong": why_wrong, "hint": hint, "image": image,
              "include": "yes", "near_duplicate_of": orig, "flags": flags, "drafted_by_claude": D,
              "reveals_answer_to": "", "variant_of": orig})


EP = "A) estimates\nB) parameters\nC) sample\nD) population"
OAK = ("Imagine we could measure every one of the 8,000 red oaks in a forest: their mean height is 18.0 m and the SD is 4.0 m. "
       "The plot shows sampling distributions of the mean height for random samples of n = 4, 16 and 64 trees "
       "(each panel is a histogram of 10,000 sample means; red line = true mean).")
PINK = ("In a large Clarkia population, 30% of plants have pink flowers. The plot shows the sampling distributions of the "
        "proportion of pink plants in random samples of n = 10, 40 and 160 plants (red line = true proportion, 0.30).")
TROUT = ("A hatchery pond holds thousands of trout with a true mean length of 31.0 cm. A technician nets 25 fish at random, "
         "measures them, and returns them, and does this 1000 times. The plot shows the 1000 estimated means (red line = true mean).")
FAMILY = ("To estimate the mean number of children per family in a town, I asked 40 randomly chosen high-school students how many "
          "children are in their family (counting themselves), and averaged their answers. I repeated this 1000 times. The plot "
          "shows my 1000 estimates; the red line is the true mean number of children per family with children (2.56).")
SIZES = "A) n: 4\nB) n: 16\nC) n: 64"

# ---------- hw-01: estimates vs parameters
add("ch08-hw-01", 1, "matching", "estimates vs parameters, samples vs populations",
    "A survey team measures the wingspan of 120 randomly caught monarch butterflies and finds a mean of 9.6 cm.\n\n"
    "Fill in the blanks: 9.6 cm is an (1) ____ calculated from our (2) ____. We use it to learn about the true mean wingspan, a (3) ____ "
    "that describes the whole (4) ____ of monarchs.",
    EP, "1-A, 2-C, 3-B, 4-D",
    "We calculate estimates (like this mean of 9.6 cm) from the sample we measured. They're our best guess at parameters, the true values for the whole population.",
    "Parameters describe populations, estimates describe samples. 9.6 cm came from 120 butterflies, so it's an estimate.",
    "Which one did the team actually calculate?")
add("ch08-hw-01", 2, "matching", "estimates vs parameters, samples vs populations",
    "Classify each:\n\n1. The true proportion of all ballots in a state that went to candidate X\n2. The proportion of 1,000 polled voters who say they voted for X\n"
    "3. The 1,000 polled voters\n4. Every voter in the state",
    EP, "1-B, 2-A, 3-C, 4-D",
    "The true proportion over all ballots is a parameter of the population (every voter). The poll's proportion is an estimate calculated from the sample of 1,000.",
    "Swapping estimate and parameter is the classic mix-up: if it's calculated from a subset, it's an estimate.",
    "Which number would you only know if you counted everyone?")

# ---------- hw-02: sampling distribution definition
add("ch08-hw-02", 1, "MC", "sampling distribution",
    "Many labs each measure 30 randomly chosen zebrafish and report the mean swimming speed. A histogram of all those reported means shows the:",
    "A) Sampling distribution of the mean\nB) Population distribution of swimming speeds\nC) Standard deviation of swimming speed\nD) Sampling bias",
    "A",
    "Each lab produced one estimate (a mean of 30 fish). A distribution of estimates from many samples of the same size is a sampling distribution.",
    "B) The population distribution would show individual fish, not means of 30.\nC) The SD is a single number describing spread among individuals.\nD) Bias would be a shift of the means away from the truth, not the distribution itself.",
    "Is each value in the histogram an individual fish, or an estimate?")
add("ch08-hw-02", 2, "MC", "sampling distribution, population distribution",
    "Which of these is a sampling distribution?",
    "A) A histogram of the heights of all 600 trees in a forest plot\nB) A histogram of the means of 1,000 random samples of 10 trees each\nC) A histogram of the heights of 10 trees in one sample\nD) A bar chart of the number of trees of each species",
    "B",
    "A sampling distribution is a distribution of estimates (here, means), one from each of many samples of the same size.",
    "A) That's the population distribution of individual trees.\nC) That's the distribution of one sample.\nD) That summarizes a categorical variable for individuals.",
    "Look for a histogram of estimates, not of individuals.")

# ---------- hw-03: why the sampling distribution matters
add("ch08-hw-03", 1, "MC", "sampling distribution, uncertainty",
    "You measured one sample of 50 frogs and found a mean jump distance of 82 cm. Why should you care about the sampling distribution of the mean?",
    "A) It tells you how much your 82 cm might differ from the truth, because a different sample of 50 would give a different mean\nB) It tells you how far an individual frog can jump\nC) It makes your 82 cm exactly correct\nD) You can read it directly off your one sample of 50 frogs",
    "A",
    "The sampling distribution describes the other estimates you might have gotten. That's what lets us say how uncertain our one estimate is (SE, CI).",
    "B) Individual variation is the population distribution.\nC) Nothing removes sampling error.\nD) We can approximate it (bootstrap, formulas), but one sample doesn't show it directly.",
    "Think about the estimates you didn't get.")
add("ch08-hw-03", 2, "MC", "sampling distribution, uncertainty",
    "Two students each estimate the mean caffeine content of a coffee shop's lattes from separate random samples of 8 drinks. They get 142 mg and 155 mg. Which idea explains why they differ, and how much difference to expect?",
    "A) The sampling distribution: estimates vary from sample to sample, and its spread tells us how much\nB) One of them must have made a measurement mistake\nC) The population distribution changed between their visits\nD) Sampling bias: one sample must be non-random",
    "A",
    "Even with perfect measurements and random samples, different samples give different estimates. The sampling distribution describes that variation.",
    "B) A difference doesn't require a mistake; chance alone produces it.\nC) Nothing suggests the lattes changed.\nD) Random samples still differ by chance; that's sampling error, not bias.",
    "Would two perfectly random samples give the same mean?")

# ---------- hw-04: SD vs SE
add("ch08-hw-04", 1, "matching", "standard deviation, standard error",
    "Bill length in a population of finches has an SD of 1.2 mm. You take samples of 36 birds.\n\n"
    "1. Which describes how much individual finches differ from each other?\n2. Which describes how much the mean of 36 birds would vary from sample to sample?",
    "A) standard deviation\nB) standard error", "1-A, 2-B",
    "The SD (1.2 mm) is the spread of individuals. The SE is the spread of estimates: here about 1.2/√36 = 0.2 mm.",
    "Swapping them is the most common confusion in the chapter.",
    "Individuals → SD. Estimates → SE.")
add("ch08-hw-04", 2, "MC", "standard deviation, standard error",
    "A paper reports: \"mean body mass = 24.1 g (± 0.3 g, SE), n = 100 mice.\" What does the 0.3 g tell you?",
    "A) How far a typical sample mean of 100 mice would be from the true mean\nB) How far a typical mouse is from the mean\nC) The difference between the heaviest and lightest mouse\nD) The measurement error of the scale",
    "A",
    "A standard error describes the variability of an estimate (the mean of 100 mice). Individual mice vary much more: the SD here would be about 0.3 × √100 = 3 g.",
    "B) That's the SD.\nC) That's the range.\nD) Measurement error is a different thing; the SE comes from sampling.",
    "SE = spread of what?")

# ---------- hw-05: what reduces sampling error
add("ch08-hw-05", 1, "MC", "sampling error, sample size",
    "A lab estimates the mean seed mass of a weed from 15 randomly chosen plants. The estimate seems imprecise. What change would most reduce sampling error?",
    "A) Weigh the seeds on a more precise scale\nB) Measure 150 randomly chosen plants instead of 15\nC) Choose the 15 healthiest-looking plants\nD) Nothing; sampling error can't be reduced",
    "B",
    "Sampling error comes from which individuals happen to be in the sample. Larger random samples average over more individuals, so the SE shrinks (with √n).",
    "A) Reduces measurement error, a different source of error.\nC) Non-random selection adds bias.\nD) It can't be eliminated, but it can be reduced.",
    "What makes a sampling distribution narrower?")
add("ch08-hw-05", 2, "MC", "sampling error, sampling bias, sample size",
    "A researcher doubles her sample size but keeps sampling only from plants near the road. What happens?",
    "A) Sampling error decreases, but any bias from sampling only near the road remains\nB) Both sampling error and bias decrease\nC) Bias decreases, but sampling error stays the same\nD) Nothing changes",
    "A",
    "A larger sample makes the estimate more precise (less sampling error), but if roadside plants differ from the rest, the estimate is still systematically off. A bigger biased sample is precisely wrong.",
    "B) and C) Sample size doesn't fix bias.\nD) Precision does improve.",
    "Does sampling more from the same place fix who's being sampled?")

# ---------- hw-06: shape (new histograms)
SHAPE = "A) Unimodal & right skewed\nB) Unimodal & left skewed\nC) Unimodal & symmetric\nD) Bimodal"
add("ch08-hw-06", 1, "MC", "shape of distributions, histograms",
    "The histogram shows the number of pollinator visits to each of 400 plants. The distribution is:",
    SHAPE, "A",
    "One peak at 0–2 visits, with a long tail stretching to the right (a few plants get 10+ visits). That's unimodal and right skewed, common for counts.",
    "B) The long tail goes to the right, not the left.\nC) The two sides aren't mirror images.\nD) There's only one peak.",
    "Which side has the long tail?", "ch08-var-visits-hist.png")
add("ch08-hw-06", 2, "MC", "shape of distributions, histograms",
    "The histogram shows the heights of 600 trees. The distribution is:",
    SHAPE, "C",
    "One peak near 18 m, falling off about equally on both sides: unimodal and roughly symmetric.",
    "A) and B) Neither tail is clearly longer.\nD) There's one peak; small bumps are just noise.",
    "Would it look about the same flipped left to right?", "ch08-var-oak-hist.png")

# ---------- hw-07: size-biased sampling
add("ch08-hw-07", 1, "MC", "sampling bias, random sampling",
    "You want the mean length of time patients stay in a hospital. Which method gives an unbiased estimate?",
    "A) Pick a random sample of patients from the year's admission records and average their stays\nB) Visit the wards on a random day and average the stays of the patients who are there\nC) Ask the first 50 patients discharged in January\nD) Visit the wards on several random days and average the stays of the patients there",
    "A",
    "Every admission should have an equal chance of being picked. On any given day, the wards are full of long-stay patients (they're there for many days), so sampling whoever is present oversamples long stays: size-biased sampling.",
    "B) and D) Long stays are more likely to be 'caught' on a random day, so the mean is biased upward; more days doesn't fix it.\nC) January discharges may not represent the whole year.",
    "Does every patient have the same chance of being included?")
add("ch08-hw-07", 2, "MC", "sampling bias, random sampling",
    "To estimate the mean size of fish schools in a bay, a diver picks random fish and records the size of the school each fish belongs to. Why will this overestimate the mean school size?",
    "A) Fish in big schools are more likely to be picked, so big schools are oversampled\nB) The diver's sample is too small\nC) Fish in the same school are non-independent, which increases sampling error but doesn't shift the mean\nD) It won't; picking random fish is random sampling of schools",
    "A",
    "A school of 200 fish has 200 chances to be picked; a school of 5 has only 5. Sampling individuals gives schools probability proportional to their size, so the estimate is biased upward. Fix: sample schools, not fish.",
    "B) More fish chosen the same way gives the same bias.\nC) True that they're related, but the main problem is the shift in the mean.\nD) Random fish ≠ random schools.",
    "Does every school have the same chance of being included?")

# ---------- hw-08: minimizing non-independence
add("ch08-hw-08", 1, "MC", "non-independence, sampling design",
    "You want to estimate the average song rate of male wrens across a forest. Which sampling plan minimizes non-independence?",
    "A) Record 30 males, each from a different randomly chosen territory spread across the forest\nB) Record one male 30 times\nC) Record 30 males that all sing from the same clearing\nD) Record 30 males on the same morning in the same weather",
    "A",
    "Independent observations don't share anything that would make them more alike. Randomly chosen, spread-out territories avoid shared individuals, locations and conditions.",
    "B) Repeated measures of one bird tell you about that bird, not the population.\nC) Birds in one clearing share habitat and may influence each other.\nD) Shared weather and time of day can make songs alike.",
    "What could make two of your observations more similar than two random birds?")
add("ch08-hw-08", 2, "MC", "non-independence, sampling design",
    "A student measures leaf toughness on 60 leaves. Which design gives the most independent observations?",
    "A) 1 leaf from each of 60 randomly chosen plants\nB) 60 leaves from one plant\nC) 10 leaves from each of 6 plants\nD) 60 leaves from one branch of one plant",
    "A",
    "Leaves on the same plant share genes and growing conditions, so they're more alike than leaves from different plants. One leaf per plant gives 60 independent observations.",
    "B) and D) Effectively a sample size of one plant.\nC) Only 6 independent plants; the 10 leaves within each are related.",
    "How many truly independent units does each design give?")

# ---------- hw-09: half above the mean (unbiased)
add("ch08-hw-09", 1, "MC", "sampling distribution, sampling bias",
    OAK + "\n\nWhich sampling distribution has the greatest proportion of sample means above the true mean (18.0 m)?",
    SIZES + "\nD) They all have about half above the true mean", "D",
    "All three are centered on the true mean (random samples give unbiased estimates), so about half of the means fall above it whatever n is. Larger n changes the spread, not the center.",
    "A)–C) Sample size affects how far estimates stray, not which side they're on.",
    "Where is each histogram centered?", "ch08-var-oak-sampdist.png")
add("ch08-hw-09", 2, "MC", "sampling distribution, sampling bias",
    TROUT + "\n\nAbout what proportion of the 1000 estimates are above the true mean?",
    "A) About 0.10\nB) About 0.25\nC) About 0.50\nD) About 0.95", "C",
    "The estimates are centered on the true mean, as expected from random sampling (no bias), so about half fall above it (here 0.49).",
    "A), B) and D) Those would mean the estimates are shifted, i.e., biased.",
    "Where is the histogram centered relative to the red line?", "ch08-var-trout-unbiased.png")

# ---------- hw-10: bias doesn't depend on n
add("ch08-hw-10", 1, "MC", "sampling bias, sample size",
    OAK + "\n\nWhich statement about sampling bias is correct?",
    "A) Sampling bias is greatest with n = 4\nB) Sampling bias is greatest with n = 64\nC) There is no difference in sampling bias between them, only in sampling error", "C",
    "All three distributions are centered on the true mean, so none is biased. They differ only in spread (sampling error).",
    "A) and B) A small sample is noisier, not biased; a large one is more precise, not less biased.",
    "Bias moves the center; error widens the spread.", "ch08-var-oak-sampdist.png")
add("ch08-hw-10", 2, "MC", "sampling bias, sample size",
    PINK + "\n\nWhich statement about sampling bias is correct?",
    "A) Sampling bias is greatest with n = 10\nB) Sampling bias is greatest with n = 160\nC) None of these is biased; they differ in sampling error", "C",
    "Each distribution is centered on 0.30, so random samples of any size give unbiased estimates. The n = 10 distribution is just much wider.",
    "A) Wide is not the same as biased.\nB) Larger random samples don't add bias.",
    "Where is each distribution centered?", "ch08-var-pink-sampdist.png")

# ---------- hw-11: sampling error greatest at small n
add("ch08-hw-11", 1, "MC", "sampling error, sample size",
    OAK + "\n\nWhich statement about sampling error is correct?",
    "A) Sampling error is greatest with n = 4\nB) Sampling error is greatest with n = 64\nC) There is no difference in sampling error between them", "A",
    "The n = 4 distribution is the widest, so its sample means stray furthest from the truth by chance.",
    "B) n = 64 is the narrowest, with the least sampling error.\nC) The widths clearly differ.",
    "Which histogram is widest?", "ch08-var-oak-sampdist.png")
add("ch08-hw-11", 2, "MC", "sampling error, sample size",
    PINK + "\n\nIf you took one random sample of each size, which estimate is most likely to be far from 0.30?",
    "A) The n = 10 estimate\nB) The n = 40 estimate\nC) The n = 160 estimate\nD) All are equally likely to be far off", "A",
    "The n = 10 distribution spreads from 0 to 0.7, so a single small sample can easily miss by 0.2 or more. Larger samples cluster tightly around 0.30.",
    "B) and C) Their distributions are narrower.\nD) Spread depends strongly on n.",
    "Which distribution reaches furthest from the red line?", "ch08-var-pink-sampdist.png")

# ---------- hw-12: proportion beyond half an SD
add("ch08-hw-12", 1, "MC", "sampling error, standard error",
    OAK + "\n\nWhich sampling distribution has the greatest proportion of sample means more than half a population SD (2 m) from the true mean, i.e., below 16 m or above 20 m?",
    SIZES + "\nD) They all have about 62% more than 2 m away", "A",
    "Only the wide n = 4 distribution has much beyond 16 and 20 m (about 32% of means). For n = 16 it's about 5%, and for n = 64 almost none. 'About 62%' describes individual trees, not means.",
    "D) About 62% of individual trees are more than 0.5 SD from the mean; means are much less spread out.\nB) and C) Narrower distributions have less in their tails.",
    "Mark 16 and 20 m on each panel. Which has bars outside them?", "ch08-var-oak-sampdist.png",
    "Computed by simulation: 0.32, 0.05 and 0.00 for n = 4, 16, 64.")
add("ch08-hw-12", 2, "MC", "sampling error, standard error",
    PINK + "\n\nFor which sample size is a sample proportion of 0.45 or higher (half again as large as the truth) most likely?",
    "A) n = 10\nB) n = 40\nC) n = 160\nD) It's equally likely for all three", "A",
    "With n = 10, about 15% of samples give 0.45 or more (exact binomial). With n = 40 it's about 3%, and with n = 160 essentially never. Small samples are much more likely to be far off.",
    "B) and C) Larger samples rarely stray that far.\nD) The spread shrinks as n grows.",
    "Find 0.45 on the x-axis in each panel.", "ch08-var-pink-sampdist.png",
    "Exact binomial: P(p̂ ≥ 0.45) = 0.150, 0.032, 0.000.")

# ---------- hw-13: smallest SE
add("ch08-hw-13", 1, "MC", "standard error, sample size",
    OAK + "\n\nWhich sample size has the smallest standard error?",
    SIZES + "\nD) They all have the same standard error", "C",
    "The SE is the SD of the sampling distribution; n = 64 is the narrowest. SE ≈ SD/√n: 4/√64 = 0.5 m vs 4/√4 = 2 m.",
    "A) n = 4 has the largest SE.\nB) Narrower than n = 4 but wider than n = 64.\nD) The SE shrinks as n grows.",
    "Narrowest histogram = smallest SE.", "ch08-var-oak-sampdist.png")
add("ch08-hw-13", 2, "MC", "standard error, sample size",
    "The SD of seed mass in a population is 0.8 mg. Which sample size gives a standard error of the mean of about 0.1 mg?",
    "A) n = 8\nB) n = 16\nC) n = 64\nD) n = 800", "C",
    "SE = SD/√n. For SE = 0.1, √n = 0.8/0.1 = 8, so n = 64. To halve the SE you need four times the sample size.",
    "A) and B) Too small: SE ≈ 0.28 and 0.2 mg.\nD) Gives SE ≈ 0.028 mg, much smaller than needed.",
    "Set 0.8/√n = 0.1 and solve for n.")

# ---------- gquiz-01: smaller samples → more sampling error
add("ch08-gquiz-01", 1, "MC", "sampling error, sample size",
    "To save time, a field crew measures 5 randomly chosen lizards per site instead of 25. This practice:",
    "A) Increases sampling bias\nB) Increases sampling error\nC) Has no real impact on the estimates", "B",
    "Smaller random samples give noisier estimates (larger SE), but each sample is still random, so the estimate isn't systematically shifted.",
    "A) Bias comes from how we sample, not how many.\nC) Fewer lizards means less precise means.",
    "Does sample size change the center or the spread of the sampling distribution?")
add("ch08-gquiz-01", 2, "MC", "sampling error, sample size",
    "Two students estimate the proportion of red crayons in the same bin. Ana draws 5 crayons at random; Ben draws 50 at random. Whose estimate is more likely to be far from the true proportion, and why?",
    "A) Ana's, because small samples have more sampling error\nB) Ben's, because more crayons means more chances for mistakes\nC) Ana's, because small samples are biased\nD) Neither; both are random", "A",
    "Both samples are random, so neither is biased. But Ana's 5 crayons can easily be all red or all blue by chance; Ben's 50 average out more of that luck.",
    "B) More data reduces, not increases, chance error.\nC) Small random samples are noisy, not biased.\nD) Both are random, but they differ in precision.",
    "With 5 crayons, how likely is a very lopsided sample?")

# ---------- gquiz-02: non-independence of reports
add("ch08-gquiz-02", 1, "MC", "non-independence",
    "For a class survey of sleep hours, a teacher asks only one person per household to respond. Why?",
    "A) To minimize sampling bias\nB) To minimize sampling error\nC) To minimize non-independence\nD) To reduce the number of responses", "C",
    "People in the same household share routines (and noise!), so their sleep is more alike. Counting several per household would treat related observations as independent.",
    "A) It doesn't systematically shift the estimate.\nB) Fewer responses would increase, not reduce, sampling error.\nD) That's a side effect, not the reason.",
    "Would two people from the same household be more alike than two random students?")
add("ch08-gquiz-02", 2, "MC", "non-independence",
    "In a class activity, each table drew one sample of 10 crayons, but everyone at the table entered that same sample into the form, so 30 entries came from 6 samples. What's the problem?",
    "A) The 30 entries aren't independent: the class really has only 6 independent samples\nB) The estimates are biased toward red\nC) There's no problem; more entries is always better\nD) The sample size per draw was too small", "A",
    "Duplicate entries of one draw aren't new information. Treating them as 30 independent samples overstates how much data we have, making results look more precise than they are.",
    "B) Duplicating samples doesn't shift the center.\nC) More entries only help if they're independent.\nD) That's a separate issue.",
    "How many independent draws were there?")

# ---------- gquiz-04: estimate vs parameter
add("ch08-gquiz-04", 1, "matching", "estimates vs parameters",
    "A lake has thousands of perch. You catch 25 at random and 8 have parasites.\n\n8/25 = 0.32 is an (1) ____ of the (2) ____, the true proportion of all perch in the lake with parasites.",
    "A) estimate\nB) parameter", "1-A, 2-B",
    "0.32 comes from the sample of 25, so it's an estimate. The true proportion for all perch in the lake is the parameter.",
    "Parameters describe populations; estimates come from samples.",
    "Which one did you calculate?")
add("ch08-gquiz-04", 2, "MC", "estimates vs parameters",
    "Which of these is a parameter?",
    "A) The mean height of all 1,204 students enrolled in a school\nB) The mean height of 30 randomly chosen students from that school\nC) The SD of heights among those 30 students\nD) The proportion of the 30 students taller than 170 cm", "A",
    "A parameter describes the whole population. If the population is all 1,204 students, their true mean height is a parameter. Everything calculated from the 30 is an estimate.",
    "B), C) and D) All are calculated from a sample, so they're estimates.",
    "Which number describes everyone?")

# ---------- gquiz-05: sampling distribution
add("ch08-gquiz-05", 1, "MC", "sampling distribution",
    "Each of 200 students flips a coin 20 times and reports the proportion of heads. The distribution of those 200 proportions approximates the:",
    "A) sampling distribution of the proportion\nB) population distribution\nC) standard error\nD) sampling bias", "A",
    "Many samples of the same size (20 flips) → many estimates → their distribution approximates the sampling distribution.",
    "B) The population distribution would be the outcomes of individual flips.\nC) The SE is the SD of this distribution, not the distribution itself.\nD) Bias would be a shift of its center away from the truth.",
    "Distribution of estimates.")
add("ch08-gquiz-05", 2, "MC", "sampling distribution, standard error",
    "If you repeated the crayon activity (10 crayons, count the red ones) an enormous number of times and plotted the proportion red each time, what would the SD of that histogram be?",
    "A) The standard error of the proportion red for samples of 10\nB) The standard deviation of crayon colors in the bin\nC) The sampling bias\nD) The true proportion of red crayons", "A",
    "The histogram is the sampling distribution, and the SD of a sampling distribution is the standard error.",
    "B) That describes individual crayons, not estimates.\nC) Bias is about the center, not the spread.\nD) The true proportion is where the histogram is centered.",
    "SE = the SD of what?")

# ---------- gquiz-07: how to find an SE
add("ch08-gquiz-07", 1, "MC", "standard error, sampling distribution",
    "A biologist wants the standard error of mean beak length for samples of 15 finches, and can catch as many finches as she likes. How could she find it directly?",
    "A) Catch many separate samples of 15 finches, compute the mean of each, and take the SD of those means\nB) Catch one sample of 15 and compute the SD of beak lengths\nC) Catch one sample of 150 and compute its mean\nD) Measure every finch on the island", "A",
    "The SE is the SD of the sampling distribution. Building it means many samples of the same size, one mean each, then the SD of those means.",
    "B) That's the SD among individuals (though SD/√15 would approximate the SE).\nC) One mean, from a different n, says nothing about variation among means.\nD) That gives the parameter, with no sampling error to describe.",
    "SE = SD of many what?")
add("ch08-gquiz-07", 2, "MC", "standard error, sampling distribution",
    "You have one sample of 40 plants and can't go back for more. What's the best way to estimate the standard error of the mean?",
    "A) Use the sample SD divided by √40 (or bootstrap the sample)\nB) Use the sample SD itself\nC) It's impossible without more samples\nD) Use the sample mean divided by √40", "A",
    "With only one sample, we approximate the sampling distribution: either with the formula SE ≈ SD/√n or by resampling the data (bootstrap).",
    "B) The SD describes individuals, not means.\nC) We can estimate it; we just can't observe it directly.\nD) The mean isn't a measure of spread.",
    "Means vary less than individuals by how much?")

# ---------- book-01: SD vs SE definitions
add("ch08-book-01", 1, "matching", "standard deviation, standard error",
    "1. If you measured more and more individuals, which would settle near a fixed value (not shrink)?\n2. Which would keep getting smaller as you added more individuals to your sample?",
    "A) standard error of the mean\nB) standard deviation", "1-B, 2-A",
    "The SD estimates a property of the population (how variable individuals are), so it settles down. The SE ≈ SD/√n keeps shrinking as n grows.",
    "Bigger samples make the SD more precise, not smaller.",
    "Would individuals become more similar if you measured more of them?")
add("ch08-book-01", 2, "MC", "standard deviation, standard error",
    "Which statement is correct?",
    "A) The SE describes how much sample means vary; the SD describes how much individuals vary\nB) The SE and SD are two names for the same thing\nC) The SE is always larger than the SD\nD) The SD shrinks as sample size increases; the SE doesn't", "A",
    "SD: spread among individuals. SE: spread among estimates (for a given n). Since SE ≈ SD/√n, the SE is smaller than the SD whenever n > 1.",
    "B) They measure different things.\nC) It's smaller, not larger.\nD) That's backwards.",
    "Individuals or estimates?")

# ---------- book-02: population vs sampling distribution, shape
add("ch08-book-02", 1, "select-all", "shape of distributions, population distribution",
    "The histogram shows the day of the year that fruit ripened on each of 5,000 plants in a population (all of them were measured). Which statements are correct? (Select all that apply.)",
    "A) The distribution is unimodal\nB) The distribution is bimodal\nC) The distribution is left skewed\nD) The distribution is right skewed\nE) The histogram displays the population distribution\nF) The histogram displays a sampling distribution", "A, C, E",
    "One peak near day 114 with a long tail toward earlier days: unimodal and left skewed (so the mean, 108, is below the median, 110). It shows every individual plant, so it's the population distribution.",
    "B) One peak.\nD) The long tail is on the left.\nF) A sampling distribution would show estimates from many samples, not individual plants.",
    "Which way does the long tail point? And is each value a plant or an estimate?", "ch08-var-ripen-pop.png")
add("ch08-book-02", 2, "select-all", "sampling distribution, shape of distributions",
    "From the same population of 5,000 plants (whose ripening days are left skewed), I drew 1,000 random samples of 40 plants and recorded the mean ripening day of each. The histogram shows those 1,000 means. Which statements are correct? (Select all that apply.)",
    "A) The distribution is unimodal and roughly symmetric\nB) The distribution is strongly left skewed, like the population\nC) The histogram displays a sampling distribution\nD) The histogram displays the population distribution\nE) It is much narrower than the population distribution", "A, C, E",
    "Means of 40 plants smooth out the skew of individuals, so the sampling distribution is roughly symmetric (a preview of the central limit theorem). It's a distribution of estimates, and it's far narrower: means range from about 104 to 112, while individuals range from about 55 to 120.",
    "B) Averaging removes most of the skew.\nD) Each value is a mean of 40 plants, not one plant.",
    "Is each value one plant, or a mean of 40?", "ch08-var-ripen-means.png")

# ---------- book-03: bias vs error in a plot
add("ch08-book-03", 1, "MC", "sampling bias",
    FAMILY + "\n\nThe difference between the true mean and my estimates is most likely explained by:",
    "A) Sampling bias\nB) Non-independence\nC) Sampling error\nD) Too few repetitions", "A",
    "Nearly all 1000 estimates are above 2.56: a systematic shift. Families with more children have more students to be asked, so big families are oversampled (size-biased sampling). Sampling error would scatter estimates on both sides of the truth.",
    "B) Non-independence would widen the spread, not shift it.\nC) Chance would put estimates on both sides of the line.\nD) More repetitions would show the same shift.",
    "Are the estimates scattered around the truth, or all off in one direction?", "ch08-var-family-biased.png",
    "Simulated: true mean 2.56; estimates average 3.16.")
add("ch08-book-03", 2, "MC", "sampling error, sampling bias",
    TROUT + "\n\nThe individual estimates range from about 27 to 34.5 cm. This spread is best explained by:",
    "A) Sampling error\nB) Sampling bias\nC) Non-independence\nD) Measurement error", "A",
    "The estimates are scattered evenly on both sides of the true mean, as expected from chance differences among random samples. There's no systematic shift, so no bias.",
    "B) Bias would shift the whole histogram away from the red line.\nC) Nothing suggests related fish.\nD) Even perfect measurements would give this spread, because each net catches different fish.",
    "Is the histogram centered on the red line?", "ch08-var-trout-unbiased.png")

# ---------- book-04: size-biased sampling, fix
add("ch08-book-04", 1, "MC", "sampling bias, random sampling",
    "I estimated the mean number of children per family by surveying random high-school students about their own families. My estimate (3.2) was well above the true mean (2.6). Why, and how could I fix it?",
    "A) Families with more children have more students who could be picked, so big families were oversampled. Fix: randomly sample families (e.g., households), not students\nB) My sample was too small. Fix: survey more students the same way\nC) Students are bad at counting siblings. Fix: check birth records\nD) Bad luck. Fix: repeat the survey",
    "A",
    "Sampling students gives each family a chance proportional to its number of children: size-biased sampling, like random nucleotides oversampling long genes. Each family needs an equal chance.",
    "B) A bigger biased sample is still biased.\nC) Even perfect counting gives the same bias.\nD) Repeating gives the same systematic error.",
    "Does every family have the same chance of being in the sample?")
add("ch08-book-04", 2, "MC", "sampling bias, random sampling",
    "To estimate mean group size of wild horses, researchers flew over the range and photographed a random spot, recording the size of the group closest to that spot. Estimates were consistently larger than the true mean group size. Why?",
    "A) Large groups cover more ground, so they're more likely to be nearest a random spot: big groups are oversampled\nB) Horses move, so photos are blurry\nC) The flights were too short\nD) The researchers made arithmetic errors",
    "A",
    "Like random nucleotides landing in long genes, random spots are more likely to land near big groups. That's size-biased sampling. Fix: sample groups with equal probability, e.g., list all groups and pick at random.",
    "B), C) and D) None of these would push estimates consistently upward.",
    "Which groups are easiest to 'hit' with a random spot?")

# ---------- book-05: means less spread than individuals
add("ch08-book-05", 1, "MC", "sampling distribution, population distribution",
    "Individual oak heights range from about 6 to 30 m, but means of random samples of 64 oaks all fall between about 16.5 and 19.5 m. Why is the range of the means so much smaller?",
    "A) Averaging many trees cancels out extremes, so estimates vary much less than individuals\nB) Sampling bias\nC) Non-independence\nD) The samples of 64 must have excluded the tallest and shortest trees",
    "A",
    "One very tall tree in a sample of 64 is diluted by 63 others. That's why SE = SD/√n is much smaller than the SD.",
    "B) Bias would shift the center, not narrow the spread.\nC) Non-independence would widen, not narrow.\nD) Random samples include extreme trees; they just don't dominate the mean.",
    "What happens to one extreme value when averaged with 63 others?")
add("ch08-book-05", 2, "MC", "sampling distribution, population distribution",
    "Which will be more spread out?",
    "A) Heights of 1,000 individual students\nB) Mean heights of 1,000 random samples of 25 students\nC) They'll be equally spread out\nD) It depends on whether the population is skewed",
    "A",
    "Individuals vary the most. Means of 25 vary about 1/√25 = 1/5 as much (SE = SD/√n), whatever the shape of the population.",
    "B) Means are less variable than individuals.\nC) and D) Averaging always reduces spread.",
    "Do means vary more or less than individuals?")

# ---------- book-06: panels differ by sampling error; smallest SE
add("ch08-book-06", 1, "MC", "sampling error, standard error, sample size",
    PINK + "\n\nWhat explains the difference between the panels, and which n has the smallest standard error?",
    "A) Less sampling error in larger samples; n = 160 has the smallest SE\nB) Less sampling bias in larger samples; n = 160 has the smallest SE\nC) Less non-independence in larger samples; n = 10 has the smallest SE\nD) Less sampling error in larger samples; they all have about the same SE",
    "A",
    "All three are centered on 0.30 (no bias) and get narrower as n increases. SE = √(0.3 × 0.7 / n): about 0.145, 0.072 and 0.036.",
    "B) None is biased.\nC) Sample size doesn't change independence; n = 10 has the largest SE.\nD) The widths clearly differ.",
    "Center = bias; width = sampling error / SE.", "ch08-var-pink-sampdist.png")
add("ch08-book-06", 2, "MC", "sampling error, standard error, sample size",
    OAK + "\n\nGoing from n = 16 to n = 64 (four times as many trees), what happens to the standard error?",
    "A) It halves (from about 1 m to about 0.5 m)\nB) It shrinks to a quarter\nC) It stays the same\nD) It doubles",
    "A",
    "SE = SD/√n. Quadrupling n doubles √n, so the SE halves: 4/√16 = 1 m, 4/√64 = 0.5 m. You can see the n = 64 panel is about half as wide as n = 16.",
    "B) That would need 16 times the sample.\nC) The SE depends on n.\nD) Larger samples reduce the SE.",
    "SE = SD / √n. What happens to √n when n quadruples?", "ch08-var-oak-sampdist.png")

# ---------- book-07: proportions above thresholds
add("ch08-book-07", 1, "matching", "sampling distribution, standard error",
    OAK + "\n\nApproximately what proportion of sample means are:\n\n1. greater than 18 m, for n = 4?\n2. greater than 18 m, for n = 64?\n3. greater than 20 m, for n = 4?\n4. greater than 20 m, for n = 64?",
    "A) way less than 0.01\nB) about 0.16\nC) about 0.50", "1-C, 2-C, 3-B, 4-A",
    "Both are centered on 18 m, so about half are above it regardless of n. Only the wide n = 4 distribution reaches 20 m often (about 16%); for n = 64 a mean of 20 m is 4 SEs away and essentially never happens.",
    "Being centered on the truth doesn't depend on n; reaching far from it does.",
    "Find the red line, then find 20 m in each panel.", "ch08-var-oak-sampdist.png",
    "Simulated: P(>18) = 0.50, 0.50; P(>20) = 0.16, 0.00.")
add("ch08-book-07", 2, "MC", "sampling distribution, standard error",
    TROUT + "\n\nIf the technician had netted 100 fish each time instead of 25, how would the histogram change?",
    "A) Still centered on 31 cm, but about half as wide\nB) Shifted closer to 31 cm\nC) Centered on 31 cm and the same width\nD) About a quarter as wide",
    "A",
    "Random samples stay centered on the truth. The SE scales with 1/√n, so 4 times the fish makes it 1/2 as wide.",
    "B) It's already centered on 31 cm.\nC) Larger samples reduce the spread.\nD) That would take 16 times the fish.",
    "SE = SD / √n.", "ch08-var-trout-unbiased.png")

# ---------- book-08: no SE for a census
add("ch08-book-08", 1, "MC", "standard error, parameters vs estimates, population",
    "A national park counts every one of its 412 bighorn sheep from the air and finds the mean group size is 7.3. What is the standard error of this mean?",
    "A) There is none: every sheep in the population was counted, so 7.3 is the parameter\nB) The SD of group sizes\nC) The SD of group sizes divided by √412\nD) 7.3 / √412",
    "A",
    "An SE describes how much an estimate would vary across samples. A complete census has no sampling, so no sampling error and no SE (though counting mistakes are still possible).",
    "B) That's the spread among groups.\nC) That would apply if these 412 were a sample from a larger population.\nD) The wrong formula, and it doesn't apply anyway.",
    "Is this a sample or the whole population?")
add("ch08-book-08", 2, "MC", "standard error, parameters vs estimates, population",
    "A teacher calculates the mean exam score of all 28 students in her class: 81.5. She only cares about this class. Should she report a standard error?",
    "A) No: she measured the whole population she cares about, so 81.5 is the parameter\nB) Yes: every mean needs a standard error\nC) Yes, because 28 is a small number\nD) Only if the scores are normally distributed",
    "A",
    "Whether something is a population depends on the question. If the class is the population of interest, the mean is known exactly. If she wanted to generalize to future classes, then this class would be a sample and an SE would make sense.",
    "B) SEs describe sampling error; no sampling, no SE.\nC) Small populations are still populations.\nD) Shape doesn't matter here.",
    "Is she sampling, or did she measure everyone she cares about?")


if __name__ == "__main__":
    P = "question_bank.csv"
    rows = list(csv.DictReader(open(P, encoding="utf-8")))
    H = list(rows[0].keys())
    if "variant_of" not in H:
        H.append("variant_of")
        for r in rows:
            r["variant_of"] = ""
    have = {r["id"] for r in rows}
    new = [v for v in V if v["id"] not in have]
    rows += new
    w = csv.DictWriter(open(P, "w", newline="", encoding="utf-8"), fieldnames=H)
    w.writeheader(); w.writerows(rows)
    print(len(V), "variants;", len(new), "added; total rows", len(rows))
