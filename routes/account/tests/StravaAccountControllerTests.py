import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'routes.routes.settings'
django.setup()

from rest_framework.test import APIClient, APITestCase

class StravaAccountControllerTests(APITestCase):
    def setUp(self) -> None:
        pass


    def test_get_strava_api_token(self):
        pass

    def test_get_strava_authorization_link(self):
        pass