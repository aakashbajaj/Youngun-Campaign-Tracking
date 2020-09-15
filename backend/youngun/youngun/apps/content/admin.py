from django.contrib import admin

from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.html import format_html

from .models import Media, InstagramPost, FacebookPost, TwitterPost, Post, Story, InstagramStory, FacebookStory, TwitterStory
from youngun.apps.campaigns.models import Campaign

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


class MediaInline(admin.TabularInline):
    model = Media
    extra = 0

    verbose_name = "Post Media"
    verbose_name_plural = "Post Medias"


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'campaign', 'platform', 'date')

    list_filter = [
        ('campaign__name', custom_titled_filter("Campaign")),
    ]

    save_on_top = True


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('url', 'campaign', 'platform', 'date', 'alive', 'likes', 'comments',
                    'post_shares', 'post_saves', 'post_reach')

    inlines = [
        MediaInline
    ]

    list_filter = [
        'platform',
        ('campaign__name', custom_titled_filter("Campaign")),
    ]

    save_on_top = True


@admin.register(InstagramPost)
class InstagramPostAdmin(admin.ModelAdmin):
    exclude = ('platform', 'post_type')
    list_display = ('url', 'campaign', 'link_to_camp', 'date', 'post_username', 'alive', 'visibility', 'likes', 'comments',
                    'post_shares', 'post_saves', 'post_reach')

    readonly_fields = ('date', 'link_to_camp')
    fields = ('url', 'campaign', 'link_to_camp', 'date', 'post_username', 'visibility', 'alt_google_photo_url',
              'likes', 'comments', 'post_shares', 'post_saves', 'post_reach', 'embed_code')
    # list_display_links = ('campaign', )

    # add_fields = ('url', 'campaign', 'date', 'likes', 'comments',
    #               'post_shares', 'post_saves', 'post_reach', 'embed_code', 'visibility', 'alt_google_photo_url')

    list_filter = [
        ('campaign__name', custom_titled_filter("Campaign")),
        'visibility',
        'post_username'
    ]
    search_fields = ('post_username', 'url')

    save_on_top = True

    inlines = [
        MediaInline
    ]

    def link_to_camp(self, obj):
        link = reverse("admin:campaigns_campaign_change",
                       args=[obj.campaign.id])

        link_live = reverse("admin:campaigns_livecampaign_change",
                            args=[obj.campaign.id])

        link_report = reverse("admin:campaigns_campaignreport_change",
                              args=[obj.campaign.id])
        return format_html('<a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/>', link, "Campaign Admin", link_live, "Live Details", link_report, "Report Data")

    link_to_camp.short_description = "Campaign URLs"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        print(request)
        if db_field.name == "campaign":
            kwargs["queryset"] = Campaign.objects.filter(
                staff_profiles=request.user.usermanager_staffprofile)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(FacebookPost)
class FacebookPostAdmin(admin.ModelAdmin):
    exclude = ('platform', 'embed_code')
    list_display = ('url', 'campaign', 'post_type', 'link_to_camp', 'date', 'likes', 'comments',
                    'post_shares', 'post_saves', 'post_reach')

    readonly_fields = ('date', 'link_to_camp')
    fields = ('url', 'campaign', 'link_to_camp', 'date', 'post_type', 'likes', 'comments',
              'post_shares', 'post_saves', 'post_reach',  'visibility', 'alt_google_photo_url')
    # list_display_links = ('campaign', )

    # add_fields = ('url', 'campaign', 'date', 'likes', 'comments',
    #               'post_shares', 'post_saves', 'post_reach', 'embed_code', 'visibility', 'alt_google_photo_url')

    list_filter = [
        ('campaign__name', custom_titled_filter("Campaign")),
    ]

    save_on_top = True

    def link_to_camp(self, obj):
        link = reverse("admin:campaigns_campaign_change",
                       args=[obj.campaign.id])

        link_live = reverse("admin:campaigns_livecampaign_change",
                            args=[obj.campaign.id])

        link_report = reverse("admin:campaigns_campaignreport_change",
                              args=[obj.campaign.id])
        return format_html('<a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/>', link, "Campaign Admin", link_live, "Live Details", link_report, "Report Data")

    link_to_camp.short_description = "Campaign URLs"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "campaign":
            kwargs["queryset"] = Campaign.objects.filter(
                staff_profiles=request.user.usermanager_staffprofile)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(TwitterPost)
