from os import name
from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


class ItemListView(ListView):
    model = Item
    template_name = 'items\items_list.html'
    context_object_name = 'items'
    queryset =  Item.objects.all()
    # for item in queryset:
    #     print(f'item: {item},   item supermarket: {item.get_supermarket()}     price: {item.price}', end='\n')
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ItemListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        
        supermarket_items = []
        supermarkets = Supermarket.objects.all()
        for supermarket in supermarkets:
            supermarket_products = []
            products = Product.objects.all()
            
            for product in products:
                
                
                supermarket_item = []
                items = Item.objects.filter(supermarket_branch__supermarket = supermarket, product = product)
                
                for item in items:
                    print(f'added item: {item}, supermarket: {item.supermarket_branch.supermarket}')
                    exist = True
                    for temp_item in supermarket_item:
                        if item.supermarket_branch.supermarket == temp_item.supermarket_branch.supermarket:
                            if item.price < temp_item.price:
                                pass
                            exist = False
                    
                    if exist == True:
                        supermarket_item.append(item)
                    
                    
                supermarket_products.append(supermarket_item)
                
            
            supermarket_items.append(supermarket_products)
        

        
        
        for supermarket in supermarket_items:
            print('supermarket nth:', end=' ')
            for product in supermarket:
                
                for item in product:
                    print(f'{item.price}', end=' ')
            
            print()    
        # for i in supermarket_items:
        #     print(supermarket_items[0])
                
        context.update({
        'supermarkets' : Supermarket.objects.all(),
        'products': Product.objects.all().order_by('name'),
        'supermarket_items': supermarket_items
    })
        return context

        


