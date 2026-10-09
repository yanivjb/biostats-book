# Applied Biostats tutor: question bank, chapters 4–6 (Exam 1, chapters 0–12)

Knowledge file for the course tutor. Each question has an ID, its concepts, the question, options, the answer, an explanation, why each wrong option is wrong, and a hint. Fields marked **tutor only** must never be shown to the student before they have answered.

- **Course originals** come from the instructor's homework, quizzes, Chime Ins and book.
- **AI-written versions** test the same idea with a new scenario or numbers. Their ID ends in -v1 or -v2 and names the original.
- 718 questions in all. 157 use a figure and are marked **Figure question (website only)**: students practice those on the study-guide website, where the figure is shown. Use one only when a student brings it to you; its figure link is included.

## Chapters and concepts

- **Chapter 0: Types of variables** — Variable types; Explanatory & response variables
- **Chapter 1: Getting started with R** — R basics; Assignment & the environment; Functions, pipes & packages; Errors & debugging; Scripts & reproducibility; Learning R
- **Chapter 2: ggplot** — Plot design principles; Aesthetics & ggplot layers; Visualizing associations
- **Chapter 3: Reproducible science** — Reproducible workflows; Data entry & data dictionaries; Missing data & bias
- **Chapter 4: Data in R** — Tidy data; dplyr verbs; Assignment & the environment; Errors & debugging
- **Chapter 5: Univariate summaries** — Shape of distributions; Center: mean & median; Spread: variance & SD; Range, IQR & boxplots; Coefficient of variation; Summaries in R
- **Chapter 6: Associations I** — Two categorical variables; Difference in means & Cohen's d; Visualizing associations; Association vs causation
- **Chapter 7: Associations II** — Covariance; Correlation; Association vs causation
- **Chapter 8: Sampling** — Samples, populations & estimates; Sampling distribution; SD vs SE; Sampling error vs bias; Non-independence; Shape of distributions
- **Chapter 9: Uncertainty** — Sampling distribution & SE; Bootstrap; Confidence intervals; Visualizing uncertainty
- **Chapter 10: Null hypothesis significance testing** — Null & alternative hypotheses; What a p-value means; Errors, power & sample size; Confounding & non-independence
- **Chapter 11: Shuffling (permutation)** — Bootstrap vs permutation; Permutation p-values; Bootstrap CIs; Non-independence & blocking
- **Chapter 12: Study design** — Experiments vs observational studies; Controls & placebos; Power & precision; Validity; The language of causation

## Chapter 4: Data in R

### ch04-book-01
- **Kind:** Course original
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

Consider the table below. The data are:

location | GC | GC | GC | GC | GC | GC
ril | A1 | A100 | A102 | A104 | A106 | A107
mean_visits | 0 | 0.1875 | 0.25 | 0 | 0 | 0

- **Options:**

  A) tidy
  B) not tidy

- **Answer (tutor only):** B
- **Explanation (tutor only):** The data are turned sideways: each variable is a row and each RIL is a column. In tidy data, each variable is a column and each observation a row.
- **Why the wrong options are wrong (tutor only):**
  A) Variables (location, ril, mean_visits) appear as rows here, not columns.
- **Hint:** Is each RIL a row?

### ch04-book-01-v1
- **Kind:** AI-written version of ch04-book-01
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

Consider the table below. The data are:

tree | T1 | T2 | T3 | T4
species | oak | oak | maple | pine
dbh_cm | 34 | 28 | 22 | 41

- **Options:**

  A) tidy
  B) not tidy

- **Answer (tutor only):** B
- **Explanation (tutor only):** Trees are spread across columns and variables down the rows. Tidy data have one row per tree.
- **Why the wrong options are wrong (tutor only):**
  A) The table is sideways.
- **Hint:** Is each tree a row?

### ch04-book-01-v2
- **Kind:** AI-written version of ch04-book-01
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

Consider the table below. The data are:

quadrat | species_count | soil_pH
Q1 | 7 | 6.2
Q2 | 4 | 5.8
Q3 | 9 | 6.9

- **Options:**

  A) tidy
  B) not tidy

- **Answer (tutor only):** A
- **Explanation (tutor only):** One row per quadrat, one column per variable: tidy.
- **Why the wrong options are wrong (tutor only):**
  B) All three tidy rules are met.
- **Hint:** Check rows, columns, cells.

### ch04-book-02
- **Kind:** Course original
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

Consider the table below. The data are:

location-ril | mean_visits
GC-A1 | 0
GC-A100 | 0.1875
GC-A102 | 0.25
GC-A104 | 0
GC-A106 | 0
GC-A107 | 0

- **Options:**

  A) tidy
  B) not tidy

- **Answer (tutor only):** B
- **Explanation (tutor only):** Location and RIL are two variables squeezed into one column. In tidy data, each variable gets its own column, otherwise you can't easily, for example, get the mean for each location.
- **Why the wrong options are wrong (tutor only):**
  A) One column holds two variables, which breaks the tidy rule of one variable per column.
- **Hint:** How many variables are hiding in the first column?

### ch04-book-02-v1
- **Kind:** AI-written version of ch04-book-02
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

Consider the table below. The data are:

site_year | count
N1-2023 | 14
N1-2024 | 18
S1-2023 | 9

- **Options:**

  A) tidy
  B) not tidy

- **Answer (tutor only):** B
- **Explanation (tutor only):** Two variables (site and year) share one column. Tidy data give each variable its own column.
- **Why the wrong options are wrong (tutor only):**
  A) One cell holds two values.
- **Hint:** How many variables are in site_year?

### ch04-book-02-v2
- **Kind:** AI-written version of ch04-book-02
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

Consider the table below. The data are:

sample | measurement
S1 | 12.4 cm
S2 | 9.1 cm
S3 | 15.0 mm

- **Options:**

  A) tidy
  B) not tidy

- **Answer (tutor only):** B
- **Explanation (tutor only):** Each measurement cell mixes a number and a unit (and units differ between rows). Store the number in one column (with consistent units) and document units separately.
- **Why the wrong options are wrong (tutor only):**
  A) Cells contain more than one piece of information.
- **Hint:** Could R average the measurement column as is?

### ch04-book-03
- **Kind:** Course original
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

Consider the table below (mean pollinator visits for each RIL at two locations). The data are:

ril | GC | SR
A1 | 0 | 0.6667
A100 | 0.1875 | 0.5833
A102 | 0.25 | 0.6667
A104 | 0 | 1.75
A106 | 0 | 0.5
A107 | 0 | 1.5

- **Options:**

  A) tidy
  B) not tidy

- **Answer (tutor only):** B
- **Explanation (tutor only):** This is 'wide format': the values of a variable (location: GC, SR) are used as column names. That can be a fine way to present data to people, but for analysis, tidy data would have columns ril, location and mean_visits.
- **Why the wrong options are wrong (tutor only):**
  A) GC and SR are values of the variable location, not variables themselves.
- **Hint:** Are GC and SR variables, or values of a variable?

### ch04-book-03-v1
- **Kind:** AI-written version of ch04-book-03
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

Consider the table below (seed counts per plant in two years). The data are:

plant | 2023 | 2024
P1 | 120 | 95
P2 | 88 | 130
P3 | 102 | 99

- **Options:**

  A) tidy
  B) not tidy

- **Answer (tutor only):** B
- **Explanation (tutor only):** Year is a variable, but its values (2023, 2024) are used as column names. Tidy: columns plant, year, seeds.
- **Why the wrong options are wrong (tutor only):**
  A) Values of a variable appear as column headers.
- **Hint:** What variable do the column names 2023 and 2024 hold?

### ch04-book-03-v2
- **Kind:** AI-written version of ch04-book-03
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

Which is the tidy version of a table of bird counts at sites N1 and S1 in 2023 and 2024?

- **Options:**

  A) Columns: site, year, count (4 rows)
  B) Columns: site, 2023, 2024 (2 rows)
  C) Columns: year, N1, S1 (2 rows)
  D) One column holding '2023: N1=14, S1=9'

- **Answer (tutor only):** A
- **Explanation (tutor only):** Each observation (a site in a year) gets its own row, and each variable (site, year, count) its own column.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Values of a variable are used as column names.
  D) Many values crammed into one cell.
- **Hint:** How many site-year combinations are there?

### ch04-book-04
- **Kind:** Course original
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

You should always make sure data are tidy when (pick the best answer)

- **Options:**

  A) collecting data
  B) presenting data
  C) analyzing data with dplyr
  D) all of the above

- **Answer (tutor only):** C
- **Explanation (tutor only):** dplyr (and ggplot) are built to work on tidy data, so data must be tidy for analysis. For presenting data to people, other layouts (like a wide table) can be clearer.
- **Why the wrong options are wrong (tutor only):**
  A) Collecting data in a tidy layout is a good habit, but not a must; the essential moment is analysis.
  B) Presentation tables can be wide if that's easier for readers.
  D) Since B isn't always true, 'all of the above' isn't the best answer.
- **Hint:** When is the tidy layout required, rather than just nice?

### ch04-book-04-v1
- **Kind:** AI-written version of ch04-book-04
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

Why do dplyr and ggplot work best with tidy data?

- **Options:**

  A) They expect each variable to be a column, so you can name columns in filter(), mutate() and aes()
  B) They can't read numbers otherwise
  C) Tidy data are smaller
  D) They don't; any shape works equally well

- **Answer (tutor only):** A
- **Explanation (tutor only):** Tidy data let you refer to each variable by its column name, which is how these tools are designed.
- **Why the wrong options are wrong (tutor only):**
  B) They read numbers either way.
  C) Tidy data are often longer.
  D) Untidy data make these tools awkward or impossible to use.
- **Hint:** How do you tell ggplot what goes on the x-axis?

### ch04-book-04-v2
- **Kind:** AI-written version of ch04-book-04
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

When is a wide (untidy) table perfectly fine?

- **Options:**

  A) As a compact display table for readers, as long as you analyze a tidy version
  B) Always, including for analysis
  C) Never, even in a presentation
  D) Only for data with fewer than 10 rows

- **Answer (tutor only):** A
- **Explanation (tutor only):** Wide tables can be easier to read in a report. For analysis with dplyr and ggplot, use tidy data.
- **Why the wrong options are wrong (tutor only):**
  B) Analysis tools expect tidy data.
  C) Display tables can be wide.
  D) Size isn't the criterion.
- **Hint:** Analysis or display?

### ch04-book-05
- **Kind:** Course original
- **Concepts:** dplyr verbs
- **Type:** numeric
- **Question:**

Here are the first rows of the iris data:

Sepal.Length | Sepal.Width | Petal.Length | Petal.Width | Species
5.1 | 3.5 | 1.4 | 0.2 | setosa
4.9 | 3.0 | 1.4 | 0.2 | setosa
4.7 | 3.2 | 1.3 | 0.2 | setosa
4.6 | 3.1 | 1.5 | 0.2 | setosa

Consider this code:

iris |>
  mutate(pl_pw_ratio = Petal.Length / Petal.Width)

What is the value of pl_pw_ratio in the first row?

- **Answer (tutor only):** 7
- **Explanation (tutor only):** mutate() calculates the new column row by row. In row 1, Petal.Length is 1.4 and Petal.Width is 0.2, so 1.4 / 0.2 = 7.
- **Why the wrong options are wrong (tutor only):**
  Common mistake: dividing the wrong columns (e.g., Sepal.Length / Sepal.Width = 1.46).
- **Hint:** Find Petal.Length and Petal.Width in the first row.

### ch04-book-05-v1
- **Kind:** AI-written version of ch04-book-05
- **Concepts:** dplyr verbs
- **Type:** numeric
- **Question:**

Here are the first rows of a penguins table:

species | bill_length | bill_depth
Adelie | 39.1 | 18.7
Adelie | 39.5 | 17.4
Adelie | 40.3 | 18.0

Consider this code:

penguins |>
  mutate(bill_diff = bill_length - bill_depth)

What is bill_diff in the second row?

- **Answer (tutor only):** 22.1
- **Explanation (tutor only):** mutate() works row by row: 39.5 − 17.4 = 22.1.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: using the first row (20.4), or adding instead of subtracting.
- **Hint:** Find row 2, then subtract.

### ch04-book-05-v2
- **Kind:** AI-written version of ch04-book-05
- **Concepts:** dplyr verbs
- **Type:** numeric
- **Question:**

A table called plants has these rows:

plant | height_cm | width_cm
P1 | 20 | 4
P2 | 15 | 5
P3 | 30 | 6

What value does this code give for P3?

plants |>
  mutate(ratio = height_cm / width_cm)

- **Answer (tutor only):** 5
- **Explanation (tutor only):** Row by row: P3's ratio is 30 / 6 = 5.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: dividing width by height (0.2), or using another row.
- **Hint:** Find P3's row and divide.

### ch04-book-06
- **Kind:** Course original
- **Concepts:** dplyr verbs
- **Type:** select-all
- **Question:**

Here are the columns in iris: Sepal.Length, Sepal.Width, Petal.Length, Petal.Width, Species. Consider this code:

iris |>
  mutate(pl_pw_ratio = Petal.Length / Petal.Width) |>
  select(Species, pl_pw_ratio)

Which column names will appear in the output? (select all that apply)

- **Options:**

  A) Sepal.Length
  B) Sepal.Width
  C) Petal.Length
  D) Petal.Width
  E) Species
  F) pl_pw_ratio

- **Answer (tutor only):** E, F
- **Explanation (tutor only):** mutate() adds pl_pw_ratio, then select() keeps only the columns named: Species and pl_pw_ratio.
- **Why the wrong options are wrong (tutor only):**
  A) to D) select() drops every column it isn't given, even ones used to calculate pl_pw_ratio.
- **Hint:** What does select() do to columns it isn't told to keep?

### ch04-book-06-v1
- **Kind:** AI-written version of ch04-book-06
- **Concepts:** dplyr verbs
- **Type:** select-all
- **Question:**

The penguins columns are species, island, bill_length, bill_depth, flipper_length, body_mass, sex. Which columns will appear in the output of this code? (Select all that apply.)

penguins |>
  mutate(mass_kg = body_mass / 1000) |>
  select(species, mass_kg)

- **Options:**

  A) species
  B) island
  C) body_mass
  D) mass_kg
  E) sex

- **Answer (tutor only):** A, D
- **Explanation (tutor only):** mutate() adds mass_kg; select() then keeps only the named columns: species and mass_kg.
- **Why the wrong options are wrong (tutor only):**
  B), C) and E) Not listed in select(), so they're dropped.
- **Hint:** select() keeps only what you name.

### ch04-book-06-v2
- **Kind:** AI-written version of ch04-book-06
- **Concepts:** dplyr verbs
- **Type:** MC
- **Question:**

How many columns does this code return?

penguins |>
  select(species, island, body_mass) |>
  mutate(heavy = body_mass > 4500)

- **Options:**

  A) 3
  B) 4
  C) 7
  D) 1

- **Answer (tutor only):** B
- **Explanation (tutor only):** select() keeps 3 columns, then mutate() adds one more (heavy): 4 in total.
- **Why the wrong options are wrong (tutor only):**
  A) Forgets the new column.
  C) select() already dropped the others.
  D) mutate() doesn't drop columns.
- **Hint:** Count after select(), then add mutate()'s new column.

### ch04-book-08
- **Kind:** Course original
- **Concepts:** dplyr verbs
- **Type:** MC
- **Question:**

What was this code aiming to do?

iris |>
  filter(Species == "setosa")

- **Options:**

  A) Create a new column called Species
  B) Convert Species to a factor
  C) Return only the rows of the iris dataset where Species is "setosa"
  D) Remove the Species column from the dataset
  E) Sort the dataset by Species

- **Answer (tutor only):** C
- **Explanation (tutor only):** filter() keeps the rows that meet a condition: here, only setosa flowers.
- **Why the wrong options are wrong (tutor only):**
  A) Creating columns is mutate().
  B) Changing type would use mutate() with factor().
  D) Removing columns is select().
  E) Sorting is arrange().
- **Hint:** Does filter() work on rows or on columns?

### ch04-book-08-v1
- **Kind:** AI-written version of ch04-book-08
- **Concepts:** dplyr verbs
- **Type:** MC
- **Question:**

What does this code aim to do?

penguins |>
  filter(sex == "female")

- **Options:**

  A) Create a column called sex
  B) Keep only the female penguins
  C) Remove the sex column
  D) Sort by sex

- **Answer (tutor only):** B
- **Explanation (tutor only):** filter() keeps rows where the condition is TRUE: here, sex equal to "female".
- **Why the wrong options are wrong (tutor only):**
  A) That's mutate().
  C) That's select().
  D) That's arrange().
- **Hint:** Rows or columns?

### ch04-book-08-v2
- **Kind:** AI-written version of ch04-book-08
- **Concepts:** dplyr verbs
- **Type:** MC
- **Question:**

Which code keeps only setosa flowers with petals longer than 1.5 cm?

- **Options:**

  A) iris |> filter(Species == "setosa", Petal.Length > 1.5)
  B) iris |> select(Species == "setosa", Petal.Length > 1.5)
  C) iris |> filter(Species = "setosa" & Petal.Length > 1.5)
  D) iris |> mutate(Species == "setosa")

- **Answer (tutor only):** A
- **Explanation (tutor only):** filter() can take several conditions separated by commas; rows must meet all of them. Use == to test equality.
- **Why the wrong options are wrong (tutor only):**
  B) select() picks columns.
  C) = assigns instead of testing equality.
  D) mutate() adds columns.
- **Hint:** Which verb keeps rows, and how do you test equality?

### ch04-hw-01
- **Kind:** Course original
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

Consider the data table below. The data are:

Species | setosa | setosa | setosa
Petal.Length | 1.4 | 1.4 | 1.3
Petal.Width | 0.2 | 0.2 | 0.2

- **Options:**

  A) tidy
  B) not tidy

- **Answer (tutor only):** B
- **Explanation (tutor only):** In tidy data, each variable is a column and each observation (here, each flower) is a row. This table is turned sideways: variables are rows and flowers are columns.
- **Why the wrong options are wrong (tutor only):**
  A) Tidy data put each variable in its own column. Here, Species, Petal.Length and Petal.Width are rows.
- **Hint:** Is each flower a row, and each variable a column?

### ch04-hw-01-v1
- **Kind:** AI-written version of ch04-hw-01
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

Consider the data table below. The data are:

frog | F1 | F2 | F3
mass_g | 12.1 | 9.8 | 14.3
jump_cm | 41 | 35 | 52

- **Options:**

  A) tidy
  B) not tidy

- **Answer (tutor only):** B
- **Explanation (tutor only):** Each frog should be a row and each variable (mass, jump) a column. Here the table is turned sideways: frogs are columns.
- **Why the wrong options are wrong (tutor only):**
  A) Variables are stored as rows, which breaks the tidy rules.
- **Hint:** Is each frog a row?

### ch04-hw-01-v2
- **Kind:** AI-written version of ch04-hw-01
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

Consider the data table below. The data are:

site | N1_2023 | N1_2024 | S1_2023 | S1_2024
bird_count | 14 | 18 | 9 | 11

- **Options:**

  A) tidy
  B) not tidy

