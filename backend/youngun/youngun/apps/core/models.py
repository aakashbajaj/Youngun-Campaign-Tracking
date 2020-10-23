from django.db import models

from youngun.apps.authentication.models import User

from django.utils.translation import gettext as _

# Create your models here.


class MasterLogger(models.Model):
    user = models.OneToOneField("authentication.User", verbose_name=_(
        "User"), on_delete=models.CASCADE, related_name="masterlogger")
    email = models.EmailField(_("User Email"), max_length=254)
    # full_name = models.CharField(
    #     _("User Name"), max_length=255, default="", blank=True)
    login_cnt = models.IntegerField(_("Total Login Count"), default=0)

    last_login = models.DateTimeField(
        _("Last Login"), auto_now=False, auto_now_add=False, blank=True, null=True)

    history_log = models.TextField(_("Login History"))

    def __str__(self):
        return self.email
    


# class LoginLogger(models.Model):
#     master_user = models.ForeignKey(MasterLogger, verbose_name=_(
#         "User Master Logger"), on_delete=models.DO_NOTHING)
#     login_time = models.DateTimeField(_("Login Time"), auto_now_add=True)

# class CampaignLogger(models.Model):
