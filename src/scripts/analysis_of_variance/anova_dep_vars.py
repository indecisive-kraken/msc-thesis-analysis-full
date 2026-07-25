# import os
# import numpy as np
# import pandas as pd
# import statsmodels.api as sm
# from scipy.stats import f_oneway
# from dotenv import load_dotenv
#
# def anova():
#
#     load_dotenv()
#     data = os.getenv("DATA")
#
#     df = pd.read_excel(data, sheet_name='INDIV_VAR_REG')
#
#     print(df.info())
#     df.head()
#
#     all = df[['D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
#             'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
#             'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'YouTube_Index']]
#
#     Age_Sorted = all.sort_values(by=['Age_Group'], ascending=True)
#
#
#     age_binsdf18_25 = all.loc[(all['Age_Group'] > 18) & (all['Age_Group'] <= 25)]
#
#     print(age_binsdf18_25.info)
#     print(age_bins["_1825"])
#
#     empl_groups = {
#         "Student": all["Empl_st_st"] == 1,
#         "Self-Employed": all["Empl_st_sfemp"] == 1,
#         "Employee": all["Empl_st_employee"] == 1,
#         "Other": all["Empl_st_oth"] == 1,
#         "Unemployed": (
#             (all["Empl_st_st"] == 0) &
#             (all["Empl_st_sfemp"] == 0) &
#             (all["Empl_st_employee"] == 0) &
#             (all["Empl_st_oth"] == 0)
#         )
#     }
#
#     education_groups = {
#         "None" : (all["Education_L"] == 0) & (all["Education_L"] == 0) & (all["Education_Highest"] == 0) ,
#         "Primary": all["Education_L"] == 1,
#         "Secondary": all["Education_P"] == 1,
#         "Highest" : all["Education_Highest"] == 1
#     }
#
#     time_g = {
#     "time_h_sorted" : all[all['Time_Spent_H'] == 1],
#     "time_m_sorted" : all[all['Time_Spent_M'] == 1],
#     "time_none_sorted" : all.loc[all['Time_Spent_H'] == 0, 'Time_Spent_M']
#     }
#
#     f_stat_age, p_value_age = f_oneway(age_bins["_1825"], age_bins["_2635"], age_bins["_3645"], age_bins["_4655"], age_bins["_5665"], age_bins["_6675"], age_bins["_7685"], age_bins["_86plus"])
#     f_stat_empl, p_value_empl = f_oneway(empl_groups["Student"], empl_groups["Self-Employed"], empl_groups["Employee"], empl_groups["Other"], empl_groups["Unemployed"])
#     f_stat_educ, p_val_educ = f_oneway(education_groups["None"], education_groups["Primary"], education_groups["Secondary"], education_groups["Highest"])
#     f_stat_time, p_val_time = f_oneway(time_g["time_h_sorted"], time_g["time_m_sorted"], time_g["time_none_sorted"])
#
#     print("F-Statistic: ", f_stat_age,"P-value",p_value_age)
#     print("F-Statistic: ", f_stat_empl, "P-value",p_value_empl)
#     print("F-Statistic: ", f_stat_educ, "P-value",p_val_educ)
#     print("F-Statistic: ", f_stat_time, "P-value",p_val_time)
#
#
#     #
#     # Your group lists
#     age_groups = [
#         all.loc[(all['Age_Group'] > 18) & (all['Age_Group'] <= 25)],
#         all.loc[(all['Age_Group'] > 25) & (all['Age_Group'] <= 35)],
#         all.loc[(all['Age_Group'] > 36) & (all['Age_Group'] <= 45)],
#         all.loc[(all['Age_Group'] > 45) & (all['Age_Group'] <= 55)],
#         all.loc[(all['Age_Group'] > 55) & (all['Age_Group'] <= 65)],
#         all.loc[(all['Age_Group'] > 65) & (all['Age_Group'] <= 75)],
#         all.loc[(all['Age_Group'] > 75) & (all['Age_Group'] <= 85)],
#         all.loc[all['Age_Group'] > 85]
#     ]
#
#     empl_groups = [
#         all.loc[all["Empl_st_st"] == 1],
#         all.loc[all["Empl_st_sfemp"] == 1],
#         all.loc[all["Empl_st_employee"] == 1],
#         all.loc[all["Empl_st_oth"] == 1],
#         all.loc[
#             (all["Empl_st_st"] == 0) &
#             (all["Empl_st_sfemp"] == 0) &
#             (all["Empl_st_employee"] == 0) &
#             (all["Empl_st_oth"] == 0)
#         ]
#     ]
#
#     education_groups = [
#         all.loc[
#             (all["Education_L"] == 0) &
#             (all["Education_P"] == 0) &
#             (all["Education_Highest"] == 0)
#         ],
#         all.loc[all["Education_L"] == 1],
#         all.loc[all["Education_P"] == 1],
#         all.loc[all["Education_Highest"] == 1]
#     ]
#
#     time_groups = [
#         all.loc[all['Time_Spent_H'] == 1],
#         all.loc[all['Time_Spent_M'] == 1],
#         all.loc[(all['Time_Spent_H'] == 0) & (all['Time_Spent_M'] == 0)]
#     ]
#
#     # Your varlist with the variable names to iterate over
#     varlist = ["D1", "D2", "D3", "D4", "BSMAS"]
#     grouplist = [age_groups, empl_groups, education_groups, time_groups]
#     namelist = ["age_groups", "empl_groups", "education_groups", "time_groups"]
#
#     for var in varlist:
#         for name ,group in zip(namelist, grouplist):
#             sample = [groupcol[var] for groupcol in group]
#             f_all, p_val_all = f_oneway(*sample)
#             print(f"{var}: F-statistic = {f_all:.4f}, P-value = {p_val_all:.4g}, group = {name}")
#
#
#
#
