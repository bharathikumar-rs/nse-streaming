# -*- coding: utf-8 -*-
"""
Created on Sun May 12 19:52:13 2019

@author: ArchuBharathi
"""

from io import StringIO
from nsetools import Nse
import pandas as pd
import urllib.request
import datetime
import pandas as pd
import time


bhavcopy_base_url = "https://www.nseindia.com/content/historical/EQUITIES/%s/%s/cm%s%s%sbhav.csv.zip"
base_url = 'https://in.finance.yahoo.com/quote/WHIRLPOOL.NS?p=WHIRLPOOL.NS&.tsrc=fin-srch'
file_path = 'D:\\nse_data\\History\\yahoo1.txt'

# Date Generator with weekdays
start = datetime.datetime(2019, 1, 8)
end = datetime.datetime(2019, 1, 9)
weekmask = 'Mon Tue Wed Thu Fri'
#date_lst = pd.bdate_range(start, end, freq='C', weekmask=weekmask)
#print(date_lst)


#url = base_url % (year, mon, day_of_month, mon, year)
url = base_url
print (url)
filename = file_path
#print (filename)
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)
urllib.request.urlretrieve(url, filename)
print("completed")

