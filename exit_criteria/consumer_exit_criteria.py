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
from kafka import KafkaConsumer
from kafka.errors import KafkaError
class consume_json_parser:

    decesion_file_path = ""
    purchase_file =""

    def __init__(self):
        self.nse = Nse()
        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')


    def exit_criteria_processor(self,c_topic_name,group_id):
        self.log.debug ('Message processing started...... ')

        consumer = KafkaConsumer(c_topic_name, bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='latest', enable_auto_commit=True,
                         auto_commit_interval_ms=1000, group_id=group_id)
                        # value_deserializer=lambda m: json.loads(m.decode('utf-8')))

        for message in consumer:
                print (message.value)
                parse = nse_json_parser()
                parse.json_to_df(message.value)
                json_stock_realtime_quotes = message.value


        self.decesion_file_path = decesion_file_path
        self.purchase_file = purchase_file

        with concurrent.futures.ThreadPoolExecutor() as executor:
            for x in executor.map(self.exit_strategy,file_list):
                self.log.debug("inside executor")
                self.log.debug("x"+str(x))

    def exit_strategy(self,curday_quotes_file):
        print("Currfile :"+curday_quotes_file)
        exitStrategy = stock_exit_strategy_simple()
        exitStrategy.main_run(curday_quotes_file, self.purchase_file,self.decesion_file_path)
        #self.log.info ('Exit strategy completed...... ')
        return "done"

"""
    def main():

        input_folder = "D:\\nse_data\\live_quotes_today\\"
        con = conctest()
        decesion_file_path = "D:\\nse_data\\decision\\"
        purchase_file ="D:\\nse_data\\purchase_details\\purchase_price_details.csv"

        con.exit_criteria_processor(input_folder,purchase_file,decesion_file_path)
"""
if __name__ == "__main__":
    #main()
    n = exit_criteria_sell()

""" End -of class """