- **Answer (tutor only):** B
- **Explanation (tutor only):** Site and year (two variables) are crammed into the column names. Tidy: one row per site-year, with columns site, year and bird_count.
- **Why the wrong options are wrong (tutor only):**
  A) Values of variables (site, year) appear as column names.
- **Hint:** How many variables are hiding in the column names?

### ch04-hw-02
- **Kind:** Course original
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

Consider the data table below. The data are:

Species | Petal.Length | Petal.Width
setosa | 1.4 | 0.2
setosa | 1.4 | 0.2
setosa | 1.3 | 0.2

- **Options:**

  A) tidy
  B) not tidy

- **Answer (tutor only):** A
- **Explanation (tutor only):** Each row is one flower (an observation), each column is one variable, and each cell holds one value. That's tidy.
- **Why the wrong options are wrong (tutor only):**
  B) Every variable has its own column and every flower its own row, so nothing breaks the tidy rules.
- **Hint:** Check: one row per flower? one column per variable? one value per cell?

### ch04-hw-02-v1
- **Kind:** AI-written version of ch04-hw-02
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

Consider the data table below. The data are:

frog | mass_g | jump_cm
F1 | 12.1 | 41
F2 | 9.8 | 35
F3 | 14.3 | 52

- **Options:**

  A) tidy
  B) not tidy

- **Answer (tutor only):** A
- **Explanation (tutor only):** One row per frog, one column per variable, one value per cell: tidy.
- **Why the wrong options are wrong (tutor only):**
  B) Nothing breaks the tidy rules.
- **Hint:** One row per frog? One column per variable?

### ch04-hw-02-v2
- **Kind:** AI-written version of ch04-hw-02
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

Consider the data table below. The data are:

site | year | bird_count
N1 | 2023 | 14
N1 | 2024 | 18
S1 | 2023 | 9
S1 | 2024 | 11

- **Options:**

  A) tidy
  B) not tidy

- **Answer (tutor only):** A
- **Explanation (tutor only):** Each row is one site in one year (an observation), and each variable has its own column: tidy.
- **Why the wrong options are wrong (tutor only):**
  B) Every variable has its own column and every observation its own row.
- **Hint:** Check the three tidy rules.

### ch04-hw-04
- **Kind:** Course original
- **Concepts:** dplyr verbs
- **Type:** MC
- **Question:**

What does this code do?

ril_data |>
  rename(petal_area = petal_area_mm, asd = asd_mm) |>
  mutate(rel_asd = asd / petal_area)

- **Options:**

  A) It renames two columns and adds a new column, rel_asd, calculated row by row as asd divided by petal_area, then prints the result. ril_data itself is unchanged.
  B) It permanently renames the columns in ril_data and adds rel_asd to it
  C) It calculates one overall value: the mean asd divided by the mean petal area
  D) It removes petal_area_mm and asd_mm and keeps only rel_asd

- **Answer (tutor only):** A
- **Explanation (tutor only):** rename() changes column names, and mutate() adds a column calculated separately for every row (each RIL gets its own rel_asd). Because the result isn't assigned with <-, it is only printed; ril_data stays as it was.
- **Why the wrong options are wrong (tutor only):**
  B) Nothing is saved: there's no <- assignment.
  C) mutate() works row by row; a single summary value would need summarize().
  D) mutate() adds a column and keeps all the others; rename() only changes names.
- **Hint:** Does mutate() give one value per row, or one value overall? And was anything saved?

### ch04-hw-04-v1
- **Kind:** AI-written version of ch04-hw-04
- **Concepts:** dplyr verbs
- **Type:** MC
- **Question:**

What does this code do?

penguins |>
  rename(mass = body_mass) |>
  mutate(mass_kg = mass / 1000)

- **Options:**

  A) Renames body_mass to mass and adds mass_kg, calculated for each penguin, then prints the result; penguins itself is unchanged
  B) Permanently changes penguins
  C) Calculates one value: the mean mass in kg
  D) Removes all columns except mass_kg

- **Answer (tutor only):** A
- **Explanation (tutor only):** rename() changes a column name; mutate() adds a column calculated row by row. Without <-, the result is just printed.
- **Why the wrong options are wrong (tutor only):**
  B) Nothing is assigned.
  C) mutate() works row by row; summarize() would give one value.
  D) mutate() keeps all columns.
- **Hint:** Row by row or one value? Saved or printed?

### ch04-hw-04-v2
- **Kind:** AI-written version of ch04-hw-04
- **Concepts:** dplyr verbs
- **Type:** MC
- **Question:**

What does this code return?

plants |>
  mutate(area = length * width) |>
  summarize(mean_area = mean(area))

- **Options:**

  A) A single row with the mean area of all plants
  B) Every plant with a new area column
  C) The area of the first plant only
  D) An error, because area doesn't exist

- **Answer (tutor only):** A
- **Explanation (tutor only):** mutate() adds an area for each plant; summarize() then collapses all rows into one summary value.
- **Why the wrong options are wrong (tutor only):**
  B) summarize() collapses the rows.
  C) It averages over all plants.
  D) area is created by mutate() in the line before.
- **Hint:** What does summarize() do to the rows?

### ch04-hw-06
- **Kind:** Course original
- **Concepts:** dplyr verbs
- **Type:** MC
- **Question:**

What does the code below aim to do?

ril_data |>
  filter(location == "SR")

- **Options:**

  A) Create a new column called location
  B) Remove the location column from the dataset
  C) Remove all columns except location from the dataset
  D) Sort the dataset by location
  E) Return only data from the SR location

- **Answer (tutor only):** E
- **Explanation (tutor only):** filter() keeps the rows that meet a condition. Here it keeps only rows where location is "SR".
- **Why the wrong options are wrong (tutor only):**
  A) Creating columns is mutate().
  B) and C) Removing or keeping columns is select().
  D) Sorting is arrange().
- **Hint:** Does filter() work on rows or on columns?

### ch04-hw-06-v1
- **Kind:** AI-written version of ch04-hw-06
- **Concepts:** dplyr verbs
- **Type:** MC
- **Question:**

What does this code aim to do?

penguins |>
  filter(island == "Dream")

- **Options:**

  A) Create a new column called island
  B) Keep only penguins from Dream island
  C) Remove the island column
  D) Sort penguins by island

- **Answer (tutor only):** B
- **Explanation (tutor only):** filter() keeps the rows that meet a condition: here, island equal to "Dream".
- **Why the wrong options are wrong (tutor only):**
  A) That's mutate().
  C) That's select().
  D) That's arrange().
- **Hint:** Rows or columns?

### ch04-hw-06-v2
- **Kind:** AI-written version of ch04-hw-06
- **Concepts:** dplyr verbs
- **Type:** MC
- **Question:**

Which code keeps only penguins heavier than 5000 g?

- **Options:**

  A) penguins |> filter(body_mass > 5000)
  B) penguins |> select(body_mass > 5000)
  C) penguins |> mutate(body_mass > 5000)
  D) penguins |> arrange(body_mass > 5000)

- **Answer (tutor only):** A
- **Explanation (tutor only):** filter() keeps rows where the condition is TRUE.
- **Why the wrong options are wrong (tutor only):**
  B) select() picks columns.
  C) mutate() would add a TRUE/FALSE column.
  D) arrange() sorts.
- **Hint:** Which verb keeps rows?

### ch04-quiz-01
- **Kind:** Course original
- **Concepts:** dplyr verbs; Errors & debugging
- **Type:** MC
- **Question:**

In a fresh R session, you type:

iris |>
  mutate(PetalLength2PetalWidth = Petal.Length / PetalWidth)

and get:
Error in mutate(iris, PetalLength2PetalWidth = Petal.Length/PetalWidth) : could not find function "mutate"

What is the most likely explanation?

- **Options:**

  A) The iris dataset is not loaded
  B) The dplyr package is not loaded
  C) You cannot have a number in a variable name in R
  D) Either PetalWidth or Petal.Length is misspelled
  E) You did not reassign iris after adding the column with mutate
  F) You did not tell R you wanted dplyr::mutate()
  G) You did not save the R script

- **Answer (tutor only):** B
- **Explanation (tutor only):** 'Could not find function' means R doesn't know mutate() at all. mutate() comes from dplyr, which isn't loaded in a fresh session. Fix: library(dplyr).
- **Why the wrong options are wrong (tutor only):**
  A) iris is built into R, and a missing dataset gives 'object not found', not 'could not find function'.
  C) Numbers are allowed in names (just not at the start).
  D) A misspelled column gives 'object not found'; R hasn't even got that far.
  E) Reassigning matters for keeping the result, not for running the code.
  F) dplyr::mutate() would also work, but the underlying reason is that dplyr isn't loaded. (Choosing between same-named functions matters for filter(), not here.)
  G) Saving a script doesn't affect whether code runs.
- **Hint:** Is R complaining about a function or an object?

### ch04-quiz-01-v1
- **Kind:** AI-written version of ch04-quiz-01
- **Concepts:** dplyr verbs; Errors & debugging
- **Type:** MC
- **Question:**

In a fresh R session you type:

penguins |>
  select(species, body_mass)

and get: could not find function "select". Most likely explanation?

- **Options:**

  A) dplyr isn't loaded
  B) body_mass is misspelled
  C) penguins wasn't reassigned
  D) select() only works in scripts

- **Answer (tutor only):** A
- **Explanation (tutor only):** 'could not find function' means the package providing it isn't loaded: add library(dplyr).
- **Why the wrong options are wrong (tutor only):**
  B) A misspelled column gives 'object not found'.
  C) Reassignment isn't involved.
  D) select() works anywhere.
- **Hint:** What does 'could not find function' usually mean?

### ch04-quiz-01-v2
- **Kind:** AI-written version of ch04-quiz-01
- **Concepts:** dplyr verbs; Errors & debugging
- **Type:** MC
- **Question:**

Match the error to its likely cause. 'could not find function "mutate"' most likely means:

- **Options:**

  A) The package containing mutate() isn't loaded (or the name is misspelled)
  B) A column name is misspelled
  C) The result wasn't saved
  D) The data file is missing

- **Answer (tutor only):** A
- **Explanation (tutor only):** R doesn't know a function called mutate in this session: load dplyr (or check the spelling).
- **Why the wrong options are wrong (tutor only):**
  B) That gives 'object not found'.
  C) Unsaved results don't cause errors.
  D) A missing file gives a 'does not exist' error.
- **Hint:** Function problem or object problem?

### ch04-quiz-02
- **Kind:** Course original
- **Concepts:** dplyr verbs; Errors & debugging
- **Type:** MC
- **Question:**

You load dplyr and rerun:

iris |>
  mutate(PetalLength2PetalWidth = Petal.Length / PetalWidth)

Now you get a new error: object 'PetalWidth' not found. (The iris columns are Sepal.Length, Sepal.Width, Petal.Length, Petal.Width and Species.) What is the most likely explanation?

- **Options:**

  A) The iris dataset is not loaded
  B) The dplyr package is not loaded
  C) You cannot have a number in a variable name in R
  D) Either PetalWidth or Petal.Length is the wrong name for the column
  E) You did not reassign iris after adding the column with mutate
  F) You did not save the R script

- **Answer (tutor only):** D
- **Explanation (tutor only):** The column is called Petal.Width (with a dot), but the code says PetalWidth. R can't find a column by that name. Names in R must match exactly.
- **Why the wrong options are wrong (tutor only):**
  A) iris is built in.
  B) dplyr is now loaded, so mutate() was found.
  C) The new name PetalLength2PetalWidth is fine; numbers are allowed in names.
  E) Reassigning wouldn't fix a misspelled column.
  F) Saving doesn't affect whether code runs.
- **Hint:** Compare the column names in the code with the real column names, character by character.

### ch04-quiz-02-v1
- **Kind:** AI-written version of ch04-quiz-02
- **Concepts:** dplyr verbs; Errors & debugging
- **Type:** MC
- **Question:**

With dplyr loaded, you run:

penguins |>
  mutate(mass_kg = bodymass / 1000)

and get: object 'bodymass' not found. The columns are species, island, bill_length, bill_depth, flipper_length, body_mass and sex. Most likely explanation?

- **Options:**

  A) The column name is misspelled; it's body_mass
  B) dplyr isn't loaded
  C) penguins wasn't reassigned
  D) You can't divide in mutate()

- **Answer (tutor only):** A
- **Explanation (tutor only):** 'object not found' inside mutate() usually means a typo in a column name.
- **Why the wrong options are wrong (tutor only):**
  B) If dplyr weren't loaded, R couldn't find mutate().
  C) Not saving doesn't cause errors.
  D) Arithmetic works in mutate().
- **Hint:** Compare the name you typed with the column list.

### ch04-quiz-02-v2
- **Kind:** AI-written version of ch04-quiz-02
- **Concepts:** dplyr verbs; Errors & debugging
- **Type:** MC
- **Question:**

You get object 'Bill_Length' not found, but the column is bill_length. Why?

- **Options:**

  A) R is case-sensitive, so Bill_Length and bill_length are different names
  B) The column was deleted
  C) dplyr isn't loaded
  D) Column names can't contain underscores

- **Answer (tutor only):** A
- **Explanation (tutor only):** Capitalization matters in R names.
- **Why the wrong options are wrong (tutor only):**
  B) The column exists with lowercase letters.
  C) That would give a 'could not find function' error.
  D) Underscores are fine.
- **Hint:** Compare the capitalization.

### ch04-quiz-03
- **Kind:** Course original
- **Concepts:** dplyr verbs; Assignment & the environment
- **Type:** MC
- **Question:**

You fix the column name, and now this code runs and prints iris with the new column:

iris |>
  mutate(PetalLength2PetalWidth = Petal.Length / Petal.Width)

But when you type View(iris), the new column is gone. What happened?

- **Options:**

  A) The iris dataset is not loaded
  B) The dplyr package is not loaded
  C) You cannot have a number in a variable name in R
  D) Either PetalWidth or Petal.Length is misspelled
  E) You did not reassign iris after adding the column with mutate
  F) You did not save the R script

- **Answer (tutor only):** E
- **Explanation (tutor only):** mutate() returns a new version of the data and prints it, but nothing saved it. To keep the column, assign the result: iris <- iris |> mutate(...).
- **Why the wrong options are wrong (tutor only):**
  A) to D) The code ran successfully, so none of these can be the problem.
  F) Saving the script saves your code, not the objects R created.
- **Hint:** Did anything get saved with <- ?

### ch04-quiz-03-v1
- **Kind:** AI-written version of ch04-quiz-03
- **Concepts:** dplyr verbs; Assignment & the environment
- **Type:** MC
- **Question:**

This code runs and prints penguins with a new mass_kg column:

penguins |>
  mutate(mass_kg = body_mass / 1000)

But when you type View(penguins), mass_kg is gone. What happened?

- **Options:**

  A) You didn't assign the result back to penguins (or to a new object)
  B) dplyr isn't loaded
  C) The column name is misspelled
  D) View() hides new columns

- **Answer (tutor only):** A
- **Explanation (tutor only):** dplyr verbs return a new table; without <- the result is printed and then lost.
- **Why the wrong options are wrong (tutor only):**
  B) The code ran, so dplyr is loaded.
  C) The column appeared in the printout.
  D) View() shows all columns.
- **Hint:** Was anything assigned with <- ?

### ch04-quiz-03-v2
- **Kind:** AI-written version of ch04-quiz-03
- **Concepts:** dplyr verbs; Assignment & the environment
- **Type:** MC
- **Question:**

Which line permanently adds mass_kg to the penguins object?

- **Options:**

  A) penguins <- penguins |> mutate(mass_kg = body_mass / 1000)
  B) penguins |> mutate(mass_kg = body_mass / 1000)
  C) mutate(mass_kg = body_mass / 1000)
  D) View(penguins |> mutate(mass_kg = body_mass / 1000))

- **Answer (tutor only):** A
- **Explanation (tutor only):** Assigning the result back to penguins replaces the old version with the new one.
- **Why the wrong options are wrong (tutor only):**
  B) and D) Only display the result.
  C) Doesn't say which data to use.
- **Hint:** Look for <-.

### ch04-quiz-04
- **Kind:** Course original
- **Concepts:** dplyr verbs
- **Type:** matching
- **Question:**

Match each R function with what it does to the data:

1. filter()
2. View()
3. mutate()
4. select()

- **Options:**

  A) Makes a new column
  B) Shows the data
  C) Only returns columns of interest
  D) Only retains rows passing some logical criteria

- **Answer (tutor only):** 1-D, 2-B, 3-A, 4-C
- **Explanation (tutor only):** filter() works on rows, select() works on columns, mutate() adds (or changes) columns, and View() opens the data to look at.
- **Why the wrong options are wrong (tutor only):**
  Common mix-up: filter() and select(). Remember: filter rows, select columns.
- **Hint:** Which two functions act on columns, and which one acts on rows?

### ch04-quiz-04-v1
- **Kind:** AI-written version of ch04-quiz-04
- **Concepts:** dplyr verbs
- **Type:** matching
- **Question:**

Match each dplyr function with what it does:

1. arrange()
2. summarize()
3. rename()
4. filter()

- **Options:**

  A) Changes column names
  B) Sorts rows
  C) Keeps rows that meet a condition
  D) Collapses rows into summary values

- **Answer (tutor only):** 1-B, 2-D, 3-A, 4-C
- **Explanation (tutor only):** arrange() sorts, summarize() collapses to summaries, rename() changes names, filter() keeps rows.
- **Why the wrong options are wrong (tutor only):**
  Confusing filter() (rows) with select() (columns), or summarize() with mutate(), are the common mix-ups.
- **Hint:** Rows, columns, names or summaries?

### ch04-quiz-04-v2
- **Kind:** AI-written version of ch04-quiz-04
- **Concepts:** dplyr verbs
- **Type:** MC
- **Question:**

You want one new column per row (e.g., each penguin's mass in kg). Which verb?

- **Options:**

  A) mutate()
  B) summarize()
  C) select()
  D) filter()

- **Answer (tutor only):** A
- **Explanation (tutor only):** mutate() adds a column calculated for each row.
- **Why the wrong options are wrong (tutor only):**
  B) summarize() gives one value per group.
  C) select() picks columns.
  D) filter() keeps rows.
- **Hint:** One value per row.

### ch04-quiz-05
- **Kind:** Course original
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

The tibble below is called score. Is it tidy?

game | points | minutes
1 | 24 | 30
2 | 12 | 20

- **Options:**

  A) Yes
  B) No

- **Answer (tutor only):** A
- **Explanation (tutor only):** Each row is one game (an observation), each column is one variable (game, points, minutes), and each cell holds one value.
- **Why the wrong options are wrong (tutor only):**
  B) Nothing breaks the tidy rules: one observation per row, one variable per column, one value per cell.
- **Hint:** Check: one row per game? one column per variable?

### ch04-quiz-05-v1
- **Kind:** AI-written version of ch04-quiz-05
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

The table below is called surveys. Is it tidy?

transect | date | frogs_seen
T1 | 2024-05-01 | 3
T2 | 2024-05-01 | 0

- **Options:**

  A) Yes
  B) No

- **Answer (tutor only):** A
- **Explanation (tutor only):** One row per transect-survey, one column per variable, one value per cell.
- **Why the wrong options are wrong (tutor only):**
  B) Nothing breaks the tidy rules.
