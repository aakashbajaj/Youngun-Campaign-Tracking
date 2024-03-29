from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models

from django.utils.translation import gettext as _
from django.core.validators import RegexValidator

from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        # if username is None:
        #     raise TypeError("User must have a username")
        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_("Email"), db_index=True, unique=True)
    username = models.CharField(
        _("Username"), max_length=255, blank=True, null=True)

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tempid = models.CharField(
        _("TempID"), blank=True, null=True, max_length=50)
    tempotp = models.CharField(
        _("TempOTP"), blank=True, null=True, max_length=50)
    authInProgress = models.BooleanField(
        _("AuthInProgress"), blank=True, default=False)
    last_requested = models.DateTimeField(
        _("Last OTP Request"), auto_now=False, auto_now_add=False, blank=True, null=True)
    last_login = models.DateTimeField(
        _("Last Login"), auto_now=False, auto_now_add=False, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super(User, self).save(*args, **kwargs)

    @property
    def token(self):
        return self._generate_token()

    @property
    def token_string(self):
        return self.token.key

    def _generate_token(self):
        token, _ = Token.objects.get_or_create(user=self)
        return token

    @property
    def profile(self):
        if hasattr(self, "usermanager_staffprofile"):
            return self.usermanager_staffprofile
        elif hasattr(self, "usermanager_clientprofile"):
            return self.usermanager_clientprofile
        else:
            return None
