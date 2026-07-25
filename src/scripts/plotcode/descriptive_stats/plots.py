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

#1. -- Check if the file is of valid type, after that Pandas loads the data -- (you can add more file suffixes with an additional if statement and with filepaths = ['.xlsx', 'xlsm',])

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

#3. -- Basic Plots_junk --

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

#3. -- Plot some graphs --

'''
counter_0 = 1
for column in df.columns[0:]:
    plot = plt.plot(y, df[column])
    plt.savefig("plot_name" + str(counter_0) + ".png", dpi=300, bbox_inches='tight')
    counter += 1
'''
counter = 0
column_counter = 0
iteration_counter = 0
list_1 = list(df[0:])

for column in tqdm(df.columns[0:], unit='seconds', desc='Looping for Hist and Box Plots_junk'):

    x = df[column]
    y = df.Q1
    fig1, ax1 = plt.subplots(6, 4, figsize = (10,8))
    fig2, ax2 = plt.subplots(6, 4, figsize = (10,8))

    if iteration_counter == 0:
        while counter % 4 != 0:
            sns.histplot(data=df, x=x)
            ax1[column_counter, counter].set_title(list_1[counter])
            sns.boxplot(data=df, x=x)
            ax2[column_counter, counter].set_title(list_1[counter])
            if counter % 4 == 0:
                column_counter = 0
                counter = 1
                iteration_counter = 0
    
    else:
        sns.histplot(data=df, x=x)
        ax1[column_counter, counter].set_title(list_1[counter])
        sns.boxplot(data=df, x=x)
        ax2[column_counter, counter].set_title(list_1[counter])

    counter += 1
    column_counter += 1

for i in tqdm([0], unit='seconds', desc='Generating Histplot'):
    plt.title('Distribution of the QoL Values in comp. to independent variables')
    plt.xlabel('Independent Variables')
    plt.ylabel('QoL Values')
    plt.savefig('histplot.png', dpi=300, bbox_inches='tight')

for i in tqdm([0], unit='seconds', desc='Generating Boxplot'):
    plt.title('Box plot of the QoL Values and Ind. Variable')
    plt.xlabel('Independent Variables')
    plt.ylabel('QoL Values')
    plt.savefig('boxplot.png', dpi=300, bbox_inches='tight')


for i in tqdm([0], unit='seconds', desc='Generating Pairplot'):
    pair_plot = sns.pairplot(df)
    pair_plot.plt.savefig('Pairplot_All.png', dpi=300, bbox_inches='tight')

for i in tqdm([0], unit='seconds', desc='Generating Scatter Matrix'):
    scatter_m = scatter_matrix(df, alpha = 0.2, figsize = (6,6), diagonal="kde")
    scatter_m.figure.savefig("Sc_Mat-Ind_Var.png")


