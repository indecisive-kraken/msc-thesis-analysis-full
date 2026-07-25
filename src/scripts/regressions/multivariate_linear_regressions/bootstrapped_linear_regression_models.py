import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.compat import lzip
from scipy.stats import shapiro
from statsmodels.formula.api import ols
from statsmodels.stats.stattools import omni_normtest
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.outliers_influence import variance_inflation_factor
from resample.bootstrap import bootstrap
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from scipy import stats
from scipy.stats import spearmanr
from patsy import dmatrices

#1
data = input('Please specify the Excel file with the data: ')
df = pd.read_excel(data, sheet_name='Sheet15')

print(df.info())
df.head()

#2
mean = np.mean(df)
variance = np.var(df, ddof=1)
std_dev = np.std(df, ddof=1)
cv = std_dev / mean

print('Sample Mean: ', mean)
print('Sample Variance: ', variance)
print('Standard Deviation of the sample: ', std_dev)
print('CV: ', cv)

#3
# y = df['Q1']
# x = df[['Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Age_Group',
#         'Time_Spent_M', 'Time_Spent_H',
#         'Instagram_index', 'Facebook_index', 'TikTok_index']]
#
# model = smf.ols(
#     'Q1 ~ Q2 + D1 + D2 + D3 + D4 + BSMAS + Gender + Age_Group +Time_Spent_M + Time_Spent_H + Instagram_index + Facebook_index + TikTok_index',
#     df).fit()

y = df[['D1']]
x = df[['D1', 'D2', 'D3', 'D4', 'BSMAS']]

model = smf.ols('D1 ~ D2 + D3 + D4 + BSMAS',df).fit()
model2 =  smf.ols('D2 ~ D1 + D3 + D4 + BSMAS',df).fit()
model3 = smf.ols('D3 ~ D1 + D2 + D4 + BSMAS',df).fit()
model4 = smf.ols('D4 ~ D1 + D2 + D3 + BSMAS',df).fit()

# model = sm.OLS(y, x).fit()

print(model.summary())
print(model2.summary())
print(model3.summary())
print(model4.summary())

# -- Bootstrapped Version --

def fitreg(A):
    scale = StandardScaler()
    reg = LinearRegression(fit_intercept=True)
    X_scale = scale.fit_transform(A[:, :A.shape[1]-2])
    y = A[:, A.shape[1]-1]
    reg.fit(X_scale, y)
    return {"coef": reg.coef_, "intercept": reg.intercept_}

boot_coef = bootstrap(a=df.join(y).values, f=fitreg, b=5000)


# # Number of bootstrap samples
# n_bootstraps = 1000
#
# # Store bootstrapped coefficients
# boot_coefs = []
#
# # Bootstrapping loop
# for _ in range(n_bootstraps):
#     sample_indices = np.random.choice(len(df), size=len(df), replace=True)
#     X_sample = x.iloc[sample_indices]
#     y_sample = y.iloc[sample_indices]
#
#     model = smf.ols(y_sample, X_sample).fit()
#     boot_coefs.append(model.params.values)
#
# # Convert to DataFrame
# coef_df = pd.DataFrame(boot_coefs, columns=x.columns)
#
# # Get means and 95% CI
# summary = coef_df.describe(percentiles=[0.025, 0.975]).loc[["mean", "2.5%", "97.5%"]]
# print("\nBootstrapped Regression Coefficients (95% CI):")
# print(summary)

#4
names = ['Lagrange multiplier statistic', 'p-value', 'f-value', 'f p-value']
bp_test = sms.het_breuschpagan(model.resid, model.model.exog)
print("Result of Breusch-Pagan Test (Heteroscedasticity): ", lzip(names, bp_test))

#5
Y, X = dmatrices(
    'Q1 ~ Q2 + D1 + D2 + D3 + D4 + BSMAS', data=df, return_type='dataframe')

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

#6
print('Autocorrelation of residuals: ', durbin_watson(model.resid))

#7
independent_vars = df.columns[df.columns != 'D1']

spearman_corrs = {}
for var in independent_vars:
    corr, p = spearmanr(df['BSMAS'], df[var])
    spearman_corrs[var] = (corr, p)

for var, (corr, p) in spearman_corrs.items():
    print(f"Spearman correlation between predictor and {var}: {corr}, p-value: {p}")


print("Analysis Finished, please see the generated files & data")
