from django.db import models
from django.conf import settings
from django.shortcuts import render
from django.core.validators import MaxValueValidator, MinValueValidator

# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, logout
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required


class Moods(models.Model):
    class enumMood(models.TextChoices):
        moods = "mood"
        sleep = "sleep"
    id_users = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='moods',    
        on_delete=models.CASCADE,
    )
    # id_users = models.ManyToManyField(User, related_name = 'courses')
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    level_mood = models.FloatField(blank=True, null=True)
    level_anxiety = models.FloatField(blank=True, null=True)
    level_nervousness = models.FloatField(blank=True, null=True)
    level_stimulation = models.FloatField(blank=True, null=True)
    epizodes_psychotik = models.PositiveSmallIntegerField(blank=True, null=True)
    what_work = models.TextField(blank=True)
    type = models.CharField(
        max_length=6,
        choices=enumMood.choices,
        default=enumMood.moods,
    )
class Actions(models.Model):
    id_users = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='actions',    
        on_delete=models.CASCADE,
    )
    level_pleasure = models.FloatField()
    name = models.TextField()

class Actions_days(models.Model):
    id_users = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='actions_days',    
        on_delete=models.CASCADE,
    )
    id_actions = models.ForeignKey(Actions,on_delete=models.CASCADE)
    date = models.DateTimeField()
class Actions_plans(models.Model):
    id_users = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='actions_plans',    
        on_delete=models.CASCADE,
    )
    id_actions = models.ForeignKey(Actions,on_delete=models.CASCADE)
    date = models.DateTimeField()
    long = models.PositiveSmallIntegerField(blank=True, null=True)
    what_work = models.TextField(blank=True)
class Descriptions(models.Model):
    id_users = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='descriptions',    
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField()
    description = models.TextField(blank=True)
class Groups(models.Model):
    id_users = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='mainGroups',    
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255) 
class Moods_actions(models.Model):
    id_actions = models.ForeignKey(Actions,on_delete=models.CASCADE)
    id_moods = models.ForeignKey(Moods,on_delete=models.CASCADE)
    percent_executing = models.PositiveSmallIntegerField(blank=True, null=True)
    minute_exe = models.PositiveSmallIntegerField(blank=True, null=True)

class Products(models.Model):
    id_users = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='products',    
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255) 
    how_percent = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    how_much = models.PositiveIntegerField(blank=True, null=True)
    type_of_portion = models.PositiveSmallIntegerField()
      
class Planned_drugs(models.Model):

    id_users = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='planned_drugs',    
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255) 
    portion = models.FloatField()
    id_products = models.ForeignKey(Products,on_delete=models.CASCADE)
  
class Sleep_types(models.Model):

    sleep_flat = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(255)],blank=True, null=True
    )
    sleep_deep = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(255)],blank=True, null=True
    )
    sleep_rem = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(255)],blank=True, null=True
    )
    sleep_working = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(255)],blank=True, null=True
    )
    id_moods = models.ForeignKey(Moods,on_delete=models.CASCADE)


class Substances(models.Model):

    id_users = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='substances',    
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255) 
    equivalent = models.FloatField(blank=True, null=True)
   

class Substances_groups(models.Model):


    id_substances = models.ForeignKey(Substances,on_delete=models.CASCADE)
    id_groups = models.ForeignKey(Groups,on_delete=models.CASCADE)

class Substances_products(models.Model):


    id_substances = models.ForeignKey(Substances,on_delete=models.CASCADE)
    id_products = models.ForeignKey(Products,on_delete=models.CASCADE)
    doseproduct = models.FloatField(blank=True, null=True)
    mg_ug = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(255)],blank=True, null=True
    )

class Usees(models.Model):

    id_users = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='usees',    
        on_delete=models.CASCADE,
    )
    id_products = models.ForeignKey(Products,on_delete=models.CASCADE)
    portion = models.FloatField()
    price = models.FloatField()
    date = models.DateTimeField()

   
class Users_descriptions(models.Model):


    id_usees = models.ForeignKey(Usees,on_delete=models.CASCADE)
    id_descriptions = models.ForeignKey(Descriptions,on_delete=models.CASCADE)
