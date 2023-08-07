from rest_framework import serializers
from .models import Post


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class UpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['post_code', 'title', 'content', 'author']

class DeletePostSerializer(serializers.Serializer):
    post_code = serializers.CharField(max_length=8)