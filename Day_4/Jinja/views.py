from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def testpaper(request):
    que="who developed python?"
    a="Guido van Rossum"
    b="Elon Musk"
    c="Laveezah Shakir"
    d="Ruchi Jain"
    context={
        'que':que,
        'a':a,
        'b':b,
        'c':c,
        'd':d,
    }
    template=loader.get_template("testpaper.html")
    res=template.render(context,request)
    return HttpResponse(res)
def add(request):
    context={
        'a':12,
        'b':34,
        'c':56,
        'd':a+b+c,
    }
    template=loader.get_template("add.html")
    res=template.render(context,request)
    return HttpResponse(res)


def info(request):
    context={
        'name':'Archana',
        'department':'AIDS',
        'age':19,
    }
    template=loader.get_template("info.html")
    res=template.render(context,request)
    return HttpResponse(res)

def result(request):
    context={
        'name':"Archana Mehra",
        'marks':82,
    }
    return render(request,'result.html',context)

def vote(request):
    context={
        'name':"Archana Mehra",
        'country':"India",
    }
    return render(request,'result.html',context)

def home(request):
   return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
   return render(request,'contact.html')        


