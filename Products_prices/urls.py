from django.urls import path, include
from . import views


print('----------------------------------------test urls.py----------------------------------------')
urlpatterns = [
    path('home/', views.ItemListView.as_view(), name='home' ),
    path('item/create/', views.CreateItemView.as_view(), name='create-item'),
]