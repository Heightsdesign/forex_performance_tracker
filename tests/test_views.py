from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth import authenticate
from users.models import User
from users.views import user_page, sign_up, login, logout_view
from django.contrib import messages

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

    def test_user_page_returns_200(self):

        user_id = self.user.id

        # Gets the response from client
        response = self.client.get(reverse("users:user_page", args=(user_id,)))

        # Checking if status code is equal to 200
        self.assertEqual(response.status_code, 200)


class SignUpPageTestCase(TestCase):

    def setUp(self):

        # Sets the request factory
        self.factory = RequestFactory()

    def test_sign_up_page_returns_200(self):

        self.request = self.factory.get(
            "/users/sign_up"
        )

        response = sign_up(self.request)

        self.assertEqual(response.status_code, 200)
