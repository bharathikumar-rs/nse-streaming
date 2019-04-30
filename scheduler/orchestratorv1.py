# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:26:24 2019

@author: ArchuBharathi
"""

from io import StringIO
import sys
from nsetools import Nse
import pandas as pd
import logging
from logging.config import fileConfig
from stream.get_daily_realtime_quotes import nse_stock_realtime_extract
from exit_criteria.stock_exit_strategy_simple import stock_exit_strategy_simple
from exit_criteria.filemove import filemove

class orchestrator:

    def __init__(self):

        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')

    def orchestrate_workflow(self):
        #sell = stock_exit_strategy_simple()
        decesion_file_path = "D:\\nse_data\\decision\\"
        purchase_file ="D:\\nse_data\\purchase_details\\purchase_price_details.csv"
        stock_scan_file = "D:\\nse_data\\scan_list_today\\stocklist_test50.txt"
        live_quotes_path = "D:\\nse_data\\live_quotes_curr_day\\"
        live_quotes_archive_path = "D:\\nse_data\\live_quotes_today\\"
        currprice = nse_stock_realtime_extract()

        currday_file= currprice.main_run(stock_scan_file,live_quotes_path)
        self.log.info ('Streaming completed successfully...... ')


        self.log.info ('Exit strategy started...... ')
        exitStrategy = stock_exit_strategy_simple()
        exitStrategy.main_run(currday_file, purchase_file, decesion_file_path)
        self.log.info ('Exit strategy completed...... ')

        self.log.info ('file move in progress...... ')
        fmove = filemove()
        fmove.move(currday_file,live_quotes_archive_path)
        self.log.info ('file move completed...... ')

# =============================================================================
        self.log.info ('stock screening/processing completed...... ')
        self.log.info ('Schedule Holding on for Next Run...... ')

# =============================================================================
# =============================================================================
# def main():
#      o = orchestrator()
#      o.orchestrate_workflow()
# =============================================================================
# =============================================================================


if __name__ == "__main__":
    main()

""" End -of class """
