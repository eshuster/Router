from django.contrib import admin

# Register your models here.

from .models import Athlete, StravaAthlete


class AthleteAdmin(admin.ModelAdmin):
    pass
class StravaAthleteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Athlete, AthleteAdmin)
admin.site.register(StravaAthlete, StravaAthleteAdmin)