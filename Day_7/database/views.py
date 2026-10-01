from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from database.models import Employee
from django.urls import reverse

def newEmployeeForm(request):
    res=render(request,'newEmployeeForm.html')
    return res

def saveuser(request):  #create record (C of CRUD)
    
    eno=request.POST['eno']
    ename=request.POST['ename']
    esal=request.POST['esal']
    emp= Employee(eno=eno,ename=ename,esal=esal)
    emp.save()
    url=reverse('employeelist')
    return HttpResponseRedirect(url)

def employeelist(request):  # read data records (R of CRUD)
    Employees=Employee.objects.all() #it return queryset of object
    res=render(request,'employeelist.html',{'Employees':Employees})
    return res 

def updateEmployeeform(request):
    id=request.GET['id']
    employee=Employee.objects.filter(id=id).values
    res=render(request,'updateEmployeeform.html',{'employee':employee[0]})
    return res 
# Create your views here.

def updateEmployee(request): # read data records (R of CRUD)
    id=request.POST['id']
    eno=request.POST['eno']
    ename=request.POST['ename']
    esal=request.POST['esal']
    Employee(id=id,eno=eno,ename=ename,esal=esal).save
    url=reverse('employeelist')
    return HttpResponseRedirect(url)

def deleteEmployee(request): # delete data records (D of CRUD)
    id=request.GET['id']
    emp=Employee.objects.filter(id=id)
    emp.delete()
    url=reverse('employeelist')
    return HttpResponseRedirect(url)

