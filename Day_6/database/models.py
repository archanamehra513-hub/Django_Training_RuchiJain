from django.db import models

# Create your models here.

class Client(models.Model):
    client_id = models.IntegerField()
    client_name = models.CharField(max_length=40)
    client_company = models.CharField(max_length=50)
    def __str__(self):
        return self.client_name

class Customer(models.Model):
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=40)
    customer_contactno = models.IntegerField()
    def __str__(self):
        return self.customer_name

class Order(models.Model):
    order_id = models.IntegerField()
    order_no = models.IntegerField()
    order_price = models.IntegerField()
    def __str__(self):
        return self.client_id