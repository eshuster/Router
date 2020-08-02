from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from unittest.mock import Mock, patch

from .mock_responses import strava_authorization_url, get_strava_oauth_token

class StravaAccountControllerTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
                username="test_username_alt",
	            password="Lola@2020!",
	            email="testemail@gmail.com"
        )

    @patch('account.services.StravaAccountAPICalls.create_authorization_url', return_value=strava_authorization_url())
    def test_get_strava_authorization_url(self, mock_request):

        res = self.client.get('/oauth/strava_auth/')

        self.assertEqual(res.status_code, 200)

    @patch('account.services.StravaAccountAPICalls.get_token', return_value=get_strava_oauth_token())
    def tests_get_oauth_token_from_strava(self, mock_request):
        self.client.force_authenticate(user=self.user)
        self.client.login(username=self.user.username, password=self.user.password)
        res = self.client.get('/oauth/strava_token_exchange/')

        self.assertEqual(res.status_code, 200)



