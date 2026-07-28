import warnings
from scipy.stats import mannwhitneyu
from scripts.data.get_data_path import open_data_file

def mann_whitneyu():

    df = open_data_file()
    warnings.filterwarnings('ignore')
    print(df.info())
    df.head()

    all = df[['BSMAS']]
    bsmas_group1 = all[all['BSMAS'] > 14]
    bsmas_group2 = all[all['BSMAS'] <= 14]

    print(bsmas_group1)
    print()
    print(bsmas_group2)

    # perform mann whitney test
    stat, p_value = mannwhitneyu(bsmas_group1, bsmas_group2)
    print('Statistics=%.2f, p=%.2f', stat, p_value)
    # Level of significance
    alpha = 0.05
    # conclusion
    if p_value < alpha:
        print('Reject Null Hypothesis (Significant difference between two samples)')
    else:
        print('Do not Reject Null Hypothesis (No significant difference between two samples)')

mann_whitneyu()
