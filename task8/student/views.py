from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse

from student.models import student

from student.models import registration

from django.urls import reverse

# Create your views here.

def home(request):

    return render(request, 'home.html')


def signup(request):

    return render(request, 'signup.html')


def saveuser(request):

    user1 = student()

    u = student.objects.filter(username=request.POST['username'])

    if not u:

        user1.username = request.POST['username']

        user1.password = request.POST['password']

        user1.name = request.POST['name']

        user1.save()

        return HttpResponseRedirect(reverse('login'))

    else:

        return render(request, 'signup.html', {
            'errormsg': 'Username already registered'
        })


def login(request):

    return render(request, 'login.html')


def loginvalidation(request):

    try:

        user1 = student.objects.get(
            username=request.POST['username'],
            password=request.POST['password']
        )

        return HttpResponseRedirect(reverse('home'))

    except student.DoesNotExist:

        return render(request, 'login.html', {
            'erg': 'Invalid Username or Password'
        })


def registration(request):

    return render(request, 'signup.html')


def saveregistration(request):

    user1 = registration()

    u = registration.objects.filter(username=request.POST['username'])

    if not u:

        user1.username = request.POST['username']

        user1.password = request.POST['password']

        user1.name = request.POST['name']

        user1.save()

        return HttpResponseRedirect(reverse('login'))

    else:

        return render(request, 'signup.html', {
            'errormsg': 'Username already registered'
        })


def lrv(request):

    try:

        user1 = registration.objects.get(
            username=request.POST['username'],
            password=request.POST['password']
        )

        return HttpResponseRedirect(reverse('home'))

    except registration.DoesNotExist:

        return render(request, 'login.html', {
            'erg': 'Invalid Username or Password'
        })