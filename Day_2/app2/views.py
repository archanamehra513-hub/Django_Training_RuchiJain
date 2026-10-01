from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Facebook(request):
    s="<h1>This is the Facebook Page</h1>"
    return HttpResponse(s)
def Linkedin(request):
    s="<h1>This is the Linkedin Page</h1>"
    return HttpResponse(s)    