- **Hint:** Check the three rules.

### ch04-quiz-05-v2
- **Kind:** AI-written version of ch04-quiz-05
- **Concepts:** Tidy data
- **Type:** MC
- **Question:**

The table below is called surveys. Is it tidy?

transect | May1_frogs | May8_frogs
T1 | 3 | 5
T2 | 0 | 1

- **Options:**

  A) Yes
  B) No

- **Answer (tutor only):** B
- **Explanation (tutor only):** Date is a variable, but its values are in the column names. Tidy: columns transect, date, frogs_seen.
- **Why the wrong options are wrong (tutor only):**
  A) Values of a variable (dates) appear as column headers.
- **Hint:** Where are the dates stored?

## Chapter 5: Univariate summaries

### ch05-book-01
- **Kind:** Course original
- **Concepts:** Shape of distributions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-book-rivers-hist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-book-rivers-hist.png)
- **Question:**

The histogram shows river lengths after a log10 transformation. The distribution is best described as:

- **Options:**

  A) unimodal and symmetric
  B) unimodal and right skewed
  C) bimodal

- **Answer (tutor only):** B
- **Explanation (tutor only):** There is one main peak (around 2.5), and a long tail stretches to the right (out to 3.6). Even after log-transforming, the data are still right skewed, though much less so than raw river lengths.
- **Why the wrong options are wrong (tutor only):**
  A) The right tail is clearly longer than the left.
  C) Small bumps in the tail (one or two rivers per bar) are noise, not a second mode.
- **Hint:** Count the main peaks, then compare the tails.

### ch05-book-01-v1
- **Kind:** AI-written version of ch05-book-01
- **Concepts:** Shape of distributions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-var-parasite-hist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-var-parasite-hist.png)
- **Question:**

The histogram shows parasite load in 350 sheep. Which transformation would make it more symmetric?

- **Options:**

  A) A log transformation
  B) Squaring the values
  C) Subtracting the mean
  D) No transformation can change the shape

- **Answer (tutor only):** A
- **Explanation (tutor only):** Logs compress large values more than small ones, pulling in a long right tail. Squaring would make the skew worse; subtracting the mean just shifts the data.
- **Why the wrong options are wrong (tutor only):**
  B) Squaring stretches large values even more.
  C) Shifting doesn't change shape.
  D) Monotonic transformations like log do change shape.
- **Hint:** Which transformation shrinks big numbers the most?

### ch05-book-01-v2
- **Kind:** AI-written version of ch05-book-01
- **Concepts:** Shape of distributions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-ripen-pop.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-ripen-pop.png)
- **Question:**

The histogram shows the day of year fruit ripened on 5,000 plants. The distribution is:

- **Options:**

  A) unimodal and symmetric
  B) unimodal and right skewed
  C) unimodal and left skewed
  D) bimodal

- **Answer (tutor only):** C
- **Explanation (tutor only):** One peak late in the season, with a long tail toward earlier days: unimodal and left skewed.
- **Why the wrong options are wrong (tutor only):**
  A) Not symmetric.
  B) The long tail points left, toward small values.
  D) One peak.
- **Hint:** Which way does the long tail point?

### ch05-book-02
- **Kind:** Course original
- **Concepts:** Shape of distributions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-book-iris-hist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-book-iris-hist.png)
- **Question:**

The histogram shows iris sepal width. The distribution is best described as:

- **Options:**

  A) unimodal and symmetric
  B) unimodal and right skewed
  C) bimodal

- **Answer (tutor only):** A
- **Explanation (tutor only):** One peak near 3, with the bars dropping off about equally on both sides. That's unimodal and symmetric, roughly bell-shaped.
- **Why the wrong options are wrong (tutor only):**
  B) The two tails are about the same length.
  C) There's only one peak.
- **Hint:** Would the histogram look about the same if you flipped it left to right?

### ch05-book-02-v1
- **Kind:** AI-written version of ch05-book-02
- **Concepts:** Shape of distributions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch08-var-oak-hist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch08-var-oak-hist.png)
- **Question:**

The histogram shows the heights of 600 trees. The distribution is:

- **Options:**

  A) unimodal and symmetric
  B) unimodal and right skewed
  C) bimodal

- **Answer (tutor only):** A
- **Explanation (tutor only):** One peak, roughly mirror-image sides: unimodal and symmetric.
- **Why the wrong options are wrong (tutor only):**
  B) Neither tail is clearly longer.
  C) One peak.
- **Hint:** Would it look similar flipped?

### ch05-book-02-v2
- **Kind:** AI-written version of ch05-book-02
- **Concepts:** Shape of distributions; Center: mean & median
- **Type:** MC
- **Question:**

For a unimodal, symmetric distribution, how do the mean and median compare?

- **Options:**

  A) They're about equal
  B) The mean is much larger
  C) The median is much larger
  D) There's no relationship

- **Answer (tutor only):** A
- **Explanation (tutor only):** With no long tail pulling it, the mean sits at about the same place as the median (and the peak).
- **Why the wrong options are wrong (tutor only):**
  B) That's typical of right skew.
  C) That's typical of left skew.
  D) Shape and these summaries are closely linked.
- **Hint:** What would pull the mean away from the middle?

### ch05-book-03
- **Kind:** Course original
- **Concepts:** Shape of distributions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-book-faithful-hist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-book-faithful-hist.png)
- **Question:**

This histogram of waiting times between eruptions of the Old Faithful geyser uses only 4 bins. With more bins, the data turn out to be clearly bimodal (peaks near 55 and 80 minutes). What's the lesson?

- **Options:**

  A) Too few bins can hide the shape of a distribution, so try several bin sizes
  B) The 4-bin histogram is correct; the data are left skewed
  C) More bins always distort a histogram, so use as few as possible
  D) Bin size only changes the y-axis, not the shape

- **Answer (tutor only):** A
- **Explanation (tutor only):** With 4 wide bins, the two humps get merged, and the plot looks unimodal and left skewed. Bin width is a choice: too few bins hide features, while too many make noise look like structure. Try a few and see what's robust.
- **Why the wrong options are wrong (tutor only):**
  B) The apparent left skew comes from the coarse bins.
  C) Too many bins can make noise look like structure, but too few hide real structure.
  D) Bin size changes how values are grouped, so it changes the apparent shape.
- **Hint:** What happens to two nearby peaks if they land in the same wide bin?

### ch05-book-03-v1
- **Kind:** AI-written version of ch05-book-03
- **Concepts:** Shape of distributions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-var-beak-2bins.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-var-beak-2bins.png), [ch05-var-beak-30bins.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-var-beak-30bins.png)
- **Question:**

The first histogram of finch beak depth uses only 2 bins. The second shows the same data with 30 bins. What's the lesson?

- **Options:**

  A) Too few bins can hide important features like bimodality, so try several bin widths
  B) The 2-bin version is more honest because it's simpler
  C) Bin width never changes what you see
  D) More bins always mislead

- **Answer (tutor only):** A
- **Explanation (tutor only):** With 2 bins, the two beak types merge and you can't see them. With 30, two clear peaks appear. Always try a few bin widths.
- **Why the wrong options are wrong (tutor only):**
  B) Simpler isn't better if it hides structure.
  C) It clearly does.
  D) Too many bins add noise, but too few hide structure.
- **Hint:** What does the 30-bin version reveal?

### ch05-book-03-v2
- **Kind:** AI-written version of ch05-book-03
- **Concepts:** Shape of distributions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [fix-hist-100bins.png](https://yanivjb.github.io/biostats-book/study_guide/images/fix-hist-100bins.png)
- **Question:**

This histogram shows 40 measurements using 100 bins. What's the problem?

- **Options:**

  A) Too many bins: noise looks like structure
  B) Too few bins
  C) The data must be bimodal
  D) Nothing; more bins is always better

- **Answer (tutor only):** A
- **Explanation (tutor only):** With 40 points spread over 100 bins, most bins hold 0, 1 or 2 points, so random bumps and gaps dominate. Use fewer bins (or a density plot) to see the overall shape.
- **Why the wrong options are wrong (tutor only):**
  B) The opposite problem.
  C) Jaggedness doesn't mean multiple modes.
  D) Too many bins add noise.
- **Hint:** How many points land in each bin?

### ch05-book-04
- **Kind:** Course original
- **Concepts:** Center: mean & median
- **Type:** MC
- **Question:**

I calculated the mean penguin body mass two ways:

penguins |>
  summarise(n_samples = n(),
            sum_mass = sum(body_mass, na.rm = TRUE),
            mean_mass_1 = sum_mass / n_samples,
            mean_mass_2 = mean(body_mass, na.rm = TRUE))

n_samples | sum_mass | mean_mass_1 | mean_mass_2
344 | 1437000 | 4177.326 | 4201.754

(Two penguins are missing body mass, NA.)

Which mean is correct?

- **Options:**

  A) mean_mass_1
  B) mean_mass_2
  C) It depends

- **Answer (tutor only):** B
- **Explanation (tutor only):** mean() with na.rm = TRUE adds the non-missing values and divides by the number of non-missing values. mean_mass_1 divides the same sum by all 344 rows, including the 2 with no data, so it's too small.
- **Why the wrong options are wrong (tutor only):**
  A) It divides by 344, but only 342 penguins have a body mass.
  C) Only one is the mean of the observed data.
- **Hint:** How many values went into sum_mass? How many did we divide by?

### ch05-book-04-v1
- **Kind:** AI-written version of ch05-book-04
- **Concepts:** Center: mean & median
- **Type:** MC
- **Question:**

I calculated mean frog mass two ways:

frogs |>
  summarize(n_frogs = n(),
            total = sum(mass, na.rm = TRUE),
            mean_1 = total / n_frogs,
            mean_2 = mean(mass, na.rm = TRUE))

n_frogs | total | mean_1 | mean_2
50 | 690 | 13.8 | 15.0

(Four frogs have missing mass, NA.)

Which mean is correct?

- **Options:**

  A) mean_1
  B) mean_2
  C) It depends

- **Answer (tutor only):** B
- **Explanation (tutor only):** 690 g comes from the 46 frogs with data, so the mean is 690 / 46 = 15.0. mean_1 divides by all 50 rows.
- **Why the wrong options are wrong (tutor only):**
  A) Divides by 50 but only 46 frogs contributed to the total.
  C) Only one is the mean of the measured frogs.
- **Hint:** How many frogs contributed to the total?

### ch05-book-04-v2
- **Kind:** AI-written version of ch05-book-04
- **Concepts:** Center: mean & median
- **Type:** MC
- **Question:**

A column has values 4, 6, NA and 10. What does mean(x) return in R, and what does mean(x, na.rm = TRUE) return?

- **Options:**

  A) NA, and 6.67
  B) 5, and 6.67
  C) 6.67, and 6.67
  D) An error, and 5

- **Answer (tutor only):** A
- **Explanation (tutor only):** Any NA makes mean() return NA unless you ask it to drop missing values. With na.rm = TRUE: (4 + 6 + 10) / 3 = 6.67.
- **Why the wrong options are wrong (tutor only):**
  B) 20 / 4 = 5 treats NA as zero, which R doesn't do.
  C) The first call returns NA.
  D) No error, and the second answer is 6.67.
- **Hint:** What does R do with NA by default?

### ch05-book-05
- **Kind:** Course original
- **Concepts:** Center: mean & median
- **Type:** MC
- **Question:**

I calculated the mean penguin body mass two ways:

penguins |>
  summarise(n_samples = n(),
            sum_mass = sum(body_mass, na.rm = TRUE),
            mean_mass_1 = sum_mass / n_samples,
            mean_mass_2 = mean(body_mass, na.rm = TRUE))

n_samples | sum_mass | mean_mass_1 | mean_mass_2
344 | 1437000 | 4177.326 | 4201.754

(Two penguins are missing body mass, NA.)

What went wrong in calculating mean_mass_1?

- **Options:**

  A) n() counts the number of rows, but we need the number of non-NA values
  B) na.rm should be set to TRUE, not T
  C) The denominator for the mean is (n − 1), not n
  D) Nothing; both are potentially correct depending on your goals

- **Answer (tutor only):** A
- **Explanation (tutor only):** sum(..., na.rm = TRUE) skips the 2 missing values, but n() still counts all 344 rows. So the numerator and denominator don't match.
- **Why the wrong options are wrong (tutor only):**
  B) T and TRUE mean the same thing.
  C) n − 1 is for the variance, not the mean.
  D) Dividing a 342-penguin sum by 344 isn't a valid mean of anything.
- **Hint:** Does n() know which rows are NA?

### ch05-book-05-v1
- **Kind:** AI-written version of ch05-book-05
- **Concepts:** Center: mean & median
- **Type:** MC
- **Question:**

I calculated mean frog mass two ways:

frogs |>
  summarize(n_frogs = n(),
            total = sum(mass, na.rm = TRUE),
            mean_1 = total / n_frogs,
            mean_2 = mean(mass, na.rm = TRUE))

n_frogs | total | mean_1 | mean_2
50 | 690 | 13.8 | 15.0

(Four frogs have missing mass, NA.)

What went wrong with mean_1?

- **Options:**

  A) n() counts all rows, including the 4 with missing mass
  B) na.rm should be FALSE
  C) The mean should divide by n − 1
  D) Nothing; both are valid

- **Answer (tutor only):** A
- **Explanation (tutor only):** The total skips NAs but n() doesn't, so the numerator and denominator don't match.
- **Why the wrong options are wrong (tutor only):**
  B) Then the total would be NA.
  C) n − 1 is for variance.
  D) Dividing a 46-frog total by 50 isn't a valid mean.
- **Hint:** Does n() know which rows are NA?

### ch05-book-05-v2
- **Kind:** AI-written version of ch05-book-05
- **Concepts:** Center: mean & median
- **Type:** MC
- **Question:**

How can you count only the non-missing values of mass inside summarize()?

- **Options:**

  A) sum(!is.na(mass))
  B) n()
  C) length(mass)
  D) mean(mass)

- **Answer (tutor only):** A
- **Explanation (tutor only):** !is.na(mass) is TRUE for each non-missing value, and sum() counts the TRUEs.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Count all rows, including NAs.
  D) That's the mean, not a count.
- **Hint:** How do you turn 'is it missing?' into a count?

### ch05-book-06
- **Kind:** Course original
- **Concepts:** Spread: variance & SD; Coefficient of variation
- **Type:** MC
- **Question:**

Body mass (g) by penguin species:

species | sd_mass | var_mass | mean_mass
Adelie | 459 | 210283 | 3701
Chinstrap | 384 | 147713 | 3733
Gentoo | 504 | 254133 | 5076

Accounting for species differences in mean body mass, which species shows the greatest variability in body mass?

- **Options:**

  A) Adelie
  B) Chinstrap
  C) Gentoo

- **Answer (tutor only):** A
- **Explanation (tutor only):** Use the coefficient of variation, CV = SD / mean: Adelie 459/3701 ≈ 0.124, Chinstrap 384/3733 ≈ 0.103, Gentoo 504/5076 ≈ 0.099. Adelie is the most variable relative to its mean.
- **Why the wrong options are wrong (tutor only):**
  C) Gentoo has the largest SD and variance, but also a much larger mean. Relative to its size, it's the least variable.
  B) Chinstrap has a mean similar to Adelie's but a smaller SD.
- **Hint:** 'Accounting for the mean' means dividing the SD by the mean.

### ch05-book-06-v1
- **Kind:** AI-written version of ch05-book-06
- **Concepts:** Spread: variance & SD; Coefficient of variation
- **Type:** MC
- **Question:**

Seed mass (mg) in three populations:

population | mean | sd
Pop 1 | 2.1 | 0.42
Pop 2 | 3.8 | 0.57
Pop 3 | 1.2 | 0.30

Which is most variable relative to its mean?

- **Options:**

  A) Pop 1
  B) Pop 2
  C) Pop 3

- **Answer (tutor only):** C
- **Explanation (tutor only):** CV = SD / mean: Pop 1 0.20, Pop 2 0.15, Pop 3 0.25. Pop 3 is the most variable relative to its size.
- **Why the wrong options are wrong (tutor only):**
  B) Largest SD, but also the largest mean: the least variable relatively.
  A) Middle CV.
- **Hint:** Divide each SD by its mean.

### ch05-book-06-v2
- **Kind:** AI-written version of ch05-book-06
- **Concepts:** Coefficient of variation
- **Type:** MC
- **Question:**

Two traits: wing length (mean 50 mm, SD 5 mm) and wing mass (mean 0.20 g, SD 0.04 g). Which varies more relative to its mean?

- **Options:**

  A) Wing mass (CV 0.20 vs 0.10)
  B) Wing length, because 5 > 0.04
  C) They're equal
  D) Different units can't be compared

- **Answer (tutor only):** A
- **Explanation (tutor only):** CV: length 5 / 50 = 0.10; mass 0.04 / 0.20 = 0.20.
- **Why the wrong options are wrong (tutor only):**
  B) Raw SDs in different units can't be compared directly.
  C) The CVs differ.
  D) CV is unitless.
- **Hint:** Compute SD / mean for each.

### ch05-book-07
- **Kind:** Course original
- **Concepts:** Center: mean & median; Spread: variance & SD; Range, IQR & boxplots
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-book-lakehuron-boxplot.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-book-lakehuron-boxplot.png)
- **Question:**

The boxplot summarizes the level of Lake Huron (in feet) every year from 1875 to 1972. Roughly, what is the:

1. Mean
2. Median
3. Mode
4. Interquartile range
5. Range
6. Variance

- **Options:**

  A) six
  B) one and three quarters
  C) five hundred seventy-nine
  D) we cannot estimate this from a boxplot

- **Answer (tutor only):** 1-D, 2-C, 3-D, 4-B, 5-A, 6-D
- **Explanation (tutor only):** A boxplot shows five numbers: min, Q1, median, Q3 and max. The median line is about 579. The box runs from about 578.1 to 579.9, so IQR ≈ 1.75. The whiskers run from about 576 to 582, so range ≈ 6. The mean, mode and variance are not shown. Skew can tell you which side of the median the mean is probably on (here the plot is roughly symmetric, so near 579), but you can't read the mean off the plot.
- **Why the wrong options are wrong (tutor only):**
  Mean: here it is probably near 579, since the box looks roughly symmetric, but a boxplot doesn't show it.
  IQR ≠ range: the IQR is just the box, and the range is whisker tip to whisker tip.
- **Hint:** Which five numbers does a boxplot actually show?

### ch05-book-07-v1
- **Kind:** AI-written version of ch05-book-07
- **Concepts:** Center: mean & median; Spread: variance & SD; Range, IQR & boxplots
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-var-box-sym.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-var-box-sym.png)
- **Question:**

From the horizontal boxplot of nest height, which of these can you read off, and roughly what are they?

1. Median
2. Mean
3. Interquartile range
4. Variance

- **Options:**

  A) about 52 cm
  B) about 9 cm
  C) can't be read from a boxplot

- **Answer (tutor only):** 1-A, 2-C, 3-B, 4-C
- **Explanation (tutor only):** A boxplot shows the median (≈ 52), the quartiles (IQR ≈ 9) and the extremes. It doesn't show the mean or the variance. (Here the box is symmetric, so the mean is probably close to the median.)
- **Why the wrong options are wrong (tutor only):**
  Mean and variance aren't drawn on a boxplot.
