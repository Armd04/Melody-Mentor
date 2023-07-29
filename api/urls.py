from django.urls import path
from .views import (CreateCourseView,
                    CreateVideoView)


urlpatterns = [
    path('create-course/', CreateCourseView.as_view()),
    path('create-video/', CreateVideoView.as_view()),
]

