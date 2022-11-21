import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import plotly.express as px
import yfinance as yf
import streamlit as st

#Getting the data
sample=['ACC.NS','ADANIENT.NS','ADANIGREEN.NS','ADANIPORTS.NS','ATGL.NS','ADANITRANS.NS','AMBUJACEM.NS','APOLLOHOSP.NS','ASIANPAINT.NS','DMART.NS','AXISBANK.NS','BAJAJ-AUTO.NS','BAJFINANCE.NS','BAJAJFINSV.NS','BAJAJHLDNG.NS','BANDHANBNK.NS','BANKBARODA.NS','BERGEPAINT.NS','BEL.NS','BPCL.NS','BHARTIARTL.NS','BIOCON.NS','BOSCHLTD.NS','BRITANNIA.NS','CHOLAFIN.NS','CIPLA.NS','COALINDIA.NS','COLPAL.NS','DLF.NS','DABUR.NS','DIVISLAB.NS','DRREDDY.NS','EICHERMOT.NS','NYKAA.NS','GAIL.NS','GLAND.NS','GODREJCP.NS','GRASIM.NS','HCLTECH.NS','HDFCAMC.NS','HDFCBANK.NS','HDFCLIFE.NS','HAVELLS.NS','HEROMOTOCO.NS','HINDALCO.NS','HAL.NS','HINDUNILVR.NS','HDFC.NS','ICICIBANK.NS','ICICIGI.NS','ICICIPRULI.NS','ITC.NS','IOC.NS','IRCTC.NS','INDUSTOWER.NS','INDUSINDBK.NS','NAUKRI.NS','INFY.NS','INDIGO.NS','JSWSTEEL.NS','KOTAKBANK.NS','LTI.NS','LT.NS','LICI.NS','M&M.NS','MARICO.NS','MARUTI.NS','MPHASIS.NS','MUTHOOTFIN.NS','NTPC.NS','NESTLEIND.NS','ONGC.NS','PAYTM.NS','PIIND.NS','PIDILITIND.NS','POWERGRID.NS','PGHH.NS','RELIANCE.NS','SBICARD.NS','SBILIFE.NS','SRF.NS','MOTHERSON.NS','SHREECEM.NS','SIEMENS.NS','SBIN.NS','SUNPHARMA.NS','TCS.NS','TATACONSUM.NS','TATAMOTORS.NS','TATAPOWER.NS','TATASTEEL.NS','TECHM.NS','TITAN.NS','TORNTPHARM.NS','UPL.NS','ULTRACEMCO.NS','MCDOWELL-N.NS','VEDL.NS','WIPRO.NS','ZOMATO.NS']

name=st.selectbox(label="Choose the stock you're most interested in",options=sample)

interval=st.selectbox(label="Interval Preference",options=('2m','5m','15m','30m','60m','90m','1d','5d','1wk'))

df=yf.download(tickers=name,period='22d',interval=interval)

df.reset_index(inplace=True)
df.rename(columns = {'Datetime':'Date'}, inplace = True)

#Get long and short window for calculation
short_window=st.number_input("Enter the short window",value=20,step=1)
long_window=st.number_input("Enter the long window",value=50,step=1)

#Calculatin of signals
if short_window<long_window:
  st.write("Window added successfully")
  try:
    df['short_window_ma'] = df['Close'].rolling(window = short_window,min_periods=1).mean()
    df['long_window_ma'] = df['Close'].rolling(window = long_window,min_periods=1).mean()
    #Then we shall create an indicator column with value 1 if short window ma is greater than long window ma and 0 otherwise.
    df['signal'] = np.where(df['short_window_ma'] > df['long_window_ma'], 1.0, 0.0) 
  except:
    print("The number of moving averages is not possible with the data available.")
else:
  st.write("Short Window should be less than long Window!")

#Identifying dates where signals have occured
df['position'] = df['signal'].diff()
df.reset_index(inplace=True)
buy_dates=[]
sell_dates=[]
for i in range(0,len(df)):
  if df['position'][i]==1:
    buy_dates.append(df['Date'][i])
  elif df['position'][i]==-1:
    sell_dates.append(df['Date'][i])
    
#Creating graph
fig = go.Figure(data=[go.Candlestick(x=df['Date'],open=df['Open'],high=df['High'],low=df['Low'],close=df['Close'])])
for i in range(0,len(buy_dates)):
  fig.add_shape(type='line',x0=buy_dates[i],x1=buy_dates[i],y0=df['Close'].min(),y1=df['Close'].max(),line=dict(color='orange', width=3))
for j in range(0,len(sell_dates)):
  fig.add_shape(type='line',x0=sell_dates[j],x1=sell_dates[j],y0=df['Close'].min(),y1=df['Close'].max(),line=dict(color='blue', width=3))

fig.add_trace(go.Scatter(x=df['Date'],
        y=df['short_window_ma'],line=dict(color="#ffe476")))
fig.add_trace(go.Scatter(x=work_data['date'],
        y=df['long_window_ma'],line=dict(color='#00FFFF')))
st.pyplot(fig=fig)

