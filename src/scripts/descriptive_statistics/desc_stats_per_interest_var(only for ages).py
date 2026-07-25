import numpy as np
import pandas as pd
import os
import warnings
from scipy import stats
from scipy.stats import mannwhitneyu
from pathlib import Path

warnings.filterwarnings('ignore')
#
# data = input('Please specify the Excel file with the data: ')

data = "/home/nopesferatu/Desktop/Thesis_R2_v2/analysis/data/o1_maybe_lates.xlsx"
# 1. -- Check if the file is of valid type, after that Pandas loads the data -- (you can add more file suffixes with an additional if statement and with filepaths = ['.xlsx', 'xlsm',])
if Path(data).suffix == '.xlsx':
    print('File received, proceeding...')
else:
    print('File is not of the form .xlsx, please input a valid file')
    os._exit()

df = pd.read_excel(data, sheet_name='INDIV_VAR_REG')

all = df[['D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
          'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
          'Instagram_index', 'Facebook_index', 'TikTok_index', 'YouTube_Index']]

# Gender separation 0 is for males, 1 is for females - the sorted is not necessary with this approach
BSMAS_Sorted_under14 = all[all['BSMAS'] < 14]
BSMAS_Sorted_over14 = all[all['BSMAS'] >= 14]


# # Define age group conditions and corresponding labels
# age_bins_under14 = {
#     "_1825": (BSMAS_Sorted_under14['Age_Group'] > 18) & (BSMAS_Sorted_under14['Age_Group'] <= 25),
#     "_2635": (BSMAS_Sorted_under14['Age_Group'] > 25) & (BSMAS_Sorted_under14['Age_Group'] <= 35),
#     "_3645": (BSMAS_Sorted_under14['Age_Group'] > 36) & (BSMAS_Sorted_under14['Age_Group'] <= 45),
#     "_4655": (BSMAS_Sorted_under14['Age_Group'] > 45) & (BSMAS_Sorted_under14['Age_Group'] <= 55),
#     "_5665": (BSMAS_Sorted_under14['Age_Group'] > 55) & (BSMAS_Sorted_under14['Age_Group'] <= 65),
#     "_6675": (BSMAS_Sorted_under14['Age_Group'] > 65) & (BSMAS_Sorted_under14['Age_Group'] <= 75),
#     "_7685": (BSMAS_Sorted_under14['Age_Group'] > 75) & (BSMAS_Sorted_under14['Age_Group'] <= 85),
#     "_86plus": (BSMAS_Sorted_under14['Age_Group'] > 85)
# }
#
# age_bins_over14 = {
#         "_1825": (BSMAS_Sorted_over14['Age_Group'] > 18) & (BSMAS_Sorted_over14['Age_Group'] <= 25),
#         "_2635": (BSMAS_Sorted_over14['Age_Group'] > 25) & (BSMAS_Sorted_over14['Age_Group'] <= 35),
#         "_3645": (BSMAS_Sorted_over14['Age_Group'] > 36) & (BSMAS_Sorted_over14['Age_Group'] <= 45),
#         "_4655": (BSMAS_Sorted_over14['Age_Group'] > 45) & (BSMAS_Sorted_over14['Age_Group'] <= 55),
#         "_5665": (BSMAS_Sorted_over14['Age_Group'] > 55) & (BSMAS_Sorted_over14['Age_Group'] <= 65),
#         "_6675": (BSMAS_Sorted_over14['Age_Group'] > 65) & (BSMAS_Sorted_over14['Age_Group'] <= 75),
#        "_7685": (BSMAS_Sorted_over14['Age_Group'] > 75) & (BSMAS_Sorted_over14['Age_Group'] <= 85),
#         "_86plus": (BSMAS_Sorted_over14['Age_Group'] > 85)
#
# }


empl_over14 = {
# Define masks for employment statuses
    "Student": BSMAS_Sorted_over14["Empl_st_st"] == 1,
    "Self-Employed": BSMAS_Sorted_over14["Empl_st_sfemp"] == 1,
    "Employee": BSMAS_Sorted_over14["Empl_st_employee"] == 1,
    "Other": BSMAS_Sorted_over14["Empl_st_oth"] == 1,
    "Unemployed": (
        (BSMAS_Sorted_over14["Empl_st_st"] == 0) &
        (BSMAS_Sorted_over14["Empl_st_sfemp"] == 0) &
        (BSMAS_Sorted_over14["Empl_st_employee"] == 0) &
        (BSMAS_Sorted_over14["Empl_st_oth"] == 0)
    )
}

