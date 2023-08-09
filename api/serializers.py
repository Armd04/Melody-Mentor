from rest_framework import serializers
from .models import Course, Video

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_number', 'title', 'description', 'allowed_users']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['video_code', 'title', 'description', 'related_course', 'video_file', 'thumbnail']

class VideoDetailSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['video_code', 'title', 'description', 'related_course', 'thumbnail']

class VideoFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['video_code', 'video_file']

class CourseAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class VideoAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
