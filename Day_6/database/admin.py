from django.contrib import admin
from database.models import Customer , Order ,Client


# Register your models here.

admin.site.register(Client)
admin.site.register(Customer)
admin.site.register(Order)

