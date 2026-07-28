import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
from statsmodels.compat import lzip
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.outliers_influence import variance_inflation_factor
from scipy.stats import spearmanr
from scipy.stats import pearsonr
from patsy import dmatrices

# -- Table of Contents --
# 1. -- Check if the file is of valid type, after that Pandas loads the data -- (you can add more file suffixes with an additional if statement and with filepaths = ['.xlsx', 'xlsm',])
# 2. -- Calculate some basic sample statistics --
# 3. -- Fit a linear regression assuming Gaussian Distribution and the assumptions of linear regression hold--
# 4. -- Test for heteroscedasticity (Breusch-Pagan) --
# 5. -- Test for multicollinearity --
  # find design matrix for regression model using '' as response variable
  # Create an empty DataFrame for VIF results
  # Calculate the VIF for each variable and store in the vif_df DataFrame
  # Print VIF assessment
# 6. -- Test for autocorrelation of residuals (Durbin-Watson) -
# 7. -- Calculate & Print the Spearman Rank correlation and corresponding p-value --

#1
# data = input('Please specify the Excel file with the data: ')
data = '/home/nopesferatu/Desktop/Thesis_R2_v2/analysis/data/o1_maybe_lates.xlsx'
df = pd.read_excel(data, sheet_name='INDIV_VAR_REG')

print(df.info())
df.head() 
#
# #2
mean = np.mean(df)
variance = np.var(df, ddof=1)
std_dev = np.std(df, ddof=1)
cv = std_dev / mean

print('Sample Mean: ', mean)
print('Sample Variance: ', variance)
print('Standard Deviation of the sample: ', std_dev)
print('CV: ', cv)

x = df[['D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
          'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
          'Instagram_index', 'Facebook_index', 'TikTok_index', 'YouTube_Index']]
y = df[['D1']]

model1 = smf.ols('D1 ~ D2 + D3 + D4 + BSMAS',df).fit()
model2 =  smf.ols('D2 ~ D1 + D3 + D4 + BSMAS',df).fit()
model3 = smf.ols('D3 ~ D1 + D2 + D4 + BSMAS',df).fit()
model4 = smf.ols('D4 ~ D1 + D2 + D3 + BSMAS',df).fit()

model_hc3  = smf.ols('D1 ~ D2 + D3 + D4 + BSMAS', df).fit(cov_type='HC3')
model2_hc3 = smf.ols('D2 ~ D1 + D3 + D4 + BSMAS', df).fit(cov_type='HC3')
model3_hc3 = smf.ols('D3 ~ D1 + D2 + D4 + BSMAS', df).fit(cov_type='HC3')
model4_hc3 = smf.ols('D4 ~ D1 + D2 + D3 + BSMAS', df).fit(cov_type='HC3')


model1_ext = smf.ols(formula='D1 ~ BSMAS +  Time_Spent_H + Time_Spent_M', data=x).fit()
model2_ext = smf.ols(formula='D2 ~ BSMAS + Time_Spent_H + Time_Spent_M', data=x).fit()
model3_ext = smf.ols(formula='D3 ~ BSMAS', data=x).fit()
model4_ext = smf.ols(formula='D4 ~ BSMAS + Education_L + Education_P + Education_Highest', data=x).fit()
model5_ext = smf.ols(formula='BSMAS ~ Age_Group + Time_Spent_M + Time_Spent_H + Facebook_index', data=x).fit()
modelextra = smf.ols(formula='BSMAS ~ Age_Group + Time_Spent_M + Time_Spent_H + TikTok_index', data=x).fit()
modelextra_forD4 = smf.ols(formula='D4 ~ BSMAS + Gender + Education_L + Education_P + Education_Highest', data=x).fit()

print(modelextra.summary())

print(modelextra_forD4.summary())

array_model = [model1, model2, model3, model4, model_hc3, model2_hc3, model3_hc3, model4_hc3, model1_ext, model2_ext, model3_ext, model4_ext, model5_ext, modelextra, modelextra_forD4]

for array in array_model:
    print(array.summary())

arr_var = ["D1", "D2", "D3", "D4", "BSMAS"]

def arr_func(*args) :
    for var in arr_var:
        index = 0
        while (index < len(arr_var) -1):
            sns.residplot(data=df, x=arr_var[index], y=arr_var[index + 1])
            plt.axhline(0, color='red')
            plt.savefig('residplot{}{}.png'.format(var, index))
            index += 1

arr_func(arr_var)


model1 = smf.ols(formula='D1 ~ BSMAS +  Time_Spent_H + Time_Spent_M', data=x).fit()
model2 = smf.ols(formula='D2 ~ BSMAS + Time_Spent_H + Time_Spent_M', data=x).fit()
model3 = smf.ols(formula='D3 ~ BSMAS', data=x).fit()
model4 = smf.ols(formula='D4 ~ BSMAS + Education_L + Education_P + Education_Highest', data=x).fit()
model5 = smf.ols(formula='BSMAS ~ Age_Group + Time_Spent_M + Time_Spent_H + Facebook_index', data=x).fit()

#4
names = ['Lagrange multiplier statistic', 'p-value', 'f-value', 'f p-value']
bp_test = sms.het_breuschpagan(model1.resid, model1.model.exog)
print("Result of Breusch-Pagan Test (Heteroscedasticity): ", lzip(names, bp_test))
bp_test = sms.het_breuschpagan(model2.resid, model2.model.exog)
print("Result of Breusch-Pagan Test (Heteroscedasticity): ", lzip(names, bp_test))
bp_test = sms.het_breuschpagan(model3.resid, model3.model.exog)
print("Result of Breusch-Pagan Test (Heteroscedasticity): ", lzip(names, bp_test))
bp_test = sms.het_breuschpagan(model4.resid, model4.model.exog)
print("Result of Breusch-Pagan Test (Heteroscedasticity): ", lzip(names, bp_test))
bp_test = sms.het_breuschpagan(model5.resid, model5.model.exog)
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
for mod in array_model:
    print('Autocorrelation of residuals: ', durbin_watson(mod.resid))

#7
independent_vars = df.columns[df.columns != 'D1']

spearman_corrs = {}
for var in independent_vars:
    corr, p = spearmanr(y, df[var])
    spearman_corrs[var] = (corr, p)

for var, (corr, p) in spearman_corrs.items():
    print(f"Spearman correlation between predictor and {var}: {corr}, p-value: {p}")

independent_vars = df.columns[df.columns != 'BSMAS']
dependent_vars = ['D1', 'D2', 'D3', 'D4', 'BSMAS']

for dep in dependent_vars:
    y = df[dep]
    pearson_corrs = {}

    for var in independent_vars:
        corr, p = pearsonr(y, df[var])
        spearman_corrs[var] = (corr, p)


    print(f"\nSpearman correlations with {dep}:")
    for var, (corr, p) in spearman_corrs.items():
        print(f"  - {var}: correlation = {corr}, p-value = {p}")
print("Analysis Finished, please see the generated files & data")
