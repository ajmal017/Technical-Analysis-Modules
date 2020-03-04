import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader as pdr
import datetime as dt
import statsmodels.api as sm
import stock_data as sd
import moving_average as ma
from scipy import stats


######################################################################
#moving average signal dataframe
#input: stock data, short moving average, long moving average
#processing: initialize a pandas data frame called signals and create
#            columns for short moving average and long moving average
#output: return initialized signals dataframe
######################################################################

def maSignalDF(stock, shortMA, longMA):
    signals = pd.DataFrame(index=stock.index)
    signals['signal'] = 0.0

    signals['short_mavg'] = shortMA
    signals['long_mavg'] = longMA

    return signals

################################################################################
#moving average buy/sell signals
#input: dataframe, shortWindow
#processing: return 1 (buy) where short_mavg is greater than long moving average
#            and return 0 otherwise (0)
#output: return dataframe with buy/sell signals
#################################################################################

def maBuySell(dataframe, shortWindow):
    dataframe['signal'][shortWindow:] = np.where(signals['short_mavg'][shortWindow:]
                                                  > signals['long_mavg'][shortWindow:],
                                                  1.0, 0.0)

    return dataframe


stock = sd.stock_data('SPY')



shortWindow = ma.getWindow()
ema8 = ma.exp_ma(stock,shortWindow)

longWindow = ma.getWindow()
ema21 = ma.exp_ma(stock,longWindow)

signals = maSignalDF(stock, ema8, ema21)

signals['Close'] = stock['Adj Close']
print(maBuySell(signals,8))
    
    




