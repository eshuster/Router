from authlib.integrations.django_client import OAuth

oauth = OAuth()

from authlib.integrations.requests_client import OAuth2Session

from django.conf import settings
from OAuth.OAuthMixin import OAuthMixin

class StravaAccountAPICalls(OAuthMixin):
    client = OAuth2Session(client_id=int(settings.STRAVA_CLIENT_ID),
                           client_secret=settings.SOCIAL_AUTH_STRAVA_KEY,
                           scope="read")

    def create_authorization_url(self):
        return super().authorize(client=self.client, client_id=settings.STRAVA_CLIENT_ID,
                                 client_secret=settings.SOCIAL_AUTH_STRAVA_KEY,
                                 auth_url=settings.STRAVA_AUTH_URL, access_token_url=settings.STRAVA_ACCESS_TOKEN_URL,
                                 redirect_url= settings.STRAVA_REDIRECT_URL)

    def get_token(self, code):
        authorization_response = super().authorize(client=self.client, client_id=settings.STRAVA_CLIENT_ID,
                                                   client_secret=settings.SOCIAL_AUTH_STRAVA_KEY,
                                                   auth_url=settings.STRAVA_AUTH_URL,
                                                   access_token_url=settings.STRAVA_ACCESS_TOKEN_URL,
                                                   redirect_url= settings.STRAVA_REDIRECT_URL)

        response = super().get_token(self.client, settings.STRAVA_ACCESS_TOKEN_URL, authorization_response, code=code,
                                     client_id=settings.STRAVA_CLIENT_ID, client_secret=settings.SOCIAL_AUTH_STRAVA_KEY)
        return response