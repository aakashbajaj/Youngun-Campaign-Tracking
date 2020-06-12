from django.db import models

from django.template.defaultfilters import slugify
from django.utils.translation import gettext as _
# Create your models here.


class Status(models.TextChoices):
    ACTIVE = 'active'
    COMPLETED = 'completed'


class Campaign(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    organisation = models.ForeignKey("profiles.Organisation", verbose_name=_(
        "Organisation"), on_delete=models.CASCADE, null=True)
    hashtag = models.CharField(_("Hashtag"), max_length=100)
    status = models.CharField(_("Campaign Status"),
                              choices=Status.choices, max_length=50)

    start_date = models.DateField(_("Campaign Start"))
    start_date = models.DateField(_("Campaign End"))

    slide_url = models.URLField(
        _("Slide URL"), max_length=200, default="example.com")

    @property
    def slug(self):
        return slugify(self.name)

    def __str__(self):
        return self.name

    # Live Metrics
    particaipating_profiles = models.IntegerField(
        _("particaipating profiles"), default=0)
    unique_content_pieces = models.IntegerField(
        _("unique content pieces"), default=0)

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
