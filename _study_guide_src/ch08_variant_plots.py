import numpy as np, matplotlib
from math import comb
matplotlib.use("Agg"); import matplotlib.pyplot as plt
plt.style.use("ggplot"); plt.rcParams.update({"font.size": 12})
rng = np.random.default_rng(2026)
OUT = "bank_images"
GREY = "#595959"


def save(fig, name):
    fig.tight_layout(); fig.savefig(f"{OUT}/{name}", dpi=200); plt.close(fig)


# --- Oak heights: normal population, sampling distributions of the mean for n = 4, 16, 64
MU, SD = 18.0, 4.0
oak = {n: rng.normal(MU, SD, (10000, n)).mean(1) for n in (4, 16, 64)}
fig, axs = plt.subplots(3, 1, figsize=(5.5, 6.5), sharex=True)
for ax, n in zip(axs, (4, 16, 64)):
    ax.hist(oak[n], 60, range=(8, 28), color=GREY, edgecolor="white", lw=.3, weights=np.ones(10000) / 10000)
    ax.axvline(MU, color="red", ls="--"); ax.set_title(f"n: {n}", loc="right", fontsize=12); ax.set_ylabel("proportion")
axs[-1].set_xlabel("sample mean height (m)")
fig.suptitle("Sampling distributions of mean oak height", x=.05, ha="left", fontsize=12)
save(fig, "ch08-var-oak-sampdist.png")
print("oak: P(mean>mu)", {n: round((v > MU).mean(), 3) for n, v in oak.items()},
      "P(|mean-mu|>2)", {n: round((abs(v - MU) > 2).mean(), 3) for n, v in oak.items()},
      "P(mean>20)", {n: round((v > 20).mean(), 4) for n, v in oak.items()},
      "SE", {n: round(v.std(), 3) for n, v in oak.items()})

# --- Proportion of pink flowers, p = 0.30, n = 10, 40, 160 (exact binomial)
P = 0.30
fig, axs = plt.subplots(3, 1, figsize=(5.5, 6.5), sharex=True)
for ax, n in zip(axs, (10, 40, 160)):
    k = np.arange(n + 1); pr = np.array([comb(n, i) * P**i * (1 - P)**(n - i) for i in k])
    ax.bar(k / n, pr, width=min(.8 / n, .03), color=GREY)
    ax.axvline(P, color="red", ls="--"); ax.set_title(f"n: {n}", loc="right", fontsize=12); ax.set_ylabel("probability")
    above = pr[k / n > P].sum(); far = pr[np.abs(k / n - P) > .229].sum()
    print(f"pink n={n}: P(phat>0.3)={above:.3f} P(=0.3)={pr[np.isclose(k / n, P)].sum():.3f} P(|phat-.3|>.229)={far:.3f} SE={np.sqrt(P * (1 - P) / n):.3f} P(phat>=0.45)={pr[k / n >= .45].sum():.4f}")
axs[-1].set_xlabel("sample proportion of pink flowers"); axs[-1].set_xlim(-.02, .9)
fig.suptitle("Sampling distributions of the proportion pink", x=.05, ha="left", fontsize=12)
save(fig, "ch08-var-pink-sampdist.png")

# --- Shape histograms
visits = rng.negative_binomial(1.2, .4, 400)
fig, ax = plt.subplots(figsize=(6, 3.6)); ax.hist(visits, np.arange(-.5, visits.max() + 1.5), color=GREY, edgecolor="white")
ax.set_xlabel("pollinator visits per plant"); ax.set_ylabel("count"); save(fig, "ch08-var-visits-hist.png")
heights = rng.normal(MU, SD, 600)
fig, ax = plt.subplots(figsize=(6, 3.6)); ax.hist(heights, 18, color=GREY, edgecolor="white")
ax.set_xlabel("tree height (m)"); ax.set_ylabel("count"); save(fig, "ch08-var-oak-hist.png")
print("visits mean/median", visits.mean().round(2), np.median(visits), "max", visits.max())

# --- Population vs sampling distribution histograms
ripen = 120 - rng.gamma(2.0, 6.0, 5000)          # left-skewed population: day of fruit ripening
fig, ax = plt.subplots(figsize=(6, 3.6)); ax.hist(ripen, 40, color=GREY, edgecolor="white")
ax.set_xlabel("day of year fruit ripened"); ax.set_ylabel("count"); save(fig, "ch08-var-ripen-pop.png")
print("ripen mean/median", ripen.mean().round(1), np.median(ripen).round(1))
means = rng.choice(ripen, (1000, 40)).mean(1)
fig, ax = plt.subplots(figsize=(6, 3.6)); ax.hist(means, 30, color=GREY, edgecolor="white")
ax.set_xlabel("mean ripening day (samples of 40 plants)"); ax.set_ylabel("count"); save(fig, "ch08-var-ripen-means.png")
print("means range", means.min().round(1), means.max().round(1), "ripen range", ripen.min().round(1), ripen.max().round(1))

# --- Biased vs unbiased estimation
sizes = np.arange(1, 7); pf = np.array([.20, .35, .25, .12, .05, .03]); true = (sizes * pf).sum()
ps = sizes * pf / (sizes * pf).sum()                # a random student comes from a family with prob ∝ size
est_b = rng.choice(sizes, (1000, 40), p=ps).mean(1)
fig, ax = plt.subplots(figsize=(6.5, 3.6)); ax.hist(est_b, 30, range=(1.5, 4), color=GREY, edgecolor="white")
ax.axvline(true, color="red", ls="--", lw=2); ax.set_xlabel("estimated mean children per family"); ax.set_ylabel("count")
save(fig, "ch08-var-family-biased.png")
print("family true", round(true, 2), "estimates mean", est_b.mean().round(2), "min", est_b.min().round(2))
fish = rng.normal(31.0, 6.0, (1000, 25)).mean(1)
fig, ax = plt.subplots(figsize=(6.5, 3.6)); ax.hist(fish, 30, color=GREY, edgecolor="white")
ax.axvline(31.0, color="red", ls="--", lw=2); ax.set_xlabel("estimated mean trout length (cm)"); ax.set_ylabel("count")
save(fig, "ch08-var-trout-unbiased.png")
print("trout est range", fish.min().round(1), fish.max().round(1), "P>31", (fish > 31).mean())
