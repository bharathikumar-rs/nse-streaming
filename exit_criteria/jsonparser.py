# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:21:13 2019

@author: ArchuBharathi
"""

from io import StringIO
import sys
from nsetools import Nse
import pandas as pd
import logging
from logging.config import fileConfig

temoutfile = "D:\\stocks_temp_file3.txt"
linelist = [line for line in open(temoutfile)]


realtime_quotes_df = pd.DataFrame.from_dict(
                linelist, orient='columns')
realtime_quotes_df.to_csv("D:\\parseout1.csv", header=True)
