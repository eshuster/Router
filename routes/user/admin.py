from django.contrib import admin

from .models import Profile
from OAuth.models import StravaAccount

admin.site.register(StravaAccount)
admin.site.register(Profile)