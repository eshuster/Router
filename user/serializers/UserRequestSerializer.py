from rest_framework import serializers

from django.contrib.auth.models import User

from athlete.models import Athlete

class UserRequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        return user