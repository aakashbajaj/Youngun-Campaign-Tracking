from django.contrib import admin

from .models import Profile, Brand, ClientProfile, StaffProfile
# Register your models here.


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     pass

@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    search_fields = ["campaigns"]
    filter_horizontal = ['campaigns']


@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    search_fields = ["campaigns"]
    filter_horizontal = ['campaigns']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass
