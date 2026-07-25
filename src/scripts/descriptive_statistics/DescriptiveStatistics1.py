import os
import numpy as np
import pandas as pd
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

# all = df[['Q1','Q2', 'Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','BSMAS1','BSMAS2','BSMAS3','BSMAS4','BSMAS5','BSMAS6','Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
#         'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
#         'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N', 'BSMAS']]

all = df[['Q1','Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

all1 = df[['D1', 'D2', 'D3', 'D4', 'BSMAS',]]
results_me_var_med = {}

for column in all1.columns:

   print(column,
        np.mean(df[column]),
        np.std(df[column]),
        np.median(df[column]),
        np.min(df[column]),
        np.max(df[column]))

    # results_me_var_med[column] = {
    #     'Mean of variable ' : mean_varb,
    #     'St.Dev of variable ' : variance_varb,
    #     'Median of variable '  : median_varb
    # }
    #
    # results_df = pd.DataFrame.from_dict(results_me_var_med, orient='index')
    #
    # results_df.to_csv('desc_stats_results_for_all_varscopy.csv')
    # print(results_df)