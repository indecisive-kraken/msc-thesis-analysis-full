from scipy import stats

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

Gen_Sorted = all.sort_values(by=['Gender'], ascending=True)

group_bsmas_under = all[all['BSMAS'] < 14] #[column]
group_bsmas_over = all[all['BSMAS'] >= 14] #[column]

instagram_sorted_yes = all[all['Instagram_index'] == 1]
instagram_sorted_no = all[all['Instagram_index'] == 0]

facebook_sorted_yes = all[all['Facebook_index'] == 1]
facebook_sorted_no = all[all['Facebook_index'] == 0]

tiktok_sorted_yes = all[all['TikTok_index'] == 1]
tiktok_sorted_no = all[all['TikTok_index'] == 0]

Gen_sorted_df1 = Gen_Sorted[Gen_Sorted['Gender'] == 0]
Gen_sorted_final = Gen_Sorted[Gen_Sorted['Gender'] == 1]

YouTube_Sorted_df1 = all[all['YouTube_Index'] == 0]
YouTube_Sorted_final = all[all['YouTube_Index'] == 1]

time_h_sorted = all[all['Time_Spent_H'] == 1]
time_m_sorted = all[all['Time_Spent_M'] == 1]

time_h_sorted_no = all[all['Time_Spent_H'] == 0]
time_m_sorted_no = all[all['Time_Spent_M'] == 0]

t_val_arr = []
p_val_arr = []

for column in all.columns:

    t_val_gen, p_val_gen = stats.ttest_ind(Gen_sorted_df1[[column]], Gen_sorted_final[[column]], equal_var=True)
    t_val_bsmas, p_val_bsmas = stats.ttest_ind(group_bsmas_under[[column]], group_bsmas_over[[column]])
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


# Dataframe separations based on BSMAS, Gender, and other variables
GenSorted_BSMAS_Under14 = Gen_Sorted[Gen_Sorted['BSMAS'] < 14]
GenSorted_BSMAS_Over14 = Gen_Sorted[Gen_Sorted['BSMAS'] >= 14]

# Gender separations
Gen_sorted_df1_over14 = GenSorted_BSMAS_Over14[GenSorted_BSMAS_Over14['Gender'] == 0]  # Male
Gen_sorted_df1_under14 = GenSorted_BSMAS_Under14[GenSorted_BSMAS_Under14['Gender'] == 0]  # Male

Gen_sorted_final_over14 = GenSorted_BSMAS_Over14[GenSorted_BSMAS_Over14['Gender'] == 1]  # Female
Gen_sorted_final_under14 = GenSorted_BSMAS_Under14[GenSorted_BSMAS_Under14['Gender'] == 1]  # Female

# Instagram separations
instagram_sorted_yes_over14 = instagram_sorted_yes[instagram_sorted_yes['BSMAS'] >= 14]
instagram_sorted_yes_under14 = instagram_sorted_yes[instagram_sorted_yes['BSMAS'] < 14]
instagram_sorted_no_over14 = instagram_sorted_no[instagram_sorted_no['BSMAS'] >= 14]
instagram_sorted_no_under14 = instagram_sorted_no[instagram_sorted_no['BSMAS'] < 14]

# Facebook separations
facebook_sorted_yes_over14 = facebook_sorted_yes[facebook_sorted_yes['BSMAS'] >= 14]
facebook_sorted_yes_under14 = facebook_sorted_yes[facebook_sorted_yes['BSMAS'] < 14]
facebook_sorted_no_over14 = facebook_sorted_no[facebook_sorted_no['BSMAS'] >= 14]
facebook_sorted_no_under14 = facebook_sorted_no[facebook_sorted_no['BSMAS'] < 14]

# TikTok separations
tiktok_sorted_yes_over14 = tiktok_sorted_yes[tiktok_sorted_yes['BSMAS'] >= 14]
tiktok_sorted_yes_under14 = tiktok_sorted_yes[tiktok_sorted_yes['BSMAS'] < 14]
tiktok_sorted_no_over14 = tiktok_sorted_no[tiktok_sorted_no['BSMAS'] >= 14]
tiktok_sorted_no_under14 = tiktok_sorted_no[tiktok_sorted_no['BSMAS'] < 14]

