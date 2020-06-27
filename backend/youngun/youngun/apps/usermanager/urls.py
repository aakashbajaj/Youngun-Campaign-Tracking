from django.urls import path

from .views import ProfileInfoRetriveAPIView

app_name = 'profile'

urlpatterns = [
    path("profile/", ProfileInfoRetriveAPIView.as_view()),
]
