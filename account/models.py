from OAuth.models import BaseOAuthModel
from django.contrib.auth.models import User

from django.db import models
from athlete.models import StravaAthlete

class StravaAccount(BaseOAuthModel):
    class Meta:
        verbose_name = 'Strava Accounts'

    strava_athelete = models.ForeignKey(StravaAthlete, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
