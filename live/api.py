import time
from datetime import datetime
import yfinance as yf

"""
Get data from yfinance example:
    eurusd = yf.Ticker("EURUSD=X")
    print(eurusd.history(period='1mo', interval='5m'))
"""


class DataFetcher:

    def __init__(self, pair, period, interval):
        self.pair = pair
        self.period = period
        self.interval = interval
        self.pairTicker = yf.Ticker(self.pair)

    def get_historical_data(self):

        self.historical_data = self.pairTicker.history(
            period=self.period,
            interval=self.interval
        )

        return self.historical_data

    def convert_ticker_to_line(self):

        data = self.get_historical_data()

        points = []

        data = data.reset_index().rename(columns={'Datetime': 'Date'})
        tick_open = data['Open'].tolist()
        tick_close = data['Close'].tolist()
        tick_dates = data['Date'].tolist()
        pydates = []

        for to in tick_open:
            for tc in tick_close:
                total = to + tc
                point = total / 2

            points.append(round(point, 5))

        for date in tick_dates:
            date = date.to_pydatetime()
            pydates.append(date.strftime("%m/%d/%Y, %H:%M:%S"))

        zip_iterator = zip(pydates, points)
        parsed_data = dict(zip_iterator)

        return parsed_data

    def get_real_time_data(self):

        real_time_data = {}

        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        price = yf.Ticker(self.pair).info['regularMarketPrice']

        real_time_data[date_time] = round(price, 5)

        return real_time_data

    def launch_live(self):

        data = self.convert_ticker_to_line()

        while True:
            real_time = self.get_real_time_data()
            now = list(real_time.keys())[0]
            price = list(real_time.values())[0]
            data[now] = price
            print(data)
            time.sleep(5)


print(DataFetcher("EURUSD=X", "1d", "30m").convert_ticker_to_line())
