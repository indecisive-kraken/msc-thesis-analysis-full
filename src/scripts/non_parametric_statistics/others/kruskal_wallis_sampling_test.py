import os
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import kruskal
from scripts.data.get_data_path import open_data_file


def kruskal_wallis_sampling_test():

    df = open_data_file()
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

kruskal_wallis_sampling_test()