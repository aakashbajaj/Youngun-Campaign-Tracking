from django.contrib import admin

from .models import Profile, Brand, ClientProfile, StaffProfile
from youngun.apps.authentication.models import User

from .forms import StaffUserChangeForm, StaffUserCreationForm, ClientUserChangeForm, ClientUserCreationForm


def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


class StaffUser(User):
    class Meta:
        proxy = True


class StaffProfileInlines(admin.StackedInline):
    model = StaffProfile
    filter_horizontal = ['campaigns']


@admin.register(StaffUser)
class StaffProfileAdmin(admin.ModelAdmin):
    form = StaffUserChangeForm
    add_form = StaffUserCreationForm

    fieldsets = (
        (None, {'fields': ('email', 'password', 'mobile',
                           'is_active', 'is_superuser', 'groups')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

    inlines = [StaffProfileInlines]
    filter_horizontal = ["groups"]
    # search_fields = ["campaigns"]

    list_filter = [
        ('usermanager_staffprofile__campaigns__name',
         custom_titled_filter("Campaign")),
    ]

    def get_queryset(self, request):
        qs = super(StaffProfileAdmin, self).get_queryset(request)
        qs = qs.exclude(usermanager_staffprofile__isnull=True)
        return qs


class ClientUser(User):
    class Meta:
        proxy = True


class ClientProfileInlines(admin.StackedInline):
    model = ClientProfile
    filter_horizontal = ['campaigns']


@admin.register(ClientUser)
class ClientProfileAdmin(admin.ModelAdmin):
    form = ClientUserChangeForm
    add_form = ClientUserCreationForm

    fieldsets = (
        (None, {'fields': ('email', 'password', 'mobile',
                           'is_active', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_superuser'),
        }),
    )
    filter_horizontal = ["groups"]

    inlines = [ClientProfileInlines]
    # search_fields = ["campaigns"]

    list_filter = [
        ('usermanager_staffprofile__campaigns__name',
         custom_titled_filter("Campaign")),
    ]

    def get_queryset(self, request):
        qs = super(ClientProfileAdmin, self).get_queryset(request)
        qs = qs.exclude(usermanager_clientprofile__isnull=True)
        return qs
