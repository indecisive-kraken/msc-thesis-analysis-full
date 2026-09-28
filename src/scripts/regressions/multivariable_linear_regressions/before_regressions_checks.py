import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
from statsmodels.compat import lzip
from scipy.stats import shapiro, jarque_bera
from scipy.stats import skew, kurtosis
from statsmodels.formula.api import ols
from statsmodels.stats.stattools import omni_normtest
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.outliers_influence import variance_inflation_factor
from scipy import stats
from scipy.stats import spearmanr
from statsmodels.stats.outliers_influence import OLSInfluence
from patsy import dmatrices

# data = input('Please specify the Excel file with the data: ')
data = "/home/nopesferatu/Desktop/Thesis_R2_v2/analysis/data/o1_maybe_lates.xlsx"
df = pd.read_excel(data, sheet_name='INDIV_VAR_REG')

print(df.info())
df.head()

y = df[['D1']]
x = df[['D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
          'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
          'Instagram_index', 'Facebook_index', 'TikTok_index', 'YouTube_Index']]

model = smf.ols("D1 ~ BSMAS +  Time_Spent_H + Time_Spent_M", df).fit()
model2 =  smf.ols('D2 ~ BSMAS + Time_Spent_H + Time_Spent_M', df).fit()
model3 = smf.ols('D3 ~ BSMAS', df).fit()
model4 = smf.ols('D4 ~ BSMAS + Education_L + Education_P + Education_Highest',df).fit()
model5 = smf.ols(formula='BSMAS ~ Age_Group + Time_Spent_M + Time_Spent_H + Facebook_index', data=x).fit()

list_models = [model, model2, model3, model4, model5]

string_list = ['D1', 'D2', 'D3', 'D4', 'BSMAS']
for ex in string_list:
    print("Skewness {}: ".format(ex), x[ex].skew())
    print("Kurtosis {}: ".format(ex), x[ex].kurtosis())

for model in list_models:
    print("Shapiro: ", shapiro(model.resid))
    print("Jarque-Bera: ", jarque_bera(model.resid))
    print("Durbin-Watson: ", durbin_watson(model.resid))
    X = model.model.exog
    print(X.shape[1])
    vif = [variance_inflation_factor(X, i) for i in range(X.shape[1])]
    print("VIF:", vif)
    influence = OLSInfluence(model)
    cooks = influence.cooks_distance[0]
    print("Cooks:", cooks)


model  = smf.ols('D1 ~ D2 + D3 + D4 + BSMAS', df).fit(cov_type='HC3')
model2 = smf.ols('D2 ~ D1 + D3 + D4 + BSMAS', df).fit(cov_type='HC3')
model3 = smf.ols('D3 ~ D1 + D2 + D4 + BSMAS', df).fit(cov_type='HC3')
model4 = smf.ols('D4 ~ D1 + D2 + D3 + BSMAS', df).fit(cov_type='HC3')