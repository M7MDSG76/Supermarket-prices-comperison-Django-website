from multiprocessing import context
from urllib import request

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, View

from .forms import CreateConsumerForm, CreateItemForm, LoginUserForm
from .models import *
from .my_validators import user_exists


class ItemListView(ListView):
    model = Item
    template_name = 'items/Home_items_list.html'
    context_object_name = 'items'
    queryset =  Item.objects.all()
    
    
    def get_context_data(self, **kwargs):
        """
        Override the class view context to add 
        products and supermarkets to use it in the data quarying
        """
        # Call the base implementation first to get a context
        context = super(ItemListView, self).get_context_data(**kwargs)
        
        
          
        context.update({
        'supermarkets' : Supermarket.objects.all(),
        'products': Product.objects.all(),  
    })
        return context

        

    
class CreateItem(LoginRequiredMixin,View):
    
    def post(self, request, *args, **kwargs):
        form = CreateItemForm(self.request.POST)
        if form.is_valid():
            
            consumer= Consumer.objects.get(user=self.request.user)
            print(f'-------------{consumer}-------------,')
            item = Item.objects.create(product=form.cleaned_data['product'],
                                       supermarket_branch=form.cleaned_data['supermarket_branch'],
                                       creator=consumer,
                                       price=form.cleaned_data['price'])
        
            return HttpResponseRedirect(reverse('home'))
        context = {
            'form': form
        }
        return render(request, 'items/create.html', context)
    
    
    def get(self, request, *args, **kwargs):
        form = CreateItemForm()
        context = {
            'form': form
        }
        return render(self.request, 'items/create.html', context)
        
    
    pass
    
 

def create_new_account(request):
    
    user = request.user
    html_template= 'consumer/create_consumer_form.html'
    # If the user is registered the view will notice the user.
    if user_exists(user):
        return HttpResponse('this account is already registered!!! \nlogout and try again')
    
    if request.method == 'POST':
        form = CreateConsumerForm(request.POST)
        
        if form.is_valid():
            if form.cleaned_data['email']:
                new_user = User.objects.create_user(username= form.cleaned_data['username'], email= form.cleaned_data['email'], password= form.cleaned_data['password'])
                new_consumer = Consumer.objects.create(user= new_user, first_name= form.cleaned_data['first_name'],
                                                   last_name= form.cleaned_data['last_name'],
                                                   email= form.cleaned_data['email'],
                                                   phone_no= form.cleaned_data['phone_no'],
                                                   )
            else:
                new_user = User.objects.create_user(username= form.cleaned_data['username'], password= form.cleaned_data['password'])
                new_consumer = Consumer.objects.create(user= new_user, first_name= form.cleaned_data['first_name'],
                                                   last_name= form.cleaned_data['last_name'],
                                                   email= form.cleaned_data['email'],
                                                   phone_no= form.cleaned_data['phone_no'],)
            
            # if user is created login.                                       
            if new_user is not None:
                login(request, new_user)
                
            return HttpResponseRedirect(reverse('home'))
        
        #if the form is not valid rerender the form with the errors.
        context = {
            'form': form
        }
        return render(request, html_template, context)
    # If method is get or else 
    else:
        form = CreateConsumerForm()
        
        context = {
            'form': form
            }
        
        return render(request, html_template, context)
        

def login_view(request):
    html_template = 'consumer/login_form.html'
    
    
    if request.user.is_authenticated:
        return HttpResponse('you are already logged in, if you want to loggin with another account please logout and try agian')
    
    if request.method == 'POST':
        
        user = authenticate(request, username= form.cleaned_data['username'], password= form.cleaned_data['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home')) 
        else:
            return HttpResponse('username does not exits!')
        
    
    else:
        form = LoginUserForm()
        
        context = {
            'form': form
       }
        
        return render(request, html_template, context)
     

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
    
      

