import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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

# Assuming you have your DataFrame loaded as df
# Compute correlation matrix

for i in tqdm([0], unit='seconds', desc='Generating HeatMap'):
    corr_matrix = df.corr(numeric_only=True)

    # Set up the matplotlib figure
    plt.figure(figsize=(16, 12))

    # Draw the heatmap
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', center=0)

    plt.title("Correlation Heatmap")
    plt.savefig('Heatmap.png')