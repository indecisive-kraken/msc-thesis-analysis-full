# import os
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import statsmodels.api as sm
# import statsmodels.formula.api as smf
# import statsmodels.stats.api as sms
# from statsmodels.compat import lzip
# from scipy.stats import shapiro, jarque_bera
# from scipy.stats import skew, kurtosis
# from statsmodels.formula.api import ols
# from statsmodels.stats.stattools import omni_normtest
# from statsmodels.stats.stattools import durbin_watson
# from statsmodels.stats.outliers_influence import variance_inflation_factor
# from scipy import stats
# from scipy.stats import spearmanr
# from statsmodels.stats.outliers_influence import OLSInfluence
# from patsy import dmatrices
# from dotenv import load_dotenv
#
# load_dotenv()
# data = os.getenv("DATA")
#
# data = "/home/nopesferatu/Desktop/Thesis_R2_v2/analysis/data/o1_maybe_lates.xlsx"
# df = pd.read_excel(data, sheet_name='INDIV_VAR_REG')
#
# print(df.info())
# df.head()
#
# y = df[['D1']]
# x = df[['D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
#           'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
#           'Instagram_index', 'Facebook_index', 'TikTok_index', 'YouTube_Index']]
#
# # can be added - 'Education_Label','AgeLabel', 'TimeLabel', 'BSMAS_CAT'
#
# new_df = pd.DataFrame()
# new_df["AgeLabel"] = np.nan
# new_df["TimeLabel"] = np.nan
# new_df["Education_Label"] = np.nan
# new_df["EmplLabel"] = np.nan
#
# for i, ages in enumerate(x["Age_Group"].values):
#     if ages > 18 and ages <=25 : new_df.loc[i, 'AgeLabel'] = "18_25"
#     elif ages > 25 and ages <=35 : new_df.loc[i, 'AgeLabel'] = "26_35"
#     elif ages > 35 and ages <=45 : new_df.loc[i,'AgeLabel'] = "36_45"
#     elif ages > 45 and ages <=55 : new_df.loc[i, 'AgeLabel'] = "46_55"
#     elif ages > 55 and ages <= 65 : new_df.loc[i, 'AgeLabel'] = "56_65"
#     elif ages > 65 and ages <= 75: new_df.loc[i, 'AgeLabel'] = "66_75"
#     elif ages > 76 and ages <= 85: new_df.loc[i, 'AgeLabel'] = "76_85"
#     else: new_df.loc[i, 'AgeLabel'] = "86+"
#
# new_df.to_csv("Labeling_of_ages.csv")
#
#
# for i, time in enumerate(zip(x["Time_Spent_H"].values, x["Time_Spent_M"].values)):
#     if time == (0, 1):
#         new_df.loc[i, 'TimeLabel'] = "2_to_5h"
#     elif time == (1, 0):
#         new_df.loc[i, 'TimeLabel'] = "5+h"
#     elif time == (0, 0):
#         new_df.loc[i, 'TimeLabel'] = "less_than_2"
#     else:
#         print("Error something went wrong")
#
# for i, educ in enumerate(zip(x["Education_L"].values, x["Education_P"].values, x["Education_Highest"].values)):
#     if educ == (1, 0, 0):
#         new_df.loc[i, 'Education_Label'] = "Lower"
#     elif educ == (0, 1, 0):
#         new_df.loc[i, 'Education_Label'] = "Secondary"
#     elif educ == (0, 0, 1):
#         new_df.loc[i, 'Education_Label'] = "Highest"
#     elif educ == (0, 0, 0):
#         new_df.loc[i, 'Education_Label'] = "Lowest"
#
# # - 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth'
#
# for i, empl in enumerate(zip(x['Empl_st_st'].values, x['Empl_st_sfemp'].values, x['Empl_st_employee'].values, x["Empl_st_oth"].values)):
#     if empl == (1, 0, 0, 0):
#         new_df.loc[i, 'EmplLabel'] = "Student"
#     elif empl == (0, 1, 0, 0):
#         new_df.loc[i, 'EmplLabel'] = "Self-Employed"
#     elif empl == (0, 0, 1, 0):
#         new_df.loc[i, 'EmplLabel'] = "Employee"
#     elif empl == (0, 0, 0, 1):
#         new_df.loc[i, 'EmplLabel'] = "Other"
#     elif empl == (0, 0, 0, 0):
#         new_df.loc[i, 'EmplLabel'] = "Unemployed"
#
#
# new_df.to_csv("Labeling_for_ANOVA_twoway.csv")
#
# # x["AgeLabel"] = pd.cut(
# #     x["Age_Group"],
# #     bins=[18, 25, 35, 45, 55, 65, 75, 85, np.inf],
# #     labels=["18_25", "26_35", "36_45", "46_55", "56_65", "66_75", "76_85", "86+"],
# #     right=True  # Includes upper bound
# # )
