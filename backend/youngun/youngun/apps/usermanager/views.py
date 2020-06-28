from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ProfileSerializer
from .renderers import ProfileJSONRenderer

from youngun.apps.campaigns.models import Campaign
from youngun.apps.authentication.models import User

# Create your views here.


class ProfileInfoRetriveAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProfileSerializer
    renderer_classes = (ProfileJSONRenderer, )

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user.profile)

        return Response(serializer.data, status=status.HTTP_200_OK)


class InviteSubUsersAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated, )

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

        print(adder_prof_obj.campaigns.all())

        if not camp_obj in adder_prof_obj.campaigns.all():
            return Response({"response": "Not Allowed. Invalid Campaign", "payload": adder_prof_obj.campaigns.all()}, status.HTTP_401_UNAUTHORIZED)

        invited_user, _ = User.objects.get_or_create(email=email)
        invited_user.profile.added_by = adder_prof_obj
        invited_user.profile.campaigns.add(camp_obj)

        invited_user.profile.save()

        return Response({"response": "Created"}, status.HTTP_201_CREATED)
