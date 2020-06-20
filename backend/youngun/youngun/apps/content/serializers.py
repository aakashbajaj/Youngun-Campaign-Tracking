from rest_framework.serializers import ModelSerializer

from .models import InstagramPost, FacebookPost, TwitterPost, Post


class InstagramPostDisplaySerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'embed_code']


class FacebookPostDisplaySerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'post_type']


class TwitterPostDisplaySerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'embed_code']


class InstagramPostReportSerializer(ModelSerializer):
    class Meta:
        model = InstagramPost
        fields = [
            'date',
            'url',
            'likes',
            'comments',
            'post_shares',
            'post_saves',
            'post_reach',
        ]


class FacebookPostReportSerializer(ModelSerializer):
    class Meta:
        model = FacebookPost
        fields = [
            'date',
            'url',
            'likes',
            'comments',
            'post_shares',
            'post_saves',
            'post_reach',
        ]


class TwitterPostReportSerializer(ModelSerializer):
    class Meta:
        model = TwitterPost
        fields = [
            'date',
            'url',
            'likes',
            'comments',
            'post_shares',
            'post_saves',
            'post_reach',
        ]
