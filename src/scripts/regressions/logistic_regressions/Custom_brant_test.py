import pandas as pd
import numpy as np
import statsmodels.api as sm
from mord import LogisticAT
from sklearn.linear_model import LogisticRegression

# 1. -- Check if the file is of valid type, after that Pandas loads the data -- (you can add more file suffixes with an additional if statement and with filepaths = ['.xlsx', 'xlsm',])
data = input('Please specify the Excel file with the data: ')
df = pd.read_excel(data, sheet_name='ENCODED_DATA')

y = df['Q1']
x = df[['Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

model = LogisticAT(alpha=1.0)
model.fit(x, y)

def fit_binary_logit(X, y_binary):
    X = sm.add_constant(x)
    logit_model = sm.Logit(y_binary, x).fit(disp=0)
    return logit_model

# First threshold: y <= 0 vs y > 0
y1 = (y <= 0).astype(int)
model1 = fit_binary_logit(x, y1)

# Second threshold: y <= 1 vs y > 1
y2 = (y <= 1).astype(int)
model2 = fit_binary_logit(x, y2)

# Compare coefficients
print("Model 1 Coefficients:\n", model1.params)
print("Model 2 Coefficients:\n", model2.params)