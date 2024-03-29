from django.contrib import admin

from django.utils.html import format_html

from .models import Campaign, LiveCampaign, CampaignReport
from youngun.apps.usermanager.models import StaffProfile, ClientProfile
from .forms import ImportPostForm
# Register your models here.


# class ProfileInline(admin.TabularInline):
#     model = Profile.campaigns.through
#     extra = 0
#     max_num = 4

#     def get_queryset(self, request):
#         qs = super(ProfileInline, self).get_queryset(request)
#         return qs.filter(profile__user__is_staff=True)
#         # return Profile.campaigns.through.all()


class StaffProfileInline(admin.TabularInline):
    model = StaffProfile.campaigns.through
    extra = 0
    # max_num = 4

    verbose_name = "Staff Profile"
    verbose_name_plural = "Staff Profiles"

    # def get_queryset(self, request):
    #     qs = super(StaffProfileInline, self).get_queryset(request)
    #     return qs.filter(profile__user__is_staff=True)
    # return Profile.campaigns.through.all()


class ClientProfileInline(admin.TabularInline):
    model = ClientProfile.campaigns.through
    extra = 0
    # max_num = 4

    verbose_name = "Client Profile"
    verbose_name_plural = "Client Profiles"

    # def get_queryset(self, request):
    #     qs = super(ProfileInline, self).get_queryset(request)
    #     return qs.filter(profile__user__is_staff=True)
    # return Profile.campaigns.through.all()


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'company_name',
        'hashtag',
        'status',
        'campaign_module',
        'start_date',
        'end_date',
        # 'posts',
        # 'instagram_posts'
    )

    inlines = [
        StaffProfileInline,
        ClientProfileInline
    ]

    list_editable = [
        'status',
        'campaign_module',
    ]

    fields = [
        'name',
        'slug',
        'company_name',
        'hashtag',
        'status',
        'campaign_module',
        'start_date',
        'end_date',
        'slide_url',
    ]

    list_filter = ['status', 'campaign_module']
    save_on_top = True

    def get_queryset(self, request):
        qs = super(CampaignAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name="MasterAdmin").exists():
            return qs
        return qs.filter(staff_profiles=request.user.profile)


@admin.register(LiveCampaign)
class LiveCampaignAdmin(admin.ModelAdmin):
    form = ImportPostForm
    list_display = (
        'name',
        'company_name',
        'status',
        'post_lists',
        'particaipating_profiles',
        'unique_content_pieces',
        'approved_content_pieces',
        'in_posts',
        'live_in_posts_cnt',
        'in_stories',
        'live_in_stories_cnt',
        'fb_posts',
        'live_fb_posts_cnt',
        'fb_stories',
        'live_fb_stories_cnt',
        'tw_posts',
        'live_tw_posts_cnt',
        'tw_stories',
        'live_tw_stories_cnt',

        'in_engagement',
        'tw_engagement',
        'fb_engagement',
        'in_reach',
        'tw_reach',
        'fb_reach'
    )

    list_filter = ['status']
    save_on_top = True

    def post_lists(self, obj):
        link = "/admin/content/post/?campaign__name=" + \
            obj.name.replace(" ", "+")
        in_link = "/admin/content/instagrampost/?campaign__name=" + \
            obj.name.replace(" ", "+")
        fb_link = "/admin/content/facebookpost/?campaign__name=" + \
            obj.name.replace(" ", "+")
        tw_link = "/admin/content/twitterpost/?campaign__name=" + \
            obj.name.replace(" ", "+")
        return format_html('<a href="{}">{}</a>\n<a href="{}">{}</a>\n<a href="{}">{}</a>\n<a href="{}">{}</a>', link, "All Posts", in_link, "Instagram", fb_link, "Facebook",  tw_link, "Twitter")

    def get_queryset(self, request):
        qs = super(LiveCampaignAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name="MasterAdmin").exists():
            return qs
        return qs.filter(staff_profiles=request.user.profile)


@admin.register(CampaignReport)
class CampaignReportAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'company_name',
        'status',
        'num_content_pieces',
        'num_posts',
        'post_engagement',
        'post_shares',
        'post_saves',
        'video_views',
        'post_reach',
        'num_stories',
        'story_views',
        'cost_per_engagement',
        'cost_per_reach',
        'total_post_engagement',
        'total_campaign_reach',
    )

    list_filter = ['status']
    save_on_top = True

    def get_queryset(self, request):
        qs = super(CampaignReportAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name="MasterAdmin").exists():
            return qs
        return qs.filter(staff_profiles=request.user.profile)


admin.site.header = "Youngun Campaign tracker Admin"
