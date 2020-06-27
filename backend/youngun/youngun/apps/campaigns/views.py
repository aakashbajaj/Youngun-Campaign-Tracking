from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import CampaignDataSerializer, LiveCampaignMetricsSerializer, LiveCampaignFeedSerilaizer
from .renderers import LiveCampaignMetricJSONRenderer, CampaignDataJSONRenderer
from .models import Campaign
# Create your views here.


class CampignListRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CampaignDataSerializer
    renderer_classes = (CampaignDataJSONRenderer, )

    def retrieve(self, request, *args, **kwargs):
        user_campaigns = request.user.profile.campaigns.all()
        serializer = self.serializer_class(user_campaigns, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CampignDataRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CampaignDataSerializer
    renderer_classes = (CampaignDataJSONRenderer, )

    def retrieve(self, request, slug, *args, **kwargs):
        try:
            campaign = request.user.profile.campaigns.all().get(slug=slug)
        except Campaign.DoesNotExist:
            raise

        serializer = self.serializer_class(campaign)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LiveCampaignFeedAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = LiveCampaignFeedSerilaizer
    renderer_classes = (LiveCampaignMetricJSONRenderer, )

    def retrieve(self, request, slug, *args, **kwargs):
        try:
            campaign = request.user.profile.campaigns.all().get(slug=slug)
        except Campaign.DoesNotExist:
            raise

        serializer = self.serializer_class(campaign)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LiveCampaignMetricsAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = LiveCampaignMetricsSerializer
    renderer_classes = (LiveCampaignMetricJSONRenderer, )

    def retrieve(self, request, slug, *args, **kwargs):
        try:
            campaign = request.user.profile.campaigns.all().get(slug=slug)
        except Campaign.DoesNotExist:
            raise

        serializer = self.serializer_class(campaign)

        return Response(serializer.data, status=status.HTTP_200_OK)
