from django.contrib import admin

# Register your models here.

from .models import OAuthToken
from account.models import StravaAccount


class OAuthTokenAdmin(admin.ModelAdmin):
    pass


admin.site.register(OAuthToken, OAuthTokenAdmin)
admin.site.register(StravaAccount)