# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:05:37 2019

@author: ArchuBharathi
"""

import os
import sys
import pandas as pd
df = pd.read_csv("D:\\Live_quotes\\curr_day_quotes_Sun_Apr_21_08_53_41_2019.csv",
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
print(df)