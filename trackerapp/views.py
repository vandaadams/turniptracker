from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Turnip
from .forms import TurnipForm, CreateUserForm

# Create your views here.
def home(request):
    context = {}
    return render(request, 'trackerapp/home.html', context)

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print('VALID')
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')
        else:
            print('NOT VALID')

    context = {'form': form}
    return render(request, 'trackerapp/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid username or password.')

    context = {}
    return render(request, 'trackerapp/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

class PriceList(View):
    def get(self, request):
        form = TurnipForm()
        turnips = Turnip.objects.all()
        morning_prices = [0,0,0,0,0,0]
        evening_prices = [0,0,0,0,0,0]

        for turnip in turnips:
            if request.user == turnip.user:
                if turnip.time == 'M':
                    morning_prices[int(turnip.day)] = turnip.price
                elif turnip.time == 'E':
                    evening_prices[int(turnip.day)] = turnip.price

        return render (request, 'trackerapp/chart.html', context={'form': form,
                                                                  'turnips': turnips,
                                                                  'morning_prices':morning_prices,
                                                                  'evening_prices':evening_prices})

    def post(self, request):
        if request.user.is_authenticated:
            if request.method =="POST":
                form = TurnipForm(request.POST)
                if form.is_valid():
                    print('valid')
                    instance = form.save(commit=False)
                    instance.user = request.user
                    instance.save()
                    return redirect('chart')
        else:
            print('not signed in')
            return redirect('login')

def calculator(request):
    context = {}
    return render(request, 'trackerapp/calculator.html', context)
