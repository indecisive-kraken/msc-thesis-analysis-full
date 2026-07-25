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


# 3. -- Plot some graphs --

list = list(df[0:])

for i in tqdm([0], unit='seconds', desc = 'Generating Jointplots'):
    numeric_cols = df.select_dtypes(include='number').columns
    print(numeric_cols)

    n_cols = 4
    n_rows = int(len(numeric_cols)/n_cols) + (len(numeric_cols) % n_cols > 0)
    plt.figure(figsize=(n_cols * 5, n_rows * 4))

    for i, col in enumerate(numeric_cols, 1):
        if i == 24:
            break
        else:
            plt.subplot(n_rows, n_cols, i)
            sns.jointplot(y=df['Q1'], x=df[col].dropna(),data=df)
            plt.title('Jointplot')
            plt.tight_layout()
            plt.savefig("JointPlot " + str(i) + ".png")

