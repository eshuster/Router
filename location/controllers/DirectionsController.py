from rest_framework.views import APIView

import requests

from shared.responses import Responses
from ..services.google_directions_services import GoogleDirectionsAPI

class DirectionController(APIView, Responses):
    def get(self, request, origin, destination, mode, waypoints, avoid):
        google_direction_services =  GoogleDirectionsAPI()

        try:
            response = google_direction_services.get_directions(request, origin, destination, mode, waypoints, avoid)
            return self.status_200(data=response)
        except requests.RequestException as e:
            return self.status_503(data=e)
