from django.urls import path
from .views import (PostsView,
                    CreatePostView,
                    UpdatePostView,
                    DeletePostView)

urlpatterns = [
    path('', PostsView.as_view()),
    path('create/', CreatePostView.as_view()),
    path('update/', UpdatePostView.as_view()),
    path('delete/', DeletePostView.as_view()),
]


