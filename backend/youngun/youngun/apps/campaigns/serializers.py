from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from youngun.apps.usermanager.serializers import BrandSerializer
from youngun.apps.content.serializers import InstagramPostDisplaySerializer, FacebookPostDisplaySerializer, TwitterPostDisplaySerializer, StoriesDisplaySerializer, InstagramPostReportSerializer, FacebookPostReportSerializer, TwitterPostReportSerializer, PostReportSerializer
from .models import LiveCampaign, Campaign


class CampaignDataSerializer(ModelSerializer):

    class Meta:
        model = LiveCampaign
        fields = [
            'name', 'company_name', 'hashtag', 'status',
            'start_date', 'end_date',
            'slide_url', 'live_google_sheet', 'slug', 'campaign_module'
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
            'live_fb_posts_cnt', 'live_fb_stories_cnt',
            'live_in_posts_cnt', 'live_in_stories_cnt',
            'live_tw_posts_cnt', 'live_tw_stories_cnt',
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

    # in_posts = InstagramPostDisplaySerializer(
    #     source='get_instagram_posts', many=True, read_only=True)
    # fb_posts = FacebookPostDisplaySerializer(
    #     source='get_facebook_posts', many=True, read_only=True)
    # tw_posts = TwitterPostDisplaySerializer(
    #     source='get_twitter_posts', many=True, read_only=True)

    in_stories = InstagramPostDisplaySerializer(
        source='get_instagram_stories', many=True, read_only=True)
    fb_stories = FacebookPostDisplaySerializer(
        source='get_facebook_stories', many=True, read_only=True)
    tw_stories = TwitterPostDisplaySerializer(
        source='get_twitter_stories', many=True, read_only=True)

    stories = StoriesDisplaySerializer(many=True, read_only=True)

    class Meta:
        model = Campaign
        fields = [
            'name', 'company_name', 'hashtag', 'status', 'slug',
            'instagram',
            'facebook',
            'twitter',
            'in_stories',
            'fb_stories',
            'tw_stories',
            # 'in_posts',
            # 'fb_posts',
            # 'tw_posts',
            # 'twitter_collection_url',
            'stories',
        ]


class CampaignReportSerializer(ModelSerializer):
    posts = PostReportSerializer(many=True, read_only=True)

    # instagram = InstagramPostReportSerializer(
    #     source='get_instagram_posts', many=True, read_only=True)
    # facebook = FacebookPostReportSerializer(
    #     source='get_facebook_posts', many=True, read_only=True)
    # twitter = TwitterPostReportSerializer(
    #     source='get_twitter_posts', many=True, read_only=True)

    # in_posts = InstagramPostDisplaySerializer(
    #     source='get_instagram_posts', many=True, read_only=True)
    # fb_posts = FacebookPostDisplaySerializer(
    #     source='get_facebook_posts', many=True, read_only=True)
    # tw_posts = TwitterPostDisplaySerializer(
    #     source='get_twitter_posts', many=True, read_only=True)

    # in_stories = InstagramPostDisplaySerializer(
    #     source='get_instagram_stories', many=True, read_only=True)
    # fb_stories = FacebookPostDisplaySerializer(
    #     source='get_facebook_stories', many=True, read_only=True)
    # tw_stories = TwitterPostDisplaySerializer(
    #     source='get_twitter_stories', many=True, read_only=True)

    # stories = StoriesDisplaySerializer(many=True, read_only=True)

    class Meta:
        model = Campaign
        fields = [
            'name', 'company_name', 'hashtag', 'status', 'slug',
            # 'instagram',
            # 'facebook',
            # 'twitter',
            # 'in_stories',
            # 'fb_stories',
            # 'tw_stories',
            # 'in_posts',
            # 'fb_posts',
            # 'tw_posts',
            # 'twitter_collection_url',
            # 'stories',
            'posts',
            'num_posts',
            'num_stories',
            'post_stats',
            'post_shares',
            'post_saves',
            'post_reach',
            'story_views',
            'website_traffic',
            'cost_per_engagement',
            'cost_per_post_impression',
            'total_post_engagement',
            'total_campaign_reach',
        ]
