from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers.OAuthTokenRequestSerializer import OAuthTokenRequestSerializer
from user.serializers import UserResponseSerializer
from account.services import StravaAccountAPICalls

class OAuthController(APIView):
    permission_classes = [IsAuthenticated,]

    @api_view(['GET'])
    def strava_auth(request):
        strava_account = StravaAccountAPICalls()
        response = strava_account.create_authorization_url()

        return Response(response)

    @api_view(['GET'])
    def strava_token_exchange(request):
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
            serializer.save()

        return Response(serializer.data)
