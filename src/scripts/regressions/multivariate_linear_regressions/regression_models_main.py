import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
from statsmodels.compat import lzip
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.outliers_influence import variance_inflation_factor
from scipy.stats import spearmanr
from scipy.stats import pearsonr
from patsy import dmatrices
from scripts.data.get_data_path import open_data_file

# 1. -- Check if the file is of valid type, after that Pandas loads the data -- (you can add more file suffixes with an additional if statement and with filepaths = ['.xlsx', 'xlsm',])
# 2. -- Calculate some basic sample statistics --
# 3. -- Fit a linear regression assuming Gaussian Distribution --
# -- Test for bootstrapping --
# 4. -- Test for heteroscedasticity (Breusch-Pagan) --
# 5. -- Test for multicollinearity --
# find design matrix for regression model using '' as response variable
# Create an empty DataFrame for VIF results
# Calculate the VIF for each variable and store in the vif_df DataFrame
# Print VIF assessment
# 6. -- Test for autocorrelation of residuals (Durbin-Watson) --
# 7. -- Calculate & Print the Spearman Rank correlation and corresponding p-value --

def regression_models_main():
    df = open_data_file().dropna()

    print(df.info())
    df.head()

    # mean = np.mean(df)
    # variance = np.var(df, ddof=1)
    # std_dev = np.std(df, ddof=1)
    # cv = std_dev / mean
    #
    # print('Sample Mean: ', mean)
    # print('Sample Variance: ', variance)
    # print('Standard Deviation of the sample: ', std_dev)
    # print('CV: ', cv)

    y = df[['D1']]
    x = df[['D1', 'D2', 'D3', 'D4', 'BSMAS', 'Age_Group', 'Gender']].dropna()

    model = smf.ols('D1 ~ D2 + D3 + D4 + BSMAS',df).fit()
    model2 =  smf.ols('D2 ~ D1 + D3 + D4 + BSMAS',df).fit()
    model3 = smf.ols('D3 ~ D1 + D2 + D4 + BSMAS',df).fit()
    model4 = smf.ols('D4 ~ D1 + D2 + D3 + BSMAS',df).fit()

    print(model.summary())
    print(model2.summary())
    print(model3.summary())
    print(model4.summary())

    names = ['Lagrange multiplier statistic', 'p-value', 'f-value', 'f p-value']

    bp_test = sms.het_breuschpagan(model.resid, model.model.exog)
    bp_test2 = sms.het_breuschpagan(model2.resid, model2.model.exog)
    bp_test3 = sms.het_breuschpagan(model3.resid, model3.model.exog)
    bp_test4 = sms.het_breuschpagan(model4.resid, model4.model.exog)

    print("Result of Breusch-Pagan Test (Heteroscedasticity): ", lzip(names, bp_test))
    print("Result of Breusch-Pagan Test (Heteroscedasticity): ", lzip(names, bp_test2))
    print("Result of Breusch-Pagan Test (Heteroscedasticity): ", lzip(names, bp_test3))
    print("Result of Breusch-Pagan Test (Heteroscedasticity): ", lzip(names, bp_test4))
    # extract coefficient distributions

    # w_sm_mu = model.params
    # w_sm_std = np.sqrt(np.diag(model.normalized_cov_params))
    #
    # print(w_sm_mu)
    # print(w_sm_std)
    #
    # w_bs = []
    # n = x.shape[0]
    # for i in range(10000):
    #     samp = np.random.randint(n, size=n)
    #     results_bs = sm.OLS(y.loc[samp], x.loc[samp, :]).fit()
    #     w_bs.append(results_bs.params)
    #
    # w_bs = np.array(w_bs)

    # # summarize coefficient distributions
    # w_bs_mu = np.mean(w_bs, axis=0)
    # w_bs_std = np.std(w_bs, axis=0)
    #
    # coefficients = pd.concat([w_sm_mu,
    #                           pd.DataFrame(data=w_bs_mu, index=x.columns),
    #                           pd.DataFrame(data=w_sm_std, index=x.columns),
    #                           pd.DataFrame(data=w_bs_std, index=x.columns)], axis=1)
    #
    # coefficients.columns = ['statsmodels_mu', 'bootstrapped_mu', 'statsmodels_std', 'bootstrapped_std']
    #
    # print(coefficients.to_string())
    #
    # fig, ax = plt.subplots(ncols=2, figsize=(10, 6))
    # ax[0].plot(range(x.shape[1]), w_sm_mu, label='statsmodels')
    # ax[0].plot(range(x.shape[1]), w_bs_mu, 'x', label='boostrapped')
    # ax[0].set_ylabel('Mean')
    # ax[1].plot(range(x.shape[1]), w_sm_std, label='statsmodels')
    # ax[1].plot(range(x.shape[1]), w_bs_std, 'x', label='boostrapped')
    # ax[1].set_ylabel('Standard deviation')
    # plt.legend()
    # plt.tight_layout()
    # plt.savefig('bootst_vs_theo100000.png')
    #
    # n_boot = 1000
    # coef_samples = []
    #
    # for _ in range(n_boot):
    #     X_resampled, y_resampled = resample(x, y)  # resample rows
    #     model = sm.OLS(y_resampled, X_resampled).fit()
    #     print(model.summary)
    #     np.append(coef_samples, model.params)  # https://careerkarma.com/blog/python-attributeerror-numpy-append/
    #
    #     coef_samples = pd.Series(coef_samples)
    #     ci_lower = coef_samples.quantile(q=0.025)
    #     ci_upper = coef_samples.quantile(q=0.975)
    #     print(ci_lower, ci_upper)

    Y, X = dmatrices(
        'Q1 ~ Q2 + D1 + D2 + D3 + D4 + BSMAS + Gender + Education_L +Education_P + Education_Highest + Attach_S + Attach_S_N + Age_Group +Time_Spent_M + Time_Spent_H +Empl_st_sfemp +Empl_st_employee +Empl_st_st +Empl_st_oth + Instagram_index + Facebook_index + TikTok_index + H_Problem',
        data=df, return_type='dataframe')

    vif_df = pd.DataFrame()
    vif_df['Variable'] = X.columns
    vif_df['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

    for index, row in vif_df.iterrows():
        if row['VIF'] == 1:
            print("There is no collinearity for", row['Variable'])
            print(row['VIF'])
        elif 1 < row['VIF'] < 5:
            print("There is moderate correlation between predictor variable", row['Variable'],
                  "and other predictor variables in the model.")
            print(row['VIF'])
        else:
            print("There is severe correlation between predictor variable", row['Variable'],
                  "and other predictor variables in the model.")
            print(row['VIF'])

    print('Autocorrelation of residuals: ', durbin_watson(model.resid))

    independent_vars = df.columns[df.columns != 'BSMAS']
    pearson_corrs = {}

    for var in independent_vars:

        print(df['BSMAS'].info)

        # -- Courtesy of Gemini --
        df['BSMAS'] = pd.to_numeric(df['BSMAS'], errors='coerce')
        df[var] = pd.to_numeric(df[var], errors='coerce')
        #   --                --

        corr, p = pearsonr(df['BSMAS'], df[var])
        pearson_corrs[var] = (corr, p)

    for var, (corr, p) in pearson_corrs.items():
        print(f"Pearson correlation between predictor and {var}: {corr}, p-value: {p}")

    for var in independent_vars:
        corr, p = pearsonr(df['D1'].dropna(), df[var])
        pearson_corrs[var] = (corr, p)

    for var, (corr, p) in pearson_corrs.items():
        print(f"Pearson correlation between predictor and {var}: {corr}, p-value: {p}")

    for var in independent_vars:
        corr, p = pearsonr(df['D2'].dropna(), df[var])
        pearson_corrs[var] = (corr, p)

    for var, (corr, p) in pearson_corrs.items():
        print(f"Pearson correlation between predictor and {var}: {corr}, p-value: {p}")

    for var in independent_vars:
        corr, p = pearsonr(df['D3'].dropna(), df[var])
        pearson_corrs[var] = (corr, p)

    for var, (corr, p) in pearson_corrs.items():
        print(f"Pearson correlation between predictor and {var}: {corr}, p-value: {p}")

    for var in independent_vars:
        corr, p = pearsonr(df['D4'].dropna(), df[var])
        pearson_corrs[var] = (corr, p)

    for var, (corr, p) in pearson_corrs.items():
        print(f"Pearson correlation between predictor and {var}: {corr}, p-value: {p}")

    independent_vars = df.columns[df.columns != 'BSMAS']
    dependent_vars = ['D1', 'D2', 'D3', 'D4', 'BSMAS']

    for dep in dependent_vars:
        y = df[dep]
        spearman_corrs = {}

        for var in independent_vars:
            corr, p = spearmanr(y, df[var])
            spearman_corrs[var] = (corr, p)

        print(f"\nSpearman correlations with {dep}:")
        for var, (corr, p) in spearman_corrs.items():
            print(f"  - {var}: correlation = {corr}, p-value = {p}")
    # print("Analysis Finished, please see the generated files & data")

    x1 = df[['D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Age_Group','Education_L','Education_P','Education_Highest',
              'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
              'Instagram_index', 'Facebook_index', 'TikTok_index', 'YouTube_Index']].dropna()

    for al in x1.columns:

        corr, p = spearmanr(x1['BSMAS'], x1[al])
        print(f"\nSpearman correlations {al} : {corr} p-value: {p}")

    # corr, p = spearmanr(x['BSMAS'], x['Gender'])
    # print(f"\nSpearman correlations : {corr} p-value: {p}")

    modelbsmas = smf.ols('BSMAS ~ Empl_st_st + TikTok_index + Age_Group + Time_Spent_M + Time_Spent_H + Empl_st_sfemp + Facebook_index',df).fit()

    print(modelbsmas.summary())

    x1['Age_Group'].info()

    print(np.mean(x1['Age_Group']))
    print(np.std(x1['Age_Group']))

regression_models_main()