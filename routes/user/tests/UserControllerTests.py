import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'routes.routes.settings'
django.setup()

from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from django.contrib.auth.models import User

class UserControllerTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
                username="test_username_alt",
	            password="Lola@2020!",
	            email="testemail@gmail.com"
        )

    def test_create_user(self):
        client = APIClient()
        data =  {
	            "username": "test_username",
	            "password": "Lola@2020!",
	            "email": "testemail@gmail.com"
                }

        res = self.client.post('/user/', data=data, format='json')

        latest_user = User.objects.latest('id')

        self.assertEqual(res.status_code, 200)

        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(latest_user.username, "test_username")
        self.assertEqual(latest_user.email, "testemail@gmail.com")

    def test_user_login(self):

        client = APIClient()
        data = {
            "username": "test_username_alt",
            "password": "Lola@2020!"
        }

        res = self.client.post('/user/login/', data=data)

        self.assertEqual(res.status_code, 200)

        self.assertEqual(res.data['username'], "test_username_alt")
        self.assertEqual(res.data['email'], "testemail@gmail.com")

