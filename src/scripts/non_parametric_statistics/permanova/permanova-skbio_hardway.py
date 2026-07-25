import os
import re
import gower
import warnings
import pandas as pd
import numpy as np
from skbio.stats.distance import permanova
from skbio import DistanceMatrix

warnings.filterwarnings('ignore')

def array_info(arr):
    print(f"Shape: {arr.shape}")
    print(f"Dtype: {arr.dtype}")
    print(f"Size (total elements): {arr.size}")
    print(f"Memory usage: {arr.nbytes / 1024:.2f} KB")
    print(f"Min: {np.min(arr)}")
    print(f"Max: {np.max(arr)}")
    print(f"Mean: {np.mean(arr):.3f}")
    print(f"Std: {np.std(arr):.3f}")

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

all = df[['Q1','Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

#2. The PERMANOVA will use Gower Distances for the differences between groups

#initial separation of the data by various levels of BSMAS and matching the data sizes for the gower distance matrix

BSMAS_Sorted = all.sort_values(by=['BSMAS'], ascending=True)
BSMAS_Sorted = BSMAS_Sorted.astype(float)

grouping1 = BSMAS_Sorted[BSMAS_Sorted['BSMAS'] < 14]    #grouping1
grouping2 = BSMAS_Sorted[BSMAS_Sorted['BSMAS'] >= 14]   #grouping2

grouping1['BSMAS_Under_14'] = grouping1[['BSMAS']]
grouping2['BSMAS_Over_14'] = grouping2[['BSMAS']]

n = len(grouping1)
half = n // 2

grouping1_sub1 = grouping1.iloc[:half]
grouping1_sub2 = grouping1.iloc[half:]

new_index_1 = max(grouping1_sub1.index) + 1
new_index_2 = max(grouping2.index) + 2

del grouping1_sub1['BSMAS']
del grouping1_sub2['BSMAS']
del grouping2['BSMAS']

grouping1_sub2['BSMAS_Under_14_Part1'] = grouping1_sub2[['BSMAS_Under_14']]
del grouping1_sub2['BSMAS_Under_14']
grouping2 = grouping2.astype(float)

random_index = df.sample(n=1).index

grouping1_sub1_drop = grouping1_sub1.drop(index = grouping1_sub1.sample(n=1).index)
grouping1_sub2_drop = grouping1_sub2.drop(index = grouping1_sub2.sample(n=2).index)

for col1 in grouping1_sub1_drop:
    grouping1_sub1_drop[col1 + '{Group1}'] = grouping1_sub1_drop[[col1]]
    del grouping1_sub1_drop[col1]

for col2 in grouping1_sub2_drop:
    grouping1_sub2_drop[col2 + '{_Group1}'] = grouping1_sub2_drop[[col2]]
    del grouping1_sub2_drop[col2]

for col3 in grouping2:
    grouping2[col3 + '{Group2}'] = grouping2[[col3]]
    del grouping2[col3]

all_data = pd.concat([grouping1_sub1_drop.reset_index(drop=True), grouping1_sub2_drop.reset_index(drop=True), grouping2.reset_index(drop=True)], axis=1, ignore_index=False)

# Gower's distance matrix
distance_df = gower.gower_matrix(all_data)

distance_df_new = distance_df.T

#make a dummy list for denoting the columns -- see https://scikit.bio/docs/dev/generated/skbio.stats.distance.permdisp.html -- similar case is PERMANOVA

dummy_list = []
for i in range(0,72):
    dummy_list.append("s" + str(i))

print(dummy_list)

# distance_matrix = DistanceMatrix(distance_df_new, dummy_list)

d = pd.DataFrame(distance_df)

#if the index of the column contains the string Group1/Group2, append in the grouping vector the string group1/group2

index_arr = list(all_data.columns)
grouping_vector = []

for el in index_arr:
    string_group1 = "Group1"
    string_group2 = "Group2"
    if string_group1 in el:
        grouping_vector.append("Group1")
    elif string_group2 in el:
        grouping_vector.append("Group2")

print("Grouping1_sub1_drop: \n", grouping1_sub1_drop.info(),"\n")
print("Grouping1_sub2_drop: \n",grouping1_sub2_drop.info(),"\n")
print("Grouping2: \n", grouping2.info(),"\n")
print("All data \n",all_data.info(),"\n")
print(all_data)
print("Grouping1_sub1_drop: \n", grouping1_sub1_drop.info(),"\n")
print("Distance df \n",distance_df,"\n")
print("Distance_df_new \n", distance_df_new, "\n")
print("Index array \n",index_arr,"\n")
print("Grouping Vector \n", grouping_vector,"\n")
print("Length of the grouping vector: " + str(len(grouping_vector)))

#--------------
do_you_accept_columns()
#--------------

# -- Final PERMANOVA --
result = permanova(distance_matrix, grouping_vector, permutations=999)
print(result)



