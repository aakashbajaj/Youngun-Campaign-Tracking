from django.contrib import admin

from youngun.apps.authentication.models import User
from .models import Profile, Organisation

# Register your models here.


class UserAdminInline(admin.StackedInline):
    model = User


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     inlines = (UserAdminInline, )


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    pass
