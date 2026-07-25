import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
from scipy.stats import chi2
from numpy.linalg import inv
from scipy.stats import chi2, norm

# === Step 1: Simulate Multivariate Normal data ===
'''
 np.random.seed(42)
 data = np.random.multivariate_normal(mean, cov, size=n_samples)
 df = pd.DataFrame(data, columns=[f"Var{i+1}" for i in range(n_variables)])
'''
# Identity covariance (independent normal variables)
n_samples = 111
n_variables = 24
mean = np.zeros(n_variables)
cov = np.identity(n_variables)

data = input('Please specify the Excel file with the data: ')

df = pd.read_excel(data, sheet_name='ENCODED_DATA')
y = df['Q1']
x = df[['Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]


df = pd.DataFrame(data, columns=['Q1','Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N'])

def plot_univariate_qq(df):
    ...
    plt.tight_layout()
    plt.savefig("univariate_qq_plots.png", dpi=300)
    plt.close()


def plot_univariate_qq(df):
    n_cols = 4
    n_rows = int(np.ceil(len(df.columns) / n_cols))
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(16, 4 * n_rows))
    axes = axes.flatten()

    for i, col in enumerate(df.columns):
        stats.probplot(df[col], dist="norm", plot=axes[i])
        axes[i].set_title(f'Q-Q Plot: {col}')

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])  # remove unused subplots

    plt.tight_layout()
    plt.savefig("plot_name0.png", dpi=300, bbox_inches='tight')

def mardia_test(df):
    X = df.values
    n, p = X.shape
    mean = np.mean(X, axis=0)
    cov = np.cov(X, rowvar=False)
    inv_cov = np.linalg.inv(cov)

    # Centered data
    X_centered = X - mean

    # Mahalanobis distances
    D = np.dot(X_centered, inv_cov)
    D = np.einsum('ij,ij->i', D, X_centered)  # Squared Mahalanobis distances

    # Skewness
    skewness = np.sum([np.dot(np.dot(X_centered[i], inv_cov), X_centered[j]) ** 3
                       for i in range(n) for j in range(n)]) / (n ** 2)

    skew_stat = n * skewness / 6
    skew_p = 1 - chi2.cdf(skew_stat, df=int(p * (p + 1) * (p + 2) / 6))

    # Kurtosis
    kurtosis = np.mean(D ** 2)
    expected_kurt = p * (p + 2)
    kurt_z = (kurtosis - expected_kurt) / np.sqrt(8 * p * (p + 2) / n)
    kurt_p = 2 * (1 - norm.cdf(abs(kurt_z)))

    print("Mardia’s Multivariate Normality Test")
    print("-------------------------------------")
    print(f"Skewness: {skewness:.4f}, Test Stat: {skew_stat:.4f}, p-value: {skew_p:.4f}")
    print(f"Kurtosis: {kurtosis:.4f}, Z-score: {kurt_z:.4f}, p-value: {kurt_p:.4f}")

    if skew_p > 0.05 and kurt_p > 0.05:
        print("✅ data likely follows multivariate normal distribution.")
    else:
        print("⚠️ Potential deviation from multivariate normality.")

    return {
        "skewness_stat": skew_stat,
        "skewness_pval": skew_p,
        "kurtosis_stat": kurtosis,
        "kurtosis_pval": kurt_p
    }


def mahalanobis_qqplot(df):
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
    plt.savefig("plot_name2.png", dpi=300, bbox_inches='tight')

def plot_correlation_heatmap(df):
    plt.figure(figsize=(12, 10))
    sns.heatmap(df.corr(), annot=False, cmap='coolwarm', center=0)
    plt.title('Correlation Heatmap')
    plt.savefig("plot_name3.png", dpi=300, bbox_inches='tight')

# Visual checks
plot_univariate_qq(df)
mahalanobis_qqplot(df)
plot_correlation_heatmap(df)

# Mardia's test
mardia_results = mardia_test(df)


