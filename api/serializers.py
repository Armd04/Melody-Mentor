from rest_framework import serializers
from .models import Course, Video

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_number', 'title', 'description', 'allowed_users']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['title', 'description', 'related_course', 'video_file', 'thumbnail']


class UpdateCourse(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'description', 'allowed_users']