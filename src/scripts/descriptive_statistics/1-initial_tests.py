import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pingouin import multivariate_normality
from scipy import stats
from patsy import dmatrices
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
data = os.getenv("DATA")

#1. -- Check if the file is of valid type, after that Pandas loads the data -- (you can add more file suffixes with an additional if statement and with filepaths = ['.xlsx', 'xlsm',])
if Path(data).suffix == '.xlsx':
    print('File received, proceeding...')
else:
    print('File is not of the form .xlsx, please input a valid file')
    os._exit()

df = pd.read_excel(data, sheet_name='ENCODED_DATA')
y = df['Q1']
x = df[['Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

#check if you agree with the data, if not the script is halted

print(df.info())


# answer = input('Please specify with a yes or no if you agree with the columns: ')

# while answer.lower() != 'yes' and answer.lower() != 'no':
#     print('The current accepts only yes or no')
#     answer = input('Please specify with a yes or no if you agree with the columns: ')
#     if answer.lower() == 'no':
#         print('Closing the script, please modify the data')
#         os._exit()

# -- Tests --

#2.1. -- Tests for Normality (Anderson-Darling, Kolmongorov-Smirvov) --

dataf = pd.DataFrame(df)
mv = multivariate_normality(dataf, alpha=0.5)

print(mv)
# #anderson(df, dist='norm')
# print(stats.kstest(df))
#
#  #2.2. -- Non-Parametric Tests --
#  #2.2.1. -- Non-Parametric Tests (Kruskal-Walls) --
#
# print(stats.kruskal(df))
#
#  #2.2.2. -- Non-Parametric Tests (Mann-Whitney U Test, to check if the variables follow a normal distribution) --
#
# stats.mannwhitneyu(df)
#
# corr_matrix = df.corr(method='pearson')
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
# plt.title('Correlation Heatmap')
# plt.show()
#
# #fig = plt.figure(figsize=(12, 8))
# #fig = sm.graphics.plot_regress_exog(fit, '', fig=fig)

