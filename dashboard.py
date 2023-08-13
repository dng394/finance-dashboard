import streamlit as st
import pandas as pd
import yfinance as yf

st.title('Finance Dashboard') 

tickers = ('TSLA', 'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'BTC-USD', 'ETH-USD')
dropdown = st.multiselect('Pick assets', tickers)
start = st.date_input('Start Date', value = pd.to_datetime('2020-01-01'))
end = st.date_input('End Date', value = pd.to_datetime('today'))

def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1 

    # Fill first value for cumulative return
    cumret = cumret.fillna(0)
    return cumret

if len(dropdown) > 0:
    df = relativeret(yf.download(dropdown,start,end)['Adj Close'])
    st.header('Returns of {}'.format(dropdown)) 

    st.line_chart(df) 