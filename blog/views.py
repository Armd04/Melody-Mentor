from typing import Optional
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics, status
from .serializers import PostSerializer, CreatePostSerializer, UpdatePostSerializer, DeletePostSerializer
from .models import Post
from api.views import If_is_staff
from rest_framework.views import APIView
from rest_framework.response import Response


class PostsView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostSerializer

class CreatePostView(If_is_staff, LoginRequiredMixin, generics.CreateAPIView):
    model = Post
    serializer_class = CreatePostSerializer


class UpdatePostView(LoginRequiredMixin, APIView):
    serializer_class = UpdatePostSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        if not self.request.session.get('user_id', False):
            return Response({'Forbidden':'You have to login'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            code = serializer.validated_data.get('post_code')

            queryset = Post.objects.filter(post_code=code)
            if not queryset.exists():
                return Response({'Not Found':'A post with this code was not found'}, status=status.HTTP_404_NOT_FOUND)
            
            post = queryset.first()

            post.title = serializer.validated_data.get('title', post.title)
            post.author = serializer.validated_data.get('author', post.author)
            post.content = serializer.validated_data.get('content', post.content)

            if not self.request.user == post.author:
                return Response({'Forbidden':'You can not update this post'}, status=status.HTTP_403_FORBIDDEN)
            
            post.save()

            return Response({'Message':'Success'}, status=status.HTTP_200_OK)
        
        return Response({'Bad Request':'Non proper request'}, status=status.HTTP_400_BAD_REQUEST)


class DeletePostView(LoginRequiredMixin, APIView):
    serializer_class = DeletePostSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        if not self.request.session.get('user_id', False):
            return Response({'Forbidden':'You have to login'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            code = serializer.validated_data.get('post_code')

            queryset = Post.objects.filter(post_code=code)
            if not queryset.exists():
                return Response({'Not Found':'A post with this code was not found'}, status=status.HTTP_404_NOT_FOUND)
            
            post = queryset.first()

            if not self.request.user == post.author:
                return Response({'Forbidden':'You can not delete this post'}, status=status.HTTP_403_FORBIDDEN)
            post.delete()

            return Response({'Message':'Success'}, status=status.HTTP_200_OK)
        
        return Response({'Bad Request':'Non proper request'}, status=status.HTTP_400_BAD_REQUEST)

class GetAllPosts(APIView):
    serializer_class = PostSerializer
    def get(self, request, format=None):
        serializer = self.serializer_class(Post.objects.all(), many=True)
        return Response(serializer.data)


class PostDetails(APIView):
    serializer_class = PostSerializer
    def get(self, requset, code):
        queryset = Post.objects.filter(post_code=code)
        if not queryset.exists():
                return Response({'Not Found':'A post with this code was not found'}, status=status.HTTP_404_NOT_FOUND)
        
        post = queryset.first()

        return Response(self.serializer_class(post).data)
