from django import forms
from .models import Turnip

class TurnipForm(forms.ModelForm):
    class Meta:
        model = Turnip
        fields = [
            'day',
            'time',
            'price'
        ]
