from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateConsumerForm
from .models import *
from .my_validators import user_exists

  
    
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
            else:
                new_user = User.objects.create_user(username= form.cleaned_data['username'], password= form.cleaned_data['password'])

            new_consumer = Consumer.objects.create(user= new_user, first_name= form.cleaned_data['first_name'],
                                                   last_name= form.cleaned_data['last_name'],
                                                   email= form.cleaned_data['email'],
                                                   phone_no= form.cleaned_data['phone_no'],
                                                   )
            return HttpResponseRedirect(reverse('home'))
    
    # If method is get or else 
    else:
        form = CreateConsumerForm()
        
        context = {
            'form': form
            }
        
        return render(request, html_template, context)
        
    
    

