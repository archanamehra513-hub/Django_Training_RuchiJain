from django.urls import path
from .views import *

app_name = "myday"

urlpatterns = [
    path('saveuser/', saveuser,name= 'saveuser'),
    path('newProductForm/',newProductForm,name='newProductForm'),
]