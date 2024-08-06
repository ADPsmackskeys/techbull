import yfinance as yf
import datetime
import plotly.graph_objects as go
import pandas as pd

data = yf.download ('TCS.NS', start = '2024-07-07', end = datetime.date.today())
print (type(data))
# data.to_csv ('TCS_data.csv')
data = pd.read_csv ('TCS_data.csv')
list = list(data)
print (data[list[1]])
chart = go.Figure (data = go.Candlestick(x = data[list[0]], open = data['Open'], high = data['High'], low = data['Low'], close = data['Close']))
chart.show()