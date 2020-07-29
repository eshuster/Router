from django.urls import path
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cyroutes/', include("cycling.urls")),
    path('oauth/', include("OAuth.urls")),
    path('user/', include("user.urls"))
]

