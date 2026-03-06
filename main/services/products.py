from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Moods
from .models.products import products as product
from .models.planedDrugs import plannedDrugs as planedDrugs
from .models.usee import usee as usee
from .models.description import description as description
from .models.userDescription import userDescription as userDescription
from datetime import datetime
import time
from dateutil import parser
from django.conf import settings
from django import forms
import logging



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
        plannedDrugs = planedDrugs()
        Product = product()
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
            
        elif (not request.GET.get("nameProduct") ):
                
            namePlaned = plannedDrugs.showName(request,request.GET.get("namePlaned"));
            showPlaned = plannedDrugs.showPlanedOne(request,namePlaned.name);
            if ((Usee.selectLastDrugsPlaned(request,showPlaned.id_products,self.date) )):
                self.errors.append( "Już wpisałeś tą dawkę zaplanowaną");
                
            

    def sumPrice(self,dose, name):
        Product = product()
        select = Product.selectProductId(name)
        if ((not select.price   and not select.how_much ) or select.how_much == 0):
            return 0;
        else:
            return (dose / select.how_much) * select.price;
        
    

    def addDrugs(self, request, date, price):
        Usee = usee()
        id = Usee.addDrugs( request,date,price);
        if ( request.GET.get("description")):
            self.addDescription(request,id,date);
        
        
    def selectPlaned(self,request,namePlaned :str):
         plannedDrugs = planedDrugs()
         list = plannedDrugs.selectPlaned(request,namePlaned);
         return list;
    

    def addPlanedDose(self,request,date):
        logger = logging.getLogger(__name__)
        plannedDrugs = planedDrugs()
        list = self.selectPlaned(request,plannedDrugs.showName(request,request.GET.get("namePlaned")).name);
        for  list2 in list:
            print(f"Debugowanie zmiennej: {float(list2.portion)}")
            price = self.sumPrice(list2.portion,list2.id_products_id);
            result = float((list2.portion)) * float(request.GET.get("dose"));
            print(f"Debugowanie zmiennej: {result}")
            self._addDrugsPlaned(request,list2.id_products_id,result,date,price);

    def _addDrugsPlaned(self,request,name,dose,date,price):
        Usee = usee()
        Usee.addDrugsPlaned(request,name,dose,date,price);

    def addDescription(self, request,id,date):
        descriptions = description()
        idDescriptions = descriptions.addDescription( request,date);
        userDescriptions = userDescription()
        userDescriptions.addUserDescription( id,idDescriptions);
    