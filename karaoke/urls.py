from django.urls import path
from .views import (home,
                    CreateKaraokeSong,
                    UpdateKaraokeSong,
                    GetAllKaraokeSongs,
                    SongDetails)
from MelodyMentor import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home),
    path('create/', CreateKaraokeSong.as_view()),
    path('update/', UpdateKaraokeSong.as_view()),
    path('all/', GetAllKaraokeSongs.as_view()),
    path('song/<str:code>/', SongDetails.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



