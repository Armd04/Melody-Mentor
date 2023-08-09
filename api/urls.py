from django.urls import path
from MelodyMentor import settings
from django.conf.urls.static import static
from .views import (CreateCourseView,
                    CreateVideoView,
                    UpdateCourseView,
                    UpdateVideoDetailsView,
                    UpdateVideoFileView,
                    VideosOfACourse,
                    VideoDetails,
                    CourseDetails)


urlpatterns = [
    path('create-course/', CreateCourseView.as_view()),
    path('create-video/', CreateVideoView.as_view()),
    path('update-course/', UpdateCourseView.as_view()),
    path('update-video/', UpdateVideoDetailsView.as_view()),
    path('update-video-file/', UpdateVideoFileView.as_view()),
    path('course-videos/<int:num>/', VideosOfACourse.as_view()),
    path('video/<str:code>/', VideoDetails.as_view()),
    path('course/<int:num>/', CourseDetails.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

