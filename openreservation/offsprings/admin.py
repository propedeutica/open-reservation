from django.contrib import admin

from .models import Offspring
import csv
from django.http import HttpResponse


# Register your models here.
class OffspringAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'grade',
                    'parent', 'assignment', 'baptized', 'father_name', 'mother_name', 'school', 'home_address')
    list_display_links = ('id', 'first_name', 'last_name')

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field)
                                   for field in field_names])

        return response

    export_as_csv.short_description = "Exportar seleccionados"


admin.site.register(Offspring, OffspringAdmin)
