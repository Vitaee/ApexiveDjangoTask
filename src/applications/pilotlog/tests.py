from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from core.models import User
from django.urls import reverse

class TestAircraftViewSet(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
       

    def test_get_aircraft_list_empty_response(self):
        response = self.client.get(reverse('aircraft-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 0)


class TestFlightViewSet(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
       
    def test_get_flight_list_empty_response(self):
        response = self.client.get(reverse('flight-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 0)
