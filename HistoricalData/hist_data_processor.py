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

class hist_data_processor:


    l = []

    def __init__(self):
        self.nse = Nse()
        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')
        #self.df = pd.DataFrame(columns=['SYMBOL','SERIES','OPEN','HIGH','LOW','CLOSE','LAST','PREVCLOSE','TOTTRDQTY','TOTTRDVAL','TIMESTAMP','TOTALTRADES','ISIN','unname'])
        self.df =pd.DataFrame()


    def read_hist_csv(self,source_dir):
        file_list = glob.glob(source_dir + '/*.csv')
        data = []

        for file_path in file_list:
           # linelist =[line.rstrip("\n") for line in open(file_path) if line[:-1]]
            tempdf = pd.read_csv(file_path,
                                 usecols =
                                 ['SYMBOL','SERIES','OPEN','HIGH',
                                  'LOW','CLOSE','LAST','PREVCLOSE',
                                  'TOTTRDQTY','TOTTRDVAL','TIMESTAMP',
                                  'TOTALTRADES','ISIN'])

            self.df=self.df.append(tempdf,ignore_index = True,)
            #print(self.df)
            tempdf.drop

            #data.append(linelist)
        #    data.append(np.genfromtxt(file_path,StringIO(data), delimiter=',', skip_header=1,autostrip=True))
        # now you can access it outside the "for loop..."
            #df2 = pd.read_csv(file_path)
        #df2 = pd.DataFrame.from_dict(data,orient='columns')
        self.df.to_csv("D:\\nse_data\\History\\HistoricalCSV\\merged.csv")
        #print (df2)
     #   for d in data:
      #      print(d)

def main():
    h =  hist_data_processor()
    h.read_hist_csv("D:\\nse_data\\History\\HistoricalCSV\\")

if __name__ == "__main__":
    main()

""" End -of class """
