from django.urls import path
from Products_prices import views
urlpattrens = [
    path('comparison/', views.comparisonView, name='compare-main' ),
    # path(),
]