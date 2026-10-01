from django.db import models

# Create your models here.

class student(models.Model):

    username = models.CharField(max_length=50, primary_key=True)

    password = models.CharField(max_length=500)

    name = models.CharField(max_length=20)

    def __str__(self):

        return self.username


class registration(models.Model):

    username = models.CharField(max_length=50, primary_key=True)

    password = models.CharField(max_length=500)

    name = models.CharField(max_length=20)

    def __str__(self):

        return self.username