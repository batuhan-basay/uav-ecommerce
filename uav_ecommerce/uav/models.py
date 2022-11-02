from unicodedata import category
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=50)

class Products(models.Model):
    model = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    battery = models.CharField(max_length=50)
    is_Active = models.BooleanField(default=True)
    is_Home = models.BooleanField(default=True)
    date = models.DateField()
    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
