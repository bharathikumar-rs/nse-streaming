# -*- coding: utf-8 -*-
"""
Created on Fri May 17 12:40:11 2019

@author: ArchuBharathi
"""

from io import StringIO
import sys
from nsetools import Nse
import pandas as pd
import logging
from logging.config import fileConfig
import numpy as np
import glob
from talib import abstract
from talib.abstract import *
import matplotlib.pyplot as plt

class hist_data_processor:


    l = []

    def __init__(self):
        self.nse = Nse()
        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')
        #self.df = pd.DataFrame(columns=['SYMBOL','SERIES','OPEN','HIGH','LOW','CLOSE','LAST','PREVCLOSE','TOTTRDQTY','TOTTRDVAL','TIMESTAMP','TOTALTRADES','ISIN','unname'])
        self.df =pd.DataFrame()
        self.symbol_to_scan = 'DCMSHRIRAM'


    def read_hist_csv(self,source_dir):
        file_list = glob.glob(source_dir + '/*.csv')
        data = []
        parse_dates = ['TIMESTAMP']
        for file_path in file_list:
           # linelist =[line.rstrip("\n") for line in open(file_path) if line[:-1]]
            tempdf = pd.read_csv(file_path,
                                 usecols =
                                 ['SYMBOL','OPEN','HIGH','LOW',
                                  'CLOSE','LAST','TOTTRDQTY',
                                  'TIMESTAMP'],dtype={"TOTTRDQTY": float}
                                 ,parse_dates=parse_dates)

            sma_df = tempdf[tempdf.SYMBOL == self.symbol_to_scan]

            sma_df.rename(columns = {'TOTTRDQTY':'volume'}, inplace = True)

            # required for ta-lib to detect column names as they are lower case
            sma_df.columns = map(str.lower, sma_df.columns)
            # descending order latest by date for TA-lib processing to be accurate
            sma_df = sma_df.sort_values('timestamp',ascending=True)


            #print(sma_df)
            #talib functions instantiation

            SMA = abstract.SMA
            OBV =abstract.OBV
            AD =abstract.AD
            # takes close
            #sma_daily_close = SMA(input_arrays, timeperiod=25, price='open') # calculate on opens
            sma_daily_close_60 = SMA(sma_df, timeperiod=60) # calculate on close prices by default
            sma_df['SMA_60_close'] = np.array(sma_daily_close_60)

            #SMA Daily close 20 days
            sma_daily_close_20 = SMA(sma_df, timeperiod=20) # calculate on close prices by default
            sma_df['SMA_20_close'] = np.array(sma_daily_close_20)
            print(sma_daily_close_20)

            # Volume indicators - OBV
            obv_list = OBV(sma_df)
            sma_df['OBV'] =  np.array(obv_list)
            ad_list = AD(sma_df)
            sma_df['AD LINE'] =  np.array(ad_list)

            sma_df.to_csv("D:\\nse_data\\History\\test\\"+self.symbol_to_scan+".csv")


            datelist = pd.date_range(pd.datetime.today(), periods=80).tolist()

            y = obv_list
            x = datelist
            #plt.p.sin(x)title("sine wave form")

            # Plot the points using matplotlib
            plt.plot(x, y)

            plt.imshow(x, aspect='auto')
            #plt.show()
            plt.savefig('D:\\nse_data\\obv2.png')







            #data.append(linelist)
        #    data.append(np.genfromtxt(file_path,StringIO(data), delimiter=',', skip_header=1,autostrip=True))
        # now you can access it outside the "for loop..."
            #df2 = pd.read_csv(file_path)
        #df2 = pd.DataFrame.from_dict(data,orient='columns')

        #print (df2)
     #   for d in data:
      #      print(d)

def main():
    h =  hist_data_processor()
    h.read_hist_csv("D:\\nse_data\\History\\test1\\")

if __name__ == "__main__":
    main()

""" End -of class """
