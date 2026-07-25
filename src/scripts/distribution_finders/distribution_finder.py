import os
import numpy as np
import pandas as pd
import scipy.stats as st
import statsmodels.api as sm
from scipy.stats import shapiro
from scipy import stats
from tqdm import tqdm

load_dotenv()
data = os.getenv("DATA") 
df = pd.read_excel(data, sheet_name='ENCODED_DATA')

print(df.info())
df.head()

names = []

# 2. -- Getting all the available distribution names from scipy to loop through the data to find the distribution
#       with the lowest p-value

for name in stats._distr_params.distcont:
    if name not in ['frechet_l', 'frechet_r']:
        names.append(name)

#- checking if it worked
print(names)

#3. Code from stack overflow : https://stackoverflow.com/questions/37487830/how-to-find-probability-distribution-and-parameters-for-real-data --Pasindu Tennage
#    --fixed line 30 because I ran into multiple errors
#    --sorted the dist_results array to see if there are any distributions with the same value, similar values
#      and in general to see the performance of the rest of the distributions.

def get_best_distribution(data):

    dist_results = []
    params = {}
    for dist_name in names:
        dist = getattr(st, str(dist_name))
        param = dist.fit(data)

        params[dist_name] = param

        #Application of the Kolmogorov-Smirnov Test
        D, p = st.kstest(data, dist_name, args=param)
        print("p value for "+dist_name +" = " + str(p))
        dist_results.append((dist_name, p))

    #selection of the best fitted distribution
    best_dist, best_p = (max(dist_results, key=lambda item: item[1]))

    #store the name of the best fit and its value
    print("Best fitting distribution: " + str(best_dist))
    print("Best p value: " + str(best_p))
    print("Parameters for the best fit: " + str(params[best_dist]))

    dist_results.sort()

    return best_dist, best_p, params[best_dist], dist_results

for i in tqdm([0], unit='seconds', desc='Finding best distribution'):
    get_best_distribution(df)