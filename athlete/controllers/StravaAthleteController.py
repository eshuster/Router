from rest_framework.views import APIView
from rest_framework.response import Response

from user.serializers.StravaAthleteRequestSerializer import StravaAthleteRequestSerializer

class StravaAthleteController(APIView):
    def post(self, request):
        strava_id = request.data['strava_id']
        user_id = request.data['user_id']

        serializer = StravaAthleteRequestSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

