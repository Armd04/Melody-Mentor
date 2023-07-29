from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'password', 'email', 'image']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'password']


