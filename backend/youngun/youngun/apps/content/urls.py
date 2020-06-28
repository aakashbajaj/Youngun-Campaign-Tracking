from django.urls import path

from .views import CreatePostAPIView

app_name = "content"

urlpatterns = [
    path("content/<str:slug>/addpost", CreatePostAPIView.as_view())
]
