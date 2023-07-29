from django.db import models
from users.models import Profile
from PIL import Image
import random

def generate_unique_code():
    while True:
        code = random.randint(1000, 10000)
        if not Course.objects.filter(course_number=code).exists():
            break
    return code


class Course(models.Model):
    title = models.CharField(max_length=100, default='')
    course_number = models.IntegerField(default=1000)
    description = models.TextField()
    allowed_users = models.ManyToManyField(Profile, related_name='allowed_courses')

    def __str__(self):
        return self.title
    
class Video(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/', null=True)
    related_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='related_videos')
    thumbnail = models.ImageField(default='default.jpg', upload_to='video_thumbnails')



    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


