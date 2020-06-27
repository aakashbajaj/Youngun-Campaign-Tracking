from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ProfileSerializer
from .renderers import ProfileJSONRenderer

# Create your views here.


class ProfileInfoRetriveAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProfileSerializer
    renderer_classes = (ProfileJSONRenderer, )

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user.profile)

        return Response(serializer.data, status=status.HTTP_200_OK)
