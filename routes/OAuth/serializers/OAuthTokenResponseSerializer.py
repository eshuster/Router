from rest_framework import serializers
from datetime import datetime, timedelta

from ..models import OAuthToken

class TokenSerializer(serializers.ModelField):
    class Meta:
        model = OAuthToken

