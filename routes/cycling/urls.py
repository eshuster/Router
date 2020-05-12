from django.urls import path
from cycling.StravaRoutesController import StravaRoutes as strava_controller

urlpatterns = [
    path('', strava_controller.as_view()),
]
