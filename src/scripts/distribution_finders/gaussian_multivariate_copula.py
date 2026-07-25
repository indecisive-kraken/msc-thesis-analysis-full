import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
from copulas.univariate import GaussianUnivariate
from sklearn.model_selection import train_test_split
from statsmodels.compat import lzip
from scipy.stats import shapiro
from statsmodels.formula.api import ols
from statsmodels.stats.stattools import omni_normtest
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.outliers_influence import variance_inflation_factor
from scipy import stats
from scipy.stats import spearmanr
from patsy import dmatrices
from copulas.multivariate import GaussianMultivariate
from sklearn.model_selection import train_test_split
import warnings
from dotenv import load_dotenv

warnings.filterwarnings('ignore')
load_dotenv()
data = os.getenv("DATA") 

df = pd.read_excel(data, sheet_name='ENCODED_DATA')

print(df.info())
df.head()

y = df['Q1']
X = df[['Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

try:
    dist = GaussianMultivariate(distribution=GaussianUnivariate)
    print(dist.fit(df))
except Exception as e:
    print(e)
#print(dist.fit(X_test, y_test))


