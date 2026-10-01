from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def About(request):
    s="<h1>This is the About Page ,offers specialized undergraduate engineering programs in artificial intelligence through its Computer Science departments. </h1>"
    return HttpResponse(s)
    

