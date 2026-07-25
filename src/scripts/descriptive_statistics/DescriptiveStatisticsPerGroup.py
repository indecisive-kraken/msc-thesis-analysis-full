# import os
# import re
# import warnings
# import numpy as np
# import pandas as pd
# from pathlib import Path
#
# #1. -- Check if the file is of valid type, after that Pandas loads the data -- (you can add more file suffixes with an additional if statement and with filepaths = ['.xlsx', 'xlsm',])
# if Path(data).suffix == '.xlsx':
#     print('File received, proceeding...')
# else:
#     print('File is not of the form .xlsx, please input a valid file')
#     os._exit()
#
# df = pd.read_excel(data, sheet_name='ENCODED_DATA')
#
# # all = df[['Q1','Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
# #         'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
# #         'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]
#
# # all = df[['Q1','Q2', 'Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','BSMAS1','BSMAS2','BSMAS3','BSMAS4','BSMAS5','BSMAS6','Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
# #         'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
# #         'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N', 'BSMAS']]
#
#
# all = df[['Q1','Q2', 'Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','BSMAS1','BSMAS2','BSMAS3','BSMAS4','BSMAS5','BSMAS6']]
#
#
# BSMAS_Sorted = all.sort_values(by=['BSMAS'], ascending=True)
# BSMAS_Sorted = BSMAS_Sorted.astype(float)
#
# grouping1 = BSMAS_Sorted[BSMAS_Sorted['BSMAS'] < 14]    #grouping1
# grouping2 = BSMAS_Sorted[BSMAS_Sorted['BSMAS'] >= 14]   #grouping2
#
# for col1 in grouping1:
#     grouping1[col1 + '{Group1}'] = grouping1[[col1]]
#     del grouping1[col1]
#
# for col3 in grouping2:
#     grouping2[col3 + '{Group2}'] = grouping2[[col3]]
#     del grouping2[col3]
#
# all_data = pd.concat([grouping1_sub1_drop.reset_index(drop=True), grouping1_sub2_drop.reset_index(drop=True), grouping2.reset_index(drop=True)], axis=1, ignore_index=False)
#
# bsmas_group1_all = grouping1
# bsmas_group2_all = grouping2
#
# print(bsmas_group1_all)
# print(bsmas_group2_all)
# print(bsmas_group1_all.info())
# print(bsmas_group2_all.info())
#
# dictGroups = {}
# dictGroups2 ={}
#
# for column in all.columns:
#     mean = np.mean(all[column])
#     mode = np.median(all[column])
#     variance = np.var(all[column])
#
#     dictGroups[column] = {
#         "Mean of {str(column)}" : mean,
#         "Mode of {str(column)}" : mode,
#         "Variance of {str(column)}" : variance
#             }
#     results_df = pd.DataFrame.from_dict(dictGroups, orient='index')
#     results_df.to_csv('desc_stats_results_all_individual_questions.csv')
#
# for column in bsmas_group2_all.columns:
#
#     mean = np.mean(bsmas_group2_all[column])
#     mode = np.median(bsmas_group2_all[column])
#     variance = np.var(bsmas_group2_all[column])
#     dictGroups2[column] = {
#         "Mean ": mean,
#         "Mode " : mode,
#         "Variance ": variance
#             }
#
#     results_df2 = pd.DataFrame.from_dict(dictGroups2, orient='index')
#     results_df2.to_csv('desc_stats_results_per_groupBSMAS>=14_all_vars.csv')
#
#
#
#
#
#
#
