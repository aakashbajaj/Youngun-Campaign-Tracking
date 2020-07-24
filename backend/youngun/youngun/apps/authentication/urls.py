from django.urls import path

from .views import UserInfoRetrieveAPIView, InitiateLogin, VerifyLogin

app_name = 'users'

urlpatterns = [
    path("users/authenticate/", UserInfoRetrieveAPIView.as_view()),
    path("users/login/", InitiateLogin.as_view()),
    path("users/verify/", VerifyLogin.as_view()),
]
