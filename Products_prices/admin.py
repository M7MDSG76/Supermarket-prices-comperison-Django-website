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

class ItemInline(admin.TabularInline):
    model = Item

@admin.register(Product)  
class AdminProduct(admin.ModelAdmin):
    fields = ['name','brand_name','catagory_name']
    list_filter = ['brand_name', 'catagory_name']
    inlines = [ItemInline]


@admin.register(SupermarketBranch)   
class AdminSupermarketBranch(admin.ModelAdmin):
    fields = ['supermarket','city','neighborhood']
    list_filter = ['supermarket', 'city', 'neighborhood']
   
    
       
@admin.register(Item)   
class AdminItem(admin.ModelAdmin):
    # Fileds in the item view
    fields = ['product', 'supermarket_branch','creator','price',]
    
    # list of attribute displayed in the list item view
    list_display = ('product', 'price', 'get_brach_supermarket', 'creator','get_product_catagory', 'register_date' )
    
    # Filter attribute in the list item view 
    list_filter = ['supermarket_branch__supermarket', 'creator', 'product', 'register_date', 'product__catagory_name', 'register_date']


    # get ManyTOMany field to the admin view 
    @admin.display(description= 'Catagory', ordering= 'product__catagory_name', empty_value='N/A')
    def get_product_catagory(self, obj):
        return obj.product.catagory_name
    
    # get ManyTOMany field to the admin view
    @admin.display(description= 'Supermarket', ordering= 'supermarket_branch__supermarket', empty_value='N/A')
    def get_brach_supermarket(self, obj):
        return obj.supermarket_branch.supermarket
 
  
class ItemInline(admin.TabularInline):
    model: Item
    
    
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget



# class ConsomerForm(forms.ModelForm):
#     class Meta:
#         widgets = {
#             'phone': PhoneNumberPrefixWidget(),
#         }
        
@admin.register(Consumer)
class AdminCunsomer(admin.ModelAdmin):
    fields = ['user', 'first_name', 'last_name', 'email', 'phone_no']
    