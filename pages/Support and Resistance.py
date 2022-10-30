import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.cluster import KMeans
import mpl_finance
import streamlit as st

data=yf.download(tickers='ACC.NS',period='60d')
ax = plot_stock_data(data)
st.plotly_chart(ax)

