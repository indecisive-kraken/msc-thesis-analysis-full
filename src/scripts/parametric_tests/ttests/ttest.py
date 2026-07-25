import os
import warnings
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import ttest_ind

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

all = df[['D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'YouTube_Index']]

Gen_sorted = all.sort_values(by=['Gender'], ascending=True)

group_bsmas_under = all[all['BSMAS'] < 14] #[column]
group_bsmas_over = all[all['BSMAS'] >= 14] #[column]

instagram_sorted_yes = all[all['Instagram_index'] == 1]
instagram_sorted_no = all[all['Instagram_index'] == 0]

facebook_sorted_yes = all[all['Facebook_index'] == 1]
facebook_sorted_no = all[all['Facebook_index'] == 0]

tiktok_sorted_yes = all[all['TikTok_index'] == 1]
tiktok_sorted_no = all[all['TikTok_index'] == 0]

Gen_sorted_df1 = Gen_sorted[Gen_sorted['Gender'] == 0]
Gen_sorted_final = Gen_sorted[Gen_sorted['Gender'] == 1]

YouTube_Sorted_df1 = all[all['YouTube_Index'] == 0]
YouTube_Sorted_final = all[all['YouTube_Index'] == 1]

t_val_arr = []
p_val_arr = []

print(group_bsmas_under.info)
print(group_bsmas_under['BSMAS'])
print(group_bsmas_over.info)
print(group_bsmas_over['BSMAS'])

for column in all.columns:

    t_val_bsmas, p_val_bsmas = stats.ttest_ind(group_bsmas_under[column], group_bsmas_over[column])
    t_val_gen, p_val_gen = stats.ttest_ind(Gen_sorted_df1[[column]], Gen_sorted_final[[column]], equal_var=True)
    t_val_bsmas, p_val_bsmas = stats.ttest_ind(instagram_sorted_no[[column]], instagram_sorted_yes[[column]])
    t_val_insta, p_val_insta = stats.ttest_ind(facebook_sorted_no[[column]], facebook_sorted_yes[[column]])
    t_val_fb, p_val_fb = stats.ttest_ind(tiktok_sorted_no[[column]], tiktok_sorted_yes[[column]])
    t_val_tiktok, p_val_tiktok = stats.ttest_ind(YouTube_Sorted_df1[[column]], YouTube_Sorted_final[[column]])

    # alpha = 0.05
    # df_gen = len(Gen_sorted_df1[[column]]) + len(Gen_sorted_final[[column]]) - 2
    # df_bsmas = 0
    # df_insta = 0
    # df_fb = 0
    # df_tiktok = 0
    print('T-test Result:')
    # crit_t = stats.t.ppf(1 - alpha / 2, df)
    #
    print("T-value of {} for separation of variable BSMAS".format(column), t_val_bsmas, p_val_bsmas)
    print("T-value of {} for separation of variable Gender:".format(column), t_val_gen)
    print("P-Value of {} for variable Gender:".format(column), p_val_gen)
    print("T-value of {} for separation of variable BSMAS:".format(column), t_val_bsmas)
    print("P-Value of {} for variable BSMAS:".format(column), p_val_bsmas)
    print("T-value of {} for separation of variable Instagram_Index:".format(column), t_val_insta)
    print("P-Value of {} for variable Instagram_Index:".format(column), p_val_insta)
    print("T-value of {} for separation of variable Facebook_Index:".format(column), t_val_fb)
    print("P-Value of {} for variable Facebook_Index:".format(column), p_val_fb)
    print("T-value of {} for separation of variable TikTok:".format(column), t_val_tiktok)
    print("P-Value of {} for variable TikTok:".format(column), p_val_tiktok)

    # print("Critical t-value:", crit_t)

    # print('T-test Result:')
    # if np.abs(t_val_gen) > crit_t:
    #     print('Significant difference found.')
    # else:
    #     print('No significant difference.')
    #
    # print('P-test Result:')
    # if p_val_gen > alpha:
    #     print('Fail to reject H0. No strong evidence of difference.')
    # else:
    #     print('Reject H0. Significant difference found.')