empl_under14 = {
# Define masks for employment statuses
    "Student": BSMAS_Sorted_under14["Empl_st_st"] == 1,
    "Self-Employed": BSMAS_Sorted_under14["Empl_st_sfemp"] == 1,
    "Employee": BSMAS_Sorted_under14["Empl_st_employee"] == 1,
    "Other": BSMAS_Sorted_under14["Empl_st_oth"] == 1,
    "Unemployed": (
        (BSMAS_Sorted_under14["Empl_st_st"] == 0) &
        (BSMAS_Sorted_under14["Empl_st_sfemp"] == 0) &
        (BSMAS_Sorted_under14["Empl_st_employee"] == 0) &
        (BSMAS_Sorted_under14["Empl_st_oth"] == 0)
    )
}


# education_groups_Over14 = {
#     "None": (BSMAS_Sorted_over14["Education_L"] == 0) & (BSMAS_Sorted_over14["Education_P"] == 0) & (BSMAS_Sorted_over14["Education_Highest"] == 0),
#     "Primary": (BSMAS_Sorted_over14["Education_L"] == 1),
#     "Secondary": (BSMAS_Sorted_over14["Education_P"] == 1),
#     "Highest": (BSMAS_Sorted_over14["Education_Highest"] == 1)
# }
#
# education_groups_Under14 = {
#     "None": (BSMAS_Sorted_under14["Education_L"] == 0) & (BSMAS_Sorted_under14["Education_P"] == 0) & (BSMAS_Sorted_under14["Education_Highest"] == 0),
#     "Primary": (BSMAS_Sorted_under14["Education_L"] == 1),
#     "Secondary": (BSMAS_Sorted_under14["Education_P"] == 1),
#     "Highest": (BSMAS_Sorted_under14["Education_Highest"] == 1)
# }

Age_dict = {}

# arr_age_bins = [age_bins_under14, age_bins_over14]
names = ["BSMAS_UNDER_14", "BSMAS_OVER_14"]
# arr_age_bins = [education_groups_Under14, education_groups_Over14]
arr_age_bins = [empl_under14, empl_over14]
dataframes = [BSMAS_Sorted_under14, BSMAS_Sorted_over14]


for name, df_bins, df_source in zip(names, arr_age_bins, dataframes):
    for label, condition in df_bins.items():
        filtered_df = df_source.loc[condition]

        if filtered_df.empty:
            continue  # Skip if no data in this group
        # Compute descriptive stats for all numeric columns
        mean = filtered_df.mean(numeric_only=True)
        mode = filtered_df.mode(numeric_only=True).iloc[0] if not df.mode(numeric_only=True).empty else None
        std = filtered_df.std(numeric_only=True)

        # Store in dictionary
        Age_dict[label] = {
            'mean': mean,
            'mode': mode,
            'std': std
        }

        # Convert to DataFrame and export
        stats_df = pd.DataFrame({
            'mean': mean,
            'mode': mode,
            'std': std
        })
        stats_df.to_csv(f'desc_stats_per_education{label}_{name}.csv')

    # Optional: Combine all stats into one summary DataFrame
    resultsdf14 = pd.concat({
        label: pd.DataFrame(stats) for label, stats in Age_dict.items()
    }, names=['Age_Group', 'Statistic'])

    resultsdf14.to_csv('summary_stats_all_groups_employment{}_{}.csv'.format(label, names))
#
#
# # ----------- Employment Group Statistics -----------
#
# # Define masks for employment statuses
# empl_groups = {
#     "Student": all["Empl_st_st"] == 1,
#     "Self-Employed": all["Empl_st_sfemp"] == 1,
#     "Employee": all["Empl_st_employee"] == 1,
#     "Other": all["Empl_st_oth"] == 1,
#     "Unemployed": (
#         (all["Empl_st_st"] == 0) &
#         (all["Empl_st_sfemp"] == 0) &
#         (all["Empl_st_employee"] == 0) &
#         (all["Empl_st_oth"] == 0)
#     )
# }

