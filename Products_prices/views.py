from os import name
from queue import Empty
from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView

from .forms import NewItemForm

class ItemListView(ListView):
    model = Item
    template_name = 'items\items_list.html'
    context_object_name = 'items'
    queryset =  Item.objects.all()
    
    
    def get_context_data(self, **kwargs):
        
        """
        Override the class view context to add 
        products and supermarkets to use it in the data quarying
        """
        # Call the base implementation first to get a context
        context = super(ItemListView, self).get_context_data(**kwargs)
        
        supermarkets = Supermarket.objects.all()
        products = Product.objects.all()
        
        print(f'supermarkets: \n{supermarkets}')
        print(f'products: \n{products}')
        
        supermarkets_list = []
        products_list = []
        
        for supermarket in supermarkets:
            supermarkets_list.append(supermarket)
        
        for product in products:
            products_list.append(product)
           
                
        context.update({
        'supermarkets' : supermarkets_list,
        'products': products_list,  
    })
        return context

        
class AddItemView(CreateView):
    model = Item
    fields = ['product', 'supermarket_branch', 'price']
    

