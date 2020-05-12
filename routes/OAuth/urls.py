from django.conf.urls import include, url

from OAuth.OAuthController import OAuthController as oauth_controller


urlpatterns = [
    url(r'^strava_token_exchange/$', oauth_controller.strava_token_exchange, name="strava_token_exchange"),
    url(r'^strava_auth/$', oauth_controller.strava_auth, name="strava_auth"),
]


