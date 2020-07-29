from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import redirect
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

from shared.responses import Responses
from ..serializers.UserRequestSerializer import UserRequestSerializer
from ..serializers.UserResponseSerializer import UserResponseSerializer

class UserController(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = UserRequestSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Responses.status_200(data=serializer.data)

        return Responses.status_400(data=serializer.errors)

    def get(self, request):
        # return render(request, 'login.html')
        return Response("Done")

    @api_view(['POST'])
    def user_login(request):
        # Like before, obtain the context for the user's request.

        # If the request is a HTTP POST, try to pull out the relevant information.
        if request.method == 'POST':
            # Gather the username and password provided by the user.
            # This information is obtained from the login form.
            username = request.data['username']
            password = request.data['password']

            # Use Django's machinery to attempt to see if the username/password
            # combination is valid - a User object is returned if it is.
            user = authenticate(username=username, password=password)

            # If we have a User object, the details are correct.
            # If None (Python's way of representing the absence of a value), no user
            # with matching credentials was found.
            if user:
                # Is the account active? It could have been disabled.
                if user.is_active:
                    # If the account is valid and active, we can log the user in.
                    # We'll send the user back to the homepage.
                    login(request, user)
                    user = UserResponseSerializer(user)
                    return Responses.status_200(data=user.data)
                else:
                    # An inactive account was used - no logging in!
                    return Responses.status_403(data="Your account is disabled.")
            else:
                # Bad login details were provided. So we can't log the user in.
                print
                "Invalid login details: {0}, {1}".format(username, password)
                return Responses.status_400(data="Invalid login details supplied.")

        # The request is not a HTTP POST, so display the login form.
        # This scenario would most likely be a HTTP GET.
        else:
            # No context variables to pass to the template system, hence the
            # blank dictionary object...
            return Responses.status_400('Failed')

    @api_view(['POST'])
    def user_logout(request):
        # Like before, obtain the context for the user's request.
        logout(request)
        return Responses.status_200(data="Logged Out")


class UserLoginController(APIView):
    def get(self, request):
        return render(request, 'login.html')

class UserLogoutController(APIView):
    def get(self, request):
        return render(request, 'login.html')