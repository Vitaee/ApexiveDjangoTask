# Standard Library
import json

# Third Party
from core.models import User

# Django Stuff
from django.urls import reverse

# Rest Framework
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class TestUserRegistrationLoginView(APITestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.user_data = {"username": "testuser", "password": "testpassword"}

        self.user = User.objects.create_user(
            username="testuser1", password="testpassword1"
        )

    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_login(self):
        # Register user
        self.client.post(self.register_url, self.user_data, format="json")

        # Login user
        self.token = Token.objects.create(user=self.user)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", json.loads(response.content))


class TestUserView(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.user_view_url = reverse("current_user")

    def test_user_view_authenticated(self):
        self.token = Token.objects.create(user=self.user)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.get(self.user_view_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
