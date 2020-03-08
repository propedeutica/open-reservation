from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('about', views.about, name='about'),
    path('help', views.help, name='help'),
]