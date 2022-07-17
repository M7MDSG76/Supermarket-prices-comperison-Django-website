from django.urls import path, include
from . import views


urlpatterns = [
    path('home/', views.ItemListView.as_view(), name='home' ),
    path('item/create/', views.CreateItem.as_view(), name='create-item'),
    path('consumer/create', views.create_new_account, name='consumer-create'),
    
    # Django authentication system urls.
    path('accounts/', include('django.contrib.auth.urls')),  
]