from django.conf.urls import url

from .controllers.UserController import UserController

# from .views import UserController
urlpatterns = [
    url(r'^$', UserController.as_view()),
]
