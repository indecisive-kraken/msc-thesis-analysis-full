import os
import warnings
from tqdm import tqdm
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = input('Please specify the Excel file with the data: ')
df = pd.read_excel(data, sheet_name='INDIV_VAR_REG')

y = df['Q1']
x1 = df[['Q2', 'Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','BSMAS1','BSMAS2','BSMAS3','BSMAS4','BSMAS5','BSMAS6','Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N', 'BSMAS']]

print(df.info())
df.head()

BSMAS_Sorted = x1.sort_values(by=['BSMAS'], ascending=True)
BSMAS_Sorted = BSMAS_Sorted.astype(float)

grouping1 = BSMAS_Sorted[BSMAS_Sorted['BSMAS'] < 14]    #grouping1
grouping2 = BSMAS_Sorted[BSMAS_Sorted['BSMAS'] >= 14]   #grouping2

#functions_to_execute = [] --functions can be collected on a list to iterate over its items (ie the string representations of the desired functions) in a separate for loop
#Make it so that the user exits when a condition is met

keep_option = []
enter_exit_command = input("Press enter to start the loop")

while enter_exit_command.lower() != "exit":

    if enter_exit_command.lower() == "exit":
        break

    print("Please type the function that you want to use from the following options\n "
          "Mean\n Variance\n Standard Deviation\n"
          "To end the program please type exit")

    enter_exit_command = input()

    if enter_exit_command != '' and enter_exit_command.lower() != 'exit':
        keep_option.append(enter_exit_command)

#stat_fun(np.mean, col) --can add regex functionality to make it even more modular, automated and meta-programmed
#is there a search engine for numpy modules? or just make a list and do a search for a keyword and use that on the command
#make it so that I can call from the top of the program the function described below to plot
    #so make a dictionary that stores the options of the user in order to know which statistic to plot and the title of the statistic

    if enter_exit_command.lower() == "mean":
        rep_var_g1 = [np.mean(grouping1[col].values) for col in grouping1.columns.values]
        rep_var_g2 = [np.mean(grouping2[col].values) for col in grouping2.columns.values]
    elif enter_exit_command.lower() == "variance":
        rep_var_g1 = [np.var(grouping1[col].values) for col in grouping1.columns.values]
        rep_var_g2 = [np.var(grouping2[col].values) for col in grouping2.columns.values]
    elif enter_exit_command.lower() == "standard deviation":
        rep_var_g1 = [np.std(grouping1[col].values) for col in grouping1.columns.values]
        rep_var_g2 = [np.std(grouping2[col].values) for col in grouping2.columns.values]

    print(rep_var_g1)
    print(rep_var_g2)

    group1_columns = list(grouping1.columns)
    group2_columns = list(grouping2.columns)

    df_grouping1 = pd.DataFrame({key : [value] for key, value in zip(group1_columns, rep_var_g1)})
    df_grouping2 = pd.DataFrame({key : [value] for key, value in zip(group2_columns, rep_var_g2)})

    print(df_grouping1.to_string())
    print(df_grouping2.to_string())


cols = df_grouping1.columns
plots_per_fig = 49
rows, cols_per_row = 7, 7

for i in tqdm(range(0, len(cols), plots_per_fig) , desc='Looping over dataframes'):

    sub_cols = cols[i:i + plots_per_fig]
    fig1, axs = plt.subplots(rows, cols_per_row, figsize=(16, 12))

    axs = axs.flatten()

    for j, column in enumerate(sub_cols):
        axs[j].hist([df_grouping1[column],df_grouping2[column]], color=['green', 'purple'], orientation='vertical')
        axs[j].set_title(column)

legend_colors = ['BSMAS < 14', 'BSMAS >= 14']

for i in tqdm([0], unit='seconds', desc='Generating all plots'):
    plt.title('')
    plt.legend(title = legend_colors)
    plt.xlabel('Independent Variables')
    plt.ylabel('Target Dependent Variable')
    plt.tight_layout()
    plt.savefig('{} + histogram.png'.format(keep_option[len(keep_option) - 1]), dpi=300, bbox_inches='tight')

