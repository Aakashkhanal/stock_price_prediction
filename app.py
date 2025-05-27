import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf 
from keras.models import load_model
import streamlit as st
 
start = '2010-01-01'
end = '2019-12-31'

st.title('Stock Trend Prediction')

user_input = st.text_input('Enter stock Ticker', 'AAPL')
df = yf.download(user_input, start=start, end=end)


# Describing data
st.subheader('Data from')
st.write(df.describe())