# Time spent separations (High, Low, Medium)
time_h_sorted_over14 = time_h_sorted[time_h_sorted['BSMAS'] >= 14]
time_h_sorted_under14 = time_h_sorted[time_h_sorted['BSMAS'] < 14]
time_m_sorted_over14 = time_m_sorted[time_m_sorted['BSMAS'] >= 14]
time_m_sorted_under14 = time_m_sorted[time_m_sorted['BSMAS'] < 14]
time_h_sorted_no_over14 = time_h_sorted_no[time_h_sorted_no['BSMAS'] >= 14]
time_h_sorted_no_under14 = time_h_sorted_no[time_h_sorted_no['BSMAS'] < 14]

# BSMAS Separations

# Loop through all columns and perform T-tests for each variable with BSMAS group and cross-group comparisons
for column in all.columns:
    print(f"\nT-tests for {column}:")

    # T-test for BSMAS >= 14 vs < 14
    t_val_bsmas, p_val_bsmas = stats.ttest_ind(GenSorted_BSMAS_Over14[[column]], GenSorted_BSMAS_Under14[[column]],
                                               equal_var=True)
    print(f"T-test for {column} (BSMAS >= 14 vs BSMAS < 14): t-value = {t_val_bsmas}, p-value = {p_val_bsmas}")

    # T-test for Male (BSMAS >= 14 vs < 14)
    t_val_male_over14, p_val_male_over14 = stats.ttest_ind(Gen_sorted_df1_over14[[column]],
                                                           Gen_sorted_df1_under14[[column]], equal_var=True)
    print(f"T-test for Male (BSMAS >= 14 vs < 14): t-value = {t_val_male_over14}, p-value = {p_val_male_over14}")

    # T-test for Female (BSMAS >= 14 vs < 14)
    t_val_female_over14, p_val_female_over14 = stats.ttest_ind(Gen_sorted_final_over14[[column]],
                                                               Gen_sorted_final_under14[[column]], equal_var=True)
    print(f"T-test for Female (BSMAS >= 14 vs < 14): t-value = {t_val_female_over14}, p-value = {p_val_female_over14}")

    # Cross-group T-tests for Gender (Male vs Female) and BSMAS (>= 14 vs < 14)

    # Male and BSMAS >= 14 vs Female and BSMAS >= 14
    t_val_male_female_over14, p_val_male_female_over14 = stats.ttest_ind(Gen_sorted_df1_over14[[column]],
                                                                         Gen_sorted_final_over14[[column]],
                                                                         equal_var=True)
    print(
        f"T-test for Male BSMAS >= 14 vs Female BSMAS >= 14: t-value = {t_val_male_female_over14} p-value = {p_val_male_female_over14}")

    # Male and BSMAS < 14 vs Female and BSMAS < 14
    t_val_male_female_under14, p_val_male_female_under14 = stats.ttest_ind(Gen_sorted_df1_under14[[column]],
                                                                           Gen_sorted_final_under14[[column]],
                                                                           equal_var=True)
    print(
        f"T-test for Male BSMAS < 14 vs Female BSMAS < 14: t-value = {t_val_male_female_under14}, p-value = {p_val_male_female_under14}")

    # Instagram Usage (Yes vs No) and BSMAS (>= 14 vs < 14)

    # Instagram Yes (BSMAS >= 14 vs < 14)
    t_val_insta_over14, p_val_insta_over14 = stats.ttest_ind(instagram_sorted_yes_over14[[column]],
                                                             instagram_sorted_yes_under14[[column]], equal_var=True)
    print(
        f"T-test for Instagram Yes (BSMAS >= 14 vs < 14): t-value = {t_val_insta_over14}, p-value = {p_val_insta_over14}")

    # Instagram No (BSMAS >= 14 vs < 14)
    t_val_insta_no_over14, p_val_insta_no_over14 = stats.ttest_ind(instagram_sorted_no_over14[[column]],
                                                                   instagram_sorted_no_under14[[column]],
                                                                   equal_var=True)
    print(
        f"T-test for Instagram No (BSMAS >= 14 vs < 14): t-value = {t_val_insta_no_over14}, p-value = {p_val_insta_no_over14}")

    # Facebook Usage (Yes vs No) and BSMAS (>= 14 vs < 14)

    # Facebook Yes (BSMAS >= 14 vs < 14)
    t_val_fb_over14, p_val_fb_over14 = stats.ttest_ind(facebook_sorted_yes_over14[[column]],
                                                       facebook_sorted_yes_under14[[column]], equal_var=True)
    print(f"T-test for Facebook Yes (BSMAS >= 14 vs < 14): t-value = {t_val_fb_over14}, p-value = {p_val_fb_over14}")

    # Facebook No (BSMAS >= 14 vs < 14)
    t_val_fb_no_over14, p_val_fb_no_over14 = stats.ttest_ind(facebook_sorted_no_over14[[column]],
                                                             facebook_sorted_no_under14[[column]], equal_var=True)
    print(
        f"T-test for Facebook No (BSMAS >= 14 vs < 14): t-value = {t_val_fb_no_over14}, p-value = {p_val_fb_no_over14}")

    # TikTok Usage (Yes vs No) and BSMAS (>= 14 vs < 14)

    # TikTok Yes (BSMAS >= 14 vs < 14)
    t_val_tiktok_over14, p_val_tiktok_over14 = stats.ttest_ind(tiktok_sorted_yes_over14[[column]],
                                                               tiktok_sorted_yes_under14[[column]], equal_var=True)
    print(
        f"T-test for TikTok Yes (BSMAS >= 14 vs < 14): t-value = {t_val_tiktok_over14}, p-value = {p_val_tiktok_over14}")

    # TikTok No (BSMAS >= 14 vs < 14)
    t_val_tiktok_no_over14, p_val_tiktok_no_over14 = stats.ttest_ind(tiktok_sorted_no_over14[[column]],
                                                                     tiktok_sorted_no_under14[[column]], equal_var=True)
    print(
        f"T-test for TikTok No (BSMAS >= 14 vs < 14): t-value = {t_val_tiktok_no_over14}, p-value = {p_val_tiktok_no_over14}")

    # Time Spent (High vs Low) and BSMAS (>= 14 vs < 14)

    # Time Spent High (BSMAS >= 14 vs < 14)
    t_val_time_h_over14, p_val_time_h_over14 = stats.ttest_ind(time_h_sorted_over14[[column]],
                                                               time_h_sorted_under14[[column]], equal_var=True)
    print(
        f"T-test for Time Spent High (BSMAS >= 14 vs < 14): t-value = {t_val_time_h_over14}, p-value = {p_val_time_h_over14}")

    # Time Spent Low (BSMAS >= 14 vs < 14)
    t_val_time_h_low_over14, p_val_time_h_low_over14 = stats.ttest_ind(time_h_sorted_no_over14[[column]],
                                                                       time_h_sorted_no_under14[[column]],
                                                                       equal_var=True)
    print(
        f"T-test for Time Spent Low (BSMAS >= 14 vs < 14): t-value = {t_val_time_h_low_over14}, p-value = {p_val_time_h_low_over14}")

    # Time Spent Medium (BSMAS >= 14 vs < 14)
    t_val_time_m_over14, p_val_time_m_over14 = stats.ttest_ind(time_m_sorted_over14[[column]],
                                                               time_m_sorted_under14[[column]], equal_var=True)
    print(
        f"T-test for Time Spent Medium (BSMAS >= 14 vs < 14): t-value = {t_val_time_m_over14}, p-value = {p_val_time_m_over14}")


