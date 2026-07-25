import pandas as pd
from patsy import dmatrices
from data import get_data_path

()

data = get_data_path()

df = pd.read_excel(data, sheet_name='ENCODED_DATA')
vars = ['Q1','Q2','D1','D2','D3','D4','BSMAS','Gender','Education','Attachment_Style','Age_Group','Time_spent','Employment_status']
df = df[vars]

Male = df.query('grouping == 1')['Gender']
Female = df.query('grouping = 0')['Gender']

df.groupby('grouping').describe()







