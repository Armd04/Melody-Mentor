from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import KaraokeSongSerializer
from .models import KaraokeSong

def home(request):
    songs = KaraokeSong.objects.all()
    return render(request, 'home.html', {'songs':songs})


class CreateKaraokeSong(generics.CreateAPIView):
    model = KaraokeSong
    serializer_class = KaraokeSongSerializer

class UpdateKaraokeSong(APIView):
    serializer_class = KaraokeSongSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
            self.request.session['is_authenticated'] = False

        if not self.request.session.get('is_authenticated', False):
            return Response({'Forbidden':'You have to login'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            code = serializer.validated_data.get('song_code')

            queryset = KaraokeSong.objects.filter(song_code=code)

            if not queryset.exists():
                return Response({'Not Found':'There is no song with this code'}, status=status.HTTP_404_NOT_FOUND)
            
            song = queryset.first()
            song.title = serializer.validated_data.get('title', song.title)
            song.artist = serializer.validated_data.get('artist', song.artist)
            song.lyrics = serializer.validated_data.get('lyrics', song.lyrics)
            song.image = serializer.validated_data.get('image', song.image)

            if not serializer.validated_data.get('mp3_file') == None:
                song.mp3_file = serializer.validated_data.get('mp3_file', song.mp3_file)


            song.save()

            return Response({'Message':'Success'}, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Non proper request'})

