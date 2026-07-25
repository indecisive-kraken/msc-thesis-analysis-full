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
all = df[['Q1','Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

distributions_set = get_common_distributions()
distributions_set.extend(['arcsine', 'cosine', 'expon', 'weibull_max', 'weibull_min',
                          'dweibull', 't', 'pareto', 'exponnorm', 'lognorm',
                         "norm", "exponweib", "weibull_max", "weibull_min", "pareto", "genextreme"])

# Remove duplicates
distributions_set = list(set(distributions_set))

# # Loop over all columns
# for col in tqdm(df.columns, desc="Fitting Distributions"):
#     print(f"\n=== Column: {col} ===")
#     try:
#         # Drop NaNs and ensure it's numeric
#         data_col = pd.to_numeric(df[col], errors='coerce').dropna()
#
#         # Skip if too few data points
#         if len(data_col) < 10:
#             print("Not enough data. Skipping...")
#             continue
#
#         f = Fitter(data_col, distributions=distributions_set)
#         f.fit()
#         f.summary()
#     except Exception as e:
#         print(f"Error fitting {col}: {e}")


for dist in distributions_set:
    try:
        f = Fitter(all, distributions=dist)
        f.fit()
        f.summary()
    except:
        print(f"Error, I dont know..")