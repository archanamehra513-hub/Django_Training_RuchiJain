from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def testpaper(request):
    template = loader.get_template('TestPaper.html')
    res = template.render()
    return HttpResponse(res)