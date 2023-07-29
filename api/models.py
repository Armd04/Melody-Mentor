from django.db import models
from users.models import Profile

class Course(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField()
    allowed_users = models.ManyToManyField(Profile, related_name='allowed_courses')

    def __str__(self):
        return self.title
    
class Video(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/', null=True)
    related_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='related_videos')


    def __str__(self):
        return self.title

