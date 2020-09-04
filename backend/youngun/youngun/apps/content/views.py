from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


# from .serializers import CreatePostSerializer
from .models import Post, Campaign

# Create your views here.


class CreatePostAPIView(CreateAPIView):
    permission_classes = (IsAdminUser, )
    # serializer_class = CreatePostSerializer

    def post(self, request, slug, *args, **kwargs):
        try:
            campaign = Campaign.objects.get(slug=slug)
        except Campaign.DoesNotExist:
            return Response({"response": "No Campaign match"}, status.HTTP_400_BAD_REQUEST)

        post_url = request.data["url"]

        if "facebook.com" in post_url:
            if "/video" in post_url:
                Post.objects.create(url=post_url, campaign=campaign,
                                    platform="fb", embed_code="", post_type="v")
            else:
                Post.objects.create(url=post_url, campaign=campaign,
                                    platform="fb", embed_code="", post_type="p")

        elif "instagram.com" in post_url:
            Post.objects.create(url=post_url, campaign=campaign,
                                platform="in", embed_code="")

        elif "twitter.com" in post_url:
            Post.objects.create(url=post_url, campaign=campaign,
                                platform="tw", embed_code="")

        else:
            return Response({"response": "No Platform match"}, status.HTTP_400_BAD_REQUEST)

        return Response({"response": "Created"}, status.HTTP_200_OK)

class CreatePostAPIView2(CreateAPIView):
    permission_classes = (IsAdminUser, )
    # serializer_class = CreatePostSerializer

    def post(self, request, *args, **kwargs):
        slug = request.data["camp_slug"]
        try:
            campaign = Campaign.objects.get(slug=slug)
        except Campaign.DoesNotExist:
            return Response({"response": "No Campaign match"}, status.HTTP_400_BAD_REQUEST)

        post_url = request.data["url"]

        if "facebook.com" in post_url:
            if "/video" in post_url:
                Post.objects.create(url=post_url, campaign=campaign,
                                    platform="fb", embed_code="", post_type="v")
            else:
                Post.objects.create(url=post_url, campaign=campaign,
                                    platform="fb", embed_code="", post_type="p")

        elif "instagram.com" in post_url:
            Post.objects.create(url=post_url, campaign=campaign,
                                platform="in", embed_code="")

        elif "twitter.com" in post_url:
            Post.objects.create(url=post_url, campaign=campaign,
                                platform="tw", embed_code="")

        else:
            return Response({"response": "No Platform match"}, status.HTTP_400_BAD_REQUEST)

        return Response({"response": "Created"}, status.HTTP_200_OK)

# post_type = "post"
