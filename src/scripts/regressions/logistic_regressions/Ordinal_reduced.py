import numpy as np
import pandas as pd
from statsmodels.miscmodels.ordinal_model import OrderedModel
from patsy import dmatrices

#1. -- Check if the file is of valid type, after that Pandas loads the data -- (you can add more file suffixes with an additional if statement and with filepaths = ['.xlsx', 'xlsm',])
data = input('Please specify the Excel file with the data: ')
df = pd.read_excel(data, sheet_name='ENCODED_DATA')

#1. -- Ordinal regression model --

y = df['Q1']
x = df[['Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H',
        'Instagram_index', 'Facebook_index', 'TikTok_index']]


ordinal_model = OrderedModel(y, x, distr='logit')
mod_log = OrderedModel(y, x, distr='logit')
res_log = mod_log.fit(method='bfgs')
print(res_log.summary())

predicted = res_log.model.predict(res_log.params, exog=x)

#pred_choice = predicted.argmax(1)
#print('Fraction of correct choice predictions')
#print(np.asarray(y.values.codes) == pred_choice).mean()