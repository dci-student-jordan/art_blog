# Create your views here.
from typing import Any
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .forms import Selledartworkform
from django.views.generic import FormView
from art_api.models import ArtWork
from django.urls import reverse_lazy
# from models import Selledartwork

def home(request):
    return HttpResponse(""" <h1>Welcome to our art_blog</h1> """)



# Create your views here.

def index(request):
    return HttpResponse("<h2>This is our Artshop</h2> <br> Here you can buy nice artwork")


def productsView(request):
    pass



class BuyProduct(FormView):
    template_name = "buy_product.html"
    form_class = Selledartworkform

    def get_item(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(ArtWork, pk=pk)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.item = self.get_item()
        instance.buyer = self.request.user
        instance.save()
        self.success_url = reverse_lazy("art_shop:success", args=[instance.item.pk])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')  # Retrieve the 'pk' from URL kwargs
        context["item"] = get_object_or_404(ArtWork, pk=pk)
        context["form"] = Selledartworkform()
        return context
    # def post:
    #     form = Selledartworkform (request.POST)
    #     if form.is_valid():
    #         item_name = form.cleaned_data['item_name']
    #         item_price = form.cleaned_data['item_price']
    #         buy_now = form.cleaned_data['buy_now']
    #         if buy_now:
    #             # Code to delete the item goes here
    #             # For example, if you have a model called Item, you can delete it like this:
    #             # Item.objects.get(name=item_name).delete()
    #             return render(request, 'thank_you.html')
    # else:
    #     form = Selledartworkform(request.GET)
    # return render(request, 'item_form.html', {'form': form})