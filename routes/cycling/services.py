import requests

from OAuth.models import OAuthToken
from user.models import StravaAthlete

class StravaAPICalls:
    def get_athlete_routes(self, user_id):
        """
        query params include page and per_page which default to 1 and 30
        :return:
        """
        strava_oauth_token = OAuthToken.objects.filter(user_id=user_id).last()
        strava_athlete = StravaAthlete.objects.get(user_id=user_id)
        response = requests.get("https://www.strava.com/api/v3/athletes/{}/routes?page=1per_page=30".format(strava_athlete.strava_id),
                                headers={'Authorization': 'Bearer {}'.format(strava_oauth_token.access_token)})

        return response