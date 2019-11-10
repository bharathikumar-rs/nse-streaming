# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:24:56 2019

@author: ArchuBharathi
"""


from nsetools import Nse
import pandas as pd
import logging
from logging.config import fileConfig
import json
from exit_criteria.stock_exit_strategy_stream import stock_exit_strategy_simple
import re

class nse_json_parser:

    def __init__(self):
        self.nse = Nse()
        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')
        self.purchase_file = \
            "D:\\nse_data\\purchase_details\\purchase_price_details.csv"
        self.output_file = "D:\\nse_data\\purchase_details\\output.csv"


    def json_to_df_yahoo(self, message,kafka_connection):

        s = message.replace("\'","\"")
        try:
            ps = json.loads(s)
        except:
            print("Error Json :"+s)
            return
        lst = [ps]
        df = pd.DataFrame.from_dict(lst, orient='columns')

        exit_strat = stock_exit_strategy_simple(kafka_connection)
        exit_strat.process_exit_criteria_yahoo(df)
        del df
        del lst
        del exit_strat
        return "done"

    def json_to_df(self, message,kafka_connection,):

# =============================================================================
#         parse the incoming kafka message
#         the json message is single quotes, convert to double quotes
#         if empty messages are posted due to index/no data check for :
#             "None" value
# =============================================================================

        z = str(message)
       # s = re.sub(r"(?<![A-Za-z])'(?=[A-Za-z])|(?<=[.A-Za-z])'(?![A-Za-z])", '"', z)
       # s = re.sub(r"(?<![A-Za-z])'(?=[A-Za-z])|(?<=[.A-Za-z])'(?![A-Za-z])|(?<=[.0-9])'(?![0-9])|(?<![0-9])'(?=[0-9])", '"', z)
       # s = re.sub(r"(\s\')", '"', s)


        regex = re.search(r'\"(.+?)\"',z)
        s = z
        if regex:
            pos = regex.span()
            startpos = pos[0]
            endpos = pos[1]
            inter_str = z[startpos:endpos]
            inter_str = inter_str.replace("\'","~")
            s=z[:startpos-1]+inter_str+z[endpos:]

        s = s.replace("\'","\"")
        if len(s) > 7:  # check for empty message : Empy msg are stored as "None"
            s = s.replace("None", '\"''None''\"')
            s = s.replace("False", '\"''False''\"')
            s = s.replace("True", '\"''True''\"')
            try:
                ps = json.loads(s)
            except:
                print("Error source json:"+ z)
                print("Error Json :"+s)
                return

            lst = [ps]
            df = pd.DataFrame.from_dict(lst, orient='columns')
            print(df)
            #print("columns are: ",df.columns.tolist())
            exit_strat = stock_exit_strategy_simple(kafka_connection)
            exit_strat.process_exit_criteria(df)
            del df
            del lst
            del exit_strat
        return "done"


if __name__ == "__main__":

    n = nse_json_parser()


""" End -of class """
