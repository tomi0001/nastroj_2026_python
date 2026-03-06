from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ...models import Users_descriptions
from django.db.models import Q
from datetime import datetime


# Create your views here.
class userDescription():   

    def addUserDescription(self,id,idDesriptions):
        Users_description = Users_descriptions()
        Users_description.id_usees_id = id;
        Users_description.id_descriptions_id = idDesriptions;
        Users_description.save();
    