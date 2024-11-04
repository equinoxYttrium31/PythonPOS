from django.db import models

# Create your models here.
class Customer(models.Model):
    CustomerName = models.CharField(max_length=100)
    CustomerNumber = models.IntegerField()
    CustomerEmail = models.EmailField()
