from django.shortcuts import render
from .api import DataFetcher
import time
import json


def homepage(request):
    return render(request, 'live/homepage.html')


def index(request):

    eurusd = DataFetcher("EURUSD=X", "1d", "5m")
    historicalData = eurusd.convert_ticker_to_line()

    while True:
        real_time = eurusd.get_real_time_data()
        now = list(real_time.keys())[0]
        price = list(real_time.values())[0]
        historicalData[now] = price
        actualData = json.dumps(historicalData)
        time.sleep(5)

        context = {
            "actualData": actualData,
        }

        return render(request, 'live/live_charts.html', context)

