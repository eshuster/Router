from rest_framework import serializers
from datetime import datetime, timedelta

from user.serializers import UserResponseSerializer

from ..models import OAuthToken

class TokenSerializer(serializers.Serializer):
    class Meta:
        model = OAuthToken

    user = UserResponseSerializer

