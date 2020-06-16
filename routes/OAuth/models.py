from authlib.integrations.requests_client import OAuth2Session
from authlib.integrations.django_client import OAuth
from django.contrib.auth.models import User

oauth = OAuth()

import os
from django.conf import settings
from django.db import models
from user.models import StravaAthlete
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    client_id = os.environ['STRAVA_CLIENT_ID'] #put in settings
    client_name = models.CharField(max_length=100)
    expires_at = models.DateTimeField()
    expires_in =  models.DateTimeField()
    token_type = models.CharField(max_length=100)
    refresh_token = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class StravaAccount(BaseOAuthModel, OAuthMixin):
    class Meta:
        verbose_name = 'Strava Account'

    strava_athelete = models.ForeignKey(StravaAthlete, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
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






