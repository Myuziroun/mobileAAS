from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Users, Games, detail_user
from .serializer import UserModelSerializer, GamesModelSerializer, detailUsersModelSerializer, UserRegistrasiModelSerializer, UserUpdateModelSerializer, UserLoginSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class UserModelAPIView(APIView):
    def get(self, request):
        users = Users.objects.all()
        serializer = UserModelSerializer(users, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    def post(self, request):
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class getUserByIDModelAPIView(APIView):
    def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserModelSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request,pk):
        user = self.get_object(pk)
        serializer = UserUpdateModelSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request, pk):
        user = Users.objects.get(pk = pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data['users']
        
        # Generate token (JWT) using simplejwt
        refresh = RefreshToken.for_user(user)
        token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        # Mengambil data pengguna yang diperlukan untuk respons
        user_data = {
            'id': user.id_user,  # Sesuaikan dengan nama atribut yang sesuai
            'nama': user.nama,
            'email': user.email,
            'created_at': user.created_at,
            # tambahkan atribut lain yang diperlukan
        }

        return Response({'token': token, 'user': user_data}, status=status.HTTP_200_OK)
class RegisterUserModelAPIView(APIView):
    def post(self, request):
        serializer = UserRegistrasiModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class gamesModelAPIView(APIView):
    def get_object(self, pk):
        try:
            return Games.objects.get(pk=pk)
        except Games.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            game = self.get_object(pk)
            serializer = GamesModelSerializer(game)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            games = Games.objects.all()
            serializer = GamesModelSerializer(games, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GamesModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        game = self.get_object(pk)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
