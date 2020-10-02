from django.db import models
from django.utils.translation import gettext as _

from django.urls import reverse

from youngun.apps.campaigns.models import Campaign

# Create your models here.


class Platform(models.TextChoices):
    FACEBOOK = "fb"
    INSTAGRAM = "in"
    TWITTER = "tw"


class MediaType(models.TextChoices):
    POST = "post"
    VIDEO = "video"


class PostVisibility(models.Choices):
    PUBLIC = 'public'
    PRIVATE = 'private'


class Post(models.Model):
    url = models.URLField(_("post url"), max_length=1000, unique=True)
    platform = models.CharField(
        _("platform"), max_length=50, choices=Platform.choices)
    campaign = models.ForeignKey(Campaign, verbose_name=_(
        "campaign"), related_name="posts", on_delete=models.CASCADE)

    post_username = models.CharField(
        _("Post Upload Username"), max_length=100, blank=True, null=True)

    social_id = models.CharField(
        _("Post Social ID"), max_length=200, blank=True, null=True)
    account_name = models.CharField(
        _("Account Name"), max_length=200, blank=True, null=True)
    upload_date = models.DateTimeField(
        _("Upload DateTime"), auto_now=False, auto_now_add=False, blank=True, null=True)
    caption = models.TextField(_("Post Caption"), blank=True, null=True)

    pre_fetched = models.BooleanField(_("Data Pre Fetched"), default=False)

    likes = models.IntegerField(_("likes"), default=0)
    comments = models.IntegerField(_("comments"), default=0)
    post_shares = models.IntegerField(_("post_shares"), default=0)
    post_saves = models.IntegerField(_("post_saves"), default=0)
    post_reach = models.IntegerField(_("post_reach"), default=0)
    date = models.DateTimeField(_("posted date"), auto_now_add=True)

    alive = models.BooleanField(_("Post Health"), default=True)

    embed_code = models.TextField(_("embed code"), null=True, blank=True)
    alt_google_photo_url = models.URLField(
        _("Alternate Google Photo URL"), max_length=8000, null=True, blank=True)
    visibility = models.CharField(
        _("post visibility"), choices=PostVisibility.choices, max_length=50, default='public')

    post_type = models.CharField(
        _("post_type"), max_length=50, choices=[("p", "Post"), ("v", "Video")], null=True, blank=True)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name_plural = "All Posts"


class Story(models.Model):
    url = models.URLField(_("Story Snapshot URL"),
                          max_length=200, default="example.com")
    campaign = models.ForeignKey(Campaign, verbose_name=_(
        "campaign"), related_name="stories", on_delete=models.CASCADE)
    platform = models.CharField(
        _("platform"), max_length=50, choices=Platform.choices, default='in')
    story_views = models.IntegerField(_("Story Views"), default=0)
    date = models.DateTimeField(_("posted timestamp"), auto_now_add=True)

    class Meta:
        verbose_name_plural = "All Stories"

    # def __str__(self):
    #     return self.url


class Media(models.Model):
    parent_post = models.ForeignKey(Post, verbose_name=_(
        "post"), related_name="medias", on_delete=models.CASCADE)
    key = models.CharField(_("Media Key"), max_length=200)
    url = models.URLField(_("Media URL"), max_length=2000)
    media_type = models.CharField(
        _("Media Type"), max_length=50, choices=MediaType.choices)
    media_views = models.IntegerField(_("Media Views"), default=0)

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media Objects")

    def __str__(self):
        return self.key

    def get_absolute_url(self):
        return reverse("Media_detail", kwargs={"pk": self.pk})


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
        verbose_name_plural = "Instagram Posts"

    objects = InstagramPostManager()


class FacebookPost(Post):
    def save(self, *args, **kwargs):
        self.platform = Platform.FACEBOOK
        return super(FacebookPost, self).save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name_plural = "Facebook Posts"

    objects = FacebookPostManager()


class TwitterPost(Post):
    def save(self, *args, **kwargs):
        self.platform = Platform.TWITTER
        return super(TwitterPost, self).save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name_plural = "Twitter Posts"

    objects = TwitterPostManager()


class InstagramStoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(platform=Platform.INSTAGRAM)


class FacebookStoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(platform=Platform.FACEBOOK)


class TwitterStoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(platform=Platform.TWITTER)


class InstagramStory(Story):
    def save(self, *args, **kwargs):
        self.platform = Platform.INSTAGRAM
        return super(InstagramStory, self).save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name_plural = "Instagram Stories"

    objects = InstagramStoryManager()


class FacebookStory(Story):
    def save(self, *args, **kwargs):
        self.platform = Platform.FACEBOOK
        return super(FacebookStory, self).save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name_plural = "Facebook Stories"

    objects = FacebookStoryManager()


class TwitterStory(Story):
    def save(self, *args, **kwargs):
        self.platform = Platform.TWITTER
        return super(TwitterStory, self).save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name_plural = "Twitter Stories"

    objects = TwitterStoryManager()
