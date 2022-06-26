from pyexpat import model
import uuid
from django.db import models
from django.contrib.auth.models import User
import uuid

class Brand(models.Model):
    name= models.CharField(unique=True, max_length=50, help_text= 'Brand name')
    
    def __str__(self):
        return self.name
    
    #def get_abolute_url
    
    
class Supermarket(models.Model):
    name= models.CharField(unique=True, max_length=50, help_text= 'Supermarket name')
    
    def __str__(self):
        return self.name
    
    #def get_abolute_url
    
    
class Catagory(models.Model):
    name= models.CharField(unique=True, max_length=50, help_text= 'Catagory name')
    
    def __str__(self):
        return self.name
    
    #def get_abolute_url
    

class SupermarketBranch(models.Model):
    supermarket= models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    city= models.CharField(max_length= 50, help_text='set the City name', null=True, blank=True, unique=True)
    neighborhood= models.CharField(max_length= 100, help_text='set the Neighborhood name', null=True, blank=True)
    
    def __str__(self):
        if self.city:
            return f'{self.supermarket} - {self.city}'
        return f'{self.supermarket}'
    
    #def get_abolute_url
    
    
class Product(models.Model):
    name= models.CharField(max_length=200, help_text= 'Product name')
    brand_name= models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    catagory_name= models.ForeignKey(Catagory, on_delete=models.SET_NULL, null=True, blank=True)
    
    # size = models.CharField() Choices between ['L', 'ml', 'g', 'KG', ...]
    
    def __str__(self):
        return self.name
    
    # def get_abolute_url(self):
    #     return    
    
class Item(models.Model):
    product= models.ForeignKey(Product, on_delete=models.RESTRICT, null=True, blank=True)
    supermarket_branch= models.ForeignKey(SupermarketBranch, on_delete=models.RESTRICT, null=True, blank=True) 
    creator= models.ForeignKey(User, on_delete=models.CASCADE)
    price= models.DecimalField( max_digits=5, decimal_places=2,)
    register_date= models.DateTimeField(verbose_name='Register date', auto_now_add=True)
    modified_date= models.DateTimeField(verbose_name='Modified date', auto_now=True)
    slug = models.SlugField(unique=True, null=True, blank = True)
    def __str__(self):
        return self.product.name
    
    def get_supermarket(self):
        return self.supermarket_branch.supermarket
    
    #def get_abolute_url


# class ItemLog(models.Model):
#     pass
    
    
    