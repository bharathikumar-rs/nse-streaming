# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 10:28:00 2019

@author: ArchuBharathi
"""

from io import StringIO
import sys
from nsetools import Nse
import pandas as pd
import logging
from logging.config import fileConfig
from exit_criteria.stock_exit_strategy_simple import stock_exit_strategy_simple

class stock_exit_strategy_simple_test:

    def __init__(self):

        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')



def main():
    s = stock_exit_strategy_simple_test()
    decesion_file_path = "D:\\nse_data\\decision\\"
    purchase_file ="D:\\nse_data\\purchase_details\\purchase_price_details.csv"
    currday_file = "D:\\nse_data\\live_quotes_curr_day\\curr_day_quotes_Fri_Apr_26_12_23_38_2019.csv"
    s.log.info ('Exit strategy started...... ')
    exitStrategy = stock_exit_strategy_simple()
    exitStrategy.main_run(currday_file, purchase_file, decesion_file_path)
    s.log.info ('Exit strategy completed...... ')


if __name__ == "__main__":
    main()

""" End -of class """
