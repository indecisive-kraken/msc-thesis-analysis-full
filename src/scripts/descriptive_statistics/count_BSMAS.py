import os
import numpy
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
data = os.getenv("DATA")

df = pd.read_excel(data, sheet_name='ENCODED_DATA')
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