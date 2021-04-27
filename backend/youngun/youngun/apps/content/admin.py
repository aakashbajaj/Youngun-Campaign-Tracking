from django.contrib import admin

from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.html import format_html

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from youngun.apps.content.forms import QuoteRTForm

from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

from youngun.apps.content.models import Media, InstagramPost, FacebookPost, TwitterPost, Post, Story, InstagramStory, FacebookStory, TwitterStory
from youngun.apps.campaigns.models import Campaign

from youngun.apps.content.mixins.exportcsv import ExportCsvMixin
from youngun.apps.content.mixins.campaignlistfilter import CampaignNameFilter

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
        CampaignNameFilter
    ]

    save_on_top = True

    def get_queryset(self, request):
        qs = super(StoryAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name="MasterAdmin").exists():
            return qs
        
        return qs.filter(campaign__staff_profiles=request.user.profile)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('url', 'campaign', 'platform', 'date', 'alive', 'likes', 'comments',
                    'post_shares', 'post_saves', 'post_reach')

    inlines = [
        MediaInline
    ]

    list_filter = [
        'platform',
        CampaignNameFilter,
        ('upload_date', DateTimeRangeFilter)
    ]

    inlines = [
        MediaInline
    ]

    actions = ['export_as_csv']

    save_on_top = True

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name="MasterAdmin").exists():
            return qs
        
        return qs.filter(campaign__staff_profiles=request.user.profile)


@admin.register(InstagramPost)
class InstagramPostAdmin(admin.ModelAdmin, ExportCsvMixin):
    exclude = ('platform', )
    list_display = (
        'url',
        'campaign',
        # 'link_to_camp',
        'upload_date',
        'post_username',
        # 'pre_fetched',
        'link_to_post',
        'alive',
        'visibility',
        'post_type',
        'likes',
        'comments',
        'post_shares',
        'total_views',
        'post_engagement',
        'post_reach'
    )

    readonly_fields = ('date', 'link_to_camp')
    fields = (
        'alive',
        'url',
        'campaign',
        'link_to_camp',
        'upload_date',
        'post_username',
        'account_name',
        'alt_google_photo_url',
        'pre_fetched',
        'caption',
        'post_type',
        'likes',
        'comments',
        'post_engagement',
        'post_shares',
        'post_saves',
        'post_reach',
        'total_views',
        # 'visibility',
        'embed_code'
    )
    # list_display_links = ('campaign', )

    # add_fields = ('url', 'campaign', 'date', 'likes', 'comments',
    #               'post_shares', 'post_saves', 'post_reach', 'embed_code', 'visibility', 'alt_google_photo_url')

    # list_filter = (CampaignNameFilter, )

    list_filter = [
        # ('campaign__name', custom_titled_filter("Campaign")),
        CampaignNameFilter,
        ('upload_date', DateTimeRangeFilter),
        'visibility',
        'post_type',
        'post_username',
    ]

    list_editable = [
        'upload_date',
        'visibility',
        'post_type',
        'likes',
        'comments',
        'post_shares',
        'total_views',
        'post_engagement',
        'post_reach'
    ]

    search_fields = ('post_username', 'url')

    save_on_top = True

    inlines = [
        MediaInline
    ]

    actions = ['export_as_csv']

    def get_rangefilter_upload_date_title(self, request, field_path):
        return 'Upload Date'

    def link_to_post(self, obj):
        return format_html('<a href='+ obj.url +' target="_blank" rel="noopener noreferrer">View Post</a>')

    def link_to_camp(self, obj):
        link = reverse("admin:campaigns_campaign_change",
                       args=[obj.campaign.id])

        link_live = reverse("admin:campaigns_livecampaign_change",
                            args=[obj.campaign.id])

        link_report = reverse("admin:campaigns_campaignreport_change",
                              args=[obj.campaign.id])
        return format_html('<a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/>', link, "Campaign Admin", link_live, "Live Details", link_report, "Report Data")

    link_to_camp.short_description = "Campaign URLs"

    def get_queryset(self, request):
        qs = super(InstagramPostAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name="MasterAdmin").exists():
            return qs
        
        return qs.filter(campaign__staff_profiles=request.user.profile)


