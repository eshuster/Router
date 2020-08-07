import requests

from django.conf import settings

class GoogleDirectionsAPI:
    def get_directions(self, origin, destination, mode, waypoints, avoid):
            response = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin={}&destination={}\
                &waypoints={}&mode={}&avoid={}&key={}')\
                .format(origin, destination, waypoints, mode, avoid, settings['GOOGLE_API_KEY'])

            return response