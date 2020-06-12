from django.contrib import admin

from .models import Campaign
# Register your models here.


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'organisation',
        'hashtag',
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

    list_filter = ['organisation']
