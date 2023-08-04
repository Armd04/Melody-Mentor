from django.urls import path
from MelodyMentor import settings
from django.conf.urls.static import static
from .views import (LoginView,
                    RegisterView,
                    ProfilesView,
                    LoggedInView,
                    LogoutView,
                    LoggedInInfoView)

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('profiles/', ProfilesView.as_view()),
    path('logged-in/', LoggedInView.as_view()),
    path('logged-in-info/', LoggedInInfoView.as_view()),
    path('logout/', LogoutView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
