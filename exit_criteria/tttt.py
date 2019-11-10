# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:05:37 2019

@author: ArchuBharathi
"""
import os
import shutil
import pandas as pd
from datetime import datetime
from nsetools import Nse
import json
import re
print (str(datetime.now()))
filedet= "D:\\nse_data\\Live_quotes_24042019\\curr_day_quotes_Wed_Apr_24_10_37_07_2019.txt"

df = pd.DataFrame(columns=['X', 'Y', 'Z'])
#df = pd.read_csv(filedet,
#             usecols = ['buyPrice1','buyPrice2'])



# =============================================================================
# s = {
# 	'pricebandupper': 2.7,
# 	'symbol': 'COUNCODOS',
# 	'applicableMargin': 39.83,
# 	'bcEndDate': '29-SEP-18',
# 	'totalSellQuantity': 'None',
# 	'adhocMargin': 'None',
# 	'companyName': 'Country Condo's Limited ',
# 	'companyName': 'Countr'y Condo's Limited '
#     }
# =============================================================================


s = "{'priceban'dupper': 0.45, 'symbol': 'UNITY', 'applicableMargin': 100.0, 'bcEndDate': '30-DEC-17', 'totalSellQuantity)': 7749.0, 'adhocMargin': None, 'companyName': 'Unity Infraprojects)' Limited', 'marketType': 'N', 'exDate': '20-DEC-17', 'bcStartDate': '22-DEC-17', 'css_status_desc': 'Listed', 'dayHigh': 0.45, 'basePrice': 0.4, 'securityVar': None, 'pricebandlower': 0.35, 'sellQuantity5': None, 'sellQuantity4': None, 'sellQuantity3': None, 'cm_adj_high_dt': '09-MAY-18', 'sellQuantity2': None, 'dayLow': 0.4, 'sellQuantity1': 7749.0, 'quantityTraded': None, 'pChange': 12.5, 'totalTradedValue': 0.01, 'deliveryToTradedQuantity': None, 'totalBuyQuantity': 17412.0, 'averagePrice': 0.44, 'indexVar': None, 'cm_ffm': 1.25, 'purpose': 'ANNUAL GENERAL MEETING (DATE REVISED)', 'buyPrice2': 0.35, 'secDate': None, 'buyPrice1': 0.4, 'high52': 3.45, 'previousClose': 0.4, 'ndEndDate': None, 'low52': 0.4, 'buyPrice4': None, 'buyPrice3': None, 'recordDate': None, 'deliveryQuantity': None, 'buyPrice5': None, 'priceBand': 5.0, 'extremeLossMargin': None, 'cm_adj_low_dt': '10-MAY-19', 'varMargin': 100.0, 'sellPrice1': 0.45, 'sellPrice2': None, 'totalTradedVolume': 2308.0, 'sellPrice3': None, 'sellPrice4': None, 'sellPrice5': None, 'change': 0.05, 'surv_indicator': 'I', 'ndStartDate': None, 'buyQuantity4': None, 'isExDateFlag': False, 'buyQuantity3': None, 'buyQuantity2': 11845.0, 'buyQuantity1': 5567.0, 'series': 'BZ', 'faceValue': 2.0, 'buyQuantity5': None, 'closePrice': 0.45, 'open': 0.4, 'isinCode': 'INE466H01028', 'lastPrice': 0.45}"

A = "{'pricebandupper': 1788.1, 'symbol': 'DIVISLAB', 'applicableMargin': 12.5, 'bcEndDate': '10-SEP-18', 'totalSellQuantity': None, 'adhocMargin': None, 'companyName': \"Divi\'s Laboratories Limited\", 'marketType': 'N', 'exDate': '31-AUG-18', 'bcStartDate': '04-SEP-18', 'css_status_desc': 'Listed', 'dayHigh': 1657.8, 'basePrice': 1625.55, 'securityVar': 5.46, 'pricebandlower': 1463.0, 'sellQuantity5': None, 'sellQuantity4': None, 'sellQuantity3': None, 'cm_adj_high_dt': '26-MAR-19', 'sellQuantity2': None, 'dayLow': 1603.0, 'sellQuantity1': None, 'quantityTraded': 637110.0, 'pChange': 1.68, 'totalTradedValue': 10460.96, 'deliveryToTradedQuantity': 35.22, 'totalBuyQuantity': 17.0, 'averagePrice': 1641.94, 'indexVar': None, 'cm_ffm': 21029.57, 'purpose': 'ANNUAL GENERAL MEETING/DIVIDEND- RS 10 PER SHARE', 'buyPrice2': None, 'secDate': '10-May-2019 00:00:00', 'buyPrice1': 1650.35, 'high52': 1774.95, 'previousClose': 1625.55, 'ndEndDate': None, 'low52': 994.95, 'buyPrice4': None, 'buyPrice3': None, 'recordDate': None, 'deliveryQuantity': 224382.0, 'buyPrice5': None, 'priceBand': 'No Band', 'extremeLossMargin': 5.0, 'cm_adj_low_dt': '28-JUN-18', 'varMargin': 7.5, 'sellPrice1': None, 'sellPrice2': None, 'totalTradedVolume': 637110.0, 'sellPrice3': None, 'sellPrice4': None, 'sellPrice5': None, 'change': 27.25, 'surv_indicator': None, 'ndStartDate': None, 'buyQuantity4': None, 'isExDateFlag': False, 'buyQuantity3': None, 'buyQuantity2': None, 'buyQuantity1': 17.0, 'series': 'EQ', 'faceValue': 2.0, 'buyQuantity5': None, 'closePrice': 1650.35, 'open': 1609.2, 'isinCode': 'INE361B01024', 'lastPrice': 1652.8}"

#s=s.replace("\'","\"")
#print(A)
print("==============")


#s = re.sub(r"(?<![A-Za-z])'(?=[A-Za-z])|(?<=[.A-Za-z])'(?![A-Za-z])|(?<=[.0-9])'(?![0-9])|(?<![0-9])'(?=[0-9])", '"', s)

#s = re.sub(r"(?<![A-Za-z])'(?=[A-Za-z])|(?<=[.A-Za-z])'(?![A-Za-z])|(?<=[.0-9])'(?![0-9])|(?<![0-9])'(?=[0-9])|(?<=[^A-Za-z0-9])'(?![^A-Za-z0-9]])|(?<![^A-Za-z0-9])'(?=[^A-Za-z0-9])", '"', s)
#s = s.replace("None", '\"''None''\"')
#s = s.replace("False", '\"''False''\"')
#s = s.replace("True", '\"''True''\"')


regex = re.search(r'\"(.+?)\"',A)
pos = regex.span()
startpos = pos[0]
endpos = pos[1]
inter_str = A[startpos:endpos]
inter_str = inter_str.replace("\'","~")
b=A[:startpos-1]+inter_str+A[endpos:]



print(b)
print(inter_str)
#s = (regex.sub(r'\1^\2', A))

#print(s)
#s = re.sub(r"(\s\')", '"', s)

#A = re.sub("(\s\')|(?<![A-Za-z])'(?=[A-Za-z])|(?<=[.A-Za-z])'(?![A-Za-z])|(?<![A-za-z])", '"', A)



#print(A)

