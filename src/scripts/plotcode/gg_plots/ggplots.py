import warnings
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.stats import f_oneway
from statsmodels.formula.api import ols
import pandas as pd
from plotnine import *
import matplotlib.pyplot as plt
from statsmodels.graphics.factorplots import interaction_plot

warnings.filterwarnings('ignore')
data = "/home/nopesferatu/Desktop/Thesis_R2_v2/analysis/data/o1_maybe_lates.xlsx"

df = pd.read_excel(data, sheet_name='INDIV_VAR_REG')

print(df.info())
df.head()

all = df[['D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group', 'AgeLabel','BSMAS_CAT','EducLabel',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth', 'TimeLabel','EmplLabel',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'YouTube_Index', 'Facebook', 'Instagram', 'TikTok','GenderL','BSMAS_CATER']]

variable_array = ['D1', 'D2', 'D3', 'D4', 'BSMAS']

for all_col in all.columns:
    for var in variable_array:
        p = (
            ggplot(df, aes(x=all_col, y=var, colour='BSMAS_CAT', group='BSMAS_CAT'))
            + geom_jitter(width=0.05)
            + stat_summary(fun_data="mean_cl_boot", geom="point", size=3)
            + stat_summary(fun_data="mean_cl_boot", geom="line")
            + scale_colour_brewer(type='qualitative', palette='Set1')

        )
        p.save(filename=f"ggplot_of_{all_col}_cont_var{var}.png")


