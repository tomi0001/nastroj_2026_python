from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ...models import Actions
from django.db.models import Q

# Create your views here.
class action():   

    def selectAction(self, idUsers = 0 ):
        
        return Actions.objects.filter( Q(id_users = idUsers) | Q(id_users=0)  ).order_by("id_users").order_by("name")
    