from django.shortcuts import render
from django.views.generic import View

from .models import Turnip
from .forms import TurnipForm

# Create your views here.

class PriceList(View):
    def get(self, request):
        form = TurnipForm()
        prices = Turnip.objects.all()
        return render (request, 'trackerapp/form.html', context={'form': form})

def home(request):
    context = {}
    return render(request, 'trackerapp/home.html', context)

def profile(request):
    context = {}
    return render(request, 'trackerapp/profile.html', context)

def chart(request):
    context = {}
    return render(request, 'trackerapp/form.html', context)
