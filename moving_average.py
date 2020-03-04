import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader as pdr
import datetime as dt
import statsmodels.api as sm
from scipy import stats

#################################################################
#moving_average
#inputs: closing price list, moving average period observed
#processing: sum closing prices and divide by desired time period
#return: moving average
##################################################################

def simple_ma(stock, period):
    sma = stock['Adj Close'].rolling(window=period).mean()
    return sma


#################################################################
#exponential moving average
#inputs: stock, period
#processing: calculate exponential moving average
#output: return ema
################################################################

def exp_ma(stock, period):
    ema = stock['Adj Close'].ewm(span=period).mean()
    return ema

#################################################################
#getWindow
#input: none
#processing: user inputs period for moving average
#output: window
#################################################################

def getWindow():
    window = int(input("Enter moving window: \n"))
    return window

