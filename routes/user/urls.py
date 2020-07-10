from django.conf.urls import url

from .controllers.UserController import UserController
from .controllers.UserController import UserLoginController
from .controllers.UserController import UserLogoutController

# from .views import UserController
urlpatterns = [
    url(r'^$', UserController.as_view()),
    url(r'^login/$', UserController.user_login, name="user_login"),
    url(r'^login_page/$', UserLoginController.as_view(), name="user_login_page"),
    url(r'^logout/$', UserController.user_logout, name="user_logout"),
    url(r'^logout_page/$', UserLogoutController.as_view(), name="user_logout_page"),
    url(r'^sathlete/$', UserController.user_login, name="create_strava_athlete"),
]

