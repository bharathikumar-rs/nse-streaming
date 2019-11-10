# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:40:23 2019

@author: ArchuBharathi
"""

from io import StringIO
import sys
from nsetools import Nse
import pandas as pd
import logging
from logging.config import fileConfig
from nsetools import Nse
import pika
import json
from pika.connection import ConnectionParameters
from pika import credentials as pika_credentials, BasicProperties
from pika.exceptions import AMQPError, ChannelClosed, ConnectionClosed
import concurrent.futures


class daily_stock_price_fetcher_kafka:

    queue_name = "NSE"
    queue_count = int(0)
    total_msg_counter = 0

    def __init__(self, connection, channel, routingkey):

        self.nse = Nse()
        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')
        self.connection = connection
        self.channel = channel
        self.routingkey = routingkey
        self._message_number_out = 0

    def read_stock_scan_list(self, filename):
# =============================================================================
#         """ Read the stock code from files and return a list  """
# =============================================================================
        self.log.debug("stock file used for scanning  :" + filename)
        linelist = [line.rstrip('\n') for line in open(filename) if line[:-1]]
        return linelist

    def nse_live_fetch(self, stockquote):
# =============================================================================
#        Fetch Realtime nse stock details
#        NSE.py module is modified please use that changes while updating
#        {PIP install NSE}
# =============================================================================
        self.log.debug("Processing of url :" + str(stockquote))
        response_json = ""
        try:
            response_json = self.nse.get_quote(str(stockquote))
            self.publish_kafka(str(response_json), stockquote)
        except BaseException as B:
            self.log.info("Exception Occured for: "+str(stockquote)+":"+str(B))

        return "done"

    def get_current_day_quotes(self, stock_scan_list):
# =============================================================================
#         concurrent processsing of Stock fetch from NSE websites
# =============================================================================
        self.log.debug("Concurrent processing of urls")

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            for x in executor.map(self.nse_live_fetch, stock_scan_list):
                pass

        return "done"

    def publish_kafka(self, message, stock_code):
# =============================================================================
#         publish the response json to Kafka queue
# =============================================================================
        if message.isspace():
            self.log.info("Response EMPTY for stockcode : %s" % (stock_code))
            return

        daily_stock_price_fetcher_kafka.total_msg_counter += 1

        self._message_number_out += 1

        self.connection.send(self.routingkey, message)
                            # json.dumps(message).encode('utf-8'))

        self.log.debug("Publish message #%s ,MSG : %s" %
                       (self._message_number_out, message))
        self.log.info("Publish message #%s,StockCode : %s " %
                      (self._message_number_out, stock_code))

    def main_workflow(self, filename):
# =============================================================================
#         Entry method and workflow orchestration method
# =============================================================================

        self.get_current_day_quotes(self.read_stock_scan_list(filename))
        self.log.info("All Stocks quotes published for FileId : "+filename)

        return daily_stock_price_fetcher_kafka.total_msg_counter


if __name__ == "__main__":
    dm = daily_stock_price_fetcher_kafka()