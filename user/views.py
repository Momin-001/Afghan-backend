from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import *
from .permissions import *
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

class UserView(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=CustomUserSerializer
    permission_classes=[IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(password=make_password(self.request.data['password']))


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)