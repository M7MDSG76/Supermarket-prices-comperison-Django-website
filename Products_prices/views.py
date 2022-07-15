from multiprocessing import context
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import CreateConsumerForm, LoginUserForm
from .models import *
from .my_validators import user_exists
from django.contrib.auth import authenticate, login, logout


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

        
class CreateItemView(CreateView):
    model = Item
    fields = ['product', 'supermarket_branch', 'price', 'creator']
    template_name = 'items/add_item_form.html'
    success_url = reverse_lazy('home')
    

 

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
    
      

