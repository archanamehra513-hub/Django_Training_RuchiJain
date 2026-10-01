from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Home(request):
    s="<h1>This is the Home Page</h1>"
    return HttpResponse(s)

def About(request): 
    s="<h1>This is the About Page</h1>"   
    return HttpResponse(s)