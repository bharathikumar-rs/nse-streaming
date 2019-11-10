
import csv
import matplotlib.pyplot as plt
import numpy as np


#symbols_list = ['INFY', 'MSFT']
symbols_list = ['INFY']

f = open('D:\\nse_streaming_py\\Stock-Analysis\\Stock-Analysis-1.0.0\\Stock Scrapers\\Datasets\\INFY.csv')
stock = csv.reader(f)
next(stock)

first_close_prices = []
second_close_prices = []
dates = []

for row in stock:
	if row[0] == symbols_list[0]:
		x = float(row[5])
		first_close_prices.append(float("{0:.2f}".format(x)))
		dates.append(row[1])

	if row[0]  == symbols_list[1]:
		y = float(row[5])
		second_close_prices.append(float("{0:.2f}".format(y)))


plt.plot(first_close_prices, 'r-')
plt.plot(second_close_prices, 'b-')
plt.ylabel("Prices")
plt.title("AAPL Vs. MSFT")
plt.subplots_adjust(bottom=0.13)
plt.subplots_adjust(top=0.92)
plt.subplots_adjust(left=0.07)
plt.subplots_adjust(right=0.96)
plt.xticks([w*20 for w in range(32)],
  ['Month %i'%w for w in range(32)])
plt.xticks(rotation=90)
plt.autoscale(enable=True, axis='both')
plt.grid()
plt.show()