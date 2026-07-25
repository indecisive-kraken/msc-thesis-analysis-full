import numpy
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from numpy import arange
from sklearn.linear_model import Ridge
from sklearn.model_selection import RepeatedKFold
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.linear_model import RidgeCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import RobustScaler
from scipy.stats import pearsonr

file = input('Please input the file here: ')

df = pd.read_excel(file, sheet_name="INDIV_VAR_REG")

# y = df['Q1']
# x = df[['Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
#         'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
#         'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]
#
# x2 = df[['Q2', 'Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','BSMAS1','BSMAS2','BSMAS3','BSMAS4','BSMAS5','BSMAS6']]
#
# print('Shape of x:', x2.shape)
# print('Shape of y:', y.shape)
# #1. -- Define cross-validation method to evaluate the model --

cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)

#2. -- Define and fit the model --
df_scaled = preprocessing.scale(df)
df_scaled = pd.DataFrame(df_scaled)

ys = df_scaled.iloc[:, 0]
xs = df_scaled.iloc[:, 1:31]

print("Response",ys)
print("Independent Vars", xs)

alpha = 100
ridge = Ridge(alpha=alpha)
ridge.fit(xs, ys)

coef = []
alphas = range(0, 50)

for a in alphas:
    ridgereg=Ridge(alpha=a)
    ridgereg.fit(xs,ys)
    coef.append(ridgereg.coef_)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(alphas, coef)
ax.set_xlabel('Alpha (Regularization Parameter)')
ax.set_ylabel('Beta (Predictor Coefficients)')
ax.set_title('Ridge Coefficients vs Regularization Techniques')
ax.axis('tight')
fig.savefig('coef_vs_alpha.png')

# Standardization
scaler = StandardScaler()
X_std = scaler.fit_transform(xs)

# Fit Ridge Regression through cross-validation
regr_cv = RidgeCV(alphas=range(1, 50))
model_cv = regr_cv.fit(X_std, ys)

print(model_cv.alpha_)

# y_pred = ridge.predict(x_test)
#
# print(mean_absolute_error(y_test, y_pred))
# print(mean_squared_error(y_test, y_pred))
# print(r2_score(y_test, y_pred))
#
# ridge_coefficients = pd.DataFrame({
#     'Feature': x.columns,
#     'Coefficient': ridge.coef_
# })
#
# print(ridge_coefficients)
#
#
# scaler = RobustScaler()
# X_train_scaled = scaler.fit_transform(x_train)
# X_test_scaled = scaler.transform(x_test)
#
# # Fit a Lasso Regression Model
# model = Ridge(alpha=100)
# model.fit(X_train_scaled, y_train)
#
# # Make Predictions
# y_pred = model.predict(X_test_scaled)
#
# # Calculate Spearman Correlation
# pearson_corr, _ = pearsonr(y_test, y_pred)
#
# print(f"Pearson Correlation: {pearson_corr:.4f}")
#
#
# #3. -- Display lambda that produced the lowest test MSE --
# #print(model.alpha_)



