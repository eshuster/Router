from rest_framework.views import APIView
from rest_framework.response import Response

from ..services import StravaAccountAPICalls
from OAuth.serializers.OAuthTokenRequestSerializer import OAuthTokenRequestSerializer

from athlete.models import StravaAthlete, Athlete

class StravaAuthorizationController(APIView):
    # generate link to connect to Strava
    def get(self, request):
        strava_account = StravaAccountAPICalls()
        response = strava_account.create_authorization_url()

        return Response(response)


class StravaTokenExchangeController(APIView):
    # once linked is clicked, callback url is to here
    def get(self, request):


        strava_account = StravaAccountAPICalls()
        authorization_code = request.GET.get('code')

        response = strava_account.get_token(code=authorization_code)
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

        return Response(serializer.data)