import talib
import numpy as np
import glob
from talib import abstract
from talib.abstract import *

print( talib.get_functions())
#print (talib.get_function_groups())

sma = abstract.SMA
obv = abstract.OBV



import matplotlib.pyplot as plt
# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
#y = np.sin(x)
y = range(0,95)
plt.title("sine wave form")

# Plot the points using matplotlib
plt.plot(x, y)
plt.show()


