from django.urls import path
from app2 import views

urlpatterns = [
    path("Facebook/",views.Facebook),
    path("Linkedin/",views.Linkedin),
]    