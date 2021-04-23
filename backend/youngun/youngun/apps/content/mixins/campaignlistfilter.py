from django.contrib.admin import SimpleListFilter
from youngun.apps.campaigns.models import Campaign

class CampaignNameFilter(SimpleListFilter):
    title = 'Campaign'
    parameter_name = 'campaign__name'

    def lookups(self, request, model_admin):

        qs = Campaign.objects.all()

        if not request.user.is_superuser or request.user.groups.filter(name="MasterAdmin").exists():
            qs = qs.filter(staff_profiles=request.user.profile)

        output_list = [(camp.id, camp.name) for camp in qs]

        return output_list

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset

        return queryset.filter(campaign__id=self.value())