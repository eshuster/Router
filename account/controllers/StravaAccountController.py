from rest_framework.views import APIView

import requests

from ..services import StravaAccountAPICalls
from athlete.models import StravaAthlete
from OAuth.serializers.OAuthSerializers import OAuthTokenRequestSerializer
from shared.responses import Responses

class StravaAuthorizationController(APIView, Responses):
    # generate link to connect to Strava
    def get(self, request):
        strava_account = StravaAccountAPICalls()

        try:
            response = strava_account.create_authorization_url()
            return self.status_200(data=response)
        except requests.RequestException as e:
            return self.status_503(data=e)

        return self.status_400(data=response)

class StravaTokenExchangeController(APIView, Responses):
    # once linked is clicked, callback url is to here
    def get(self, request):

        strava_account = StravaAccountAPICalls()
        authorization_code = request.GET.get('code')

        try:
            response = strava_account.get_token(code=authorization_code)
        except requests.RequestException as e:
            return self.status_503(data=e)

        from datetime import datetime, timedelta

        now = datetime.now()

        response.update({'expires_in': now + timedelta(seconds=response['expires_in']),
                         'expires_at': now + timedelta(seconds=response['expires_at'])})

        user = request.user
        serializer = OAuthTokenRequestSerializer(data=dict(user_id=user.id, **response))


        if not serializer.is_valid():
            return self.status_400(data=serializer.errors)

        serializer.save()
        athlete = user.athlete
        try:
            strava_athlete = StravaAthlete.objects.get(athlete=athlete)

        except:
            StravaAthlete.objects.create(**{'strava_id': response['athlete']['id'], 'athlete_id': athlete.id})


        return self.status_200(data=serializer.data)

