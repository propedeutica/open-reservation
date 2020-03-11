from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'info/home.html')


def about(request):
    return render(request, 'info/about.html')


def help(request):
    return render(request, 'info/help.html')
