from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Turnip
from .forms import TurnipForm, CreateUserForm

# Create your views here.
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
