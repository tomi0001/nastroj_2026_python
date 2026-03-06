from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ...models import Descriptions
from django.db.models import Q
from datetime import datetime


# Create your views here.
class description():   

    def addDescription(self, request,date):
        user = request.user
        text = request.GET.get("description")
        text.replace("\n", "<br>")
        Description = Descriptions()
        Description.description = text.replace("\n", "<br>")
        Description.date = date;
        Description.id_users_id = user.id
        Description.save();
        return Description.id;
      
    