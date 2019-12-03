# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:26:24 2019

@author: ArchuBharathi
"""

from io import StringIO
import sys
import time
import concurrent.futures
import pandas as pd
import logging
from logging.config import fileConfig
from util.folder_traverse_util import folder_traverse
from  stream.daily_stock_price_yahoo_kafka import daily_stock_price_fetcher_kafka
import pika
from pika.connection import ConnectionParameters
from pika import credentials as pika_credentials, BasicProperties
from pika.exceptions import AMQPError, ChannelClosed, ConnectionClosed
from kafka import KafkaProducer
import json
class orchestrator:
    Total_msg_counter = 0
    threadlvl_msg_counter =0

    def __init__(self):

        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')
        self.connection = KafkaProducer(bootstrap_servers='localhost:9092'
                                        ,value_serializer=lambda v:json.dumps(v).encode('utf-8'))

    def multi_file_get_quotes(self, stockListFolder):
# =============================================================================
#       Collects the path to scan
#        reads all the files in folder and process them in Multi Threading
#
# =============================================================================
        ft = folder_traverse()
        files_to_scan_lst = ft.folder_nav_path(stockListFolder)

        self.log.info('Starting multi-File Threading process...... ')
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for x in executor.map(self.get_live_quotes, files_to_scan_lst):
                pass
        self.log.info("Total  Messages Processed:" +
                      str(orchestrator.threadlvl_msg_counter))
        return

    def get_live_quotes(self, file_id):
# =============================================================================
#          For Each file
#             nse_stock_realtime_extract() object is created
#             file will be extracted and stock list will be passed as List
#
# =============================================================================
        # change needed in group id 2/12/2019 identified bug fix reequired
        get_stock_price = daily_stock_price_fetcher_kafka(
                self.connection, "self.channel", "NSE_NEW")
        self.log.debug("started Processing File FileID : " + file_id)

        orchestrator.threadlvl_msg_counter = \
            get_stock_price.main_workflow(file_id)

        self.log.info('Streaming completed successfully for file.: ' + file_id)

        #self.log.info(" waiting for other threads to complete... sleep for 10 sec ")
        #time.sleep(10)
        return "done"

    def main():
    # =============================================================================
    #  Test Method Before scheduling
    # =============================================================================
        scanfolder = "D:\\nse_data\\scan_list_today\\"
        o = orchestrator()
        o.multi_file_get_quotes(scanfolder)
        o.log.info(" waiting for other all objects threads to complete... sleep for 10 sec ")
        time.sleep(10)
        #o.connection.close()


if __name__ == "__main__":

    o = orchestrator()
    time.sleep(10)
    o.log.info("waiting for other all objects threads to complete \
               ... sleep for 10 sec ")
    o.log.info("Total  Messages Processed:",
               str(orchestrator.threadlvl_msg_counter))

""" End -of class """
