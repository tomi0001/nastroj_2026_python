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
    