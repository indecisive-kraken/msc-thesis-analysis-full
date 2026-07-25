import os
import numpy as np
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
data = os.getenv("DATA")

#1. -- Check if the file is of valid type, after that Pandas loads the data -- (you can add more file suffixes with an additional if statement and with filepaths = ['.xlsx', 'xlsm',])
if Path(data).suffix == '.xlsx':
    print('File received, proceeding...')
else:
    print('File is not of the form .xlsx, please input a valid file')
    os._exit()

df = pd.read_excel(data, sheet_name='ENCODED_DATA')
y = df['Q1']
x = df[['Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

#count = []
#arr_age[18,25,35,45,55,65,75,85]
# for i in arr_age
#    count[i] = arr_age[] continue make it pretty sometime, now too tired and sleepy

count_1825 = 0
count_2635 = 0
count_3645 = 0
count_4655 = 0
count_5665 = 0
count_6675 = 0
count_7685 = 0
count_86plus = 0

for i, j in zip(x['Time_Spent_M'], x['Age_Group']):
    if i == 1 and j <= 25 and j > 0:
        count_1825 += 1
    elif i == 1 and j > 25 and j <= 35:
        count_2635 += 1
    elif i == 1 and j > 35 and j <= 45:
        count_3645 += 1
    elif i == 1 and j > 45 and j <= 55:
        count_4655 += 1
    elif i == 1 and j > 55 and j <= 65:
        count_5665 += 1
    elif i == 1 and j > 65 and j <= 75:
        count_6675 += 1
    elif i == 1 and j > 75 and j <= 85:
        count_7685 += 1
    elif i == 1 and j > 85:
        count_86plus += 1

first_print = "First Print: "

print(first_print, count_1825, count_2635, count_3645, count_4655, count_5665, count_6675, count_7685, count_86plus)

sum1 = count_1825 + count_2635 + count_3645 + count_4655 + count_5665 + count_6675 + count_7685 + count_86plus

print("Sum 2 to 5 hours count: " + str(sum1))

count_1825 = 0
count_2635 = 0
count_3645 = 0
count_4655 = 0
count_5665 = 0
count_6675 = 0
count_7685 = 0
count_86plus = 0
second_print = "Second Print: "

for i, j in zip(x['Time_Spent_H'], x['Age_Group']):
    if i == 1 and j <= 25 and j > 0:
        count_1825 += 1
    elif i == 1 and j > 25 and j <= 35:
        count_2635 += 1
    elif i == 1 and j > 35 and j <= 45:
        count_3645 += 1
    elif i == 1 and j > 45 and j <= 55:
        count_4655 += 1
    elif i == 1 and j > 55 and j <= 65:
        count_5665 += 1
    elif i == 1 and j > 65 and j <= 75:
        count_6675 += 1
    elif i == 1 and j > 75 and j <= 85:
        count_7685 += 1
    elif i == 1 and j > 85:
        count_86plus += 1

print(second_print, count_1825, count_2635, count_3645, count_4655, count_5665, count_6675, count_7685, count_86plus)

sum2 = count_1825 + count_2635 + count_3645 + count_4655 + count_5665 + count_6675 + count_7685 + count_86plus
print("Sum over 5 hours count: " + str(sum2))

for i, j, k in zip(x['Time_Spent_M'], x['Time_Spent_H'], x['Age_Group']):
    if i == 0 and j == 0 and k <= 25 and k > 0:
        count_1825 += 1
    elif i == 0 and j == 0 and k > 25 and k <= 35:
        count_2635 += 1
    elif i == 0 and j == 0 and k > 35 and k <= 45:
        count_3645 += 1
    elif i == 0 and j == 0 and k > 45 and k <= 55:
        count_4655 += 1
    elif i == 0 and j == 0 and k > 55 and k <= 65:
        count_5665 += 1
    elif i == 0 and j == 0 and k > 65 and k <= 75:
        count_6675 += 1
    elif i == 0 and j == 0 and k > 75 and k <= 85:
        count_7685 += 1
    elif i == 0 and j == 0 and k > 85:
        count_86plus += 1

third_print = "Third Print: "

print(third_print, count_1825, count_2635, count_3645, count_4655, count_5665, count_6675, count_7685, count_86plus)
sum3 = count_1825 + count_2635 + count_3645 + count_4655 + count_5665 + count_6675 + count_7685 + count_86plus

print("Sum less than 2 hours per day: " + str(sum3))