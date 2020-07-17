from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from youngun.apps.usermanager.serializers import BrandSerializer
from youngun.apps.content.serializers import InstagramPostDisplaySerializer, FacebookPostDisplaySerializer, TwitterPostDisplaySerializer, StoriesDisplaySerializer
from .models import LiveCampaign, Campaign


class CampaignDataSerializer(ModelSerializer):

    class Meta:
        model = LiveCampaign
        fields = [
            'name', 'company_name', 'hashtag', 'status',
            'start_date', 'end_date',
            'slide_url', 'live_google_sheet', 'slug',
        ]


class CreateCampaignSerializer(ModelSerializer):

    class Meta:
        model = Campaign
        fields = [
            'name', 'company_name', 'start_date'
        ]


class LiveCampaignMetricsSerializer(ModelSerializer):

    class Meta:
        model = LiveCampaign
        fields = [
            'name', 'company_name', 'hashtag', 'status',
            'start_date', 'end_date',
            'slide_url', 'live_google_sheet', 'slug',
            'particaipating_profiles',
            'unique_content_pieces', 'approved_content_pieces', 'remaining_content_pieces',
            'last_updated',
            'fb_posts', 'fb_stories',
            'in_posts', 'in_stories',
            'tw_posts', 'tw_stories',
            'live_fb_posts', 'live_fb_stories',
            'live_in_posts', 'live_in_stories',
            'live_tw_posts', 'live_tw_stories',
        ]


class LiveCampaignFeedSerilaizer(ModelSerializer):
    # posts = InstagramPostDisplaySerializer(many=True, read_only=True)

    instagram = InstagramPostDisplaySerializer(
        source='get_instagram_posts', many=True, read_only=True)
    facebook = FacebookPostDisplaySerializer(
        source='get_facebook_posts', many=True, read_only=True)
    twitter = TwitterPostDisplaySerializer(
        source='get_twitter_posts', many=True, read_only=True)
    stories = StoriesDisplaySerializer(many=True, read_only=True)

    class Meta:
        model = Campaign
        fields = [
            'name', 'company_name', 'hashtag', 'status', 'slug',
            'instagram',
            'facebook',
            'twitter',
            'stories',
        ]
