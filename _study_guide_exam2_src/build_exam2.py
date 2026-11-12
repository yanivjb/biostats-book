"""Build the Exam 2 study guide data (data.js + images) by reusing the Exam 1 build_data.py with Exam 2 settings.
    python3 build_exam2.py OUTPUT_DIR
"""
import csv, re, sys
import build_data as B
from app_config_ch00 import CHAPTER_0, CONCEPTS_0

B.CHAPTERS = {0: CHAPTER_0, 13: 'Linear Models', 14: 'Normal distribution', 15: 'The t distribution',
              16: 'Comparing two means', 17: 'F this!', 18: '>2 Groups', 19: 'Regression',
              20: 'Multiple Predictors', 21: 'Interactions'}
B.CONCEPTS = {
    0: CONCEPTS_0,
    13: {'Statistical vs scientific models': ['scientific vs statistical models'],
         'Categorical predictors & reference levels': ['categorical predictors', 'reference level', 'means'],
         'Coefficients & predictions': ['linear model coefficients', 'predictions', 'intercept', 'coefficients', 'slope', 'slopes',
                                        'interpreting linear models', 'linear model formulas', 'multiple predictors', 'covariates',
                                        'extrapolation', 'writing results'],
         'Residuals & model fit': ['residuals', 'residual standard deviation', 'sums of squares', 'degrees of freedom', 'model fit'],
         'Regression from summaries': ['covariance', 'correlation', 'regression', 'regression slope', 'regression intercept']},
    14: {'The normal & Z': ['Z-transform', 'standard normal', '68-95 rule', 'normal probabilities'],
         "Density & R's _norm functions": ['_norm functions', 'probability density'],
         'Sampling distribution & CLT': ['central limit theorem', 'sampling distribution', 'standard error', 'law of large numbers'],
         'Z tests & p-values': ['p-values', 'Z test', 'NHST', 'interpreting p-values'],
         'Normality & transformations': ['transformations', 'assessing normality']},
    15: {'t vs z': ['t vs z', 'critical t', 'critical values', 'central limit theorem', 't-test assumptions', 'assessing normality', 'QQ plots'],
         'The t statistic & SE': ['t statistic', 'standard error', 'standard deviation', 'variance', 'sample size', 'test statistics',
                                  'one-sample t-test', 'R'],
         'p-values & NHST': ['p-values', 'NHST', 'null and alternative hypotheses', 'sampling error', 'interpreting results', 'writing results'],
         'Effect size & CIs': ['effect size', "Cohen's d", 'confidence intervals'],
         'Paired designs': ['paired t-test', 'study design']},
    16: {'Effect size vs significance': ['effect size', "Cohen's d", 't statistic', 'sample size', 'standard error', 'critical values'],
         'Two-sample t & equal variance': ['equal variance assumption', 'pooled variance', 'two-sample t-test', "Welch's t-test",
                                           'assessing normality', 'visualizing two groups'],
         'Confidence intervals': ['confidence intervals', 'interpreting CIs'],
         'Interpreting tests': ['NHST', 'p-values', 'interpreting results', 'interpreting non-significant results', 'null and alternative hypotheses'],
         'p-hacking & HARKing': ['p-hacking', 'HARKing', 'study design']},
    17: {'Sums of squares & deviations': ['sums of squares', 'deviations', 'group means', 'linear models'],
         'F & the ANOVA table': ['F statistic', 'F', 'mean squares', 'ANOVA table', 'F distribution', 'one vs two tails', 'critical values', 't-test vs ANOVA'],
         'Hypotheses & p-values': ['p-values', 'null hypothesis', 'NHST', 'ANOVA hypotheses', 'interpreting results'],
         'Effect size & R²': ['effect size', "Cohen's d", 'R squared', 'pooled variance'],
         'SD vs SE': ['standard error', 'standard deviation', 'uncertainty vs variability']},
    18: {'Multiple testing & post-hoc tests': ['multiple testing', 'post-hoc tests', 'pairwise comparisons', 'significance groups'],
         'ANOVA calculations': ['sums of squares', 'deviations', 'ANOVA table', 'degrees of freedom', 'mean squares', 'ANOVA calculations',
                                'R squared', 'generalizing', 'ANOVA'],
         'Assumptions & diagnostics': ['equal variance assumption', 'ANOVA assumptions', 'QQ plots', 'normality assumption'],
         'ANOVA in R': ['R', 'summary() output', 'intercept', 'R errors', 'R output', 'ANOVA workflow', 'writing results', 'NHST'],
         'SD vs SE': ['sampling distribution', 'standard error', 'standard deviation', 'visualizing groups']},
    19: {'Slopes, intercepts & predictions': ['regression', 'slope', 'regression slope', 'intercept', 'predictions', 'extrapolation',
                                              'linear model equation', 'covariance', 'correlation', 'regression concepts', 'interpretation', 'residuals'],
         'Confidence & prediction intervals': ['confidence intervals', 'confidence vs prediction intervals'],
         'Sums of squares, F & R²': ['sums of squares', 'deviations', 'degrees of freedom', 'F statistic', 'R squared', 'test statistics',
                                     'NHST', 'p-values', 'null hypothesis', 'interpreting results'],
         'Assumptions & diagnostics': ['regression assumptions', 'diagnostics', 'influence', 'outliers', 'leverage', 'robustness'],
         'Measurement error & causation': ['measurement error', 'causation', 'study design']},
    20: {'Coefficients & predictions': ['predictions', 'multiple predictors', 'categorical predictors', 'intercept', 'coefficients',
                                        'interpreting coefficients', 'units', 'explanatory variables', 'response', 'covariates',
                                        'why multiple regression', 'model building'],
         'Adjusting vs controlling': ['adjusting', 'adjusting vs controlling', 'adjusting for variables', 'confounding', 'causation', 'observational studies'],
         'Type I vs Type II sums of squares': ['Type II sums of squares', 'Type I vs Type II sums of squares', 'NHST', 'summary() output',
                                               'coefficient p-values', 'R'],
         'Partial R² & multicollinearity': ['effect sizes', 'partial R squared', 'multicollinearity', 'VIF'],
         'Plots & diagnostics': ['diagnostics', 'plots should match models', 'regression assumptions', 'transformations'],
         'Adjusted means': ['post-hoc tests', 'adjusted means']},
    21: {'What interactions mean': ['interactions', 'interaction models', 'when to include interactions', 'additive models', 'linear models'],
         'Predictions & coefficients': ['predictions', 'interpreting coefficients', 'intercept', 'centering', 'extrapolation', 'summary() output'],
         'Main effects with interactions': ['main effects', 'main effects with interactions', 'interpreting interactions', 'emmeans',
                                            'emmeans vs summary()', 'contrasts'],
         'Visualizing interactions': ['visualizing', 'plotting', 'visualizing interactions', 'plots should match models'],
         'Testing interactions': ['Type II vs Type III sums of squares', 'Type II sums of squares', 'Type I vs Type II sums of squares',
                                  'diagnostics', 'assumptions']},
}

