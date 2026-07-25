import os
import warnings
import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import mannwhitneyu

warnings.filterwarnings('ignore')

def do_you_accept_columns():
    answer = input('Please specify with a yes or no if you agree with the columns: ')
    while answer.lower() != 'yes' and answer.lower() != 'no':
        print('The current accepts only yes or no')
        answer = input('Please specify with a yes or no if you agree with the columns: ')
    if answer.lower() == 'no':
        print('Closing the script, please modify the data')
        os._exit()


data = input('Please specify the Excel file with the data: ')
df = pd.read_excel(data, sheet_name='INDIV_VAR_REG')

print(df.info())
df.head()

all = df[['BSMAS']]

bsmas_group1 = all[all['BSMAS'] > 14]
bsmas_group2 = all[all['BSMAS'] <= 14]

print(bsmas_group1)
print()
print(bsmas_group2)

do_you_accept_columns()

# perform mann whitney test
stat, p_value = mannwhitneyu(bsmas_group1, bsmas_group2)
print('Statistics=%.2f, p=%.2f' % (stat, p_value))
# Level of significance
alpha = 0.05
# conclusion
if p_value < alpha:
    print('Reject Null Hypothesis (Significant difference between two samples)')
else:
    print('Do not Reject Null Hypothesis (No significant difference between two samples)')



