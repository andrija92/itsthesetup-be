from rest_framework import viewsets

from api.serializers import TestSerializer
from .models import Test
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
import os
from dotenv import load_dotenv
from api.helpers.jwt import generateToken, generateRefreshToken

load_dotenv()

class TestView(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class LoginView(APIView):
    
    JWT_NAME = os.getenv("JWT_NAME")
    JWT_REFRESH_NAME = os.getenv("JWT_REFRESH_NAME")

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)
        if user:
            token = generateToken(email, str(user.id))
            refresh_token = generateRefreshToken(email, str(user.id))
            return Response({'message': 'Login successful', "data": { self.JWT_NAME: token, self.JWT_REFRESH_NAME: refresh_token} })
        else:
            return Response({'message': 'Invalid credentials'}, status=401)

    
class RegisterView(APIView):
    JWT_NAME = os.getenv("JWT_NAME")
    JWT_REFRESH_NAME = os.getenv("JWT_REFRESH_NAME")

    def post(self, request):
        user_model = get_user_model()
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = user_model.objects.create_user(username=email, password=password)
            token = generateToken(email, str(user.id))
            refresh_token = generateRefreshToken(email, str(user.id))
            return Response({'message': 'Registered successfully', "data": { self.JWT_NAME: token, self.JWT_REFRESH_NAME: refresh_token} })
        except Exception as e:
            return Response({'message': 'Failed to register', "error": str(e)}, status=400)


class LogoutView(APIView):
    def get(self, request):
        print(request.user)
        return Response({'message': 'Logged out successfully'})