from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ...models import Usees
from django.db.models import Q
from datetime import datetime


# Create your views here.
class usee():   

    def selectLastDrugs(self,request, idProduct :int, date :str, dose :float):
        user = request.user 
        dateConvert = datetime.strptime(date,"%Y-%m-%d %H:%M:%S");
        dateConvert2 = datetime.fromtimestamp(dateConvert.timestamp()- 80)
        # datetime.strptime(self.date,"%Y-%m-%d %H:%M:%S");
        return Usees.objects.filter(id_users_id = user.id).filter(id_products_id = idProduct).filter(portion = dose).filter(date__gte =  dateConvert2.strftime("%Y-%m-%d %H:%M:%S")).filter(date__lte  = date).first();
    


    def selectLastDrugsPlaned(self,request, idProduct :int, date :str):
        user = request.user
        dateConvert = datetime.strptime(date,"%Y-%m-%d %H:%M:%S");
        dateConvert2 = datetime.fromtimestamp(dateConvert.timestamp()- 80)
        return Usees.objects.filter(id_users_id =  user.id).filter(id_products_id = idProduct).filter(date__gte = dateConvert2.strftime("%Y-%m-%d %H:%M:%S")).filter(date__lte = date).first();


    def addDrugsPlaned(self,request, name,dose,date,price):
        user = request.user
        Usee = Usees()
        Usee.id_users_id = user.id
        Usee.id_products_id = name;
        Usee.date = date;
        Usee.price = price;
        Usee.portion = dose;
        Usee.save();

        
    # def deleteDrugs( id) {
    #     user = request.user
    #     $Drugs = new self;
    #     $Drugs->where("id",$id)->where("id_users",Auth::User()->id)->delete();
    # }
    def addDrugs(self, request,date,price):
        user = request.user
        Usee = Usees()
        Usee.id_users_id = user.id
        Usee.id_products_id = request.GET.get("nameProduct");
        Usee.date = date;
        Usee.price = price;
        Usee.portion = request.GET.get("dose");
        Usee.save();
        return Usee.id;
       
        
