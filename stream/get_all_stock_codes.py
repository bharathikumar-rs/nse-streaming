# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:13:46 2019

@author: ArchuBharathi
"""

from nsetools import Nse
import pandas as pd
import logging
from logging.config import fileConfig


class get_all_stock_codes:

    """
        This class will retrive all Stock codes from NSE website
    """

    def __init__(self):
        self.all_stock_codes = []
        self.nse = Nse()
        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')

    def nsetools_get_codes(self, out_stock_file):
        """ This method retrivies all stock codes and write to CSV files
            Method uses NSETools to retrieve data from NSE website
        """
        self.log.info("Retriving stock Codes from NSE site .. ")
        self.all_stock_codes = self.nse.get_stock_codes()
        df2 = pd.DataFrame.from_dict(self.all_stock_codes, orient='index')
        self.log.info("Total Stock Codes received :" + str(df2.shape[0]))
        df2.to_csv(out_stock_file)


def main():
    getStock = get_all_stock_codes()
    getStock.nsetools_get_codes("D:\\stock_codes_D20042019.csv")


if __name__ == "__main__":
    main()

""" End -of class """
