import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data = input('Please specify the Excel file with the data: ')

# 1. -- Check if the file is of valid type, after that Pandas loads the data -- (you can add more file suffixes with an additional if statement and with filepaths = ['.xlsx', 'xlsm',])

if Path(data).suffix == '.xlsx':
    print('File received, proceeding...')
else:
    print('File is not of the form .xlsx, please input a valid file')
    os._exit()

df = pd.read_excel(data, sheet_name='ENCODED_DATA')

# 2. -- Dataframes for plots, X and y axis --

y = df['Q1']
X = df[['Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]
x2=df[[]]

print(df.info())

def box_plotting(title, alternative_title, statistic_function1, statistic_function2):

    #Two by two as you model the regular statistic and the bootstrap statistic.
    fig, axs = plt.subplots(2,2, figsize=(16,12))
    axs = axs.flatten()

    axs[0].boxplot(statistic_function1)
    axs[1].boxplot(statistic_function2)
    axs.set_title()
    plt.title('Normal' + str(title) + 'vs' + str(alternative_title))
    plt.ylabel('Measure Values')
    plt.tight_layout()
    plt.savefig(str(title) + 'vs' + str(alternative_title) + '.png')

def hist_plotting(title, alternative_title, statistic_function1, statistic_function2):

    # Two by two as you model the regular statistic and the bootstrap statistic.
    fig, axs = plt.subplots(2, 2, figsize=(16, 12))
    axs = axs.flatten()

    axs[0].histplot(statistic_function1)
    axs[1].histplot(statistic_function2)
    axs.set_title()
    plt.title('Normal' + str(title) + 'vs' + str(alternative_title))
    plt.ylabel('Measure Values')
    plt.tight_layout()
    plt.savefig(str(title) + 'vs' + str(alternative_title) + '.png')

NBoot = 400
def bootstrap(x, Nboot, statfun):

    x = np.array(x)
    resampled_stat = []

    for k in range(NBoot):
        index = np.random.randint(0, len(x), len(x))
        sample = x[index]

        def stat_fun(statfun):
            return statfun

        bstatistic = stat_fun(sample)
        resampled_stat.append(bstatistic)

    return np.array(resampled_stat)

print(bootstrap(X, NBoot, np.mean(X)))

# box_plotting('Mean', 'vs Bootstrapped Mean', np.mean(X), bootstrap(X, NBoot, np.mean(X)))
#You can make it so that the title is being added from user input and then the string of the input concatenated


