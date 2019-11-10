# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 22:19:15 2019

@author: ArchuBharathi
"""

from io import StringIO
import sys
from nsetools import Nse
import pandas as pd
import logging
from logging.config import fileConfig
import schedule
import time
from scheduler.orchestrator_yahoo_kafka import orchestrator
from exit_criteria.exit_criteria_sell import exit_criteria_sell
from exit_criteria.filemove import filemove
from exit_criteria import live_exit_strategy

class nsescheduler:

    def __init__(self):
        self.nse = Nse()
        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('scheduler intiated ')

    def get_live_data(self):
# =============================================================================
#   Schedule method to fetch live data -
#        Scheduled for every 30 mins
# =============================================================================
        stocks_to_scan_folder = "D:\\nse_data\\scan_list_today\\"
        self.log.info("Live data running ")
        o = orchestrator()
        o.multi_file_get_quotes(stocks_to_scan_folder)
        return

    def exit_criteria_run(self):
        self.log.info("Schedule for Exit criteria started")
        print("schedule is running about to trigger exit strat")
        Quotes_curr_folder = "D:\\nse_data\\live_quotes_today\\"
        decesion_file_path = "D:\\nse_data\\decision\\"
        purchase_file = "D:\\nse_data\\purchase_details\\purchase_price_details.csv"
        e = exit_criteria_sell()
        e.exit_criteria_processor(Quotes_curr_folder,purchase_file,decesion_file_path)

    def consume(self):
        consume = live_exit_strategy()
        consume.consume_topic()

    def file_copy(self):

        self.log.info ('file move in progress...... ')
        live_quotes_archive_folder = "D:\\nse_data\\History\\Moved\\"
        Quotes_curr_folder = "D:\\nse_data\\live_quotes_today\\"

        fmove = filemove()
        fmove.folder_content_move(Quotes_curr_folder,live_quotes_archive_folder)
        self.log.info ('file move completed...... ')

def main():
    sc = nsescheduler()
    print ("Schedule Started ................")
    sc.get_live_data()
    #sc.consume()
    #sc.exit_criteria_run()
    #sc.file_copy()
    #schedule.every().hour.do(sc.schedule_run())

    schedule.every(5).seconds.do(sc.get_live_data)
    #schedule.every().hour.do(sc.schedule_run)
    print ("Continuing with next run")


    while True:
    	#Checks whether a scheduled task
    	#is pending to run or not
    	schedule.run_pending()
    	time.sleep(10)


if __name__ == "__main__":
    main()

""" End -of class """