@admin.register(FacebookPost)
class FacebookPostAdmin(admin.ModelAdmin, ExportCsvMixin):
    exclude = ('platform', 'embed_code')
    list_display = ('url', 'link_to_post', 'campaign', 'post_type', 'link_to_camp', 'date', 'likes', 'comments',
                    'post_shares', 'post_saves', 'post_reach')

    readonly_fields = ('date', 'link_to_camp')
    fields = ('url', 'campaign', 'link_to_camp', 'date', 'post_type', 'pre_fetched', 'likes', 'comments',
              'post_shares', 'post_saves', 'post_reach',  'visibility', 'alt_google_photo_url')
    # list_display_links = ('campaign', )

    # add_fields = ('url', 'campaign', 'date', 'likes', 'comments',
    #               'post_shares', 'post_saves', 'post_reach', 'embed_code', 'visibility', 'alt_google_photo_url')

    list_filter = [
        CampaignNameFilter,
        ('upload_date', DateTimeRangeFilter)
    ]

    # list_editable = [
    #     'upload_date'
    # ]

    save_on_top = True

    actions = ['export_as_csv']
    search_fields = ('post_username', 'url')

    def link_to_post(self, obj):
        return format_html('<a href='+ obj.url +' target="_blank" rel="noopener noreferrer">Open Post</a>')

    def link_to_camp(self, obj):
        link = reverse("admin:campaigns_campaign_change",
                       args=[obj.campaign.id])

        link_live = reverse("admin:campaigns_livecampaign_change",
                            args=[obj.campaign.id])

        link_report = reverse("admin:campaigns_campaignreport_change",
                              args=[obj.campaign.id])
        return format_html('<a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/>', link, "Campaign Admin", link_live, "Live Details", link_report, "Report Data")

    link_to_camp.short_description = "Campaign URLs"

    def get_queryset(self, request):
        qs = super(FacebookPostAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name="MasterAdmin").exists():
            return qs
        
        return qs.filter(campaign__staff_profiles=request.user.profile)


@admin.register(TwitterPost)
class TwitterPostAdmin(admin.ModelAdmin, ExportCsvMixin):
    exclude = ('platform', )
    # list_display = ('url', 'campaign', 'link_to_camp', 'upload_date',
    #                 'visibility', 'pre_fetched', 'alive', 'likes', 'comments')

    readonly_fields = ('date', 'link_to_camp')
    # fields = ('url', 'campaign', 'link_to_camp', 'upload_date', 'pre_fetched', 'likes', 'comments',
    #           'post_shares', 'post_saves', 'post_reach', 'embed_code', 'visibility', 'alt_google_photo_url')

    list_display = (
        'url',
        'campaign',
        # 'link_to_camp',
        'upload_date',
        'post_username',
        'link_to_post',
        'alive',
        'visibility',
        # 'pre_fetched',
        'likes',
        'comments',
        'post_shares',
        'total_views',
        'post_engagement',
        'post_reach',
    )

    fields = (
        'alive',
        'pre_fetched',
        'url',
        'campaign',
        'link_to_camp',
        'post_username',
        'prof_img_url',
        'account_name',
        'caption',
        'upload_date',
        'likes',
        'comments',
        'post_shares',
        'total_views',
        'post_engagement',
        'post_reach',
        'embed_code',
        'alt_google_photo_url'
    )
    # list_display_links = ('campaign', )

    # add_fields = ('url', 'campaign', 'date', 'likes', 'comments',
    #               'post_shares', 'post_saves', 'post_reach', 'embed_code', 'visibility', 'alt_google_photo_url')

    list_filter = [
        CampaignNameFilter,
        ('upload_date', DateTimeRangeFilter),
        'visibility',
        'post_username'
    ]

    list_editable = [
        'upload_date',
        'likes',
        'comments',
        'post_shares',
        'total_views',
        'post_engagement',
        'post_reach',
    ]

    save_on_top = True

    search_fields = ('post_username', 'url')

    inlines = [
        MediaInline
    ]

    actions = ['export_as_csv', 'add_quote_rt']

    def add_quote_rt(self, request, queryset):
        
        if "apply" in request.POST:

            imgurl = request.POST["imgurl"]

            for post in queryset:
                media_obj, _ = Media.objects.get_or_create(parent_post=post, key="111111", media_type="post")
                media_obj.url = imgurl
                media_obj.save()

            self.message_user(request, "Added Quote RT image on {} tweets".format(queryset.count()))
            
            return HttpResponseRedirect(request.get_full_path())

        form = QuoteRTForm(initial={'_selected_action': queryset.values_list('id', flat=True)})

        return render(
            request,
            'admin/quote_rt_form.html',
            context = {'posts': queryset, 'form': form}
        )

    add_quote_rt.short_description = "Add Quote RT"

    def link_to_post(self, obj):
        return format_html('<a href='+ obj.url +' target="_blank" rel="noopener noreferrer">Open Post</a>')

    def get_rangefilter_upload_date_title(self, request, field_path):
        return 'Upload Date'

    def link_to_camp(self, obj):
        link = reverse("admin:campaigns_campaign_change",
                       args=[obj.campaign.id])

        link_live = reverse("admin:campaigns_livecampaign_change",
                            args=[obj.campaign.id])

        link_report = reverse("admin:campaigns_campaignreport_change",
                              args=[obj.campaign.id])
        return format_html('<a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/>', link, "Campaign Admin", link_live, "Live Details", link_report, "Report Data")

    link_to_camp.short_description = "Campaign URLs"

    def get_queryset(self, request):
        qs = super(TwitterPostAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name="MasterAdmin").exists():
            return qs
        
        return qs.filter(campaign__staff_profiles=request.user.profile)


