import warnings
import pandas as pd
from scipy.stats import shapiro
from scipy.stats import kstest
from scipy.stats import anderson
from data import get_data_path


def normality_tests():

    warnings.filterwarnings('ignore')

    data = get_data_path()
    df = pd.read_excel(data, sheet_name='ENCODED_DATA')

    print(df.info())
    df.head()

    all = df[['D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
            'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
            'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

    normality_dict = {}
    normality_kolm = {}
    normality_anderson = {}

    for col in all.columns:

        shapiro_res = shapiro(list(all[col]))
        normality_dict[col] = {col : shapiro_res}
        kolmon_res = kstest(list(all[col]), 'norm', alternative='less')
        normality_kolm[col] = {col: kolmon_res}
        anderson_res = anderson(list(all[col]))
        normality_anderson = {col:anderson_res}

        results_anderson = pd.DataFrame.from_dict(normality_anderson)

    results_kolm = pd.DataFrame.from_dict(normality_kolm)

    results_shap = pd.DataFrame.from_dict(normality_dict)
    results_shap.to_csv('Shapiro_res_compact.csv')
    results_kolm.to_csv('Kolmongorov.csv')
    results_anderson.to_csv('Anderson_less.csv')


