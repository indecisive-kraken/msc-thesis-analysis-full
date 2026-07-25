import os
import warnings
import numpy as np
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
data = os.getenv("DATA")

warnings.filterwarnings('ignore')

# #1. -- Check if the file is of valid type, after that Pandas loads the data -- (you can add more file suffixes with an additional if statement and with filepaths = ['.xlsx', 'xlsm',])
# if Path(data).suffix == '.xlsx':
#     print('File received, proceeding...')
# else:
#     print('File is not of the form .xlsx, please input a valid file')
#     os._exit()

df1 = pd.read_excel(data, sheet_name='Sheet1')
df2 = pd.read_excel(data, sheet_name='Sheet2')

df_df1 = df1[["col","Mean of {str(column)}", "Mode of {str(column)}", "Variance of {str(column)}"]]

df_df2 = df2[["col","Mean of {str(column)}", "Mode of {str(column)}", "Variance of {str(column)}"]]

group_comp = {}

for col1, col2 in zip(df_df1.columns, df_df2.columns):
    for col1_r, col2_r in zip(col1.iterrows(), col2.iterrows()):
        if col1_r < col2_r:
            group_comp[col1] = { df_df1.iloc[col1] : 'mean of {col1} is lower in BSMAS Group >= 14'}
        elif col1_r > col2_r:
            group_comp[col2] = { df_df2.iloc[col2] : 'mean of {col2} is lower in BSMAS Group > 14 '}
        else:
            group_comp[col1] = {'result': 'equal'}

    results_df2 = pd.DataFrame.from_dict(group_comp, orient='index')
    results_df2.to_csv('comparison_res.csv')