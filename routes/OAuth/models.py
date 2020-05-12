import os
from datetime import timedelta

from django.db import models
from django.urls import reverse
from django.utils import timezone
from urllib.parse import urljoin
from authlib.integrations.requests_client import OAuth2Session
from authlib.integrations.django_client import OAuth
oauth = OAuth()

from OAuth.OAuthMixin import OAuthMixin
from django.contrib.auth.models import User

class BaseOAuthModel(models.Model, OAuthMixin):
    class Meta:
        abstract = True

    refresh_token = models.TextField()
    access_token = models.TextField()
    expires_at = models.DateTimeField()
    token_type = models.TextField()
    auth_url = models.TextField()


class StravaAccount(BaseOAuthModel, OAuthMixin):
    class Meta:
        verbose_name = 'Strava Account'

    client_id = os.environ['STRAVA_CLIENT_ID']
    client_secret = os.environ['STRAVA_CLIENT_SECRET']

    auth_url = "https://www.strava.com/oauth/authorize"
    access_token_url = "https://www.strava.com/oauth/token"
    base_url = "https://www.strava.com"
    refresh_url = urljoin(base_url, '/oauth/token')
    redirect_url = "http://localhost:8000/oauth/strava_token_exchange"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    client = OAuth2Session(client_id=int(client_id), client_secret=client_secret, scope="read")

    def create_authorization_url(self):
        return super().authorize(client=self.client, client_id=self.client_id, client_secret=self.client_secret, auth_url=self.auth_url, access_token_url=self.access_token_url, redirect_url=self.redirect_url)

    def get_token(self, code):
        authorization_response = super().authorize(client=self.client, client_id=self.client_id, client_secret=self.client_secret, auth_url=self.auth_url, access_token_url=self.access_token_url, redirect_url=self.redirect_url)

        response = super().get_token(self.client, self.access_token_url, authorization_response, code=code, client_id=self.client_id, client_secret=self.client_secret)
        return response

    def create_token(self):
        token = None

class OAuthToken(models.Model):
    # user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    client_id = os.environ['STRAVA_CLIENT_ID']
    client_name = models.CharField(max_length=100)
    expires_at = models.DateTimeField()
    expires_in =  models.DateTimeField()
    token_type = models.CharField(max_length=100)
    refresh_token = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



