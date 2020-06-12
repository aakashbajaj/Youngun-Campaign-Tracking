from django.db import models
from django.utils.translation import gettext as _


class Organisation(models.Model):
    name = models.CharField(max_length=255)
    email_prefix = models.CharField(_("email suffix"), max_length=255)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )

    mainUser = models.BooleanField(default=False)

    organisation = models.ForeignKey("Organisation", verbose_name=_(
        "organisation"), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username
