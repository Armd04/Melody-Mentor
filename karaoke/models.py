from django.db import models
import random
import string

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

    def __str__(self):
        return f'{self.title} by {self.artist}'
