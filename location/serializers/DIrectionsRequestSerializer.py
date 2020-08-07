from rest_framework import serializers

class DirectionsRequestSerializer(serializers.ModelSerializer):
    origin = serializers.CharField(max_length=100)
    origin_type = serializers.CharField(max_length=100)
    destination = serializers.CharField(max_length=100)
    destination_type = serializers.CharField(max_length=100)
    mode = serializers.CharField(max_length=100)
    waypoints = serializers.CharField(max_length=100)
    waypoints_type = serializers.CharField(max_length=100)
    avoid = serializers.CharField(max_length=100)

    def validate(self, data):
        if data['origin_type'] == 'geo_coordinates':
           try:
               coordinates = int(data['origin'])
           except:
               raise serializers.ValidationError('origin must be a float value')

        if data['destination_type'] == 'geo_coordinates':
            try:
                coordinates = int(data['destination'])
            except:
                raise serializers.ValidationError('origin must be a float value')
        return data