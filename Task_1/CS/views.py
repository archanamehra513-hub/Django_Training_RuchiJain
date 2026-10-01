from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Contact(request):
    s="<h1>This is the Contact Page</h1>"
    return HttpResponse(s)

