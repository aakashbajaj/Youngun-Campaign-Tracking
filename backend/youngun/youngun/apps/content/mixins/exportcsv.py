import csv
from django.http import HttpResponse

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        fields_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = "attachment; filename={}.csv".format(
            meta)
        writer = csv.writer(response)

        writer.writerow(fields_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field)
                                   for field in fields_names])

        return response


    def export_only_post_links_csv(self, request, queryset):
        meta = self.model._meta
        fields_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = "attachment; filename={}.csv".format(
            meta)
        writer = csv.writer(response)

        # writer.writerow(fields_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, 'url')])

        return response