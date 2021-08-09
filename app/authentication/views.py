from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework.exceptions import NotAuthenticated
from .models import Authentication
from .serializers import AuthenticationSerializer
from django.contrib.auth import authenticate, login


class Signup(APIView):
    def post(self, request, format=None):
        user = Authentication.objects.create_user(
            request.data['username'],
            request.data['email'],
            request.data['password']
        )
        user = AuthenticationSerializer(user)

        return Response(user.data, status=status.HTTP_201_CREATED)


class Login(APIView):
    def post(self, request, format=None):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)

        if user.is_authenticated:
            login(request, user)
            user = AuthenticationSerializer(user)

            return Response(user.data, status=status.HTTP_200_OK)
        else:
            raise NotAuthenticated(detail="Unable to login.")
