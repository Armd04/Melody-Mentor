from django.urls import path
from .views import (PostsView,
                    CreatePostView,
                    UpdatePostView,
                    DeletePostView,
                    GetAllPosts,
                    PostDetails)

urlpatterns = [
    path('', PostsView.as_view()),
    path('create/', CreatePostView.as_view()),
    path('update/', UpdatePostView.as_view()),
    path('delete/', DeletePostView.as_view()),
    path('all/', GetAllPosts.as_view()),
    path('detail/<str:code>/', PostDetails.as_view()),
]


