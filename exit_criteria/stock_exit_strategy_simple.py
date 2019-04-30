# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 08:54:42 2019

@author: ArchuBharathi
"""

from io import StringIO
import sys
from nsetools import Nse
import pandas as pd
import logging
from logging.config import fileConfig
import time
from util.folder_traverse_util import folder_traverse

class stock_exit_strategy_simple:

    def __init__(self):
        self.nse = Nse()
        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('stock_exit_strategy_simple intiated ')

    def fetch_curr_date_time(self):
        """ Fetch current Date & time"""
        curr_date_time = time.asctime(time.localtime(time.time()))
        curr_date_time = curr_date_time.replace(" ", "_")
        curr_date_time = curr_date_time.replace(":", "_")
        return curr_date_time


    def process_exit_criteria(self, curr_stock_price_fname ,pur_stock_price_fname,outputfile):
        """
            Selling logic Simple as of now
            profit  = (Buying_price -  LTP) - agent_trade_cost
            if profit%  =  negative and > -20 % sell
            if profit%  = positive  and > 20 % sell

            Dynamic Decision (Safe play)
                If /selling rrate & TradeQuantity_high & Selling price is low
                    profit drops < 15% sell

        """
        self.log.info("Evaluating  exit criteria....")
        #self.log.info("Stock File in Evaluation ..: "+filename)
        df = pd.read_csv(curr_stock_price_fname,
             usecols = ['buyPrice1','buyPrice2','buyPrice3','buyPrice4',
                        'buyPrice5','buyQuantity1','buyQuantity2',
                        'buyQuantity3','buyQuantity4','buyQuantity5',
                        'change','companyName','dayHigh','dayLow','high52',
                        'lastPrice','low52','open','pChange','previousClose',
                        'pricebandlower','pricebandupper','quantityTraded',
                        'sellPrice1','sellPrice2','sellPrice3','sellPrice4',
                        'sellPrice5','sellQuantity1','sellQuantity2',
                        'sellQuantity3','sellQuantity4','sellQuantity5',
                        'symbol','totalBuyQuantity','totalSellQuantity',
                        'totalTradedValue','totalTradedVolume','varMargin'
                        ])

        agent_fee_prchase = 50.00
        agent_fee_sell  = 50.00

        purchase_price_df = pd.read_csv(pur_stock_price_fname)
        out_df = pd.DataFrame(columns=['Symbol', 'lastPrice', 'Total_profit'
                                            ,'profit_per','Decision'])
        # Exit /Selling criteria

        for df_row in range(len(df)) :
            #for pp_row in range(len(purchase_price_df)):
            if (df.iloc[df_row, 15] > purchase_price_df.iloc[df_row,4]):
            # current price * total quantity purchase
            # total profit  = currprice * quantity - agenfee -total purchase price
                total_profit = df.iloc[df_row, 15] * purchase_price_df.iloc[df_row,2]
                total_profit = \
                total_profit - (agent_fee_prchase + agent_fee_sell) - purchase_price_df.iloc[df_row,5]
                profit_per = total_profit /100
                if(profit_per > 20):
                    """
                    print(str(df.iloc[df_row, 33]), str(df.iloc[df_row, 15])\
                    + " Profit Sell |" + str(total_profit) +"|" +str(profit_per))
                    """
                    out_df.loc[-1] = [str(df.iloc[df_row, 33]), str(df.iloc[df_row, 15])
                    ,str(total_profit),str(profit_per),"Profit Sell"]  # adding a row
                    out_df.index = out_df.index + 1  # shifting index
                    out_df = out_df.sort_index()  # sorting by index

        out_df.to_csv(outputfile, header=True)

    def main_run(self,currday_file,purchase_file,outputpath):
        start = time.time()

        exit_strategy = stock_exit_strategy_simple()
        curr_dtime = exit_strategy.fetch_curr_date_time()
        exit_strategy.log.info("Exit Strategy Module Started...")
        #ft = folder_traverse()
        #filename = ft.folder_nav_path('D:\\Live_quotes')

        #exit_strategy.process_exit_criteria('D:\\Live_quotes\\curr_day_quotes.csv',\
        #                                    'D:\\Live_quotes\\purchase_price_details.csv')
        outputfile = outputpath + "_Decision_"+curr_dtime+".csv"
        exit_strategy.process_exit_criteria(currday_file,purchase_file,outputfile)

        exit_strategy.log.info("exit_strategy - Total RunTimeElapsed Time:"
                             "%ss" % (time.time() - start))


if __name__ == "__main__":
    e = stock_exit_strategy_simple()
    #main()

""" End -of class """
