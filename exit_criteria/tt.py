# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:05:37 2019

@author: ArchuBharathi
"""
import os
import shutil
import pandas as pd

filedet= "D:\\nse_data\\Live_quotes_24042019\\curr_day_quotes_Wed_Apr_24_10_37_07_2019.txt"

df = pd.DataFrame(columns=['X', 'Y', 'Z'])
#df = pd.read_csv(filedet,
#             usecols = ['buyPrice1','buyPrice2'])

print(df)
df.loc[-1] = [2, 3,4]  # adding a row
df.index = df.index + 1  # shifting index
df = df.sort_index()  # sorting by index
print("after append")
print(df)