from django.db import models
import random
import string
from PIL import Image

def generate_unique_song_code():
    length = 8

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if not KaraokeSong.objects.filter(song_code=code).exists():
            break

    return code

class KaraokeSong(models.Model):
    song_code = models.CharField(max_length=8, default=generate_unique_song_code, null=False)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    lyrics = models.TextField()
    mp3_file = models.FileField(upload_to='karaoke-songs/', null=True)
    image = models.ImageField(upload_to='music-photos/', null=True)

    def __str__(self):
        return f'{self.title} by {self.artist}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
