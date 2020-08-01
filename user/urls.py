from django.conf.urls import url
from django.urls import path

from .controllers.UserControllers import UserController
from .controllers.UserControllers import UserLoginController
from .controllers.UserControllers import UserLogoutController

# from .views import UserController
urlpatterns = [
    path('', UserController.as_view()),
    path('login/', UserLoginController.as_view(), name="user_login"),
    # path('login_page/', UserLoginController.as_view(), name="user_login_page"),
    path('logout/', UserLogoutController.as_view(), name="user_logout"),
    # path('logout_page/', UserLogoutController.as_view(), name="user_logout_page"),
]

