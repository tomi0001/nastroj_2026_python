from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..services.calendar import *
from ..services.main import *
from ..services.mood import *
from django.template.defaulttags import register
from django.contrib.auth.models import User
from datetime import datetime
from datetime import datetime, timedelta
import time

@register.filter
def get_range(value):
    return range(value)

# Create your views here.
@login_required
def main(request,year="",month="",day=""):
    Calendar = calendar(request,year,month,day)
    user = request.user 
    style = user.css;
    tomorrow = datetime.now() + timedelta(days=1)
    return render(request,    style.replace("css","html") +  '/main/main.html',{ 'text_month': Calendar.text_month ,
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
                                "date": str(Calendar.year) + "-" + str(Calendar.month) + "-" +  str(Calendar.day), 
                                "tomorrow": tomorrow
                                }
    )
def addMoodSubmit(request):
                # Mood = new serviceMood;
            Mood = mood()
            user = request.user 
            style = user.css;
            print (request.GET.get('timeStart'))
            # return render(request,    style.replace("css","html") +  '/main/ajax/error.html',{ 'error': request.GET.get('timeStart') })
            # username = request.GET.get('timeStart')
            if (not request.GET.get('timeStart')  ):
                timeStart = Mood.selectLastMoods(request)
                if (timeStart ==0):
                     return render(request,    style.replace("css","html") +  '/main/ajax/error.html',{ 'error': ["Uzupełnij datę zaczęcia"] })
                     
                # if ( not timeStart.date_end):
                #     return render(request,    style.replace("css","html") +  '/main/ajax/error.html',{ 'error': ["uzupełnij czas zaczęcia"] })
                # else:
                # timeStart = timeStart[0].date_end
                # try:
                #      obj = timeStart.date_end
                # except IndexError:
                #      obj = None 
                


                # for timeS in timeStart:
                timeStart =  timeStart.date_end.strftime("%Y-%m-%d %H:%M:%S") 
                
                
            
            else:
                timeStart = request.GET.get('dateStart') + " " +  request.GET.get("timeStart") + ':00';
            
            if (request.GET.get("timeEnd") == ""):
                 dateNow = datetime.now()
                 timeEnd = dateNow.strftime("%Y-%m-%d %H:%M:%S")
                #  timeEnd = date("Y-m-d H:i")
            else:
                timeEnd = request.GET.get("dateEnd") + " " +  request.GET.get("timeEnd") + ':00';
            print (timeStart)
            # return render(request,    style.replace("css","html") +  '/main/ajax/error.html',{ 'error': timeStart })
            
            # $Mood->setVariableMood($request);
            # Mood.convertValue(request);
            Mood.checkError(timeStart,timeEnd,request);
            Mood.checkAddMood(request);
            
            # if (!empty($request->get("idActions")) ) {
            #     $Mood->checkErrorAction($request,round(((StrToTime($timeEnd) - StrToTime($timeStart)) /60 ),2) );
            # }
            if (len(Mood.errors) != 0):
                return render(request,    style.replace("css","html") +  '/main/ajax/error.html',{ 'error': Mood.errors })
            else:
                id = Mood.saveMood(request,timeStart,timeEnd);
            
             

            # if (!empty($request->get("idAction"))) {
            #         $Mood->saveAction($request,$id);
            #              Mood.saveMood(request)
            # } 
            return render(request,    style.replace("css","html") +  '/main/f.html')
