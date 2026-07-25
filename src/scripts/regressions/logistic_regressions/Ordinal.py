import numpy as np
import pandas as pd
from statsmodels.miscmodels.ordinal_model import OrderedModel
from patsy import dmatrices
from scipy.stats import spearmanr

#1. -- Check if the file is of valid type, after that Pandas loads the data -- (you can add more file suffixes with an additional if statement and with filepaths = ['.xlsx', 'xlsm',])
data = input('Please specify the Excel file with the data: ')
df = pd.read_excel(data, sheet_name='INDIV_VAR_REG')

#1. -- Ordinal regression model --

# y = df['Q1']
# x = df[['Q2','D1','D2','D3','D4','BSMAS','Gender','Education_L','Education_P','Education_Highest','Age_Group','Time_Spent_M','Time_Spent_H','Empl_st_sfemp','Empl_st_employee','Empl_st_st','Empl_st_oth','Instagram_index','Facebook_index','TikTok_index','H_Problem','Attach_S','Attach_S_N' ]]

y = df['Q1']
x = df[['Q2', 'Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','BSMAS1','BSMAS2','BSMAS3','BSMAS4','BSMAS5','BSMAS6','Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

ordinal_model = OrderedModel(y, x, distr='probit')
mod_log = OrderedModel(y, x, distr='probit')
res_log = mod_log.fit(method='bfgs')
print(res_log.summary())


independent_vars = df.columns[df.columns != 'Q1']

spearman_corrs = {}
for var in independent_vars:
    corr, p = spearmanr(df['Q1'], df[var])
    spearman_corrs[var] = (corr, p)

for var, (corr, p) in spearman_corrs.items():
    print(f"Spearman correlation between predictor and {var}: {corr}, p-value: {p}")


predicted = res_log.model.predict(res_log.params, exog=x)

#pred_choice = predicted.argmax(1)
#print('Fraction of correct choice predictions')
#print(np.asarray(y.values.codes) == pred_choice).mean()