import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader as pdr
import datetime as dt
import statsmodels.api as sm
from scipy import stats

#######################################################################
#RSI
#input: ticker, rsi_period
#processing: calculate sum of up/down price moves, sum price moves, avg
#            price moves, calculate RS, and calculate RSI
#output: return rsi
#######################################################################

def RSI(ticker, rsi_period):
    data_source = pdr.get_data_yahoo(ticker)
    close = data_source['Adj Close'][rsi_period-1:]
    df = pd.DataFrame(close).dropna()
    chg = df['Adj Close'].diff(1)

    gain = chg.mask(chg<0,0)
    df['gain'] = gain
    loss = chg.mask(chg>0,0)
    df['loss'] = loss

    avg_gain = gain.ewm(com = rsi_period-1, min_periods = rsi_period).mean()
    avg_loss = loss.ewm(com = rsi_period-1, min_periods = rsi_period).mean()

    rs = abs(avg_gain/avg_loss)

    rsi = 100-(100/(1+rs))

    return rsi
