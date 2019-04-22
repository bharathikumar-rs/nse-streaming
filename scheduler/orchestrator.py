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

class orchestrator:

    def __init__(self):

        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')

    def orchestrate_workflow(self):
        #sell = stock_exit_strategy_simple()
        currprice = nse_stock_realtime_extract()
        currprice.main_run()

# =============================================================================
# def main():
#     o = orchestrator()
#     o.orchestrate_workflow()
# =============================================================================


if __name__ == "__main__":
    main()

""" End -of class """
