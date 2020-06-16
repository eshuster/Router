from rest_framework import serializers

from django.contrib.auth.models import User

class UserRequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return User.objects.create(**validated_data)