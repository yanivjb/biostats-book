from ai_helpers import V, r
from scipy.stats import t as T
import importlib.util, os
spec = importlib.util.spec_from_file_location('o15', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rows_ch15.py')); o = importlib.util.module_from_spec(spec); spec.loader.exec_module(o)
TEMP, CHAT, HYENA = o.TEMP, o.CHAT, o.HYENA
TEMP2 = "To check the folk value of 98.6 °F for human body temperature, a class measured 16 healthy volunteers: mean 98.30 °F, sample variance 0.64."
ANT = "To ask whether ant colonies forage more in warm weather, a researcher counted foragers leaving 10 nests on a cool morning and again on a warm afternoon (difference = warm minus cool). The mean difference is 12 ants, and the variance of the differences is 100."
p2 = lambda t, df: 2*T.sf(abs(t), df)
ROWS = [
V("ch15-quiz-01", 1, question=TEMP2 + "\n\nTesting the null hypothesis that mean body temperature is 98.6 °F, what is the numerator of t (the estimate minus its null value)?",
answer=r(98.30-98.6,2), explanation="98.30 - 98.6 = -0.30 °F.", hint="Estimate minus null value."),
V("ch15-quiz-01", 2, question=TEMP + "\n\nIf instead we tested the null hypothesis that mean body temperature is 98.2 °F, what would the numerator of t be?",
answer=r(98.524-98.2,3), explanation="98.524 - 98.2 = 0.324 °F.", hint="Estimate minus the new null value."),

V("ch15-quiz-02", 1, question=TEMP2 + "\n\nWhat is the sample standard deviation?",
answer=r(0.64**0.5,2), explanation="SD = √0.64 = 0.80 °F.", hint="Square root of the variance."),
V("ch15-quiz-02", 2, question="A sample of 25 body temperatures has a standard deviation of 0.678 °F. What is the sample variance?",
answer=r(0.678**2,3), explanation="Variance = SD² = 0.678² = 0.460.", hint="Square the SD."),

V("ch15-quiz-03", 1, question=TEMP2 + "\n\nThe mean is 0.30 °F below 98.6, and the SD is 0.80 °F. What is Cohen's d, and how big is this effect?",
options="""A) d ≈ 0.38, a small effect (< 0.5)
B) d ≈ 0.60, a medium effect (0.5 to 0.8)
C) d ≈ 1.50, a large effect (> 0.8)
D) d ≈ 0.09, a small effect (< 0.5)""", answer="A",
explanation="d = 0.30 / 0.80 = 0.375, a small effect.",
why_wrong="""B) Divides by something other than the SD.
C) That's t (0.30 / SE of 0.20), not d.
D) That's 0.30 × 0.30.""", hint="Difference ÷ SD."),
V("ch15-quiz-03", 2, question=TEMP + "\n\nWhy is Cohen's d (0.11) so much smaller than |t| (0.56) for these data?",
options="""A) d divides by the SD, while t divides by the smaller SE
B) d divides by the SE, while t divides by the larger SD
C) d ignores the sign of the difference, so it is smaller
D) d is a probability, so it must be less than t""", answer="A",
explanation="d = difference / SD; t = difference / SE, and SE = SD / √n is smaller, so |t| = d × √n = 0.11 × 5 = 0.56.",
why_wrong="""B) It's the other way around.
C) Ignoring the sign doesn't change the size.
D) d is not a probability.""", hint="Compare the denominators."),

V("ch15-quiz-04", 1, question=TEMP2 + "\n\nThe sample SD is 0.80 °F. What is the standard error of the mean?",
answer=r(0.8/4,2), explanation="SE = 0.80 / √16 = 0.80 / 4 = 0.20 °F.", hint="SD / √n."),
V("ch15-quiz-04", 2, question=TEMP + "\n\nThe sample SD is 0.678 °F. What would the standard error be if the same SD came from a sample of 100 people?",
answer=r(0.678/10,4), explanation="SE = 0.678 / √100 = 0.0678 °F.", hint="SD / √n with n = 100."),

V("ch15-quiz-05", 1, question=TEMP2 + "\n\nThe estimate minus the null value is -0.30, and the standard error is 0.20. What is t?",
answer=r(-0.3/0.2,2), explanation="t = -0.30 / 0.20 = -1.5.", hint="Numerator ÷ SE."),
V("ch15-quiz-05", 2, question=TEMP + "\n\nThe numerator of t is -0.076 and the standard error is 0.136. If the sample had been 4 times larger with the same mean and SD, the SE would be 0.068. What would t be?",
answer=r(-0.076/0.068,2), explanation="t = -0.076 / 0.068 = -1.12. Quadrupling n halves the SE and doubles t.", hint="Numerator ÷ the new SE."),

V("ch15-quiz-06", 1, question=TEMP2 + "\n\nt = -1.5 (15 df). Before calculating a p-value, what do you expect to do with the null hypothesis at α = 0.05?",
options="""A) Obviously reject the null
B) Probably fail to reject the null
C) Can't tell without knowing the SD""", answer="B",
explanation="Rejecting at α = 0.05 needs |t| of about 2 or more (2.13 for 15 df). -1.5 isn't there. (p = 0.15.)",
why_wrong="""A) |t| is below ~2.
C) t already incorporates the SD.""", hint="Compare |t| with about 2."),
V("ch15-quiz-06", 2, question="A one-sample t-test with 24 df gives t = 4.8. Before calculating a p-value, what do you expect to do with the null hypothesis at α = 0.05?",
options="""A) Clearly reject the null
B) Clearly fail to reject the null
C) Uncertain: it's on the border""", answer="A",
explanation="|t| = 4.8 is far beyond the critical value of about 2.06, so p is tiny (< 0.001).",
why_wrong="""B) Large |t| means the estimate is far from the null.
C) 4.8 is nowhere near the border of ~2.""", hint="Compare |t| with about 2."),

V("ch15-quiz-07", 1, question=TEMP2 + "\n\nThe two-tailed p-value is 0.15. At α = 0.05, what do we do and conclude?",
options="""A) Reject the null; mean body temperature is not 98.6 °F
B) Fail to reject; mean body temperature is exactly 98.6 °F
C) Fail to reject; the data are consistent with a mean of 98.6 °F
D) Accept the null; it has an 85% chance of being true""", answer="C",
explanation="p > 0.05, so we fail to reject. That means the data are consistent with 98.6, not that it's proven.",
why_wrong="""A) p > α.
B) Failing to reject doesn't prove the null.
D) p isn't the probability the null is false.""", hint="Failing to reject ≠ proving the null."),
V("ch15-quiz-07", 2, question="A one-sample t-test of whether mean body temperature equals 98.6 °F gives p = 0.002. At α = 0.05, what do we do and conclude?",
options="""A) Reject; the data are unlikely if the mean were 98.6 °F
B) Reject; there's a 0.2% chance the mean is 98.6 °F
C) Fail to reject; p is smaller than α, so the null stands
D) Fail to reject; we need a larger sample to decide""", answer="A",
explanation="p < α, so we reject: data this extreme would be rare if the true mean were 98.6.",
why_wrong="""B) p isn't the probability the null is true.
C) and D) p < α means we reject.""", hint="What does a small p say about the data under the null?"),

V("ch15-quiz-08", 1, question="For the body temperature data (t = -0.56, n = 25, so 24 df), which R code gives the ONE-tailed p-value for the alternative that mean temperature is LESS than 98.6?",
options="""A) pt(-0.56, df = 24)
B) 2 * pt(-0.56, df = 24)
C) pt(-0.56, df = 24, lower.tail = FALSE)
D) qt(-0.56, df = 24)""", answer="A",
explanation="pt() gives the area below t, which is the lower tail for this one-sided alternative.",
why_wrong="""B) That's two-tailed.
C) That's the area above -0.56.
D) qt() takes a probability.""", hint="Which tail matches 'less than'?"),
V("ch15-quiz-08", 2, question="For a one-sample t-test with n = 16 and t = 2.1, which R code gives the two-tailed p-value?",
options="""A) 2 * pt(2.1, df = 15, lower.tail = FALSE)
B) 2 * pt(2.1, df = 16, lower.tail = FALSE)
C) pt(2.1, df = 15, lower.tail = FALSE)
D) 2 * pt(2.1, df = 15)""", answer="A",
explanation="One-sample df = n - 1 = 15. Area above |t| in one tail, doubled.",
why_wrong="""B) df should be 15.
C) That's one-tailed.
D) That doubles the area BELOW 2.1, giving more than 1.""", hint="df = n - 1; double one tail."),

V("ch15-quiz-09", 1, question=TEMP2 + "\n\nThe standard error is 0.20 and the critical t value for 15 df at α = 0.05 is 2.131. What is the 95% confidence interval for mean body temperature?",
options="""A) 98.30 ± 0.20, i.e. (98.10, 98.50)
B) 98.30 ± 0.43, i.e. (97.87, 98.73)
C) 98.30 ± 1.70, i.e. (96.60, 100.00)
D) 98.60 ± 0.43, i.e. (98.17, 99.03)""", answer="B",
explanation="98.30 ± 2.131 × 0.20 = 98.30 ± 0.43. It includes 98.6, matching p > 0.05.",
why_wrong="""A) Forgets the critical t.
C) Uses the SD × critical t.
D) Centers on the null value instead of the estimate.""", hint="Estimate ± critical t × SE."),
V("ch15-quiz-09", 2, question=TEMP + "\n\nThe 95% confidence interval for mean body temperature is (98.24, 98.80). Without calculating a p-value, what can you say about a test of the null hypothesis that the mean is 98.6 °F?",
options="""A) p > 0.05, because 98.6 is inside the 95% CI
B) p < 0.05, because 98.6 is inside the 95% CI
C) p > 0.05, because 98.6 is not equal to 98.524
D) Nothing; CIs and p-values are unrelated""", answer="A",
explanation="A two-tailed test at α = 0.05 rejects exactly when the null value falls outside the 95% CI. 98.6 is inside, so p > 0.05.",
why_wrong="""B) Inside the CI means don't reject.
C) The estimate never equals the null exactly.
D) They're two sides of the same calculation.""", hint="Is 98.6 inside the interval?"),

V("ch15-hw-01", 1, question="A researcher knows the true population SD of fish length from decades of census data, and samples 12 fish. Should they use a z or a t to test whether mean length has changed?",
options="""A) z, because the population SD is known
B) t, because the sample size is small
C) t, because the mean is not zero
D) z, because fish length is continuous""", answer="A",
explanation="The t accounts for estimating the SD. If σ is truly known, z is appropriate even for small samples.",
why_wrong="""B) Small n matters only because the SD is estimated.
C) Neither needs the mean to be 0.
D) Both handle continuous data.""", hint="What extra uncertainty does the t account for?"),
V("ch15-hw-01", 2, question="Why do we usually use a t distribution rather than a z for a sample mean in biology?",
options="""A) We rarely know the population SD, so we estimate it from the sample
B) Biological data are rarely normally distributed, and the t corrects for that
C) The t works for proportions, and the z only works for means
D) Our sample sizes are almost always larger than 1,000 individuals""", answer="A",
explanation="The t adds uncertainty for estimating σ from the data.",
why_wrong="""B) The t assumes normality too.
C) Not the distinction.
D) Large n would make t ≈ z anyway.""", hint="What does the t assume we don't know?"),

V("ch15-hw-02", 1, question="A researcher runs a t-test on 6 measurements of flower height, and the data are strongly right-skewed with one huge value. Which statement best describes whether the test is appropriate?",
options="""A) It's risky: with so few points, the CLT can't fix the skew
B) It's fine: the t distribution automatically corrects for skew
C) It's fine: t-tests make no assumptions about the data
D) It's risky only because the sample mean is not zero""", answer="A",
explanation="The t-test is robust to skew mainly in larger samples. With n = 6 and strong skew, the sampling distribution of the mean may be far from normal.",
why_wrong="""B) The t corrects for estimating the SD, not for skew.
C) It assumes normality of the sampling distribution.
D) The mean being zero is irrelevant.""", hint="Does the CLT help with n = 6?"),
V("ch15-hw-02", 2, question="Which situation makes a t-test MOST robust to mildly skewed data?",
options="""A) A large sample, such as 200 observations
B) A small sample, such as 5 observations
C) A sample whose mean happens to be near zero
D) A sample with a large standard deviation""", answer="A",
explanation="With large samples, the CLT makes the sampling distribution of the mean nearly normal.",
why_wrong="""B) Small samples don't benefit from the CLT.
C) and D) These don't affect robustness to skew.""", hint="Central limit theorem."),

V("ch15-hw-03", 1, question="With which sample would a t-test and a z-test give the MOST different p-values?",
options="""A) n = 4
B) n = 40
C) n = 400
D) They always give identical p-values""", answer="A",
explanation="With few df, the t has much fatter tails than the z (critical t for 3 df is 3.18 vs 1.96).",
why_wrong="""B) and C) t approaches z as n grows.
D) They differ, especially for small n.""", hint="When does t look least like z?"),
V("ch15-hw-03", 2, question="The critical t value (α = 0.05, two-tailed) is 2.78 for 4 df, 2.09 for 20 df and 1.98 for 100 df. What does this pattern show?",
options="""A) The t approaches the z (1.96) as degrees of freedom grow
B) The t has thinner tails than the z for small samples
C) Larger samples need larger t values to reject the null
D) The critical value depends on the sample mean""", answer="A",
explanation="As df grow, the SD is estimated more precisely and the t converges to the z.",
why_wrong="""B) The t has fatter tails for small samples.
C) The critical value shrinks with n.
D) It depends only on df and α.""", hint="Compare each to 1.96."),

V("ch15-hw-04", 1, question=ANT + "\n\nFor a two-tailed test, match each hypothesis to its statement:\n\n1. Null hypothesis\n2. Alternative hypothesis",
options="""A) The mean difference in foragers (warm - cool) equals 0
B) The mean difference in foragers (warm - cool) does not equal 0
C) The mean difference in foragers (warm - cool) is greater than 0
D) Warm weather makes ants forage more""", answer="1-A, 2-B",
explanation="Null: no difference. Two-tailed alternative: a difference in either direction.", why_wrong="C) is one-tailed; D) is a scientific hypothesis, not a statistical one.", hint="Two-tailed means 'not equal'."),
V("ch15-hw-04", 2, question=CHAT + "\n\nFor a ONE-tailed test of whether the chatbot improves scores, match each hypothesis to its statement:\n\n1. Null hypothesis\n2. Alternative hypothesis",
options="""A) The mean difference in exam scores (chatbot - control) is 0 or less
B) The mean difference in exam scores (chatbot - control) does not equal 0
C) The mean difference in exam scores (chatbot - control) is greater than 0
D) Chatbots help you learn""", answer="1-A, 2-C",
explanation="A one-tailed alternative specifies a direction (greater than 0); the null covers everything else.", why_wrong="B) is two-tailed; D) is not a statistical hypothesis.", hint="One-tailed means one direction."),

V("ch15-hw-05", 1, question=ANT + "\n\nWhat is Cohen's d for this difference?",
options="""A) 1.2
B) 0.12
C) 3.8
D) 12""", answer="A",
explanation="SD = √100 = 10, so d = 12 / 10 = 1.2.",
why_wrong="""B) Divides by the variance.
C) That's t (12 / SE of 3.16).
D) That's the raw difference.""", hint="Mean difference ÷ SD."),
V("ch15-hw-05", 2, question=CHAT + "\n\nWhy is Cohen's d (1.42) a better measure of effect size here than t (3.17)?",
options="""A) d doesn't change with sample size; t grows as n grows
B) d accounts for sample size; t ignores it entirely
C) d is a probability; t is not a probability at all
D) d is always larger than t, so it's easier to detect""", answer="A",
explanation="d = difference / SD describes the size of the effect. t = difference / SE grows with √n, so it mixes effect size with sample size.",
why_wrong="""B) It's the reverse.
C) Neither is a probability.
D) d is usually smaller than t.""", hint="Which one depends on n?"),

V("ch15-hw-06", 1, question=ANT + "\n\nWhat is the standard error of the mean difference?",
answer=r(10/10**0.5,2), explanation="SD = √100 = 10; SE = 10 / √10 = 3.16.", hint="SD / √n."),
V("ch15-hw-06", 2, question=ANT + "\n\nThe standard error of the mean difference is 3.16. What is t?",
answer=r(12/(10/10**0.5),2), explanation="t = 12 / 3.16 = 3.79.", hint="Mean difference ÷ SE."),

V("ch15-hw-07", 1, question=ANT + " t = 3.79.\n\nIn R:\n2 * pt(3.79, df = 9, lower.tail = FALSE)\n[1] " + r(p2(3.79,9),4) + "\n\nWhat is the two-tailed p-value? Report it to three decimals.",
answer=r(p2(3.79,9),3), explanation="With 10 nests, df = 9. The p-value is " + r(p2(3.79,9),3) + ".", hint="Read it from the R output."),
V("ch15-hw-07", 2, question=CHAT + "\n\nHow many degrees of freedom does this paired t-test have?",
answer="4", explanation="A paired t-test is a one-sample test on the differences: df = number of pairs - 1 = 5 - 1 = 4.", hint="Count pairs, not students."),

V("ch15-hw-08", 1, question=ANT + " The two-tailed p-value is " + r(p2(3.79,9),3) + ". At α = 0.05, what do we do, and what does it mean?",
options="""A) Reject; warm weather definitely increases foraging
B) Reject; we act as if the null is false, knowing we could be wrong
C) Fail to reject; foraging is the same at both temperatures
D) Fail to reject; we need more nests before deciding""", answer="B",
explanation="p < 0.05, so we reject. That's not proof: a type I error is possible.",
why_wrong="""A) Rejection isn't proof.
C) and D) p < α.""", hint="Rejecting isn't proving."),
V("ch15-hw-08", 2, question=CHAT + "\n\nSuppose instead the p-value had been 0.21. At α = 0.05, what would we do, and what would it mean?",
options="""A) Reject; the chatbot has no effect on exam scores
B) Fail to reject; the chatbot has no effect on exam scores
C) Fail to reject; the data don't show a clear effect either way
D) Accept the null; the chatbot certainly does not help""", answer="C",
explanation="p > α, so we fail to reject. With five pairs, we may simply lack power; it doesn't show there's no effect.",
why_wrong="""A) p > α.
B) and D) Failing to reject isn't evidence of no effect.""", hint="Absence of evidence…"),

V("ch15-hw-09", 1, question=ANT + " The SE is 3.16, and the critical t value for 9 df at α = 0.05 is 2.262. What is the 95% confidence interval for the mean difference?",
options="""A) (4.85, 19.15)
B) (8.84, 15.16)
C) (-10.6, 34.6)
D) (5.80, 18.20)""", answer="A",
explanation="12 ± 2.262 × 3.16 = 12 ± 7.15 → (4.85, 19.15). It excludes 0, matching p < 0.05.",
why_wrong="""B) Forgets the critical t.
C) Uses the SD instead of the SE.
D) Uses 1.96 × 3.16, the z value, instead of the critical t.""", hint="Estimate ± critical t × SE."),
V("ch15-hw-09", 2, question=CHAT + "\n\nThe 95% CI for the mean difference is (0.65, 9.85). Which statement is correct?",
options="""A) It excludes 0, consistent with rejecting the null at α = 0.05
B) It includes 5.25, so we fail to reject the null at α = 0.05
C) It is wide, so the chatbot must have no real effect on scores
D) There is a 95% chance the true difference is between 0.65 and 9.85""", answer="A",
explanation="A 95% CI excluding 0 corresponds to p < 0.05 for a two-tailed test of no difference.",
why_wrong="""B) The CI always contains the estimate; what matters is the null value (0).
C) A wide CI means imprecision, not no effect.
D) The 95% describes the procedure, not this interval.""", hint="Is the null value inside the interval?"),

V("ch15-chimein-01", 1, question="A t value of -3 means that the parameter estimate is:",
options="""A) 3 standard errors below its null value
B) 3 standard deviations below its null value
C) 3 units below its true population value
D) 3 times smaller than its null value""", answer="A",
explanation="t = (estimate - null) / SE: the distance from the null in standard errors.",
why_wrong="""B) That would be like Cohen's d.
C) and D) t is in SE units, measured from the null.""", hint="t's denominator is the SE."),
V("ch15-chimein-01", 2, question="Fill in the blanks: t = (1) ____ minus its null value, divided by its (2) ____.",
options="""A) the estimate
B) the true parameter
C) standard error
D) standard deviation""", answer="1-A, 2-C",
explanation="t = (estimate - null) / SE.", why_wrong="We never know the true parameter; dividing by the SD gives an effect size.", hint="What do we actually have from the sample?"),

V("ch15-chimein-02", 1, question="Because the t distribution has fatter tails than the z, the critical value for a 95% confidence interval with a small sample is:",
options="""A) Larger than 1.96
B) Smaller than 1.96
C) Exactly 1.96
D) Negative""", answer="A",
explanation="Fatter tails push 2.5% of the area farther out, so the critical t exceeds 1.96 (e.g. 2.78 for 4 df).",
why_wrong="""B) and C) Fatter tails mean a larger cutoff.
D) We use the absolute value.""", hint="Where does the outer 2.5% start in a fat-tailed distribution?"),
V("ch15-chimein-02", 2, question="Why does the t distribution have fatter tails than the standard normal (z)?",
options="""A) Because the SD is estimated from the sample, adding uncertainty
B) Because biological data are skewed, adding extreme values
C) Because the t is used only for paired data, not independent data
D) Because the null hypothesis is usually false in real studies""", answer="A",
explanation="Estimating the SD (and so the SE) adds uncertainty, making extreme t values more common.",
why_wrong="""B) The t assumes normal data.
C) The t is used for many tests.
D) Tails come from the sampling math, not the truth of the null.""", hint="What does the t estimate that the z knows?"),

V("ch15-chimein-03", 1, question="A large p-value (say 0.6) means that, if the null were true, sampling error would ____ produce a sample as extreme as ours (or more extreme).",
options="""A) often
B) rarely
C) never
D) always""", answer="A",
explanation="p = 0.6 means 60% of samples under the null would be at least as extreme: very common.",
why_wrong="""B) That's a small p.
C) and D) p is between 0 and 1.""", hint="What fraction of null samples are this extreme?"),
V("ch15-chimein-03", 2, question="A p-value is the probability of a result at least as extreme as ours, assuming:",
options="""A) The null hypothesis is true
B) The alternative hypothesis is true
C) There is no sampling error
D) The sample is very large""", answer="A",
explanation="p-values are calculated under the null: how often would chance alone produce this?",
why_wrong="""B) p doesn't assume the alternative.
C) Sampling error is what p accounts for.
D) p-values exist for any sample size.""", hint="Which hypothesis do we assume?"),

V("ch15-chimein-04", 1, question="Two studies find the same difference from the null and the same SD, but one has n = 10 and the other n = 1,000. Which is the same in both?",
options="""A) Cohen's d
B) t
C) The p-value
D) The standard error""", answer="A",
explanation="d = difference / SD, which doesn't depend on n. The SE, t and p all change with n.",
why_wrong="""B), C) and D) All depend on sample size.""", hint="Which one doesn't involve n?"),
V("ch15-chimein-04", 2, question="Which quantity measures how far an estimate is from the null in units of standard errors?",
options="""A) t
B) Cohen's d
C) The p-value""", answer="A",
explanation="t = (estimate - null) / SE. Cohen's d uses the SD instead.",
why_wrong="""B) d uses the SD.
C) p is a probability.""", hint="SE units."),

V("ch15-chimein-05", 1, question="A researcher increases sample size from 10 to 40. Which effect on their 95% CI is larger?",
options="""A) The critical t shrinks from 2.26 to 2.02
B) The SE halves, since √40 is double √10""", answer="B",
explanation="Halving the SE halves the CI width. The drop in critical t (about 11%) is much smaller.",
why_wrong="A) It's real but small compared with the SE change.", hint="Compare a halving with an 11% change."),
V("ch15-chimein-05", 2, question="For samples larger than about 30, the main reason confidence intervals keep shrinking as n grows is:",
options="""A) The standard error keeps shrinking with √n
B) The t distribution keeps getting closer to z""", answer="A",
explanation="By n ≈ 30 the t is already close to z, but the SE keeps shrinking as 1/√n.",
why_wrong="B) The t vs z difference is already tiny by then.", hint="Which change continues at all sample sizes?"),

V("ch15-chimein-07", 1, question="Researchers measure blood pressure in 20 patients before and after a drug. Why is a paired t-test better than a two-sample t-test here?",
options="""A) It removes variation among patients, increasing power
B) It doesn't assume the differences are normally distributed
C) It needs only half as many patients as a two-sample test
D) It works even when the measurements are not independent pairs""", answer="A",
explanation="Each patient is their own control, so differences among patients drop out.",
why_wrong="""B) The paired t assumes normal differences.
C) It's about power, not a rule on sample size.
D) It needs genuine pairs.""", hint="What does comparing within a patient remove?"),
V("ch15-chimein-07", 2, question="Compared with ignoring the pairs and running a two-sample t-test, a paired t-test on naturally paired data usually gives:",
options="""A) A smaller SE and more power
B) A larger SE and less power
C) The same SE and the same power""", answer="A",
explanation="Removing pair-to-pair variation shrinks the SE, increasing power.",
why_wrong="""B) Pairing reduces noise.
C) Pairing changes the SE when pairs share variation.""", hint="What happens to noise when you compare within pairs?"),

V("ch15-chimein-08", 1, question="Which designs are appropriate for a paired t-test? (Select all that apply.)",
options="""A) Measuring the same lizards' sprint speed at two temperatures
B) Comparing twins, one given a supplement and one a placebo
C) Matching ten treatment and ten control mice at random after the experiment""", answer="A, B",
explanation="Repeated measures and twins are real pairs. Random after-the-fact matching shares nothing.",
why_wrong="C) Random pairing adds no information.", hint="Do the pairs share something real?"),
V("ch15-chimein-08", 2, question="Which designs are NOT appropriate for a paired t-test? (Select all that apply.)",
options="""A) Pairing plants at random after the experiment because the design is balanced
B) Comparing left and right leaves on the same plant, one treated and one not
C) Pairing the tallest treated plant with the tallest control plant after the experiment""", answer="A, C",
explanation="Pairs must be set by real shared features before treatment. Pairing after the fact (randomly or by the outcome) is invalid.",
why_wrong="B) Two leaves on the same plant are natural pairs.", hint="When and how were the pairs formed?"),

V("ch15-chimein-09", 1, question="Which quantity describes VARIABILITY among individuals rather than uncertainty in an estimate?",
options="""A) The standard deviation
B) The standard error
C) The width of the confidence interval""", answer="A",
explanation="The SD describes spread among individuals; the SE and CI describe uncertainty in an estimate.",
why_wrong="B) and C) describe uncertainty.", hint="Individuals vs estimates."),
V("ch15-chimein-09", 2, question="As sample size increases, which of these is expected to shrink?",
options="""A) The standard error
B) The standard deviation
C) The variance""", answer="A",
explanation="Uncertainty (SE) shrinks with n; variability (SD, variance) is a property of the population and doesn't.",
why_wrong="B) and C) estimate population variability, which doesn't depend on n.", hint="Uncertainty vs variability."),

V("ch15-chimein-10", 1, question="Which tells us how large an effect is, regardless of sample size?",
options="""A) Cohen's d
B) The t value
C) The p-value""", answer="A",
explanation="d standardizes the difference by the SD. t and p both depend on sample size.",
why_wrong="B) and C) change with n.", hint="Which one ignores n?"),
V("ch15-chimein-10", 2, question="Which measures how many standard errors our estimate is from the null value?",
options="""A) t
B) p
C) Cohen's d""", answer="A",
explanation="t = (estimate - null) / SE.", why_wrong="B) p is a probability. C) d uses the SD.", hint="SE units."),

V("ch15-chimein-11", 1, question="TRUE or FALSE: A p-value of 0.03 means there is a 3% chance that the alternative hypothesis is false.",
options="""A) TRUE
B) FALSE""", answer="B",
explanation="p is the probability of data this extreme if the null were true. It says nothing directly about the probability of either hypothesis.",
why_wrong="TRUE: p is not a probability about hypotheses.", hint="What does p condition on?"),
V("ch15-chimein-11", 2, question="TRUE or FALSE: A p-value is the probability of getting a result at least as extreme as ours if the null hypothesis were true.",
options="""A) TRUE
B) FALSE""", answer="A",
explanation="That's exactly the definition.", why_wrong="FALSE: this is the correct definition.", hint="Data given the null."),

V("ch15-book-01", 1, question="Which assumption do the z and t share?",
options="""A) The sampling distribution of the estimate is normal
B) The population standard deviation is known
C) The population mean is exactly zero
D) The sample size is larger than 100""", answer="A",
explanation="Both assume a normal sampling distribution. Only z assumes σ is known.",
why_wrong="""B) Only z assumes that.
C) Neither does.
D) Neither requires this.""", hint="What do both rely on?"),
V("ch15-book-01", 2, question="A t-based test differs from a z-based test because the t:",
options="""A) Uses an SD estimated from the sample
B) Does not assume normality at all
C) Is only for comparing two groups
D) Assumes the true mean is zero""", answer="A",
explanation="The t accounts for estimating the SD from the sample.",
why_wrong="""B) Both assume normality.
C) The t is used for one sample, two samples and more.
D) Neither assumes that.""", hint="What does the t not know?"),

V("ch15-book-02", 1, question="A sample of 80 leaf areas is slightly right-skewed. Can we use a t-test?",
options="""A) Yes, probably: the CLT makes the mean nearly normal
B) No: t-tests require perfectly normal data
C) Yes: the t is designed to correct for skewed data
D) No: skewed data can never be analyzed with t""", answer="A",
explanation="With 80 observations and mild skew, the sampling distribution of the mean is close to normal.",
why_wrong="""B) and D) Perfect normality isn't required.
C) The t corrects for estimating the SD, not for skew.""", hint="Central limit theorem."),
V("ch15-book-02", 2, question="Which situation is the BIGGEST concern for using a t-test?",
options="""A) A small sample with strong skew
B) A large sample with mild skew
C) A large sample with normal data
D) A small sample with normal data""", answer="A",
explanation="Strong skew with few observations means the CLT can't make the sampling distribution normal.",
why_wrong="""B) The CLT handles mild skew in large samples.
C) and D) Normal data are fine.""", hint="When can't the CLT help?"),

V("ch15-book-03", 1, question="With which degrees of freedom are the t and z distributions most different?",
options="""A) 2 df
B) 20 df
C) 200 df
D) They're equally different at every df""", answer="A",
explanation="With very few df, the t has much fatter tails; it approaches z as df grow.",
why_wrong="""B) and C) t is closer to z there.
D) The difference shrinks with df.""", hint="When is the SD estimate least reliable?"),
V("ch15-book-03", 2, question="Why does the t approach the z as sample size grows?",
options="""A) The SD estimate gets more precise, adding less uncertainty
B) The data themselves become more normally distributed
C) The sample mean gets closer and closer to zero
D) The null hypothesis becomes more likely to be true""", answer="A",
explanation="With many observations, the estimated SD is close to σ, so the extra uncertainty that fattens t's tails disappears.",
why_wrong="""B) Data keep their shape.
C) and D) Irrelevant to the t's shape.""", hint="What extra uncertainty does the t include?"),

V("ch15-book-04", 1, question="Two studies of beak depth find mean differences of 0.5 mm and 0.6 mm from the null value. The SDs are 0.25 mm and 1.2 mm. Which study has the larger effect size?",
options="""A) The first: d = 2.0 vs d = 0.5
B) The second: its difference is larger
C) They are equal, since the differences are similar
D) Can't tell without the p-values""", answer="A",
explanation="d = difference / SD: 0.5 / 0.25 = 2.0 versus 0.6 / 1.2 = 0.5.",
why_wrong="""B) Raw differences ignore spread.
C) Standardizing by SD makes them very different.
D) Effect size doesn't need p.""", hint="Standardize by the SD."),
V("ch15-book-04", 2, question="Why is effect size standardized by the SD rather than by the SE?",
options="""A) The SD doesn't shrink with sample size
B) The SE is harder to calculate than the SD
C) The SD always gives a larger effect size
D) The SE describes variation among individuals""", answer="A",
explanation="Dividing by the SE would make the 'effect size' grow with n (that's t). The SD keeps it independent of sample size.",
why_wrong="""B) The SE is easy: SD / √n.
C) Dividing by the larger SD gives a smaller value.
D) The SD describes individuals; the SE describes estimates.""", hint="Which one depends on n?"),

V("ch15-book-05", 1, image="ch15-book-hyena-qq.png", question=HYENA + "\n\nThe QQ plot of the nine differences is shown. Which feature would most worry you about the normality assumption?",
options="""A) Points curving far from the line, e.g. a strong bend
B) Points wobbling a little around the line at the ends
C) Points that are exactly on the line from end to end
D) The plot having only nine points""", answer="A",
explanation="A systematic curve suggests skew. Small wobbles are expected, especially with few points.",
why_wrong="""B) Expected with small samples.
C) That would be reassuring.
D) Few points make the plot noisy but aren't a violation.""", hint="Wobble vs systematic curve."),
V("ch15-book-05", 2, image="ch15-book-hyena-qq.png", question=HYENA + "\n\nFor a paired t-test, which values should be checked for normality?",
options="""A) The nine differences
B) The dominant and subordinate values separately
C) The dominant values only
D) All 18 values pooled together""", answer="A",
explanation="A paired t-test is a one-sample t-test on the differences, so it assumes the differences are normal.",
why_wrong="""B), C) and D) The test is on the differences.""", hint="What does the paired t-test analyze?"),

V("ch15-book-06", 1, question=HYENA + "\n\nWhat is the standard error of the mean difference?",
answer=r(0.0954/3,4), explanation="SE = 0.0954 / √9 = 0.0954 / 3 = 0.0318.", hint="SD / √n."),
V("ch15-book-06", 2, question=HYENA + "\n\nWhat is Cohen's d for the difference in giggling?",
answer=r(0.0906/0.0954,2), explanation="d = 0.0906 / 0.0954 = 0.95, a large effect.", hint="Mean difference ÷ SD."),

V("ch15-book-07", 1, question="A 95% CI is calculated as the estimate ± ____ × the standard error.",
options="""A) the critical t value
B) the observed t value
C) Cohen's d
D) the p-value""", answer="A",
explanation="CI = estimate ± critical t × SE.",
why_wrong="""B) The observed t is for the test.
C) and D) Not used to build the CI.""", hint="Which t is a cutoff?"),
V("ch15-book-07", 2, question="Which change would make a 95% confidence interval narrower?",
options="""A) A larger sample size
B) A larger standard deviation
C) Using a 99% interval instead
D) Using fewer degrees of freedom""", answer="A",
explanation="Larger n shrinks the SE (and slightly the critical t).",
why_wrong="""B) Larger SD widens the CI.
C) 99% needs a larger critical value.
D) Fewer df means a larger critical t.""", hint="What shrinks the SE?"),

V("ch15-book-08", 1, question="For a paired study of 12 pairs, which R code gives the critical t value for a two-tailed 95% confidence interval?",
options="""A) qt(0.025, df = 11, lower.tail = FALSE)
B) qt(0.025, df = 12, lower.tail = FALSE)
C) qt(0.05, df = 11, lower.tail = FALSE)
D) pt(0.025, df = 11)""", answer="A",
explanation="2.5% in each tail; df = 12 pairs - 1 = 11.",
why_wrong="""B) df is pairs - 1.
C) That's for a 90% two-tailed interval.
D) pt() returns a probability.""", hint="df = pairs - 1; 2.5% per tail."),
V("ch15-book-08", 2, question="For the nine hyena pairs, which R code gives the critical t value for a two-tailed 99% confidence interval?",
options="""A) qt(0.005, df = 8, lower.tail = FALSE)
B) qt(0.01, df = 8, lower.tail = FALSE)
C) qt(0.005, df = 9, lower.tail = FALSE)
D) qt(0.025, df = 8, lower.tail = FALSE)""", answer="A",
explanation="A 99% two-tailed interval leaves 0.5% in each tail; df = 9 - 1 = 8.",
why_wrong="""B) That puts 1% in each tail (98% CI).
C) df should be 8.
D) That's for 95%.""", hint="Split 1% between two tails."),

V("ch15-book-09", 1, question=HYENA + "\n\nSuppose t had been 1.9, with a critical t value of 2.31 (8 df, α = 0.05). What should we conclude?",
options="""A) Fail to reject: |t| is below the critical value
B) Reject: |t| is close to the critical value
C) Fail to reject, so subordinates and dominants giggle equally
D) Reject, because t is positive in this study""", answer="A",
explanation="|t| < critical t means p > 0.05, so we fail to reject. That doesn't show no difference.",
why_wrong="""B) Close doesn't count.
C) Failing to reject isn't proof of no difference.
D) The sign doesn't decide significance.""", hint="Compare |t| with 2.31."),
V("ch15-book-09", 2, question=HYENA + "\n\nt = 2.85 and p = 0.022. Which statement is correct?",
options="""A) We reject the null, but could be making a type I error
B) We reject the null, which proves subordinates giggle more
C) There's a 2.2% chance subordinates giggle the same amount
D) We fail to reject, because 2.85 is larger than 2.31""", answer="A",
explanation="p < 0.05, so we reject, accepting a chance of a false positive.",
why_wrong="""B) Rejection isn't proof.
C) p isn't the probability the null is true.
D) |t| > critical t means reject.""", hint="What can p < α not guarantee?"),

V("ch15-book-10", 1, question="A study reports p = 0.01. Which interpretation is correct?",
options="""A) If the null were true, 1% of samples would be this extreme or more
B) There is a 1% chance the null hypothesis is true
C) There is a 99% chance the alternative hypothesis is true
D) The effect is large, because p is small""", answer="A",
explanation="p is calculated assuming the null is true.",
why_wrong="""B) and C) p is not a probability about hypotheses.
D) Small p can come from a tiny effect in a big sample.""", hint="What does p assume?"),
V("ch15-book-10", 2, question="Which statement about p-values is FALSE?",
options="""A) A p-value is the probability that the null is true
B) A p-value is calculated assuming the null is true
C) Smaller p-values mean data less compatible with the null
D) A p-value depends on both effect size and sample size""", answer="A",
explanation="p is P(data this extreme | null), not P(null | data).",
why_wrong="B), C) and D) are all true.", hint="Look for the reversed conditional."),

V("ch15-book-11", 1, question="A researcher measured giggling in 10 dominant and 10 subordinate hyenas from different groups. Is a paired t-test appropriate?",
options="""A) Yes
B) No""", answer="B",
explanation="The hyenas aren't in natural pairs (they don't share a group), so a two-sample test is appropriate.",
why_wrong="A) Equal group sizes don't create pairs.", hint="Is there a real basis for pairing?"),
V("ch15-book-11", 2, question="A researcher measured giggling in the same hyenas when they were dominant in one group and subordinate after moving to another. Is a paired t-test appropriate?",
options="""A) Yes
B) No""", answer="A",
explanation="Each hyena is measured twice (repeated measures), so the two measurements form a natural pair.",
why_wrong="B) The same individual measured twice is a natural pair.", hint="Same individual, two conditions."),
]
