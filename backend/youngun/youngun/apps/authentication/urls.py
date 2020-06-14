from django.urls import path

from .views import UserInfoApiView

app_name = 'userinfo'

urlpatterns = [
    path("user/", UserInfoApiView.as_view()),
]
