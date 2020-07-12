from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Turnip(models.Model):
    day_choice = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    )
    day = models.CharField(max_length=10, blank=False, choices=day_choice, default='Monday')
    time_choice = (
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    )
    time = models.CharField(max_length=10, blank=False, choices=time_choice, default='Morning')
    price = models.IntegerField(blank=False, validators=[
            MaxValueValidator(700),
            MinValueValidator(0)
        ])

    def __str__(self):
        return self.day
