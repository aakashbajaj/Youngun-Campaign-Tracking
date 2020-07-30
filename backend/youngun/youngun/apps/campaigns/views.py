from datetime import datetime

from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import CampaignDataSerializer, LiveCampaignMetricsSerializer, LiveCampaignFeedSerilaizer
from .renderers import LiveCampaignMetricJSONRenderer, CampaignDataJSONRenderer
from .models import Campaign
# Create your views here.


class CreateCampaignAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    # serializer_class = CreateCampaignSerializer

    def post(self, request, *args, **kwargs):
        try:
            camp_name = request.data["campaign_name"]
            company_name = request.data["company_name"]
            date_str = request.data["start_date"]

            start_date = datetime.strptime(date_str, "%Y-%m-%d").date()

            hashtag = camp_name.replace(" ", "")

            Campaign.objects.create(
                name=camp_name, company_name=company_name, hashtag=hashtag, start_date=start_date)

            return Response({"response": "Campaign Created"}, status=status.HTTP_201_CREATED)

        except Exception:
            return Response({"response": "Internal Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CampignListRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CampaignDataSerializer
    renderer_classes = (CampaignDataJSONRenderer, )

    def retrieve(self, request, *args, **kwargs):
        if hasattr(request.user.profile, "campaigns"):
            user_campaigns = request.user.profile.campaigns.all()
            serializer = self.serializer_class(user_campaigns, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"response": "No Campaigns found"}, status=status.HTTP_200_OK)


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
