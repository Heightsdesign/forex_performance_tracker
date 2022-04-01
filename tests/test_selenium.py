from django.test import TestCase
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException


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
        time.sleep(1)
        # Verifies if Pur Beurre is in the title of the page
        assert 'Quren' in self.browser.title
        assert self.user.username in self.browser.page_source

        # Gets the users page

        # For production environment
        # browser.get('http://159.65.51.134:80/users/{}/')

        # For local environment
        self.browser.get('http://127.0.0.1:8000/users/{}/'.format(self.user.id))

        # Verifies if the user's first_name is on the page

        """
        favorites_page_button = self.browser.find_element(by=By.ID, value="favorites")
        self.assertTrue(favorites_page_button)
        favorites_page_button.click()
        time.sleep(1)
        """

        self.browser.quit()
