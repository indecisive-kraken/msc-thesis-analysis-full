import os
import re
import gower
import warnings
import pandas as pd
import numpy as np
from skbio.stats.distance import permanova
from skbio.stats.distance import permdisp
from skbio import DistanceMatrix

warnings.filterwarnings('ignore')

def do_you_accept_columns():
    answer = input('Please specify with a yes or no if you agree with the columns: ')
    while answer.lower() != 'yes' and answer.lower() != 'no':
        print('The current accepts only yes or no')
        answer = input('Please specify with a yes or no if you agree with the columns: ')
    if answer.lower() == 'no':
        print('Closing the script, please modify the data')
        os._exit()

# 1. -- Check if the file is of valid type, after that Pandas loads the data -- (you can add more file suffixes with an additional if statement and with filepaths = ['.xlsx', 'xlsm',])

data = input('Please specify the Excel file with the data: ')
df = pd.read_excel(data, sheet_name='ENCODED_DATA')

print(df.info())
df.head()

#--------------
do_you_accept_columns()
#--------------
#
all = df[['Q1', 'Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
         'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
         'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N'
        ]]
#
# all = df[[ 'Q1' , 'BSMAS'
#         ]]

print(all)
#
# numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
# for c in [c for c in all.columns if all[c].dtype in numerics]:
#     all[c] = np.log10(all[c])

#2. The PERMANOVA will use Gower Distances for the differences between groups

#initial separation of the data by various levels of BSMAS and matching the data sizes for the gower distance matrix

BSMAS_Sorted = all.sort_values(by=['BSMAS'], ascending=True)
BSMAS_Sorted = BSMAS_Sorted.astype(float)

grouping_vector = []

for el in BSMAS_Sorted['BSMAS']:
    if el > 14:
        grouping_vector.append('Group1')
    else:
        grouping_vector.append('Group2')

dummy_list = []

for i in range(0,111):
    dummy_list.append("s" + str(i))


#all_new = BSMAS_Sorted.drop('BSMAS')

distance_df = gower.gower_matrix(BSMAS_Sorted)
distance_matrix = DistanceMatrix(distance_df, dummy_list)

print(BSMAS_Sorted.info())
print(BSMAS_Sorted)
print(dummy_list)
print(distance_matrix)
print(grouping_vector)

result = permanova(distance_matrix, grouping_vector, permutations=9999)
# variance_check = permdisp(distance_matrix, grouping_vector, permutations=9999)
print(result)
#
# print(variance_check)

def calc_permanova_r2(distance_matrix, groups):
    """
    Calculate PERMANOVA R² effect size manually.

    distance_matrix: square symmetric matrix of distances (numpy array or object with .data attribute)
    groups: list or array of group labels

    Returns R² effect size.
    """
    groups = np.array(groups)
    n = len(groups)

    # Extract numpy array from distance matrix object if needed
    if hasattr(distance_matrix, 'data'):
        dist_arr = distance_matrix.data
    else:
        dist_arr = np.array(distance_matrix)

    # Square distances element-wise
    dist_sq = dist_arr ** 2

    # Total sum of squares (SST)
    # sum of squared distances divided by number of observations
    SST = np.sum(dist_sq) / n

    # Calculate sum of squares within groups (SSW)
    unique_groups = np.unique(groups)
    SSW = 0

    for g in unique_groups:
        idx = np.where(groups == g)[0]
        group_dists = dist_sq[np.ix_(idx, idx)]
        ng = len(idx)
        # sum of squared distances within group divided by group size
        SSW += np.sum(group_dists) / ng

    # Sum of squares between groups (SSB)
    SSB = SST - SSW

    # Calculate R^2 (proportion of variance explained)
    R_2 = SSB / SST

    print(dist_arr)
    print(dist_sq)

    return R_2


R_2 = calc_permanova_r2(distance_matrix, grouping_vector)

print(R_2)


