from rest_framework import serializers
from ..models import StravaAthlete

class StravaAthleteRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StravaAthlete
        fields = '__all__'