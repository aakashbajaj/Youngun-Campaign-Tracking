from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ProfileSerializer, InvitedUserSerializer
from .renderers import ProfileJSONRenderer, InvitedProfileJSONRenderer

from youngun.apps.campaigns.models import Campaign
from youngun.apps.authentication.models import User
from .models import ClientProfile

# Create your views here.


class ProfileInfoRetriveAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProfileSerializer
    renderer_classes = (ProfileJSONRenderer, )

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user.profile)

        return Response(serializer.data, status=status.HTTP_200_OK)


class MyInvitedUsersRetriveAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = InvitedUserSerializer
    renderer_classes = (InvitedProfileJSONRenderer, )

    def retrieve(self, request, *args, **kwargs):
        if not request.user.profile.is_main_user:
            return Response({"response": "Not Allowed. Not Main User"}, status.HTTP_401_UNAUTHORIZED)

        invited_profiles = {}
        for camp in request.user.profile.campaigns.all():
            serializer = self.serializer_class(
                request.user.profile.invited_users.filter(campaigns=camp), many=True)

            invited_profiles[camp.slug] = serializer.data

        return Response(invited_profiles, status=status.HTTP_200_OK)


class InviteSubUsersAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = InvitedUserSerializer

    def post(self, request, *args, **kwargs):
        if not request.user.profile.is_main_user:
            return Response({"response": "Not Allowed. Not Main User"}, status.HTTP_401_UNAUTHORIZED)

        email = request.data["email"]

        campaign_slug = request.data["campaign_slug"]
        try:
            camp_obj = Campaign.objects.get(slug=campaign_slug)
        except Campaign.DoesNotExist:
            return Response({"response": "Not Allowed. Invalid Campaign"}, status.HTTP_401_UNAUTHORIZED)

        adder_prof_obj = request.user.profile

        if not camp_obj in adder_prof_obj.campaigns.all():
            return Response({"response": "Not Allowed. Invalid Campaign"}, status.HTTP_401_UNAUTHORIZED)

        invited_user, _ = User.objects.get_or_create(email=email)
        invited_profile, _ = ClientProfile.objects.get_or_create(
            user=invited_user)
        if not hasattr(request.user, "usermanager_staffprofile"):
            invited_profile.added_by = adder_prof_obj

        invited_profile.campaigns.add(camp_obj)

        invited_profile.save()

        invited_profiles = {}
        for camp in request.user.profile.campaigns.all():
            serializer = self.serializer_class(
                request.user.profile.invited_users.filter(campaigns=camp), many=True)

            invited_profiles[camp.slug] = serializer.data

        return Response({"response": "Created", "invited_profiles": invited_profiles}, status.HTTP_201_CREATED)


class RemoveInvitedUserAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = InvitedUserSerializer

    def post(self, request, *args, **kwargs):
        if not request.user.profile.is_main_user:
            return Response({"response": "Not Allowed. Not Main User"}, status.HTTP_401_UNAUTHORIZED)

        email = request.data["email"]

        campaign_slug = request.data["campaign_slug"]
        try:
            camp_obj = Campaign.objects.get(slug=campaign_slug)
        except Campaign.DoesNotExist:
            return Response({"response": "Not Allowed. Invalid Campaign"}, status.HTTP_401_UNAUTHORIZED)

        adder_prof_obj = request.user.profile

        if not camp_obj in adder_prof_obj.campaigns.all():
            return Response({"response": "Not Allowed. Invalid Campaign"}, status.HTTP_401_UNAUTHORIZED)

        try:
            invited_user = User.objects.get(email=email)
            if invited_user not in request.user.profile.invited_users.all():
                return Response({"response": "Not Allowed. Invalid User"}, status.HTTP_401_UNAUTHORIZED)

            invited_user.delete()

        except User.DoesNotExist:
            return Response({"response": "No User Found With Matching Email"}, status.HTTP_400_BAD_REQUEST)

        invited_profiles = {}
        for camp in request.user.profile.campaigns.all():
            serializer = self.serializer_class(
                request.user.profile.invited_users.filter(campaigns=camp), many=True)

            invited_profiles[camp.slug] = serializer.data

        return Response({"response": "Created", "invited_profiles": invited_profiles}, status.HTTP_201_CREATED)
