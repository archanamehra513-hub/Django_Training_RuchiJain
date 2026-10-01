from django.db import models

class Product(models.Model):
    poffer = models.FloatField()
    pname = models.CharField(max_length=40)
    pprice = models.FloatField()
    def __str__(self):
        return self.pname
# Create your models here.