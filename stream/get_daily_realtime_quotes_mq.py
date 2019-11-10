# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 12:48:16 2019

@author: ArchuBharathi
"""
import concurrent.futures
import time
from nsetools import Nse
import pandas as pd
import logging
from logging.config import fileConfig
import pika

class nse_stock_realtime_extract:
    """
        Extract Daily Stock market quotes in Real-Time
        Run this class whenever required in frequent manner
    """

    def __init__(self):
        self.json_stock_realtime_quotes = []
        self.nse = Nse()
        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')
        self.temoutfile = open("D:\\stocks_temp_file4.txt","a")


    def read_stock_scan_list(self, filename):
        """ Read the stocks to be scanned  """
        self.log.info("stock file used for scanning  :" + filename)
        # print(""filename)
        linelist = [line.rstrip('\n') for line in open(filename)]
        return linelist

    def nse_live_fetch(self, stockquote):
        """ Fetch Realtime nse stock details  """
        self.log.debug("Processing of url :" + stockquote)

        test_list = self.nse.get_quote(str(stockquote))

        self.json_stock_realtime_quotes.append(test_list)
        self.temoutfile.writelines(str(test_list)+"\n")

        return test_list
        #return self.nse.get_quote(str(stockquote))

    def get_current_day_quotes(self, stock_scan_list):
        """ concurrent processsing of Stock fetch from NSE websites"""
        self.log.debug("Concurrent processing of urls"
                       "in method get_current_day_quotes")
        #with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for x in executor.map(self.nse_live_fetch, stock_scan_list):
                #self.json_stock_realtime_quotes.append(x)
                self.log.info("Length of list"+str(len(self.json_stock_realtime_quotes)))
                #self.log.debug("X value"+str(x))

    def write_file_current_day_quotes(self, out_current_day_quotes_filename):
        """ convert the list to Datafframe
            write to CSV files
        """
        self.log.info("writing Realtime quotes to files")
        realtime_quotes_df = pd.DataFrame.from_dict(
                self.json_stock_realtime_quotes, orient='columns')
        realtime_quotes_df.to_csv(out_current_day_quotes_filename, header=True)
        # print(df)

    def fetch_curr_date_time(self):
        """ Fetch current Date & time"""
        curr_date_time = time.asctime(time.localtime(time.time()))
        curr_date_time = curr_date_time.replace(" ", "_")
        curr_date_time = curr_date_time.replace(":", "_")
        return curr_date_time

    def main_run(self,scan_list,output_path):
        """ Main method to flow the program"""
        start = time.time()
        fetchquotes = nse_stock_realtime_extract()
        fetchquotes.log.info("get_daily_realtime_quotes started")
        # stock_list_arr =['infy', 'HEG', 'HDFC', 'ABAN']
        stocklist = fetchquotes.read_stock_scan_list(scan_list)
        #       "d:\\scan_list_today\\stocklist_test50.txt")
        # print(stocklist)
        fetchquotes.get_current_day_quotes(stocklist)
        curr_dtime = fetchquotes.fetch_curr_date_time()
        output_file = output_path+"curr_day_quotes_"+curr_dtime+".csv"
        fetchquotes.log.info("live quotes output_file :" + output_file)
        fetchquotes.write_file_current_day_quotes(output_file)
        #        "d:\\Live_quotes_24042019\\curr_day_quotes_"+curr_dtime+".txt")
        print("Current time %s" + curr_dtime)
        fetchquotes.log.info("GetQuotes - Total RunTimeElapsed Time:"
                             "%ss" % (time.time() - start))
        self.temoutfile.flush()
        self.temoutfile.close()
        return output_file

if __name__ == "__main__":
    n = nse_stock_realtime_extract()
