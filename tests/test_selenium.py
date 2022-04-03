from django.test import TestCase
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

"""
Inserted Selenium user:
Username: SeleniumTest
Password: SL123
Email: selenium@test.com
Capital: 10000.00
Id: 12
"""


class SeleniumUser():

    def __init__(self, id, email, username, password):
        self.id = id
        self.email = email
        self.username = username
        self.password = password


class SeleniumTestCase(TestCase):

    def setUp(self):

        self.user = SeleniumUser(
            "12",
            "selenium@test.com",
            "SeleniumTest",
            "SL123"
        )

        # Sets driver options
        self.options = Options()

        # Uncheck to run tests without browser window
        # options.headless = True

        # Sets the driver
        # For production environment
        # self.browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver', options=self.options)

        # For local environment
        self.browser = webdriver.Firefox(executable_path='D:\webdrivers\geckodriver.exe', options=self.options)
        self.browser.maximize_window()

    def test_selenium_logic(self):

        # Browses to the connexion page local environment
        self.browser.get('http://127.0.0.1:8000/users/login/')

        # Fetches the email and password inputs
        email_input = self.browser.find_element(by=By.ID, value='email_input_log')
        password_input = self.browser.find_element(by=By.ID, value='password_input_log')

        # Inserts the email and password inputs
        email_input.send_keys(self.user.email)
        time.sleep(1)
        password_input.send_keys(self.user.password + Keys.RETURN)
        time.sleep(2)
        # Verifies if Pur Beurre is in the title of the page
        assert 'Quren' in self.browser.title
        time.sleep(2)
        assert self.user.username in self.browser.page_source

        # Goes to the dashboard

        # For production environment
        # browser.get('http://159.65.51.134:80/users/{}/')

        # For local environment
        self.browser.get('http://127.0.0.1:8000/users/{}/'.format(self.user.id))
        time.sleep(2)

        """Tests user strategy change"""

        strategy_input = self.browser.find_element(by=By.ID, value='content')
        strategy_input.send_keys("Test Strategy")
        change_strat_button = self.browser.find_element(by=By.ID, value='stratButton')
        change_strat_button.click()
        time.sleep(2)
        self.browser.get('http://127.0.0.1:8000/users/{}/'.format(self.user.id))
        time.sleep(2)
        assert "Test Strategy" in self.browser.page_source

        """Tests user adds trade"""

        # Enters entry point
        entry_point = self.browser.find_element(by=By.ID, value="entry_point")
        entry_point.send_keys(1.35100)
        time.sleep(1)

        # Enters exit point
        exit_point = self.browser.find_element(by=By.ID, value="exit_point")
        exit_point.send_keys(1.35200)
        time.sleep(1)

        # Enters profit
        profit = self.browser.find_element(by=By.ID, value="profit")
        profit.send_keys(100.00)
        time.sleep(1)

        # Adds the trade, clicks the button
        add_trade_button = self.browser.find_element(by=By.ID, value="submitButton")
        time.sleep(1)
        add_trade_button.click()
        time.sleep(1)

        self.browser.get('http://127.0.0.1:8000/users/{}/'.format(self.user.id))

        # Checks if the trade was added checks by looking for its entry point value
        assert "1.35100" in self.browser.page_source
        time.sleep(5)
        self.browser.get('http://127.0.0.1:8000/live/')
        time.sleep(10)

        # dropdowns = self.browser.find_element(
        # by=By.XPATH, value="//div[@class='ui dropdown selection']//i[@class='dropdown icon']"
        # )
        # dropdowns.click()
        # time.sleep(2)
        # select = Select(dropdowns)
        # select.select_by_index(2)

        change_button = self.browser.find_element(by=By.ID, value="submitButton")
        time.sleep(1)
        change_button.click()
        time.sleep(1)
        self.browser.get('http://127.0.0.1:8000/live/')
        time.sleep(10)
        assert "EURUSD" in self.browser.page_source
        time.sleep(2)
        self.browser.quit()

