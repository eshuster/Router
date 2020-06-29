from django.db import models

# Create your models here.
from django.db import models

class Route(models.Model):
    name = models.CharField(max_length=250)
    distance = models.DecimalField(blank=True, null=True, decimal_places=2)
    elevation_gain = models.IntegerField(blank=True, null=True)
    # type = models.IntegerField(blank=True, null=True)
    # sub_type = models.IntegerField(blank=True, null=True)

class Segment(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=250)
    activity_type = models.CharField(max_length=250)
    distance = models.DecimalField(blank=True, null=True, decimal_places=2)
    # average_grade
    # maximum_grade
    elevation_high = models.IntegerField(blank=True, null=True)
    elevation_low = models.IntegerField(blank=True, null=True)
    start_latlng = models.DecimalField(blank=True, null=True, decimal_places=5)
    end_latlng = models.DecimalField(blank=True, null=True, decimal_places=5)
    climb_category = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
