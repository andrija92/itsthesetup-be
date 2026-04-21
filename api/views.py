from rest_framework import viewsets, filters

from api.serializers import SetupDetailSerializer, SetupListSerializer
from .models import Setup
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate, get_user_model
import os
from dotenv import load_dotenv
from api.helpers.jwt import generateToken, generateRefreshToken
from rest_framework_simplejwt.tokens import RefreshToken


load_dotenv()

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

        if not email or not password:
            return Response({'error': 'Email and password required'}, status=400)
        if user_model.objects.filter(username=email).exists():
            return Response({'error': 'User already exists'}, status=400)

        try:
            user = user_model.objects.create_user(username=email, password=password)
            token = RefreshToken.for_user(user)
            return Response({'message': 'Registered successfully', "data": { self.JWT_NAME: str(token.access_token), self.JWT_REFRESH_NAME: str(token)} })
        except Exception as e:
            print(e)
            return Response({'message': 'Failed to register', "error": str(e)}, status=400)


class LogoutView(APIView):
    def get(self, request):
        # treba izbrisat refresh token iz baze
        print(request.user)
        return Response({'message': 'Logged out successfully'})


class SetupView(viewsets.ModelViewSet):
    queryset = Setup.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['track__name', 'car__full_name', 'title']

    def get_serializer_class(self):
        if self.action == 'list':
            return SetupListSerializer
        
        return SetupDetailSerializer

    def get_queryset(self):
        if self.action == 'list':
            print("user", self.request.user)
            game = self.request.query_params.get('game')
            qs = Setup.objects.select_related('user', 'track', 'car', 'game')
            if game and not game == 'all':
                qs = qs.filter(game__short_name__iexact=game)

            return qs

        return Setup.objects.select_related('user', 'track', 'car', 'game', 'setup_data')

    @action(detail=False, methods=['get'], url_path='my')
    def my_setups(self, request):
        user = request.user
        print(user)
        qs = Setup.objects.select_related('user', 'track', 'car', 'game')
        qs = qs.filter(user=user)
        serializer = SetupListSerializer(qs, many=True)
        return Response(serializer.data)