- **Hint:** Which five numbers does a boxplot show?

### ch05-book-07-v2
- **Kind:** AI-written version of ch05-book-07
- **Concepts:** Range, IQR & boxplots
- **Type:** select-all
- **Question:**

Which of these does a standard boxplot display directly? (Select all that apply.)

- **Options:**

  A) Median
  B) First and third quartiles
  C) Mean
  D) Standard deviation
  E) Outliers

- **Answer (tutor only):** A, B, E
- **Explanation (tutor only):** Boxplots show the median, the quartiles (box edges), the whiskers and individual outliers. The mean and SD aren't drawn.
- **Why the wrong options are wrong (tutor only):**
  C) and D) Not part of a standard boxplot.
- **Hint:** Think: five-number summary plus outliers.

### ch05-book-08
- **Kind:** Course original
- **Concepts:** Spread: variance & SD
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-book-hybrid-ss.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-book-hybrid-ss.png)
- **Question:**

Brooke planted RILs at four locations and measured the proportion of hybrid seed at each: GC = 0.15, LB = 0.23, SR = 0.18, US = 0.03. The grand mean is 0.15. The plot shows each location's squared deviation from the grand mean as a pink square.

What is the sum of squares for the differences between each location's proportion hybrid and the grand mean?

- **Answer (tutor only):** 0.0217
- **Explanation (tutor only):** Deviations: 0, 0.08, 0.03, −0.12. Squares: 0, 0.0064, 0.0009, 0.0144. Sum = 0.0217. In the plot, these are the areas of the pink squares. US (0.03) contributes the most.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: not squaring (deviations sum to about 0); squaring 0.12 as 0.0144 but writing 0.144.
- **Hint:** Each pink square's area is a squared deviation. Add them up.

### ch05-book-08-v1
- **Kind:** AI-written version of ch05-book-08
- **Concepts:** Spread: variance & SD
- **Type:** numeric
- **Question:**

Germination rates at four sites are 0.40, 0.55, 0.60 and 0.45 (grand mean = 0.50). What is the sum of squares of the deviations from the grand mean?

- **Answer (tutor only):** 0.025
- **Explanation (tutor only):** Deviations: −0.10, 0.05, 0.10, −0.05. Squares: 0.01, 0.0025, 0.01, 0.0025. Sum = 0.025.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: not squaring (sum ≈ 0), or squaring 0.05 as 0.025.
- **Hint:** Square each deviation, then add.

### ch05-book-08-v2
- **Kind:** AI-written version of ch05-book-08
- **Concepts:** Spread: variance & SD
- **Type:** numeric
- **Question:**

Clutch sizes at three sites are 3, 5 and 7 eggs (mean = 5). What is the sum of squares?

- **Answer (tutor only):** 8
- **Explanation (tutor only):** (3 − 5)² + (5 − 5)² + (7 − 5)² = 4 + 0 + 4 = 8.
- **Why the wrong options are wrong (tutor only):**
  Forgetting to square gives 0.
- **Hint:** Square, then add.

### ch05-book-09
- **Kind:** Course original
- **Concepts:** Spread: variance & SD
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-book-hybrid-ss.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-book-hybrid-ss.png)
- **Question:**

Brooke planted RILs at four locations and measured the proportion of hybrid seed at each: GC = 0.15, LB = 0.23, SR = 0.18, US = 0.03. The grand mean is 0.15. The plot shows each location's squared deviation from the grand mean as a pink square.

The sum of squares is 0.0217. What are the sample variance and the standard deviation?

- **Answer (tutor only):** variance ≈ 0.0072; SD ≈ 0.085
- **Explanation (tutor only):** Variance = SS / (n − 1) = 0.0217 / 3 ≈ 0.0072. SD = √0.0072 ≈ 0.085, back in the original units (proportion hybrid).
- **Why the wrong options are wrong (tutor only):**
  Dividing by n = 4 gives 0.0054 (that's the population formula).
  Forgetting the square root mixes up variance and SD.
- **Hint:** n = 4 locations. Divide by n − 1, then take the square root for the SD.

### ch05-book-09-v1
- **Kind:** AI-written version of ch05-book-09
- **Concepts:** Spread: variance & SD
- **Type:** numeric
- **Question:**

Germination rates at four sites have a sum of squares of 0.025. What are the sample variance and SD?

- **Answer (tutor only):** variance ≈ 0.0083; SD ≈ 0.091
- **Explanation (tutor only):** Variance = 0.025 / 3 ≈ 0.0083. SD = √0.0083 ≈ 0.091.
- **Why the wrong options are wrong (tutor only):**
  Dividing by 4 gives 0.00625.
  Forgetting the square root mixes up variance and SD.
- **Hint:** n − 1 = 3; then take the square root.

### ch05-book-09-v2
- **Kind:** AI-written version of ch05-book-09
- **Concepts:** Spread: variance & SD
- **Type:** numeric
- **Question:**

Three clutch sizes (3, 5, 7) have a sum of squares of 8. What are the sample variance and SD?

- **Answer (tutor only):** variance = 4; SD = 2
- **Explanation (tutor only):** Variance = 8 / 2 = 4; SD = √4 = 2.
- **Why the wrong options are wrong (tutor only):**
  Dividing by 3 gives 2.67.
- **Hint:** Divide by n − 1, then square root.

### ch05-book-10
- **Kind:** Course original
- **Concepts:** Coefficient of variation
- **Type:** MC
- **Question:**

Proportion hybrid seed across four locations has mean 0.15 and SD ≈ 0.085. Petal area among RILs has mean 62 mm² and SD 14.3 mm². Accounting for differences in their means, how does their variability compare?

- **Options:**

  A) They are very similar
  B) Petal area among RILs is roughly thirty times as variable
  C) Proportion hybrid seed among sites is roughly two times as variable
  D) You can't compare variability for traits measured on such different scales

- **Answer (tutor only):** C
- **Explanation (tutor only):** CV = SD / mean. Hybrid seed: 0.085/0.15 ≈ 0.57. Petal area: 14.3/62 ≈ 0.23. 0.57 / 0.23 ≈ 2.5, so hybrid proportion is roughly twice as variable relative to its mean.
- **Why the wrong options are wrong (tutor only):**
  B) That compares raw SDs (14.3 vs 0.085, actually about 170 times), which mostly reflects the different units.
  D) That's exactly what the CV is for: it's unitless.
  A) The CVs are about 0.57 and 0.23: more than twice as different.
- **Hint:** Divide each SD by its mean, then compare.

### ch05-book-10-v1
- **Kind:** AI-written version of ch05-book-10
- **Concepts:** Coefficient of variation
- **Type:** MC
- **Question:**

Nectar volume has mean 2 µL and SD 1 µL. Flower width has mean 40 mm and SD 4 mm. Accounting for their means, how does their variability compare?

- **Options:**

  A) Nectar volume is about five times as variable (CV 0.5 vs 0.1)
  B) Flower width is more variable because 4 > 1
  C) They're equally variable
  D) They can't be compared

- **Answer (tutor only):** A
- **Explanation (tutor only):** CV: nectar 1 / 2 = 0.5; width 4 / 40 = 0.1. Nectar varies five times as much relative to its mean.
- **Why the wrong options are wrong (tutor only):**
  B) Raw SDs in different units mislead.
  C) The CVs differ fivefold.
  D) The CV is unitless.
- **Hint:** SD / mean for each.

### ch05-book-10-v2
- **Kind:** AI-written version of ch05-book-10
- **Concepts:** Coefficient of variation
- **Type:** MC
- **Question:**

If you converted flower width from mm to cm, what would happen to its SD and its CV?

- **Options:**

  A) The SD would shrink 10-fold; the CV would stay the same
  B) Both would shrink 10-fold
  C) Neither would change
  D) The CV would grow 10-fold

- **Answer (tutor only):** A
- **Explanation (tutor only):** Units change the SD (and the mean) by the same factor, so their ratio, the CV, is unchanged. That's why the CV can compare traits measured in different units.
- **Why the wrong options are wrong (tutor only):**
  B) The CV is unitless.
  C) The SD changes with units.
  D) The CV doesn't depend on units.
- **Hint:** Mean and SD both change by the same factor.

### ch05-book-11
- **Kind:** Course original
- **Concepts:** Spread: variance & SD; Coefficient of variation
- **Type:** MC
- **Question:**

Why is it important to standardize by the mean when comparing variability between variables?

- **Options:**

  A) Because the SD depends on the scale and units of measurement: bigger numbers tend to vary by bigger amounts, so dividing by the mean puts variables on a common, unitless scale
  B) Because the mean is always larger than the SD
  C) Because dividing by the mean removes outliers
  D) Because variables with larger means are always more variable

- **Answer (tutor only):** A
- **Explanation (tutor only):** If you measured petal area in cm² instead of mm², the SD would shrink 100-fold even though nothing biological changed. The CV (SD / mean) is unaffected by units, so it compares relative variability fairly.
- **Why the wrong options are wrong (tutor only):**
  B) Not necessarily true, and irrelevant anyway.
  C) Dividing doesn't remove any data points.
  D) Larger values often vary more in absolute terms, which is exactly why we standardize. Relative variability can be larger or smaller.
- **Hint:** What would happen to the SD of petal area if you switched from mm² to cm²?

### ch05-book-11-v1
- **Kind:** AI-written version of ch05-book-11
- **Concepts:** Spread: variance & SD; Coefficient of variation
- **Type:** MC
- **Question:**

A student says: 'Elephant mass is more variable than mouse mass because its SD is 500 kg and the mouse SD is 3 g.' What's the flaw?

- **Options:**

  A) SDs scale with the size and units of the trait; comparing variability fairly requires dividing by the mean (CV)
  B) Nothing; bigger SD means more variable
  C) Mice can't be weighed precisely
  D) Elephants should be weighed in grams

- **Answer (tutor only):** A
- **Explanation (tutor only):** Big things vary by big amounts. The CV compares relative variability on a unitless scale.
- **Why the wrong options are wrong (tutor only):**
  B) Raw SDs mostly reflect scale here.
  C) Not the issue.
  D) Changing units changes the SD but not the conclusion; the CV is the fix.
- **Hint:** What would the CVs say?

### ch05-book-11-v2
- **Kind:** AI-written version of ch05-book-11
- **Concepts:** Coefficient of variation
- **Type:** MC
- **Question:**

Which statement about the coefficient of variation is true?

- **Options:**

  A) It is SD divided by the mean, and has no units
  B) It is the variance divided by n
  C) It has the same units as the data
  D) It only works for normally distributed data

- **Answer (tutor only):** A
- **Explanation (tutor only):** CV = SD / mean, so the units cancel and traits on different scales can be compared.
- **Why the wrong options are wrong (tutor only):**
  B) That's not the CV.
  C) Units cancel.
  D) It's used regardless of shape (though it needs positive values).
- **Hint:** What happens to the units when you divide SD by the mean?

### ch05-book-12
- **Kind:** Course original
- **Concepts:** Summaries in R
- **Type:** MC
- **Question:**

What is wrong with the code below? (Pick the most egregious issue.)

iris <- iris |>
  summarise(mean_sepal_length = mean(Sepal.Length))

- **Options:**

  A) I overwrote iris and lost the raw data
  B) I did not show the output
  C) I used summarise() rather than summarize()
  D) I did not tell R to remove missing data when calculating the mean

- **Answer (tutor only):** A
- **Explanation (tutor only):** summarise() collapses iris into one row. Assigning that to iris replaces the whole data set with a single number. Save summaries under a new name.
- **Why the wrong options are wrong (tutor only):**
  B) Not printing is harmless; you can print it later.
  C) Both spellings are the same function.
  D) iris has no missing values, and even if it did, that's a minor issue compared to losing the data.
- **Hint:** After this runs, what's left in iris?

### ch05-book-12-v1
- **Kind:** AI-written version of ch05-book-12
- **Concepts:** Summaries in R
- **Type:** MC
- **Question:**

What is the most serious problem here?

penguins <- penguins |>
  summarize(max_mass = max(body_mass, na.rm = TRUE))

- **Options:**

  A) penguins is replaced by a single number, so the raw data are lost
  B) max() should be mean()
  C) It should be summarise()
  D) na.rm = TRUE isn't needed

- **Answer (tutor only):** A
- **Explanation (tutor only):** Save summaries under a new name; don't overwrite your data.
- **Why the wrong options are wrong (tutor only):**
  B) Which summary to use is a separate question.
  C) Both spellings work.
  D) It's needed if any values are NA.
- **Hint:** What's in penguins afterward?

### ch05-book-12-v2
- **Kind:** AI-written version of ch05-book-12
- **Concepts:** Summaries in R
- **Type:** MC
- **Question:**

You accidentally ran `iris <- iris |> summarize(m = mean(Sepal.Length))`. What's the easiest way to get iris back?

- **Options:**

  A) Restart R (or remove your copy) so the built-in iris is available again, and fix the line
  B) Run the line again
  C) It's gone forever
  D) Type undo()

- **Answer (tutor only):** A
- **Explanation (tutor only):** Built-in datasets come back in a fresh session (or with rm(iris)). For your own data, rerun the script from the top, which is why scripts matter.
- **Why the wrong options are wrong (tutor only):**
  B) Running it again summarizes the summary.
  C) The original is restored from the package.
  D) R has no undo().
- **Hint:** Your script and fresh sessions are your safety net.

### ch05-gquiz-01
- **Kind:** Course original
- **Concepts:** Center: mean & median; Spread: variance & SD; Range, IQR & boxplots
- **Type:** select-all
- **Question:**

Which TWO of the following summaries are largely unaffected by rare extreme values?

- **Options:**

  A) range
  B) 3rd quartile
  C) mean
  D) median
  E) variance

- **Answer (tutor only):** B, D
- **Explanation (tutor only):** Quantiles, such as the median and the 3rd quartile, depend only on the order of the values. Changing the most extreme value barely moves them.
- **Why the wrong options are wrong (tutor only):**
  A) The range is max − min, so it is set entirely by the extremes.
  C) The mean uses every value, so one huge value pulls it toward itself.
  E) The variance squares deviations, so extreme values have an outsized effect.
- **Hint:** Which summaries are based on the ordered position of values, rather than on their size?

### ch05-gquiz-01-v1
- **Kind:** AI-written version of ch05-gquiz-01
- **Concepts:** Center: mean & median; Spread: variance & SD; Range, IQR & boxplots
- **Type:** select-all
- **Question:**

One lizard in your sample is a giant (twice the size of any other). Which TWO summaries would barely change if you removed it?

- **Options:**

  A) mean
  B) median
  C) standard deviation
  D) interquartile range
  E) maximum

- **Answer (tutor only):** B, D
- **Explanation (tutor only):** The median and IQR depend on the middle of the ordered data, so one extreme value barely moves them.
- **Why the wrong options are wrong (tutor only):**
  A) The mean is pulled toward the giant.
  C) The SD is inflated by the large deviation.
  E) The maximum is the giant itself.
- **Hint:** Which summaries depend on order, not size?

### ch05-gquiz-01-v2
- **Kind:** AI-written version of ch05-gquiz-01
- **Concepts:** Center: mean & median
- **Type:** MC
- **Question:**

A dataset of household incomes includes a few billionaires. Which summary best describes a typical household?

- **Options:**

  A) The median
  B) The mean
  C) The range
  D) The variance

- **Answer (tutor only):** A
- **Explanation (tutor only):** The median is the middle value, so it isn't dragged upward by a few extreme incomes.
- **Why the wrong options are wrong (tutor only):**
  B) The mean is pulled far up by the billionaires.
  C) and D) Measures of spread, not of a typical value.
- **Hint:** Which center isn't pulled by extremes?

### ch05-gquiz-02
- **Kind:** Course original
- **Concepts:** Spread: variance & SD
- **Type:** MC
- **Question:**

You correctly calculate a variance of zero in a sample of size 30. What must be TRUE?

- **Options:**

  A) Half of the numbers are above the mean
  B) All of the values are zero
  C) The numbers are evenly spaced around the mean
  D) All values are equal

- **Answer (tutor only):** D
- **Explanation (tutor only):** Variance is the average squared distance from the mean. Squares can't be negative, so the only way the total is zero is for every value to be exactly at the mean, i.e. all values are equal.
- **Why the wrong options are wrong (tutor only):**
  A) and C) Both describe data with some spread, which gives a variance above zero.
  B) All values must be the same, but not necessarily zero; thirty 5s also have variance 0.
- **Hint:** Can a squared deviation be negative? What has to happen for them all to add to zero?

### ch05-gquiz-02-v1
- **Kind:** AI-written version of ch05-gquiz-02
- **Concepts:** Spread: variance & SD
- **Type:** MC
- **Question:**

A sample of 12 seeds has a standard deviation of 0. What must be true?

- **Options:**

  A) All 12 seeds have the same mass
  B) All seeds weigh 0 mg
  C) Half the seeds are above the mean
  D) The seeds were weighed incorrectly

- **Answer (tutor only):** A
- **Explanation (tutor only):** SD = 0 means no deviations from the mean at all, so every value is identical.
- **Why the wrong options are wrong (tutor only):**
  B) They must be equal, not necessarily zero.
  C) That describes data with spread.
  D) Identical values are possible (e.g., rounded measurements).
- **Hint:** When can the average squared deviation be zero?

### ch05-gquiz-02-v2
- **Kind:** AI-written version of ch05-gquiz-02
- **Concepts:** Spread: variance & SD
- **Type:** MC
- **Question:**

Which dataset has the larger variance?
Set 1: 10, 10, 10, 10
Set 2: 8, 9, 11, 12

- **Options:**

  A) Set 1
  B) Set 2
  C) They're equal
  D) Can't tell without the means

- **Answer (tutor only):** B
- **Explanation (tutor only):** Set 1 has no spread (variance 0). Set 2 has the same mean (10) but values spread around it (variance ≈ 3.3).
- **Why the wrong options are wrong (tutor only):**
  A) No variation means variance 0.
  C) Same mean, different spread.
  D) Both means are 10, and spread is visible directly.
- **Hint:** Which set has values away from the mean?

### ch05-gquiz-03
- **Kind:** Course original
- **Concepts:** Center: mean & median; Spread: variance & SD; Range, IQR & boxplots
- **Type:** MC
- **Question:**

Which of the following values is likely to increase with an increase in the sample size?

- **Options:**

  A) Sample mean
  B) Sample variance
  C) Sample range
  D) Sample IQR

- **Answer (tutor only):** C
- **Explanation (tutor only):** The range depends on the most extreme values, and the more you sample, the more likely you are to catch a rare extreme one. So the range tends to grow with sample size. The other summaries estimate a fixed population value: they get more precise, but they don't drift up.
- **Why the wrong options are wrong (tutor only):**
  A), B) and D) These estimate population values (mean, variance, IQR), so they settle near the true value as n grows. They don't systematically increase.
- **Hint:** If you sample more individuals, which summary can only stay the same or get bigger as you add data?

