import requests, os, json, csv

size = 'compact' # 'full' for complete historical data, 'compact' for most recent 100
ticker = ['GME', 'SPY', 'TWTTR', 'TSLA', 'AMD'] # stock tickers to search for
datatype = 'csv' # 'json' for JSON output, 'csv' for CSV output

for stock in ticker:
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&outputsize={size}&datatype={datatype}&apikey=QC1C7LRPUTLC597Q'
    response = requests.get(url)
    #Save CSV to file
    with open(f'{stock}.csv', 'wb') as file:
        file.write(response.content)