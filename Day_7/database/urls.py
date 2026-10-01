from django.urls import path
from . views import *

urlpatterns = [
    
    path('deleteEmployee/',deleteEmployee,name='deleteEmployee'),
    path('updateEmployee/',updateEmployee,name='updateEmployee'),
    path('employeelist/', employeelist,name='employeelist'),
    path('saveuser/', saveuser,name= 'saveuser'),
    path('newEmployeeForm/',newEmployeeForm,name='newEmployeeForm'),
    path('updateEmployeeForm/',updateEmployeeform,name='updateEmployeeForm'),
]

