# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:26:24 2019

@author: ArchuBharathi
"""


import time
import concurrent.futures
import logging
from logging.config import fileConfig
from util.folder_traverse_util import folder_traverse
from  stream.daily_stock_price_mq import daily_stock_price_fetcher_mq
import pika
from pika.connection import ConnectionParameters
from pika import credentials as pika_credentials, BasicProperties
from pika.exceptions import AMQPError, ChannelClosed, ConnectionClosed

class orchestrator:

    def __init__(self):

        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='NSE', exchange_type='fanout')
        #self.channel.queue_declare(queue="NSE_NEW")

    def multi_file_get_quotes(self, stockListFolder):
        # multi processing of multiple files of quotes to scan
        ft = folder_traverse()
        files_to_scan_lst = ft.folder_nav_path(stockListFolder)
        self.log.info ('workflow streaming completed successfully...... ')
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for x in executor.map(self.get_live_quotes, files_to_scan_lst):
                self.log.debug("inside executor")
                pass
                #elf.log.debug("x")


# =============================================================================
        self.log.info ('stock screening/processing completed...... ')
        self.log.info ('Schedule Holding on for Next Run...... ')
        return


    def get_live_quotes(self,file_id):
# =============================================================================
#          For Each file
#             nse_stock_realtime_extract() object is created
#             file will be extracted and stock list will be passed as List
#
# =============================================================================
        get_stock_price = daily_stock_price_fetcher_mq(self.connection,self.channel,"NSE_NEW")
        self.log.debug("started Processing File FileID : "+ file_id)
        get_stock_price.main_workflow(file_id)
        self.log.info ('Streaming completed successfully for file.: '+file_id)
        #self.log.info(" waiting for other threads to complete... sleep for 10 sec ")
        #time.sleep(10)


        return "done"

def main():

    scanfolder = "D:\\nse_data\\scan_list_today\\"
    o = orchestrator()
    o.multi_file_get_quotes(scanfolder)
    o.log.info(" waiting for other all objects threads to complete... sleep for 10 sec ")
    time.sleep(10)
    #o.connection.close()

if __name__ == "__main__":
    main()


""" End -of class """
