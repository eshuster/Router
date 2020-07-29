from rest_framework.views import APIView
import requests

from ..services import StravaAccountAPICalls
from athlete.models import StravaAthlete
from shared.responses import Responses
from OAuth.serializers.OAuthSerializers import OAuthTokenRequestSerializer
from shared.responses import Responses

class StravaAuthorizationController(APIView):
    # generate link to connect to Strava
    def get(self, request):
        strava_account = StravaAccountAPICalls()

        try:
            response = strava_account.create_authorization_url()
        except requests.RequestException as e:
            return Responses.status_503(data=e)

        return Responses.status_400(data=response)



class StravaTokenExchangeController(APIView):
    # once linked is clicked, callback url is to here
    def get(self, request):

        strava_account = StravaAccountAPICalls()
        authorization_code = request.GET.get('code')

        try:
            response = strava_account.get_token(code=authorization_code)
        except requests.RequestException as e:
            return Responses.status_503(data=e)

        from datetime import datetime, timedelta

        now = datetime.now()

        response.update({'expires_in': now + timedelta(seconds=response['expires_in']),
                         'expires_at': now + timedelta(seconds=response['expires_at'])})

        user = request.user
        serializer = OAuthTokenRequestSerializer(data=dict(user_id=user.id, **response))

        if serializer.is_valid():
            athlete = user.athlete

            try:
                strava_athlete = StravaAthlete.objects.get(athlete__user_id=request.user.id)
            except:
                StravaAthlete.objects.create(**{'strava_id': response['athlete']['id'], 'athlete_id': athlete.id})
            serializer.save()

        return Responses.status_200(data=serializer.data)