from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Brand)
class AdminBrand(admin.ModelAdmin):
    fields = ['name']

@admin.register(Supermarket)    
class AdminSupermarket(admin.ModelAdmin):
    fields = ['name']

@admin.register(Catagory)
class AdminCatagory(admin.ModelAdmin):
    fields = ['name']
  
@admin.register(Product)  
class AdminProduct(admin.ModelAdmin):
    fields = ['name','brand_name','catagory_name']
    list_filter = ['brand_name', 'catagory_name']

@admin.register(SupermarketBranch)   
class AdminSupermarketBranch(admin.ModelAdmin):
    fields = ['supermarket','city','neighborhood']
    list_filter = ['supermarket', 'city', 'neighborhood']
 
@admin.register(Item)   
class AdminItem(admin.ModelAdmin):
    fields = ['product', 'supermarket_branch','creator','price']
    list_display = ('product', 'price', 'supermarket_branch', 'creator', )
    list_filter = ['price', 'supermarket_branch', 'creator', 'product', 'register_date']