### ch05-gquiz-03-v1
- **Kind:** AI-written version of ch05-gquiz-03
- **Concepts:** Spread: variance & SD; Range, IQR & boxplots
- **Type:** MC
- **Question:**

You measure heights in a sample of 20 trees, then in a sample of 500 trees from the same forest. Which summary is most likely to be larger in the bigger sample?

- **Options:**

  A) Mean
  B) Median
  C) Range
  D) Standard deviation

- **Answer (tutor only):** C
- **Explanation (tutor only):** The range is set by the most extreme trees. A bigger sample is more likely to include very short and very tall trees, so the range tends to grow.
- **Why the wrong options are wrong (tutor only):**
  A), B) and D) These estimate population values and don't trend upward with n.
- **Hint:** Which summary can only stay the same or grow when you add data?

### ch05-gquiz-03-v2
- **Kind:** AI-written version of ch05-gquiz-03
- **Concepts:** Spread: variance & SD; Range, IQR & boxplots
- **Type:** MC
- **Question:**

Why is the range a poor summary for comparing samples of very different sizes?

- **Options:**

  A) It tends to grow with sample size, because larger samples catch more extreme values
  B) It can't be calculated for large samples
  C) It always equals the SD
  D) It ignores the minimum

- **Answer (tutor only):** A
- **Explanation (tutor only):** A bigger sample is more likely to include rare extremes, so the range depends on n as well as on the population.
- **Why the wrong options are wrong (tutor only):**
  B) It can always be calculated.
  C) Not true.
  D) The range uses both the minimum and the maximum.
- **Hint:** What happens to the extremes as you sample more?

### ch05-gquiz-04
- **Kind:** Course original
- **Concepts:** Shape of distributions; Center: mean & median; Range, IQR & boxplots
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-gquiz-boxplot.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-gquiz-boxplot.png)
- **Question:**

Use the boxplot to visually estimate:

1. The median
2. The interquartile range
3. The range
4. The mean

- **Options:**

  A) about 10
  B) about 4
  C) a bit below the median (about 3); a boxplot doesn't show it directly
  D) about 3.8
  E) about 7.3

- **Answer (tutor only):** 1-D, 2-B, 3-A, 4-C
- **Explanation (tutor only):** The median is the thick line (about 3.8). The box runs from Q1 (about 1) to Q3 (about 4.9), so IQR ≈ 3.9 ≈ 4. The range runs from the bottom whisker (about −2.6) to the top (about 7.3), so ≈ 10. A boxplot doesn't show the mean, but the long lower whisker and the median near the top of the box suggest left skew, which pulls the mean below the median.
- **Why the wrong options are wrong (tutor only):**
  7.3 is the maximum, not the range (range = max − min).
  The IQR is the height of the box, not the median.
  A boxplot shows the median, not the mean.
- **Hint:** The middle line is the median. The box edges are Q1 and Q3. Range = max − min. Which way is the long tail?

### ch05-gquiz-04-v1
- **Kind:** AI-written version of ch05-gquiz-04
- **Concepts:** Shape of distributions; Center: mean & median; Range, IQR & boxplots
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-var-box-right.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-var-box-right.png)
- **Question:**

Use the boxplot of time to first flower to estimate:

1. The median
2. The range
3. The mean
4. The direction of skew

- **Options:**

  A) about 45
  B) about 10
  C) a bit above the median; a boxplot doesn't show it directly
  D) right skewed (long upper tail)

- **Answer (tutor only):** 1-B, 2-A, 3-C, 4-D
- **Explanation (tutor only):** The median line is near 10 days and the values run from about 1 to 46 (≈ 45). The long upper whisker and the high outliers show right skew, which pulls the mean above the median.
- **Why the wrong options are wrong (tutor only):**
  Don't stop the range at the whisker: include the outlier points.
  The mean isn't drawn on a boxplot.
- **Hint:** Which way is the long tail?

### ch05-gquiz-04-v2
- **Kind:** AI-written version of ch05-gquiz-04
- **Concepts:** Shape of distributions; Center: mean & median; Range, IQR & boxplots
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [fix-skewed-boxplot.png](https://yanivjb.github.io/biostats-book/study_guide/images/fix-skewed-boxplot.png)
- **Question:**

Here is a boxplot of a sample. What can you say about the mean?

- **Options:**

  A) It's probably above the median, because the data are right skewed
  B) It's probably below the median
  C) It equals the median
  D) Nothing at all

- **Answer (tutor only):** A
- **Explanation (tutor only):** The median sits low in the box, the upper whisker is longer than the lower one, and there are several high outliers: the data are right skewed. A long upper tail pulls the mean above the median. The boxplot doesn't show the mean, but the skew tells you its likely direction.
- **Why the wrong options are wrong (tutor only):**
  B) That would be for left skew.
  C) Only for symmetric data.
  D) The shape does give a clue.
- **Hint:** Which way would the long tail pull the mean?

### ch05-gquiz-05
- **Kind:** Course original
- **Concepts:** Spread: variance & SD
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-gquiz-lollipop.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-gquiz-lollipop.png)
- **Question:**

The plot shows the proportion of each of 7 females' eggs fertilized by males from another population. The dotted blue line is the mean (about 0.41), and the black lines show each value's deviation from the mean.

Reading approximate values off the plot (x1 to x7: 0.15, 0.22, 0.30, 0.37, 0.38, 0.50, 0.95), estimate the sample variance.

Recall: Var = SS / (n − 1), where SS = Σ(Xi − X̄)².

- **Answer (tutor only):** about 0.07 (anything from about 0.06 to 0.08 is fine)
- **Explanation (tutor only):** Deviations from 0.41: −0.26, −0.19, −0.11, −0.04, −0.03, 0.09, 0.54. Squared: 0.068, 0.036, 0.012, 0.002, 0.001, 0.008, 0.292. SS ≈ 0.418, so Var ≈ 0.418 / 6 ≈ 0.07 (SD ≈ 0.26). Notice that x7 alone contributes about 70% of the SS: squaring makes big deviations dominate.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: dividing by n (7) instead of n − 1 (6); forgetting to square the deviations (they sum to 0); reporting the SD (≈ 0.26) instead of the variance.
- **Hint:** Subtract the mean from each value, square, add them up, then divide by n − 1.

### ch05-gquiz-05-v1
- **Kind:** AI-written version of ch05-gquiz-05
- **Concepts:** Spread: variance & SD
- **Type:** numeric
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-var-lollipop.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-var-lollipop.png)
- **Question:**

The plot shows wing lengths of 7 butterflies (11, 14, 16, 18, 20, 21, 26 mm) and their deviations from the mean (18 mm). What is the sample variance? (Two decimals.)

- **Answer (tutor only):** 24.33
- **Explanation (tutor only):** Deviations: −7, −4, −2, 0, 2, 3, 8. Squares: 49, 16, 4, 0, 4, 9, 64. SS = 146. Variance = 146 / 6 ≈ 24.33.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: dividing by 7 (20.86), or forgetting to square.
- **Hint:** Square each deviation, add, divide by n − 1.

### ch05-gquiz-05-v2
- **Kind:** AI-written version of ch05-gquiz-05
- **Concepts:** Spread: variance & SD
- **Type:** numeric
- **Question:**

Five lizards have tail lengths of 6, 8, 9, 11 and 16 cm (mean = 10). What is the sample standard deviation? (Two decimals.)

- **Answer (tutor only):** 3.81
- **Explanation (tutor only):** Deviations: −4, −2, −1, 1, 6. Squares: 16, 4, 1, 1, 36 → SS = 58. Variance = 58 / 4 = 14.5. SD = √14.5 ≈ 3.81.
- **Why the wrong options are wrong (tutor only):**
  Dividing by 5 gives SD ≈ 3.41.
  Forgetting the square root gives the variance (14.5).
- **Hint:** SS → variance (n − 1) → square root.

### ch05-gquiz-06
- **Kind:** Course original
- **Concepts:** Summaries in R
- **Type:** select-all
- **Question:**

I try to estimate the variance in Iris setosa sepal length with the code below, but it doesn't work. What is wrong? (select all that apply)

library(dplyr)
iris |>
    dplyr::summarize(var_sl = var(Sepal.Length)) |>
    dplyr::filter(Species =  setosa)

- **Options:**

  A) The filter comes after summarize(), so the Species column no longer exists (and the variance would be for all species anyway)
  B) = should be == inside filter()
  C) setosa needs quotes: "setosa"
  D) var() can't be used inside summarize()
  E) dplyr:: should not be written before function names

- **Answer (tutor only):** A, B, C
- **Explanation (tutor only):** Order matters in a pipeline: summarize() collapses iris into one row with only var_sl, so there is no Species left to filter on. Filter first, then summarize. Also, == tests equality (= is for assigning arguments), and setosa is a value, not an object, so it needs quotes. Fixed:

iris |>
  filter(Species == "setosa") |>
  summarize(var_sl = var(Sepal.Length))
- **Why the wrong options are wrong (tutor only):**
  D) Any summary function, including var(), mean() and sd(), works inside summarize().
  E) dplyr:: is optional but harmless; it just names the package explicitly.
- **Hint:** Read the pipe step by step: after summarize(), what columns are left?

### ch05-gquiz-06-v1
- **Kind:** AI-written version of ch05-gquiz-06
- **Concepts:** Summaries in R
- **Type:** select-all
- **Question:**

This code tries to get the mean body mass of Gentoo penguins, but it doesn't work. What's wrong? (Select all that apply.)

penguins |>
  summarize(mean_mass = mean(body_mass)) |>
  filter(species = Gentoo)

- **Options:**

  A) filter() comes after summarize(), so species no longer exists
  B) = should be ==
  C) Gentoo needs quotes
  D) mean() can't be used inside summarize()

- **Answer (tutor only):** A, B, C
- **Explanation (tutor only):** Filter first, then summarize: penguins |> filter(species == "Gentoo") |> summarize(mean_mass = mean(body_mass, na.rm = TRUE)).
- **Why the wrong options are wrong (tutor only):**
  D) Summary functions like mean() are exactly what summarize() uses.
- **Hint:** After summarize(), what columns remain?

### ch05-gquiz-06-v2
- **Kind:** AI-written version of ch05-gquiz-06
- **Concepts:** Summaries in R
- **Type:** MC
- **Question:**

Which code gives the SD of flipper length for Adelie penguins only?

- **Options:**

  A) penguins |> filter(species == "Adelie") |> summarize(sd_flip = sd(flipper_len, na.rm = TRUE))
  B) penguins |> summarize(sd_flip = sd(flipper_len)) |> filter(species == "Adelie")
  C) penguins |> filter(species = "Adelie") |> summarize(sd(flipper_len))
  D) penguins |> select(species == "Adelie") |> sd(flipper_len)

- **Answer (tutor only):** A
- **Explanation (tutor only):** Keep the Adelie rows first, then summarize them.
- **Why the wrong options are wrong (tutor only):**
  B) After summarize(), species is gone.
  C) = instead of ==.
  D) select() picks columns, and sd() isn't a pipe step on a data frame.
- **Hint:** Filter, then summarize.

### ch05-gquiz-07
- **Kind:** Course original
- **Concepts:** Center: mean & median
- **Type:** MC
- **Question:**

The following are high temperatures for a week in August: 94, 93, 98, 101, 98, 96, and 93. What is the largest increase in the highest temperature that doesn't change the median temperature?

- **Options:**

  A) Infinity degrees
  B) Two degrees
  C) Five degrees
  D) 8 degrees

- **Answer (tutor only):** A
- **Explanation (tutor only):** Sorted: 93, 93, 94, 96, 98, 98, 101. The median is the middle (4th) value, 96. Making the hottest day hotter, by any amount, doesn't change which value is in the middle. The median is robust to extremes.
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) Any increase in the maximum leaves the median at 96; there is no limit. (The mean, by contrast, would change with any increase.)
- **Hint:** Sort the values. Which one is the median? Does changing the largest value move it?

### ch05-gquiz-07-v1
- **Kind:** AI-written version of ch05-gquiz-07
- **Concepts:** Center: mean & median
- **Type:** MC
- **Question:**

Seven frogs have masses 12, 15, 15, 17, 19, 22 and 24 g. What is the largest amount you could add to the heaviest frog's mass without changing the median?

- **Options:**

  A) No limit: any amount
  B) 2 g
  C) 5 g
  D) It would always change the median

- **Answer (tutor only):** A
- **Explanation (tutor only):** The median is the 4th of 7 ordered values (17 g). Making the heaviest frog heavier doesn't change which value is in the middle.
- **Why the wrong options are wrong (tutor only):**
  B) and C) There's no limit.
  D) The median ignores how extreme the largest value is.
- **Hint:** Which value is the median, and does it move?

### ch05-gquiz-07-v2
- **Kind:** AI-written version of ch05-gquiz-07
- **Concepts:** Center: mean & median
- **Type:** MC
- **Question:**

Seven frogs have masses 12, 15, 15, 17, 19, 22 and 24 g. If the heaviest frog's mass is recorded as 240 g by mistake, what happens?

- **Options:**

  A) The mean rises a lot; the median stays at 17 g
  B) Both rise a lot
  C) The median rises; the mean stays the same
  D) Neither changes

- **Answer (tutor only):** A
- **Explanation (tutor only):** The mean uses every value: (124 + 216 extra) / 7 jumps from about 17.7 to about 48.6 g. The median is still the 4th value, 17 g.
- **Why the wrong options are wrong (tutor only):**
  B) The median is robust to one extreme value.
  C) Backwards.
  D) The mean changes.
- **Hint:** Mean uses sizes; median uses order.

### ch05-gquiz-08
- **Kind:** Course original
- **Concepts:** Spread: variance & SD; Coefficient of variation
- **Type:** matching
- **Question:**

Imagine you were at a track meet.

1. The variance in 100-meter dash times is probably ______ the variance in mile run times.
2. The coefficient of variation in 100-meter dash times is probably ______ the coefficient of variation in mile run times.

- **Options:**

  A) smaller than
  B) greater than
  C) similar to

- **Answer (tutor only):** 1-A, 2-C
- **Explanation (tutor only):** Mile times are much longer (minutes versus seconds), so runners differ by many more seconds, which gives a much larger variance. The coefficient of variation (SD / mean) scales spread by the mean, so relative variability can be similar for the two events.
- **Why the wrong options are wrong (tutor only):**
  Variance is in squared units of the data, so longer races naturally have bigger variance. CV removes that scale effect.
- **Hint:** Variance depends on the scale of the measurement. CV = SD / mean. What happens when you divide out the mean?

### ch05-gquiz-08-v1
- **Kind:** AI-written version of ch05-gquiz-08
- **Concepts:** Spread: variance & SD; Coefficient of variation
- **Type:** matching
- **Question:**

Elephants and mice both vary in body mass.

1. The SD of body mass is probably ______ in elephants than in mice.
2. After dividing by the mean (CV), variability in elephants is probably ______ that in mice.

- **Options:**

  A) much larger
  B) much smaller
  C) roughly similar to

- **Answer (tutor only):** 1-A, 2-C
- **Explanation (tutor only):** Elephants weigh thousands of kilograms, so differences among them are huge in absolute terms. Relative to their mean (CV), the variation can be similar to that of mice.
- **Why the wrong options are wrong (tutor only):**
  Raw SD depends on the scale; CV removes it.
- **Hint:** SD has units; CV doesn't.

### ch05-gquiz-08-v2
- **Kind:** AI-written version of ch05-gquiz-08
- **Concepts:** Spread: variance & SD; Coefficient of variation
- **Type:** MC
- **Question:**

Tree height SD is 3 m (mean 30 m); seedling height SD is 2 cm (mean 10 cm). Which is more variable relative to its mean?

- **Options:**

  A) Seedlings (CV = 0.20 vs 0.10)
  B) Trees, because 3 m is bigger than 2 cm
  C) Equal
  D) Can't compare different units

- **Answer (tutor only):** A
- **Explanation (tutor only):** CV = SD / mean: trees 3 / 30 = 0.10; seedlings 2 / 10 = 0.20. Seedlings vary twice as much relative to their size.
- **Why the wrong options are wrong (tutor only):**
  B) Raw SDs depend on units and scale.
  C) The CVs differ.
  D) CV is unitless, which is exactly what makes the comparison possible.
- **Hint:** Divide each SD by its mean.

### ch05-quiz-01
- **Kind:** Course original
- **Concepts:** Shape of distributions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-quiz-bodymass-hist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-quiz-bodymass-hist.png)
- **Question:**

The histogram shows penguin body mass. The distribution is BEST described as:

- **Options:**

  A) unimodal and symmetric
  B) unimodal and right skewed
  C) bimodal

- **Answer (tutor only):** B
- **Explanation (tutor only):** There is one clear peak (3500–4000 g), and the right tail stretches out further than the left (toward 6000+ g). That is right skew.
- **Why the wrong options are wrong (tutor only):**
  A) The two sides aren't mirror images: the right tail is longer.
  C) There is only one peak; the bars decline steadily after it.
- **Hint:** Count the peaks, then compare the lengths of the left and right tails.

### ch05-quiz-01-v1
- **Kind:** AI-written version of ch05-quiz-01
- **Concepts:** Shape of distributions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-var-seedmass-hist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-var-seedmass-hist.png)
- **Question:**

The histogram shows seed mass for 400 seeds. The distribution is best described as:

- **Options:**

  A) unimodal and symmetric
  B) unimodal and right skewed
  C) bimodal

- **Answer (tutor only):** B
- **Explanation (tutor only):** One peak near 2.5–3 mg with a long tail toward heavy seeds: unimodal and right skewed (mean 3.5 mg > median 3.0 mg).
- **Why the wrong options are wrong (tutor only):**
  A) The right tail is much longer than the left.
  C) There's only one peak.
- **Hint:** Which side has the long tail?

### ch05-quiz-01-v2
- **Kind:** AI-written version of ch05-quiz-01
- **Concepts:** Shape of distributions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-var-parasite-hist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-var-parasite-hist.png)
- **Question:**

The histogram shows parasite load (eggs per gram) in 350 sheep. The distribution is best described as:

- **Options:**

  A) unimodal and symmetric
  B) unimodal and right skewed
  C) unimodal and left skewed
  D) bimodal

- **Answer (tutor only):** B
- **Explanation (tutor only):** Most sheep have low loads and a few have very high loads, giving a long right tail. Mean (54) is well above the median (40).
- **Why the wrong options are wrong (tutor only):**
  A) Very lopsided.
  C) The long tail is on the right (high values).
  D) One peak.
- **Hint:** Where are most values, and where does the tail go?

### ch05-quiz-02
- **Kind:** Course original
- **Concepts:** Shape of distributions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-quiz-flipper-hist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-quiz-flipper-hist.png)
- **Question:**

The histogram shows penguin flipper length. The distribution is BEST described as:

- **Options:**

  A) unimodal and symmetric
  B) unimodal and right skewed
  C) bimodal

- **Answer (tutor only):** C
- **Explanation (tutor only):** There are two separate peaks (around 190 mm and around 210–215 mm) with a dip between them. Bimodality often means two groups are mixed together; here, different penguin species.
- **Why the wrong options are wrong (tutor only):**
  A) and B) There isn't just one peak: the bars drop around 200 mm and rise again.
- **Hint:** How many humps do you see?

