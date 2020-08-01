from rest_framework.serializers import ModelSerializer

from .models import InstagramPost, FacebookPost, TwitterPost, Post, Story


class StoriesDisplaySerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = ['url']


class InstagramPostDisplaySerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'url', 'date', 'embed_code', 'alt_google_photo_url']


class FacebookPostDisplaySerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'url', 'date', 'post_type', 'alt_google_photo_url']


class TwitterPostDisplaySerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'url', 'date', 'embed_code', 'alt_google_photo_url']


class InstagramStoryDisplaySerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'url']


class FacebookStoryDisplaySerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'url']


class TwitterStoryDisplaySerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'url']


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
