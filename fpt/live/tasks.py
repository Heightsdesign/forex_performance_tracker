
from asgiref.sync import AsyncToSync
from celery import shared_task
from .api import DataFetcher
import time
import json


@shared_task
def get_rtdata():

    eurusd = DataFetcher("EURUSD=X", "1d", "5m")
    historicalData = eurusd.convert_ticker_to_line()
    real_time = eurusd.get_real_time_data()
    now = list(real_time.keys())[0]
    price = list(real_time.values())[0]
    historicalData[now] = price
    actualData = json.dumps(historicalData)

    print(actualData)
    channel_layer.group_send('live_data', {'type': 'send_data', 'actualData': actualData})

