from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserInfoSerializer, OrganisationSerializer
from .renderers import UserInfoJSONRenderer
from .models import User, Organisation

# Create your views here.


class UserInfoRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserInfoSerializer
    renderer_classes = (UserInfoJSONRenderer, )

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)
