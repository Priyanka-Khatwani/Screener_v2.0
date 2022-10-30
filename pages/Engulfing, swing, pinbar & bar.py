import pandas as pd
import yfinance as yf
import streamlit as st

st.title("Patterns for 5 minutes interval")
sample=['ACC.NS','ADANIENT.NS','ADANIGREEN.NS','ADANIPORTS.NS','ATGL.NS','ADANITRANS.NS','AMBUJACEM.NS','APOLLOHOSP.NS','ASIANPAINT.NS','DMART.NS','AXISBANK.NS','BAJAJ-AUTO.NS','BAJFINANCE.NS','BAJAJFINSV.NS','BAJAJHLDNG.NS','BANDHANBNK.NS','BANKBARODA.NS','BERGEPAINT.NS','BEL.NS','BPCL.NS','BHARTIARTL.NS','BIOCON.NS','BOSCHLTD.NS','BRITANNIA.NS','CHOLAFIN.NS','CIPLA.NS','COALINDIA.NS','COLPAL.NS','DLF.NS','DABUR.NS','DIVISLAB.NS','DRREDDY.NS','EICHERMOT.NS','NYKAA.NS','GAIL.NS','GLAND.NS','GODREJCP.NS','GRASIM.NS','HCLTECH.NS','HDFCAMC.NS','HDFCBANK.NS','HDFCLIFE.NS','HAVELLS.NS','HEROMOTOCO.NS','HINDALCO.NS','HAL.NS','HINDUNILVR.NS','HDFC.NS','ICICIBANK.NS','ICICIGI.NS','ICICIPRULI.NS','ITC.NS','IOC.NS','IRCTC.NS','INDUSTOWER.NS','INDUSINDBK.NS','NAUKRI.NS','INFY.NS','INDIGO.NS','JSWSTEEL.NS','KOTAKBANK.NS','LTI.NS','LT.NS','LICI.NS','M&M.NS','MARICO.NS','MARUTI.NS','MPHASIS.NS','MUTHOOTFIN.NS','NTPC.NS','NESTLEIND.NS','ONGC.NS','PAYTM.NS','PIIND.NS','PIDILITIND.NS','POWERGRID.NS','PGHH.NS','RELIANCE.NS','SBICARD.NS','SBILIFE.NS','SRF.NS','MOTHERSON.NS','SHREECEM.NS','SIEMENS.NS','SBIN.NS','SUNPHARMA.NS','TCS.NS','TATACONSUM.NS','TATAMOTORS.NS','TATAPOWER.NS','TATASTEEL.NS','TECHM.NS','TITAN.NS','TORNTPHARM.NS','UPL.NS','ULTRACEMCO.NS','MCDOWELL-N.NS','VEDL.NS','WIPRO.NS','ZOMATO.NS']

indicators=("Bullish engulfing","Bearish engulfing","Bullish Swing","Bearish swing","Bullish pinbar","Bearish pinbar","Inside bar","Outside bar")
indicator=st.selectbox(label="Choose an indicator you're most interested in",options=indicators)
name=st.selectbox(label="Choose the stock you're most interested in",options=sample)

df=yf.download(tickers=name,period='22d',interval='5m')
df.reset_index(inplace=True)

for i in range(2,len(df)):
  current = df.iloc[i,:]
  prev = df.iloc[i-1,:]
  prev_2 = df.iloc[i-2,:]
  realbody = abs(current['Open'] - current['Close'])
  candle_range = current['High'] - current['Low']
  idx = df.index[i]

  df.loc[idx,'Bullish engulfing'] = current['High'] > prev['High'] and current['Low'] < prev['Low'] and realbody >= 0.8 * candle_range and current['Close'] > current['Open'] #Bullish engulfing
  df.loc[idx,'Bearish engulfing'] = current['High'] > prev['High'] and current['Low'] < prev['Low'] and realbody >= 0.8 * candle_range and current['Close'] < current['Open'] #Bearish engulfing
  df.loc[idx,'Bullish swing'] = current['Low'] > prev['Low'] and prev['Low'] < prev_2['Low']  #Bullish Swing
  df.loc[idx,'Bearish swing'] = current['High'] < prev['High'] and prev['High'] > prev_2['High'] #Bearish Swing
  df.loc[idx,'Bullish pinbar'] = realbody <= candle_range/3 and  min(current['Open'], current['Close']) > (current['High'] + current['Low'])/2 and current['Low'] < prev['Low'] #Bullish pinbar
  df.loc[idx,'Bearish pinbar'] = realbody <= candle_range/3 and max(current['Open'] , current['Close']) < (current['High'] + current['Low'])/2 and current['High'] > prev['High'] #Bearish pinbar
  df.loc[idx,'Inside bar'] = current['High'] < prev['High'] and current['Low'] > prev['Low'] #Inside bar
  df.loc[idx,'Outside bar'] = current['High'] > prev['High'] and current['Low'] < prev['Low'] #Outside bar
  df.fillna(False, inplace=True)

         
  for types in range(0,len(indicators)):
           if indicator==indicators[types]:
              df=df[df[indicator]==True]
              
        
            

st.dataframe(df)
    
    
   
  
  
