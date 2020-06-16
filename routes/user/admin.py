from django.contrib import admin

from user.models import UserProfile
from OAuth.models import StravaAccount

admin.site.register(StravaAccount)
admin.site.register(UserProfile)