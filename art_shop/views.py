# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import products


def home(request):
    return HttpResponse(""" <h1>Welcome to our art_blog</h1> """)



# Create your views here.

def index(request):
    return HttpResponse("<h2>This is our Artshop</h2>")


def productsView(request):
    pass



def product_detail(request,id):
    pass



def add_product(request):
    pass


def update_product(request, id):
    pass

def delete_product(request, id):
    pass