# Columns to compute stats for (exclude non-numeric or group-identifying columns if needed)
numeric_columns = all.select_dtypes(include='number').columns.tolist()

# # Conditions for subgroups
# conditions = {
#     "Gender_0_BSMAS_Over14": (all['Gender'] == 0) & (all['BSMAS'] >= 14),
#     "Gender_0_BSMAS_Under14": (all['Gender'] == 0) & (all['BSMAS'] < 14),
#     "Gender_1_BSMAS_Over14": (all['Gender'] == 1) & (all['BSMAS'] >= 14),
#     "Gender_1_BSMAS_Under14": (all['Gender'] == 1) & (all['BSMAS'] < 14),
#
#     "Instagram_1_BSMAS_Over14": (all['Instagram_index'] == 1) & (all['BSMAS'] >= 14),
#     "Instagram_1_BSMAS_Under14": (all['Instagram_index'] == 1) & (all['BSMAS'] < 14),
#     "Instagram_0_BSMAS_Over14": (all['Instagram_index'] == 0) & (all['BSMAS'] >= 14),
#     "Instagram_0_BSMAS_Under14": (all['Instagram_index'] == 0) & (all['BSMAS'] < 14),
#
#     "Facebook_1_BSMAS_Over14": (all['Facebook_index'] == 1) & (all['BSMAS'] >= 14),
#     "Facebook_1_BSMAS_Under14": (all['Facebook_index'] == 1) & (all['BSMAS'] < 14),
#     "Facebook_0_BSMAS_Over14": (all['Facebook_index'] == 0) & (all['BSMAS'] >= 14),
#     "Facebook_0_BSMAS_Under14": (all['Facebook_index'] == 0) & (all['BSMAS'] < 14),
#
#     "TikTok_1_BSMAS_Over14": (all['TikTok_index'] == 1) & (all['BSMAS'] >= 14),
#     "TikTok_1_BSMAS_Under14": (all['TikTok_index'] == 1) & (all['BSMAS'] < 14),
#     "TikTok_0_BSMAS_Over14": (all['TikTok_index'] == 0) & (all['BSMAS'] >= 14),
#     "TikTok_0_BSMAS_Under14": (all['TikTok_index'] == 0) & (all['BSMAS'] < 14),
#
#     "YouTube_1_BSMAS_Over14": (all['YouTube_Index'] == 1) & (all['BSMAS'] >= 14),
#     "YouTube_1_BSMAS_Under14": (all['YouTube_Index'] == 1) & (all['BSMAS'] < 14),
#     "YouTube_0_BSMAS_Over14": (all['YouTube_Index'] == 0) & (all['BSMAS'] >= 14),
#     "YouTube_0_BSMAS_Under14": (all['YouTube_Index'] == 0) & (all['BSMAS'] < 14),
#
#     "Time_High_BSMAS_Over14": (all['Time_Spent_H'] == 1) & (all['BSMAS'] >= 14),
#     "Time_High_BSMAS_Under14": (all['Time_Spent_H'] == 1) & (all['BSMAS'] < 14),
#     "Time_Medium_BSMAS_Over14": (all['Time_Spent_M'] == 1) & (all['BSMAS'] >= 14),
#     "Time_Medium_BSMAS_Under14": (all['Time_Spent_M'] == 1) & (all['BSMAS'] < 14),
# }
#
# # Storage for results
#
# summary_stats = []
#
# # Compute statistics for each group
# for name, condition in conditions.items():
#     group_data = all[condition]
#     if group_data.empty:
#         print(f"Skipping {name} (empty group)")
#         continue
#     for col in numeric_columns:
#         mean_val = group_data[col].mean()
#         median_val = group_data[col].median()
#         std_val = group_data[col].std()
#
#         summary_stats.append({
#             "Group": name,
#             "Variable": col,
#             "Mean": mean_val,
#             "Median": median_val,
#             "Std": std_val,
#             "Count": group_data[col].count()
#         })
#
# # Convert to DataFrame
# summary_df = pd.DataFrame(summary_stats)
#
# # Optional: Save to CSV
# summary_df.to_csv("grouped_summary_stats.csv", index=False)
#
# # Print sample
# print(summary_df.head(10))
