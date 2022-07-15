from django.urls import path, include
from . import views


print('----------------------------------------test urls.py----------------------------------------')
urlpatterns = [
    path('home/', views.ItemListView.as_view(), name='home' ),
    path('item/create/', views.CreateItemView.as_view(), name='create-item'),
    
    path('consumer/create', views.create_new_account, name='consumer-create'),
    path('consumer/login', views.login_view, name='consumer-login'),
    path('consumer/logout', views.logout_view, name='consumer-logout'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    
    
]