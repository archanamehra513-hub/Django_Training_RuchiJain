from django.contrib import admin

from student.models import student

from student.models import registration

admin.site.register(student)

admin.site.register(registration)

# Register your models here.