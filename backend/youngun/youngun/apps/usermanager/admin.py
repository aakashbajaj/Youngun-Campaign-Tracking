from django.contrib import admin


from youngun.apps.authentication.models import User
from .models import Profile, Brand, Organisation

from youngun.apps.authentication.admin import UserAdmin
# Register your models here.


class InlineUser(admin.StackedInline):
    model = User
    extra = 1
    max_num = 1


class ProfileAdmin(admin.ModelAdmin):
    model = Profile

# @admin.register(Profile)


class ExtendedProfileAdmin(ProfileAdmin):
    inlines = ProfileAdmin.inlines + [InlineUser, ]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    pass


# admin.site.unregister(User)
admin.site.register(Profile, ExtendedProfileAdmin)
