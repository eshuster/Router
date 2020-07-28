import os
import requests

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User

from user.serializers.StravaAthleteRequestSerializer import StravaAthleteRequestSerializer

class StravaCyclingRoutesController(APIView):
    def post(self, request):
        strava_id = request.data['strava_id']
        user_id = request.data['user_id']

        serializer = StravaAthleteRequestSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

