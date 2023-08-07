from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from rest_framework import generics, status
from .serializers import ProfileSerializer, LoginSerializer, UserSerializer, UserInfoSerializer
from .models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from PIL import Image
import re


def username_acceptibility(str):
    p = re.compile('[\d\w]+')
    if (p.match(str)):
        return True
    return False

def password_acceptibility(str):
    flag_upper = False
    flag_lower = False
    flag_number = False
    flag_weird = False
    weird_list = ['!', '@', '#', '$', '%', '&', '*']
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            flag_lower = True
        if str[i] >= 'A' and str[i] <= 'Z':
            flag_upper = True
        if str[i] >= '0' and str[i] <= '9':
            flag_number = True
        if str[i] in weird_list:
            flag_weird = True
    if flag_upper and flag_lower and flag_number and flag_weird:
        return True
    return False

class ProfilesView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                self.request.session['user_id'] = user.id
                return Response({'Message':'Logged in'}, status=status.HTTP_200_OK)
            return Response({'Message':'Wrong password or username'}, status=status.HTTP_403_FORBIDDEN)
        return Response({'Bad Request': 'Non proper request'})


class RegisterView(APIView):
    serializer_class = ProfileSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            email = serializer.validated_data.get('email')
            image = serializer.validated_data.get('image', 'default.jpg')

            

            if not username_acceptibility(username):
                return Response({'Bad Request': 'Username\'s format is wrong'}, status=status.HTTP_400_BAD_REQUEST)
            
            if not password_acceptibility(serializer.data.get('password')):
                return Response({'Bad Request': 'Password\'s format is wrong'}, status=status.HTTP_400_BAD_REQUEST)

            queryset = User.objects.filter(username=username)
            if queryset.exists():
                return Response({'Bad Request': 'A user with this username already exits'},
                                 status=status.HTTP_400_BAD_REQUEST)
            
            queryset = User.objects.filter(email=email)
            if queryset.exists():
                return Response({'Bad Request': 'A user with this email already exits'}, status=status.HTTP_400_BAD_REQUEST)
            
            user = User(username=username, password=password, email=email)
            user.save()

            profile = Profile(user=user, image=image)
            profile.save()
            print(password)
            return Response({'Message':'Success'}, status=status.HTTP_201_CREATED)
        
        return Response({'Bad Request': 'Non proper request'})

class LoggedInView(APIView):

    def get(self,request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        if self.request.session.get('user_id', False):
            user = self.request.user
            profile = Profile.objects.filter(user=user).first()
            return Response(UserSerializer(profile).data, status=status.HTTP_200_OK)
        
        else:
            return Response({'Message': 'No one is there'}, status=status.HTTP_204_NO_CONTENT)
        
class LoggedInInfoView(APIView):

    def get(self,request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        if self.request.session.get('user_id', False):
            user = self.request.user
            return Response(UserInfoSerializer(user).data, status=status.HTTP_200_OK)
        
        else:
            return Response({'Message': 'No one is there'}, status=status.HTTP_204_NO_CONTENT)

class LogoutView(APIView):

    def get(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        if self.request.session.get('user_id', False):
            user = self.request.user
            logout(request=request)
            self.request.session['user_id'] = None
            return Response({'Message': 'Logout successful'}, status=status.HTTP_200_OK)
        
        else:
            return Response({'Message': 'No one is there'}, status=status.HTTP_204_NO_CONTENT)

