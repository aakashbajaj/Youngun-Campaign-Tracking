from django.contrib import admin


from youngun.apps.authentication.models import User
from .models import Profile, Brand, Organisation

from youngun.apps.authentication.admin import UserAdmin
# Register your models here.


class InlineProfile(admin.StackedInline):
    model = Profile
    extra = 1
    max_num = 1


# @admin.register(Profile)
class ExtendedProfileAdmin(UserAdmin):
    inlines = [InlineProfile, ] + UserAdmin.inlines


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(User)
admin.site.register(User, ExtendedProfileAdmin)
