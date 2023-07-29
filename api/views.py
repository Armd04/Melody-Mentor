from django.shortcuts import render
from rest_framework import generics, status
from .serializers import CourseSerializer, VideoSerializer
from .models import Course, Video
from rest_framework.views import APIView
from rest_framework.response import responses

class CreateCourseView(generics.CreateAPIView):
    model = Course
    serializer_class = CourseSerializer

class CreateVideoView(generics.CreateAPIView):
    model = Video
    serializer_class = VideoSerializer



