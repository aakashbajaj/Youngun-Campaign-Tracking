from django.db import models

from django.utils.translation import gettext as _
# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Profile(models.Model):
    # user = models.OneToOneField(
    #     "authentication.User", verbose_name=_(""), on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(
        _("First Name"), max_length=255, blank=True, default="")
    last_name = models.CharField(
        _("Last Name"), max_length=255, blank=True, default="")

    campaigns = models.ManyToManyField(
        "campaigns.Campaign", verbose_name=_("campaigns"), related_name="profiles", blank=True)

    is_main_user = models.BooleanField(_("Main User"), default=False)
    is_staff_profile = models.BooleanField(
        _("Is Staff Profile"), default=False)
    is_client_profile = models.BooleanField(
        _("Is Client Profile"), default=True)

    added_by = models.ForeignKey("self", verbose_name=_(
        "Added By"), on_delete=models.DO_NOTHING, related_name='invited_users', blank=True, default=None, null=True)

    def __str__(self):
        return self.user.email

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    @property
    def full_name(self):
        return self.get_full_name


class StaffProfileManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_staff_profile=True)


class StaffProfile(Profile):
    def save(self, *args, **kwargs):
        self.is_staff_profile = True
        return super(StaffProfile, self).save(*args, **kwargs)

    class Meta:
        proxy = True

    objects = StaffProfileManager()


class ClientProfileManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_client_profile=True)


class ClientProfile(Profile):
    def save(self, *args, **kwargs):
        self.is_client_profile = True
        return super(ClientProfile, self).save(*args, **kwargs)

    class Meta:
        proxy = True

    objects = ClientProfileManager()
