import numpy
import pandas as pd
import sklearn
from numpy import arange
from sklearn.linear_model import Ridge
from sklearn.model_selection import RepeatedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import RobustScaler
from scipy.stats import pearsonr

file = input('Please input the file here: ')

df = pd.read_excel(file, sheet_name="ENCODED_DATA")

y = df['Q1']
x = df[['Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H',
        'Instagram_index', 'Facebook_index', 'TikTok_index']]

print('Shape of x:', x.shape)
print('Shape of y:', y.shape)
#1. -- Define cross-validation method to evaluate the model --

cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)

#2. -- Define and fit the model --
scaler = StandardScaler()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=102)

x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)
alpha = 100
ridge = Ridge(alpha=alpha)
ridge.fit(x_train, y_train)

y_pred = ridge.predict(x_test)

print(mean_absolute_error(y_test, y_pred))
print(mean_squared_error(y_test, y_pred))
print(r2_score(y_test, y_pred))

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
pearson_corr, _ = pearsonr(y_test, y_pred)

print(f"Pearson Correlation: {pearson_corr:.4f}")


#3. -- Display lambda that produced the lowest test MSE --
#print(model.alpha_)
