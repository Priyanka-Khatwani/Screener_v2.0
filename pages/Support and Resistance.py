# import necessary libraries

import pandas as pd
import yfinance as yf
import numpy as np
import math
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

sample=['ACC.NS','ADANIENT.NS','ADANIGREEN.NS','ADANIPORTS.NS','ATGL.NS','ADANITRANS.NS','AMBUJACEM.NS','APOLLOHOSP.NS','ASIANPAINT.NS','DMART.NS','AXISBANK.NS','BAJAJ-AUTO.NS','BAJFINANCE.NS','BAJAJFINSV.NS','BAJAJHLDNG.NS','BANDHANBNK.NS','BANKBARODA.NS','BERGEPAINT.NS','BEL.NS','BPCL.NS','BHARTIARTL.NS','BIOCON.NS','BOSCHLTD.NS','BRITANNIA.NS','CHOLAFIN.NS','CIPLA.NS','COALINDIA.NS','COLPAL.NS','DLF.NS','DABUR.NS','DIVISLAB.NS','DRREDDY.NS','EICHERMOT.NS','NYKAA.NS','GAIL.NS','GLAND.NS','GODREJCP.NS','GRASIM.NS','HCLTECH.NS','HDFCAMC.NS','HDFCBANK.NS','HDFCLIFE.NS','HAVELLS.NS','HEROMOTOCO.NS','HINDALCO.NS','HAL.NS','HINDUNILVR.NS','HDFC.NS','ICICIBANK.NS','ICICIGI.NS','ICICIPRULI.NS','ITC.NS','IOC.NS','IRCTC.NS','INDUSTOWER.NS','INDUSINDBK.NS','NAUKRI.NS','INFY.NS','INDIGO.NS','JSWSTEEL.NS','KOTAKBANK.NS','LTI.NS','LT.NS','LICI.NS','M&M.NS','MARICO.NS','MARUTI.NS','MPHASIS.NS','MUTHOOTFIN.NS','NTPC.NS','NESTLEIND.NS','ONGC.NS','PAYTM.NS','PIIND.NS','PIDILITIND.NS','POWERGRID.NS','PGHH.NS','RELIANCE.NS','SBICARD.NS','SBILIFE.NS','SRF.NS','MOTHERSON.NS','SHREECEM.NS','SIEMENS.NS','SBIN.NS','SUNPHARMA.NS','TCS.NS','TATACONSUM.NS','TATAMOTORS.NS','TATAPOWER.NS','TATASTEEL.NS','TECHM.NS','TITAN.NS','TORNTPHARM.NS','UPL.NS','ULTRACEMCO.NS','MCDOWELL-N.NS','VEDL.NS','WIPRO.NS','ZOMATO.NS']

name=st.selectbox(label="Choose the stock you're most interested in",options=sample)
interval=st.selectbox(label="Interval Preference",options=('2m','5m','15m','30m','60m','90m','1d','5d','1wk'))
period_preference=st.selectbox(label="Period Preference",options=('2d','5d','10d','20d','22d','30d','40d','60d','90d'))

# get stock prices using yfinance library
def get_stock_price(name):
  df = yf.download(symbol,period=period_preference,interval=interval)
  df['Date'] = pd.to_datetime(df.index)
  df['Date'] = df['Date'].apply(mpl_dates.date2num)
  df = df.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]
  return df
symbol = 'COST'

df = get_stock_price(symbol)

# determine bullish fractal 
def is_support(df,i):  
  cond1 = df['Low'][i] < df['Low'][i-1]   
  cond2 = df['Low'][i] < df['Low'][i+1]   
  cond3 = df['Low'][i+1] < df['Low'][i+2]   
  cond4 = df['Low'][i-1] < df['Low'][i-2]  
  return (cond1 and cond2 and cond3 and cond4) 

# determine bearish fractal
def is_resistance(df,i):  
  cond1 = df['High'][i] > df['High'][i-1]   
  cond2 = df['High'][i] > df['High'][i+1]   
  cond3 = df['High'][i+1] > df['High'][i+2]   
  cond4 = df['High'][i-1] > df['High'][i-2]  
  return (cond1 and cond2 and cond3 and cond4)

# to make sure the new level area does not exist already
def is_far_from_level(value, levels, df):    
  ave =  np.mean(df['High'] - df['Low'])    
  return np.sum([abs(value-level)<ave for _,level in levels])==0

# a list to store resistance and support levels
levels = []
for i in range(2, df.shape[0] - 2):  
  if is_support(df, i):    
    low = df['Low'][i]    
    if is_far_from_level(low, levels, df):      
      levels.append((i, low))  
  elif is_resistance(df, i):    
    high = df['High'][i]    
    if is_far_from_level(high, levels, df):      
      levels.append((i, high))
      
# for visualization
fig,x = plt.subplots(figsize=(16, 9))   
candlestick_ohlc(ax,df.values,width=0.6, colorup='green',colordown='red', alpha=0.8)    
date_format = mpl_dates.DateFormatter('%d %b %Y')
ax.xaxis.set_major_formatter(date_format)    
for level in levels:        
    plt.hlines(level[1], xmin = df['Date'][level[0]], xmax = max(df['Date']), colors='blue', linestyle='--')    
#fig.show()
st.plotly_chart(fig, use_container_width=True)

