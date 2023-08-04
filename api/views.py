from django.shortcuts import render
from rest_framework import generics, status
from .serializers import CourseSerializer, VideoSerializer, VideoDetailSeralizer, VideoFileSerializer
from .models import Course, Video
from rest_framework.views import APIView
from rest_framework.response import Response

class CreateCourseView(generics.CreateAPIView):
    model = Course
    serializer_class = CourseSerializer

class CreateVideoView(generics.CreateAPIView):
    model = Video
    serializer_class = VideoSerializer

class UpdateCourseView(APIView):
    serializer_class = CourseSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        if not self.request.session.get('user_id', False):
            return Response({'Forbidden':'You have to login'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            course_number = serializer.validated_data.get('course_number')
            new_users = serializer.validated_data.get('allowed_users', [])
            
            queryset = Course.objects.filter(course_number=course_number)
            if queryset.exists():
                course = queryset.first()

                course.title = serializer.validated_data.get('title')
                course.description = serializer.validated_data.get('description')
                course.allowed_users.add(*new_users)

                course.save()

                return Response({'Message':'Success'}, status=status.HTTP_200_OK)
            return Response({'Not Found':'There is no course with this id'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Bad Request': 'Non proper request'})
    
class UpdateVideoDetailsView(APIView):
    serializer_class = VideoDetailSeralizer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        if not self.request.session.get('user_id', False):
            return Response({'Forbidden':'You have to login'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            video_code = serializer.validated_data.get('video_code')
            
            
            queryset = Video.objects.filter(video_code=video_code)
            if queryset.exists():
                video = queryset.first()

                video.title = serializer.validated_data.get('title', video.title)
                video.description = serializer.validated_data.get('description', video.description)
                video.thumbnail = serializer.validated_data.get('thumbnail', video.thumbnail)
                video.video_file = serializer.validated_data.get('video_file', video.video_file.path)
                video.related_course = serializer.validated_data.get('related_course', video.related_course)

                video.save()

                return Response({'Message':'Success'}, status=status.HTTP_200_OK)
            return Response({'Not Found':'There is no course with this id'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Bad Request': 'Non proper request'})

class UpdateVideoFileView(APIView):
    serializer_class = VideoFileSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        if not self.request.session.get('user_id', False):
            return Response({'Forbidden':'You have to login'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            video_code = serializer.validated_data.get('video_code')
            
            
            queryset = Video.objects.filter(video_code=video_code)
            if queryset.exists():
                video = queryset.first()

                video.video_file = serializer.validated_data.get('video_file')

                video.save()

                return Response({'Message':'Success'}, status=status.HTTP_200_OK)
            return Response({'Not Found':'There is no course with this id'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Bad Request': 'Non proper request'})