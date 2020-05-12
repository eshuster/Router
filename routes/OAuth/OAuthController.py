import os
import requests

from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from .serializers.TokenRequestSerializer import TokenRequestSerializer

from OAuth.models import StravaAccount

class OAuthController():

    @api_view(['GET'])
    def strava_auth(request):
        strava_account = StravaAccount()

        response = strava_account.create_authorization_url()

        return Response(response)

    @api_view(['GET'])
    def strava_token_exchange(request):
        strava_account = StravaAccount()
        authorization_code = request.GET.get('code')

        response = strava_account.get_token(code=authorization_code)
        serializer = TokenRequestSerializer(data=response)
        if serializer.is_valid():
            serializer.save()


        return Response(serializer.data)
