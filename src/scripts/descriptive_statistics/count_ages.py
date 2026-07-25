import openpyxl
import numpy as np
import pandas as pd

data = input('Please specify the Excel file with the data: ')

df = pd.read_excel(data, sheet_name='Statistics')

target_list = df['Age_Group_1'].values[0]

group_18_25 = 0
group_26_35 = 0
group_36_45 = 0
group_46_55 = 0
group_56_65 = 0
group_66_75 = 0
group_76_85 = 0
group_86_over = 0

for ages in target_list:
    if ages > 18 and ages <=25 : group_18_25 += 1
    elif ages > 25 and ages <=35 : group_26_35 += 1
    elif ages > 35 and ages <=45 : group_36_45 += 1
    elif ages > 45 and ages <=55 : group_46_55 += 1
    elif ages > 55 and ages <= 65 : group_56_65 += 1
    elif ages > 65 and ages <= 75: group_66_75 += 1
    elif ages > 76 and ages <= 85: group_76_85 += 1
    else: group_86_over += 1

print('Ages 18 -25: ' + str(group_18_25),
      'Ages 26 - 35: ' + str(group_26_35),
      'Ages 36 - 45: ' + str(group_36_45),
      'Ages 46 - 55: ' + str(group_46_55),
      'Ages 56 - 65: ' + str(group_56_65),
      'Ages 66 - 75: ' + str(group_66_75),
      'Ages 76 - 85: ' + str(group_76_85),
      'Ages 86 + : ' + str(group_86_over))
