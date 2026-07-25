import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
from scipy.stats import chi2
from numpy.linalg import inv
from scipy.stats import chi2, norm

class mahalanobis_qqplot():

    def malahabosis_qq(df):

        script_dir = os.path.dirname(__file__)
        X = df.values
        mean_vec = np.mean(X, axis=0)
        cov_mat = np.cov(X, rowvar=False)
        inv_covmat = inv(cov_mat)

        # Compute Mahalanobis distances
        md_squared = np.array([np.dot(np.dot((x - mean_vec), inv_covmat), (x - mean_vec).T) for x in X])

        # Chi-squared quantiles
        chi2_q = chi2.ppf((np.arange(1, len(md_squared)+1) - 0.5) / len(md_squared), df.shape[1])

        # Sort for Q-Q plot
        md_sorted = np.sort(md_squared)

        plt.figure(figsize=(8, 6))
        plt.plot(chi2_q, md_sorted, 'o', label='Observed vs. Theoretical')
        plt.plot(chi2_q, chi2_q, 'r--', label='Ideal Fit')
        plt.xlabel('Chi-squared Quantiles')
        plt.ylabel('Ordered Mahalanobis Distances²')
        plt.title('Mahalanobis Q-Q Plot')
        plt.legend()
        plt.grid(True)

        results_dir = os.path.join(script_dir, 'results/')
        if not os.path.isdir(results_dir):
            os.makedirs(results_dir)

        plt.savefig(os.path.join(results_dir, 'plot.png'),"plot_name2.png", dpi=300, bbox_inches='tight')