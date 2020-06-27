from django.contrib import admin

from .models import Profile, Brand, Organisation
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    pass
