from django.urls import path
from .views import (CreateCourseView,
                    CreateVideoView,
                    UpdateCourseView)


urlpatterns = [
    path('create-course/', CreateCourseView.as_view()),
    path('create-video/', CreateVideoView.as_view()),
    path('update-course/', UpdateCourseView.as_view()),
]

