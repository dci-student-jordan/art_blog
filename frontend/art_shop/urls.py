from django.contrib import admin
from django.shortcuts import HttpResponse
from django.urls import path
from .views import CreateArtistView, CreateUserView, add_artwork
from django.views.generic import TemplateView
from . import views

app_name = "art_shop"
urlpatterns = [
    path('buy/<int:pk>', lambda request: HttpResponse("<p>Not implemented yet</p>"), name='buyproduct'),
    path('bought/<int:pk>', TemplateView.as_view(template_name="success.html"), name='success'),
    path("register/artist/", CreateArtistView.as_view(), name="register_artist"),
    path("register/user/", CreateUserView.as_view(), name="register_user"),
    path("upload/", add_artwork, name="upload"),
    path("uploaded/", TemplateView.as_view(template_name="artwork_uploaded.html"), name="upload_success"),
]