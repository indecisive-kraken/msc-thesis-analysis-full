import numpy as np
import pandas as pd
import os
import warnings
from scipy import stats
from scipy.stats import mannwhitneyu
from pathlib import Path
from dotenv import load_dotenv

warnings.filterwarnings('ignore')
load_dotenv()
data = os.getenv("DATA")

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
YouTube_Sorted = all.sort_values(by=['YouTube_Index'], ascending=True)
Gen_sorted = all.sort_values(by=['Gender'], ascending=True)
BSMAS_Sorted = all.sort_values(by=['BSMAS'], ascending=True)
Time_Sorted_M = all.sort_values(by=['Time_Spent_M'], ascending=True)
Time_Sorted_H = all.sort_values(by=['Time_Spent_H'], ascending=True)
Instagram_Sorted = all.sort_values(by=['Facebook_index'], ascending=True)
Facebook_Sorted = all.sort_values(by=['Instagram_index'], ascending=True)

# Gen_sorted = pd.DataFrame(Gen_sorted.col.str.split('1', n=1).tolist(), columns = [col for col in Gen_sorted.columns])

YouTube_Sorted_df1 = YouTube_Sorted[YouTube_Sorted['YouTube_Index'] == 0]
YouTube_Sorted_final = YouTube_Sorted[YouTube_Sorted['YouTube_Index'] == 1]

# Gen_sorted_df1 = Gen_sorted[Gen_sorted['Gender'] == 0]
# Gen_sorted_final = Gen_sorted[Gen_sorted['Gender'] == 1]
#
# BSMAS_sorted_df1 = BSMAS_Sorted[BSMAS_Sorted['BSMAS'] < 14]
# BSMAS_Sorted_final = BSMAS_Sorted[BSMAS_Sorted['BSMAS'] >= 14]
#
# Time_Sorted_M_df1 = Time_Sorted_M[Time_Sorted_M['Time_Spent_M'] == 0]
# Time_Sorted_M_final = Time_Sorted_M[Time_Sorted_M['Time_Spent_M'] == 1]
#
# Time_Sorted_H_df1 = Time_Sorted_H[Time_Sorted_H['Time_Spent_H'] == 0]
# Time_Sorted_H_final = Time_Sorted_H[Time_Sorted_H['Time_Spent_H'] == 1]
#
# Instagram_Sorted_df1 = Instagram_Sorted[Instagram_Sorted['Instagram_index'] == 0]
# Instagram_Sorted_Y = Instagram_Sorted[Instagram_Sorted['Instagram_index'] == 1]
#
# Facebook_Sorted_df1 = Facebook_Sorted[Facebook_Sorted['Facebook_index'] == 0]
# Facebook_Sorted_Y = Facebook_Sorted[Facebook_Sorted['Facebook_index'] == 1]
#
you_tube_gen_df1 = {}
you_tube_gen_fin = {}
# dict_gen = {}
# dict_gen2 = {}
# bsmas_gen = {}
# bsmas_gen2 = {}
# Qol_gen = {}
# Qol_gen_2 = {}
# Time_gen_M_df1 = {}
# Time_gen_M_fin = {}
# Time_gen_H = {}
# Time_gen_H_fin = {}
# face_gen = {}
# face_gen_fin = {}
# insta_gen = {}
# insta_gen_fin = {}
# results_mann_w = {}
#

for youtubecol in YouTube_Sorted_df1.columns:
    mean = np.mean(YouTube_Sorted_df1[youtubecol])
    mode = np.median(YouTube_Sorted_df1[youtubecol])
    std = np.std(YouTube_Sorted_df1[youtubecol])
    you_tube_gen_df1[youtubecol] = {
        "Mean": mean,
        "Mode": mode,
        "STD": std
    }

for youtubecol in YouTube_Sorted_final.columns:
    mean = np.mean(YouTube_Sorted_final[youtubecol])
    mode = np.median(YouTube_Sorted_final[youtubecol])
    std = np.std(YouTube_Sorted_final[youtubecol])
    you_tube_gen_fin[youtubecol] = {
        "Mean": mean,
        "Mode": mode,
        "STD": std
    }
