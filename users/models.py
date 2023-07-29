from django.db import models
from django.utils import timezone
from PIL import Image


class Profile(models.Model):
    username = models.CharField(max_length=25, default='')
    password = models.CharField(max_length=15, default='')
    email = models.EmailField(null=False, default='')
    image = models.ImageField(null=False, default='default.jpg', upload_to='profile_pics')
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

