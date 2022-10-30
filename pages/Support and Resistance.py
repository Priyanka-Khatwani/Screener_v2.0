import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.cluster import KMeans
import mpl_finance
import streamlit as st

symbol = "CBIO"
start = "2019-12-19"
end = "2019-12-20"
est = pytz.timezone('US/Eastern')
date_format = "%H:%M"
ticker = yf.Ticker(symbol)
data = ticker.history(period="1d", interval="1m",start=start, end=end, prepost=False, actions=False)
data["Time"] = [d.timestamp() for d in data.index]
data.Time = data.Time.tz_convert(est)
data = data[["Time", "Open", "High", "Low", "Close", "Volume"]]
ax = plot_stock_data(data)
ax = plot_stock_data(data)
st.plotly_chart(ax)

