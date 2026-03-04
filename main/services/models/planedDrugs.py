from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ...models import Planned_drugs
from django.db.models import Q
from django.db.models import Count

# Create your views here.
class plannedDrugs():
    def selectDose(self,idUsers :int):
        return Planned_drugs.objects.filter(id_users_id = idUsers).distinct("name").order_by("name");
    