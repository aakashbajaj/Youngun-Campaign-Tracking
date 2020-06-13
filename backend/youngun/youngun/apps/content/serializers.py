from rest_framework.serializers import ModelSerializer

from .models import InstagramPost, FacebookPost, TwitterPost


class InstagramPostDisplaySerializer(ModelSerializer):
    class Meta:
        model = InstagramPost
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


class FacebookPostDisplaySerializer(ModelSerializer):
    class Meta:
        model = FacebookPost
        fields = ['url', 'post_type']


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


class TwitterPostDisplaySerializer(ModelSerializer):
    class Meta:
        model = TwitterPost
        fields = ['url']


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
