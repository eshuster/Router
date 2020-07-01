import os
import requests

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User

from .services import StravaAPICalls

class StravaCyclingRoutesController(APIView):

    def get(self, request):
        strava_api = StravaAPICalls()

        try:
            strava_cycling_routes = strava_api.get_athlete_routes()
        except:
            return Response

        return Response(strava_cycling_routes)