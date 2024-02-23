from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "art_shop"
urlpatterns = [
    path('buy/<int:pk>', views.BuyProduct.as_view(), name='buyproduct'),
    path('bought/<int:pk>', TemplateView.as_view(template_name="success.html"), name='success'),
]