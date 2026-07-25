import numpy as np
import pandas as pd
from statistics import LinearRegression
from numpy import arange
from sklearn.model_selection import RepeatedKFold
from sklearn.linear_model import HuberRegressor
from sklearn.linear_model import RANSACRegressor
from sklearn.linear_model import TheilSenRegressor
from statsmodels.stats.outliers_influence import variance_inflation_factor
import os
from matplotlib import pyplot
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


# 1. -- Check if the file is of valid type, after that Pandas loads the data -- (you can add more file suffixes with an additional if statement and with filepaths = ['.xlsx', 'xlsm',])
data = input('Please specify the Excel file with the data: ')
df = pd.read_excel(data, sheet_name='INDIV_VAR_REG')

# y = df['Q1']
# x = df[['Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
#         'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
#         'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

y = df[['D1']].dropna()
x = df[['D2', 'D3', 'D4', 'BSMAS']].dropna()

print(x.info)
print(y.info)

linear = LinearRegression(intercept=True, slope=True)
huber = HuberRegressor(max_iter = 1000)
RANSAC = RANSACRegressor()
TheilSen = TheilSenRegressor()

huber_regression = huber.fit(x, y)
huber_score = huber.score(x, y)
print(huber_score)
#huber.predict(x[:1,])
#print("Coefficients of regressions:", huber.coef_)

RANSAC_regression = RANSAC.fit(x, y)
RANSAC_score = RANSAC.score(x, y)
print(RANSAC_score)

Theilsen_regression = TheilSen.fit(x, y)
Theilsen_score = TheilSen.score(x, y)
print(Theilsen_score)

'''
xaxis = arange(x.min(), x.max(), 0.01)
for model in get_models():
    #plot the line of best fit
    plot_best_fit(x, y, xaxis, model)

pyplot.scatter(x, y)
pyplot.title('Robust Regression')
pyplot.legend()
pyplot.show()
'''


def mse(actual, pred):
    actual, pred = np.array(actual), np.array(pred)
    return np.square(np.subtract(actual, pred)).mean()