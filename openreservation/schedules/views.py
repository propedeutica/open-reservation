from django.shortcuts import render

# Create your views here.

from .models import Schedule
from .models import Room

# To annotate values
from django.db.models import Value


def index(request):
    schedules = Schedule.objects.order_by('day_of_week', 'room').all()

    # from django.db.models import Count
    # schedules.objects.anotate(reserved=Count('assignments'))

    context = {
        'schedules': schedules,
    }
    return render(request, 'schedules/index.html', context)
