from django.contrib import admin
from django.urls import path
from . import views

app_name = "art_shop"
urlpatterns = [
    path('', views.index),
    path('', views.productsView, name='product'),
    path('', views.buyproduct, name='buyproduct'),
]