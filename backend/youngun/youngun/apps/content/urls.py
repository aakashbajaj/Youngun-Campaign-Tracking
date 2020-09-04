from django.urls import path

from .views import CreatePostAPIView, CreatePostAPIView2

app_name = "content"

urlpatterns = [
    path("content/<str:slug>/addpost", CreatePostAPIView.as_view()),
    path("content/addpost", CreatePostAPIView2.as_view())
]
