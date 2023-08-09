from rest_framework import serializers
from .models import KaraokeSong

class KaraokeSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = KaraokeSong
        fields = ['song_code', 'title', 'artist', 'lyrics', 'mp3_file', 'image']

class KaraokeSongAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = KaraokeSong
        fields = '__all__'
