import os
import re
import gower
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from skbio import DistanceMatrix

data = input('Please specify the Excel file with the data: ')
df = pd.read_excel(data, sheet_name='ENCODED_DATA')

print(df.info())
df.head()

all = df[['Q1', 'Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
         'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
         'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N'
         ]]

bsmas_group1 = all[all['BSMAS'] >= 14]
bsmas_group2 = all[all['BSMAS'] < 14]

print(bsmas_group1)
print()
print(bsmas_group2)

data = np.vstack([bsmas_group1, bsmas_group2])

variables = [f'Var {col}' for col in all.columns]

x = np.arange(len(variables))
width = 0.35
fig, ax = plt.subplots(figsize=(12, 5))

bars1 = ax.bar(x- width/2, data[0], width, label='Group1', color='skyblue')
bars2 = ax.bar(x + width/2, data[1], width, label = 'Group2', color = 'salmon')

ax.set_xlabel('Variables')
ax.set_ylabel('Average Gower Distance')
ax.set_title('Per-variable Gower Distances by Group')
ax.set_xticks(x)
ax.set_xticklabels(variables, rotation=45, ha='right')
ax.legend()

plt.tight_layout()
plt.savefig("1.jpg")