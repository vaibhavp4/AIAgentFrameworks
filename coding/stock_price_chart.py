# filename: stock_price_chart.py

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# get today's date 
today = pd.to_datetime('today').isoformat()

# download historical stock price data
nvda = yf.download('NVDA', start='2021-01-01', end=today)
tesla = yf.download('TSLA', start='2021-01-01', end=today)

# calculate the percentage change in closing price
nvda['Percent Change'] = (nvda['Close']/nvda['Close'].iloc[0]) - 1
tesla['Percent Change'] = (tesla['Close']/tesla['Close'].iloc[0]) - 1

# plot a line chart
plt.figure(figsize=(10,5))
plt.title('NVDA vs TESLA YTD Stock Price Change')
plt.xlabel('Dates')
plt.ylabel('Percent Change')
plt.grid(True)
plt.plot(nvda.index, nvda['Percent Change'], label='NVDA')
plt.plot(tesla.index, tesla['Percent Change'], label='TESLA')
plt.legend(loc='best')
plt.savefig('stock_price_chart.png')
plt.show()