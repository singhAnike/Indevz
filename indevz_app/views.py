from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, serializers
from django.contrib.auth import login, authenticate
from rest_framework.authtoken.models import Token
from indevz_app.models import CustomUser 

class SignupAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SigninAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UsersApi(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        user_id= serializers.IntegerField(source='id')

        class Meta:
            model= CustomUser
            fields=['user_id', 'username', 'email', 'phone', 'company_name', 'access_code', 'password']
            
    def get(self, request,*args, **kwargs):
        users = CustomUser.objects.all()
        serializer=self.OutputSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
