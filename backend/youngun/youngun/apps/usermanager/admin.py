from django.contrib import admin


from youngun.apps.authentication.models import User
from .models import Profile, Brand, StaffProfile, ClientProfile

# Register your models here.


class InlineUser(admin.StackedInline):
    model = User
    extra = 1
    max_num = 1


class ProfileAdmin(admin.ModelAdmin):
    model = Profile

# @admin.register(Profile)
# class ExtendedProfileAdmin(ProfileAdmin):
#     inlines = ProfileAdmin.inlines + [InlineUser, ]


class StaffProfileAdmin(admin.ModelAdmin):
    model = StaffProfile


class ClientProfileAdmin(admin.ModelAdmin):
    model = ClientProfile


@admin.register(StaffProfile)
class ExtendedStaffProfileAdmin(StaffProfileAdmin):
    inlines = StaffProfileAdmin.inlines + [InlineUser, ]


@admin.register(ClientProfile)
class ExtendedClientProfileAdmin(ClientProfileAdmin):
    inlines = ClientProfileAdmin.inlines + [InlineUser, ]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


# admin.site.unregister(User)
# admin.site.register(Profile, ExtendedProfileAdmin)
