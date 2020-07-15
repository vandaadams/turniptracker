from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse


from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Turnip, ZingChartSeriesData1, ZingChartConfig
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
        return render (request, 'trackerapp/chart.html', context={'form': form, 'turnips': turnips})

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

#################  chart #################

def data(request):
    # Getting all chart-series data from DB
    oData = ZingChartSeriesData1.objects.all()
    aSeriesPriceData1 = []
    aSeriesDayData1 = []
    response_data = {}
    for e in oData:
        aSeriesPriceData1.append(e.price)
        aSeriesDayData1.append(e.day)
    response_data['days'] = aSeriesDayData1
    response_data['prices'] = aSeriesPriceData1
    return JsonResponse(response_data)

def zingchartConfig(request):
    # Getting all chart-config data from DB
    configData = ZingChartConfig.objects.all()
    response_data = {}
    for e in configData:
        print('e: ', e.title)
        response_data['title'] = e.title
        response_data['xAxis'] = e.xAxis
        response_data['yAxis'] = e.yAxis
        response_data['theme'] = e.theme
    return JsonResponse(response_data)
