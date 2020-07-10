from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'trackerapp/home.html', context)

def profile(request):
    context = {}
    return render(request, 'trackerapp/profile.html', context)
