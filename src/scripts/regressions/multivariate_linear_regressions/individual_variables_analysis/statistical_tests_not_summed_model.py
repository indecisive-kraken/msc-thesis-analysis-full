import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
from statsmodels.compat import lzip
from scipy.stats import shapiro
from statsmodels.formula.api import ols
from statsmodels.stats.stattools import omni_normtest
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.outliers_influence import variance_inflation_factor
from scipy import stats
from scipy.stats import spearmanr
from patsy import dmatrices

#    -- Table of Contents --
# 1. -- Check if the file is of valid type, after that Pandas loads the data -- (you can add more file suffixes with an additional if statement and with filepaths = ['.xlsx', 'xlsm',])
# 2. -- Calculate some basic sample statistics --
# 4. -- Test for heteroscedasticity (Breusch-Pagan) --
# 5. -- Test for multicollinearity --
# find design matrix for regression model using '' as response variable
# Create an empty DataFrame for VIF results
# Calculate the VIF for each variable and store in the vif_datafr DataFrame
# Print VIF assessment
# 6. -- Test for autocorrelation of residuals (Durbin-Watson) --
# 7. -- Calculate & Print the Spearman Rank correlation and corresponding p-value --

data = input('Please specify the Excel file with the data: ')
datafr = pd.read_excel(data, sheet_name='Sheet13')
datafr = datafr.drop_na(axis=0)

datafr = datafr.astype('int64')

print(datafr.info())
datafr.head()


mean = np.mean(datafr)
variance = np.var(datafr, ddof=1)
std_dev = np.std(datafr, ddof=1)
cv = std_dev / mean

print('Sample Mean: ', mean)
print('Sample Variance: ', variance)
print('Standard Deviation of the sample: ', std_dev)
print('CV: ', cv)

y = datafr[['Q1']]
x = datafr[['Q2', 'Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','BSMAS1','BSMAS2','BSMAS3','BSMAS4','BSMAS5','BSMAS6']]

model = smf.ols(
    'Q1 ~ Q2 + Q3 + Q4 +Q5 + Q6 + Q7 + Q8 + Q9 + Q10 + Q11 + Q12 +Q13 + Q14 + Q15 + Q16 + Q17 + Q18 + Q19 +Q20 +Q21 + Q22 + Q23 + Q24 + Q25 + Q26 + BSMAS1 + BSMAS2 + BSMAS3 + BSMAS4 + BSMAS5+ BSMAS6', datafr).fit()

# Reduced Model
# model = smf.ols(
#     'Q1 ~ Q2 + D1 + D2 + D3 + D4 + BSMAS + Gender + Age_Group +Time_Spent_M + Time_Spent_H + Instagram_index + Facebook_index + TikTok_index + H_Problem',
#     datafr).fit()

print(model.summary())

names = ['Lagrange multiplier statistic', 'p-value', 'f-value', 'f p-value']
bp_test = sms.het_breuschpagan(model.resid, model.model.exog)
print("Result of Breusch-Pagan Test (Heteroscedasticity): ", lzip(names, bp_test))

Y, X = dmatrices(
    'Q1 ~ Q2 + Q3 + Q4 +Q5 + Q6 + Q7 + Q8 + Q9 + Q10 + Q11 + Q12 +Q13 + Q14 + Q15 + Q16 + Q17 + Q18 + Q19 +Q20 +Q21 + Q22 + Q23 + Q24 + Q25 + Q26 + BSMAS1 + BSMAS2 + BSMAS3 + BSMAS4 + BSMAS5+ BSMAS6 + Gender + Education_L +Education_P + Education_Highest + Attach_S + Attach_S_N + Age_Group +Time_Spent_M + Time_Spent_H +Empl_st_sfemp +Empl_st_employee +Empl_st_st +Empl_st_oth + Instagram_index + Facebook_index + TikTok_index + H_Problem',
    data=datafr, return_type='dataframe')

vif_datafr = pd.DataFrame()
vif_datafr['Variable'] = X.columns
vif_datafr['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

for index, row in vif_datafr.iterrows():
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

independent_vars = datafr.columns[datafr.columns != 'Q1']

spearman_corrs = {}
for var in independent_vars:
    corr, p = spearmanr(datafr['Q1'], datafr[var])
    spearman_corrs[var] = (corr, p)

for var, (corr, p) in spearman_corrs.items():
    print(f"Spearman correlation between predictor and {var}: {corr}, p-value: {p}")

print("Analysis Finished, please see the generated files & data")
