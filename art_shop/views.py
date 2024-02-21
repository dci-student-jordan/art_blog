# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse(""" <h1>Welcome to our art_blog</h1> """)