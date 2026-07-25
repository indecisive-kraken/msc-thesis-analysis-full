import mord
import numpy as np
import pandas as pd
import sklearn
import seaborn as sns
from mord import OrdinalRidge
from numpy import arange
from sklearn.linear_model import Ridge
from sklearn.model_selection import RepeatedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder

# Performance metrics
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.metrics import log_loss
from sklearn.linear_model import Ridge
from sklearn.preprocessing import RobustScaler
from scipy.stats import pearsonr

file = input('Please input the file here: ')

df = pd.read_excel(file, sheet_name="INDIV_VAR_REG")

y = df['Q1']
x = df[['Q2', 'Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','BSMAS1','BSMAS2','BSMAS3','BSMAS4','BSMAS5','BSMAS6','Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

print('Shape of x:', x.shape)
print('Shape of y:', y.shape)
#1. -- Define cross-validation method to evaluate the model --

cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)

#2. -- Define and fit the model --
scaler = StandardScaler()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=102)

ord_reg = OrdinalRidge()
ord_reg.fit(x_train, y_train)

y_pred = ord_reg.predict(x_test)

ridge_coefficients = pd.DataFrame({
    'Feature': x.columns,
    'Coefficient': ord_reg.coef_
})

print(ridge_coefficients)
print(f'MAE: {mean_absolute_error(y_test, y_pred)}')
print(f'MSE: {mean_squared_error(y_test, y_pred)}')
print(f'R-Squared: {r2_score(y_pred, y_test)}')


def sse_calc(y_test, y_pred):
    sse = np.sum((y_test - y_pred)**2)
    return sse

def aic_calc(n, sse, k):
    aic = n * np.log(sse / n) + 2 * k
    return aic

def bic_calc(n, sse, k):
    bic = n * np.log(sse/n) + k + np.log(n)
    return bic

sse = sse_calc(y_test, y_pred)
aic = aic_calc(111,sse,112 )
bic = bic_calc(111,sse,112)
print("AIC: ", aic)
print("BIC: ", bic)

# ord_reg_prob = mord.OrdinalRidge()
# ord_reg_prob.fit(x, y)
#
# y_prob = ord_reg_prob.predict_proba(x)
# log_likelihood = -log_loss(y, y_prob, normalize=False)
# k = x.shape[1] + 1
# n = x.shape[0]
#
# AIC = -2 * log_likelihood + 2 * k
# BIC = -2 * log_likelihood + np.log(n) * k
#
# print("AIC: ",AIC)
# print("BIC: ",BIC)
#
# accuracy = accuracy_score(y_test, y_pred)
# mae = mean_absolute_error(y_test, y_pred)
#
# print(accuracy)
# print(mae)
#
# cm = confusion_matrix(y_test, y_pred)
# print(cm)
#
#
# # Calculate Spearman Correlation
# pearson_corr, _ = pearsonr(y_test, y_pred)
#
# print(f"Pearson Correlation: {pearson_corr:.4f}")
#
# sns.heatmap(cm/np.sum(cm), annot=True,fmt='.2%', cmap='GnBu')