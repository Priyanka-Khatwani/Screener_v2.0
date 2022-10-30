import pandas as pd
import numpy as np
import yfinance as yf
import streamlit as st
import plotly.graph_objects as go

chart_choice=st.sidebar.selectbox(label="Choose Stock Name",options=('ACC.NS','ADANIENT.NS','ADANIGREEN.NS','ADANIPORTS.NS','ATGL.NS','ADANITRANS.NS','AMBUJACEM.NS','APOLLOHOSP.NS','ASIANPAINT.NS','DMART.NS','AXISBANK.NS','BAJAJ-AUTO.NS','BAJFINANCE.NS','BAJAJFINSV.NS','BAJAJHLDNG.NS','BANDHANBNK.NS','BANKBARODA.NS','BERGEPAINT.NS','BEL.NS','BPCL.NS','BHARTIARTL.NS','BIOCON.NS','BOSCHLTD.NS','BRITANNIA.NS','CHOLAFIN.NS','CIPLA.NS','COALINDIA.NS','COLPAL.NS','DLF.NS','DABUR.NS','DIVISLAB.NS','DRREDDY.NS','EICHERMOT.NS','NYKAA.NS','GAIL.NS','GLAND.NS','GODREJCP.NS','GRASIM.NS','HCLTECH.NS','HDFCAMC.NS','HDFCBANK.NS','HDFCLIFE.NS','HAVELLS.NS','HEROMOTOCO.NS','HINDALCO.NS','HAL.NS','HINDUNILVR.NS','HDFC.NS','ICICIBANK.NS','ICICIGI.NS','ICICIPRULI.NS','ITC.NS','IOC.NS','IRCTC.NS','INDUSTOWER.NS','INDUSINDBK.NS','NAUKRI.NS','INFY.NS','INDIGO.NS','JSWSTEEL.NS','KOTAKBANK.NS','LTI.NS','LT.NS','LICI.NS','M&M.NS','MARICO.NS','MARUTI.NS','MPHASIS.NS','MUTHOOTFIN.NS','NTPC.NS','NESTLEIND.NS','ONGC.NS','PAYTM.NS','PIIND.NS','PIDILITIND.NS','POWERGRID.NS','PGHH.NS','RELIANCE.NS','SBICARD.NS','SBILIFE.NS','SRF.NS','MOTHERSON.NS','SHREECEM.NS','SIEMENS.NS','SBIN.NS','SUNPHARMA.NS','TCS.NS','TATACONSUM.NS','TATAMOTORS.NS','TATAPOWER.NS','TATASTEEL.NS','TECHM.NS','TITAN.NS','TORNTPHARM.NS','UPL.NS','ULTRACEMCO.NS','MCDOWELL-N.NS','VEDL.NS','WIPRO.NS','ZOMATO.NS'))

sample=['ACC.NS','ADANIENT.NS','ADANIGREEN.NS','ADANIPORTS.NS','ATGL.NS','ADANITRANS.NS','AMBUJACEM.NS','APOLLOHOSP.NS','ASIANPAINT.NS','DMART.NS','AXISBANK.NS','BAJAJ-AUTO.NS','BAJFINANCE.NS','BAJAJFINSV.NS','BAJAJHLDNG.NS','BANDHANBNK.NS','BANKBARODA.NS','BERGEPAINT.NS','BEL.NS','BPCL.NS','BHARTIARTL.NS','BIOCON.NS','BOSCHLTD.NS','BRITANNIA.NS','CHOLAFIN.NS','CIPLA.NS','COALINDIA.NS','COLPAL.NS','DLF.NS','DABUR.NS','DIVISLAB.NS','DRREDDY.NS','EICHERMOT.NS','NYKAA.NS','GAIL.NS','GLAND.NS','GODREJCP.NS','GRASIM.NS','HCLTECH.NS','HDFCAMC.NS','HDFCBANK.NS','HDFCLIFE.NS','HAVELLS.NS','HEROMOTOCO.NS','HINDALCO.NS','HAL.NS','HINDUNILVR.NS','HDFC.NS','ICICIBANK.NS','ICICIGI.NS','ICICIPRULI.NS','ITC.NS','IOC.NS','IRCTC.NS','INDUSTOWER.NS','INDUSINDBK.NS','NAUKRI.NS','INFY.NS','INDIGO.NS','JSWSTEEL.NS','KOTAKBANK.NS','LTI.NS','LT.NS','LICI.NS','M&M.NS','MARICO.NS','MARUTI.NS','MPHASIS.NS','MUTHOOTFIN.NS','NTPC.NS','NESTLEIND.NS','ONGC.NS','PAYTM.NS','PIIND.NS','PIDILITIND.NS','POWERGRID.NS','PGHH.NS','RELIANCE.NS','SBICARD.NS','SBILIFE.NS','SRF.NS','MOTHERSON.NS','SHREECEM.NS','SIEMENS.NS','SBIN.NS','SUNPHARMA.NS','TCS.NS','TATACONSUM.NS','TATAMOTORS.NS','TATAPOWER.NS','TATASTEEL.NS','TECHM.NS','TITAN.NS','TORNTPHARM.NS','UPL.NS','ULTRACEMCO.NS','MCDOWELL-N.NS','VEDL.NS','WIPRO.NS','ZOMATO.NS']
interval_choice=st.sidebar.selectbox(label="interval preference",options=('1m','2m','5m','15m','30m','90m','1hr','1d','5d','1wk','1mo'))
for l in range(0,len(sample)):
  if chart_choice==sample[l]:
    df=yf.download(tickers=sample[l],period='30d',interval=interval_choice)
    df.reset_index(inplace=True)
    fig=go.Figure(data=[go.Candlestick(x=df['Date'],open=df['Open'],high=df['High'],low=df['Low'],close=df['Close'])])
    st.plotly_chart(fig, use_container_width=True)
                        
                                      
