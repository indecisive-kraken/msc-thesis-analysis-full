import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pingouin import multivariate_normality
from scipy import stats
from scipy.stats import mannwhitneyu
from statsmodels.stats.multitest import multipletests
from patsy import dmatrices
from pathlib import Path

from statistic_models.DescriptiveStats.desc_stats_per_interest_var import YouTube_Sorted

data = input('Please specify the Excel file with the data: ')
df = pd.read_excel(data, sheet_name='ENCODED_DATA')

print(df.info())
df.head()

all = df[['D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'YouTube_Index']]

#
# all = df[['Q1','Q2', 'Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','BSMAS1','BSMAS2','BSMAS3','BSMAS4','BSMAS5','BSMAS6','Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
#         'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
#         'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N', 'BSMAS']]


results_mann_w_gend = {}
results_mann_w_bsmas = {}
results_mann_w_facebook = {}
results_mann_w_tiktok = {}
results_mann_w_instagram = {}
results_mann_w_youtube = {}

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

print(group_bsmas_under.info)
print(group_bsmas_over.info)

for column in all.columns:

    # Gen_sorted = pd.DataFrame(Gen_sorted.col.str.split('1', n=1).tolist(), columns = [col for col in Gen_sorted.columns])

    statistic, p_value = mannwhitneyu(Gen_sorted_df1[[column]], Gen_sorted_final[[column]], alternative='two-sided')
    statistic_bsmas, p_value_bsmas = mannwhitneyu(group_bsmas_under[[column]],group_bsmas_over[[column]], alternative='two-sided')
    statistic_instagram, p_value_insta = mannwhitneyu(instagram_sorted_yes[column], instagram_sorted_no[column], alternative='two-sided')
    statistic_facebook, p_value_facebook = mannwhitneyu(facebook_sorted_yes[column], facebook_sorted_no[column], alternative='two-sided')
    statistic_tiktok, p_values_tiktok = mannwhitneyu(tiktok_sorted_yes[column], tiktok_sorted_no[column], alternative='two-sided')
    statistic_youtube, p_values_youtube = mannwhitneyu(YouTube_Sorted_df1[column], YouTube_Sorted_final[column], alternative='two-sided')


    results_mann_w_bsmas[column] = {
        'Mann-Whitney U Statistic': statistic_bsmas,
        'P-Value' : p_value_bsmas

    }
    results_mann_w_gend[column] = {
        'Mann-Whitney U Statistic': statistic,
        'P-Value' : p_value
    }

    results_mann_w_facebook[column] = {
        'Mann-Whitney U Statistic': statistic_facebook,
        'P-Value': p_value_facebook

    }

    results_mann_w_tiktok[column] = {
        'Mann-Whitney U Statistic': statistic_tiktok,
        'P-Value': p_values_tiktok

    }

    results_mann_w_instagram[column] = {
        'Mann-Whitney U Statistic': statistic_instagram,
        'P-Value': p_value_insta

    }

    results_mann_w_youtube[column] = {
        'Mann-Whitney U Statistic': statistic_youtube,
        'P-Value': p_values_youtube
    }

    results_df = pd.DataFrame.from_dict(results_mann_w_gend, orient='index')
    results_df_bsmas = pd.DataFrame.from_dict(results_mann_w_bsmas, orient='index')
    results_df_f = pd.DataFrame.from_dict(results_mann_w_facebook, orient='index')
    results_df_in = pd.DataFrame.from_dict(results_mann_w_instagram, orient='index')
    results_df_tik = pd.DataFrame.from_dict(results_mann_w_tiktok, orient='index')
    results_df_yt = pd.DataFrame.from_dict(results_mann_w_youtube, orient='index')

    results_df_bsmas.to_csv('mwres_bsmas.csv')
    results_df.to_csv('mannwhitney_results_gender_vars_2nd_try.csv')
    results_df_f.to_csv("mwresfb.csv")
    results_df_in.to_csv("mwrin.csv")
    results_df_tik.to_csv("mwrtik.csv")
    results_df_yt.to_csv('yt.csv')

    # print(results_df)

# p_values = [v['P-Value'] for v in results_mann_w_gend.values()]
# corrected = multipletests(p_values, method='bonferroni')
#
# print(corrected)

'''
if np.mean(df[column]) / len(df[column]) == 

for column in all.columns:
    #add the frequency function or a summation approach because the sum in my case is always going to be smaller or equal to 111 in the 0-1 case 
'''