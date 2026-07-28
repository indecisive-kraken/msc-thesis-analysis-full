import pandas as pd
from pingouin import multivariate_normality
from scripts.data.get_data_path import open_data_file

def multivariate_normality_test():

        df = open_data_file()
        y = df['Q1']
        x = df[['Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
                'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
                'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

        # -- Tests for Multivariate Normality  --

        data = pd.DataFrame(df)
        print(multivariate_normality(data, alpha=0.5))

multivariate_normality_test()