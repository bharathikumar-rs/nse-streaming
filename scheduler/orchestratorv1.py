# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:26:24 2019

@author: ArchuBharathi
"""

from io import StringIO
import sys
import concurrent.futures
from nsetools import Nse
import pandas as pd
import logging
from logging.config import fileConfig
from stream.get_daily_realtime_quotes import nse_stock_realtime_extract
from exit_criteria.stock_exit_strategy_simple import stock_exit_strategy_simple
from exit_criteria.filemove import filemove
from util.folder_traverse_util import folder_traverse
class orchestrator:
    live_quotes_outpath = "D:\\nse_data\\live_quotes_curr_day\\"
    def __init__(self):

        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')

    def orchestrate_workflow(self,StockListFolder):
        #sell = stock_exit_strategy_simple()

        stock_scan_file = "D:\\nse_data\\scan_list_today\\stocklist_test50.txt"
        #live_quotes_outpath = "D:\\nse_data\\live_quotes_curr_day\\"
        currday_file =[]
        ft = folder_traverse()
        scan_quotes_files= ft.folder_nav_path(StockListFolder)

        #currday_file= currprice.main_run(stock_scan_file,live_quotes_path)
        # multi processing of multiple files of quotes to scan

        self.log.info ('workflow streaming completed successfully...... ')
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for x in executor.map(self.get_live_quotes, scan_quotes_files):
                self.log.debug("inside executor")
                self.log.debug("x")


# =============================================================================
        self.log.info ('stock screening/processing completed...... ')
        self.log.info ('Schedule Holding on for Next Run...... ')



    def get_live_quotes(self,fileList):
        outpath = self.live_quotes_outpath
        currprice = nse_stock_realtime_extract()
        self.log.info("outpath ind:"+outpath)
        self.log.info("File ind:"+fileList)
        currday_file= currprice.main_run(fileList,outpath)
        self.log.info ('Streaming completed successfully...... ')
        return currday_file

if __name__ == "__main__":
    main()

""" End -of class """
