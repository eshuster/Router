from authlib.integrations.requests_client import OAuth2Session
from authlib.integrations.django_client import OAuth
from django.contrib.auth.models import User

oauth = OAuth()

import os
from django.conf import settings
from django.db import models
from athlete.models import StravaAthlete
from OAuth.OAuthMixin import OAuthMixin

class BaseOAuthModel(models.Model, OAuthMixin):
    class Meta:
        abstract = True

    refresh_token = models.TextField()
    access_token = models.TextField()
    expires_at = models.DateTimeField()
    token_type = models.TextField()
    auth_url = models.TextField()

class OAuthToken(models.Model):
    class Meta:
        verbose_name = 'OAuth Tokens'

    def __str__(self):
        return 'OAuthToken'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    client_id = os.environ['STRAVA_CLIENT_ID'] #put in settings
    client_name = models.CharField(max_length=100, blank=True, null=True)
    expires_at = models.DateTimeField()
    expires_in = models.DateTimeField()
    token_type = models.CharField(max_length=100)
    refresh_token = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)








