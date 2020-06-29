from django.conf.urls import url

from .controllers.UserController import UserController

# from .views import UserController
urlpatterns = [
    url(r'^$', UserController.as_view()),
    url(r'^login/$', UserController.user_login, name="user_login"),
]

