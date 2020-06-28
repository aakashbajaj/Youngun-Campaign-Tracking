from django.contrib import admin
from .models import InstagramPost, FacebookPost, TwitterPost, Post, Story
from django.utils.translation import gettext_lazy as _


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
    list_display = ('url', 'campaign', 'date', 'likes', 'comments',
                    'post_shares', 'post_saves', 'post_reach')

    list_filter = [
        ('campaign__name', custom_titled_filter("Campaign")),
    ]


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
