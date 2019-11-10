# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:05:37 2019

@author: ArchuBharathi
"""
import os
import shutil
import pandas as pd
from datetime import datetime
from nsetools import Nse
import json
print (str(datetime.now()))
filedet= "D:\\nse_data\\Live_quotes_24042019\\curr_day_quotes_Wed_Apr_24_10_37_07_2019.txt"

df = pd.DataFrame(columns=['X', 'Y', 'Z'])
#df = pd.read_csv(filedet,
#             usecols = ['buyPrice1','buyPrice2'])




nse = Nse()
tst = nse.get_quote('PRAKASHSTL')
print(tst)


"""

print(df)
df.loc[-1] = [2, 3,4]  # adding a row
df.index = df.index + 1  # shifting index
df = df.sort_index()  # sorting by index
print("after append")
print(df)

df.loc[df['X'] == '2']
print("selected :",df)

s = str({"sellQuantity5": None})
z = s.replace("None",'\"''None''\"')
print(z)


if len(z) > 6:
    print("its valid")
if z.__contains__("None"):

    print("String has none")

lst =[]
nse = Nse()
tst = nse.get_quote('infy')
print( type(tst))
lst.append(tst)
tst = nse.get_quote('HEG')
lst.append(tst)
df = pd.DataFrame.from_dict(
                lst, orient='columns')
#df = df.iloc[0:0]

symbol = df.iloc[0]['symbol']
temp_df = df.loc[df['symbol'] == "symbol"]

print ("Temp_df",temp_df)
print ("======================")

ttt = df.loc[df['symbol'] == symbol]
il= df.iloc[0]['symbol']



symb = ttt['symbol']
print ("Symbol value is ",il)



d ={}
d["Name"] = "Luje"
d["AGe"] ="12"


jobj = json.dumps(d, ensure_ascii=False)
print (jobj)

"""


