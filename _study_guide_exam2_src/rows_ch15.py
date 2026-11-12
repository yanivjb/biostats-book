TEMP = "To check the folk value of 98.6 °F for human body temperature, researchers measured 25 random people: mean 98.524 °F, sample variance 0.4594."
CHAT = """To test whether a chatbot tutor helps students study, five pairs of students matched on their first exam scores were split so one got the tutor and the other did not.

• Mean difference in exam scores (chatbot minus control): 5.25
• Variance of the differences: 13.716
• t = 3.170"""
HYENA = """To ask whether hyena "laughter" signals social rank, Mathevon et al. (2010) measured giggling in nine natural pairs of one dominant and one subordinate hyena (differences are subordinate minus dominant):

pair | dominant | subordinate | diff
1 | 0.384 | 0.507 | 0.123
2 | 0.386 | 0.569 | 0.183
3 | 0.252 | 0.235 | -0.017
4 | 0.226 | 0.415 | 0.189
5 | 0.323 | 0.436 | 0.113
6 | 0.287 | 0.451 | 0.164
7 | 0.303 | 0.399 | 0.096
8 | 0.317 | 0.220 | -0.097
9 | 0.277 | 0.338 | 0.061

Mean difference = 0.0906; SD of the differences = 0.0954."""

ROWS = [
# ---------------- Quiz: t distribution (Oct 26) ----------------
dict(id="ch15-quiz-01", source="t distribution quiz (2026), Q1", topics="t statistic, one-sample t-test", type="numeric",
question=TEMP + "\n\nTesting the null hypothesis that mean body temperature is 98.6 °F, what is the numerator of t (the estimate minus its null value)?",
answer="-0.076", explanation="Numerator = estimate - null value = 98.524 - 98.6 = -0.076 °F.",
why_wrong="Common mistake: subtracting in the other order (+0.076). Either sign gives the same two-tailed test, but by convention it's estimate minus null.",
hint="t = (estimate - null value) / SE."),

dict(id="ch15-quiz-02", source="t distribution quiz (2026), Q2", topics="standard deviation, variance", type="numeric",
question=TEMP + "\n\nWhat is the sample standard deviation?",
answer="0.678", explanation="SD = √variance = √0.4594 = 0.678 °F.",
why_wrong="Common mistake: using the variance (0.4594) as the SD.",
hint="How are the variance and the SD related?"),

dict(id="ch15-quiz-03", source="t distribution quiz (2026), Q3", topics="effect size, Cohen's d", type="MC",
question=TEMP + "\n\nThe mean is 0.076 °F below 98.6, and the SD is 0.678 °F. What is Cohen's d, and how big is this effect?",
options="""A) d ≈ 0.11, a small effect (< 0.5)
B) d ≈ 0.56, a medium effect (0.5 to 0.8)
C) d ≈ 8.9, a large effect (> 0.8)
D) d ≈ 0.076, a small effect""",
answer="A",
explanation="Cohen's d = |difference| / SD = 0.076 / 0.678 = 0.11, a small effect: the average differs from 98.6 by about a tenth of an SD.",
why_wrong="""B) 0.56 is the t value (difference / SE), not d.
C) That's SD / difference, upside down.
D) 0.076 is the raw difference, not standardized.""",
hint="Cohen's d divides by the standard deviation, not the standard error."),

dict(id="ch15-quiz-04", source="t distribution quiz (2026), Q4", topics="standard error", type="numeric",
question=TEMP + "\n\nThe sample SD is 0.678 °F. What is the standard error of the mean?",
answer="0.136", explanation="SE = SD / √n = 0.678 / √25 = 0.678 / 5 = 0.136 °F.",
why_wrong="Common mistakes: dividing by n (0.027), or using the variance (0.092).",
hint="SE = SD / √n."),

dict(id="ch15-quiz-05", source="t distribution quiz (2026), Q5", topics="t statistic", type="numeric",
question=TEMP + "\n\nThe estimate minus the null value is -0.076, and the standard error is 0.136. What is t?",
answer="-0.56", explanation="t = -0.076 / 0.136 = -0.56. The sample mean is about half a standard error below 98.6.",
why_wrong="Common mistake: dividing by the SD (gives -0.11, which is Cohen's d).",
hint="t = (estimate - null) / SE."),

dict(id="ch15-quiz-06", source="t distribution quiz (2026), Q6-7", topics="t statistic, NHST", type="MC",
question=TEMP + "\n\nt = -0.56 (24 df). Before calculating a p-value, what do you expect to do with the null hypothesis at α = 0.05?",
options="""A) Obviously reject the null
B) Obviously fail to reject the null
C) Uncertain: it's on the border, so I should look it up""",
answer="B",
explanation="To reject at α = 0.05 we need |t| of roughly 2 or more. A t of -0.56 means the sample mean is only about half a standard error from 98.6, which happens all the time by chance. (The p-value is 0.58.)",
why_wrong="""A) t is far too small to reject.
C) Borderline would be |t| near 2.""",
hint="Roughly how many standard errors away does an estimate need to be to reject at α = 0.05?"),

dict(id="ch15-quiz-07", source="t distribution quiz (2026), Q8-9", topics="NHST, interpreting results", type="MC",
question=TEMP + "\n\nThe two-tailed p-value is 0.58. At α = 0.05, what do we do and conclude?",
options="""A) Reject the null; mean body temperature is not 98.6 °F
B) Fail to reject the null; mean body temperature is exactly 98.6 °F
C) Fail to reject the null; we act as if it's true, but could be wrong
D) Accept the null; the null has a greater than 0.5 chance of being true""",
answer="C",
explanation="p = 0.58 > 0.05, so we fail to reject. That doesn't prove the mean is exactly 98.6; it means our data are consistent with it. A p-value also isn't the probability the null is true.",
why_wrong="""A) p is much bigger than 0.05.
B) Failing to reject isn't proof the null is true.
D) We never 'accept' the null, and p isn't the probability the null is true.""",
hint="Compare p to α. Then ask what a non-significant result can and can't tell you."),

dict(id="ch15-quiz-08", source="t distribution quiz (2026), Q11", topics="p-values, R", type="MC",
question="For the body temperature data (t = -0.56, n = 25, so 24 df), which R code gives the two-tailed p-value?",
options="""A) 2 * pt(0.56, df = 24, lower.tail = FALSE)
B) pt(0.56, df = 24, lower.tail = FALSE)
C) 2 * pt(0.56, df = 25)
D) qt(0.56, df = 24)""",
answer="A",
explanation="pt(..., lower.tail = FALSE) gives the area above |t| in one tail; doubling it gives a two-tailed p-value. The df for a one-sample t-test are n - 1 = 24.",
why_wrong="""B) This is one-tailed.
C) Uses the wrong df, and the lower tail of a positive value (that's about 0.71 before doubling).
D) qt() returns a quantile, not a probability.""",
hint="Two tails, upper area, n - 1 degrees of freedom."),

dict(id="ch15-quiz-09", source="t distribution quiz (2026), Q12-13", topics="confidence intervals, critical t", type="MC",
question=TEMP + "\n\nThe standard error is 0.136 and the critical t value for 24 df at α = 0.05 is 2.064. What is the 95% confidence interval for mean body temperature?",
options="""A) 98.52 ± 0.136, i.e. (98.39, 98.66)
B) 98.52 ± 0.28, i.e. (98.24, 98.80)
C) 98.52 ± 1.40, i.e. (97.12, 99.92)
D) 98.6 ± 0.28, i.e. (98.32, 98.88)""",
answer="B",
explanation="95% CI = estimate ± critical t × SE = 98.524 ± 2.064 × 0.136 = 98.524 ± 0.28, or (98.24, 98.80). The interval includes 98.6, matching our failure to reject.",
why_wrong="""A) Forgets to multiply the SE by the critical t.
C) Uses the SD (0.678) instead of the SE.
D) Centers the interval on the null value instead of the estimate.""",
hint="CI = estimate ± critical t × SE."),

dict(id="ch15-quiz-10", source="t distribution quiz (2026), Q14", topics="writing results", type="open", include="no",
question=TEMP + "\n\nThe SD was 0.678 °F (Cohen's d = 0.11), t = -0.56 with 24 df, p = 0.58, and the 95% CI is (98.24, 98.80). Write up these results in a brief paragraph.",
answer="Model answer: The mean body temperature of 25 people was 98.52 °F (SD = 0.68; 95% CI: 98.24 to 98.80 °F). This is not significantly different from the commonly cited 98.6 °F (t = -0.56, df = 24, p = 0.58), and the difference is small (Cohen's d = 0.11). Our data are consistent with a mean of 98.6 °F, though values from about 98.2 to 98.8 °F are also plausible.",
explanation="A good write-up gives the estimate with uncertainty (CI), the test (t, df, p), an effect size, and a plain-language conclusion that doesn't claim the null is proven.",
hint="Start with the estimate and its CI, then the test, then what it means."),

# ---------------- Homework ----------------
dict(id="ch15-hw-01", source="t distribution homework, Q1", topics="t vs z", type="MC",
question="When would you use a t distribution instead of a z (standard normal) distribution?",
options="""A) When you are comparing two proportions
B) When the population standard deviation is unknown and must be estimated from the sample
C) When the data are not approximately normal
D) When the sample size is very large
E) When the mean is not zero and/or the standard deviation is not one""",
answer="B",
explanation="The t accounts for the extra uncertainty from estimating the SD from the sample. If we knew σ, we'd use z.",
why_wrong="""A) Proportions are a different problem.
C) The t still assumes (roughly) normal data or sampling distributions.
D) With very large samples, t and z are nearly identical, so it barely matters.
E) Any normal can be standardized; that's what Z scores do.""",
hint="What does the t do that the z doesn't?"),

dict(id="ch15-hw-02", source="t distribution homework, Q2", topics="t-test assumptions, central limit theorem", type="MC",
question="A researcher runs a t-test on 100 measurements of flower height, which are slightly right-skewed. Which statement best describes whether the test is appropriate?",
options="""A) It's inappropriate: t-tests need symmetric data, even for large samples
B) It's inappropriate: t-tests strictly require perfectly normal data
C) It's probably fine: the t distribution automatically corrects for skew
D) It's probably fine: with n = 100, the CLT makes t-tests robust to mild skew""",
answer="D",
explanation="With 100 observations, the sampling distribution of the mean is close to normal even if the data are a bit skewed, so the t-test works well.",
why_wrong="""A) and B) t-tests are robust to mild departures from normality, especially with large samples.
C) The t doesn't correct for skew; the CLT is what helps.""",
hint="Which theorem helps when n is large?"),

dict(id="ch15-hw-03", source="t distribution homework, Q3", topics="t vs z", type="MC",
question="Your advisor tells you to just use a z-test instead of a t-test, claiming they are practically the same. When would this substitution make little practical difference?",
options="""A) When the sample is large, so the t and z distributions are nearly identical
B) When your data contain no outliers
C) When you have more than one predictor variable
D) When the sample mean equals the population mean""",
answer="A",
explanation="As degrees of freedom grow, the t distribution's tails shrink toward the z's. With large samples the critical values are nearly the same (e.g. 1.98 vs 1.96 at 100 df).",
why_wrong="""B) Outliers matter for both tests equally.
C) The number of predictors doesn't make t and z alike.
D) The estimate's value doesn't change the shape of the distribution.""",
hint="When does the t's fatter tails stop mattering?"),

dict(id="ch15-hw-04", source="t distribution homework, Q4", topics="null and alternative hypotheses, paired t-test", type="matching",
question=CHAT + "\n\nFor a two-tailed test, match each hypothesis to its statement:\n\n1. Null hypothesis\n2. Alternative hypothesis",
options="""A) The mean difference in exam scores (chatbot - control) equals 0
B) The mean difference in exam scores (chatbot - control) does not equal 0
C) The mean difference in exam scores (chatbot - control) is greater than 0
D) Chatbots help you learn""",
answer="1-A, 2-B",
explanation="The null is a specific value (no difference). A two-tailed alternative is 'not equal to', allowing a difference in either direction.",
why_wrong="""C) That's a one-tailed alternative.
D) That's a biological hypothesis, not a statistical one.""",
hint="Two-tailed means either direction counts."),

dict(id="ch15-hw-05", source="t distribution homework, Q5", topics="effect size, Cohen's d", type="MC",
question=CHAT + "\n\nWhat is the best measure of the effect size?",
options="""A) The mean difference between chatbot and control, 5.25
B) The p-value
C) Cohen's d, 1.42
D) The t value, 3.170""",
answer="C",
explanation="Cohen's d = mean difference / SD = 5.25 / √13.716 = 5.25 / 3.70 = 1.42. It puts the difference on a standard scale, independent of sample size.",
why_wrong="""A) The raw difference is useful but depends on the units (exam points).
B) A p-value depends on sample size and isn't an effect size.
D) t also grows with sample size; it measures evidence, not effect size.""",
hint="Which measure doesn't depend on sample size?"),

dict(id="ch15-hw-06", source="t distribution homework, Q6", topics="standard error, paired t-test", type="numeric",
question=CHAT + "\n\nWhat is the standard error of the mean difference?",
answer="1.656", explanation="SD = √13.716 = 3.704. SE = SD / √n = 3.704 / √5 = 1.656. (Check: 5.25 / 1.656 = 3.17 = t.)",
why_wrong="Common mistakes: using the variance instead of the SD, or dividing by n instead of √n.",
hint="Start by turning the variance into an SD."),

dict(id="ch15-hw-07", source="t distribution homework, Q7", topics="p-values, paired t-test", type="numeric",
question=CHAT + """

In R:
2 * pt(3.170, df = 4, lower.tail = FALSE)
[1] 0.0339

What is the two-tailed p-value? Report it to three decimals.""",
answer="0.034", explanation="With five pairs, df = 5 - 1 = 4. The two-tailed p-value is 0.034.",
why_wrong="Common mistake: halving or doubling again. The code already doubles the one-tailed area.",
hint="The R output gives it directly; make sure you understand why df = 4."),

dict(id="ch15-hw-08", source="t distribution homework, Q8-9", topics="NHST, interpreting results", type="MC",
question=CHAT + "\n\nThe two-tailed p-value is 0.034. At α = 0.05, what do we do to the null, and what does this mean?",
options="""A) Reject it; this proves the null is false
B) Reject it; act as if it's false, but may be wrong
C) Fail to reject it; so the null must be true
D) Accept it; so the alternative must be false""",
answer="B",
explanation="0.034 < 0.05, so we reject the null. That doesn't prove the null false: with only five pairs, we could be making a type I error.",
why_wrong="""A) Rejecting is not proof.
C) and D) p < α means we reject; and we never 'accept' a null.""",
hint="Compare p to α. Can a p-value prove anything for certain?"),

dict(id="ch15-hw-09", source="t distribution homework, Q10", topics="confidence intervals, critical t", type="MC",
question=CHAT + "\n\nThe SE is 1.656, and the critical t value for 4 df at α = 0.05 is 2.776. What is the 95% confidence interval for the mean difference?",
options="""A) (1.50, 9.00)
B) (1.71, 8.79)
C) (1.90, 8.60)
D) (0.65, 9.85)
E) (2.00, 8.50)""",
answer="D",
explanation="95% CI = 5.25 ± 2.776 × 1.656 = 5.25 ± 4.60, giving (0.65, 9.85). The interval excludes 0, consistent with rejecting the null.",
why_wrong="""B) Uses 1.96 (the z critical value) instead of the t critical value for 4 df.
A), C) and E) Don't match the formula.""",
hint="CI = estimate ± critical t × SE."),

# ---------------- ChimeIn ----------------
dict(id="ch15-chimein-01", source="Chime In (t), Q1-3", topics="t statistic", type="matching",
question="Fill in the blanks: A t value is the distance in (1) ____ between a parameter estimate and its (2) ____ value.",
options="""A) standard errors
B) standard deviations
C) null
D) true""",
answer="1-A, 2-C",
explanation="t = (estimate - null value) / SE: how many standard errors the estimate is from the null.",
why_wrong="Common mix-ups: standard deviations (that's Cohen's d) and the true value (which we don't know).",
hint="What's in the denominator of t?"),

dict(id="ch15-chimein-02", source="Chime In (t), Q4-5", topics="t vs z", type="MC",
question="The main difference between a t value and a z value is that for t we estimate the standard error from the sample. As a consequence, compared to the z (standard normal) distribution, the t distribution has:",
options="""A) A taller peak
B) Fatter tails
C) More tolerance for non-independence
D) No symmetry around its mean""",
answer="B",
explanation="Estimating the SE adds uncertainty, so extreme t values are more common than extreme z values: the t has fatter tails (and needs a larger critical value).",
why_wrong="""A) The t's peak is actually a bit lower.
C) Non-independence is a problem for both.
D) The t is symmetric.""",
hint="More uncertainty means extreme values are more likely."),

dict(id="ch15-chimein-03", source="Chime In (t), Q6", topics="p-values, sampling error", type="MC",
question="A very low p-value means that ____ rarely produces a sample as extreme as ours (or more extreme).",
options="""A) Sampling error
B) Sampling bias
C) The alternative model
D) Non-independence""",
answer="A",
explanation="A p-value asks how often chance alone (sampling error when the null is true) would give a result at least as extreme as ours.",
why_wrong="""B) A p-value assumes no bias; it can't detect it.
C) The p-value is calculated under the null, not the alternative.
D) Non-independence violates the test's assumptions; it isn't what p measures.""",
hint="What model is the p-value calculated under?"),

dict(id="ch15-chimein-04", source="Chime In (t), Q7 and Q14", topics="effect size, Cohen's d", type="MC",
question="Which best captures the effect size?",
options="""A) The number of standard deviations our estimate is from the null (distance from null / SD)
B) The number of standard errors our estimate is from the null (distance from null / SE)
C) The p-value""",
answer="A",
explanation="Effect size (Cohen's d) divides by the SD, which doesn't shrink with sample size. Dividing by the SE gives t, which grows with sample size.",
why_wrong="""B) That's t: it measures evidence against the null and depends on n.
C) The p-value also depends on n.""",
hint="Which quantity stays the same if you collect more data?"),

dict(id="ch15-chimein-05", source="Chime In (t), Q8-9", topics="standard error, sample size, t vs z", type="MC",
question="""Sample size plays two roles when we use the t to describe uncertainty and test null hypotheses:

Role 1: It accounts for uncertainty in our estimate of the SD (the t starts quite different from the z but approaches it as n gets big)
Role 2: It sets the size of the standard error, which describes uncertainty in our estimate of the mean

For most sample sizes, which role matters more?""",
options="""A) Role 1 (t vs z)
B) Role 2 (the standard error)""",
answer="B",
explanation="The SE shrinks with √n at every sample size: quadrupling n halves the SE. The difference between t and z matters only for small samples (with 20 or more observations, critical t values are within a few percent of 1.96).",
why_wrong="A) The t/z difference is real but quickly becomes small; the SE keeps shrinking as n grows.",
hint="Compare how much the critical t changes from n = 10 to 100 with how much the SE changes."),

dict(id="ch15-chimein-06", source="Chime In (t), Q9", topics="standard error, sample size, t vs z", type="open", include="no",
question="""Sample size plays two roles when we use the t: (1) accounting for uncertainty in our estimate of the SD (t approaches z as n grows), and (2) setting the size of the standard error. Explain which matters more, and why.""",
answer="Model answer: B matters more for most studies. The SE is SD/√n, so it keeps shrinking as n grows: quadrupling the sample halves the SE, narrowing CIs and increasing power. The t vs z difference (A) mainly matters for small samples; once n is around 20 or 30 the critical t is close to 1.96, so further increases in n barely change it.",
explanation="Both effects push toward narrower intervals with larger n, but the √n in the SE is the big one.",
hint="How much does the critical t change between n = 30 and n = 300? How much does the SE change?"),

dict(id="ch15-chimein-07", source="Chime In (t), Q10", topics="paired t-test, study design", type="MC",
question="What is the advantage of a paired t-test over a two-sample t-test?",
options="""A) The paired t-test is an easier experiment to pull off
B) The paired t-test does not assume a normal distribution of residuals
C) The paired t-test has more power, because it controls for extraneous variation""",
answer="C",
explanation="Comparing within pairs removes variation among pairs (e.g. some hyena pairs giggle more overall), making the treatment effect easier to see.",
why_wrong="""A) Finding good pairs is often harder.
B) It assumes the differences are roughly normal.""",
hint="What variation disappears when you look at within-pair differences?"),

dict(id="ch15-chimein-08", source="Chime In (t), Q11", topics="paired t-test, study design", type="select-all",
question="When can you use a paired t-test? (Select all that apply.)",
options="""A) When you have natural pairs, one with the treatment and one with the control
B) When you pair individuals who are similar in most ways, with one receiving the treatment and the other the control
C) Whenever you have a balanced design, by making artificial pairs after the fact (one treatment, one control)""",
answer="A, B",
explanation="Pairing has to reflect real shared features (twins, the same individual before and after, matched individuals). Pairing at random after the fact adds no information and is wrong.",
why_wrong="C) Arbitrary pairs don't share anything, so a paired test would be invalid.",
hint="What makes two observations a real pair?"),

dict(id="ch15-chimein-09", source="Chime In (t), Q12", topics="standard error, standard deviation, t statistic", type="MC",
question="Fill in the blanks: The ____ and the ____ describe uncertainty, while the ____ describes variability.",
options="""A) standard error and standard deviation describe uncertainty; the t statistic describes variability
B) standard error and t statistic describe uncertainty; the standard deviation describes variability
C) standard deviation and t statistic describe uncertainty; the standard error describes variability""",
answer="B",
explanation="The SD describes how much individuals vary. The SE (and t, which is built on it) describe uncertainty in an estimate.",
why_wrong="""A) The SD describes spread among individuals, not uncertainty in the mean.
C) The SE describes uncertainty, not variability among individuals.""",
hint="Which of these describes how different individuals are from each other?"),

dict(id="ch15-chimein-10", source="Chime In (t), Q13", topics="p-values, test statistics, effect size", type="MC",
question="Which measures how 'surprising' it would be to see our data if the null were true?",
options="""A) t
B) p
C) Cohen's d""",
answer="B",
explanation="The p-value is the probability of a result at least as extreme as ours if the null were true: small p means surprising.",
why_wrong="""A) t is a test statistic; we need its null distribution to turn it into a probability.
C) Cohen's d is an effect size.""",
hint="Which one is a probability?"),

dict(id="ch15-chimein-11", source="Chime In (t), Q15", topics="p-values", type="TF",
question="TRUE or FALSE: A p-value is the probability that our null hypothesis is true.",
options="""A) TRUE
B) FALSE""",
answer="B",
explanation="A p-value assumes the null is true and asks how often we'd see data this extreme. It's a statement about the data given the null, not about the null given the data.",
why_wrong="TRUE: a very common misreading of p-values.",
hint="Is p calculated assuming the null is true, or is it about whether the null is true?"),

# ---------------- Book: t summary ----------------
dict(id="ch15-book-01", source="Book: t summary (Q1)", topics="t vs z", type="MC",
question="The difference between a t value and a z value is:",
options="""A) The z assumes the mean is zero; the t does not
B) The z assumes samples come from a normal distribution; the t does not
C) The z assumes we know the population SD; the t uses an estimate""",
answer="C", near_duplicate_of="ch15-hw-01",
explanation="Both assume normality. The t adds uncertainty because the SD is estimated from the sample.",
why_wrong="""A) Both are calculated relative to a null value, which need not be zero.
B) The t also assumes (approximate) normality.""",
hint="Where does the SD in each formula come from?"),

dict(id="ch15-book-02", source="Book: t summary (Q2)", topics="t-test assumptions, central limit theorem", type="MC",
question="If our sample is not perfectly normal:",
options="""A) We cannot use t-based tests at all, as they assume normality
B) We can, if n is large and the deviations are modest (thanks to the CLT)
C) It has no impact; that's why we use a t distribution instead of a z""",
answer="B", near_duplicate_of="ch15-hw-02",
explanation="t-tests are robust to modest non-normality, especially in larger samples, because sampling distributions of means become roughly normal.",
why_wrong="""A) Perfect normality is never required (and never true).
C) The t handles an estimated SD, not non-normality.""",
hint="Which theorem is about means of large samples?"),

dict(id="ch15-book-03", source="Book: t summary (Q3)", topics="t vs z", type="MC",
question="The t and z distributions are never perfectly identical. When are they very close to one another?",
options="""A) When the sample size is large
B) When the standard deviation is small
C) When the data are normal
D) Never: they are very different distributions""",
answer="A", near_duplicate_of="ch15-hw-03",
explanation="As df grow, the estimated SD gets more precise and the t converges to the z.",
why_wrong="""B) The size of the SD doesn't change the shape of t.
C) Normal data don't remove the extra uncertainty from estimating the SD.
D) They converge with large samples.""",
hint="What happens to the t's fat tails as the sample grows?"),

dict(id="ch15-book-04", source="Book: t summary (Q4)", topics="effect size, Cohen's d", type="MC",
question="Which is the best summary of the effect size for normally distributed data?",
options="""A) The p-value
B) The difference between the estimate and its null value
C) The difference between the estimate and its null value, standardized by the standard deviation
D) The difference between the estimate and its null value, standardized by the standard error""",
answer="C", near_duplicate_of="ch15-chimein-04",
explanation="That's Cohen's d: the difference in SD units, comparable across studies and independent of sample size.",
why_wrong="""A) p depends on sample size.
B) Useful, but depends on units.
D) That's t, which grows with sample size.""",
hint="Which one doesn't change if you collect more data?"),

dict(id="ch15-book-05", source="Book: t summary (Q5)", topics="assessing normality, QQ plots", type="MC",
question=HYENA + "\n\nThe QQ plot of the nine differences is shown. Evaluate it in relation to the normality assumption.",
image="ch15-book-hyena-qq.png",
options="""A) The data are perfectly normal
B) The data likely deviate somewhat from normality, but a t-test is probably OK
C) The data deviate strongly from normality, so any test assuming normality can't be trusted""",
answer="B",
explanation="The points follow the line reasonably well, with some wobble at the ends, which is expected with only nine points. Nothing suggests a serious problem.",
why_wrong="""A) Real data are never perfectly normal.
C) The departures are modest; with nine points some scatter around the line is normal.""",
hint="With only nine points, how closely would you expect them to follow the line?"),

dict(id="ch15-book-06", source="Book: t summary (Q6)", topics="t statistic, standard error, paired t-test", type="numeric",
question=HYENA + "\n\nHow many standard errors away from zero is the mean difference in giggling? (That is, what is t?)",
answer="2.85", explanation="SE = 0.0954 / √9 = 0.0318. t = 0.0906 / 0.0318 = 2.85.",
why_wrong="Common mistake: dividing by the SD instead of the SE (gives 0.95, Cohen's d).",
hint="First find the SE = SD / √n."),

dict(id="ch15-book-07", source="Book: t summary (Q7)", topics="confidence intervals", type="MC",
question="The 95% CI is calculated as the estimate ± the critical t value (at α = 0.05) times ____.",
options="""A) Cohen's d
B) The standard deviation
C) The variance
D) t
E) The standard error
F) 1.96""",
answer="E",
explanation="CI = estimate ± critical t × SE.",
why_wrong="""B) Using the SD would describe where individuals fall, not uncertainty in the estimate.
F) 1.96 is the z critical value; with the t we use the critical t.""",
hint="Which quantity describes uncertainty in the estimate?"),

dict(id="ch15-book-08", source="Book: t summary (Q8)", topics="critical t, R", type="MC",
question="For the nine hyena pairs (8 df), which R code gives the (absolute) critical t value for a two-tailed 95% confidence interval?",
options="""A) qt(0.025, df = 8, lower.tail = FALSE)
B) qt(0.05, df = 8, lower.tail = FALSE)
C) pt(0.025, df = 8)
D) qt(0.025, df = 9, lower.tail = FALSE)""",
answer="A",
explanation="A two-tailed 95% interval leaves 2.5% in each tail, and a paired test with nine pairs has 9 - 1 = 8 df. qt(0.025, 8, lower.tail = FALSE) = 2.31.",
why_wrong="""B) 0.05 in one tail gives a 90% two-tailed interval.
C) pt() returns a probability, not a quantile.
D) Wrong df: n - 1 = 8.""",
hint="How much area goes in each tail? How many df?"),

dict(id="ch15-book-09", source="Book: t summary (Q9-10)", topics="NHST, critical values", type="MC",
question=HYENA + "\n\nt = 2.85 and the critical t value is 2.31 (8 df, α = 0.05). What should we conclude?",
options="""A) Reject the null, since t exceeds the critical value; we could be wrong
B) Fail to reject the null, since t exceeds the critical value
C) We can't know what to do until we find the exact p-value
D) Reject the null, which proves that subordinates giggle more""",
answer="A",
explanation="|t| exceeds the critical value, so p < 0.05 (it's 0.022). We act as if the null is false while acknowledging a real chance of a type I error.",
why_wrong="""B) A t beyond the critical value means rejection.
C) Comparing t to the critical value gives the same decision as comparing p to α.
D) Rejecting the null doesn't prove anything.""",
hint="Being beyond the critical value is the same as p < α."),

dict(id="ch15-book-10", source="Book: t summary (Q11)", topics="p-values", type="MC",
question="Say you found a p-value of p. Which is a correct interpretation?",
options="""A) p is the probability that the null hypothesis generated the data
B) p is the probability that the null hypothesis is true
C) p is the probability that a random sample from the null distribution would be as or more extreme than our data""",
answer="C", near_duplicate_of="ch15-chimein-11",
explanation="A p-value is calculated assuming the null is true: how often would the null produce a result at least this extreme?",
why_wrong="""A) and B) Both treat p as a probability about the null itself, which it isn't.""",
hint="Is p calculated assuming the null is true?"),

dict(id="ch15-book-11", source="Book: t summary (Q12)", topics="paired t-test, study design", type="TF",
question="Say you had data from two more dominant and two more subordinate hyenas, but they weren't in pairs. Would it be legitimate to pair them at random and do a paired t-test?",
options="""A) Yes
B) No""",
answer="B", near_duplicate_of="ch15-chimein-08",
explanation="Pairs must share something real (here, living together). Random pairs share nothing, so the paired analysis would be invalid; use a two-sample approach instead.",
why_wrong="A) Random pairing creates the appearance of a design that doesn't exist.",
hint="What makes a pair a pair?"),
]
