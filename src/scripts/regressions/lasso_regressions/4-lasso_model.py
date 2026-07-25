import numpy as np
import pandas as pd
import sklearn
from numpy import arange
from sklearn.linear_model import Lasso
from sklearn.preprocessing import RobustScaler
from scipy.stats import pearsonr
from sklearn.model_selection import RepeatedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

file = input('Please input the file here: ')
df = pd.read_excel(file, sheet_name="ENCODED_DATA")

y = df['Q1']
x = df[['Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
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


alpha = 0.031
lasso = Lasso(alpha=alpha)
lasso.fit(x_train, y_train)

y_pred = lasso.predict(x_test)

print(mean_absolute_error(y_test, y_pred))
print(mean_squared_error(y_test, y_pred))
print(r2_score(y_test, y_pred))

lasso_coefficients = pd.DataFrame({
    'Feature': x.columns,
    'Coefficient': lasso.coef_
})

print(lasso_coefficients)

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


# Apply Robust Transformation
scaler = RobustScaler()
X_train_scaled = scaler.fit_transform(x_train)
X_test_scaled = scaler.transform(x_test)

# Fit a Lasso Regression Model
model = Lasso(alpha=1.0)
model.fit(X_train_scaled, y_train)

# Make Predictions
y_pred = model.predict(X_test_scaled)

# Calculate Spearman Correlation
pearson_corr, _ = pearsonr(y_test, y_pred)

print(f"Pearson Correlation: {pearson_corr:.4f}")

#3. -- Display lambda that produced the lowest test MSE --
#print(model.alpha_)
