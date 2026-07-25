# -- Code from : https://builtin.com/data-science/tsne-python

import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D

data = input('Please specify the Excel file with the data: ')
df = pd.read_excel(data, sheet_name='INDIV_VAR_REG')

print(df.info())
df.head()

y = df['Q1']
x1 = df[['Q2', 'Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','BSMAS1','BSMAS2','BSMAS3','BSMAS4','BSMAS5','BSMAS6','Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

x2 = df[['Q2', 'Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','BSMAS1','BSMAS2','BSMAS3','BSMAS4','BSMAS5','BSMAS6']]

all = df[[]]
print(x1.shape, y.shape)

feat_cols = ['pixel' + str(i for i in range(x1.shape[1]))]

df_new = pd.DataFrame(all, columns =feat_cols)
df['y'] = y
df['label'] = df['y'].apply(lambda i : str(i))

X, y = None

print('Size of the dataframe: {}'.format(df_new.shape))

# plt.gray()
# fig = plt.figure(figsize=(10,5))
#
# for i in range(0, 9):
#     ax = fig.add_subplot()

pca = PCA(n_components=all.shape)
pca_result = pca.fit_transform(all[feat_cols].values)

df['pca-one'] = pca_result[:, 0]
df['pca_two'] = pca_result[:, 1]
df['pca-three'] = pca_result[:, 2]
