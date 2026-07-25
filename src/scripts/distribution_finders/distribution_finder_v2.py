import os
import numpy as np
import pandas as pd
import scipy.stats as st
import statsmodels.api as sm
from scipy.stats import shapiro
from scipy import stats
from tqdm import tqdm
from fitter import Fitter, get_common_distributions
from dotenv import load_dotenv

load_dotenv()
data = os.getenv("DATA") 

df = pd.read_excel(data, sheet_name='ENCODED_DATA')

print(df.info())
df.head()

y = df['Q1']
x = df[['Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

distributions_set = get_common_distributions()
distributions_set.extend(['arcsine', 'cosine', 'expon', 'weibull_max', 'weibull_min',
                          'dweibull', 't', 'pareto', 'exponnorm', 'lognorm',
                         "norm", "exponweib", "weibull_max", "weibull_min", "pareto", "genextreme"])

for i in tqdm([0], unit='seconds', desc='Finding best distribution'):
    f = Fitter(df, distributions = distributions_set)
    f.fit()
    f.summary()