@admin.register(InstagramStory)
class InstagramStoryAdmin(admin.ModelAdmin, ExportCsvMixin):
    exclude = ('platform', )
    list_display = ('url', 'campaign', 'date')

    list_filter = [
        CampaignNameFilter
    ]

    save_on_top = True

    actions = ['export_as_csv']

    def link_to_camp(self, obj):
        link = reverse("admin:campaigns_campaign_change",
                       args=[obj.campaign.id])

        link_live = reverse("admin:campaigns_livecampaign_change",
                            args=[obj.campaign.id])

        link_report = reverse("admin:campaigns_campaignreport_change",
                              args=[obj.campaign.id])
        return format_html('<a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/>', link, "Campaign Admin", link_live, "Live Details", link_report, "Report Data")

    link_to_camp.short_description = "Campaign URLs"

    def get_queryset(self, request):
        qs = super(InstagramStoryAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name="MasterAdmin").exists():
            return qs
        
        return qs.filter(campaign__staff_profiles=request.user.profile)


@admin.register(FacebookStory)
class FacebookStoryAdmin(admin.ModelAdmin, ExportCsvMixin):
    exclude = ('platform', )
    list_display = ('url', 'campaign', 'date')

    list_filter = [
        CampaignNameFilter
    ]

    save_on_top = True

    actions = ['export_as_csv']

    def link_to_camp(self, obj):
        link = reverse("admin:campaigns_campaign_change",
                       args=[obj.campaign.id])

        link_live = reverse("admin:campaigns_livecampaign_change",
                            args=[obj.campaign.id])

        link_report = reverse("admin:campaigns_campaignreport_change",
                              args=[obj.campaign.id])
        return format_html('<a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/><br/><a href="{}">{}</a><br/>', link, "Campaign Admin", link_live, "Live Details", link_report, "Report Data")

    link_to_camp.short_description = "Campaign URLs"

    def get_queryset(self, request):
        qs = super(FacebookStoryAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name="MasterAdmin").exists():
            return qs
        
        return qs.filter(campaign__staff_profiles=request.user.profile)


@admin.register(TwitterStory)
class TwitterStoryAdmin(admin.ModelAdmin, ExportCsvMixin):
    exclude = ('platform', )
    list_display = ('url', 'campaign', 'date')

    list_filter = [
        CampaignNameFilter
    ]

    actions = ['export_as_csv']

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

    def get_queryset(self, request):
        qs = super(TwitterStoryAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name="MasterAdmin").exists():
            return qs
        
        return qs.filter(campaign__staff_profiles=request.user.profile)
