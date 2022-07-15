from django.urls import path, include
from . import views

# from django.contrib.auth.urls
print('----------------------------------------test urls.py----------------------------------------')
urlpatterns = [
    path('home/', views.ItemListView.as_view(), name='home' ),
    path('item/c/', views.CreateItemView.as_view(), name='create-item'),
    path('item/create/', views.CreateItem.as_view(), name='create-item'),
    path('consumer/create', views.create_new_account, name='consumer-create'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    
]