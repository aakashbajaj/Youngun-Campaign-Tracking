from django.contrib import admin

from .models import Campaign, LiveCampaign, CampaignReport
# Register your models here.


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'organisation',
        'hashtag',
        'status',
        'start_date',
        'end_date',
    )

    list_filter = ['organisation', 'status']


@admin.register(LiveCampaign)
class LiveCampaignAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'organisation',
        'status',
        'particaipating_profiles',
        'unique_content_pieces',
        'approved_content_pieces',
        'last_updated',
        'fb_posts',
        'fb_stories',
        'in_posts',
        'in_stories',
        'tw_posts',
        'tw_stories',
        'live_fb_posts',
        'live_fb_stories',
        'live_in_posts',
        'live_in_stories',
        'live_tw_posts',
        'live_tw_stories',
    )

    list_filter = ['organisation', 'status']


@admin.register(CampaignReport)
class CampaignReportAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'organisation',
        'status',
        'num_content_pieces',
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
    )

    list_filter = ['organisation', 'status']
