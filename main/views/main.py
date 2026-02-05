from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..services.calendar import *
from ..services.main import *
from django.template.defaulttags import register

@register.filter
def get_range(value):
    return range(value)

# Create your views here.
@login_required
def main(request,year="",month="",day=""):
    Calendar = calendar(request,year,month,day)
    return render(request,    'main/main.html',{ 'text_month': Calendar.text_month ,
                                                "year" :Calendar.year,
                                "day2": 1,
                                "day1": 1,
                                "how_day_month": Calendar.how_day_month,
                                "day_week": Calendar.day_week,
                                "day3" :Calendar.day ,
                                "month": Calendar.month,
                                "back" :Calendar.back_month,
                                "next": Calendar.next_month,
                                "back_year":  Calendar.back_year,
                                "next_year": Calendar.next_year,
                                "date": str(Calendar.year) + "-" + str(Calendar.month) + "-" +  str(Calendar.day)
                                }
    )   