class TwitterPostAdmin(admin.ModelAdmin):
    exclude = ('platform', 'post_type')
    list_display = ('url', 'campaign', 'link_to_camp', 'date', 'visibility', 'alive', 'likes', 'comments',
                    'post_shares', 'post_saves', 'post_reach')

    readonly_fields = ('date', 'link_to_camp')
    fields = ('url', 'campaign', 'link_to_camp', 'date', 'likes', 'comments',
              'post_shares', 'post_saves', 'post_reach', 'embed_code', 'visibility', 'alt_google_photo_url')
    # list_display_links = ('campaign', )

    # add_fields = ('url', 'campaign', 'date', 'likes', 'comments',
    #               'post_shares', 'post_saves', 'post_reach', 'embed_code', 'visibility', 'alt_google_photo_url')

    list_filter = [
        ('campaign__name', custom_titled_filter("Campaign")),
    ]

    save_on_top = True

    inlines = [
        MediaInline
    ]

    def link_to_camp(self, obj):
        link = reverse("admin:campaigns_campaign_change",
                       args=[obj.campaign.id])

        link_live = reverse("admin:campaigns_livecampaign_change",
                            args=[obj.campaign.id])

        link_report = reverse("admin:campaigns_campaignreport_change",
                              args=[obj.campaign.id])
        return format_html('<a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/>', link, "Campaign Admin", link_live, "Live Details", link_report, "Report Data")

    link_to_camp.short_description = "Campaign URLs"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "campaign":
            kwargs["queryset"] = Campaign.objects.filter(
                staff_profiles=request.user.usermanager_staffprofile)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(InstagramStory)
class InstagramStoryAdmin(admin.ModelAdmin):
    exclude = ('platform', )
    list_display = ('url', 'campaign', 'date')

    list_filter = [
        ('campaign__name', custom_titled_filter("Campaign")),
    ]

    save_on_top = True

    def link_to_camp(self, obj):
        link = reverse("admin:campaigns_campaign_change",
                       args=[obj.campaign.id])

        link_live = reverse("admin:campaigns_livecampaign_change",
                            args=[obj.campaign.id])

        link_report = reverse("admin:campaigns_campaignreport_change",
                              args=[obj.campaign.id])
        return format_html('<a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/>', link, "Campaign Admin", link_live, "Live Details", link_report, "Report Data")

    link_to_camp.short_description = "Campaign URLs"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "campaign":
            kwargs["queryset"] = Campaign.objects.filter(
                staff_profiles=request.user.usermanager_staffprofile)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(FacebookStory)
class FacebookStoryAdmin(admin.ModelAdmin):
    exclude = ('platform', )
    list_display = ('url', 'campaign', 'date')

    list_filter = [
        ('campaign__name', custom_titled_filter("Campaign")),
    ]

    save_on_top = True

    def link_to_camp(self, obj):
        link = reverse("admin:campaigns_campaign_change",
                       args=[obj.campaign.id])

        link_live = reverse("admin:campaigns_livecampaign_change",
                            args=[obj.campaign.id])

        link_report = reverse("admin:campaigns_campaignreport_change",
                              args=[obj.campaign.id])
        return format_html('<a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/>', link, "Campaign Admin", link_live, "Live Details", link_report, "Report Data")

    link_to_camp.short_description = "Campaign URLs"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "campaign":
            kwargs["queryset"] = Campaign.objects.filter(
                staff_profiles=request.user.usermanager_staffprofile)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(TwitterStory)
class TwitterStoryAdmin(admin.ModelAdmin):
    exclude = ('platform', )
    list_display = ('url', 'campaign', 'date')

    list_filter = [
        ('campaign__name', custom_titled_filter("Campaign")),
    ]

    save_on_top = True

    def link_to_camp(self, obj):
        link = reverse("admin:campaigns_campaign_change",
                       args=[obj.campaign.id])

        link_live = reverse("admin:campaigns_livecampaign_change",
                            args=[obj.campaign.id])

        link_report = reverse("admin:campaigns_campaignreport_change",
                              args=[obj.campaign.id])
        return format_html('<a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/>', link, "Campaign Admin", link_live, "Live Details", link_report, "Report Data")

    link_to_camp.short_description = "Campaign URLs"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "campaign":
            kwargs["queryset"] = Campaign.objects.filter(
                staff_profiles=request.user.usermanager_staffprofile)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
