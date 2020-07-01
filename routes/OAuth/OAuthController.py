import os
import requests

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers.OAuthTokenRequestSerializer import OAuthTokenRequestSerializer
from user.serializers import UserResponseSerializer
from .models import StravaAccount

class OAuthController(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication,]
    permission_classes = [IsAuthenticated,]

    @api_view(['GET'])
    # @authentication_classes([SessionAuthentication, BasicAuthentication])
    # @permission_classes([IsAuthenticated])
    def strava_auth(request):
        strava_account = StravaAccount(APIView)

        response = strava_account.create_authorization_url()

        return Response(response)

    @api_view(['GET'])
    def strava_token_exchange(request):
        strava_account = StravaAccount()
        authorization_code = request.GET.get('code')

        response = strava_account.get_token(code=authorization_code)
        from datetime import datetime, timedelta

        now = datetime.now()

        response.update({'expires_in': now + timedelta(seconds=response['expires_in']),
                         'expires_at': now + timedelta(seconds=response['expires_at'])})

        user = request.user
        user_serializer = UserResponseSerializer.UserResponseSerializer(user)

        serializer = OAuthTokenRequestSerializer(data=dict(user=user_serializer.data, **response))

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
