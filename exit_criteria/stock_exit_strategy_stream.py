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
from datetime import datetime
import json
class stock_exit_strategy_simple:

    total_sell_counter = 0
    def __init__(self,kafka_connection):
        self.nse = Nse()
        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('stock_exit_strategy_simple intiated ')
        self._message_number_out = 0
        self.connection = kafka_connection
    def fetch_curr_date_time(self):
        """ Fetch current Date & time"""
       # curr_date_time = time.asctime(time.localtime(time.time()))
        curr_date_time = str(datetime.now())
        curr_date_time = curr_date_time.replace(" ", "_")
        curr_date_time = curr_date_time.replace(":", "_")
        return curr_date_time


    def process_exit_criteria_yahoo(self, df):

# =============================================================================
#     Selling logic Simple as of now
#        profit  = (Buying_price -  LTP) - agent_trade_cost
#        positive Sell
#      ==================
#        if profit%  =  negative and > -20 % sell
#            if profit%  = positive  and > 20 % sell
#        negative_sell (Mitigate_Loss)
#      ==================
#              Dynamic Decision (Safe play)
#                If /selling rrate & TradeQuantity_high & Selling price is low
#                    profit drops < 15% sell
#   note:    Implemented only positive sell
# =============================================================================



        # Load purchase price Note have to send as Dataframe
        #print(df)
        pur_stock_price_fname = \
            "D:\\nse_data\\purchase_details\\purchase_price_details_test_v2.csv"
        self.log.debug("purchase file use.."+pur_stock_price_fname)

        purchase_price_df = pd.read_csv(pur_stock_price_fname)
        #print("columns are: ",purchase_price_df.columns.tolist())
        #print(df.iloc[0,1])
        #Symbol = df.iloc[1]['symbol']
        Symbol = df.iloc[0,1]

        self.log.info("Processing Exit criteria for stock..." + Symbol)

        temp_df = purchase_price_df.loc[purchase_price_df['Symbol'] == Symbol]

        if not temp_df.empty:

         #   print ("TempDF:",temp_df)
            #self.log.debug("Temp_df Created from purchase_price ....."+ temp_df)

            agent_fee_prchase = 50.00
            agent_fee_sell = 50.00
            last_price = df.iloc[0, 0]
            purchased_quantity = temp_df.iloc[0, 2]

            #  from csv(qty*purchprice) adjust field id post test
            purchase_price = temp_df.iloc[0, 1]

            total_purchased_price = purchase_price * purchased_quantity
            brokerage_charges = agent_fee_prchase + agent_fee_sell

            # Exit /Selling criteria
            #if (df.iloc[0, 15] > temp_df.iloc[0, 1]):
            if (last_price > purchase_price):
                total_profit = last_price * purchased_quantity
                total_profit = (total_profit - brokerage_charges) - total_purchased_price
                profit_per = (total_profit / total_purchased_price) * 100
                #print (profit_per)
                self.log.info ("Symbol:"+Symbol+" | purch_price:"+str(purchase_price)+
                       " | Last_price:"+str(last_price) + "| Profit_%: "+str(profit_per ))

                if(profit_per > 10):
                    profit_data = {}
                    profit_data["symbol"] = Symbol
                    profit_data["purchase_price"] = purchase_price
                    profit_data["purchased_quantity"] = purchased_quantity
                    profit_data["last_price"] = last_price
                    profit_data["total_profit_amount"] = total_profit
                    profit_data["profit_perc"] = profit_per
                    profit_data["Decision"] = "Sell"
                    profit_data["sell_Indicator"] = "Positive"

                    #profit_json = json.dumps(profit_data, ensure_ascii=False)
                    profit_json = json.dumps(profit_data)
                    self.log.info("profitable stock ....." + str(profit_data))
                    self.publish_profit(profit_json, Symbol)
                    profit_data.clear()
                    del profit_json
            # clean all intermediate variable & dataframes
            temp_df = temp_df.iloc[0:0]
            del temp_df
        return "done"

    def process_exit_criteria(self, df1):

