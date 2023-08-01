from django.urls import path
from MelodyMentor import settings
from django.conf.urls.static import static
from .views import (CreateCourseView,
                    CreateVideoView,
                    UpdateCourseView,
                    UpdateVideoDetailsView,
                    UpdateVideoFileView)


urlpatterns = [
    path('create-course/', CreateCourseView.as_view()),
    path('create-video/', CreateVideoView.as_view()),
    path('update-course/', UpdateCourseView.as_view()),
    path('update-video/', UpdateVideoDetailsView.as_view()),
    path('update-video-file/', UpdateVideoFileView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

