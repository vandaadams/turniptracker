from django.urls import path
from . import views
from .views import PriceList

urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
	path('', views.home, name="home"),
	path('profile/', views.profile, name="profile"),
	path('form/', PriceList.as_view(), name="form")
]