### ch05-quiz-02-v1
- **Kind:** AI-written version of ch05-quiz-02
- **Concepts:** Shape of distributions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-var-beak-bimodal.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-var-beak-bimodal.png)
- **Question:**

The histogram shows beak depth for 400 finches. The distribution is best described as:

- **Options:**

  A) unimodal and symmetric
  B) unimodal and right skewed
  C) bimodal

- **Answer (tutor only):** C
- **Explanation (tutor only):** Two clear peaks (near 9 and 12.5 mm) with a dip between: bimodal. This often means two groups are mixed, e.g., two species or beak morphs.
- **Why the wrong options are wrong (tutor only):**
  A) and B) There are two humps, not one.
- **Hint:** Count the peaks.

### ch05-quiz-02-v2
- **Kind:** AI-written version of ch05-quiz-02
- **Concepts:** Shape of distributions
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-var-temp-hist.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-var-temp-hist.png)
- **Question:**

The histogram shows body temperature for 300 healthy mice. The distribution is best described as:

- **Options:**

  A) unimodal and symmetric
  B) unimodal and right skewed
  C) unimodal and left skewed
  D) bimodal

- **Answer (tutor only):** A
- **Explanation (tutor only):** One peak near 37 °C, falling off about equally on both sides: unimodal and symmetric.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Neither tail is clearly longer.
  D) There's one peak.
- **Hint:** Would it look the same flipped left to right?

### ch05-quiz-03
- **Kind:** Course original
- **Concepts:** Center: mean & median; Range, IQR & boxplots
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-quiz-boxplot.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-quiz-boxplot.png)
- **Question:**

Use the boxplot to visually estimate each value:

1. The mean of y
2. The median of y
3. The range of y
4. The interquartile range of y

- **Options:**

  A) about 7.5
  B) about 19
  C) a bit above 19 (about 20); a boxplot doesn't show it directly
  D) about 23.5
  E) about 34

- **Answer (tutor only):** 1-C, 2-B, 3-D, 4-A
- **Explanation (tutor only):** The thick line is the median (about 19). The box runs from Q1 (about 15.5) to Q3 (about 23), so IQR ≈ 23 − 15.5 = 7.5. The range is max − min, including the outlier point: about 34 − 10.5 = 23.5. A boxplot doesn't show the mean, but the long upper whisker and the high outlier pull the mean slightly above the median.
- **Why the wrong options are wrong (tutor only):**
  34 is the maximum, not the range (range = max − min).
  The box spans the IQR; don't confuse it with the median line or the box's top edge.
  A boxplot shows the median, not the mean.
- **Hint:** The middle line is the median. The box edges are Q1 and Q3. Range = max − min. Don't forget the dot!

### ch05-quiz-03-v1
- **Kind:** AI-written version of ch05-quiz-03
- **Concepts:** Center: mean & median; Range, IQR & boxplots
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-var-box-right.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-var-box-right.png)
- **Question:**

Use the boxplot to visually estimate each value:

1. The median
2. The interquartile range
3. The range
4. The mean

- **Options:**

  A) about 10
  B) about 11
  C) a bit above 10 (about 13); a boxplot doesn't show it directly
  D) about 45
  E) about 33

- **Answer (tutor only):** 1-A, 2-B, 3-D, 4-C
- **Explanation (tutor only):** The median line sits near 10 days. The box runs from about 6 to 17, so IQR ≈ 11. The range runs from the lowest value (~1) to the top outlier (~46), so ≈ 45. A boxplot doesn't show the mean, but the long upper whisker and high outliers pull it above the median.
- **Why the wrong options are wrong (tutor only):**
  33 is the end of the upper whisker, not the range: include the outlier points.
  The IQR is the height of the box, not the median.
- **Hint:** Median = middle line; IQR = box height; range = lowest point to highest point, including outliers.

### ch05-quiz-03-v2
- **Kind:** AI-written version of ch05-quiz-03
- **Concepts:** Center: mean & median; Range, IQR & boxplots
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch05-var-box-sym.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch05-var-box-sym.png)
- **Question:**

Use the horizontal boxplot of nest height to estimate:

1. The median
2. The interquartile range
3. The range

- **Options:**

  A) about 9
  B) about 52
  C) about 31
  D) about 70

- **Answer (tutor only):** 1-B, 2-A, 3-C
- **Explanation (tutor only):** The median line is near 52 cm. The box spans about 48 to 57 cm, so IQR ≈ 9. The whiskers run from about 39 to 70 cm, so the range ≈ 31.
- **Why the wrong options are wrong (tutor only):**
  70 is the maximum, not the range.
  The IQR is the box's width, not the median.
- **Hint:** Box edges = Q1 and Q3; whisker ends = min and max (no outliers here).

### ch05-quiz-04
- **Kind:** Course original
- **Concepts:** Spread: variance & SD
- **Type:** numeric
- **Question:**

The grand mean of penguin flipper lengths is 201 mm. The mean flipper lengths of three penguin species are:

Adelie = 190
Chinstrap = 196
Gentoo = 217

What is the sum of squares for the differences between each species' flipper length and the grand mean?

- **Answer (tutor only):** 402
- **Explanation (tutor only):** Square each deviation from the grand mean, then add: (190 − 201)² + (196 − 201)² + (217 − 201)² = 121 + 25 + 256 = 402.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: adding the deviations without squaring them (−11 − 5 + 16 = 0, which is always 0), or squaring the sum instead of summing the squares.
- **Hint:** Subtract 201 from each value, square each result, then add them up.

### ch05-quiz-04-v1
- **Kind:** AI-written version of ch05-quiz-04
- **Concepts:** Spread: variance & SD
- **Type:** numeric
- **Question:**

The grand mean of chick mass is 50 g. The mean masses in three broods are 44, 51 and 55 g.

What is the sum of squares of the differences between each brood mean and the grand mean?

- **Answer (tutor only):** 62
- **Explanation (tutor only):** (44 − 50)² + (51 − 50)² + (55 − 50)² = 36 + 1 + 25 = 62.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: forgetting to square (−6 + 1 + 5 = 0), or squaring the sum.
- **Hint:** Subtract 50 from each, square, add.

### ch05-quiz-04-v2
- **Kind:** AI-written version of ch05-quiz-04
- **Concepts:** Spread: variance & SD
- **Type:** numeric
- **Question:**

Four tadpoles have tail lengths of 8, 10, 11 and 15 mm (mean = 11 mm). What is the sum of squares?

- **Answer (tutor only):** 26
- **Explanation (tutor only):** Deviations: −3, −1, 0, 4. Squares: 9, 1, 0, 16. Sum = 26.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: adding the raw deviations (always 0), or dividing by n (that's a variance step).
- **Hint:** Square each deviation from the mean, then add.

### ch05-quiz-05
- **Kind:** Course original
- **Concepts:** Spread: variance & SD
- **Type:** numeric
- **Question:**

The grand mean of penguin flipper lengths is 201 mm. The mean flipper lengths of three penguin species are:

Adelie = 190
Chinstrap = 196
Gentoo = 217

The sum of squared differences from the grand mean is 402. What is the sample variance?

- **Answer (tutor only):** 201
- **Explanation (tutor only):** Sample variance = sum of squares / (n − 1) = 402 / (3 − 1) = 201. We divide by n − 1, not n, because the mean was estimated from the same data.
- **Why the wrong options are wrong (tutor only):**
  402 / 3 = 134 uses n instead of n − 1 (that's the population formula).
  √201 ≈ 14.2 is the standard deviation, not the variance.
- **Hint:** Divide the sum of squares by n − 1.

### ch05-quiz-05-v1
- **Kind:** AI-written version of ch05-quiz-05
- **Concepts:** Spread: variance & SD
- **Type:** numeric
- **Question:**

Three brood means (44, 51 and 55 g) have a sum of squares around their grand mean of 62. What is the sample variance?

- **Answer (tutor only):** 31
- **Explanation (tutor only):** Variance = SS / (n − 1) = 62 / 2 = 31.
- **Why the wrong options are wrong (tutor only):**
  62 / 3 ≈ 20.7 divides by n instead of n − 1.
  √31 ≈ 5.6 is the SD, not the variance.
- **Hint:** Divide by n − 1.

### ch05-quiz-05-v2
- **Kind:** AI-written version of ch05-quiz-05
- **Concepts:** Spread: variance & SD
- **Type:** numeric
- **Question:**

Four tadpole tail lengths have a sum of squares of 27. What is the sample standard deviation (to two decimals)?

- **Answer (tutor only):** 3.00
- **Explanation (tutor only):** Variance = 27 / (4 − 1) = 9, so SD = √9 = 3.
- **Why the wrong options are wrong (tutor only):**
  Forgetting the square root gives the variance (9).
  Dividing by 4 gives √6.75 ≈ 2.60.
- **Hint:** Variance first (divide by n − 1), then take the square root.

### ch05-quiz-06
- **Kind:** Course original
- **Concepts:** Summaries in R
- **Type:** MC
- **Question:**

What is the single worst thing about the code below?

penguins <- penguins |>
  summarise(flipper_len = sd(flipper_len))

- **Options:**

  A) I used summarise() instead of summarize()
  B) I calculated the sample standard deviation, not the population standard deviation
  C) I overwrote the penguins data set

- **Answer (tutor only):** C
- **Explanation (tutor only):** summarise() collapses the data to a single row (the SD). Assigning that back to penguins replaces the whole data set with one number, so every later analysis breaks. Save summaries to a new name, e.g. flipper_summary <- ...
- **Why the wrong options are wrong (tutor only):**
  A) summarise() and summarize() are the same function; the spelling doesn't matter.
  B) sd() gives the sample SD, which is almost always what we want, since our data are a sample.
- **Hint:** After this runs, what is left in penguins?

### ch05-quiz-06-v1
- **Kind:** AI-written version of ch05-quiz-06
- **Concepts:** Summaries in R
- **Type:** MC
- **Question:**

What is the single worst thing about this code?

frogs <- frogs |>
  summarize(mean_mass = mean(mass))

- **Options:**

  A) It uses summarize() instead of summarise()
  B) It overwrites frogs with a one-row summary, losing the raw data
  C) It should use the median instead

- **Answer (tutor only):** B
- **Explanation (tutor only):** After this line, frogs holds only the mean. Save summaries under a new name, e.g., frog_summary <- frogs |> summarize(...).
- **Why the wrong options are wrong (tutor only):**
  A) Both spellings work identically.
  C) The choice of summary isn't the main problem; losing the data is.
- **Hint:** What's left in frogs after this runs?

### ch05-quiz-06-v2
- **Kind:** AI-written version of ch05-quiz-06
- **Concepts:** Summaries in R
- **Type:** MC
- **Question:**

Which line safely stores the mean flipper length without losing the penguins data?

- **Options:**

  A) flipper_summary <- penguins |> summarize(mean_flipper = mean(flipper_len, na.rm = TRUE))
  B) penguins <- penguins |> summarize(mean_flipper = mean(flipper_len, na.rm = TRUE))
  C) penguins <- mean(penguins)
  D) summarize(penguins) <- mean(flipper_len)

- **Answer (tutor only):** A
- **Explanation (tutor only):** Assigning the summary to a new name keeps the original data intact.
- **Why the wrong options are wrong (tutor only):**
  B) Overwrites penguins with one row.
  C) and D) Not valid ways to summarize, and C also overwrites.
- **Hint:** Which keeps penguins unchanged?

### ch07-gquiz-02
- **Kind:** Course original
- **Concepts:** Coefficient of variation
- **Type:** MC
- **Question:**

You want to compare the variability in fruit area between apples and oranges. Which statistic should you use?

- **Options:**

  A) The coefficient of variation (SD / mean), because oranges and apples differ in mean size, and bigger things tend to vary by bigger amounts
  B) The variance, because it uses all the data
  C) The range, because it shows the biggest and smallest fruit
  D) The covariance between apple area and orange area

- **Answer (tutor only):** A
- **Explanation (tutor only):** The CV puts variability relative to the mean, so it compares spread fairly between groups with different average sizes.
- **Why the wrong options are wrong (tutor only):**
  B) Variance is in squared units and scales with the mean, so larger fruits would look more variable just because they are larger.
  C) The range depends on extremes and on sample size.
  D) Covariance measures how two variables vary together, which doesn't apply here (apples and oranges aren't paired).
- **Hint:** If oranges were twice as big on average, would you expect their SD to be bigger even if they were 'equally variable'?

### ch07-gquiz-02-v1
- **Kind:** AI-written version of ch07-gquiz-02
- **Concepts:** Coefficient of variation
- **Type:** MC
- **Question:**

You want to compare how variable body mass is in hummingbirds versus eagles. Which statistic is most appropriate?

- **Options:**

  A) The coefficient of variation (SD / mean)
  B) The variance
  C) The standard deviation
  D) The range

- **Answer (tutor only):** A
- **Explanation (tutor only):** Eagles weigh about a thousand times more, so their SD will be far larger even if they're no more variable relative to their size. The CV puts both on a unitless scale.
- **Why the wrong options are wrong (tutor only):**
  B), C) and D) All scale with the size of the animal.
- **Hint:** What happens to the SD when everything is a thousand times bigger?

### ch07-gquiz-02-v2
- **Kind:** AI-written version of ch07-gquiz-02
- **Concepts:** Coefficient of variation
- **Type:** MC
- **Question:**

Petal length: species X has mean 10 mm and SD 2 mm; species Y has mean 40 mm and SD 4 mm. Which is more variable relative to its size?

- **Options:**

  A) X (CV 0.20 vs 0.10)
  B) Y, because 4 > 2
  C) Equal
  D) Can't compare

- **Answer (tutor only):** A
- **Explanation (tutor only):** CV = SD / mean: X 2/10 = 0.20, Y 4/40 = 0.10.
- **Why the wrong options are wrong (tutor only):**
  B) Raw SDs scale with size.
  C) The CVs differ.
  D) The CV allows the comparison.
- **Hint:** Divide each SD by its mean.

## Chapter 6: Associations I

### ch06-book-01
- **Kind:** Course original
- **Concepts:** Two categorical variables
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch06-titanic-bars.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-titanic-bars.png)
- **Question:**

The plot shows survival of adult males on the Titanic in 1st class vs crew, with three geom_bar() positions. Which position makes it easiest to:

1. Read off the number of males in 1st class?
2. Read off the number of male crew members who did not survive?
3. Compare survival probabilities of 1st-class males vs crew?

- **Options:**

  A) dodge
  B) fill
  C) stack

- **Answer (tutor only):** 1-C, 2-A, 3-B
- **Explanation (tutor only):** stack: bar height = group total. dodge: each subgroup count from a common baseline. fill: each bar scaled to 1, so you see the proportion surviving.
- **Why the wrong options are wrong (tutor only):**
  fill hides the counts.
  In stack, the upper segment's count has to be read by subtraction.
  dodge needs mental division to compare proportions.
- **Hint:** Totals, individual counts, or proportions?

### ch06-book-01-v1
- **Kind:** AI-written version of ch06-book-01
- **Concepts:** Two categorical variables
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch06-var-adelie-bars.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-var-adelie-bars.png)
- **Question:**

The plots show Adelie penguins by island (x) and sex (fill), using three geom_bar() positions. Which plot makes it easiest to:

1. Read off the total number of Adelie on Dream island?
2. Compare the proportion of females across islands?
3. Read off the number of males on Torgersen?

- **Options:**

  A) Plot 1
  B) Plot 2
  C) Plot 3

- **Answer (tutor only):** 1-B, 2-A, 3-C
- **Explanation (tutor only):** Plot 1 is "fill" (proportions), Plot 2 is "stack" (totals), and Plot 3 is "dodge" (each count from a common baseline). The proportions are all close to half here.
- **Why the wrong options are wrong (tutor only):**
  Identify the position first: bars all the same height → fill; tallest bars = totals → stack; side-by-side bars → dodge.
- **Hint:** Which plot has bars that all reach 1?

### ch06-book-01-v2
- **Kind:** AI-written version of ch06-book-01
- **Concepts:** Two categorical variables
- **Type:** MC
- **Question:**

A stacked bar chart shows survival (yes/no) for two groups of very different sizes (50 and 500 animals). Why is it hard to compare survival rates from it?

- **Options:**

  A) Stacked bars show counts, so the big group's bar dominates; you'd need fill to compare proportions
  B) Stacked bars can't show two categories
  C) The colors are too similar
  D) Survival can't be plotted

- **Answer (tutor only):** A
- **Explanation (tutor only):** With counts, the 500-animal bar towers over the 50-animal bar; proportions are hidden. position = "fill" scales both to 1.
- **Why the wrong options are wrong (tutor only):**
  B) They can.
  C) Not the main problem.
  D) It can.
- **Hint:** What would make both bars the same height?

### ch06-book-02
- **Kind:** Course original
- **Concepts:** Two categorical variables
- **Type:** matching
- **Question:**

The Titanic data, subset to adult males who were in 1st class or crew (n = 1037):

Class | Survived = Yes | Survived = No | total
1st | 57 | 118 | 175
Crew | 192 | 670 | 862
total | 249 | 788 | 1037

What proportion:

1. were in 1st class?
2. survived?
3. were in 1st class AND survived?
4. survived, given 1st class (P(Survive | 1st))?
5. survived, given crew (P(Survive | Crew))?

- **Options:**

  A) 0.055
  B) 0.169
  C) 0.223
  D) 0.240
  E) 0.326

- **Answer (tutor only):** 1-B, 2-D, 3-A, 4-E, 5-C
- **Explanation (tutor only):** 1. 175/1037 = 0.169. 2. 249/1037 = 0.240. 3. 57/1037 = 0.055 (joint). 4. 57/175 = 0.326. 5. 192/862 = 0.223 (conditional: divide within the row).
- **Why the wrong options are wrong (tutor only):**
  Joint proportions divide by everyone (1037). Conditional proportions divide only by the 'given' group.
- **Hint:** For 'given 1st class,' only look at the 175 people in 1st class.

### ch06-book-02-v1
- **Kind:** AI-written version of ch06-book-02
- **Concepts:** Two categorical variables
- **Type:** matching
- **Question:**

We trapped 100 mice and recorded coat color and habitat:

coat | lava | sand | total
dark | 30 | 10 | 40
light | 5 | 55 | 60
total | 35 | 65 | 100

What proportion of mice:

1. were caught on lava?
2. were dark AND caught on lava?
3. were dark, given they were caught on lava?
4. were dark, given they were caught on sand?

- **Options:**

  A) 0.15
  B) 0.30
  C) 0.35
  D) 0.86

- **Answer (tutor only):** 1-C, 2-B, 3-D, 4-A
- **Explanation (tutor only):** Lava: 35/100 = 0.35. Dark and lava: 30/100 = 0.30. Dark given lava: 30/35 ≈ 0.86. Dark given sand: 10/65 ≈ 0.15.
- **Why the wrong options are wrong (tutor only):**
  Joint: divide by all 100. Conditional: divide by the 'given' column only.
- **Hint:** For 'given lava', look only at the lava column.

### ch06-book-02-v2
- **Kind:** AI-written version of ch06-book-02
- **Concepts:** Two categorical variables
- **Type:** MC
- **Question:**

