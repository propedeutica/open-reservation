from django.contrib import admin

from .models import User
from offsprings.models import Offspring
import csv



class OffspringInline(admin.TabularInline):
    model = Offspring


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name',
                    'email', 'phone', 'offsprings_surname', 'offsprings_count',
                    'has_usable_password','phone2','phone3','comments',)
    list_display_links = ('id', 'first_name', 'last_name', 'email',)

    inlines = [
        OffspringInline,
    ]

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


admin.site.register(User, UserAdmin)
