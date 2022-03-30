from django.test import TestCase
from trades.calculator import percentage_calculator
from live import api


""" Tests the calculator file """


class CalculatorTestCase(TestCase):

    # Test the percentage calculator function
    def test_percentage_calculator(self):

        # Mock the data needed to run the function
        total_val = 1000
        partial_positive_val = 250
        partial_negative_val = -250

        # Checks if the result is what is expected with positive values
        self.assertEqual(
            percentage_calculator(
                total_val, partial_positive_val), 25)

        # Checks if the result is what is expected with negative values
        self.assertEqual(
            percentage_calculator(
                total_val, partial_negative_val), -25)


""" Tests the api file functions"""


class ApiTestCase(TestCase):

    def setUp(self):
        self.fetcher = api.DataFetcher("EURUSD=X", "1d", "30m")

    # Tests the get historical data function
    def test_get_historical_data(self):

        # Runs the function
        response = self.fetcher.get_historical_data()
        # Gets the open column from the response
        tick_open = response['Open']
        # Checks if the column has values
        self.assertTrue(len(tick_open))

    # Tests the convert ticker to line function
    def test_convert_ticker_to_line(self):

        # Creates a dictionary
        test_dict = {}

        # Checks if the function returns a dictionary
        self.assertTrue(type(self.fetcher.convert_ticker_to_line()) == type(test_dict))

    # Tests the get real time data function
    def test_get_real_time_data(self):

        # Runs the function
        result = self.fetcher.get_real_time_data()

        # Verifies function is iterable
        self.assertTrue(len(result))
