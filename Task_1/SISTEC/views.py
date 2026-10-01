from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    s="<h1>Sagar Institute of Science and Technology (SISTec) is a prominent private technical and professional education institution in Bhopal, Madhya Pradesh, established in 2007 by the Sagar Group.</h1>"
    return HttpResponse(s)
    
    