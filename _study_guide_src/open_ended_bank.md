# Applied Biostats: Open-Ended Discussion Bank (Exam 1, Chapters 0–12)

This is a knowledge base for the tutor bot's discussion mode (Mode 4). Each entry has:

- **Prompt**: what to ask the student, with any data or context they need.
- **Key ideas**: what a complete answer contains. This is for the tutor only. Never paste it to the student.
- **Good enough when**: the bar for saying "this is good enough to submit."
- **What could go wrong**: common misconceptions to listen for, and how to redirect.
- **Hints**: escalating nudges, used one at a time and only after the student has tried.
- **Related**: IDs in `question_bank.csv` that cover the same idea as multiple choice.

Images are in `bank_images/`. Chapter numbers follow the bank: 0 types of variables, 1 getting started, 2 ggplot, 3 reproducible science, 4 data in R, 5 univariate summaries, 6 associations I, 7 associations II, 8 sampling, 9 uncertainty, 10 NHST, 11 shuffling, 12 study design.

---

## Tutor rules (apply to every entry)

1. **Attempt first.** Give no help until the student has tried an answer. If they ask for help first, say something like "I'm happy to help once you give it a first shot."
2. **Don't give the answer.** Guide with questions, examples and hints. Never paste the key ideas.
3. **Be encouraging.** Say specifically what is right in their answer before addressing what's missing.
4. **Hints in order.** Give one hint at a time. Move to the next only if the student is still stuck.
5. **Good enough is good enough.** Once the student has tried more than once and has a complete sentence showing they understand, say: "Great job, this is good enough to submit. I'm here if you want to refine it further." Don't keep pushing for a perfect answer.
6. **Correct misconceptions gently but clearly.** If the student says something wrong (e.g., "there's a 95% chance the true value is in my CI"), don't let it slide. Ask a question that exposes the problem.
7. **No R needed.** Students won't have R on the exam. Don't ask them to run code. Talking about what code *does* is fine.
8. **Stay in scope.** If a student asks something outside these chapters, give a short answer and steer back.

---

## Chapter 0: Types of variables

### O-00-01 · What kind of variable is it, and why does it matter?
- **Source:** new (concept gap)
- **Prompt:** Classify each variable, then explain why the type matters for how you plot and summarize it:
  - ZIP code
  - number of pollinator visits to a plant
  - petal color (pink or white)
  - an ice-cream "deliciousness" rating ("yuck," "meh," "good," "best ever")
  - leaf water content

  In a study of whether petal color affects pollinator visits, which variable is explanatory and which is the response?
