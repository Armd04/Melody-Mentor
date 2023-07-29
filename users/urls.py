from django.urls import path
from .views import (LoginView,
                    RegisterView,
                    ProfilesView,
                    LoggedInView,
                    LogoutView)

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('profiles/', ProfilesView.as_view()),
    path('logged-in/', LoggedInView.as_view()),
    path('logout/', LogoutView.as_view()),
]
