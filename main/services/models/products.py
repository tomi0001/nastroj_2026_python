from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ...models import Products
from django.db.models import Q

# Create your views here.
class products():
    def selectProduct(self,idUsers :int):
        return Products.objects.filter(id_users_id = idUsers).order_by("name");
    