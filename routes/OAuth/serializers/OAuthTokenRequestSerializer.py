from datetime import datetime, timedelta

from rest_framework import serializers

from ..models import OAuthToken

class OAuthTokenRequestSerializer(serializers.Serializer):
    token_type = serializers.CharField(max_length=100)
    refresh_token = serializers.CharField(max_length=100)
    access_token = serializers.CharField(max_length=100)
    expires_in = serializers.IntegerField()
    expires_at = serializers.IntegerField()

    def create(self, validated_data):
        now = datetime.now()
        validated_data['expires_in'] = now + timedelta(seconds=validated_data['expires_in'])
        validated_data['expires_at'] = now + timedelta(seconds=validated_data['expires_at'])
        return OAuthToken.objects.create(**validated_data)

