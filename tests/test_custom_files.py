from django.test import TestCase
import pytest
from channels.testing import WebsocketCommunicator

from trades.calculator import percentage_calculator
from live import api
from live.consumers import LiveConsumer
from trades.management.commands import dbinsert
from trades.models import CurrencyPair


@pytest.mark.django_db(transaction=True)
@pytest.mark.asyncio
async def test_my_consumer_connects(self):
    communicator = WebsocketCommunicator(LiveConsumer.as_asgi(), "/ws/live/")
    connected, subprotocol = await communicator.connect()
    assert connected
    await communicator.send(
        {"action": "test_async_action", "pk": 2, "request_id": 1}
    )

    response = await communicator.receive()

    assert response == {
        "errors": [],
        "data": {"pk": 2},
        "action": "test_async_action",
        "response_status": 200,
        "request_id": 1,
    }

    # Test on connection welcome message
    # user = await communicator.receive_from()
    # assert user == 'test'
    # Close
    await communicator.disconnect()


""" Tests the calculator file """


class CalculatorTestCase(TestCase):

    # Test the percentage calculator function
    def test_percentage_calculator(self):

        # Mock the data needed to run the function
        total_val = 1000
        partial_pos_val = 250
        partial_ne_val = -250

        # Checks if the result is what is expected with positive values
        self.assertEqual(percentage_calculator(total_val, partial_pos_val), 25)

        # Checks if the result is what is expected with negative values
        self.assertEqual(percentage_calculator(total_val, partial_ne_val), -25)


""" Tests the api file functions"""


class ApiTestCase(TestCase):
    def setUp(self):
        self.fetcher = api.DataFetcher("EURUSD=X", "1d", "30m")

    # Tests the get historical data function
    def test_get_historical_data(self):

        # Runs the function
        response = self.fetcher.get_historical_data()
        # Gets the open column from the response
        tick_open = response["Open"]
        # Checks if the column has values
        self.assertTrue(len(tick_open))

    # Tests the convert ticker to line function
    def test_convert_ticker_to_line(self):

        # Creates a dictionary
        test_dict = {}
        fetcher_dict = self.fetcher.convert_ticker_to_line()
        # Checks if the function returns a dictionary
        self.assertTrue(type(fetcher_dict) == type(test_dict))

    # Tests the get real time data function
    def test_get_real_time_data(self):

        # Runs the function
        result = self.fetcher.get_real_time_data()

        # Verifies function is iterable
        self.assertTrue(len(result))


class DbInsert(TestCase):

    def test_dbinsert(self):

        initial_vals = len(CurrencyPair.objects.all())
        dbinsert.Command.handle(self)
        new_vals = len(CurrencyPair.objects.all())
        assert(new_vals > initial_vals)
