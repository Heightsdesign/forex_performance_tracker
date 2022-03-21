from asyncio import sleep
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .api import DataFetcher
from .models import UserSettings
from trades.models import CurrencyPair
from users.models import User
import json


class LiveConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        await self.accept()
        self.user = self.scope["user"]

        self.model_user = await self.get_model_user(self.user)
        self.currency_obj = await self.get_currency_obj(self.model_user)
        currency_id = await self.get_currency_id(self.currency_obj)
        self.time_frame = await self.get_time_frame(self.currency_obj)
        self.currency_name = await self.get_currency_name(currency_id)

        while True:

            if self.currency_name is not None:
                if self.currency_name[:-3] == "USD" and self.time_frame == "DAY":
                    currency = DataFetcher(f"{self.currency_name[-3:]}=X", "1d", "5m")
                elif self.currency_name[:-3] == "USD" and self.time_frame == "WEEK":
                    currency = DataFetcher(f"{self.currency_name[-3:]}=X", "1wk", "30m")
                elif self.currency_name[:-3] == "USD" and self.time_frame == "MONTH":
                    currency = DataFetcher(f"{self.currency_name[-3:]}=X", "1mo", "1d")
                elif self.currency_name[:-3] != "USD" and self.time_frame == "DAY":
                    currency = DataFetcher(f"{self.currency_name}=X", "1d", "5m")
                elif self.currency_name[:-3] != "USD" and self.time_frame == "WEEK":
                    currency = DataFetcher(f"{self.currency_name}=X", "1wk", "30m")
                elif self.currency_name[:-3] != "USD" and self.time_frame == "MONTH":
                    currency = DataFetcher(f"{self.currency_name}=X", "1mo", "1d")
                else:
                    currency = DataFetcher(f"{self.currency_name}=X", "1d", "5m")
            else:
                currency = DataFetcher("EURUSD=X", "1d", "5m")

            historicalData = currency.convert_ticker_to_line()
            real_time = currency.get_real_time_data()
            now = list(real_time.keys())[0]
            price = list(real_time.values())[0]
            historicalData[now] = price
            actualData = json.dumps(historicalData)

            await self.send(json.dumps(historicalData))
            await sleep(3)

    @database_sync_to_async
    def get_model_user(self, user):

        email = str(user)
        return User.objects.filter(email=email)[0]

    @database_sync_to_async
    def get_currency_obj(self, user):
        # Gets the last user choice for live currency
        return UserSettings.objects.filter(user=user)[UserSettings.objects.count() - 1]

    async def get_currency_id(self, currency_obj):
        # Gets the id of the currency
        currency_choice = currency_obj.currency_graph_id
        return currency_choice

    async def get_time_frame(self, currency_obj):
        # Gets the user requested time frame
        time_frame = currency_obj.time_frame
        return time_frame

    @database_sync_to_async
    def get_currency_name(self, currency_id):
        # Gets the currency name from currency pair table
        return CurrencyPair.objects.get(id=currency_id).name
