# users/models.py
#from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
#from django.utils import timezone



class User(AbstractUser):
    start_day = models.SmallIntegerField( default=0 )
    css_color = models.CharField( max_length=500, default="light_color")
    css = models.CharField( max_length=500, default="new_style_css")
    level_mood_10 = models.FloatField(null=True)
    level_mood_9 = models.FloatField(null=True)
    level_mood_8 = models.FloatField(null=True)
    level_mood_7 = models.FloatField(null=True)
    level_mood_6 = models.FloatField(null=True)
    level_mood_5 = models.FloatField(null=True)
    level_mood_4 = models.FloatField(null=True)
    level_mood_3 = models.FloatField(null=True)
    level_mood_2 = models.FloatField(null=True)
    level_mood_1 = models.FloatField(null=True)
    level_mood0 = models.FloatField(null=True)
    level_mood1 = models.FloatField(null=True)
    level_mood2 = models.FloatField(null=True)
    level_mood3 = models.FloatField(null=True)
    level_mood4 = models.FloatField(null=True)
    level_mood5 = models.FloatField(null=True)
    level_mood6 = models.FloatField(null=True)
    level_mood7 = models.FloatField(null=True)
    level_mood8 = models.FloatField(null=True)
    level_mood9 = models.FloatField(null=True)
    level_mood10 = models.FloatField(null=True)
