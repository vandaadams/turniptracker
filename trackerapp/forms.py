from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Turnip

class TurnipForm(forms.ModelForm):
    class Meta:
        model = Turnip
        fields = [
            'day',
            'time',
            'price'
        ]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
