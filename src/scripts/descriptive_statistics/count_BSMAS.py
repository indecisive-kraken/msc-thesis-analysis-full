import os
import numpy
import pandas as pd
from scripts.data.get_data_path import open_data_file

count_BSMAS():
    df = open_data_file().dropna()
    print(df.info())
    df.head()

    target_list = df['BSMAS']
    under_14 = 0
    from_14_to_24 = 0
    above_24 = 0

    for el in target_list:
        if el < 14:
            under_14 += 1
        elif el >= 14 and el < 24:
            from_14_to_24 += 1
        elif el >= 24:
            above_24 += 1

    print(under_14, from_14_to_24, above_24)

count_BSMAS()