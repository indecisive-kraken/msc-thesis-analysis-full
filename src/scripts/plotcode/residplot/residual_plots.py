import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import plot_regress_exog
from scripts.data.get_data_path import open_data_file

def residual_plots():

    df = open_data_file()
    print(df.info())

    model = smf.ols('D1 ~ D2 + D3 + D4 + BSMAS',df).fit()
    model2 =  smf.ols('D2 ~ D1 + D3 + D4 + BSMAS',df).fit()
    model3 = smf.ols('D3 ~ D1 + D2 + D4 + BSMAS',df).fit()
    model4 = smf.ols('D4 ~ D1 + D2 + D3 + BSMAS',df).fit()

    fig1 = plt.figure(figsize=(14, 8))
    fig1 = sm.graphics,plot_regress_exog(model, 'D2', fig=fig1)

    plt.savefig('residplot-D2.png')

    fig2 = plt.figure(figsize=(14, 8))
    fig2 = sm.graphics, plot_regress_exog(model2, 'D1', fig=fig2)

    plt.savefig('residplot-D1.png')


residual_plots()