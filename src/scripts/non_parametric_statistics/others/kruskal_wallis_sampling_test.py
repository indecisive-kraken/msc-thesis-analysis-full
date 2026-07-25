import os
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import kruskal


def do_you_accept_columns():
    answer = input('Please specify with a yes or no if you agree with the columns: ')
    while answer.lower() != 'yes' and answer.lower() != 'no':
        print('The current accepts only yes or no')
        answer = input('Please specify with a yes or no if you agree with the columns: ')
    if answer.lower() == 'no':
        print('Closing the script, please modify the data')
        os._exit()

data = input('Please specify the Excel file with the data: ')
df = pd.read_excel(data, sheet_name='ENCODED_DATA')

print(df.info())
df.head()

all = df[['Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

separation_1 = all.iloc[2:49]
separation_2 = all.iloc[50:63]
separation_3 = all.iloc[64:70]
separation_4 = all.iloc[71:103]
separation_5 = all.iloc[104:110]
separation_6 = all.iloc[110:113]

arr = [separation_1,separation_2,separation_3,separation_4,separation_5,separation_6]

complete_df = [
    separation_1.values.flatten(),
    separation_2.values.flatten(),
    separation_3.values.flatten(),
    separation_4.values.flatten(),
    separation_5.values.flatten(),
    separation_6.values.flatten()]

print(f"{complete_df[:3]} ... {complete_df[-3:]}")

print(stats.kruskal(*complete_df))