# =============================================================================
#     Selling logic Simple as of now
#        profit  = (Buying_price -  LTP) - agent_trade_cost
#        positive Sell
#      ==================
#        if profit%  =  negative and > -20 % sell
#            if profit%  = positive  and > 20 % sell
#        negative_sell (Mitigate_Loss)
#      ==================
#              Dynamic Decision (Safe play)
#                If /selling rrate & TradeQuantity_high & Selling price is low
#                    profit drops < 15% sell
#   note:    Implemented only positive sell
# =============================================================================


        # Select only the required columns and drop the original Dataframe to
        # reduce memory footprint
        df = df1[['buyPrice1', 'buyPrice2', 'buyPrice3', 'buyPrice4',
                  'buyPrice5', 'buyQuantity1', 'buyQuantity2',
                  'buyQuantity3', 'buyQuantity4', 'buyQuantity5',
                  'change', 'companyName', 'dayHigh', 'dayLow', 'high52',
                  'lastPrice', 'low52', 'open', 'pChange', 'previousClose',
                  'pricebandlower', 'pricebandupper', 'quantityTraded',
                  'sellPrice1', 'sellPrice2', 'sellPrice3', 'sellPrice4',
                  'sellPrice5', 'sellQuantity1', 'sellQuantity2',
                  'sellQuantity3', 'sellQuantity4', 'sellQuantity5',
                  'symbol', 'totalBuyQuantity', 'totalSellQuantity',
                  'totalTradedValue', 'totalTradedVolume', 'varMargin'
                 ]]

        df1 = df1.iloc[0:0]   # drop the entire df
        #print(df)
        del df1
        # Load purchase price Note have to send as Dataframe
        pur_stock_price_fname = \
            "D:\\nse_data\\purchase_details\\purchase_price_details_test_v2.csv"
        self.log.debug("purchase file use.."+ pur_stock_price_fname)

        purchase_price_df = pd.read_csv(pur_stock_price_fname)
        #print("columns are: ",purchase_price_df.columns.tolist())
        Symbol = df.iloc[0]['symbol']
        self.log.info("Processing Exit criteria for stock..." + Symbol)

        temp_df = purchase_price_df.loc[purchase_price_df['Symbol'] == Symbol]

        if not temp_df.empty:

            print ("TempDF:",temp_df)
          #  self.log.debug("Temp_df Created from purchase_price ....."+ temp_df)

            agent_fee_prchase = 50.00
            agent_fee_sell = 50.00
            last_price = df.iloc[0, 15]
            purchased_quantity = temp_df.iloc[0, 2]

            #  from csv(qty*purchprice) adjust field id post test
            purchase_price = temp_df.iloc[0, 1]
            print (purchase_price,last_price)
            total_purchased_price = purchase_price * purchased_quantity
            brokerage_charges = agent_fee_prchase + agent_fee_sell

            # Exit /Selling criteria
            #if (df.iloc[0, 15] > temp_df.iloc[0, 1]):
            if (last_price > purchase_price):
                total_profit = last_price * purchased_quantity
                total_profit = (total_profit - brokerage_charges) - total_purchased_price
                profit_per = (total_profit / total_purchased_price) * 100
                print (profit_per)
                if(profit_per > 10):
                    profit_data = {}
                    profit_data["symbol"] = Symbol
                    profit_data["purchase_price"] = purchase_price
                    profit_data["purchased_quantity"] = purchased_quantity
                    profit_data["last_price"] = last_price
                    profit_data["total_profit_amount"] = total_profit
                    profit_data["profit_perc"] = profit_per
                    profit_data["Decision"] = "Sell"
                    profit_data["sell_Indicator"] = "Positive"

                    #profit_json = json.dumps(profit_data, ensure_ascii=False)
                    profit_json = json.dumps(profit_data)
                    self.log.info("profitable stock ....." + str(profit_data))
                    self.publish_profit(profit_json, Symbol)
                    profit_data.clear()
                    del profit_json
            # clean all intermediate variable & dataframes
            temp_df = temp_df.iloc[0:0]
            del temp_df
        return "done"

    def publish_profit(self, message, symbol):
# =============================================================================
#   publish the profit sell message to kafka queue.
# =============================================================================

        stock_exit_strategy_simple.total_sell_counter += 1

        self._message_number_out += 1

        self.connection.send("NSE_Sell_Profit", message)
                            # json.dumps(message).encode('utf-8'))

        self.log.debug("Publish message #%s ,MSG : %s" %
                       (self._message_number_out, message))
        self.log.info("Publish message #%s,StockCode : %s " %
                      (self._message_number_out, symbol))
        return "done"


if __name__ == "__main__":
    e = stock_exit_strategy_simple()

""" End -of class """
