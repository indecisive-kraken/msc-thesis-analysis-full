import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.linalg import inv
from scipy.stats import chi2, norm
from pandas.plotting import scatter_matrix
from tqdm import tqdm
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
print(df.info())


counter = 0
column_counter = 0
iteration_counter = 0
list = list(df[0:])


cols = df.columns
plots_per_fig = 24
rows, cols_per_row = 6, 4

for i in tqdm(range(0, len(cols), plots_per_fig), desc='Plotting Boxplots'):
    sub_cols = cols[i:i+plots_per_fig]
    fig, axs = plt.subplots(rows, cols_per_row, figsize=(16, 12))
    axs = axs.flatten()

    for j, column in enumerate(sub_cols):
        axs[j].boxplot(df[column].dropna())  # Drop NaNs for cleaner plots
        axs[j].set_title(column)

    for k in range(j+1, len(axs)):
        fig.delaxes(axs[k])  # remove unused subplots

    plt.tight_layout()
    plt.show()

for i in tqdm([0], unit='seconds', desc='Generating Boxplot'):
    plt.title('Box plot of the QoL Values and Ind. Variable')
    plt.xlabel('Independent Variables')
    plt.ylabel('QoL Values')
    plt.savefig('boxplot.png', dpi=300, bbox_inches='tight')
