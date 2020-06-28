from django.urls import path

from .views import CampignListRetrieveAPIView, LiveCampaignFeedAPIView, LiveCampaignMetricsAPIView, CampignDataRetrieveAPIView

app_name = 'campaigns'

urlpatterns = [
    path("campaigns/", CampignListRetrieveAPIView.as_view()),
    path("campaigns/<str:slug>", CampignDataRetrieveAPIView.as_view()),
    path("campaigns/<str:slug>/feed", LiveCampaignFeedAPIView.as_view()),
    path("campaigns/<str:slug>/metrics", LiveCampaignMetricsAPIView.as_view()),
]
