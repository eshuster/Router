from django.urls import path
from cycling.StravaCyclingRoutesController import StravaCyclingRoutesController as strava_cycling_routes_controller

urlpatterns = [
    path('', strava_cycling_routes_controller.as_view()),
]
