from django.shortcuts import render
from rest_framework import generics, status
from .serializers import ProfileSerializer, LoginSerializer
from .models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from hashlib import sha256
from PIL import Image
import re


def make_hash(str):
    return sha256(str.encode('utf-8')).hexdigest()


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
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
            self.request.session['is_authenticated'] = False

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = make_hash(serializer.data.get('password'))


            queryset = Profile.objects.filter(username=username)
            if not queryset.exists():
                return Response({'User Not Found': 'Invalid username.'}, status=status.HTTP_404_NOT_FOUND)
            else:
                profile = Profile.objects.filter(username=username).first()

                if profile.password == password:
                    self.request.session['user_id'] = profile.id
                    self.request.session['is_authenticated'] = True
                    return Response({'Message': 'Logged in'}, status=status.HTTP_200_OK)
                else:
                    return Response({'Bad Request': 'Wrong password'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'Bad Request': 'Non proper request'})


class RegisterView(APIView):
    serializer_class = ProfileSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = make_hash(serializer.validated_data.get('password'))
            email = serializer.validated_data.get('email')
            image = serializer.validated_data.get('image', 'default.jpg')

            

            if not username_acceptibility(username):
                return Response({'Bad Request': 'Username\'s format is wrong'}, status=status.HTTP_400_BAD_REQUEST)
            
            if not password_acceptibility(serializer.data.get('password')):
                return Response({'Bad Request': 'Password\'s format is wrong'}, status=status.HTTP_400_BAD_REQUEST)

            queryset = Profile.objects.filter(username=username)
            if queryset.exists():
                return Response({'Bad Request': 'A user with this username already exits'},
                                 status=status.HTTP_400_BAD_REQUEST)
            
            queryset = Profile.objects.filter(email=email)
            if queryset.exists():
                return Response({'Bad Request': 'A user with this email already exits'}, status=status.HTTP_400_BAD_REQUEST)
            
            profile = Profile(username=username, password=password, email=email, image=image)
            profile.save()

            return Response({'Message':'Success'}, status=status.HTTP_201_CREATED)
        
        return Response({'Bad Request': 'Non proper request'})

class LoggedInView(APIView):

    def get(self,request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
            self.request.session['is_authenticated'] = False
        
        if self.request.session.get('is_authenticated', False):
            user = Profile.objects.filter(id=self.request.session.get('user_id')).first()
            return Response(ProfileSerializer(user).data, status=status.HTTP_200_OK)
        
        else:
            return Response({'Message': 'No one is there'}, status=status.HTTP_204_NO_CONTENT)

class LogoutView(APIView):

    def get(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
            self.request.session['is_authenticated'] = False
        
        if self.request.session.get('is_authenticated', False):
            self.request.session['is_authenticated'] = False
            self.request.session.pop('user_id')
            return Response({'Message': 'Logout successful'}, status=status.HTTP_200_OK)
        
        else:
            return Response({'Message': 'No one is there'}, status=status.HTTP_204_NO_CONTENT)