# for gencol in Gen_sorted_df1.columns:
#     mean = np.mean(Gen_sorted_df1[gencol])
#     mode = np.median(Gen_sorted_df1[gencol])
#     st_dev = np.std(Gen_sorted_df1[gencol])
#     dict_gen[gencol] = {
#         "Mean ": mean,
#         "Mode ": mode,
#         "STD ": st_dev
#     }
#
# for gencol in Gen_sorted_final.columns:
#     mean = np.mean(Gen_sorted_final[gencol])
#     mode = np.median(Gen_sorted_final[gencol])
#     st_dev = np.std(Gen_sorted_final[gencol])
#     dict_gen2[gencol] = {
#         "Mean ": mean,
#         "Mode ": mode,
#         "STD ": st_dev
#     }
#
# for bsmascol in BSMAS_sorted_df1.columns:
#     mean = np.mean(BSMAS_sorted_df1[bsmascol])
#     mode = np.median(BSMAS_sorted_df1[bsmascol])
#     st_dev = np.std(BSMAS_sorted_df1[bsmascol])
#     bsmas_gen[bsmascol] = {
#         "Mean ": mean,
#         "Mode ": mode,
#         "STD ": st_dev
#     }
#
# for bsmascol in BSMAS_Sorted_final.columns:
#     mean = np.mean(BSMAS_Sorted_final[bsmascol])
#     mode = np.median(BSMAS_Sorted_final[bsmascol])
#     st_dev = np.std(BSMAS_Sorted_final[bsmascol])
#     bsmas_gen2[bsmascol] = {
#         "Mean ": mean,
#         "Mode ": mode,
#         "STD ": st_dev
#     }
#
# for timecol in Time_Sorted_M_df1.columns:
#     mean = np.mean(Time_Sorted_M_df1[timecol])
#     mode = np.median(Time_Sorted_M_df1[timecol])
#     st_dev = np.std(Time_Sorted_M_df1[timecol])
#     Time_gen_M_df1[timecol] = {
#         "Mean ": mean,
#         "Mode ": mode,
#         "STD ": st_dev
#     }
#
# for timecol in Time_Sorted_M_final.columns:
#     mean = np.mean(Time_Sorted_M_final[timecol])
#     mode = np.median(Time_Sorted_M_final[timecol])
#     st_dev = np.std(Time_Sorted_M_final[timecol])
#     Time_gen_M_fin[timecol] = {
#         "Mean ": mean,
#         "Mode ": mode,
#         "STD ": st_dev
#     }
#
# for timecol in Time_Sorted_H_df1.columns:
#     mean = np.mean(Time_Sorted_H_df1[timecol])
#     mode = np.median(Time_Sorted_H_df1[timecol])
#     st_dev = np.std(Time_Sorted_H_df1[timecol])
#     Time_gen_H[timecol] = {
#         "Mean ": mean,
#         "Mode ": mode,
#         "STD ": st_dev
#     }
#
# for timecol in Time_Sorted_H_final.columns:
#     mean = np.mean(Time_Sorted_H_final[timecol])
#     mode = np.median(Time_Sorted_H_final[timecol])
#     st_dev = np.std(Time_Sorted_H_final[timecol])
#     Time_gen_H_fin[timecol] = {
#         "Mean ": mean,
#         "Mode ": mode,
#         "STD ": st_dev
#     }
#
# for facecol in Facebook_Sorted_df1.columns:
#     mean = np.mean(Facebook_Sorted_df1[facecol])
#     mode = np.median(Facebook_Sorted_df1[facecol])
#     st_dev = np.std(Facebook_Sorted_df1[facecol])
#     face_gen[facecol] = {
#         "Mean ": mean,
#         "Mode ": mode,
#         "STD ": st_dev
#     }
#
# for facecol in Facebook_Sorted_Y.columns:
#     mean = np.mean(Facebook_Sorted_Y[facecol])
#     mode = np.median(Facebook_Sorted_Y[facecol])
#     st_dev = np.std(Facebook_Sorted_Y[facecol])
#     face_gen_fin[facecol] = {
#         "Mean ": mean,
#         "Mode ": mode,
#         "STD ": st_dev
#     }
#
# for instacol in Instagram_Sorted_df1.columns:
#     mean = np.mean(Instagram_Sorted_df1[instacol])
#     mode = np.median(Instagram_Sorted_df1[instacol])
#     st_dev = np.std(Instagram_Sorted_df1[instacol])
#     insta_gen[instacol] = {
#         "Mean ": mean,
#         "Mode ": mode,
#         "STD ": st_dev
#     }
#
# for instacol in Instagram_Sorted_Y.columns:
#     mean = np.mean(Instagram_Sorted_Y[instacol])
#     mode = np.median(Instagram_Sorted_Y[instacol])
#     st_dev = np.std(Instagram_Sorted_Y[instacol])
#     insta_gen_fin[instacol] = {
#         "Mean ": mean,
#         "Mode ": mode,
#         "STD ": st_dev
#     }
#
#
# results_df1 = pd.DataFrame.from_dict(dict_gen, orient='index')
# results_df1.to_csv('desc_stats_per_gend-Fem.csv')
#
# results_df2 = pd.DataFrame.from_dict(dict_gen2, orient='index')
# results_df2.to_csv('desc_stats_per_gend-Mal.csv')
#
# results_df3 = pd.DataFrame.from_dict(bsmas_gen, orient='index')
# results_df3.to_csv('desc_stats_per_bsmas<14Mal.csv')
#
# results_df4 = pd.DataFrame.from_dict(bsmas_gen2, orient='index')
# results_df4.to_csv('desc_stats_per_bsmas>=14.csv')
#
# results_df5 = pd.DataFrame.from_dict(Time_gen_M_df1, orient='index')
# results_df5.to_csv('desc_stats_per_time_mid_no.csv')
#
# results_df6 = pd.DataFrame.from_dict(Time_gen_M_fin, orient='index')
# results_df6.to_csv('desc_stats_per_time_mid_yes.csv')
#
# results_df7 = pd.DataFrame.from_dict(Time_gen_H, orient='index')
# results_df7.to_csv('desc_stats_per_time_high_no.csv')
#
# results_df8 = pd.DataFrame.from_dict(Time_gen_H_fin, orient='index')
# results_df8.to_csv('desc_stats_per_time_high_yes.csv')
#
# results_df9 = pd.DataFrame.from_dict(face_gen, orient='index')
# results_df9.to_csv('desc_stats_per_fb_no.csv')
#
# results_df10 = pd.DataFrame.from_dict(face_gen_fin, orient='index')
# results_df10.to_csv('desc_stats_per_fb-yes.csv')
#
# results_df11 = pd.DataFrame.from_dict(insta_gen, orient='index')
# results_df11.to_csv('desc_stats_per_insta_no.csv')
#
# results_df12 = pd.DataFrame.from_dict(insta_gen_fin, orient='index')
# results_df12.to_csv('desc_stats_per_insta_yes.csv')

resultsdf13 = pd.DataFrame.from_dict(you_tube_gen_df1, orient='index')
resultsdf13.to_csv('desc_stats_per_yt_no.csv')

resultsdf14 = pd.DataFrame.from_dict(you_tube_gen_fin, orient='index')
resultsdf14.to_csv('desc_stats_per_yt_yes.csv')