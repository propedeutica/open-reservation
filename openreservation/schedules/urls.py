from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='schedules_index'),
]
