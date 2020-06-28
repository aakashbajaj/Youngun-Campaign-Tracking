from django.urls import path

from .views import ProfileInfoRetriveAPIView, InviteSubUsersAPIView

app_name = 'profile'

urlpatterns = [
    path("profile/", ProfileInfoRetriveAPIView.as_view()),
    path("profile/inviteuser/", InviteSubUsersAPIView.as_view()),
]
