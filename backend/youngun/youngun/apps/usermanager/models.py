from django.db import models

from django.utils.translation import gettext as _
# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(
        "authentication.User", verbose_name=_(""), on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s")
    first_name = models.CharField(
        _("First Name"), max_length=255, blank=True, default="")
    last_name = models.CharField(
        _("Last Name"), max_length=255, blank=True, default="")

    class Meta:
        abstract = True

    def __str__(self):
        return self.user.email

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    @property
    def full_name(self):
        return self.get_full_name


class ClientProfile(Profile):
    campaigns = models.ManyToManyField(
        "campaigns.Campaign", verbose_name=_("campaigns"), related_name="client_profiles", blank=True)

    brand = models.ForeignKey(Brand, verbose_name=_(
        "Brand"), related_name="client_profile", on_delete=models.CASCADE, null=True, blank=True)

    is_main_user = models.BooleanField(_("Main User"), default=False)
    added_by = models.ForeignKey("self", verbose_name=_(
        "Added By"), on_delete=models.DO_NOTHING, related_name='invited_users', blank=True, default=None, null=True)


class StaffProfile(Profile):
    campaigns = models.ManyToManyField(
        "campaigns.Campaign", verbose_name=_("campaigns"), related_name="staff_profiles", blank=True)

    brand = models.ForeignKey(Brand, verbose_name=_(
        "Brand"), related_name="staff_profile", on_delete=models.CASCADE, null=True, blank=True)

    added_by = models.ForeignKey("self", verbose_name=_(
        "Added By"), on_delete=models.DO_NOTHING, related_name='invited_users', blank=True, default=None, null=True)

    @property
    def is_main_user(self):
        return True

    @property
    def invited_by_user(self):
        return self.added_by.user
