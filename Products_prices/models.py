from cProfile import label
from pydoc import Helper
from queue import Empty
from statistics import mode
from django.db import models

# Create your models here.

class Brand(models.Model):
    name= models.CharField(unique=True, max_length=50, help_text= 'Brand name')
    
    def __str__(self):
        return self.name
    
class Supermarket(models.Model):
    name= models.CharField(unique=True, max_length=50, help_text= 'Supermarket name')

    def __str__(self):
        return self.name
    
class Catagory(models.Model):
    name= models.CharField(unique=True, max_length=50, help_text= 'Catagory name')

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name= models.CharField(max_length=200, help_text= 'Product name')
    brand_name= models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    catagory_name= models.ForeignKey(Catagory, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        if self.brand_name:
            return f'{self.brand_name} {self.name}'
        return self.name
    
class SupermarketBranch(models.Model):
    supermarket= models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    city= models.CharField(max_length= 50, help_text='set the City name', null=True, blank=True)
    neighborhood= models.CharField(max_length= 100, help_text='set the Neighborhood name', null=True, blank=True)
    def __str__(self):
        if self.city:
            return f'{self.supermarket} - {self.city}'
        return self.supermarket
    
class Item(models.Model):
    product= models.ForeignKey(Product, on_delete=models.SET_NULL)
    name= models.CharField(max_length=200, help_text= 'Item name')
    
    