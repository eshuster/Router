from django.db import models
from django.contrib.auth.models import User

class Athlete(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class StravaAthlete(models.Model):
    strava_id = models.CharField(max_length=100)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
