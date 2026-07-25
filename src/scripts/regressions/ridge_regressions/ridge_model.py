import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange
from sklearn.linear_model import Ridge
from sklearn import preprocessing
from sklearn.model_selection import RepeatedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import RobustScaler
from scipy.stats import pearsonr
from scipy.stats import spearmanr

file = input('Please input the file here: ')
df = pd.read_excel(file, sheet_name="INDIV_VAR_REG")

y = df['Q1']
# x = df[['Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
#         'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
#         'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

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

x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

alpha = 49

ridge = Ridge(alpha=alpha)
ridge.fit(x_train, y_train)

y_pred = ridge.predict(x_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R-squared: ", r2_score(y_test, y_pred))

ridge_coefficients = pd.DataFrame({
    'Feature': x.columns,
    'Coefficient': ridge.coef_
})

print(ridge_coefficients)

scaler = RobustScaler()
X_train_scaled = scaler.fit_transform(x_train)
X_test_scaled = scaler.transform(x_test)

# Fit a Lasso Regression Model
model = Ridge(alpha=100)
model.fit(X_train_scaled, y_train)

# Make Predictions
y_pred = model.predict(X_test_scaled)

# Calculate Spearman Correlation
spearman_corr, _ = spearmanr(y_test, y_pred)

print(f"Spearman Correlation: {spearman_corr:.4f}")

#3. -- Display lambda that produced the lowest test MSE --
#print(model.alpha_)

df_scaled = preprocessing.scale(df)
df_scaled = pd.DataFrame(df_scaled)

ysc = df_scaled.iloc[:, 0:1]
xsc = df_scaled.iloc[:, 1:48]

print("Scaled Dataframe")
print(df_scaled.info())
print("Dataframe of Y scaled")
print(ysc.info())
print("Dataframe of X scaled")
print(xsc.info())

independent_vars = df_scaled.columns[df_scaled.columns != '0']

coef = []
ridgereg = Ridge(alpha=49)
ridgereg.fit(xsc, ysc)
coef.append(ridgereg.coef_)

df_coef = pd.DataFrame(coef)
print("Dataframe containing coefficients: ")
print(df_coef.info())

print("All elements of array coef \n", coef)
print("First element of array coef \n", coef[0])

spearman_corrs = {}

arr_new = coef.pop(0)

for co in coef:
    corr, p = spearmanr(coef[0], arr_new)
    spearman_corrs[co] = (corr, p)
    print(f"Spearman correlation between predictor and {co}: {corr}, p-value: {p}")

# spearman_corrs = {}
# y_coef = df_coef.columns[df_coef.columns == '0']

# for var in independent_vars:
#     corr, p = spearmanr(y_coef, df_coef[var])
#     spearman_corrs[var] = (corr, p)
#
# for var, (corr, p) in spearman_corrs.items():
#     print(f"Spearman correlation between predictor and {var}: {corr}, p-value: {p}")

def sse_calc(y, y_pred):
    sse = np.sum((y - y_pred)**2)

    for i, (yi, yp) in enumerate(zip(y, y_pred)):
        diff = yi - yp
        print(f"Point {i + 1}: ({yi:.2f} - {yp:.2f})**2 = {diff**2: .2f}")
    print(f"SSE = {sse:.2f}")
    return sse

def aic_calc(n, sse, k):
    aic = np.log(sse/n) + 2 * (k /n)
    return aic

def bic_calc(n, sse, k):
    bic = np.log(sse/n) + (k/n) * np.log(n)
    return bic

sse = sse_calc(y_test, y_pred)
aic = aic_calc(111,sse,112 )
bic = bic_calc(111,sse,112)
print("AIC: ", aic)
print("BIC: ", bic)