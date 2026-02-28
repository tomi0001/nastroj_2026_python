from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Moods
from .models.mood import mood as modelsMood
from .models.sleepType import sleepType as sleepType
from datetime import datetime
import time
from dateutil import parser
from django.conf import settings
from django import forms



# Create your views here.
class sleep():
    def __init__(self):
            
         self.errors = [];
    
    def checkError(self, request):
        ModelsMood = modelsMood()
        dateStart2 = datetime.strptime(request.GET.get("dateStart")  + " " + request.GET.get("timeStart") + ":00" , "%Y-%m-%d %H:%M:%S")
        dateEnd2 = datetime.strptime(request.GET.get("dateEnd")  + " " + request.GET.get("timeEnd") + ":00", "%Y-%m-%d %H:%M:%S")
        if ( not request.GET.get("dateStart") ):
            self.errors.append("Uzupełnij datę zaczęcia");            
        if ( ( not request.GET.get("dateEnd") )):
            self.errors.append("Uzupełnij datę zakończenia");
        if ( ( not request.GET.get("timeStart") )):                    
            self.errors.append("Uzupełnij czas zaczęcia");
        if ( ( not request.GET.get("timeEnd") )):                
            self.errors.append("Uzupełnij czas zakończenia");
        if (ModelsMood.checkTimeExist(request,request.GET.get("dateStart") + " " + request.GET.get("timeStart") , request.GET.get("dateEnd") + " " + request.GET.get("timeEnd")  )):
            self.errors.append("Godziny snu  nachodza na inne sny/nastroje");
        if (dateStart2.timestamp() >= dateEnd2.timestamp()):
            self.errors.append("Godzina zaczęcia jest wieksza bądź równa godzinie skończenia");
        if (int(time.time())  < (dateEnd2.timestamp())):
            self.errors.append("Data skończenia nastroju jest wieksza od teraźniejszej daty");
    
            
        if (  dateEnd2.timestamp() - dateStart2.timestamp() > settings.LONG_SLEEP):
            self.errors.append("Nastroj nie może mieć takiego dużego przedziału czasowego");
        
        if (  dateEnd2.timestamp() - dateStart2.timestamp() < settings.SHORT_SLEEP):
            self.errors.append("Nastroj nie może mieć takiego krótkiego przedziału czasowego");
       
    
    def addSleep(self,request):
        Sleep =  modelsMood();
        idSleep = Sleep.addSleep(request);
        SleepType =  sleepType();
        SleepType.addSleepPercent(request,idSleep);

    