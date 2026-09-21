import os
import re
import gower
import warnings
import numpy as np
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame
from scipy import stats
from skbio.stats.distance import permanova
from skbio.stats.distance import permdisp
from skbio import DistanceMatrix
from scipy.spatial import distance_matrix
from statsmodels.stats.multitest import multipletests
from scipy.cluster.hierarchy import centroid, fcluster
from scipy.spatial.distance import pdist

warnings.filterwarnings('ignore')

# 1. -- Check if the file is of valid type, after that Pandas loads the data -- (you can add more file suffixes with an additional if statement and with filepaths = ['.xlsx', 'xlsm',])

data = input('Please specify the Excel file with the data: ')
df = pd.read_excel(data, sheet_name='ENCODED_DATA')

print(df.info())
df.head()

#--------------
do_you_accept_columns()
#--------------

all = df[['Q1','Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

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

distance_df = gower.gower_matrix(BSMAS_Sorted)
distancematrix = DistanceMatrix(distance_df, dummy_list)

print("All\n", all)
print("BSMAS Sorted Info\n", BSMAS_Sorted.info())
print("BSMAS Sorted\n", BSMAS_Sorted)
print("Dummy List\n", dummy_list)
print("Distance Matrix\n", distancematrix)
print("Grouping Vector\n", grouping_vector)

result = permanova(distancematrix, grouping_vector, permutations=9999)
# variance_check = permdisp(distance_matrix, grouping_vector, permutations=9999)
print(result)


group_over14 = all[all['BSMAS'] >= 14]
group_under14 = all[all['BSMAS'] < 14]

print(group_over14)
print(group_over14.info())
print(group_under14)
print(group_under14.info())

mean_group_over14 = centroid(group_over14)
mean_group_under14 = centroid(group_under14)

print("Mean of the group with BSMAS scores under 14: ",mean_group_under14)
print("Mean of the group with BSMAS scores over 14: ", mean_group_over14)


group_over14df = all[all['BSMAS'] >= 14]
group_under14df  = all[all['BSMAS'] < 14]


mean_dict1 = {}
mean_dict2 = {}

for column in group_over14df.columns:
    indv_col = group_over14df[column]
    mean_col = np.mean(indv_col)
    mean_dict1 = {
        "Column" : column,
        "Mean" : mean_col
    }
    mean_dictdf = pd.DataFrame.from_dict(mean_dict1, orient='index')
    mean_dictdf.to_csv("Mean Values of GroupOver14")


for column in group_under14df.columns:
    indv_col2 = group_under14df[column]
    mean_col2= np.mean(indv_col2)
    mean_dict2[column] = {
        "Mean": mean_col2
    }
    mean_dict2df = pd.DataFrame.from_dict(mean_dict2, orient='index')
    mean_dict2df.to_csv("Mean Values of GroupUnder14")


ind_col1 = group_over14df['Q1']
ind_col2 = group_under14df['Q1']

mean1 = np.mean(ind_col1)
mean2 = np.mean(ind_col2)

print(ind_col1)
print(ind_col1.info())
print(ind_col2)
print(ind_col2.info())

print(mean1)
print(mean2)

grouping_vector_2 = []

for time_col1, time_col2 in zip(BSMAS_Sorted["Time_Spent_M"], BSMAS_Sorted["Time_Spent_H"]):
    try:
        if time_col1 == 1 or time_col2 == 1:
            grouping_vector_2.append("Group1")
        elif time_col1 == 0 and time_col2 == 0:
            grouping_vector_2.append("Group2")
    except:
        print("There is a wrong value or a logic error in the code")

print(f"Grouping vector 2 for separation of groups by time spent: \n {grouping_vector_2}")

result_separation_2 = permanova(distancematrix, grouping_vector_2 ,permutations=9999)

print(result_separation_2)

grouping_vector_3 = []

print(variance_check)

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


# Per variable PERMANOVA and p-value Bonferroni correction

for column in BSMAS_Sorted.columns:

    print(column)
    print("BSMAS Sorted\n", BSMAS_Sorted.info())

    if column == 'BSMAS':
        continue

    distance_df = pd.DataFrame(BSMAS_Sorted)

    print(distance_df.info())
    print(distance_df)

    distance_group1 = distance_df[distance_df['BSMAS'] >= 14]
    distance_group2 = distance_df[distance_df['BSMAS'] < 14]

    print(distance_group1)
    print(distance_group2)

    distanceMatrix = distance_matrix(distance_group1[column] , distance_group2[column])

    result = permanova(distanceMatrix, grouping_vector, permutations=9999)

    p_values = result.findall(r"^[\w]+\s+[\d]\b", 'p-value')

    print("PERMANOVA results of column {column}", result, p_values)

    results_df = pd.DataFrame(p_values)

print(results_df)
p_val_rev = [v['P-Value'] for v in results_df.items()]
corrected = multipletests(p_val_rev, method='bonferroni')

print(corrected)
