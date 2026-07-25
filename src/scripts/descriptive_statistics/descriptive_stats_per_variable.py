import numpy as np
import pandas as pd
import os
import warnings
from scipy import stats
from scipy.stats import mannwhitneyu
from pathlib import Path

from statistic_models.DescriptiveStats.desc_stats_per_interest_var import results_mann_w

results_mann_w = {}

data_desc_statistics = pd.read_excel("gend.xlsx",sheet_name="Sheet1")
stats_df = data_desc_statistics[["Mean", "Mode", "Std", "Mean_Males","Mode_Males","Std_Males"]]

for i in range(0,2):

    statistic, p_value = mannwhitneyu(stats_df.iloc[:, i], stats_df.iloc[:, i + 2], alternative='two-sided')

    results_mann_w[i] = {
        'Mann-Whitney U Statistic': statistic,
        'P-Value' : p_value
    }

    results_df = pd.DataFrame.from_dict(results_mann_w, orient='index')

    results_df.to_csv('mannwhitney_results_desc_stats_{}.csv'.format(i))

    print(results_df)

