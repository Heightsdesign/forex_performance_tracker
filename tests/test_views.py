from django.test import TestCase, RequestFactory
from django.urls import reverse
from users.models import User, Strategy
from trades.models import Trade, CurrencyPair
from live.models import UserSettings
from users.views import user_page, sign_up, login, logout_view
from info.views import about_us, legal
from live.views import homepage, index

# Create your tests here.


class UserPageTestCase(TestCase):
    def setUp(self):

        # Sets the request factory
        self.factory = RequestFactory()

        # Creates the user for the tests
        self.user = User.objects.create_user(
            email="test@gmail.com",
            password="test123",
            first_name="test",
            username="test",
            last_name=None,
            country=None,
            city=None,
            zip_code=None,
            address=None,
            capital=10000.00,
        )

        self.currency_pair = CurrencyPair.objects.create(name="EURUSD")

    def test_user_page_returns_200(self):

        user_id = self.user.id

        # Gets the response from client
        response = self.client.get(reverse("users:user_page", args=(user_id,)))

        # Checking if status code is equal to 200
        self.assertEqual(response.status_code, 200)

    def test_add_trade_post_request(self):

        user_id = self.user.id
        intial_trades_count = Trade.objects.all().count()

        mock_post_data = {
            "tradeButton": "tradeButton",
            "currency_pair": "EURUSD",
            "entry_point": "1.12100",
            "exit_point": "1.12200",
            "position": "BUY",
            "profit": 100.00,
        }

        response = self.client.post(f"/users/{user_id}/", data=mock_post_data)
        final_trades_count = Trade.objects.all().count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(final_trades_count, intial_trades_count + 1)

    def test_add_strategy_post_request(self):

        user_id = self.user.id
        initial_strategy_count = Strategy.objects.all().count()
        mock_post_data = {
            "stratButton": "stratButton",
            "content": "Test content",
        }

        response = self.client.post(f"/users/{user_id}/", data=mock_post_data)
        final_strategy_count = Strategy.objects.all().count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(final_strategy_count, initial_strategy_count + 1)


class SignUpPageTestCase(TestCase):
    def setUp(self):

        # Sets the request factory
        self.factory = RequestFactory()

    def test_sign_up_page_returns_200(self):

        self.request = self.factory.get("/users/sign_up")

        response = sign_up(self.request)
        self.assertEqual(response.status_code, 200)

    def test_user_creation(self):

        # Gets all users
        all_users = User.objects.all()

        # Counts the users
        initial_count = all_users.count()

        # Builds the request for subscription
        self.request = self.factory.post(
            "/users/sign_up",
            {
                "email": "test2@gmail.com",
                "username": "test2",
                "password": "pass123",
                "capital": 10000.00,
            },
        )

        # Sends the request and stores the response
        response = sign_up(self.request)

        # Checks the count of users after the request
        new_count = all_users.count()

        # Checks if a user was added to the db
        self.assertEqual(new_count, initial_count + 1)

        # Checks if the response's status code is 200
        self.assertEqual(response.status_code, 200)


class LogInPageTestCase(TestCase):
    def setUp(self):

        # Sets the request factory
        self.factory = RequestFactory()

        # Creates the user for the tests
        self.user = User.objects.create_user(
            email="test@gmail.com",
            password="test123",
            first_name="test",
            username="test",
            last_name=None,
            country=None,
            city=None,
            zip_code=None,
            address=None,
            capital=10000.00,
        )

    def test_login_page_returns_200(self):

        self.request = self.factory.get("/users/login/")
        response = login(self.request)
        self.assertEqual(response.status_code, 200)

    def test_login_successful(self):

        self.request = self.factory.post(
            "/users/login/",
            {"email": self.user.email, "password": self.user.password},
        )

        self.response = login(self.request)
        self.assertTrue(self.user.is_authenticated)

        self.assertEqual(self.response.status_code, 200)

    def test_login_unsuccessful(self):

        self.request = self.factory.post(
            "/users/login/",
            {"email": "wrong@mail", "password": "wrong123"},
        )

        self.response = login(self.request)
        self.assertContains(
            self.response,
            "WRONG EMAIL OR PASSWORD",
            html=True
        )

    def test_thank_you_returns_200(self):

        self.request = self.factory.post(
            "/users/login/",
            {"email": self.user.email, "password": self.user.password},
        )
        request = self.factory.get("/users/thank_you.html")
        response = login(request)
        self.assertEqual(response.status_code, 200)


class PerformancePageTestCase(TestCase):
    def setUp(self):
        # Sets the request factory
        self.factory = RequestFactory()

        # Creates the user for the tests
        self.user = User.objects.create_user(
            email="test@gmail.com",
            password="test123",
            first_name="test",
            username="test",
            last_name=None,
            country=None,
            city=None,
            zip_code=None,
            address=None,
            capital=10000.00,
        )

    def test_user_page_returns_200(self):

        user_id = self.user.id

        # Gets the response from client
        response = self.client.get(reverse(
            "users:performance",
            args=(user_id,)
        ))

        # Checking if status code is equal to 200
        self.assertEqual(response.status_code, 200)


class InfoViewsTestCase(TestCase):
    def setUp(self):

        # Sets the request factory
        self.factory = RequestFactory()

    def test_about_us_page_returns_200(self):

        self.request = self.factory.get("/info/about_us")
        response = about_us(self.request)
        self.assertEqual(response.status_code, 200)

    def test_legal_page_returns_200(self):

        self.request = self.factory.get("/info/legal")
        response = legal(self.request)
        self.assertEqual(response.status_code, 200)


class LiveViewsTestCase(TestCase):
    def setUp(self):

        # Sets the request factory
        self.factory = RequestFactory()

        # Creates the user for the tests
        self.user = User.objects.create_user(
            email="test@gmail.com",
            password="test123",
            first_name="test",
            username="test",
            last_name=None,
            country=None,
            city=None,
            zip_code=None,
            address=None,
            capital=10000.00,
        )

        self.pair_eurusd = CurrencyPair.objects.create(name="EURUSD")

        self.pair_usdjpy = CurrencyPair.objects.create(name="USDJPY")

    def test_homepage_returns_200(self):

        self.request = self.factory.get("/")
        response = homepage(self.request)
        self.assertEqual(response.status_code, 200)

    def test_index_returns_200(self):

        self.request = self.factory.get("/live/")
        self.request.user = self.user
        response = index(self.request)
        self.assertEqual(response.status_code, 200)

    def test_index_returns_200_with_settings(self):

        self.request = self.factory.get("/live/")
        self.request.user = self.user

        self.user_settings = UserSettings.objects.create(
            user=self.user, currency_graph=self.pair_eurusd, time_frame="DAY"
        )

        response = index(self.request)
        self.assertEqual(response.status_code, 200)

    def test_add_settings_post_request_end_usd(self):

        initial_settings_count = UserSettings.objects.all().count()
        mock_post_data = {
            "currency_pair": "EURUSD",
            "time_frame": "DAY",
        }
        self.request = self.factory.post("/live/", data=mock_post_data)
        self.request.user = self.user

        response = index(self.request)
        final_settings_count = UserSettings.objects.all().count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(final_settings_count, initial_settings_count + 1)

    def test_add_settings_post_request_start_usd(self):

        initial_settings_count = UserSettings.objects.all().count()
        mock_post_data = {
            "currency_pair": "USDJPY",
            "time_frame": "WEEK",
        }
        self.request = self.factory.post("/live/", data=mock_post_data)
        self.request.user = self.user

        response = index(self.request)
        final_settings_count = UserSettings.objects.all().count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(final_settings_count, initial_settings_count + 1)
