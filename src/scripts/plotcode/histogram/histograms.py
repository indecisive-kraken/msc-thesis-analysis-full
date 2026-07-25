import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.linalg import inv
from scipy.stats import chi2, norm
from pandas.plotting import scatter_matrix
# from tqdm import tqdm
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


# 3. -- Basic Plots_junk --

def malahabosis_qq(df):
    script_dir = os.path.dirname(__file__)
    X = df.values
    mean_vec = np.mean(X, axis=0)
    cov_mat = np.cov(X, rowvar=False)
    inv_covmat = inv(cov_mat)

    # Compute Mahalanobis distances
    md_squared = np.array([np.dot(np.dot((x - mean_vec), inv_covmat), (x - mean_vec).T) for x in X])

    # Chi-squared quantiles
    chi2_q = chi2.ppf((np.arange(1, len(md_squared) + 1) - 0.5) / len(md_squared), df.shape[1])

    # Sort for Q-Q plot
    md_sorted = np.sort(md_squared)

    plt.figure(figsize=(8, 6))
    plt.plot(chi2_q, md_sorted, 'o', label='Observed vs. Theoretical')
    plt.plot(chi2_q, chi2_q, 'r--', label='Ideal Fit')
    plt.xlabel('Chi-squared Quantiles')
    plt.ylabel('Ordered Mahalanobis Distances²')
    plt.title('Mahalanobis Q-Q Plot')
    plt.legend()
    plt.grid(True)

    results_dir = os.path.join(script_dir, 'results/')
    if not os.path.isdir(results_dir):
        os.makedirs(results_dir)
    plt.savefig(os.path.join(results_dir, 'plot.png'), dpi=300, bbox_inches='tight')


malahabosis_qq(df)

# 3. -- Plot some graphs --

'''
counter_0 = 1
for column in df.columns[0:]:
    plot = plt.plot(y, df[column])
    plt.savefig("plot_name" + str(counter_0) + ".png", dpi=300, bbox_inches='tight')
    counter += 1
# '''
# counter = 0
# column_counter = 0
# iteration_counter = 0
# list = list(df[0:])
#
#
# cols = df.columns
# plots_per_fig = 24
# rows, cols_per_row = 6, 4
#
# for i in tqdm(range(0, len(cols), plots_per_fig), desc='Plotting Histograms'):
#     sub_cols = cols[i:i+plots_per_fig]
#     fig, axs = plt.subplots(rows, cols_per_row, figsize=(16, 12))
#     axs = axs.flatten()
#
#     for j, column in enumerate(sub_cols):
#         axs[j].hist(df[column].dropna(), bins=30)  # Drop NaNs for cleaner plots
#         axs[j].set_title(column)
#
#     for k in range(j+1, len(axs)):
#         fig.delaxes(axs[k])  # remove unused subplots
#
#     plt.tight_layout()
#     plt.show()
#
#
# for i in tqdm([0], unit='seconds', desc='Generating Histplot'):
#     plt.title('Distribution of the QoL Values in comp. to independent variables')
#     plt.xlabel('Independent Variables')
#     plt.ylabel('QoL Values')
#     plt.savefig('histplot2.png', dpi=300, bbox_inches='tight')

# fig, axs = plt.subplot()
# axs = axs.flatten()
# axs.hist(X[X['D1']])
#
# plt.tight_layout()
# plt.xlabel('saj')
# plt.ylabel('sbc')
# plt.savefig('histplot1212.png', dpi=300, bbox_inches='tight')

# Apply log transformation (with np.log1p to handle zero values)
df['log_D1'] = np.log1p(df['D1'])
df['log_D2'] = np.log1p(df['D2'])
df['log_D3'] = np.log1p(df['D3'])
df['log_D4'] = np.log1p(df['D4'])
df['log_BSMAS'] = np.log1p(df['BSMAS'])

# Plot the histograms of the log-transformed variables
fig, axes = plt.subplots(3, 2, figsize=(12, 10))

axes[0, 0].hist(df['D1'], bins=20, color='skyblue', edgecolor='black')
axes[0, 0].set_title('D1')

axes[0, 1].hist(df['D2'], bins=20, color='skyblue', edgecolor='black')
axes[0, 1].set_title('D2')

axes[1, 0].hist(df['D3'], bins=20, color='skyblue', edgecolor='black')
axes[1, 0].set_title('D3')

axes[1, 1].hist(df['D4'], bins=20, color='skyblue', edgecolor='black')
axes[1, 1].set_title('D4')

axes[2, 0].hist(df['BSMAS'], bins=20, color='skyblue', edgecolor='black')
axes[2, 0].set_title('BSMAS')

# Adjust layout
plt.tight_layout()
plt.savefig('histplot-nonlogtransformed.png', dpi=300, bbox_inches='tight')