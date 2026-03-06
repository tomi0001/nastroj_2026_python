from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ...models import Planned_drugs
from django.db.models import Q
from django.db.models import Count

# Create your views here.
class plannedDrugs():
    def selectDose(self,idUsers :int):
        return Planned_drugs.objects.filter(id_users_id = idUsers).distinct("name").order_by("name");
    
    def showPlanedOne(self,request,name :str):
        user = request.user
        return Planned_drugs.objects.filter(id_users_id = user.id).filter(name = name).first();
    
    def showPlanedOneSettings(self,request, name :str):
        user = request.user
        return Planned_drugs.objects.filter(id_users_id = user.id).filter(name = name);
    
    def showName(self,request, id :int):
        user = request.user
        return Planned_drugs.objects.filter(id_users_id =  user.id).filter(id = id).first();

    def selectPlaned(self,request,  namePlaned):
        user = request.user
        return  Planned_drugs.objects.filter(id_users_id = user.id).filter(name  = namePlaned).all();
                                                                           