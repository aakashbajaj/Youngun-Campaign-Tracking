from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models

from django.utils.translation import gettext as _

from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError("User must have a username")
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


class Organisation(models.Model):
    name = models.CharField(max_length=255)
    email_suffix = models.CharField(_("email suffix"), max_length=255)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_("Name"), max_length=255, blank=True, default="")
    email = models.EmailField(_("Email"), db_index=True, unique=True)
    username = models.CharField(
        _("Username"), db_index=True, max_length=255, unique=True)
    organisation = models.ForeignKey("Organisation", verbose_name=_(
        "organisation"), on_delete=models.CASCADE, null=True)
    mainUser = models.BooleanField(_("Main User"), default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_token()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def _generate_token(self):
        token, _ = Token.objects.get_or_create(user=self)
        return token
