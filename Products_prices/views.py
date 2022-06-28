from os import name
from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


class ItemListView(ListView):
    model = Item
    template_name = 'items\items_list.html'
    context_object_name = 'items'
    queryset: Item.objects.all().order_by('supermarket_branch__supermarket')
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ItemListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        context.update({
        'supermarkets' : Supermarket.objects.all(),
        'products': Product.objects.all().order_by('name')
    })
        return context
        


