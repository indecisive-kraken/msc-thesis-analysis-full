import warnings
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.stats import f_oneway
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison

warnings.filterwarnings('ignore')

def anova_twoway():
       
    data = "/home/nopesferatu/Desktop/Thesis_R2_v2/analysis/data/o1_maybe_lates.xlsx"

    df = pd.read_excel(data, sheet_name='INDIV_VAR_REG')

    print(df.info())
    df.head()

    all = df[['D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group', 'AgeLabel','BSMAS_CAT','EducLabel',
            'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth', 'TimeLabel','EmplLabel',
            'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'YouTube_Index', 'Facebook', 'Instagram', 'TikTok','GenderL','BSMAS_CATE']]

    variable_array = ['D1', 'D2', 'D3', 'D4']

    for var in variable_array:
        modelGend = ols('{} ~ C(Gender) + C(BSMAS_CAT) + C(Gender):C(BSMAS_CAT)'.format(var), data=all).fit()
        modelInsta = ols('{} ~ C(Instagram_index) + C(BSMAS_CAT) + C(Instagram_index):C(BSMAS_CAT)'.format(var), data=all).fit()
        modelFacebook = ols('{} ~ C(Facebook_index) + C(BSMAS_CAT) + C(Facebook_index):C(BSMAS_CAT)'.format(var), data=all).fit()
        modelTikTok = ols('{} ~ C(TikTok_index) + C(BSMAS_CAT) + C(TikTok_index):C(BSMAS_CAT)'.format(var), data=all).fit()
        modelAge = ols('{} ~ C(AgeLabel) + C(BSMAS_CAT) + C(AgeLabel):C(BSMAS_CAT)'.format(var), data=all).fit()
        modelEduc = ols('{} ~ C(EducLabel) + C(BSMAS_CAT) + C(EducLabel):C(BSMAS_CAT)'.format(var), data=all).fit()
        modelEmploy = ols('{} ~ C(EmplLabel) + C(BSMAS_CAT) + C(EmplLabel):C(BSMAS_CAT)'.format(var), data=all).fit()
        modelTime = ols('{} ~ C(TimeLabel) + C(BSMAS_CAT) + C(TimeLabel):C(BSMAS_CAT)'.format(var), data=all).fit()

        print()
        print("For variable {}:".format(var))
        print(sm.stats.anova_lm(modelGend, typ=2))
        print(sm.stats.anova_lm(modelInsta, typ=2))
        print(sm.stats.anova_lm(modelFacebook, typ=2))
        print(sm.stats.anova_lm(modelTikTok, typ=2))
        print(sm.stats.anova_lm(modelAge, typ=2))
        print(sm.stats.anova_lm(modelEduc, typ=2))
        print(sm.stats.anova_lm(modelEmploy, typ=2))
        print(sm.stats.anova_lm(modelTime, typ=2))

    print(" ----- For ANOVA oneway only BSMAS -----")
    BSmodelGend = ols('BSMAS_CATE ~ C(GenderL)', data=all).fit()
    BSmodelInsta = ols('BSMAS_CATE ~ C(Instagram)', data=all).fit()
    BSmodelFacebook = ols('BSMAS_CATE ~ C(Facebook)', data=all).fit()
    BSmodelTikTok = ols('BSMAS_CATE ~ C(TikTok)', data=all).fit()
    BSmodelAge = ols('BSMAS_CATE ~ C(AgeLabel)', data=all).fit()
    BSmodelEduc = ols('BSMAS_CATE ~ C(EducLabel)', data=all).fit()
    BSmodelEmploy = ols('BSMAS_CATE ~ C(EmplLabel)', data=all).fit()
    BSmodelTime = ols('BSMAS_CATE ~ C(TimeLabel)', data=all).fit()

    mod_arr = [BSmodelGend, BSmodelInsta, BSmodelFacebook, BSmodelTikTok, BSmodelAge, BSmodelEduc, BSmodelEmploy, BSmodelTime ]

    for modl in mod_arr:
        print(sm.stats.anova_lm(modl, typ=2))

    # - Tukey's Tests - after finding significance

    # Step 1: Keep only rows with valid 'D1' and 'BSMAS_CAT'
    clean_df = all[['D1','D2','D3','D4','BSMAS_CAT']].dropna(subset=['D1', 'BSMAS_CAT'])

    # Step 2: Convert BSMAS_CAT to string and filter out 'nan' strings
    clean_df['BSMAS_CAT'] = clean_df['BSMAS_CAT'].astype(str)

    # Remove any string 'nan' that might result from conversion
    clean_df = clean_df[clean_df['BSMAS_CAT'].str.lower() != 'nan']

    # Optional but good: make category explicit
    clean_df['BSMAS_CAT'] = pd.Categorical(clean_df['BSMAS_CAT'])

    for var in variable_array:

        tukey = pairwise_tukeyhsd(endog=clean_df[var], groups=clean_df['BSMAS_CAT'], alpha=0.05)
        print(tukey.summary())


        
# for var in variable_array:
#     tukey = pairwise_tukeyhsd(endog=all[var],
#                               groups=all['BSMAS_CATE'],
#                               alpha=0.05)
#     print(tukey)
#     mc = MultiComparison(all[var], all['BSMAS_CAT'])
#     mcresult = mc.tukeyhsd(0.05)
#     mcresult.summary()


