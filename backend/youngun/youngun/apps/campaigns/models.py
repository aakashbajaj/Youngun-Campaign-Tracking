from django.db import models

from django.utils.translation import gettext as _

from youngun.apps.usermanager.models import Brand
# Create your models here.


class Status(models.TextChoices):
    ACTIVE = 'active'
    COMPLETED = 'completed'


class Campaign(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    brand = models.ForeignKey(Brand, verbose_name=_(
        "Brand"), related_name="campaigns", on_delete=models.CASCADE, null=True, blank=True)
    hashtag = models.CharField(_("Hashtag"), max_length=100)
    status = models.CharField(
        _("Status"), choices=Status.choices, max_length=50, default=Status.ACTIVE)

    start_date = models.DateField(_("Campaign Start"), blank=True, null=True)
    end_date = models.DateField(_("Campaign End"), blank=True, null=True)

    slide_url = models.URLField(
        _("Slide URL"), max_length=200, default="http://example.com")

    live_google_sheet = models.URLField(
        _("Live Google Sheet"), max_length=200, default="http://example.com")
    reports_google_sheet = models.URLField(
        _("Reports Google Sheet"), max_length=200, default="http://example.com")

    slug = models.SlugField(_("Slug"), blank=True)

    @property
    def get_instagram_posts(self):
        return self.posts.filter(platform="in")

    @property
    def get_facebook_posts(self):
        return self.posts.filter(platform="fb")

    @property
    def get_twitter_posts(self):
        return self.posts.filter(platform="tw")

    @property
    def get_instagram_stories(self):
        return self.stories.filter(platform="in")

    @property
    def get_facebook_stories(self):
        return self.stories.filter(platform="fb")

    @property
    def get_twitter_stories(self):
        return self.stories.filter(platform="tw")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Admin - Campaign"

    # Live Metrics
    particaipating_profiles = models.IntegerField(
        _("participating profiles"), default=0)
    unique_content_pieces = models.IntegerField(
        _("unique content pieces"), default=0)

    approved_content_pieces = models.IntegerField(
        _("approved content pieces"), default=0)

    @property
    def remaining_content_pieces(self):
        return self.unique_content_pieces - self.approved_content_pieces

    last_updated = models.DateTimeField(_("last updated"), auto_now=True)

    fb_posts = models.IntegerField(_("facebook posts"), default=0)
    fb_stories = models.IntegerField(_("facebook stories"), default=0)
    in_posts = models.IntegerField(_("instagram posts"), default=0)
    in_stories = models.IntegerField(_("instagram stories"), default=0)
    tw_posts = models.IntegerField(_("twitter posts"), default=0)
    tw_stories = models.IntegerField(_("twitter stories"), default=0)

    live_fb_posts = models.IntegerField(_("live facebook posts"), default=0)
    live_fb_stories = models.IntegerField(
        _("live facebook stories"), default=0)
    live_in_posts = models.IntegerField(_("live instagram posts"), default=0)
    live_in_stories = models.IntegerField(
        _("live instagram stories"), default=0)
    live_tw_posts = models.IntegerField(_("live twitter posts"), default=0)
    live_tw_stories = models.IntegerField(_("live twitter stories"), default=0)

    in_stories_google_photos_album_url = models.URLField(
        _("Instagram Stories Album URL"), max_length=500, default="http://example.com", blank=True)

    in_stories_fetch_ctrl = models.BooleanField(
        _("Instagram Stories fetched?"), default=False)

    fb_stories_google_photos_album_url = models.URLField(
        _("Facebook Stories Album URL"), max_length=500, default="http://example.com", blank=True)

    fb_stories_fetch_ctrl = models.BooleanField(
        _("Facebook Stories fetched?"), default=False)

    tw_stories_google_photos_album_url = models.URLField(
        _("Twitter Stories Album URL"), max_length=500, default="http://example.com", blank=True)

    tw_stories_fetch_ctrl = models.BooleanField(
        _("Twitter Stories fetched?"), default=False)

    # Campaign Report
    num_content_pieces = models.IntegerField(
        _("num content pieces"), default=0)
    num_posts = models.IntegerField(_("num posts"), default=0)
    num_stories = models.IntegerField(_("num stories"), default=0)
    post_stats = models.IntegerField(_("post stats"), default=0)
    post_shares = models.IntegerField(_("post shares"), default=0)
    post_saves = models.IntegerField(_("post saves"), default=0)
    post_reach = models.IntegerField(_("post reach"), default=0)
    story_views = models.IntegerField(_("story views"), default=0)
    website_traffic = models.IntegerField(_("website traffic"), default=0)
    cost_per_engagement = models.CharField(
        _("cost per engagement"), max_length=50, blank=True)
    cost_per_post_impression = models.CharField(
        _("cost per post impression"), max_length=50, blank=True)
    total_post_engagement = models.CharField(
        _("total post engagement"), max_length=50, blank=True)
    total_campaign_reach = models.CharField(
        _("total campaign reach"), max_length=50, blank=True)


class LiveCampaign(Campaign):
    class Meta:
        proxy = True
        verbose_name_plural = "Campaign Live Details"


class CampaignReport(Campaign):
    class Meta:
        proxy = True
        verbose_name_plural = "Campaign Report Data"
