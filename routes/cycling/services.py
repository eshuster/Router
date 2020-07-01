import requests

from OAuth.models import OAuthToken

class StravaAPICalls:
    def get_athlete_routes(self):
        """
        query params include page and per_page which default to 1 and 30
        :return:
        """
        strava_oauth_token = OAuthToken.objects.latest('id')
        response = requests.get("https://www.strava.com/api/v3/athletes/{}/routes?page=1per_page=30".format(strava_oauth_token.client_id),
                                headers={'Authorization': 'Bearer {}'.format(strava_oauth_token.access_token)})

        return response