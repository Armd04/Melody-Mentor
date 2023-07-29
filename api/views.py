from django.shortcuts import render
from rest_framework import generics, status
from .serializers import CourseSerializer, VideoSerializer, UpdateCourse
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
            self.request.session['is_authenticated'] = False

        if not self.request.session.get('is_authenticated', False):
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

                print(new_users.data)

                course.save()

                return Response({'Message':'Success'}, status=status.HTTP_200_OK)
            return Response({'Not Found':'There is no course with this id'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Bad Request': 'Non proper request'})