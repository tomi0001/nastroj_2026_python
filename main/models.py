from django.db import models
from django.conf import settings
from django.shortcuts import render

# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, logout
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required


class Moods(models.Model):
    class enumMood(models.TextChoices):
        moods = "moods"
        sleep = "sleep"
    id_users = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='moods',    
        on_delete=models.CASCADE,
    )
    # id_users = models.ManyToManyField(User, related_name = 'courses')
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    level_mood = models.FloatField()
    level_anxiety = models.FloatField()
    level_nervousness = models.FloatField()
    level_stimulation = models.FloatField()
    epizodes_psychotik = models.SmallIntegerField(blank=True, null=True)
    what_work = models.TextField(blank=True)
    type = models.CharField(
        max_length=6,
        choices=enumMood.choices,
        default=enumMood.moods,
    )
