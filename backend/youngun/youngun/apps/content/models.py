from django.db import models
from django.utils.translation import gettext as _

from youngun.apps.campaigns.models import Campaign

# Create your models here.


class Platform(models.TextChoices):
    FACEBOOK = "fb"
    INSTAGRAM = "in"
    TWITTER = "tw"


class PostVisibility(models.Choices):
    PUBLIC = 'public'
    PRIVATE = 'private'


class Post(models.Model):
    url = models.URLField(_("post url"), max_length=255, unique=True)
    platform = models.CharField(
        _("platform"), max_length=50, choices=Platform.choices)
    campaign = models.ForeignKey(Campaign, verbose_name=_(
        "campaign"), related_name="posts", on_delete=models.CASCADE)
    likes = models.IntegerField(_("likes"), default=0)
    comments = models.IntegerField(_("comments"), default=0)
    post_shares = models.IntegerField(_("post_shares"), default=0)
    post_saves = models.IntegerField(_("post_saves"), default=0)
    post_reach = models.IntegerField(_("post_reach"), default=0)
    date = models.DateField(_("posted date"), auto_now_add=True)

    embed_code = models.TextField(_("embed code"), null=True, blank=True)
    visibility = models.CharField(
        _("post visibility"), choices=PostVisibility.choices, max_length=50, default=PostVisibility.PUBLIC)

    post_type = models.CharField(
        _("post_type"), max_length=50, choices=[("p", "Post"), ("v", "Video")], null=True, blank=True)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name_plural = "All Posts"


class Story(models.Model):
    campaign = models.ForeignKey(Campaign, verbose_name=_(
        "campaign"), on_delete=models.CASCADE)
    platform = models.CharField(
        _("platform"), max_length=50, choices=Platform.choices)
    story_views = models.IntegerField(_("Story Views"), default=0)
    date = models.DateField(_("posted date"), auto_now_add=True)

    class Meta:
        verbose_name_plural = "All Stories"


class InstagramPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(platform=Platform.INSTAGRAM)


class FacebookPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(platform=Platform.FACEBOOK)


class TwitterPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(platform=Platform.TWITTER)


class InstagramPost(Post):
    def save(self, *args, **kwargs):
        self.platform = Platform.INSTAGRAM
        return super(InstagramPost, self).save(*args, **kwargs)

    class Meta:
        proxy = True

    objects = InstagramPostManager()


class FacebookPost(Post):
    def save(self, *args, **kwargs):
        self.platform = Platform.FACEBOOK
        return super(FacebookPost, self).save(*args, **kwargs)

    class Meta:
        proxy = True

    objects = FacebookPostManager()


class TwitterPost(Post):
    def save(self, *args, **kwargs):
        self.platform = Platform.TWITTER
        return super(TwitterPost, self).save(*args, **kwargs)

    class Meta:
        proxy = True

    objects = TwitterPostManager()
