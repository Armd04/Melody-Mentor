from django.db import models
from django.utils import timezone
from users.models import Profile
import random
import string

def generate_unique_post_code():
    length = 8

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if not Post.objects.filter(post_code=code).exists():
            break

    return code

class Post(models.Model):
    post_code = models.CharField(max_length=8, null=False, default=generate_unique_post_code)
    title = models.CharField(max_length=100, null=False, default='')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    

