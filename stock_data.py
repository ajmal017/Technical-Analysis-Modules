import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader as pdr
import datetime as dt
import statsmodels.api as sm
from scipy import stats

###############################################################
#stock_data
#input: ticker
#processing: use pandas data reader to retrieve stock data
#output: pandas dataframe of historical stock data
###############################################################

def stock_data(ticker):
    stock = pdr.get_data_yahoo(ticker)

    return stock
###################################################################
#get_close
#input: stock
#processing: return stock closing prices
#output: return dataframe
###################################################################

def get_close(stock):
    return stock['Adj Close']


##################################################################
#get_volume
#input: stock ticker and desired time period
#processing: retrieve desired data from yahoo finance
#output: return stock volume
##################################################################

def get_volume(ticker, period): 
    ticker = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
    volume = ticker['Volume']

    return volume

##################################################################
#avg_volume
#input: stock volume and desired period
#processing: calculate average volume
#output: return average volume
##################################################################

def avg_volume(volume, period):
    return volume/period

##################################################################
#getLastPrice
#input: ticker
#processing: retrieve last closing price of stock
#output: last closing price
###################################################################

def getLastPrice(ticker):
    lastPrice = pdr.get_data_yahoo(ticker)

    return lastPrice['Close'][-1]


###################################################################
#getStartDate
#input:range
#processing: return period starting date
#output: stock starting date
###################################################################

def getStartDate(range):
    return dt.datetime.now() - dt.timedelta(days=range)


