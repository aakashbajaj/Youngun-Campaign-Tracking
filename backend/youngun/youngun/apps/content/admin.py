from django.contrib import admin

from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.html import format_html

from .models import InstagramPost, FacebookPost, TwitterPost, Post, Story, InstagramStory, FacebookStory, TwitterStory
# class CampaignFilter(admin.SimpleListFilter):
#     title = _("Campiagn")
#     parameter_name = "campaign__name"


def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'campaign', 'platform', 'date')

    list_filter = [
        ('campaign__name', custom_titled_filter("Campaign")),
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('url', 'campaign', 'platform', 'date', 'likes', 'comments',
                    'post_shares', 'post_saves', 'post_reach')

    list_filter = [
        'platform',
        ('campaign__name', custom_titled_filter("Campaign")),
    ]


@admin.register(InstagramPost)
class InstagramPostAdmin(admin.ModelAdmin):
    exclude = ('platform', 'post_type')
    list_display = ('url', 'link_to_camp', 'date', 'likes', 'comments',
                    'post_shares', 'post_saves', 'post_reach')

    readonly_fields = ('date', 'link_to_camp')
    fields = ('url', 'link_to_camp', 'date', 'likes', 'comments',
              'post_shares', 'post_saves', 'post_reach', 'embed_code', 'visibility', 'alt_google_photo_url')
    # list_display_links = ('campaign', )

    list_filter = [
        ('campaign__name', custom_titled_filter("Campaign")),
    ]

    def link_to_camp(self, obj):
        link = reverse("admin:campaigns_campaign_change",
                       args=[obj.campaign.id])
        return format_html('<a href="{}">{}</a>', link, obj.campaign.name)

    link_to_camp.short_description = "Campaign"


@admin.register(FacebookPost)
class FacebookPostAdmin(admin.ModelAdmin):
    exclude = ('platform', 'embed_code')
    list_display = ('url', 'campaign', 'date', 'likes', 'comments',
                    'post_shares', 'post_saves', 'post_reach')

    list_filter = [
        ('campaign__name', custom_titled_filter("Campaign")),
    ]


@admin.register(TwitterPost)
class TwitterPostAdmin(admin.ModelAdmin):
    exclude = ('platform', 'post_type')
    list_display = ('url', 'campaign', 'date', 'likes', 'comments',
                    'post_shares', 'post_saves', 'post_reach')

    list_filter = [
        ('campaign__name', custom_titled_filter("Campaign")),
    ]


@admin.register(InstagramStory)
class InstagramStoryAdmin(admin.ModelAdmin):
    exclude = ('platform', )
    list_display = ('url', 'campaign', 'date')

    list_filter = [
        ('campaign__name', custom_titled_filter("Campaign")),
    ]


@admin.register(FacebookStory)
class FacebookStoryAdmin(admin.ModelAdmin):
    exclude = ('platform', )
    list_display = ('url', 'campaign', 'date')

    list_filter = [
        ('campaign__name', custom_titled_filter("Campaign")),
    ]


@admin.register(TwitterStory)
class TwitterStoryAdmin(admin.ModelAdmin):
    exclude = ('platform', )
    list_display = ('url', 'campaign', 'date')

    list_filter = [
        ('campaign__name', custom_titled_filter("Campaign")),
    ]