# Numeric answers: accept within 2% of the answer, or within one unit of its last shown decimal, whichever is wider.
def numeric_spec(ans):
    s = ans.replace('≈', '').replace('−', '-').strip()
    x = float(s)
    dec = len(s.split('.')[1]) if '.' in s else 0
    tol = max(abs(x) * 0.02, 10 ** -dec)
    return [('', round(x - tol, 6), round(x + tol, 6), ans)]
B.NUMERIC = {r['id']: numeric_spec(r['answer']) for r in csv.DictReader(open('question_bank.csv', encoding='utf-8'))
             if r['type'] == 'numeric' and r['include'] == 'yes'}

B.OPEN_CONCEPTS = {
    'O-13-01': ['Categorical predictors & reference levels'], 'O-13-02': ['Coefficients & predictions'],
    'O-14-01': ['Normality & transformations'],
    'O-15-01': ['p-values & NHST', 'Effect size & CIs'], 'O-15-02': ['t vs z', 'The t statistic & SE'],
    'O-16-01': ['Two-sample t & equal variance'], 'O-16-02': ['p-hacking & HARKing'],
    'O-18-01': ['Multiple testing & post-hoc tests'], 'O-18-02': ['Multiple testing & post-hoc tests', 'ANOVA in R'],
    'O-19-01': ['Assumptions & diagnostics'], 'O-19-02': ['Measurement error & causation'],
    'O-20-01': ['Partial R² & multicollinearity'], 'O-20-02': ['Adjusting vs controlling', 'Coefficients & predictions'],
    'O-20-03': ['Partial R² & multicollinearity', 'Coefficients & predictions'],
}
B.OPEN_CHAPTER_OVERRIDE = {}
B.STUDENT_PROMPT = {
    'O-13-02': ("To ask whether fishing makes fish populations more variable, a model of 28 fish species gives: "
                "lm(cv ~ exploited + age), with (Intercept) = 1.25, exploitedyes = 0.45, age = -0.04, and residual SD = 0.313 (25 df). "
                "Here cv is the year-to-year coefficient of variation in larval abundance, and age is age at maturation (years). "
                "The plot below shows the data. Summarize these results in a short paragraph for a biologist.", ['ch13-quiz-fish.png']),
    'O-19-01': ("Male collared lizards use their jaws as weapons in territorial fights, so researchers asked whether bite force predicts "
                "territory size in 11 males (bite forces 4.3 to 5.4 N). Looking at the diagnostic plots below for lm(territory ~ bite), "
                "which assumptions of the linear model (if any) concern you? Point to features of the study design and/or the plots. "
                "What, if anything, can you do about it?", ['ch19-quiz-lizard-diag.png']),
}

if __name__ == '__main__':
    B.OUT = sys.argv[1] if len(sys.argv) > 1 else 'study_guide'
    import runpy
    g = vars(B)
    exec(compile(open('build_data.py').read().split("if __name__ == '__main__':")[1].replace('\n    ', '\n'), 'main', 'exec'), g)
