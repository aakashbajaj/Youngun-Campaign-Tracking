from django.contrib import admin

from django.utils.safestring import mark_safe
from django.urls import reverse
from django.utils.html import format_html

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


# class EditLinkToInlineObject(object):
#     def edit_link(self, instance):
#         print(self)
#         print(instance)
#         # print(self._meta)
#         print("***** ", instance._meta)
#         print("***** ", instance._meta.model_name)
#         url = reverse('admin:%s_%s_change' % (
#             instance._meta.app_label,  "staffuser"),  args=[instance.user.pk])
#         print("**&& ", url)
#         if instance.pk:
#             return mark_safe(u'<a href="{u}">edit</a>'.format(u=url))
#         else:
#             return ''


class AddedUserInline(admin.TabularInline):
    model = ClientProfile
    # fk_name = "invited_by_user"


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


class StaffUser(User):
    class Meta:
        proxy = True


class StaffProfileInlines(admin.StackedInline):
    model = StaffProfile
    filter_horizontal = ['campaigns']
    # readonly_fields = ('edit_link', )


@admin.register(StaffUser)
class StaffProfileAdmin(admin.ModelAdmin):
    form = StaffUserChangeForm
    add_form = StaffUserCreationForm

    fieldsets = (
        (None, {'fields': ('email', 'password', 'mobile',
                           'is_active', 'is_superuser', 'groups')}),
    )

    list_display = ['email', 'list_invited_profiles']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'list_invited_profiles'),
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

    def list_invited_profiles(self, obj):
        email_list = [x.user.email for x in obj.profile.invited_users.filter(
            user__is_active=True)]
        if(len(email_list) > 0):
            disp_list = ""
            for email in email_list:
                disp_list = disp_list + "<p>" + email + "</p><br/>"
            return format_html(disp_list)
        else:
            return format_html('<p>--</p>')

    list_invited_profiles.short_description = "Invitees"


class ClientUser(User):
    class Meta:
        proxy = True


class ClientProfileInlines(admin.StackedInline):
    model = ClientProfile
    filter_horizontal = ['campaigns']


class AddedClientProfileInline(admin.TabularInline):
    model = ClientProfile
    extra = 0


@admin.register(ClientUser)
class ClientProfileAdmin(admin.ModelAdmin):
    form = ClientUserChangeForm
    add_form = ClientUserCreationForm

    fieldsets = (
        (None, {'fields': ('email', 'password', 'mobile',
                           'is_active', 'is_superuser')}),
    )

    search_fields = ["email"]

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_superuser'),
        }),
    )
    filter_horizontal = ["groups"]

    list_display = ['email', 'list_invited_profiles',
                    'is_main_user', 'is_active']

    inlines = [ClientProfileInlines]
    # search_fields = ["campaigns"]

    list_filter = [
        ('usermanager_staffprofile__campaigns__name',
         custom_titled_filter("Campaign")),
        'is_active'
    ]

    def get_queryset(self, request):
        qs = super(ClientProfileAdmin, self).get_queryset(request)
        qs = qs.exclude(usermanager_clientprofile__isnull=True)
        return qs

    def is_main_user(self, obj):
        return obj.profile.is_main_user

    def list_invited_profiles(self, obj):
        email_list = [x.user.email for x in obj.profile.invited_users.filter(
            user__is_active=True)]
        if(len(email_list) > 0):
            disp_list = ""
            for email in email_list:
                disp_list = disp_list + "<p>" + email + "</p><br/>"
            return format_html(disp_list)
        else:
            return format_html('<p>--</p>')

    list_invited_profiles.short_description = "Invitees"
