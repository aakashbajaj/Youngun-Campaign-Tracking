from django.urls import path

from .views import ProfileInfoRetriveAPIView, InviteSubUsersAPIView, MyInvitedUsersRetriveAPIView, RemoveInvitedUserAPIView

app_name = 'profile'

urlpatterns = [
    path("profile/", ProfileInfoRetriveAPIView.as_view()),
    path("profile/inviteuser/", InviteSubUsersAPIView.as_view()),
    path("profile/removeinvite/", RemoveInvitedUserAPIView.as_view()),
    path("profile/myinvites/", MyInvitedUsersRetriveAPIView.as_view()),

]
