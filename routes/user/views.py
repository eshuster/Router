from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers.UserRequestSerializer import UserRequestSerializer

class UserController(APIView):
    def post(self, request):
        serializer = UserRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def get(self, request):
        return Response("Done")


    def login(self, request):
        return Response()

