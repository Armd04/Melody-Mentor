from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile, CheckProfile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckProfile
        fields = ['username', 'password', 'email', 'image']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, error_messages={'required':'Please provide a username.'})
    password = serializers.CharField(max_length=100, error_messages={'required':'Please provide a password.'})
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'image']

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

