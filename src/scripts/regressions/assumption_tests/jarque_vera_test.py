import pandas as pd
from scipy.stats import jarque_bera
from scripts.data.get_data_path import open_data_file

def jarque_bera_test():

        df = open_data_file().dropna()
        print(df.info())
        df.head()

        all = df[['Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest',
                  'Age_Group',
                  'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
                  'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

        stat, p_value = jarque_bera(df)

        print(f"Jarque-Bera statistic & p-value: {stat} {p_value}")

jarque_bera_test()