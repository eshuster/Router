from django.urls import path

from account.controllers.StravaAccountController import StravaAuthorizationController as strava_auth_controller
from account.controllers.StravaAccountController import StravaTokenExchangeController as strava_token_exchange_controller


urlpatterns = [
    path('strava_auth/', strava_auth_controller.as_view(), name="strava_auth"),
    path('strava_token_exchange/', strava_token_exchange_controller.as_view(), name="strava_token_exchange"),
]


