from django.urls import path, include
from . import views


print('----------------------------------------test urls.py----------------------------------------')
urlpatterns = [
    path('comparison/', views.ItemListView.as_view(), name='home' ),
    # path(),
]