from django.db import models
from users.models import Profile
from PIL import Image
import string
import random

def generate_unique_course_number():
    while True:
        code = random.randint(1000, 10000)
        if not Course.objects.filter(course_number=code).exists():
            break
    return code

def generate_unique_video_code():
    length = 8

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if not Video.objects.filter(video_code=code).exists():
            break

    return code


class Course(models.Model):
    title = models.CharField(max_length=100, default='')
    course_number = models.IntegerField(default=generate_unique_course_number, null=False)
    description = models.TextField()
    allowed_users = models.ManyToManyField(Profile, related_name='allowed_courses')

    def __str__(self):
        return self.title
    
class Video(models.Model):
    title = models.CharField(max_length=100, default='')
    video_code = models.CharField(max_length=8, default=generate_unique_video_code, null=False)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/', null=True)
    related_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='related_videos')
    thumbnail = models.ImageField(default='default.jpg', upload_to='video_thumbnails')



    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.thumbnail.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.thumbnail.path)


