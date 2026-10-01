from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myday.models import Product
from django.urls import reverse

def newProductForm(request):
    res=render(request,'newProductForm.html')
    return res

def saveuser(request):  #create record (C of CRUD)
    
    pprice=request.POST['pprice']
    pname=request.POST['pname']
    poffer=request.POST['poffer']
    emp= Product(pprice=pprice,pname=pname,poffer=poffer)
    emp.save()
    url=reverse('employeelist')
    return HttpResponseRedirect(url)

def home(request):
    return render(request, 'home.html')
