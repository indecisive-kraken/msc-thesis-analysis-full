import numpy as np
import matplotlib.pyplot as plt
from scripts.data.get_data_path import open_data_file

def histogram():

    df = open_data_file()
    # Apply log transformation (with np.log1p to handle zero values)
    df['log_D1'] = np.log1p(df['D1'])
    df['log_D2'] = np.log1p(df['D2'])
    df['log_D3'] = np.log1p(df['D3'])
    df['log_D4'] = np.log1p(df['D4'])
    df['log_BSMAS'] = np.log1p(df['BSMAS'])

    # Plot the histograms of the log-transformed variables
    fig, axes = plt.subplots(3, 2, figsize=(12, 10))

    axes[0, 0].hist(df['D1'], bins=20, color='skyblue', edgecolor='black')
    axes[0, 0].set_title('D1')

    axes[0, 1].hist(df['D2'], bins=20, color='skyblue', edgecolor='black')
    axes[0, 1].set_title('D2')

    axes[1, 0].hist(df['D3'], bins=20, color='skyblue', edgecolor='black')
    axes[1, 0].set_title('D3')

    axes[1, 1].hist(df['D4'], bins=20, color='skyblue', edgecolor='black')
    axes[1, 1].set_title('D4')

    axes[2, 0].hist(df['BSMAS'], bins=20, color='skyblue', edgecolor='black')
    axes[2, 0].set_title('BSMAS')

    # Adjust layout
    plt.tight_layout()
    plt.savefig('histplot-nonlogtransformed.png', dpi=300, bbox_inches='tight')

histogram()