# for group_name, mask in empl_groups.items():
#     df_group = all[mask]
#     if df_group.empty:
#         continue
#
#     mean = df_group.mean(numeric_only=True)
#     mode = df_group.mode(numeric_only=True)
#     mode_value = mode.iloc[0] if not mode.empty else None
#     std = df_group.std(numeric_only=True)
#
#     # Save individual CSV for each employment group
#     stats_df = pd.DataFrame({'mean': mean, 'mode': mode_value, 'std': std})
#     stats_df.to_csv(f'desc_stats_employment_{group_name}.csv')
#
# # Optional combined summary for employment
# combined_emp_df = pd.concat(
#     {group_name: pd.DataFrame({'mean': mean, 'mode': mode_value, 'std': std})
#      for group_name, (mask, mean, mode, std) in zip(empl_groups.keys(), [
#          (all[mask],
#           all[mask].mean(numeric_only=True),
#           all[mask].mode(numeric_only=True),
#           all[mask].std(numeric_only=True)
#          )
#          for mask in empl_groups.values()
#      ])},
#     names=['Employment_Status', 'Statistic']
# )
# combined_emp_df.to_csv('summary_stats_employment_all.csv')

# ---------------------- SEPARATION HERE -------------------------------




# # Define the education and employment indicator columns
# education_cols = ['Education_L', 'Education_P', 'Education_Highest']
# employment_cols = ['Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth']
#
# # ---------- Loop 1: Education ----------
# education_stats = {}
#
# df_edu = {
#     "None" : (all["Education_L"] == 0) & (all["Education_L"] == 0) & (all[all["Education_Highest" == 0]]) ,
#     "Primary": all["Education_L"] == 1,
#     "Secondary": all["Education_P"] == 1,
#     "Highest" : all["Education_Highest"] == 1
# }
#
#
# for col in education_cols:
#     # df_edu = all[all[col] == 1]  # Filter where this education level applies
#     #
#     # if df_edu.empty:
#     #     continue  # Skip if no data in this group
#
#     mean = df_edu.mean(numeric_only=True)
#     mode = df_edu.mode(numeric_only=True).iloc[0] if not df_edu.mode(numeric_only=True).empty else None
#     std = df_edu.std(numeric_only=True)
#
#     education_stats[col] = {
#         'mean': mean,
#         'mode': mode,
#         'std': std
#     }
#
#     # Save individual CSV for this education group
#     edu_stats_df = pd.DataFrame({
#         'mean': mean,
#         'mode': mode,
#         'std': std
#     })
#     edu_stats_df.to_csv(f'desc_stats_education_{col}.csv')
#
# # Optional combined summary
# combined_edu_df = pd.concat({
#     col: pd.DataFrame(stats) for col, stats in education_stats.items()
# }, names=['Education_Level', 'Statistic'])
#
# combined_edu_df.to_csv('summary_stats_education_all.csv')
#
#
# # ---------- Loop 2: Employment ----------
#
# employment_stats = {}
# #'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth'
# empl_cols= {
#     "Student" : (all[all["Empl_st_st"] == 1]),
#     "Self-Employed" : (all[all["Empl_st_sfemp"] == 1]),
#     "Employee" : (all[all["Empl_st_employee"] == 1]),
#     "Other" : (all[all["Empl_st_oth"] == 1]),
#     "Unemployed" : (all[all["Empl_st_st"] == 0]) & (all[all["Empl_st_sfemp"] == 0]) & (all[all["Empl_st_employee"] == 0]) & (all[all["Empl_st_oth"] == 0])
# }
#
# for col in employment_cols:
#
#     mean = empl_cols.mean(numeric_only=True)
#     mode = empl_cols.mode(numeric_only=True).iloc[0] if not all.mode(numeric_only=True).empty else None
#     std = empl_cols.std(numeric_only=True)
#
#     employment_stats[col] = {
#         'mean': mean,
#         'std': std,
#         'mode': mode
#     }
#
#     # Save individual CSV for this employment group
#     emp_stats_df = pd.DataFrame({
#         'mean': mean,
#         'std': std,
#         'mode': mode
#
#     })
#     emp_stats_df.to_csv(f'desc_stats_employment_{col}.csv')
#
# # Optional combined summary
# combined_emp_df = pd.concat({
#     col: pd.DataFrame(stats) for col, stats in employment_stats.items()
# }, names=['Employment_Status', 'Statistic'])
#
# combined_emp_df.to_csv('summary_stats_employment_all.csv')
#
# import pandas as pd
#
# # Assuming 'all', 'BSMAS_Sorted_under14', and 'age_bins' are predefined DataFrames/dictionaries
# # Example placeholders (replace with your actual data)
# # all = pd.DataFrame(...)
# # BSMAS_Sorted_under14 = pd.DataFrame(...)
# # age_bins = {'Young': condition1, 'Adult': condition2, ...}
#
# # ----------- Age Group Statistics -----------
# Age_dict = {}
#
# for label, condition in age_bins.items():
#     df = BSMAS_Sorted_under14.loc[condition]
#     if df.empty:
#         continue  # Skip if no data in this group
#
#     mean = df.mean(numeric_only=True)
#     mode = df.mode(numeric_only=True)
#     mode_value = mode.iloc[0] if not mode.empty else None
#     std = df.std(numeric_only=True)
#
#     Age_dict[label] = {
#         'mean': mean,
#         'mode': mode_value,
#         'std': std
#     }
#
# # Save combined age group stats
# resultsdf14 = pd.concat(
#     {label: pd.DataFrame(stats) for label, stats in Age_dict.items()},
#     names=['Age_Group', 'Statistic']
# )
# resultsdf14.to_csv('summary_stats_all_groups.csv')
#
#
# # ----------- Education Group Statistics -----------
#
# # Define masks for education levels
# education_groups = {
#     "None": (all["Education_L"] == 0) & (all["Education_P"] == 0) & (all["Education_Highest"] == 0),
#     "Primary": (all["Education_L"] == 1),
#     "Secondary": (all["Education_P"] == 1),
#     "Highest": (all["Education_Highest"] == 1)
# }
#
# for group_name, mask in education_groups.items():
#     df_group = all[mask]
#     if df_group.empty:
#         continue  # Skip empty groups
#
#     mean = df_group.mean(numeric_only=True)
#     mode = df_group.mode(numeric_only=True)
#     mode_value = mode.iloc[0] if not mode.empty else None
#     std = df_group.std(numeric_only=True)
#
#     # Save individual CSV for each education group
#     stats_df = pd.DataFrame({'mean': mean, 'mode': mode_value, 'std': std})
#     stats_df.to_csv(f'desc_stats_education_{group_name}.csv')
#
# # Optional combined summary for education
# combined_edu_df = pd.concat(
#     {group_name: pd.DataFrame({'mean': mean, 'mode': mode_value, 'std': std})
#      for group_name, (mask, mean, mode, std) in zip(education_groups.keys(), [
#          (all[mask],
#           all[mask].mean(numeric_only=True),
#           all[mask].mode(numeric_only=True),
#           all[mask].std(numeric_only=True)
#          )
#          for mask in education_groups.values()
#      ])},
#     names=['Education_Group', 'Statistic']
# )
# combined_edu_df.to_csv('summary_stats_education_all.csv')

