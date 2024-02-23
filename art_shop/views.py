# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Selledartworkform


def home(request):
    return HttpResponse(""" <h1>Welcome to our art_blog</h1> """)



# Create your views here.

def index(request):
    return HttpResponse("<h2>This is our Artshop</h2> <br> Here you can buy nice artwork")


def productsView(request):
    pass



def buyproduct(request):
    if request.method == 'POST':
        form = Selledartworkform (request.POST)
        if form.is_valid():
            item_name = form.cleaned_data['item_name']
            item_price = form.cleaned_data['item_price']
            buy_now = form.cleaned_data['buy_now']
            if buy_now:
                # Code to delete the item goes here
                # For example, if you have a model called Item, you can delete it like this:
                # Item.objects.get(name=item_name).delete()
                return render(request, 'thank_you.html')
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})