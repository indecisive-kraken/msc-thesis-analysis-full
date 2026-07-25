import os
import re
import gower
import warnings
import pandas as pd
import numpy as np
from skbio.stats.distance import permanova
from skbio.stats.distance import permdisp
from skbio.stats.distance import anosim
from skbio import DistanceMatrix
from numpy import random

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
df = pd.read_excel(data, sheet_name='INDIV_VAR_REG')
# df = pd.read_excel(data, sheet_name='ENCODED_DATA')

print(df.info())
df.head()

#--------------
do_you_accept_columns()
#--------------

# all = df[['Q1', 'BSMAS', 'Gender', 'Age_Group'
#         ]]

all = df[['Q1','Q2', 'Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','BSMAS1','BSMAS2','BSMAS3','BSMAS4','BSMAS5','BSMAS6','Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N', 'BSMAS']]

# all = df[['Q1', 'Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
#         'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
#         'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]


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

# BSMAS_Sorted = BSMAS_Sorted.drop('BSMAS', axis=1)

distance_df = gower.gower_matrix(BSMAS_Sorted)
distance_matrix = DistanceMatrix(distance_df, dummy_list)

# -- Random Assignment for the validation of the exchangeabilty assumption

# shuffled_grouping_vector = np.random.permutation(grouping_vector)


print(BSMAS_Sorted.info())
print(BSMAS_Sorted)
print(dummy_list)
print(distance_matrix)
print(grouping_vector)
# print(shuffled_grouping_vector)

# result = permanova(distance_matrix, shuffled_grouping_vector, permutations=9999)
variance_check = anosim(distance_matrix, grouping_vector, permutations=9999)
#print(result)
#
print(variance_check)
