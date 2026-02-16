from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from ..services.calendar import *
# from ..services.main import *
from django.template.defaulttags import register
from django.contrib.auth.models import User

@register.filter
def get_range(value):
    return range(value)

# Create your views here.
@login_required
def search(request):

    user = request.user 
    style = user.css;
    return render(request,    style.replace("css","html") +  '/search/searchMood/searchMood.html')   
