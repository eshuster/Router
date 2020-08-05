from django.db import models

class Location(models.Model):
    latitude = models.DecimalField()
    longitude = models.DecimalField()

class BaseLocationInfo(models.Model):

    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Place(BaseLocationInfo):
    class TypeChoices(models.IntegerChoices):
        ADDRESS = 1
        PREMISE = 2
        COORDINATES = 3

    name = models.CharField(default="Residential")
    type = models.IntegerField(choices=TypeChoices.choices, required=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Route(models.Model):
    name = models.CharField()
    start_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='start_location')
    end_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='end_location')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class MapUnit(models.Model):
    class TypeChoices(models.IntegerChoices):
        Leg = 1
        Step = 2

    start_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='start_location')
    end_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='end_location')
    type = models.IntegerField(choices=TypeChoices.choices, required=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

