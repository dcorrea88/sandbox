import yfinance as yf


tickers =['AAPL','GOOG']

df = yf.download(tickers, start='2022-03-10', end= '2022-03-17')

#print(df.head())

df.to_csv('test.csv')