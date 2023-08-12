from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import login, logout, authenticate
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .tokens import account_activation_token
from rest_framework import generics, status
from .serializers import ProfileSerializer, LoginSerializer, UserSerializer, UserInfoSerializer, PasswordResetSerializer, NewPasswordSerializer
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


class ForgotPasswordView(APIView):
    serializer_class = PasswordResetSerializer
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            reset_url = f'http//localhost:8000/users/reset-password/{uid}/{token}'
            email_body = render_to_string('reset_password_email.html', {
                'reset_url':reset_url,
                'user':user
            })
            send_mail('Reset your Password',
                      email_body,
                      'mohaghegh.ar82@gmail.com',
                      [user.email],
                      html_message=email_body,
                      fail_silently=False)
            # Send email
            return Response({'message':'Password reset email sent'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordView(APIView):
    serializer_class = NewPasswordSerializer
    def post(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except:
            return Response({'error':'Invalid reset link'}, status=status.HTTP_400_BAD_REQUEST)

        if account_activation_token.check_token(user, token):
            serializer = NewPasswordSerializer(data=request.data)
            if serializer.is_valid():
                user.set_password(serializer.data.get('password'))
                user.save()
                return Response({'message':'Password reset successfully'})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':'Link expired'}, status=status.HTTP_400_BAD_REQUEST)
