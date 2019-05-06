# -*- coding: utf-8 -*-
"""
Created on Fri May  3 20:20:34 2019

@author: ArchuBharathi
"""

from io import StringIO
import sys
from nsetools import Nse
import pandas as pd
import logging
from logging.config import fileConfig
from exit_criteria.stock_exit_strategy_simple import stock_exit_strategy_simple
from exit_criteria.filemove import filemove
from util.folder_traverse_util import folder_traverse
import concurrent.futures

class conctest:


    def __init__(self):
        self.nse = Nse()
        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')


    def concurrent_file_processor(self,file_list,purchase_file,decesion_outpath):
        print(purchase_file)
        print(decesion_outpath)
        print(file_list)
        self.log.debug ('Concurrent file processor started...... ')
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for x in executor.map(self.exit_strategy,file_list,purchase_file,decesion_outpath):
                self.log.debug("inside executor")
                self.log.debug("x"+str(x))

    def exit_strategy(self,curday_quotes_file,purchase_file,decesion_outpath):
        exitStrategy = stock_exit_strategy_simple()
        exitStrategy.main_run(curday_quotes_file, purchase_file,decesion_outpath)
        self.log.info ('Exit strategy completed...... ')


    def workflow_orchestrator(self,input_quotes_folder,purchase_file,decesion_file_path):
        ft = folder_traverse()
        #file_list = ft.folder_nav_path("D:\\nse_data\\live_quotes_today\\")
        file_list = ft.folder_nav_path(input_quotes_folder)
        self.concurrent_file_processor(file_list,purchase_file,decesion_file_path)

def main():
    decesion_file_path = "D:\\nse_data\\decision\\"
    purchase_file ="D:\\nse_data\\purchase_details\\purchase_price_details.csv"
    input_folder = "D:\\nse_data\\live_quotes_today\\"
    con = conctest()
    con.workflow_orchestrator(input_folder,purchase_file,decesion_file_path)

if __name__ == "__main__":
    main()

""" End -of class """
