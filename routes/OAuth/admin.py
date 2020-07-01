from django.contrib import admin

# Register your models here.

from .models import OAuthToken, StravaAccount


class OAuthTokenAdmin(admin.ModelAdmin):
    pass


admin.site.register(OAuthToken, OAuthTokenAdmin)
admin.site.register(StravaAccount)