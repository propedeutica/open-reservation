from django.contrib import admin

# Register your models here.
from .models import Room, Schedule


class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'capacity')
    list_display_links = ('id', 'name')
    list_editable = ('capacity',)


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'room', 'day_of_week', 'start_time',
                    'duration', 'seats_reserved', 'seats_available')
    list_display_links = ('id', '__str__',)
    list_filter = ('room', 'day_of_week', 'start_time',)
    list_editable = ('duration', 'seats_reserved',)


admin.site.register(Room, RoomAdmin)
admin.site.register(Schedule, ScheduleAdmin)
