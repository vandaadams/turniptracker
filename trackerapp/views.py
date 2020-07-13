from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .models import Turnip
from .forms import TurnipForm

# Create your views here.
def registerPage(request):
    context = {}
    return render(request, 'trackerapp/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'trackerapp/login.html', context)

class PriceList(View):
    def get(self, request):
        form = TurnipForm()
        prices = Turnip.objects.all()
        return render (request, 'trackerapp/form.html', context={'form': form, 'prices': prices})

    def post(self, request):
        if request.method =="POST":
            form = TurnipForm(request.POST)
            if form.is_valid():
                print('valid')
                new_price = form.save()
                return redirect('form')
            else:
                print('not valid')
                print(form.errors)
                return redirect('form')

def home(request):
    context = {}
    return render(request, 'trackerapp/home.html', context)

def profile(request):
    context = {}
    return render(request, 'trackerapp/profile.html', context)
