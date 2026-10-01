from django.urls import path
from app1 import views

urlpatterns = [
    path("Home/",views.Home),
    path("About/",views.About),
]    