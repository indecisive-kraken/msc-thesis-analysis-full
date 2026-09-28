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
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# from resample.bootstrap import bootstrap
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from scipy import stats
from scipy.stats import spearmanr
from patsy import dmatrices

# 1. -- Check if the file is of valid type, after that Pandas loads the data -- (you can add more file suffixes with an additional if statement and with filepaths = ['.xlsx', 'xlsm',])
data = input('Please specify the Excel file with the data: ')
df = pd.read_excel(data, sheet_name='Sheet15')

print(df.info())
df.head()

# 2. -- Calculate some basic sample statistics --
mean = np.mean(df)
variance = np.var(df, ddof=1)
std_dev = np.std(df, ddof=1)
cv = std_dev / mean

print('Sample Mean: ', mean)
print('Sample Variance: ', variance)
print('Standard Deviation of the sample: ', std_dev)
print('CV: ', cv)

# 3. -- Fit a linear regression assuming Gaussian Distribution --
y = df['Q1']
x1 = df[['Q2', 'Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','BSMAS1','BSMAS2','BSMAS3','BSMAS4','BSMAS5','BSMAS6','Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

x2 = df[['Q2', 'Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','BSMAS1','BSMAS2','BSMAS3','BSMAS4','BSMAS5','BSMAS6']]

model = sm.OLS(y, x2).fit(cov_type="HC3")

#model = smf.ols(
#    'Q1 ~ Q2 + Q3 + Q4 +Q5 + Q6 + Q7 + Q8 + Q9 + Q10 + Q11 + Q12 +Q13 + Q14 + Q15 + Q16 + Q17 + Q18 + Q19 +Q20 +Q21 + Q22 + Q23 + Q24 + Q25 + Q26 + BSMAS1 + BSMAS2 + BSMAS3 + BSMAS4 + BSMAS5+ BSMAS6 + Gender + Education_L +Education_P + Education_Highest + Attach_S + Attach_S_N + Age_Group +Time_Spent_M + Time_Spent_H +Empl_st_sfemp +Empl_st_employee +Empl_st_st +Empl_st_oth + Instagram_index + Facebook_index + TikTok_index + H_Problem', df).fit()

# Reduced Model
# model = smf.ols(
#     'Q1 ~ Q2 + D1 + D2 + D3 + D4 + BSMAS + Gender + Age_Group +Time_Spent_M + Time_Spent_H + Instagram_index + Facebook_index + TikTok_index + H_Problem',
#     df).fit()

print(model.summary())

X_train, X_test, y_train, y_test = train_test_split(x2, y, test_size=0.2, random_state=42)

model2 = LinearRegression()
model2.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r_squared = r2_score(y_test, y_pred)

print(f'Mean Squared Error (MSE): {mse: 2f}')
print(f'R-squared : {r_squared : 2f}')

# # 4. -- Test for heteroscedasticity (Breusch-Pagan) --
# names = ['Lagrange multiplier statistic', 'p-value', 'f-value', 'f p-value']
# bp_test = sms.het_breuschpagan(model.resid, model.model.exog)
# print("Result of Breusch-Pagan Test (Heteroscedasticity): ", lzip(names, bp_test))

# 5. -- Test for multicollinearity --
# find design matrix for regression model using '' as response variable
Y, X = dmatrices(
    'Q1 ~ Q2 + Q3 + Q4 +Q5 + Q6 + Q7 + Q8 + Q9 + Q10 + Q11 + Q12 +Q13 + Q14 + Q15 + Q16 + Q17 + Q18 + Q19 +Q20 +Q21 + Q22 + Q23 + Q24 + Q25 + Q26 + BSMAS1 + BSMAS2 + BSMAS3 + BSMAS4 + BSMAS5+ BSMAS6 + Gender + Education_L +Education_P + Education_Highest + Attach_S + Attach_S_N + Age_Group +Time_Spent_M + Time_Spent_H +Empl_st_sfemp +Empl_st_employee +Empl_st_st +Empl_st_oth + Instagram_index + Facebook_index + TikTok_index + H_Problem',
    data=df, return_type='dataframe')

# Create an empty DataFrame for VIF results
vif_df = pd.DataFrame()

# Calculate the VIF for each variable and store in the vif_df DataFrame
vif_df['Variable'] = X.columns
vif_df['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

# Print VIF assessment
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

# 6. -- Test for autocorrelation of residuals (Durbin-Watson) --
print('Autocorrelation of residuals: ', durbin_watson(model.resid))

# 7. -- Calculate & Print the Spearman Rank correlation and corresponding p-value --

independent_vars = df.columns[df.columns != 'Q1']

spearman_corrs = {}
for var in independent_vars:
    corr, p = spearmanr(df['Q1'], df[var])
    spearman_corrs[var] = (corr, p)

for var, (corr, p) in spearman_corrs.items():
    print(f"Spearman correlation between predictor and {var}: {corr}, p-value: {p}")

# # -- Bootstraping Section
#
# def fitreg(A):
#     scale = StandardScaler()
#     reg = LinearRegression(fit_intercept=True)
#     X_scale = scale.fit_transform(A[:, :A.shape[1]-2])
#     y = A[:, A.shape[1]-1]
#     reg.fit(X_scale, y)
#     return {"coef": reg.coef_, "intercept": reg.intercept_}
#
# boot_coef = bootstrap(sample=x2.join(y).values, fn=fitreg)
# print(boot_coef)
#
# print("Analysis Finished, please see the generated files & data")