# you_tube_gen_df1 = {}
# you_tube_gen_fin = {}
# # dict_gen = {}
# # dict_gen2 = {}
# # bsmas_gen = {}
# # bsmas_gen2 = {}
# # Qol_gen = {}
# # Qol_gen_2 = {}
# # Time_gen_M_df1 = {}
# # Time_gen_M_fin = {}
# # Time_gen_H = {}
# # Time_gen_H_fin = {}
# # face_gen = {}
# # face_gen_fin = {}
# # insta_gen = {}
# # insta_gen_fin = {}
# # results_mann_w = {}
# #
#
# for youtubecol in YouTube_Sorted_df1.columns:
#     mean = np.mean(YouTube_Sorted_df1[youtubecol])
#     mode = np.median(YouTube_Sorted_df1[youtubecol])
#     std = np.std(YouTube_Sorted_df1[youtubecol])
#     you_tube_gen_df1[youtubecol] = {
#         "Mean": mean,
#         "Mode": mode,
#         "STD": std
#     }
#
# for youtubecol in YouTube_Sorted_final.columns:
#     mean = np.mean(YouTube_Sorted_final[youtubecol])
#     mode = np.median(YouTube_Sorted_final[youtubecol])
#     std = np.std(YouTube_Sorted_final[youtubecol])
#     you_tube_gen_fin[youtubecol] = {
#         "Mean": mean,
#         "Mode": mode,
#         "STD": std
#     }
# # for gencol in Gen_sorted_df1.columns:
# #     mean = np.mean(Gen_sorted_df1[gencol])
# #     mode = np.median(Gen_sorted_df1[gencol])
# #     st_dev = np.std(Gen_sorted_df1[gencol])
# #     dict_gen[gencol] = {
# #         "Mean ": mean,
# #         "Mode ": mode,
# #         "STD ": st_dev
# #     }
# #
# # for gencol in Gen_sorted_final.columns:
# #     mean = np.mean(Gen_sorted_final[gencol])
# #     mode = np.median(Gen_sorted_final[gencol])
# #     st_dev = np.std(Gen_sorted_final[gencol])
# #     dict_gen2[gencol] = {
# #         "Mean ": mean,
# #         "Mode ": mode,
# #         "STD ": st_dev
# #     }
# #
# # for bsmascol in BSMAS_sorted_df1.columns:
# #     mean = np.mean(BSMAS_sorted_df1[bsmascol])
# #     mode = np.median(BSMAS_sorted_df1[bsmascol])
# #     st_dev = np.std(BSMAS_sorted_df1[bsmascol])
# #     bsmas_gen[bsmascol] = {
# #         "Mean ": mean,
# #         "Mode ": mode,
# #         "STD ": st_dev
# #     }
# #
# # for bsmascol in BSMAS_Sorted_final.columns:
# #     mean = np.mean(BSMAS_Sorted_final[bsmascol])
# #     mode = np.median(BSMAS_Sorted_final[bsmascol])
# #     st_dev = np.std(BSMAS_Sorted_final[bsmascol])
# #     bsmas_gen2[bsmascol] = {
# #         "Mean ": mean,
# #         "Mode ": mode,
# #         "STD ": st_dev
# #     }
# #
# # for timecol in Time_Sorted_M_df1.columns:
# #     mean = np.mean(Time_Sorted_M_df1[timecol])
# #     mode = np.median(Time_Sorted_M_df1[timecol])
# #     st_dev = np.std(Time_Sorted_M_df1[timecol])
# #     Time_gen_M_df1[timecol] = {
# #         "Mean ": mean,
# #         "Mode ": mode,
# #         "STD ": st_dev
# #     }
# #
# # for timecol in Time_Sorted_M_final.columns:
# #     mean = np.mean(Time_Sorted_M_final[timecol])
# #     mode = np.median(Time_Sorted_M_final[timecol])
# #     st_dev = np.std(Time_Sorted_M_final[timecol])
# #     Time_gen_M_fin[timecol] = {
# #         "Mean ": mean,
# #         "Mode ": mode,
# #         "STD ": st_dev
# #     }
# #
# # for timecol in Time_Sorted_H_df1.columns:
# #     mean = np.mean(Time_Sorted_H_df1[timecol])
# #     mode = np.median(Time_Sorted_H_df1[timecol])
# #     st_dev = np.std(Time_Sorted_H_df1[timecol])
# #     Time_gen_H[timecol] = {
# #         "Mean ": mean,
# #         "Mode ": mode,
# #         "STD ": st_dev
# #     }
# #
# # for timecol in Time_Sorted_H_final.columns:
# #     mean = np.mean(Time_Sorted_H_final[timecol])
# #     mode = np.median(Time_Sorted_H_final[timecol])
# #     st_dev = np.std(Time_Sorted_H_final[timecol])
# #     Time_gen_H_fin[timecol] = {
# #         "Mean ": mean,
# #         "Mode ": mode,
# #         "STD ": st_dev
# #     }
# #
# # for facecol in Facebook_Sorted_df1.columns:
# #     mean = np.mean(Facebook_Sorted_df1[facecol])
# #     mode = np.median(Facebook_Sorted_df1[facecol])
# #     st_dev = np.std(Facebook_Sorted_df1[facecol])
# #     face_gen[facecol] = {
# #         "Mean ": mean,
# #         "Mode ": mode,
# #         "STD ": st_dev
# #     }
# #
# # for facecol in Facebook_Sorted_Y.columns:
# #     mean = np.mean(Facebook_Sorted_Y[facecol])
# #     mode = np.median(Facebook_Sorted_Y[facecol])
# #     st_dev = np.std(Facebook_Sorted_Y[facecol])
# #     face_gen_fin[facecol] = {
# #         "Mean ": mean,
# #         "Mode ": mode,
# #         "STD ": st_dev
# #     }
# #
# # for instacol in Instagram_Sorted_df1.columns:
# #     mean = np.mean(Instagram_Sorted_df1[instacol])
# #     mode = np.median(Instagram_Sorted_df1[instacol])
# #     st_dev = np.std(Instagram_Sorted_df1[instacol])
# #     insta_gen[instacol] = {
# #         "Mean ": mean,
# #         "Mode ": mode,
# #         "STD ": st_dev
# #     }
# #
# # for instacol in Instagram_Sorted_Y.columns:
# #     mean = np.mean(Instagram_Sorted_Y[instacol])
# #     mode = np.median(Instagram_Sorted_Y[instacol])
# #     st_dev = np.std(Instagram_Sorted_Y[instacol])
# #     insta_gen_fin[instacol] = {
# #         "Mean ": mean,
# #         "Mode ": mode,
# #         "STD ": st_dev
# #     }
# #
# #
# # results_df1 = pd.DataFrame.from_dict(dict_gen, orient='index')
# # results_df1.to_csv('desc_stats_per_gend-Fem.csv')
# #
# # results_df2 = pd.DataFrame.from_dict(dict_gen2, orient='index')
# # results_df2.to_csv('desc_stats_per_gend-Mal.csv')
# #
# # results_df3 = pd.DataFrame.from_dict(bsmas_gen, orient='index')
# # results_df3.to_csv('desc_stats_per_bsmas<14Mal.csv')
# #
# # results_df4 = pd.DataFrame.from_dict(bsmas_gen2, orient='index')
# # results_df4.to_csv('desc_stats_per_bsmas>=14.csv')
# #
# # results_df5 = pd.DataFrame.from_dict(Time_gen_M_df1, orient='index')
# # results_df5.to_csv('desc_stats_per_time_mid_no.csv')
# #
# # results_df6 = pd.DataFrame.from_dict(Time_gen_M_fin, orient='index')
# # results_df6.to_csv('desc_stats_per_time_mid_yes.csv')
# #
# # results_df7 = pd.DataFrame.from_dict(Time_gen_H, orient='index')
# # results_df7.to_csv('desc_stats_per_time_high_no.csv')
# #
# # results_df8 = pd.DataFrame.from_dict(Time_gen_H_fin, orient='index')
# # results_df8.to_csv('desc_stats_per_time_high_yes.csv')
# #
# # results_df9 = pd.DataFrame.from_dict(face_gen, orient='index')
# # results_df9.to_csv('desc_stats_per_fb_no.csv')
# #
# # results_df10 = pd.DataFrame.from_dict(face_gen_fin, orient='index')
# # results_df10.to_csv('desc_stats_per_fb-yes.csv')
# #
# # results_df11 = pd.DataFrame.from_dict(insta_gen, orient='index')
# # results_df11.to_csv('desc_stats_per_insta_no.csv')
# #
# # results_df12 = pd.DataFrame.from_dict(insta_gen_fin, orient='index')
# # results_df12.to_csv('desc_stats_per_insta_yes.csv')
#
# resultsdf13 = pd.DataFrame.from_dict(you_tube_gen_df1, orient='index')
# resultsdf13.to_csv('desc_stats_per_yt_no.csv')
#
# resultsdf14 = pd.DataFrame.from_dict(you_tube_gen_fin, orient='index')
# resultsdf14.to_csv('desc_stats_per_yt_yes.csv')