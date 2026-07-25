import warnings
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.stats import f_oneway
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison

warnings.filterwarnings('ignore')
data = "/home/nopesferatu/Desktop/Thesis_R2_v2/analysis/data/o1_maybe_lates.xlsx"

df = pd.read_excel(data, sheet_name='INDIV_VAR_REG')

print(df.info())
df.head()

all = df[['D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group', 'AgeLabel','BSMAS_CAT','EducLabel',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth', 'TimeLabel','EmplLabel',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'YouTube_Index', 'Facebook', 'Instagram', 'TikTok','GenderL','BSMAS_CATE']]

variable_array = ['D1', 'D2', 'D3', 'D4']


for var in variable_array:
    modelGend = ols('{} ~ C(Gender) + C(BSMAS_CATE) + C(Gender):C(BSMAS_CAT)'.format(var), data=all).fit()
    modelInsta = ols('{} ~ C(Instagram_index) + C(BSMAS_CATE) + C(Instagram_index):C(BSMAS_CATE)'.format(var), data=all).fit()
    modelFacebook = ols('{} ~ C(Facebook_index) + C(BSMAS_CATE) + C(Facebook_index):C(BSMAS_CATE)'.format(var), data=all).fit()
    modelTikTok = ols('{} ~ C(TikTok_index) + C(BSMAS_CATE) + C(TikTok_index):C(BSMAS_CATE)'.format(var), data=all).fit()
    modelAge = ols('{} ~ C(AgeLabel) + C(BSMAS_CATE) + C(AgeLabel):C(BSMAS_CATE)'.format(var), data=all).fit()
    modelEduc = ols('{} ~ C(EducLabel) + C(BSMAS_CATE) + C(EducLabel):C(BSMAS_CATE)'.format(var), data=all).fit()
    modelEmploy = ols('{} ~ C(EmplLabel) + C(BSMAS_CATE) + C(EmplLabel):C(BSMAS_CATE)'.format(var), data=all).fit()
    modelTime = ols('{} ~ C(TimeLabel) + C(BSMAS_CATE) + C(TimeLabel):C(BSMAS_CATE)'.format(var), data=all).fit()

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

for var in variable_array:
    mc = MultiComparison(all[var], all['BSMAS_CATE'])
    mcresult = mc.tukeyhsd(0.05)
    print(mcresult.summary())