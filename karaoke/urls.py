from django.urls import path
from .views import (home,
                    CreateKaraokeSong,
                    UpdateKaraokeSong)
from MelodyMentor import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home),
    path('create/', CreateKaraokeSong.as_view()),
    path('edit/', UpdateKaraokeSong.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