- **Key ideas:**
  - **ZIP code:** categorical (nominal). It's a number, but averaging ZIP codes is meaningless.
  - **Visits:** numeric, discrete (a count).
  - **Petal color:** categorical (binary).
  - **Deliciousness:** categorical, ordinal (ordered, but the gaps between levels aren't equal).
  - **Leaf water content:** numeric, continuous.
  - **Why it matters:** type determines sensible summaries (a mean vs proportions), plots (histogram vs bar chart) and analyses.
  - **Explanatory vs response:** petal color is explanatory and visits are the response. The roles come from the *question*, not from the variable itself.
- **Good enough when:** the classifications are mostly right, including that ZIP code is categorical, plus one concrete reason type matters.
- **What could go wrong:**
  - "It's a number, so it's numeric." Ask: what would the average ZIP code mean?
  - Treating the ordinal scale as continuous without noticing the unequal spacing.
  - Thinking explanatory and response are fixed properties of a variable.
- **Hints:**
  1. Would it make sense to add or average these values?
  2. Do the categories have a natural order?
- **Related:** ch00 questions (types of variables)

---

## Chapters 1 and 4: R basics and data in R

Students won't run R on the exam. Some entries ask them to write short code by hand, and others to reason about what code does. The bot should check the *logic*: the right functions, in the right order, applied to the right objects. Exact syntax matters less. Don't nitpick spacing.

### O-01-01 · Write it by hand: vector, sqrt, mean
- **Source:** Intro to R group quiz, Q4
- **Prompt:** Write R code by hand that:
  1. assigns a vector with the values 2, 4, 6 and 8 to the variable `appreciate`;
  2. passes this vector to `sqrt()` to (temporarily) make a new vector of square roots;
  3. pipes that result forward to find its mean.
- **Key ideas:**
  - `appreciate <- c(2, 4, 6, 8)`
  - `sqrt(appreciate) |> mean()`, which gives about 2.17.
  - Also fine: `%>%` instead of `|>`, or `mean(sqrt(appreciate))`. The prompt asks for a pipe, though, so nudge toward it.
- **Good enough when:** the code makes the vector with `c()`, assigns it, takes the square roots *then* the mean, and uses a pipe.
- **What could go wrong:**
  - `appreciate = 2, 4, 6, 8`, with no `c()`.
  - Mean first, then square root: `sqrt(mean(appreciate))` = 2.24, not 2.17. Ask which operation the prompt says to do first.
  - The student saves the square roots back into `appreciate`. The prompt says "temporarily."
- **Hints:**
  1. Break it into steps: make the vector, transform it, summarize it.
  2. Which function combines values into a vector?
- **Related:** ch01-quiz-04 (excluded from the multiple-choice bank)

### O-04-01 · Write it by hand: add a column
- **Source:** Data in R group quiz, Q5B
- **Prompt:** The tibble `score` has columns `game`, `points` and `minutes` (game 1: 24 points in 30 minutes; game 2: 12 points in 20 minutes). Write R code that adds a column `points_per_min`. What values will it contain?
- **Key ideas:**
  - `score |> mutate(points_per_min = points / minutes)`
  - To keep the column: `score <- score |> mutate(...)`.
  - The values are 24/30 = 0.8 and 12/20 = 0.6.
- **Good enough when:** the student uses `mutate()` with points / minutes, and knows that the result needs `<-` to be saved.
- **What could go wrong:**
  - Dividing the wrong way (`minutes / points`).
  - Using `select()`, `filter()` or `summarize()`. Ask which verb makes a new column with one value per row.
  - Assuming `score` now has the column without assigning. Ask what `View(score)` would show.
- **Hints:**
  1. Which dplyr verb adds a column?
  2. "Per minute" means divide by what?
- **Related:** ch04-quiz-06 (excluded from the multiple-choice bank), ch04-quiz-03

### O-01-02 · "But I changed it!" Assignment and the R environment
- **Source:** new (concept gap; ties to ch01-quiz-02, ch04-quiz-03, practice exam Q27)
- **Prompt:**
  - (a) You run `clean_names(iris)`. The console shows nicely renamed columns, but `View(iris)` still shows the old names. Why?
  - (b) Your script worked all afternoon. You close R, reopen it, run the script from the top, and get `object 'gc_rils' not found`. What probably happened, and how do you prevent it?
- **Key ideas:**
  - **(a)** Functions return a *new* object and don't change the original. Without `<-`, the result is printed and then lost. Fix: `iris <- clean_names(iris)`, or better, a new name.
  - **(b)** The R environment remembers objects made by running lines out of order or in the console. In a fresh session, a line that uses `gc_rils` before it's created fails. Fix: order the script so each object is created before it's used, and regularly restart R and run the whole script top to bottom.
- **Good enough when:** the student explains that printing ≠ saving (needs `<-`), and that a script must run top to bottom in a fresh session.
- **What could go wrong:**
  - "R is buggy," or "the file changed."
  - The student thinks saving the script saves the objects.
- **Hints:**
  1. Where did the output of `clean_names()` go?
  2. When you reopen R, what's in your environment?
- **Related:** ch01-quiz-02, ch04-quiz-03, ch04-hw-03

### O-01-03 · Reading an error: the `filter()` mystery
- **Source:** new (concept gap; ties to ch04-hw-07, ch04-book-10, practice exam Q22)
- **Prompt:** The column `location` definitely exists, and dplyr is loaded, yet `ril_data |> filter(location == "SR")` gives `object 'location' not found`. What's going on, and how would you fix it? More generally, how do you approach an R error you don't understand?
- **Key ideas:**
  - Two packages define a `filter()`: dplyr's and stats'. R used `stats::filter()`, which doesn't look inside the data for column names.
  - **Fixes:** `dplyr::filter()`, or `conflicts_prefer(dplyr::filter)`.
  - **General strategy:**
    - Read the error literally (what object is missing?).
    - Check spelling and case.
    - Check that the package is loaded and that you're using the function you think you are.
    - Check that the object exists, and in what order things ran.
    - Search the error message.
- **Good enough when:** the student identifies the function-name conflict and one fix, plus at least two general debugging steps.
- **What could go wrong:**
  - The student keeps re-checking the column name (which is fine).
  - "Reinstall dplyr."
- **Hints:**
  1. Could two different functions be called `filter`?
  2. How could you tell R exactly which package's function to use?
- **Related:** ch04-hw-07, ch04-book-10, ch04-quiz-01, ch04-quiz-02

### O-04-02 · What is tidy data, and why bother?
- **Source:** new (concept gap; ties to practice exam Q25–26, ch04-hw-01)
- **Prompt:** Hemoglobin was measured in people from four populations. Table B has one column per population (USA, Andes, Ethiopia, Tibet), with values stacked under each. Is it tidy? What are the rules of tidy data, and why do they matter?
- **Key ideas:**
  - **Tidy data:**
    - Each variable is a column.
    - Each observation is a row.
    - Each value is a cell.
  - **Table B is not tidy.** Population (a variable) is spread across the column names, and each row combines unrelated people from different populations, implying a pairing that doesn't exist.
  - **The tidy version** has two columns: `population` and `hemoglobin`.
  - **Why it matters:** tools like ggplot and dplyr expect tidy data. It avoids implied pairings, and it makes grouping and plotting straightforward.
- **Good enough when:** the student states the rules, identifies the problem in Table B, and gives one reason it matters.
- **What could go wrong:**
  - "Wide tables are easier to read, so they're tidy."
  - The student focuses on cosmetics (rounding, column order).
- **Hints:**
  1. What are the variables here? Is each one in its own column?
  2. What does it mean that USA and Tibet values share a row?
- **Related:** ch04-hw-01, ch04-hw-02, ch04-quiz-05, ch04-book-01

---

## Chapter 2: Data visualization

### O-02-01 · Why make a plot?
- **Source:** Chime In (ggplot)
- **Prompt:** What are good reasons to make a plot?
- **Key ideas:**
  - To explore the data and see patterns you didn't expect.
  - To check for errors, outliers and impossible values.
  - To see the shape of a distribution before choosing summaries.
  - To avoid being fooled by summary statistics (very different datasets can share the same means, SDs and correlations, e.g., the "datasaurus").
  - To communicate results.
- **Good enough when:** the student gives at least two distinct reasons, including one about *exploring or checking* (not only communicating).
- **What could go wrong:**
  - The student lists only "to show results to others." Ask what plotting could do for *them* before they analyze anything.
  - The student says "plots are prettier than tables." Push toward what a plot reveals that a summary hides.
- **Hints:**
  1. Think about two moments: before you analyze the data, and when you share results.
  2. Could two datasets have the same mean and SD but look completely different?
- **Related:** ch02-chimein-01

### O-02-02 · Which plot do you prefer, and why?
- **Source:** Chime In (ggplot); originally a preference poll
- **Prompt:** Show `ch02-chimein-02.png` (small multiples, layouts A and B). Which layout do you prefer for comparing the groups, and why?
- **Key ideas:**
  - There's no single right answer. A strong answer ties the choice to the **comparison the reader needs to make**.
  - Panels that share an axis let you compare positions directly.
  - Stacking panels vertically makes it easy to compare x-values; placing them side by side makes it easy to compare y-values.
  - Good answers mention shared scales, alignment, and what the eye compares.
- **Good enough when:** the student names a preference *and* links it to a specific comparison the layout makes easier.
- **What could go wrong:**
  - "It looks nicer." Ask: nicer for *what* comparison?
  - The student claims the panels have different scales when they share one. Have them check the axes.
- **Hints:**
  1. What is the main comparison a reader would want to make here?
  2. In which layout are the things you'd compare lined up along the same axis?
- **Related:** ch02-chimein-02

### O-02-03 · Matching the plot to the variables
- **Source:** new (concept gap)
- **Prompt:** For each question, choose a good plot and explain why it fits:
  1. What's the distribution of petal area?
  2. Does petal area differ between pink and white flowers?
  3. Does survival differ by passenger class (Titanic)?
  4. Is petal area associated with proportion hybrid seed?

  What's one principle that applies to all four?
- **Key ideas:**
  1. One continuous variable: a histogram or density plot.
  2. Categorical × continuous: jittered points with a boxplot or means ± CI, or faceted histograms.
  3. Two categorical: a bar chart. Use `fill` to compare proportions, `dodge` to compare counts.
  4. Two continuous: a scatterplot (optionally with a trend line).
  - **General principles:** show the data, make the comparison of interest easy, and match the plot to the variable types.
- **Good enough when:** at least three of the four choices are sensible, with reasons tied to variable types.
- **What could go wrong:**
  - Bar charts of means that hide the data (or bars that *sum* values; see ch02-quiz-03).
  - A scatterplot with a categorical x-axis and no jitter, so points overplot.
- **Hints:**
  1. What type is each variable: categorical or numeric?
- **Related:** ch02 questions, ch06-hw-01, ch06-hw-06, ch06-book-06

### O-02-04 · How can a plot mislead?
- **Source:** new (concept gap; ties to the facet question in the ggplot Chime In and ch02-quiz-03)
- **Prompt:** Describe three ways a plot can mislead its reader (even by accident), and how you'd fix each.
- **Key ideas:**
  - **Inconsistent or free axes across panels** make different groups look similar or different. Fix: share scales.
  - **Truncated or odd axis ranges** exaggerate differences.
  - **Hiding the data:** bars of means with no spread, or `geom_col()` summing values instead of showing means. Fix: show the points, and the uncertainty.
  - **Overplotting**, or jitter so wide that groups blur.
  - **Unlabeled error bars** (SD vs SE vs CI).
  - **Colors or ordering** that suggest a pattern that isn't there.
- **Good enough when:** the student names three distinct problems, each with a fix.
- **What could go wrong:**
  - Purely aesthetic complaints ("ugly colors"). Push toward what the reader would *conclude wrongly*.
- **Hints:**
  1. If two panels have different y-axis ranges, what might a reader assume?
  2. What do error bars show if no one says what they are?
- **Related:** ch02-chimein-04, ch02-quiz-03, ch06-hw-06

---

## Chapter 3: Reproducible science

### O-03-01 · What makes an analysis reproducible?
- **Source:** new (concept gap; ties to the reproducibility homework, book and Chime In)
- **Prompt:** A labmate sends you their data and R script, and you can't get it to run or match their results. List the practices that would have prevented this, and explain why each matters.
- **Key ideas:**
  - **Scripts, not clicks:** analysis lives in a script, not the console or spreadsheet edits.
  - **Load everything at the top:** load packages before use, and read data before using it.
  - **Run top to bottom in a fresh session.**
  - **Relative paths and projects,** not `setwd("~/my/computer")`. Leave out interactive clutter like `View()` and `install.packages()`.
  - **Raw data is never edited by hand.** All cleaning is in code.
  - **Comments** explain *why*.
  - **A data dictionary** (units, codes, formats), with no implied values ("blank = same as above").
  - **Version control or dated versions.**
- **Good enough when:** the student gives four or more distinct practices, each with a reason.
- **What could go wrong:**
  - Only "add comments." That's useful, but it doesn't make code run.
  - The student thinks absolute paths are more reliable.
- **Hints:**
  1. What on *your* computer won't exist on theirs?
  2. If you restarted R, would the script still work?
- **Related:** ch03 questions, O-01-02

### O-03-02 · Why can't we just drop the missing values?
- **Source:** new (concept gap; ties to ch03-chimein-02, insulin "below curve")
- **Prompt:** In a glucose tolerance dataset, some insulin values are NA with the note "insulin below curve" (too low to measure). What goes wrong if we just drop the NAs before calculating mean insulin? More generally, when is ignoring missing data dangerous, and what should you record when data are missing?
- **Key ideas:**
  - The values are missing *because* they were low (missing not at random).
  - Dropping them **overestimates** mean insulin: it's bias, not just a smaller sample.
  - Ignoring missing data is dangerous whenever the *reason* for missingness relates to the value or to the treatment.
  - **What to record:** why each value is missing (detection limit, died, lost sample), and the detection limit itself.
  - Options include treating the values as "below X" or running sensitivity analyses.
- **Good enough when:** the student explains the direction of the bias and why the missingness isn't random.
- **What could go wrong:**
  - "It just lowers the sample size." Push: which values are being removed?
- **Hints:**
  1. Are the missing values random, or are they a particular kind of value?
- **Related:** ch03-chimein-02, ch03-book-01, ch03-book-02

---

## Chapter 5: Univariate summaries

### O-05-01 · Can you estimate the mean from a boxplot?
- **Source:** discussion arising from Canvas quiz, group quiz and book Q6 (Lake Huron)
- **Prompt:** Show `ch05-quiz-boxplot.png` (or `ch05-gquiz-boxplot.png`). Can you estimate the mean from this boxplot? What can and can't a boxplot tell you?
- **Key ideas:**
  - A boxplot shows five numbers (min, Q1, median, Q3, max) plus outliers. It does **not** show the mean, mode or variance.
  - Skew tells you the mean's likely *direction*: a long upper tail or high outliers pull the mean above the median, and a long lower tail pulls it below.
  - So you can say "probably a bit above the median," but you can't read off a value.
- **Good enough when:** the student says the mean isn't shown, *and* reasons about which side of the median it is probably on, using skew.
- **What could go wrong:**
  - The student reads the median line as the mean. Ask what the thick line represents.
  - The student says "you can't know anything about the mean." Push them to use the skew.
  - The student confuses IQR with range. Ask which part of the plot each one spans.
- **Hints:**
  1. List the five numbers a boxplot shows. Is the mean one of them?
  2. If the upper whisker is much longer, which way would extreme values pull the mean?
- **Related:** ch05-quiz-03, ch05-gquiz-04, ch05-book-07

### O-05-02 · Why standardize by the mean? (coefficient of variation)
- **Source:** Book, Summarizing summaries Q8 (originally had a dedicated chatbot)
- **Prompt:** Why is it important to standardize by the mean when comparing variability between variables? (Context: proportion hybrid seed across sites has SD ≈ 0.085 and mean 0.15; RIL petal area has SD ≈ 14.3 mm² and mean 62 mm².)
- **Key ideas:**
  - The SD depends on the units and scale of measurement. Bigger numbers tend to vary by bigger amounts.
  - Dividing by the mean (CV = SD / mean) gives a unitless measure of *relative* variability that can be compared across traits.
  - Here: CV(hybrid) ≈ 0.57 and CV(petal area) ≈ 0.23. Hybrid proportion is about twice as variable relative to its mean, even though its raw SD is roughly 170 times smaller.
- **Good enough when:** the student explains that raw SDs depend on scale or units, so you must divide by the mean to compare fairly.
- **What could go wrong:**
  - "Petal area is more variable because its SD is bigger." Ask what the SD of petal area would be if it were measured in cm² instead of mm² (100 times smaller).
  - "You can't compare different traits at all." The CV is exactly what makes that comparison possible.
- **Hints:**
  1. What would happen to the SD of hybrid seed if we reported percent instead of proportion?
  2. What happens to the SD of petal area if we switch from mm² to cm²? Did the biology change?
  3. What quantity could you divide by so that the units cancel?
- **Related:** ch05-book-10, ch05-book-11, ch05-book-06, ch07-gquiz-02

### O-05-03 · Debug the iris variance code
- **Source:** Summarizing data group quiz, Q9 ("circle the mistakes, fix them, and explain")
- **Prompt:** This code was meant to estimate the variance in *Iris setosa* sepal length, but it doesn't work. What went wrong, and how would you fix it?
  ```
  iris |>
    dplyr::summarize(var_sl = var(Sepal.Length)) |>
    dplyr::filter(Species =  setosa)
  ```
- **Key ideas:**
  1. **Order:** `summarize()` collapses the data to one row with only `var_sl`, so there is no `Species` left to filter on. Even if the code ran, the variance would be for all species. Filter first.
  2. Use `==` (a test of equality), not `=`.
  3. `"setosa"` needs quotes because it is a value, not an object.
  - Fixed version: `iris |> filter(Species == "setosa") |> summarize(var_sl = var(Sepal.Length))`
- **Good enough when:** the student identifies the order problem plus at least one of `==` or the quotes. Fully correct means all three.
- **What could go wrong:**
  - The student fixes the syntax but keeps summarize before filter. Ask what columns exist after `summarize()`.
  - The student thinks `dplyr::` is the problem. It's optional but harmless.
- **Hints:**
  1. Read the pipe one step at a time. After `summarize()`, what does the data look like?
  2. What's the difference between `=` and `==` in R?
  3. Is `setosa` the name of an object, or a value in a column?
- **Related:** ch05-gquiz-06

### O-05-04 · Variance step by step (pseudocode)
- **Source:** Summarizing data group quiz, extra credit (originally "write R code without var()"; here as plain-language steps)
- **Prompt:** Without using a built-in variance function, describe step by step how you would calculate the sample variance of a set of numbers. Then explain why we divide by n − 1.
- **Key ideas:**
  1. Find the mean.
  2. Subtract the mean from each value (the deviations).
  3. Square each deviation.
  4. Add up the squares (the sum of squares, SS).
  5. Divide by n − 1.
  - **Why n − 1:** the mean was estimated from the same data, so the deviations are slightly too small on average. Dividing by n − 1 corrects that (Bessel's correction).
  - The SD is the square root of the variance.
- **Good enough when:** the steps are in the right order, including squaring and dividing by n − 1, with a reasonable sentence on why n − 1.
- **What could go wrong:**
  - The student forgets to square. Deviations always sum to 0, so ask what happens if you just add them.
  - The student divides by n. Ask what we used to compute the deviations, and whether that was the true mean or an estimate.
  - The student takes the square root and calls it the variance.
- **Hints:**
  1. What's the first number you need before you can measure "distance from the center"?
  2. Try adding up the raw deviations for 1, 2 and 3. What do you get? Why is that a problem?
- **Related:** ch05-quiz-04, ch05-quiz-05, ch05-gquiz-05

### O-05-05 · Choosing summaries for skewed data
- **Source:** new (concept gap; ties to practice exam Q20 and the shape questions)
- **Prompt:** Pollinator visits per plant are strongly right-skewed: most plants get 0 visits and a few get many. Which summaries of center and spread would you report, and why? Would a log transformation help? What would you do if the data were bimodal?
- **Key ideas:**
  - With a long right tail, **mean > median**. The median and IQR describe a "typical" plant better.
  - The mean is still meaningful for some questions, such as total visits.
  - A log transform (log(x + 1) with zeros) can make right-skewed data more symmetric.
  - **Bimodal data:** no single center describes it well. Look for two groups and summarize each.
  - **Always plot first.**
  - The SD can still be calculated, but it's less descriptive here.
- **Good enough when:** the student gets the mean–median direction right and justifies the median/IQR, plus one point about transforming or bimodality.
- **What could go wrong:**
  - "You can't calculate an SD for skewed data."
  - "Median > mean for right skew."
- **Hints:**
  1. Which way do a few huge values pull the mean?
- **Related:** ch05-quiz-01, ch05-book-01, ch05-gquiz-07, ch05-book-03

### O-05-06 · What does the standard deviation really tell you?
- **Source:** new (concept gap; ties to practice exam Q22)
- **Prompt:** In plain words, what does a standard deviation tell you about a dataset? Why do we square deviations when computing variance, and why do we usually report the SD rather than the variance?
- **Key ideas:**
  - The SD is roughly how far a typical value is from the mean.
  - **Why square:**
    - Raw deviations always sum to 0, and squaring makes them all positive.
    - Squaring also gives large deviations more weight.
  - **Why report the SD:** the variance is in squared units (e.g., g²); taking the square root puts the SD back in the original units.
  - The SD describes spread among individuals; it does **not** shrink as the sample grows.
- **Good enough when:** the student gives a plain-language meaning, plus a reason for squaring and a reason for reporting the SD.
- **What could go wrong:**
  - "SD = range."
  - "SD is how far the mean is from the truth." That's the SE.
- **Hints:**
  1. What units is variance in, if the data are in grams?
- **Related:** ch05-gquiz-02, ch05-quiz-05, O-05-04, O-08-07

---

## Chapters 6–7: Associations

### O-07-01 · Variance vs covariance
- **Source:** Apples and oranges group quiz, Q1
- **Prompt:** Compare the equations for variance and covariance. How are they similar? How do they differ?
  - Var(X) = Σ(xᵢ − x̄)² / (n − 1)
  - Cov(X, Y) = Σ(xᵢ − x̄)(yᵢ − ȳ) / (n − 1)
- **Key ideas:**
  - **Similar:** both sum products of deviations from the mean and divide by n − 1.
  - **Different:** variance multiplies a variable's deviation by *itself*, while covariance multiplies the deviations of *two* variables.
  - Therefore variance is never negative, but covariance can be negative (when one goes up and the other goes down).
  - Variance is the covariance of a variable with itself: Cov(X, X) = Var(X).
- **Good enough when:** the student gives one similarity and one difference, ideally noting that covariance can be negative.
- **What could go wrong:**
  - "Covariance is the square root of variance." That's the SD.
  - "They use different denominators." Both use n − 1.
- **Hints:**
  1. What would you get if you plugged X in for Y in the covariance formula?
  2. Can (xᵢ − x̄)² ever be negative? Can (xᵢ − x̄)(yᵢ − ȳ)?
- **Related:** ch07-gquiz-01

### O-07-02 · Which statistic for comparing variability: apples vs oranges?
- **Source:** Apples and oranges group quiz, Q2 (review of chapter 5)
- **Prompt:** You want to compare the variability in fruit area between apples and oranges. Which statistic should you use, and why?
- **Key ideas:**
  - Use the **coefficient of variation** (SD / mean).
  - The fruits differ in average size, and bigger things tend to vary by bigger absolute amounts.
  - The CV compares *relative* variability.
- **Good enough when:** the student names the CV and explains that it accounts for different means.
- **What could go wrong:**
  - The student picks the variance or SD. Ask whether the bigger fruit would look more variable just because it's bigger.
  - The student picks covariance or correlation. Apples and oranges aren't paired, so there's no "together" to measure.
- **Hints:**
  1. If oranges were twice as big on average, would you expect their SD to be bigger even if they were equally variable?
- **Related:** ch07-gquiz-02, O-05-02

### O-07-03 · Covariance or correlation for comparing strength?
- **Source:** Apples and oranges group quiz, Q3
- **Prompt:** You want to compare how strongly fruit size is related to cost per pound in apples vs oranges. Should you use covariance or correlation? Why?
- **Key ideas:**
  - Use **correlation**.
  - Covariance depends on the units and spreads of both variables, so a bigger covariance might just mean more variable sizes or prices.
  - Correlation = Cov / (SD_x × SD_y) is standardized (unitless, between −1 and 1), so strength can be compared across groups.
- **Good enough when:** the student picks correlation and mentions standardization, units, or scale.
- **What could go wrong:**
  - "Covariance, because it keeps the units." That's exactly the problem.
  - The student thinks correlation can't be negative.
- **Hints:**
  1. What would happen to the covariance if you measured size in cm instead of inches? What about the correlation?
- **Related:** ch07-gquiz-03

### O-07-04 · Inches and feet: covariance and correlation
- **Source:** Apples and oranges group quiz, Q6 ("explain and show math")
- **Prompt:** Height in inches and height in feet are perfectly linearly related (inches = 12 × feet). What is the covariance between them? What is the correlation? Explain and show math.
- **Key ideas:**
  - **Covariance:** Cov(12F, F) = 12 · Cov(F, F) = 12 · Var(F). There's no fixed number; it depends on how variable heights are and on the units.
  - **Correlation:** SD_inches = 12 · SD_feet, so r = 12 · Var(F) / (12 · SD_F · SD_F) = 1.
  - Any perfect positive linear relationship has r = 1, whatever the units.
- **Good enough when:** the student shows r = 1 with some reasoning, and recognizes that the covariance isn't a single fixed number (it's 12 × the variance in feet).
- **What could go wrong:**
  - The student says "covariance = 1." Ask whether covariance is standardized.
  - The student says "correlation = 12." Correlation can't exceed 1.
  - The student is stuck on the algebra. Try a concrete example: three people at 5, 6 and 7 feet.
- **Hints:**
  1. Try three people: 5, 6 and 7 feet (60, 72 and 84 inches). Compute both SDs. How are they related?
  2. What is Cov(F, F)?
- **Related:** ch07-gquiz-06

### O-07-05 · Buy-one-get-one covariance (show work)
- **Source:** Apples and oranges group quiz, Q4
- **Prompt:** A store had a buy-one-get-one-free sale on apples and oranges. Half of all fruit sold were apples and half were oranges. Of the pairs sold, one third were two oranges. Code orange = 1 and apple = 0. What is the covariance between the two fruits in a pair (ignoring Bessel's correction)? Explain what it means.
- **Key ideas:**
  - Cov = P(both orange) − P(orange) × P(orange) = 1/3 − 1/4 = **1/12 ≈ 0.083**.
  - It's positive: people who pick one orange tend to pick another, compared with independence (which would give 1/4 two-orange pairs).
- **Good enough when:** the student gets 1/12 (or about 0.083) and says it's positive because two-orange pairs are more common than independence predicts.
- **What could go wrong:**
  - The student answers 1/3. That's the joint proportion, not the covariance.
  - The student doesn't know where 1/4 comes from. Walk through the multiplication rule.
- **Hints:**
  1. If the two fruits were chosen independently, what fraction of pairs would be two oranges?
  2. Covariance for 0/1 variables = observed joint proportion − expected joint proportion.
- **Related:** ch07-gquiz-04, ch07-hw-02, ch07-book-03, ch07-book-04
- **Note:** check that the E[XY] − E[X]E[Y] framing matches how the course presents covariance for binary variables.

### O-06-01 · Difference in means vs Cohen's d
- **Source:** Apples and oranges group quiz, Q5 (two parts)
- **Prompt:** You want to describe the difference in mean fruit area between apples and oranges. (a) When and why would you report the difference in conditional means? (b) When and why would you report Cohen's d?
- **Key ideas:**
  - **(a) Raw difference:** it's in real units (e.g., "oranges are 12 cm² larger"), so it's best when the units are meaningful to readers.
  - **(b) Cohen's d:** difference / pooled SD, a unitless effect size relative to the spread. It's best for comparing across traits or studies measured in different units, or for asking "is this difference big compared with the natural variation?"
  - Good answers note that reporting both is often ideal.
- **Good enough when:** the student gives one reasonable use for each, mentioning units for the raw difference and standardizing by variability for d.
- **What could go wrong:**
  - "Cohen's d is always better." Raw differences are often more interpretable.
  - The student thinks d tells you whether the difference is "real" or significant. It's a size, not a test.
- **Hints:**
  1. Which one has units? Which one would let you compare fruit area with fruit weight?
- **Related:** ch06-gquiz-05, ch06-hw-04, ch06-book-04

### O-07-06 · Chocolate and Nobel prizes: what's going on?
- **Source:** discussion built from the Associations I and II homework (Nobel data)
- **Prompt:** Across 27 countries, chocolate consumption and number of Nobel laureates have r ≈ 0.36. Without the USA, UK and Germany, r ≈ −0.06. Show `ch07-hw-choc-nobel-scatter.png`. Does chocolate make people smarter? What else could explain this pattern?
- **Key ideas:**
  - **Correlation ≠ causation.** This is observational, country-level data.
  - **Confounding:** wealth and population size plausibly drive both chocolate buying and Nobel counts.
  - **Outliers:** three countries create the whole correlation.
  - **Raw counts:** laureate numbers aren't per capita, so big countries dominate.
  - **Ecological fallacy:** country-level patterns say little about individuals.
- **Good enough when:** the student rejects the causal claim *and* gives at least one specific alternative (a confounder, the outliers, or per-capita scaling).
- **What could go wrong:**
  - "It's just correlation, so it means nothing." Push: the association exists; the question is why.
  - The student wants to delete the outliers. They're real data; you can report results both with and without them.
- **Hints:**
  1. Look at the plot. Where would the line go without the three labeled countries?
  2. What kinds of countries can afford both lots of chocolate and big research universities?
- **Related:** ch06-hw-05, ch07-hw-03, ch07-hw-04, ch07-hw-06

### O-06-02 · Counts vs conditional proportions (and what independence looks like)
- **Source:** new (concept gap; ties to the Titanic and Nobel questions)
- **Prompt:** Among adult male Titanic passengers and crew:
  - 1st class: 57 survived, 118 died.
  - Crew: 192 survived, 670 died.

  A friend says, "More crew survived than first-class passengers, so it was safer to be crew." What's wrong with this? What would the numbers look like if survival were independent of class?
- **Key ideas:**
  - Raw counts reflect group sizes (862 crew vs 175 first class).
  - Compare **conditional proportions** instead: P(survive | 1st) = 57/175 = 0.33 and P(survive | crew) = 192/862 = 0.22. First class was safer.
  - **Independence** would mean the conditional proportions are equal, and the joint proportion equals the product of the marginals: P(1st and survived) = P(1st) × P(survived).
- **Good enough when:** the student computes or describes the conditional proportions, reaches the right conclusion, and describes independence as equal conditional proportions.
- **What could go wrong:**
  - Using joint proportions (57/1037) to compare groups.
  - Thinking a small joint probability means "no association."
- **Hints:**
  1. Out of all first-class men, what fraction survived? Out of all crew?
- **Related:** ch06-book-02, ch06-book-03, ch06-hw-02, ch06-hw-03, ch07-hw-01

### O-07-07 · What correlation does and doesn't tell you
- **Source:** new (concept gap; ties to the four-panel plots)
- **Prompt:** Show `ch07-hw-fourpanels.png`. In panel b, y is a perfect wave-shaped function of x, yet r ≈ 0. Explain how that's possible. What does a correlation coefficient tell you, and what doesn't it tell you?
- **Key ideas:**
  - **r measures only *linear* association** (direction and tightness around a straight line).
  - r ≈ 0 does not mean "no relationship": curved relationships can have r ≈ 0.
  - **r doesn't give the slope.** A steep and a shallow line can both have r = 0.9.
  - **r is sensitive to outliers** (e.g., the chocolate–Nobel data).
  - **r doesn't imply causation.**
  - **Always plot.**
- **Good enough when:** the student explains "linear only," plus two other things r doesn't tell you.
- **What could go wrong:**
  - "r = 0 means x and y are unrelated."
  - "A bigger r means a steeper slope."
- **Hints:**
  1. If you fit a straight line through panel b, would it tilt?
- **Related:** ch07-hw-05, ch07-book-05, ch07-hw-06

---

## Chapter 8: Sampling

### O-08-01 · How would you find the standard error of red crayons?
- **Source:** Sampling group quiz, Q7
- **Prompt:** Describe how you would find the standard error of the proportion of red crayons in a sample of size ten from the bin.
- **Key ideas:**
  - Build the sampling distribution: draw a sample of 10 (returning crayons between samples), record the proportion red, and repeat many times.
  - The SE is the **standard deviation of those proportions**.
  - (Advanced, optional: approximate it with √(p(1 − p)/n).)
- **Good enough when:** the student describes many samples of the same size, one proportion per sample, and the SD of those proportions.
- **What could go wrong:**
  - The student takes the SD of the colors within one sample. That's spread among individuals, not estimates.
  - The student counts the whole bin. That gives the parameter, with no uncertainty to describe.
  - The student changes the sample size between repeats. The SE is for n = 10 specifically.
- **Hints:**
  1. The SE is the SD of what?
  2. How would you get many estimates instead of one?
- **Related:** ch08-gquiz-07

### O-08-02 · Gene lengths: how did I get it so wrong?
- **Source:** Book, Sampling summary Q6 (originally had a dedicated chatbot)
- **Prompt:** I estimated mean human gene length by picking random nucleotides from the genome and recording the length of the gene each one landed in, until I had 50 genes. I repeated this 1000 times. Show `ch08-book-biased-sampdist.png`: every estimate is far above the true mean (2.62 kb). Explain why, and how you would fix it.
- **Key ideas:**
  - **Size-biased sampling:** long genes contain more nucleotides, so they're more likely to be hit. A 20 kb gene is ten times as likely to be picked as a 2 kb gene.
  - That's **sampling bias**, not sampling error: all 1000 estimates are off in the same direction.
  - **Fix:** sample genes from a list of all genes, so each gene has an equal chance.
  - A bigger sample would *not* help.
- **Good enough when:** the student explains that longer genes are more likely to be chosen, and proposes giving each gene an equal chance.
- **What could go wrong:**
  - "The sample was too small." Ask whether a bigger sample, drawn the same way, would be centered on the truth.
  - "Bad luck." All 1000 repeats were too high, so it isn't luck.
- **Hints:**
  1. Does every gene have the same chance of being picked?
  2. Imagine a 1 kb gene and a 100 kb gene. If you throw a dart at the genome, which are you more likely to hit?
- **Related:** ch08-book-03, ch08-book-04, ch08-hw-07

### O-08-03 · Old Faithful: random eruptions vs random times
- **Source:** Sampling homework Q7 (MC + "why")
- **Prompt:** To estimate the mean eruption length at Old Faithful, why is it better to randomly select *eruptions* than to randomly select *times of day* and measure the current or next eruption? (Hint: eruption length and waiting time are positively correlated.)
- **Key ideas:**
  - Random times are more likely to land in long gaps between eruptions, and long gaps go with long eruptions.
  - So random times oversample long eruptions: **size-biased sampling**.
  - Random eruptions give each eruption an equal chance, so the estimate is unbiased.
  - It's the same logic as the gene-length example (O-08-02).
- **Good enough when:** the student links long gaps → more likely to be sampled → long eruptions, and calls it bias.
- **What could go wrong:**
  - "Times of day are more random." Both methods are random, but not every eruption has an equal chance under the second one.
- **Hints:**
  1. If you show up at a random time, are you more likely to arrive during a short gap or a long gap?
- **Related:** ch08-hw-07

### O-08-04 · The rainbow crayon bin: biased or non-independent? (debated)
- **Source:** Sampling group quiz, Q6. Excluded from the multiple-choice bank because the key is debatable, which makes it good for discussion.
- **Prompt:** If the crayons were arranged by color like a rainbow and you grabbed one handful from one place, what kind of sample would you have? Is it biased, non-independent, or both? Defend your answer.
- **Key ideas:**
  - **Class key: non-independent.** Neighboring crayons are similar colors, so each extra crayon adds little new information.
  - If the grab spot is random, the sampling distribution is still **centered on the truth**, just much wider. So it's not biased, but the error is badly inflated.
  - **Biased** is defensible if you always reach into the same spot.
  - Strong answers distinguish a *shifted center* (bias) from *clumped, redundant observations* (non-independence).
- **Good enough when:** the student makes a clear argument that uses the center-vs-spread distinction, whichever answer they pick.
- **What could go wrong:**
  - The student says "biased" without considering where the hand goes. Ask: if you grabbed from a random spot each time and averaged many handfuls, where would the average land?
- **Hints:**
  1. Over many handfuls from random spots, would the average proportion red be too high, too low, or about right?
  2. How similar are crayons that sit next to each other?
- **Related:** ch08-gquiz-06 (excluded from the bank)

### O-08-05 · Choosing crayons you like: bias, non-independence, or both? (debated)
- **Source:** Sampling group quiz, Q3. Excluded from the multiple-choice bank; the class settled on "both."
- **Prompt:** Instead of picking crayons at random, everyone picked crayons they liked. What could go wrong with the estimates?
- **Key ideas:**
  - **Bias:** preferred colors get a better chance of being picked, which shifts the estimate.
  - **Non-independence:** classmates share color preferences, so their samples resemble each other.
  - Class key: **both**.
- **Good enough when:** the student names bias with a reason and at least considers non-independence.
- **What could go wrong:**
  - The student names only one, with no reason. Ask about the other.
- **Hints:**
  1. Does every crayon have an equal chance of being picked?
  2. If your whole table loves blue, are your samples independent of each other?
- **Related:** ch08-gquiz-03 (excluded from the bank)

### O-08-06 · Sampling error vs sampling bias
- **Source:** new (concept gap; the core idea behind many chapter 8 questions)
- **Prompt:** Explain the difference between sampling error and sampling bias, with a biological example of each. Which one does a bigger sample fix? Which one does random sampling fix?
- **Key ideas:**
  - **Sampling error** is chance differences between an estimate and the parameter.
    - It's unavoidable, and it goes in both directions.
    - It shrinks with larger n.
  - **Sampling bias** is a systematic difference, from a non-representative sampling process.
    - Examples: the first turtles to reach the food are the fast ones; random nucleotides oversample long genes.
    - A bigger biased sample is just *precisely wrong*.
  - **Random sampling** guards against bias. **Large n** shrinks error.
  - In a sampling distribution, bias shifts the *center* and error sets the *spread*.
- **Good enough when:** the student gives clear definitions and an example of each, and correctly says which fix goes with which.
- **What could go wrong:**
  - "A bigger sample removes bias."
  - "Random sampling removes sampling error."
- **Hints:**
  1. If you repeated the study many times, would the estimates be scattered around the truth, or all off in one direction?
- **Related:** ch08-hw-05, ch08-hw-10, ch08-hw-11, ch08-book-03, ch08-gquiz-01

### O-08-07 · Standard deviation vs standard error
- **Source:** new (concept gap; ties to practice exam Q22–23 and many SD/SE items)
- **Prompt:** Explain the difference between the standard deviation and the standard error to a friend who missed class. If you increased your sample size from 10 to 1000, what would happen to each, and why?
- **Key ideas:**
  - **SD:** spread of *individuals* around the mean.
    - With more data it gets *more precisely estimated*, but it doesn't shrink (it estimates a fixed population property).
  - **SE:** spread of *estimates* (e.g., sample means) around the parameter, i.e., the SD of the sampling distribution.
    - SE ≈ SD/√n, so it shrinks as n grows.
  - **Analogy:** the SD is about how different people are; the SE is about how much your average would change if you resampled.
- **Good enough when:** the student gives correct definitions and the correct behavior of each as n grows, with a reason.
- **What could go wrong:**
  - "Both shrink with n."
  - "SE is the error in measuring individuals."
- **Hints:**
  1. Would people's heights become less variable if you measured more people?
- **Related:** ch08-hw-04, ch08-book-01, ch09-chime-04, ch09-chime-07

### O-08-08 · Non-independence: what it is and why it matters
- **Source:** new (concept gap; ties to the greenhouse bench, squirrel family and crayon table questions)
- **Prompt:** Fertilizer is given to all 50 plants on one greenhouse bench and to none of the 50 plants on another. Is n = 50 per treatment? What's the problem, why does it matter for our conclusions, and how would you fix the design?
- **Key ideas:**
  - Plants on the same bench share conditions (light, temperature, watering), so they aren't independent.
  - Treatment is confounded with bench: the real sample size is about one bench per treatment (pseudoreplication).
  - Non-independence makes SEs and p-values look far more convincing than they should.
  - **Fixes:** many benches with random assignment of treatment to benches, or both treatments on each bench (blocking). Analyze at the right level, or permute within blocks.
- **Good enough when:** the student explains shared conditions → not independent → overconfident results, plus a design fix.
- **What could go wrong:**
  - "50 plants is too small." The number of plants isn't the problem.
  - "It's sampling bias."
- **Hints:**
  1. If the fertilizer bench happened to be sunnier, could you tell?
  2. How many truly independent units per treatment are there?
- **Related:** ch10-gquiz-05, ch08-gquiz-02, ch11-hw-08, ch08-hw-08

---

## Chapter 9: Uncertainty

### O-09-01 · Explain the sampling distribution
- **Source:** Uncertainty group quiz, Q1
- **Prompt:** Explain the idea of a sampling distribution and how it relates to sampling error and to uncertainty in an estimate.
- **Key ideas:**
  - It's the distribution of **estimates** (e.g., means) we would get from many samples of the same size.
  - Its spread shows **sampling error**, the chance differences between estimates and the true parameter.
  - Its SD is the **standard error**, which measures uncertainty in a single estimate.
  - We usually can't see it directly; we approximate it with the bootstrap or with math.
- **Good enough when:** the student says "distribution of estimates from many samples" and connects its spread to sampling error or the SE.
- **What could go wrong:**
  - "The distribution of values in my sample." That's the sample distribution, the most common mix-up.
  - The student says it shows bias. Its *center* would show bias only if we knew the truth; its *spread* is about error.
- **Hints:**
  1. Is it a distribution of individuals, or of something else?
  2. If you repeated your study many times, what would you collect?
- **Related:** ch09-gquiz-01, ch09-chime-01, ch08-hw-02

### O-09-02 · Explain the bootstrap
- **Source:** Uncertainty group quiz, Q2
- **Prompt:** Explain how the bootstrap approximates the sampling distribution. Include how observations are selected, the size of each resample, and what is calculated.
- **Key ideas:**
  - Resample the data **with replacement**.
  - Each resample has the **same size (n)** as the original.
  - Calculate the estimate (e.g., the mean) for each resample, and repeat many times (e.g., 1000–5000).
  - The distribution of these estimates approximates the sampling distribution. Its SD is the bootstrap SE, and its percentiles give a CI.
- **Good enough when:** all three parts are present: with replacement, same n, and an estimate for each resample.
- **What could go wrong:**
  - "Without replacement." Every resample would then be identical to the data.
  - "Bigger resamples." That would understate uncertainty.
  - The student thinks the bootstrap creates new data from the population.
- **Hints:**
  1. What would happen if you drew n values from your n values *without* replacement?
  2. Why keep the resample size equal to n?
- **Related:** ch09-gquiz-02, ch09-book-02

### O-09-03 · Why does the bootstrap fail for tiny samples?
- **Source:** Uncertainty group quiz, Q3
- **Prompt:** Why does bootstrapping do a poor job of approximating the sampling distribution when the sample size is very small?
- **Key ideas:**
  - The bootstrap treats your sample as a stand-in for the population.
  - With very few values, that stand-in is crude: few distinct resamples, missing extremes, a lumpy distribution.
  - The bootstrap SE and CI tend to **understate** uncertainty.
- **Good enough when:** the student explains that a tiny sample poorly represents the population, and the bootstrap can only reuse those few values.
- **What could go wrong:**
  - "Small samples are biased." They're noisy, not biased.
  - "The bootstrap needs 1000 data points." The number of *replicates* is different from the sample size.
- **Hints:**
  1. What does the bootstrap use as its "population"?
  2. Try it in your head with n = 3, values 2, 5 and 9. How many different resamples are possible?
- **Related:** ch09-gquiz-03

### O-09-04 · Interpret a Cohen's d with a CI
- **Source:** Uncertainty group quiz, Q4
- **Prompt:** Comparing the prediction accuracy of astrologers vs random guessers gave Cohen's d = 0.27, 95% CI [0.05, 0.48]. Explain what this means. Benchmarks: tiny 0.01–0.20, small 0.20–0.50, medium 0.50–0.80, large 0.80–1.20, very large 1.20–2.00, huge > 2.00.
- **Key ideas:**
  - The best estimate is a **small** effect: astrologers scored about a quarter of an SD higher.
  - The CI says effects from tiny (0.05) to nearly medium (0.48) are plausible.
  - The CI excludes 0, but the effect is modest at best.
  - Correct CI language: the method catches the true d 95% of the time, not "95% chance d is in here."
- **Good enough when:** the student interprets the size (small), the direction, and the range of plausible values.
- **What could go wrong:**
  - "There's a 95% chance d is between 0.05 and 0.48." Gently redirect to O-09-07.
  - "Astrologers are good at predicting." Small and modest; ask what d = 0.27 means for how much the two groups overlap.
- **Hints:**
  1. Start with the point estimate. What size category is it?
  2. What do the two ends of the CI tell you?
- **Related:** ch09-gquiz-04

### O-09-05 · What does this bootstrap code do? (high level)
- **Source:** Uncertainty group quiz, Q5
- **Prompt:** At a high level, not line by line, describe what this code does and what you would do with its output:
  ```
  boot_slope <- iris |>
    filter(Species == "versicolor") |>
    specify(Sepal.Length ~ Sepal.Width) |>
    generate(reps = 1000, type = "bootstrap") |>
    calculate(stat = "slope")
  ```
- **Key ideas:**
  - It takes only the versicolor flowers and makes 1000 bootstrap resamples.
  - For each resample it calculates the slope of sepal length on sepal width.
  - The result is a bootstrap distribution of the slope.
  - Then: SE = the SD of the 1000 slopes; 95% CI = their 2.5th and 97.5th percentiles.
- **Good enough when:** the student says it bootstraps the slope (1000 resamples, one slope each) and names one use (SE or CI).
- **What could go wrong:**
  - The student describes it line by line without the big picture. Ask: "What's the final product?"
  - "It makes 1000 new samples from the population." No, it resamples the data.
- **Hints:**
  1. What's in `boot_slope` at the end: one number, or many?
  2. How would you turn many slopes into an SE?
- **Related:** ch09-gquiz-05

### O-09-06 · Which plot do you prefer: error bars or boxplots?
- **Source:** Uncertainty group quiz, Q6b
- **Prompt:** Show `ch09-gquiz-astrology-plots.png`. Plot A shows means with error bars over the raw points; Plot B shows boxplots over the raw points. Which do you prefer, and why?
- **Key ideas:**
  - There's no single right answer.
  - **Plot A** highlights uncertainty in the means, which suits the question "do the groups differ on average?"
  - **Plot B** highlights variability among individuals and the shape of the distribution.
  - Strong answers say which question each plot answers and note that both show the raw data.
  - Bonus: the error bars should say what they are (SE or CI).
- **Good enough when:** the student states a preference tied to a specific question or goal.
- **What could go wrong:**
  - The student treats error bars as the spread of the data. Ask what would happen to the error bars with 10 times as much data.
- **Hints:**
  1. What question does each plot answer best?
- **Related:** ch09-gquiz-06

### O-09-07 · Why isn't a 95% CI a "95% chance"? Is it worth policing?
- **Source:** Uncertainty group quiz, Q7 (optional) and Chime In free response
- **Prompt:** People often say a 95% CI has "a 95% chance of capturing the true parameter." Statisticians prefer: "95% of confidence intervals from samples of a population will include the true parameter." What's the difference? Does it matter? Is it worth policing? Show `ch09-gquiz-ringtoss.png` (archery vs ring toss, by Ellie Murray, @epiellie).
- **Key ideas:**
  - The parameter is fixed; it's the interval that varies from sample to sample (ring toss, not archery).
  - Before sampling, the method has a 95% chance of producing an interval that catches the parameter. After sampling, your interval either caught it or didn't.
  - Coin analogy: once flipped and hidden under a cup, it's heads or tails, not "50% heads."
  - **Worth policing?** Reasonable people differ. The distinction matters for understanding where randomness lives; in casual talk the shortcut is common. (See also Julia Rohrer's "the100.ci" post.)
- **Good enough when:** the student explains that the probability belongs to the process, not to one finished interval, and gives a thoughtful opinion on policing.
- **What could go wrong:**
  - "The parameter moves around." It's fixed; the interval moves.
  - The student memorizes the phrasing without understanding. Ask them to explain it with the ring-toss picture.
- **Hints:**
  1. In ring toss, what moves: the ring or the post?
  2. After the coin is flipped and hidden, is it "50% heads"?
- **Related:** ch09-gquiz-07, ch09-hw-03, ch09-chime-09, ch09-book-04

### O-09-08 · Draw it: plots from summary statistics
- **Source:** Practice exam, Q15–16
- **Prompt:** Bill length in Adelie penguins on Dream island: mean male = 40.1 mm, male − female difference = 3.23 mm, 95% CI for the difference 2.08 to 4.38, Cohen's d = 1.64. (a) What is the pooled SD? (b) Describe or sketch two histograms (males and females) with enough labeling that a reader could roughly recover these values.
- **Key ideas:**
  - **(a)** Pooled SD = difference / d = 3.23 / 1.64 ≈ **1.97 mm**.
  - **(b)** Two roughly bell-shaped distributions: females centered near 36.9 mm and males near 40.1 mm, each with SD ≈ 2.
    - Most values fall within about ±4 mm of each mean.
    - They overlap, but their centers are separated by about 1.6 SDs.
    - Label the axes, units and means.
- **Good enough when:** (a) is correct, and the description has the right centers, a sensible spread, and visible overlap.
- **What could go wrong:**
  - The student uses the CI width as the spread of the data. The CI is about uncertainty in the difference, not individual variation.
  - The student draws non-overlapping distributions. With d ≈ 1.6 there's still substantial overlap.
- **Hints:**
  1. Cohen's d = difference / pooled SD. Rearrange it.
  2. Where should the female distribution be centered?
- **Related:** ch06-book-04, ch09-gquiz-04

### O-09-09 · What makes a confidence interval wide or narrow?
- **Source:** new (concept gap)
- **Prompt:** Two studies estimate the same mean. Study A's 95% CI is 2 units wide; Study B's is 10 units wide. List the reasons B's could be wider. What's the trade-off in reporting a 99% instead of a 95% CI?
- **Key ideas:**
  - Width depends on the **sample size** (smaller n → wider) and on **variability** in the data (larger SD → wider).
  - Width also depends on the **confidence level** (99% → wider).
  - A 99% CI catches the parameter more often but is less precise: confidence costs precision.
  - Width says nothing about bias. A narrow CI from a biased sample is precisely wrong.
- **Good enough when:** the student names n and variability, plus the confidence-level trade-off.
- **What could go wrong:**
  - "A wider CI means a bigger effect."
  - "99% CIs are narrower because they're more confident."
- **Hints:**
  1. What happens to the SE when n grows?
- **Related:** ch09-hw-02, ch09-book-03, ch09-book-08, ch10-gquiz-06

---

## Chapter 10: Hypothesis testing (NHST)

### O-10-01 · Two labs, opposite results (big pilot effect vs larger null)
- **Source:** Hypothesis testing quiz A, Q7 (MC + "Explain")
- **Prompt:** Lab 1 runs a small pilot study, reports a very large and significant effect (P = 0.02), and publicizes it in the New York Times. Lab 2 runs a larger study and finds basically no effect (P = 0.83). Which conclusion is most likely, and why?
  - (a) weak or no effect
  - (b) very strong effect
  - (c) real but modest effect
  - (d) equally likely
- **Key ideas:**
  - **(a) Weak or no effect** is most likely.
  - Small studies are noisy. A "significant" result from a small study tends to **overestimate** the effect (the winner's curse), and big surprising results get publicized.
  - The larger study is more precise, and it found nothing.
  - Publication and attention bias favor flashy small studies.
- **Good enough when:** the student trusts the larger study more and explains why small significant studies exaggerate effects.
- **What could go wrong:**
  - "P = 0.02 proves it works." Ask how precise a small study is.
  - "P = 0.83 proves there's no effect." Failing to reject isn't proving the null, though a large precise study does make big effects implausible.
- **Hints:**
  1. Which study has the smaller standard error?
  2. If a small study happens to get significance, would its estimate tend to be too big or too small?
- **Related:** ch10-gquiz-07

### O-10-02 · Two labs again (small non-significant vs large significant)
- **Source:** Hypothesis testing quiz A, Q8 (MC + "Explain")
- **Prompt:** Lab 1 runs a small pilot, finds a modest but non-significant effect (P = 0.35), and gives up. Lab 2 runs a larger study, finds a very similar modest effect, and rejects the null (P ≪ 0.05). Which conclusion is most likely, and why? (Same options as O-10-01.)
- **Key ideas:**
  - **(c) Real but modest effect.**
  - Both studies estimate a similar effect. The small study simply lacked power, so its CI was wide and included 0.
  - Non-significant ≠ no effect, and the p-value partly reflects sample size.
- **Good enough when:** the student says the effect is real but modest, and explains that the small study was underpowered.
- **What could go wrong:**
  - "The studies disagree." Their *estimates* agree; only their p-values differ.
  - "Lab 1 proved there's no effect."
- **Hints:**
  1. Compare the estimated effects, not the p-values. Are they similar?
  2. Why might a real effect be non-significant in a small study?
- **Related:** ch10-gquiz-08, O-10-03

### O-10-03 · How often is the null true? And why the p-value jokes?
- **Source:** Chime In B, Q4–5 (a "justify" question and three "why" follow-ups)
- **Prompt:** For a two-tailed test, the null is usually "no difference" or "no association." (1) How often do you expect such a null to be *exactly* true? Justify your answer. (2) Given that answer, why do statisticians joke that the p-value is a crude measure of sample size? (3) Why should we avoid using a p-value threshold as a bright line for conclusions or policy? (4) Why do we never say we "accept the null hypothesis"?
- **Key ideas:**
  1. **Very rarely.** In biology, almost nothing has an effect of exactly zero; true effects are usually just small.
  2. If the null is almost always slightly false, then with a big enough sample you'll reject it. Whether p is small then largely reflects how much data you have.
  3. 0.049 vs 0.051 is not a meaningful difference. Significance ≠ importance. Decisions should weigh effect sizes, uncertainty (CIs) and costs.
  4. Failing to reject means the data are *consistent with* the null, not that the null is true. The study may have lacked power, and absence of evidence isn't evidence of absence.
- **Good enough when:** the student gives a sensible justification for (1), and correct reasoning for at least two of (2)–(4).
- **What could go wrong:**
  - "The null is true about half the time." Ask for a biological example of two groups that are *exactly* identical.
  - The student says a small p means a big effect. Ask how p would change with 10 times the sample size and the same effect.
- **Hints:**
  1. Can you think of two populations whose means are identical to infinite decimal places?
  2. Hold the effect fixed and increase n. What happens to the p-value?
- **Related:** ch10-hw-03, ch10-hw-04, ch10-gquiz-03, ch10-hw-06

### O-10-04 · Is a p-value "the probability the null generated the data"?
- **Source:** NHST Chime In ("TRUE/FALSE… then explain why you chose it")
- **Prompt:** TRUE or FALSE: "A p-value is the probability that the data (or something more extreme) were generated by the null hypothesis." Give your answer, then explain why.
- **Key ideas:**
  - **FALSE.** A p-value is calculated *assuming* the null is true: P(data this extreme or more | H0).
  - "The probability the data were generated by the null" is a claim about the null given the data, P(H0 | data), which a p-value can't give you.
  - This is the prosecutor's fallacy in disguise.
  - Getting P(H0 | data) would need extra information, such as how plausible the null was to begin with.
- **Good enough when:** the student says FALSE and explains that the p-value assumes the null rather than giving its probability, ideally writing the two conditional probabilities.
- **What could go wrong:**
  - The student says TRUE because the wording sounds right. Ask them to rewrite the statement as "P( ___ | ___ )".
  - The student says FALSE for the wrong reason (e.g., "because it's about the alternative").
- **Hints:**
  1. When you calculate a p-value, what do you assume about the null?
  2. If you assume something is true, can your calculation tell you the probability that it's true?
  3. Is P(evidence | innocent) the same as P(innocent | evidence)?
- **Related:** ch10-chime-01, ch10-gquiz-04, ch10-chime-04, ch10-hw-07, ch10-book-06

### O-10-05 · Can mothers smell their children? What does "fail to reject" mean?
- **Source:** built from the NHST homework and book (Porter and Moore T-shirt study)
- **Prompt:** Show `ch10-smell-null-dist.png`. In the real study, 8 of 9 mothers picked their own child's shirt (p ≈ 0.04). In the homework version, 7 of 9 did (p ≈ 0.18). For each version: what do you conclude about the null, and what can't you conclude? If 7 of 9 is "not significant," does that mean mothers can't identify their children by smell?
- **Key ideas:**
  - **8/9:** reject the null at α = 0.05. This doesn't prove the null is false, and it doesn't mean there's a 4% chance mothers are guessing.
  - **7/9:** fail to reject. That is NOT evidence that mothers are just guessing: 7/9 is well above 50%, but with only 9 mothers the test has little power. Never "accept" the null.
  - The two results differ by one mother, so a bright-line threshold makes them sound more different than they are.
  - A CI or a larger study would be more informative.
- **Good enough when:** the student gets both decisions right and explains why "fail to reject" ≠ "no effect" in the 7/9 case.
- **What could go wrong:**
  - "p = 0.18 means there's an 18% chance mothers are guessing."
  - "7/9 proves mothers can't smell their kids."
  - The student computes a one-sided p. Ask what "two-tailed" means here.
- **Hints:**
  1. What proportion of mothers got it right with 7 of 9? Is that close to 50%?
  2. How many mothers were tested? How would that affect your ability to detect a real ability?
- **Related:** ch10-hw-05, ch10-hw-06, ch10-book-04, ch10-book-05

### O-10-06 · Type I and type II errors, and what α controls
- **Source:** new (concept gap; ties to practice exam Q11 and the Chime In items)
- **Prompt:** Define a type I and a type II error with a biological example of each. If a field switched from α = 0.05 to α = 0.01, what would happen to each kind of error, and to confidence intervals?
- **Key ideas:**
  - **Type I error:** rejecting a true null (a false positive). Its probability is α.
  - **Type II error:** failing to reject a false null (a false negative). Its probability is 1 − power, which depends on effect size and n.
  - **Lowering α to 0.01:**
    - fewer type I errors
    - more type II errors (lower power)
    - wider CIs (99%)
  - The choice of α should depend on the costs of each kind of mistake.
- **Good enough when:** the student gives correct definitions and examples, and the right direction for both errors when α drops.
- **What could go wrong:**
  - Swapping type I and type II.
  - "α is the probability the null is true."
  - "Lower α is always better."
- **Hints:**
  1. With a stricter threshold, will you reject more or less often?
- **Related:** ch10-chime-02, ch10-chime-03, ch10-hw-04, ch10-book-02

### O-10-07 · Why default to two-tailed tests?
- **Source:** new (concept gap; ties to ch10-gquiz-01, ch10-hw-02, ch10-book-03)
- **Prompt:** What's the difference between a one-tailed and a two-tailed test? Why does the course recommend two-tailed tests by default, and why is it a problem to choose one-tailed *after* seeing which way the data point?
- **Key ideas:**
  - **One-tailed** tests only one direction; **two-tailed** tests "different" in either direction.
  - A one-tailed test puts all of α in one tail, so p is half as big in that direction, and it can't detect an effect in the other direction.
  - Choosing the direction after seeing the data inflates false positives (effectively testing at α = 0.10).
  - Two-tailed is the honest default unless the other direction is truly impossible or irrelevant, and that has to be decided in advance.
- **Good enough when:** the student gives the definition, plus why choosing after looking is a problem.
- **What could go wrong:**
  - "One-tailed is better because it's more powerful."
- **Hints:**
  1. If you peeked at the data and then picked the tail, how often would you "find" something under the null?
- **Related:** ch10-hw-02, ch10-gquiz-01, ch10-book-03

---

## Chapter 11: Shuffling (permutation)

### O-11-01 · Bootstrap vs permutation: what's the difference?
- **Source:** built from the permutation Chime In and homework (originally fill-in-the-blank items)
- **Prompt:** Both the bootstrap and permutation use our data to approximate a sampling distribution. Explain how each one works, which distribution each approximates, and what each is used for.
- **Key ideas:**
  - **Bootstrap:**
    - Resample *with replacement*, same n.
    - The association is **kept**.
    - Approximates the sampling distribution around our estimate, so it's centered on the estimate.
    - Used for **uncertainty** (SE, CI).
  - **Permutation:**
    - *Shuffle* one variable (or the labels) relative to the other.
    - The association is **broken**.
    - Approximates the **null** distribution, so it's centered on the null value (e.g., 0).
    - Used for **hypothesis tests** (p-values).
  - In a permutation, every value is used exactly once, so the overall mean never changes. In a bootstrap, values are duplicated or left out.
- **Good enough when:** the student gets the procedure, the target distribution and the purpose right for both methods.
- **What could go wrong:**
  - "The bootstrap tests the null." It doesn't assume any null.
  - "Permutation resamples with replacement." It's a reshuffle.
  - The student thinks the permutation distribution is centered on the estimate.
- **Hints:**
  1. Which method keeps the association between x and y, and which destroys it?
  2. Where would each histogram be centered: on your estimate, or on 0?
- **Related:** ch11-chime-03, ch11-book-01, ch11-book-02, ch11-book-03, ch11-hw-01, ch11-hw-03

### O-11-02 · The line-up: why does picking the real data tell us about p?
- **Source:** permutation Chime In (line-up, "guesstimate the p-value")
- **Prompt:** Show `ch11-chime-lineup.png`. One panel is real and 19 are shuffled. If you can reliably pick out the real one, what does that say about the p-value? What would it mean if you couldn't?
- **Key ideas:**
  - Under the null (no association), the real data are just another shuffle, so you'd pick them only 1 time in 20 by luck.
  - Reliably picking them means data like ours are rare under the null: p ≲ 1/20 = 0.05.
  - If you can't pick them out, the real data look like the null, so you fail to reject. That does *not* show the null is true.
  - This is exactly the logic of a permutation test, done by eye.
- **Good enough when:** the student links "can pick it out" to "rare under the null" to "small p," and avoids saying the null is proven true or false.
- **What could go wrong:**
  - "I picked it, so the null is false." Push back: it's evidence, not proof.
  - The student only describes the panel's features, with no inference. Ask what the shuffled panels represent.
- **Hints:**
  1. If there were truly no difference between localities, would the real panel look special?
  2. If you guessed at random, how often would you pick the right panel?
- **Related:** ch11-chime-04, ch11-chime-05

### O-11-03 · Permuting with non-independence (garden beds)
- **Source:** permutation homework Q11
- **Prompt:** A study compares seedling growth in clay vs sandy soil, with both soil types in each of several garden beds. Seedlings in the same bed share a microclimate. How should you shuffle to build a null distribution, and why would shuffling across all beds be a mistake?
- **Key ideas:**
  - **Shuffle soil labels within each bed.** This breaks any soil–growth link but keeps each bed's shared conditions together.
  - Shuffling across beds would mix bed differences into the null, so the null wouldn't match the real data structure and the p-value could mislead.
  - Blocked designs *can* be permuted, as long as you permute within blocks.
- **Good enough when:** the student says "within beds" and explains that it preserves the bed structure.
- **What could go wrong:**
  - "Shuffle bed labels." Bed isn't the treatment.
  - "Blocked designs can't be permuted."
- **Hints:**
  1. What do you want the shuffle to destroy, and what do you want it to keep?
- **Related:** ch11-hw-08, ch11-chime-01

---

## Chapter 12: Study design

### O-12-01 · Random assignment vs random sampling
- **Source:** built from the study design homework Q6 and book Q1
- **Prompt:** What's the difference between random *assignment* and random *sampling (selection)*? What does each one protect you against? Can a study have one without the other?
- **Key ideas:**
  - **Random assignment** (who gets which treatment) balances confounders across groups on average. It supports **causal** conclusions (internal validity).
  - **Random sampling** (who gets into the study) makes the sample representative of the population. It supports **generalization** (external validity).
  - Yes, you can have one without the other:
    - A lab experiment on volunteers has random assignment but not random sampling.
    - A random survey has random sampling but no assignment, so it's observational.
- **Good enough when:** the student correctly links assignment to causation and sampling to generalization, with an example of one without the other.
- **What could go wrong:**
  - The student treats them as the same thing.
  - "Random assignment works by modeling covariates." It works through design, not modeling.
- **Hints:**
  1. Which one decides *who is in* the study, and which decides *who gets the treatment*?
  2. Which helps you say "X causes Y"? Which helps you say "this applies to everyone"?
- **Related:** ch12-book-01, ch12-book-05

### O-12-02 · Why didn't the experiment find anything?
- **Source:** study design homework Q9 and book Q6
- **Prompt:** An experiment with appropriate controls failed to reject the null hypothesis. Does that prove there's no causal relationship? Give at least two reasons a real effect could still go undetected, and say what you'd change in a follow-up study.
- **Key ideas:**
  - No: absence of evidence isn't evidence of absence.
  - **Low power:** the sample is too small for a modest effect. Fix: a larger sample, or blocking or matching to reduce noise.
  - **Unrealistic dose or intensity:** the treatment differs from nature. Fix: realistic levels.
  - **Unnatural conditions** block the pathway (e.g., no pollinators present). Fix: a field setting.
  - Look at the CI: is it wide enough to include meaningful effects?
- **Good enough when:** the student gives two valid reasons plus a matching fix, and does not claim the null is proven.
- **What could go wrong:**
  - "The null is true." Ask what a wide CI that includes meaningful effects would say.
- **Hints:**
  1. What determines whether a real effect reaches significance?
  2. Could the lab setup differ from where the effect happens in nature?
- **Related:** ch12-book-06, ch10-gquiz-08, O-10-02, O-10-05

### O-12-03 · Glyphosate: what can we conclude?
- **Source:** built from the book's glyphosate questions (Q7–Q11)
- **Prompt:** A widely used herbicide (glyphosate) has been linked to non-Hodgkin lymphoma. The strongest human evidence comes from farmworkers with heavy exposure (often alongside other pesticides), and some animal evidence comes from very high doses. More than 170,000 lawsuits have been filed. Weigh the evidence: what are the main threats to internal, external and ecological validity, and what study or natural experiment would help?
- **Key ideas:**
  - **Internal validity:** co-exposure to other pesticides is a confound, and there's no random assignment.
  - **External validity:** heavy occupational exposure may not generalize to occasional home use.
  - **Ecological validity:** results at the maximum tolerated dose may not apply at everyday doses.
  - **The lawsuit count is a biased measure.** It could overstate harm (frivolous claims) or understate it (exposed workers unlikely to sue).
  - **A helpful comparison:** Bayer's 2023 removal of glyphosate from residential products. If glyphosate is causal, rates should fall more among residential users than among agricultural workers (difference-in-differences).
- **Good enough when:** the student names at least two kinds of validity threat correctly, plus one idea for better evidence.
- **What could go wrong:**
  - Mixing up internal and external validity. Ask: "Is the problem *what caused it*, or *who it applies to*?"
  - "Lawsuits prove harm" or "settlements prove no harm."
  - The student wants to run a randomized experiment on people. Discuss why that's unethical, and what natural experiments offer instead.
- **Hints:**
  1. Were people randomly assigned to glyphosate exposure?
  2. Do the studied people and doses look like the people and doses you care about?
  3. Who decides whether to file a lawsuit?
- **Related:** ch12-book-07, ch12-book-08, ch12-book-09, ch12-book-10, ch12-book-11

### O-12-04 · Designing good controls (and blinding)
- **Source:** new (concept gap; ties to ch12-hw-07, the placebo material)
- **Prompt:** You're testing whether a new fertilizer increases Clarkia flower number. Why is "do nothing" usually a poor control? Design a better control, and explain how blinding could improve the study.
- **Key ideas:**
  - A good control differs from the treatment **only** in the factor of interest.
  - "Doing nothing" also differs in handling, watering volume and attention, all of which could matter. For people, it also differs in expectation (placebo effects).
  - **Better control:** apply the same volume of liquid without the active ingredient, handled identically (a sham or placebo).
  - **Blinding:** the people measuring flowers (and the subjects, for humans) shouldn't know which group is which, to avoid biased measurement.
  - Randomly assign treatment and control.
- **Good enough when:** the student explains "differs only in the factor of interest," describes a sensible sham control, and gives a reason for blinding.
- **What could go wrong:**
  - "Blinding is only for human studies." Measurer bias applies to plants too.
- **Hints:**
  1. List everything the treated plants experience. Which of those does a do-nothing plant miss?
- **Related:** ch12-hw-07, ch12-book-05

### O-12-05 · Planning for power
- **Source:** new (concept gap; ties to ch12-hw-08, the NHST "two labs" questions)
- **Prompt:** Before running a study, what determines its power? Name three ways you could increase power without changing α, and explain why underpowered studies are a problem even when they *do* find something significant.
- **Key ideas:**
  - **Power depends on:** the true effect size, the sample size, the variability (SD) and α.
  - **To increase power:**
    - a larger n
    - reduce noise (more precise measurement, blocking or matching, more uniform conditions)
    - study a stronger or more realistic treatment
  - **Problems with underpowered studies:**
    - They miss real effects.
    - When they do reach significance, the estimate tends to be exaggerated (winner's curse), as in the "two labs" questions.
  - Plan around the *smallest biologically meaningful* effect.
- **Good enough when:** the student lists the determinants, gives two or three ways to increase power, and states one problem with underpowered studies.
- **What could go wrong:**
  - "Power is the probability the null is false."
  - "Just lower α to get more power." That's backwards: a lower α reduces power.
- **Hints:**
  1. What makes a real effect easier to see through the noise?
- **Related:** ch12-hw-08, ch12-book-04, ch10-gquiz-07, ch10-gquiz-08, O-10-01

### O-12-06 · From observation to experiment
- **Source:** new (concept gap; ties to the diary/depression Chime In and ch12-hw-01 to 03)
- **Prompt:** An observational study found that students who keep diaries are more likely to be depressed. List the possible explanations. Then design an experiment that could test whether diary-keeping causes depression. What can the experiment tell you that the observational study can't, and what would make such an experiment hard or unethical?
- **Key ideas:**
  - **Explanations:**
    - diaries → depression
    - depression → diary-keeping (reverse causation)
    - a confounder (e.g., stress) causing both
    - chance
  - **An experiment:** randomly assign volunteers to journal or to a matched control activity, blind the outcome assessors where possible, and measure depression afterward.
  - Random assignment rules out reverse causation and confounding (on average), leaving cause or chance.
  - **Limits:** ethics (you can't assign harmful exposures), volunteers may not represent the population (external validity), and compliance.
  - Natural experiments can help when true experiments are impossible.
- **Good enough when:** the student gives at least three explanations, a design with random assignment, and one limit.
- **What could go wrong:**
  - The design lets people choose whether to journal (that's not random assignment).
  - "Experiments prove causation 100%." Sampling error remains.
- **Hints:**
  1. Who decides who keeps a diary in your design?
- **Related:** ch10-chime-05, ch12-hw-01, ch12-hw-02, ch12-hw-03, ch12-book-01

---

## Notes for the instructor

- Entries **O-08-04** and **O-08-05** correspond to questions you excluded from the multiple-choice bank because their keys are debatable. That debate is what makes them good discussion prompts.
- **Hand-written code questions** (ch01-quiz-04, ch04-quiz-06) now live here as O-01-01 and O-04-01, and are excluded from the multiple-choice bank.
- Entries marked **"new (concept gap)"** were written to cover key ideas the quizzes and homework touched on only through multiple choice (or not at all). Check that they match your emphasis.
- **Not included:** post-exam reflection questions, which are about study habits rather than content.
