from django.urls import path

from .views import UserInfoRetrieveAPIView

app_name = 'users'

urlpatterns = [
    path("users/", UserInfoRetrieveAPIView.as_view()),
]