We trapped 100 mice and recorded coat color and habitat:

coat | lava | sand | total
dark | 30 | 10 | 40
light | 5 | 55 | 60
total | 35 | 65 | 100

What proportion of light-coated mice were caught on sand?

- **Options:**

  A) 55/60 ≈ 0.92
  B) 55/65 ≈ 0.85
  C) 55/100 = 0.55
  D) 60/100 = 0.60

- **Answer (tutor only):** A
- **Explanation (tutor only):** 'Of light mice' → restrict to the 60 light mice; 55 were on sand.
- **Why the wrong options are wrong (tutor only):**
  B) That's P(light | sand).
  C) That's the joint proportion.
  D) That's P(light).
- **Hint:** Which group is the denominator?

### ch06-book-03
- **Kind:** Course original
- **Concepts:** Two categorical variables; Association vs causation
- **Type:** MC
- **Question:**

The Titanic data, subset to adult males who were in 1st class or crew (n = 1037):

Class | Survived = Yes | Survived = No | total
1st | 57 | 118 | 175
Crew | 192 | 670 | 862
total | 249 | 788 | 1037

P(Survive | 1st) = 0.326 and P(Survive | Crew) = 0.223. What do you conclude?

- **Options:**

  A) First-class males were more likely to survive than male crew members
  B) Survival was independent of class; it was safer to be a crew member
  C) It was safer to be crew, because more crew members survived than first-class passengers
  D) Because the joint probability is small, class and survival are unrelated

- **Answer (tutor only):** A
- **Explanation (tutor only):** Compare conditional proportions: 33% of 1st-class males survived vs 22% of crew.
- **Why the wrong options are wrong (tutor only):**
  B) Contradicts itself, and the proportions differ.
  C) More crew survived in raw numbers (192 vs 57) only because there were far more crew. Compare proportions, not counts.
  D) A joint probability being small says nothing about association; it depends on how common each category is.
- **Hint:** Compare the conditional proportions, not the raw counts.

### ch06-book-03-v1
- **Kind:** AI-written version of ch06-book-03
- **Concepts:** Two categorical variables; Association vs causation
- **Type:** MC
- **Question:**

We trapped 100 mice and recorded coat color and habitat:

coat | lava | sand | total
dark | 30 | 10 | 40
light | 5 | 55 | 60
total | 35 | 65 | 100

P(dark | lava) ≈ 0.86 and P(dark | sand) ≈ 0.15. What do you conclude?

- **Options:**

  A) Coat color is strongly associated with habitat: dark mice are far more common on lava
  B) Because more light mice were caught overall, light coats are favored on lava
  C) Coat color and habitat are independent
  D) The joint proportion of dark lava mice is small, so there's no association

- **Answer (tutor only):** A
- **Explanation (tutor only):** Compare conditional proportions: most lava mice are dark and most sand mice are light, a strong association (consistent with camouflage, though this survey alone doesn't prove cause).
- **Why the wrong options are wrong (tutor only):**
  B) Overall counts don't answer a question about lava mice.
  C) The conditional proportions are very different.
  D) A joint proportion's size doesn't measure association.
- **Hint:** Compare conditional proportions, not raw counts.

### ch06-book-03-v2
- **Kind:** AI-written version of ch06-book-03
- **Concepts:** Two categorical variables; Association vs causation
- **Type:** MC
- **Question:**

More women than men survived a shipwreck (300 vs 200), but there were 400 women and 1,600 men aboard. Who was more likely to survive?

- **Options:**

  A) Women (75% vs 12.5%)
  B) Men, because 200 is close to 300
  C) Equally likely
  D) Can't tell

- **Answer (tutor only):** A
- **Explanation (tutor only):** Survival rates: women 300/400 = 75%, men 200/1600 = 12.5%. Compare proportions, not raw counts.
- **Why the wrong options are wrong (tutor only):**
  B) Counts reflect group sizes.
  C) The rates differ sixfold.
  D) The rates can be calculated.
- **Hint:** Divide by each group's size.

### ch06-book-04
- **Kind:** Course original
- **Concepts:** Difference in means & Cohen's d
- **Type:** MC
- **Question:**

Clarkia RILs at site GC were classified as visited (some_visits) or not (no_visits) by pollinators. Anther–stigma distance (mm):

visited | n | mean | sd
no_visits | 66 | 0.821 | 0.375
some_visits | 23 | 0.964 | 0.378

(Pooled SD ≈ 0.376)

What is the difference in mean anther–stigma distance (some_visits − no_visits), and how big is this 'effect' by traditional interpretations of Cohen's d?

- **Options:**

  A) 0.14 mm; small (d ≈ 0.38)
  B) 0.14 mm; large (d ≈ 1.4)
  C) −0.14 mm; small
  D) 0.14 mm; tiny, not worth reporting

- **Answer (tutor only):** A
- **Explanation (tutor only):** 0.964 − 0.821 = 0.143 mm. d = 0.143 / 0.376 ≈ 0.38, which is 'small' by convention (about 0.2 small, 0.5 medium, 0.8 large).
- **Why the wrong options are wrong (tutor only):**
  B) d divides by the SD, not into it: 0.143/0.376 ≈ 0.38, not 1.4.
  C) The order is some_visits − no_visits, so the difference is positive.
  D) 0.38 is above the 0.2 'small' threshold.
- **Hint:** d = difference / pooled SD.

### ch06-book-04-v1
- **Kind:** AI-written version of ch06-book-04
- **Concepts:** Difference in means & Cohen's d
- **Type:** MC
- **Question:**

Bill length (mm) in Gentoo penguins by sex:

sex | n | mean | sd
female | 58 | 45.56 | 2.05
male | 61 | 49.47 | 2.72

(Pooled SD ≈ 2.42)

What is the difference in mean bill length (male − female), and how big is it by traditional Cohen's d benchmarks?

- **Options:**

  A) 3.91 mm; huge or very large (d ≈ 1.6)
  B) 3.91 mm; small (d ≈ 0.3)
  C) −3.91 mm; large
  D) 1.62 mm; large

- **Answer (tutor only):** A
- **Explanation (tutor only):** Difference = 49.47 − 45.56 = 3.91 mm. d = 3.91 / 2.42 ≈ 1.62, well above the 0.8 'large' benchmark.
- **Why the wrong options are wrong (tutor only):**
  B) d is 1.6, not 0.3.
  C) The order is male − female, so it's positive.
  D) 1.62 is d, not the difference in mm.
- **Hint:** Compute the difference, then divide by the pooled SD.

### ch06-book-04-v2
- **Kind:** AI-written version of ch06-book-04
- **Concepts:** Difference in means & Cohen's d
- **Type:** MC
- **Question:**

Two studies report differences: A) 2 mm with pooled SD 10 mm; B) 2 mm with pooled SD 1 mm. Which shows the bigger effect relative to the variation?

- **Options:**

  A) Study B (d = 2.0 vs 0.2)
  B) Study A
  C) Equal, since both differences are 2 mm
  D) Can't compare

- **Answer (tutor only):** A
- **Explanation (tutor only):** Cohen's d scales the difference by the spread: 2/1 = 2.0 is huge, 2/10 = 0.2 is small.
- **Why the wrong options are wrong (tutor only):**
  B) Same difference, but much more noise.
  C) Same raw difference, different d.
  D) d is designed for this.
- **Hint:** Divide each difference by its SD.

### ch06-book-05
- **Kind:** Course original
- **Concepts:** Association vs causation
- **Type:** MC
- **Question:**

Clarkia RILs at site GC were classified as visited (some_visits) or not (no_visits) by pollinators. Anther–stigma distance (mm):

visited | n | mean | sd
no_visits | 66 | 0.821 | 0.375
some_visits | 23 | 0.964 | 0.378

(Pooled SD ≈ 0.376)

From these analyses we conclude (pick best):

- **Options:**

  A) Anther–stigma distance causes pollinators to visit plants more often
  B) Pollinators prefer plants with greater anther–stigma separation
  C) There is no relationship between anther–stigma distance and visitation
  D) Visited plants tend to have greater anther–stigma distance than plants that did not receive visits

- **Answer (tutor only):** D
- **Explanation (tutor only):** D describes the observed association without assuming a cause. A and B make causal claims that these data can't support.
- **Why the wrong options are wrong (tutor only):**
  A) and B) Causal; something else (e.g., flower size) could drive both.
  C) There is a difference (d ≈ 0.38), even if it's small.
- **Hint:** Which answer just describes the pattern?

### ch06-book-05-v1
- **Kind:** AI-written version of ch06-book-05
- **Concepts:** Association vs causation
- **Type:** MC
- **Question:**

Bill length (mm) in Gentoo penguins by sex:

sex | n | mean | sd
female | 58 | 45.56 | 2.05
male | 61 | 49.47 | 2.72

(Pooled SD ≈ 2.42)

Which conclusion is best?

- **Options:**

  A) Male Gentoo penguins tend to have longer bills than females
  B) Being male causes long bills through testosterone
  C) There's no difference in bill length
  D) All males have longer bills than all females

- **Answer (tutor only):** A
- **Explanation (tutor only):** A describes the observed difference in means. Sex differences may well have biological causes, but these summaries alone don't show the mechanism.
- **Why the wrong options are wrong (tutor only):**
  B) A mechanism claim these data can't test.
  C) The difference is large.
  D) The distributions overlap; some females have longer bills than some males.
- **Hint:** Which answer describes the pattern without over-reaching?

### ch06-book-05-v2
- **Kind:** AI-written version of ch06-book-05
- **Concepts:** Association vs causation
- **Type:** MC
- **Question:**

Plants that received more pollinator visits had larger petals on average. Which conclusion is best supported by this observational result?

- **Options:**

  A) Visited plants tend to have larger petals
  B) Large petals attract pollinators
  C) Pollinator visits make petals grow
  D) Petal size and visits are unrelated

- **Answer (tutor only):** A
- **Explanation (tutor only):** A describes the association. B is plausible but needs an experiment (e.g., manipulating petal size) to show cause.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Causal claims, in opposite directions.
  D) The data show an association.
- **Hint:** Description vs explanation.

### ch06-book-06
- **Kind:** Course original
- **Concepts:** Visualizing associations
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch06-asd-plot1.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-asd-plot1.png), [ch06-asd-plot2.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-asd-plot2.png), [ch06-asd-plot3.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-asd-plot3.png), [ch06-asd-plot4.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-asd-plot4.png), [ch06-asd-plot5.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-asd-plot5.png)
- **Question:**

Five plots compare anther–stigma distance between visited and unvisited Clarkia RILs. Which plot is the worst?

Plot 1: jittered points with a line connecting the group means
Plot 2: faceted histograms
Plot 3: overlapping densities (alpha = .4)
Plot 4: boxplot with jittered points on top
Plot 5: geom_jitter(width = 1)

- **Options:**

  A) Plot 1
  B) Plot 2
  C) Plot 3
  D) Plot 4
  E) Plot 5

- **Answer (tutor only):** E
- **Explanation (tutor only):** With width = 1 the jitter is so wide that the two groups' points overlap and you can't tell which point belongs to which group.
- **Why the wrong options are wrong (tutor only):**
  Plots 1–4 each show the two groups clearly, with different trade-offs (individual points, distribution shape, summary).
  A) Plot 1 shows every point plus the group means, so both groups are clear.
  B) Plot 2 shows each group's distribution clearly.
  C) Plot 3's transparency lets you see both groups where they overlap.
  D) Plot 4 shows a summary and the data. That's a great choice.
- **Hint:** In which plot can you not tell the groups apart?

### ch06-book-06-v1
- **Kind:** AI-written version of ch06-book-06
- **Concepts:** Visualizing associations
- **Type:** MC
- **Question:**

Which of these is the worst way to show how a numeric trait differs between two groups?

- **Options:**

  A) Jittered points with the group means connected
  B) Faceted histograms on a shared axis
  C) Overlapping transparent densities
  D) Jittered points spread so widely that the two groups overlap

- **Answer (tutor only):** D
- **Explanation (tutor only):** If the jitter is wider than the space between groups, readers can't tell which point belongs to which group.
- **Why the wrong options are wrong (tutor only):**
  A), B) and C) Each shows the groups clearly, with different trade-offs.
- **Hint:** Which one makes the groups indistinguishable?

### ch06-book-06-v2
- **Kind:** AI-written version of ch06-book-06
- **Concepts:** Visualizing associations
- **Type:** MC
- **Question:**

Which plot best shows both the individual data and a summary for two groups?

- **Options:**

  A) A boxplot with jittered points drawn on top
  B) A bar chart of the two means only
  C) A pie chart
  D) A table of the two means

- **Answer (tutor only):** A
- **Explanation (tutor only):** Boxplot + jittered points shows the distribution, the median and quartiles, and every individual.
- **Why the wrong options are wrong (tutor only):**
  B) and D) Only the means, with no spread or data.
  C) Pie charts compare parts of a whole, not groups' values.
- **Hint:** Which shows the data, not just a summary?

### ch06-gquiz-05
- **Kind:** Course original
- **Concepts:** Difference in means & Cohen's d
- **Type:** MC
- **Question:**

You want to describe the difference in mean fruit area of apples and oranges. When would you report Cohen's d rather than the raw difference in means?

- **Options:**

  A) When you want a unitless effect size relative to the variability in the data, e.g., to compare with other studies or traits measured in different units; the raw difference is better when its units are meaningful to readers (e.g., 'oranges are 12 cm² larger')
  B) Always; the raw difference is never useful
  C) When the two groups have the same mean
  D) Only when the data are categorical

- **Answer (tutor only):** A
- **Explanation (tutor only):** The difference in means is in real units, so it's easy to interpret when those units mean something. Cohen's d scales the difference by the pooled SD, which tells you how big it is relative to the spread and allows comparison across traits or studies.
- **Why the wrong options are wrong (tutor only):**
  B) Raw differences are often more interpretable.
  C) Then both are zero.
  D) Both require a numeric response.
- **Hint:** Which one has units? Which one is relative to the spread?

### ch06-gquiz-05-v1
- **Kind:** AI-written version of ch06-gquiz-05
- **Concepts:** Difference in means & Cohen's d
- **Type:** MC
- **Question:**

When is the raw difference in means (e.g., 'treated plants grew 4 cm taller') more useful than Cohen's d?

- **Options:**

  A) When the units are meaningful to readers and you want to say how much something changed in real terms
  B) Never
  C) Only when the groups have equal sample sizes
  D) When comparing traits measured in different units

- **Answer (tutor only):** A
- **Explanation (tutor only):** Raw differences are directly interpretable ('4 cm taller'). Cohen's d is better for comparing across traits or studies with different units or variability.
- **Why the wrong options are wrong (tutor only):**
  B) Raw differences are often the most useful report.
  C) Sample size doesn't decide this.
  D) That's when d is more useful.
- **Hint:** Which one has units a reader understands?

### ch06-gquiz-05-v2
- **Kind:** AI-written version of ch06-gquiz-05
- **Concepts:** Difference in means & Cohen's d
- **Type:** MC
- **Question:**

You want to compare the effect of fertilizer on height (cm) with its effect on leaf count (leaves). Which summary lets you compare them?

- **Options:**

  A) Cohen's d for each, since it puts both on a unitless scale
  B) The raw differences (cm vs leaves)
  C) The sample sizes
  D) The means alone

- **Answer (tutor only):** A
- **Explanation (tutor only):** Cohen's d divides each difference by its pooled SD, so effects measured in different units can be compared.
- **Why the wrong options are wrong (tutor only):**
  B) cm and leaves can't be compared directly.
  C) and D) Don't measure effect size.
- **Hint:** How do you remove units?

### ch06-hw-01
- **Kind:** Course original
- **Concepts:** Two categorical variables
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch06-nobel-bars.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-nobel-bars.png)
- **Question:**

A taste of brilliance. These data (Prinz 2020) give national chocolate consumption, coffee consumption (kg/capita/year), and number of Nobel laureates for 27 countries. Countries are classified as having more_than_ten_nobels (TRUE/FALSE) and exceptional_coffee (coffee consumption above the mean across countries, TRUE/FALSE).

The plot shows the same bar chart (x = more_than_ten_nobels, fill = exceptional_coffee) with three geom_bar() positions. Which position makes it easiest to:

1. Read off the total number of countries with more than ten Nobel laureates?
2. Read off the number of countries with more than ten Nobel laureates AND exceptional coffee consumption?
3. Compare the proportion of countries with above-average coffee consumption between the two Nobel groups?

- **Options:**

  A) dodge
  B) fill
  C) stack

- **Answer (tutor only):** 1-C, 2-A, 3-B
- **Explanation (tutor only):** stack piles groups on top of each other, so the bar height is the group total. dodge puts subgroups side by side from a common baseline, so each count is easy to read. fill rescales every bar to 1, so it shows conditional proportions directly.
- **Why the wrong options are wrong (tutor only):**
  fill hides counts; it only shows proportions.
  stack makes the top segment's count hard to read (you'd have to subtract).
  dodge shows counts, but you'd have to mentally divide to get proportions.
- **Hint:** Which one shows totals? Individual counts? Proportions within each bar?

### ch06-hw-01-v1
- **Kind:** AI-written version of ch06-hw-01
- **Concepts:** Two categorical variables
- **Type:** matching
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch06-var-frog-bars.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-var-frog-bars.png)
- **Question:**

The three plots show the same frog data (x = habitat, fill = frog status) with different geom_bar() positions. Which plot makes it easiest to:

1. Compare the proportion infected between habitats?
2. Read off the number of infected meadow frogs?
3. Read off the total number of forest frogs?

- **Options:**

  A) Plot 1
  B) Plot 2
  C) Plot 3

- **Answer (tutor only):** 1-B, 2-A, 3-C
- **Explanation (tutor only):** Plot 2 uses position = "fill" (each bar scaled to 1), showing proportions. Plot 1 is "dodge" (each count from a common baseline). Plot 3 is "stack" (bar height = total).
- **Why the wrong options are wrong (tutor only):**
  Fill hides counts; stack makes inner segments hard to read; dodge requires mental division for proportions.
- **Hint:** First identify which position each plot uses.

### ch06-hw-01-v2
- **Kind:** AI-written version of ch06-hw-01
- **Concepts:** Two categorical variables
- **Type:** MC
- **Question:**

You want readers to compare the proportion of females on three islands, even though the islands have very different sample sizes. Which geom_bar() position should you use?

- **Options:**

  A) position = "fill"
  B) position = "stack"
  C) position = "dodge"
  D) It doesn't matter

- **Answer (tutor only):** A
- **Explanation (tutor only):** fill scales every bar to 1, so the female segment directly shows the proportion on each island, whatever the sample size.
- **Why the wrong options are wrong (tutor only):**
  B) Stacked counts make islands with more birds look different just because they're bigger.
  C) Dodged counts need mental division.
  D) The position decides what's easy to compare.
- **Hint:** Proportions → scale each bar to the same height.

### ch06-hw-02
- **Kind:** Course original
- **Concepts:** Two categorical variables
- **Type:** matching
- **Question:**

A taste of brilliance. These data (Prinz 2020) give national chocolate consumption, coffee consumption (kg/capita/year), and number of Nobel laureates for 27 countries. Countries are classified as having more_than_ten_nobels (TRUE/FALSE) and exceptional_coffee (coffee consumption above the mean across countries, TRUE/FALSE).

