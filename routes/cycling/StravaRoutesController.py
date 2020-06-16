import os
import requests

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User

class StravaRoutes(APIView):

    def get(self, request):
        user = User.objects.create_user(username=request.query_params['username'], password=request.query_params['password'], email=None)
        return Response(user)