from datetime import datetime, timedelta

from rest_framework import serializers

from ..models import OAuthToken
from user.serializers import UserResponseSerializer

class OAuthTokenRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OAuthToken
        fields = '__all__'

    user_id = serializers.CharField(max_length=100)
    token_type = serializers.CharField(max_length=100)
    refresh_token = serializers.CharField(max_length=100)
    access_token = serializers.CharField(max_length=100)
    expires_in = serializers.DateTimeField()
    expires_at = serializers.DateTimeField()

    def create(self, validated_data):
        return OAuthToken.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return instance

class TokenSerializer(serializers.Serializer):
    class Meta:
        model = OAuthToken

    user = UserResponseSerializer