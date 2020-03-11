from django.urls import path

from . import views

app_name = 'info'
urlpatterns = [
    path('', views.home, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
]