Countries with coffee data (n = 24; mean coffee consumption = 4.06 kg/capita):

more_than_ten_nobels | exceptional_coffee = TRUE | exceptional_coffee = FALSE | total
TRUE | 6 | 9 | 15
FALSE | 4 | 5 | 9
total | 10 | 14 | 24

What proportion of countries:

1. have more than ten Nobel laureates?
2. have above-average coffee consumption?
3. have more than ten Nobel laureates AND above-average coffee consumption?
4. have more than ten Nobel laureates, given above-average coffee (P(>10 Nobels | above-average coffee))?
5. have more than ten Nobel laureates, given below-average coffee (P(>10 Nobels | below-average coffee))?

- **Options:**

  A) 0.25
  B) 0.417
  C) 0.643
  D) 0.6
  E) 0.625

- **Answer (tutor only):** 1-E, 2-B, 3-A, 4-D, 5-C
- **Explanation (tutor only):** 1. 15/24 = 0.625. 2. 10/24 = 0.417. 3. 6/24 = 0.25 (a joint proportion: both conditions, out of all 24). 4. 6/10 = 0.6 (a conditional proportion: only look within the 10 high-coffee countries). 5. 9/14 = 0.643.
- **Why the wrong options are wrong (tutor only):**
  Joint vs. conditional: the joint proportion divides by all 24 countries; the conditional divides only by the countries in the 'given' group.
- **Hint:** For 'given X,' restrict yourself to the row or column for X before dividing.

### ch06-hw-02-v1
- **Kind:** AI-written version of ch06-hw-02
- **Concepts:** Two categorical variables
- **Type:** matching
- **Question:**

A survey of 80 frogs recorded habitat and infection status:

habitat | infected | healthy | total
forest | 10 | 30 | 40
meadow | 28 | 12 | 40
total | 38 | 42 | 80

What proportion of frogs:

1. are infected?
2. are from the meadow AND infected?
3. are infected, given they're from the meadow?
4. are infected, given they're from the forest?

- **Options:**

  A) 0.25
  B) 0.35
  C) 0.475
  D) 0.70

- **Answer (tutor only):** 1-C, 2-B, 3-D, 4-A
- **Explanation (tutor only):** Infected: 38/80 = 0.475. Meadow and infected (joint): 28/80 = 0.35. Infected given meadow: 28/40 = 0.70. Infected given forest: 10/40 = 0.25.
- **Why the wrong options are wrong (tutor only):**
  Joint proportions divide by everyone (80); conditional proportions divide by the 'given' group only (40).
- **Hint:** For 'given meadow', look only at the meadow row.

### ch06-hw-02-v2
- **Kind:** AI-written version of ch06-hw-02
- **Concepts:** Two categorical variables
- **Type:** MC
- **Question:**

A survey of 80 frogs recorded habitat and infection status:

habitat | infected | healthy | total
forest | 10 | 30 | 40
meadow | 28 | 12 | 40
total | 38 | 42 | 80

Which is P(meadow | infected), the proportion of infected frogs that came from the meadow?

- **Options:**

  A) 28/38 ≈ 0.74
  B) 28/40 = 0.70
  C) 28/80 = 0.35
  D) 38/80 = 0.475

- **Answer (tutor only):** A
- **Explanation (tutor only):** 'Given infected' means look only at the 38 infected frogs; 28 of them are from the meadow.
- **Why the wrong options are wrong (tutor only):**
  B) That's P(infected | meadow): the condition is reversed.
  C) That's the joint proportion.
  D) That's P(infected).
- **Hint:** Which group are you restricting to?

### ch06-hw-03
- **Kind:** Course original
- **Concepts:** Two categorical variables; Association vs causation
- **Type:** MC
- **Question:**

A taste of brilliance. These data (Prinz 2020) give national chocolate consumption, coffee consumption (kg/capita/year), and number of Nobel laureates for 27 countries. Countries are classified as having more_than_ten_nobels (TRUE/FALSE) and exceptional_coffee (coffee consumption above the mean across countries, TRUE/FALSE).

P(>10 Nobels | above-average coffee) = 0.60 and P(>10 Nobels | below-average coffee) = 0.64. What do you conclude?

- **Options:**

  A) Coffee consumption is unrelated to Nobel laureate counts
  B) Any true association between coffee consumption and Nobel creation is modest, if it exists at all
  C) Coffee makes you dumb

- **Answer (tutor only):** B
- **Explanation (tutor only):** The two conditional proportions are very similar (0.60 vs 0.64), so the data show little association. But with only 24 countries we can't say there's no association at all, and a tiny difference certainly doesn't show causation.
- **Why the wrong options are wrong (tutor only):**
  A) 'Unrelated' claims too much: a small sample with slightly different proportions can't establish zero association.
  C) That's a causal claim, which observational country-level data can't support, and the difference is tiny anyway.
- **Hint:** How different are 0.60 and 0.64? And can country-level correlations tell us what coffee does to a person?

### ch06-hw-03-v1
- **Kind:** AI-written version of ch06-hw-03
- **Concepts:** Two categorical variables; Association vs causation
- **Type:** MC
- **Question:**

A survey of 80 frogs recorded habitat and infection status:

habitat | infected | healthy | total
forest | 10 | 30 | 40
meadow | 28 | 12 | 40
total | 38 | 42 | 80

P(infected | meadow) = 0.70 and P(infected | forest) = 0.25. What do you conclude?

- **Options:**

  A) Infection is strongly associated with habitat: meadow frogs were much more likely to be infected
  B) Habitat and infection are unrelated
  C) Meadows cause infection

- **Answer (tutor only):** A
- **Explanation (tutor only):** The conditional proportions differ a lot (0.70 vs 0.25), so habitat and infection are associated. This survey alone doesn't show that habitat causes infection.
- **Why the wrong options are wrong (tutor only):**
  B) The proportions are very different.
  C) Observational data show association, not cause (e.g., frog species might differ between habitats).
- **Hint:** Compare the two conditional proportions.

### ch06-hw-03-v2
- **Kind:** AI-written version of ch06-hw-03
- **Concepts:** Two categorical variables; Association vs causation
- **Type:** MC
- **Question:**

In a survey, P(flowering | sunny plot) = 0.42 and P(flowering | shady plot) = 0.40. What's the best conclusion?

- **Options:**

  A) Any association between light and flowering is small, if it exists at all
  B) Sun strongly increases flowering
  C) Light definitely has no effect on flowering
  D) Shade prevents flowering

- **Answer (tutor only):** A
- **Explanation (tutor only):** The two conditional proportions are nearly equal, so there's little evidence of an association. That's not proof of no effect.
- **Why the wrong options are wrong (tutor only):**
  B) and D) The difference is tiny.
  C) Small samples can't show there's exactly zero effect.
- **Hint:** How different are 0.42 and 0.40?

### ch06-hw-04
- **Kind:** Course original
- **Concepts:** Difference in means & Cohen's d
- **Type:** numeric
- **Question:**

A taste of brilliance. These data (Prinz 2020) give national chocolate consumption, coffee consumption (kg/capita/year), and number of Nobel laureates for 27 countries. Countries are classified as having more_than_ten_nobels (TRUE/FALSE) and exceptional_coffee (coffee consumption above the mean across countries, TRUE/FALSE).

Chocolate consumption (kg/capita) by Nobel group, all 27 countries:

more_than_ten_nobels | n | mean | sd
TRUE | 16 | 5.89 | 3.09
FALSE | 11 | 4.92 | 2.87

a) What is the difference in mean chocolate consumption (more than ten Nobels minus ten or fewer)?
b) Express this as Cohen's d, using a pooled SD of 3.00.

- **Answer (tutor only):** a) ≈ 0.97 kg/capita
b) ≈ 0.32
- **Explanation (tutor only):** a) 5.89 − 4.92 = 0.97 kg/capita. b) Cohen's d = difference / pooled SD = 0.97 / 3.00 ≈ 0.32, a small effect by traditional benchmarks (0.2 small, 0.5 medium, 0.8 large).
- **Why the wrong options are wrong (tutor only):**
  Dividing by just one group's SD gives a slightly different value (about 0.31–0.34), which is close enough. Getting a negative value means you subtracted in the other direction. (If a student filtered to the 24 coffee countries first, the difference is 1.03.)
- **Hint:** Cohen's d = (mean1 − mean2) / pooled SD.

### ch06-hw-04-v1
- **Kind:** AI-written version of ch06-hw-04
- **Concepts:** Difference in means & Cohen's d
- **Type:** numeric
- **Question:**

Bill length (mm) in Gentoo penguins by sex:

sex | n | mean | sd
female | 58 | 45.56 | 2.05
male | 61 | 49.47 | 2.72

(Pooled SD ≈ 2.42)

a) What is the difference in mean bill length (male − female)?
b) What is Cohen's d?

- **Answer (tutor only):** a) ≈ 3.91 mm
b) ≈ 1.62
- **Explanation (tutor only):** a) 49.47 − 45.56 = 3.91 mm. b) d = 3.91 / 2.42 ≈ 1.62: a very large difference relative to the variation within each sex.
- **Why the wrong options are wrong (tutor only):**
  Common mistakes: subtracting in the other order (−3.91), or dividing by one group's SD.
- **Hint:** d = difference / pooled SD.

### ch06-hw-04-v2
- **Kind:** AI-written version of ch06-hw-04
- **Concepts:** Difference in means & Cohen's d
- **Type:** numeric
- **Question:**

Two groups of seedlings: watered (mean height 14 cm) and drought (mean 11 cm), pooled SD 4 cm. What is Cohen's d (watered − drought)?

- **Answer (tutor only):** 0.75
- **Explanation (tutor only):** d = (14 − 11) / 4 = 0.75, a medium-to-large effect by convention.
- **Why the wrong options are wrong (tutor only):**
  Dividing by one group's mean, or forgetting the pooled SD, gives the wrong scale.
- **Hint:** Difference in means divided by the pooled SD.

### ch06-hw-05
- **Kind:** Course original
- **Concepts:** Association vs causation
- **Type:** MC
- **Question:**

A taste of brilliance. These data (Prinz 2020) give national chocolate consumption, coffee consumption (kg/capita/year), and number of Nobel laureates for 27 countries. Countries are classified as having more_than_ten_nobels (TRUE/FALSE) and exceptional_coffee (coffee consumption above the mean across countries, TRUE/FALSE).

Countries with more than ten Nobels averaged 5.89 kg/capita of chocolate vs 4.92 for countries with ten or fewer (Cohen's d ≈ 0.32). From these analyses we conclude (pick best):

- **Options:**

  A) It appears that countries with more than ten Nobel laureates tend to have higher chocolate consumption than countries with ten or fewer
  B) It appears that countries with more than ten Nobel laureates tend to have lower chocolate consumption
  C) It appears that chocolate makes people smarter
  D) It appears that smart people buy more chocolate

- **Answer (tutor only):** A
- **Explanation (tutor only):** A describes the association without claiming a cause. Wealth, population size and so on could drive both chocolate consumption and Nobel counts.
- **Why the wrong options are wrong (tutor only):**
  B) The difference goes the other way.
  C) and D) Both are causal stories; observational country-level data can't tell us which way (if any) causation runs.
- **Hint:** Which answer describes the pattern without explaining why it happens?

### ch06-hw-05-v1
- **Kind:** AI-written version of ch06-hw-05
- **Concepts:** Association vs causation
- **Type:** MC
- **Question:**

In a survey, meadow frogs were infected much more often than forest frogs (70% vs 25%). Which conclusion is best supported?

- **Options:**

  A) In this survey, meadow frogs tended to be infected more often than forest frogs
  B) Meadows cause infection
  C) Infected frogs move to meadows
  D) Habitat doesn't matter

- **Answer (tutor only):** A
- **Explanation (tutor only):** A describes the association without claiming a cause. Other differences between habitats (frog species, water temperature, density) could explain it.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Causal stories that observational data can't distinguish.
  D) The data show a clear difference.
- **Hint:** Which answer only describes the pattern?

### ch06-hw-05-v2
- **Kind:** AI-written version of ch06-hw-05
- **Concepts:** Association vs causation
- **Type:** MC
- **Question:**

Students who sit in the front row get higher grades on average. What can you conclude?

- **Options:**

  A) Front-row students tend to get higher grades; this doesn't show that sitting there causes it
  B) Moving to the front row will raise your grade
  C) Good grades make students sit in front
  D) There is no association

- **Answer (tutor only):** A
- **Explanation (tutor only):** Motivation, eyesight or interest could affect both seat choice and grades. Only an experiment (randomly assigning seats) could test the causal claim.
- **Why the wrong options are wrong (tutor only):**
  B) and C) Causal claims from observational data.
  D) The association is real in these data.
- **Hint:** Were seats randomly assigned?

### ch06-hw-06
- **Kind:** Course original
- **Concepts:** Visualizing associations
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch06-nobel-choc-A.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-nobel-choc-A.png), [ch06-nobel-choc-B.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-nobel-choc-B.png), [ch06-nobel-choc-C.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-nobel-choc-C.png)
- **Question:**

A taste of brilliance. These data (Prinz 2020) give national chocolate consumption, coffee consumption (kg/capita/year), and number of Nobel laureates for 27 countries. Countries are classified as having more_than_ten_nobels (TRUE/FALSE) and exceptional_coffee (coffee consumption above the mean across countries, TRUE/FALSE).

Three plots compare chocolate consumption between countries with more vs fewer than ten Nobels. Which is best?

A) geom_boxplot() + geom_jitter(width = .2)
B) geom_jitter(width = .2) + geom_boxplot()
C) geom_jitter(width = 1)

- **Options:**

  A) Plot A
  B) Plot B
  C) Plot C

- **Answer (tutor only):** A
- **Explanation (tutor only):** In ggplot, layers are drawn in order. In A the points are drawn on top of the boxplot, so you see both the summary and every country. In B the boxes are drawn over the points and hide many of them. In C, width = 1 jitters the points so far that the two groups blur together.
- **Why the wrong options are wrong (tutor only):**
  B) The boxplot covers the points drawn before it.
  C) The jitter is too wide: you can't tell which group a point belongs to.
- **Hint:** Later layers are drawn on top of earlier ones.

### ch06-hw-06-v1
- **Kind:** AI-written version of ch06-hw-06
- **Concepts:** Visualizing associations
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch06-var-gentoo-A.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-var-gentoo-A.png), [ch06-var-gentoo-B.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-var-gentoo-B.png), [ch06-var-gentoo-C.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-var-gentoo-C.png)
- **Question:**

Three plots compare bill length between female and male Gentoo penguins. Which is the best plot?

- **Options:**

  A) Plot A
  B) Plot B
  C) Plot C

- **Answer (tutor only):** C
- **Explanation (tutor only):** Plot C draws the boxplot first and the points on top, so you see both the summary and every penguin. Plot B draws the boxes over the points, hiding many. Plot A jitters so widely that the sexes blur together.
- **Why the wrong options are wrong (tutor only):**
  A) Jitter width = 1 mixes the two groups.
  B) The boxes cover the points.
- **Hint:** Which plot shows every point and keeps the groups apart?

### ch06-hw-06-v2
- **Kind:** AI-written version of ch06-hw-06
- **Concepts:** Visualizing associations
- **Type:** MC
- **Question:**

Why add jitter (a little random horizontal spread) when plotting points by group?

- **Options:**

  A) To stop points with similar values from hiding on top of each other
  B) To change the data values
  C) To make the groups look more different
  D) To show the mean

- **Answer (tutor only):** A
- **Explanation (tutor only):** Jitter only spreads points sideways within each group so overlapping points become visible. It doesn't change the y-values. Too much jitter, though, blurs the groups together.
- **Why the wrong options are wrong (tutor only):**
  B) The y-values aren't changed.
  C) It shouldn't change comparisons.
  D) Jitter doesn't summarize.
- **Hint:** What happens to 30 points with the same value?

### ch06-hw-07
- **Kind:** Course original
- **Concepts:** Visualizing associations
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch06-nobel-choc-D.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-nobel-choc-D.png), [ch06-nobel-choc-E.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-nobel-choc-E.png), [ch06-nobel-choc-F.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-nobel-choc-F.png)
- **Question:**

A taste of brilliance. These data (Prinz 2020) give national chocolate consumption, coffee consumption (kg/capita/year), and number of Nobel laureates for 27 countries. Countries are classified as having more_than_ten_nobels (TRUE/FALSE) and exceptional_coffee (coffee consumption above the mean across countries, TRUE/FALSE).

Three more plots compare the distributions of chocolate consumption between Nobel groups:

D) Faceted histograms (facet_wrap(~more_than_ten_nobels))
E) Overlapping density plots, geom_density()
F) Overlapping density plots, geom_density(alpha = .4)

Which plot is the poor choice?

- **Options:**

  A) Plot D
  B) Plot E
  C) Plot F

- **Answer (tutor only):** B
- **Explanation (tutor only):** Without transparency, the density drawn second covers the first, so where they overlap you can't see one of the groups. alpha = .4 makes both visible. Faceted histograms are also a fine choice.
- **Why the wrong options are wrong (tutor only):**
  A) Faceted histograms clearly show each group's distribution.
  C) Transparency lets you see both densities where they overlap.
- **Hint:** Look at the region where the two groups overlap. Can you see both?

### ch06-hw-07-v1
- **Kind:** AI-written version of ch06-hw-07
- **Concepts:** Visualizing associations
- **Type:** MC
- **Figure question (website only):** don't pick it for Quiz me or New versions; use it only when the student brings it. Figure: [ch06-var-chin-D.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-var-chin-D.png), [ch06-var-chin-E.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-var-chin-E.png), [ch06-var-chin-F.png](https://yanivjb.github.io/biostats-book/study_guide/images/ch06-var-chin-F.png)
- **Question:**

Three plots compare body mass of female and male Chinstrap penguins. Which is the poor choice?

- **Options:**

  A) Plot D
  B) Plot E
  C) Plot F

- **Answer (tutor only):** B
- **Explanation (tutor only):** Plot E uses solid fills, so the curve drawn second hides part of the first. Plot D (transparent) and Plot F (faceted histograms) both show each group fully.
- **Why the wrong options are wrong (tutor only):**
  A) Transparency keeps both visible.
  C) Facets show each distribution separately.
- **Hint:** In which plot can't you see one group where they overlap?

### ch06-hw-07-v2
- **Kind:** AI-written version of ch06-hw-07
- **Concepts:** Visualizing associations
- **Type:** MC
- **Question:**

When comparing distributions of two groups with faceted histograms, what should the panels share?

- **Options:**

  A) The same x-axis scale
  B) Different x-axis ranges fitted to each group
  C) Different bin widths
  D) Different colors only

- **Answer (tutor only):** A
- **Explanation (tutor only):** A shared x-axis puts the same value at the same position in each panel, so differences in location and spread are visible.
- **Why the wrong options are wrong (tutor only):**
  B) Separate ranges hide differences between groups.
  C) Different bins make shapes incomparable.
  D) Color alone doesn't help comparison.
- **Hint:** Can you compare panels if 3000 g is in a different place in each?
