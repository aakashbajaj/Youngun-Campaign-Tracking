from rest_framework.serializers import ModelSerializer

from youngun.apps.content.serializers import *
from .models import LiveCampaign, Campaign


class LiveCampaignDataSerializer(ModelSerializer):
    class Meta:
        model = LiveCampaign
        fields = [
            'name', 'organisation', 'hashtag', 'status',
            'start_date', 'end_date',
            'slide_url', 'live_google_sheet', 'slug',
            'particaipating_profiles', 'unique_content_pieces', 'approved_content_pieces', 'remaining_content_pieces',
            'last_updated',
            'fb_posts', 'fb_stories',
            'in_posts', 'in_stories',
            'tw_posts', 'tw_stories',
            'live_fb_posts', 'live_fb_stories',
            'live_in_posts', 'live_in_stories',
            'live_tw_posts', 'live_tw_stories',
        ]


class LiveCampaignFeedSerilaizer(ModelSerializer):
    instagram = InstagramPostDisplaySerializer(many=True, read_only=True)
    facebook = FacebookPostDisplaySerializer(many=True, read_only=True)
    twitter = TwitterPostDisplaySerializer(many=True, read_only=True)
