from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Moods
from .models.products import products as product
from .models.planedDrugs import plannedDrugs as planedDrugs
from .models.usee import usee as usee
from datetime import datetime
import time
from dateutil import parser
from django.conf import settings
from django import forms




# Create your views here.
class products():
    def __init__(self):
        self.date :str;
        self.errors = [] 

    def selectProduct(self,idUser):
        Product = product()
        return Product.selectProduct(idUser);
    def selectDose(self,idUsers :int):
        plannedDrugs = planedDrugs()
        return plannedDrugs.selectDose(idUsers);

    def setDate(self,request)  -> bool:
        if (not request.GET.get("date")  and  not request.GET.get("time") ):
            self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True;
        
        elif (bool(not request.GET.get("date"))  ^ bool((not request.GET.get("time") ))):
            return False;
        
        else:
            self.date = request.GET.get("date") + " " + request.GET.get("time")  + ":00";
            return True;
        
    

    def checkError(self,request):
        dateNow = datetime.now()
        # dateNow = dateNow.strftime("%Y-%m-%d %H:%M:%S") 
        dateProduct = datetime.strptime(self.date,"%Y-%m-%d %H:%M:%S");
        Usee = usee()
        error = self.setDate(request);
        if (error == False):
            self.errors.append( "Błędna data");
      
        elif (dateNow.timestamp() < dateProduct.timestamp()):
            self.errors.append("Data wzięcia jest wieksza od teraźniejszej daty");
            
        if (not request.GET.get("nameProduct") and  not request.GET.get("namePlaned") ):
            self.errors.append( "Wpisz nazwę");
            
        if (not request.GET.get("dose")  and not request.GET.get("namePlaned")):
            self.errors.append("Uzupełnij pole dawka");
        
        field = forms.FloatField(required=False,min_value=0.00)
        try:
            mood_level = field.clean(request.GET.get('dose'))
        except forms.ValidationError:
            self.errors.append("Pole dawka musi być numeryczne i większe od 0");

        if (  request.GET.get("nameProduct")  and request.GET.get("dose") and    (Usee.selectLastDrugs(request,request.GET.get("nameProduct"),self.date,request.GET.get("dose")) )):
            self.errors.append("Już wpisałeś ten lek");
            
        # elif (not request.GET.get("nameProduct") ) {
                
        #         $namePlaned = Planned_drug::showName($request->get("namePlaned"));
        #         $showPlaned = Planned_drug::showPlanedOne($namePlaned->name);
        #         if (!empty(Usee::selectLastDrugsPlaned($showPlaned->id_products,$Drugs->date) )) {
        #             self.errors.append($this->error, "Już wpisałeś tą dawkę zaplanowaną");
        #         }
        #     }