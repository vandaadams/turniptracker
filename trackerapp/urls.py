from django.urls import path
from . import views
from .views import PriceList

urlpatterns = [
	path('', views.home, name="home"),
	path('profile/', views.profile, name="profile"),
	path('form/', PriceList.as_view(), name="form")
]
