from YahooFinance.basics import basics
from bs4 import *
import json
import logging
from logging.config import fileConfig


class fetch_yahoo_live:


    def __init__(self):

        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')
        self.basics = basics()


    def generate_info_table(self,decoded_item):
        #print (decoded_item)
        quote = decoded_item.find(id="quote-summary")

        left_table = quote.find(attrs={"data-test": "left-summary-table"})
        right_table = quote.find(attrs={"data-test": "right-summary-table"})

        # this particular section i sthe table in yahoo webpage , the class /color may get changed in website
        #if so change the "class"" y inspecting website and when you gget index out of execpetion
#        left_stream = left_table.find_all(class_="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($c-fuji-grey-c) H(36px) ")
 #       left_stream.append(left_table.find(class_="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($c-fuji-grey-c) H(36px) Bdbw(0)! "))
  #      right_stream = right_table.find_all(class_="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($c-fuji-grey-c) H(36px) ")
   #     right_stream.append(right_table.find(class_="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($c-fuji-grey-c) H(36px) Bdbw(0)! "))

        left_stream = left_table.find_all(class_="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) ")
        left_stream.append(left_table.find(class_="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) Bdbw(0)! "))
        right_stream = right_table.find_all(class_="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor)) H(36px) ")
        right_stream.append(right_table.find(class_="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) Bdbw(0)! "))


        tables = [left_stream, right_stream]
        self.log.debug(tables)
        return tables


    def get_price(self,decoded_item):

        tittle = decoded_item.find(id="quote-header-info")

        price = tittle.find(class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
        info = price.get_text()
        self.log.debug(info)

        return info


    def get_info(self,type, info_table):
    # to add bid and ask
        if type == 'volume':  # 1,7
            x = 0
            y = 6
        elif type == 'avg_volume':  # 1,8
            x = 0
            y = 7
        elif type == 'price':
            x = None
            y = None
        elif type == 'market_cap':  # 2,1
            x = 1
            y = 0
        elif type == 'beta':  # 2,2
            x = 1
            y = 1
        elif type == 'pe_ratio':  # 2,3
            x = 1
            y = 2
        elif type == 'eps':  # 2,4
            x = 1
            y = 3
        elif type == 'earning_date':  # 2,5
            x = 1
            y = 4
        elif type == 'dividend_yield':  # 2,6
            x = 1
            y = 5
        else:
            raise Exception('fck you')

        info = info_table[x][y].contents[1].get_text()

        return info

    def yahoo_live(self,symbol):
        fl = fetch_yahoo_live()
        decoded_item = self.basics.https_get(symbol)
        #print (decoded_item)
        table = fl.generate_info_table(decoded_item)
        volume = fl.get_info('avg_volume', table)
        price = fl.get_price(decoded_item)
        #response_json = '{"symbol":'+'"'+symbol+'"'+',"price":'+str(price)+',"volume":'+str(volume)+'}'
        response_json ="{'symbol':'"+symbol+"','price':"+str(price)+",'volume':'"+str(volume)+"'}"

        #print(response_json)
        return response_json
#if __name__ == "__main__":
    #fl = fetch_yahoo_live()
