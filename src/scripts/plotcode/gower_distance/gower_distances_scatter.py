import os
import gower
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
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

print(all)
#
# numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
# for c in [c for c in all.columns if all[c].dtype in numerics]:
#     all[c] = np.log10(all[c])

#2. The PERMANOVA will use Gower Distances for the differences between groups

#initial separation of the data by various levels of BSMAS and matching the data sizes for the gower distance matrix

BSMAS_Sorted = all.sort_values(by=['BSMAS'], ascending=True)
BSMAS_Sorted = BSMAS_Sorted.astype(float)

grouping1 = BSMAS_Sorted[BSMAS_Sorted['BSMAS'] < 14]    #grouping1
grouping2 = BSMAS_Sorted[BSMAS_Sorted['BSMAS'] >= 14]   #grouping2

grouping1['BSMAS_Under_14'] = grouping1[['BSMAS']]
grouping2['BSMAS_Over_14'] = grouping2[['BSMAS']]
grouping_vector = []

for el in BSMAS_Sorted['BSMAS']:
    if el > 14:
        grouping_vector.append('Group1')
    else:
        grouping_vector.append('Group2')

dummy_list = []

for i in range(0,111):
    dummy_list.append("s" + str(i))

# all_new = BSMAS_Sorted.drop('BSMAS')

distance_df = gower.gower_matrix(BSMAS_Sorted)
distance_matrix = DistanceMatrix(distance_df, dummy_list)

print(BSMAS_Sorted.info())
print(BSMAS_Sorted)
print(dummy_list)
print(distance_matrix)
print(grouping_vector)

# Plotting

distance_group1 = gower.gower_matrix(grouping1)
distance_group2 = gower.gower_matrix(grouping2)

print(distance_group1)
print(distance_group2)

fig, ax = plt.subplots(figsize=(8, 6))

# Plot each group's variables as scatter points
ax.scatter(distance_group1, distance_group2, color='skyblue', label='Group 1', s=60)
# ax.scatter(distance_group2, color='salmon', label='Group 2', s=60)

plt.title('Scatterplot of BSMAS Groups')
plt.savefig('scatterplot_bsmas_groups.png')

# Add ellipses to indicate group spread
def add_ellipse(data, ax, color, label):
    mean = np.mean(data, axis=0)
    cov = np.cov(data.T)
    vals, vecs = np.linalg.eigh(cov)
    order = vals.argsort()[::-1]
    vals, vecs = vals[order], vecs[:, order]
    angle = np.degrees(np.arctan2(*vecs[:, 0][::-1]))
    width, height = 2 * np.sqrt(vals)
    ellipse = Ellipse(mean, width, height, edgecolor=color, facecolor='none', lw=2, label=label)
    ax.add_patch(ellipse)

add_ellipse(distance_group1, distance_group2, ax, 'blue', 'Group 1 Ellipse')
# add_ellipse(distance_group2, ax, 'red', 'Group 2 Ellipse')

# Draw example Gower distance line between corresponding variables (e.g., Var5 in both groups)
# i = 5  # Index of example variable
# ax.plot(
#     [grouping1[i, 0], grouping2[i, 0]],
#     [grouping1[i, 1], grouping2[i, 1]],
#     color='gray', linestyle='--', linewidth=2, label='Example Gower Distance'
# )

ax.plot(distance_group1, distance_group2, color='gray', linestyle='--', linewidth=2, label='Gower Distance between groups')
# Labels and styling
ax.set_title("Variable Representation by Group with Gower Distance")
ax.set_xlabel("Feature Space Dimension 1")
ax.set_ylabel("Feature Space Dimension 2")
ax.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("gower_distance_scatter.png")
