import numpy
import talib

close = numpy.random.random(100)
output = talib.SMA(close)

from talib import MA_Type

upper, middle, lower = talib.BBANDS(close, matype=MA_Type.T3)
output1 = talib.MOM(close, timeperiod=5)


from talib.abstract import *

# uses close prices (default)
output = SMA(inputs, timeperiod=25)

# uses open prices
output = SMA(inputs, timeperiod=25, price='open')

# uses close prices (default)
upper, middle, lower = BBANDS(inputs, 20, 2, 2)

# uses high, low, close (default)
slowk, slowd = STOCH(inputs, 5, 3, 0, 3, 0) # uses high, low, close by default

# uses high, low, open instead
slowk, slowd = STOCH(inputs, 5, 3, 0, 3, 0, prices=['high', 'low', 'open'])