from django.conf.urls import include, url

from account.controllers.StravaAccountController import StravaAuthorizationController as strava_auth_controller
from account.controllers.StravaAccountController import StravaTokenExchangeController as strava_token_exchange_controller


urlpatterns = [
    url(r'^strava_auth/$', strava_auth_controller.as_view(), name="strava_auth"),
    url(r'^strava_token_exchange/$', strava_token_exchange_controller.as_view(), name="strava_token_exchange"),
]


