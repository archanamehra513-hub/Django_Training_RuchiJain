from django.contrib import admin
from django.urls import path
from colleges import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sistec/", views.sistec, name="sistec"),
    path("lnct/", views.lnct, name="lnct"),
    path("oist/", views.oist, name="oist"),
    path("admin/", admin.site.urls),
]