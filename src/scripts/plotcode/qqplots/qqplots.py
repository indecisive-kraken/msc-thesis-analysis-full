import os
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
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

print(df.info())

for i in tqdm([0], unit='seconds', desc='Generating qqplots'):
    # Loop through each numeric column
    numeric_cols = df.select_dtypes(include='number').columns

    # Plot Q-Q plots in a grid
    n_cols = 3
    n_rows = int(len(numeric_cols) / n_cols) + (len(numeric_cols) % n_cols > 0)
    plt.figure(figsize=(n_cols * 5, n_rows * 4))

    for i, col in enumerate(numeric_cols, 1):
        plt.subplot(n_rows, n_cols, i)
        stats.probplot(df[col].dropna(), dist="norm", plot=plt)
        plt.title(f'Q-Q Plot: {col}')

    plt.tight_layout()
    plt.savefig('qqplots.png')
