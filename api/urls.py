from django.urls import path
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

