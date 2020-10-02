from rest_framework.serializers import ModelSerializer

from .models import InstagramPost, FacebookPost, TwitterPost, Post, Story, Media


class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = [
            'key',
            'url',
            'media_type',
            'media_views'
        ]


class InstagramPostDisplaySerializer(ModelSerializer):
    media_objs = MediaSerializer(source='medias', many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'url', 'date', 'embed_code', 'alt_google_photo_url', 'media_objs']


class FacebookPostDisplaySerializer(ModelSerializer):
    media_objs = MediaSerializer(source='medias', many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'url', 'date', 'post_type', 'alt_google_photo_url', 'media_objs']


class TwitterPostDisplaySerializer(ModelSerializer):
    media_objs = MediaSerializer(source='medias', many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'url', 'date', 'embed_code', 'alt_google_photo_url', 'media_objs']


class StoriesDisplaySerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = ['url']


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
