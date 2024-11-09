from django.db import models

# Create your models here.
class Customer(models.Model):
    CustomerName = models.CharField(max_length=100)
    CustomerNumber = models.IntegerField()
    CustomerEmail = models.EmailField()

class Menu(models.Model):
    FoodName = models.CharField(max_length=100)
    foodPrice = models.IntegerField()
    foodDescription = models.CharField(max_length=1000)
    foodType = models.CharField(max_length=200)