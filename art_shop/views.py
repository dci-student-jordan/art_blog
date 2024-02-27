# Create your views here.
from typing import Any
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .forms import Selledartworkform
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import RegisterArtistForm, RegisterUserForm, AddArtworkForm
from dotenv import load_dotenv
from datetime import datetime
from os import getenv
import requests
import jwt
from django.conf import settings

# Create your views here.

class CreateArtistView(FormView):
    template_name = "registration/register_artist.html"
    form_class = RegisterArtistForm
    success_url = reverse_lazy('art_blog:main_page')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_staff = True
        user.save()
        return super().form_valid(form)



class CreateUserView(FormView):
    template_name = "registration/register_user.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy('art_blog:main_page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def add_artwork(request):
    if request.method == 'POST':
        form = AddArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            # Get or refresh the access token
            access_token = get_or_refresh_access_token()

            # Construct the request to the art API
            url = settings.ART_API_URL+"artwork/add/"
            headers = access_token
            data = {
                "name": form.cleaned_data['name'],
                "owner": "ARTshop",
                "artist": form.cleaned_data['artist'],
                "size": form.cleaned_data['size']
            }

            files = {'image': request.FILES['image']}

            print("DATA:", data)
            # Send the POST request to the art API
            response = requests.post(url, data=data, files=files, headers=headers)
            if response.status_code == 201:
                return redirect('success_url')  # Redirect to a success page
            else:
                print(response.content)
                print(response.status_code)
                print(response.headers)

                # Handle the case where the request fails
                return render(request, 'upload_artwork.html', {'form': form})
    else:
        form = AddArtworkForm()
    return render(request, 'upload_artwork.html', {'form': form})


# class UploadArtWorkView(FormView):
    # template_name = "upload_artwork.html"
    # form_class= AddArtworkForm
    # success_url = reverse_lazy("art_api:upload_success")

    # def form_valid(self, form):
    #     instance = form.save(commit=False)
    #     instance.owner = self.request.user
    #     instance.save()
    #     return super().form_valid(form)


def home(request):
    return HttpResponse(""" <h1>Welcome to our art_blog</h1> """)


def index(request):
    return HttpResponse("<h2>This is our Artshop</h2> <br> Here you can buy nice artwork")


# class BuyProduct(FormView):
#     template_name = "buy_product.html"
#     form_class = Selledartworkform

#     def get_item(self):
#         pk = self.kwargs.get('pk')
#         return get_object_or_404(ArtWork, pk=pk)

#     def form_valid(self, form):
#         instance = form.save(commit=False)
#         instance.item = self.get_item()
#         instance.buyer = self.request.user
#         instance.save()
#         self.success_url = reverse_lazy("art_shop:success", args=[instance.item.pk])
#         return super().form_valid(form)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.user.is_authenticated:
#             context["headers"] = get_or_refresh_access_token()
#         pk = self.kwargs.get('pk')  # Retrieve the 'pk' from URL kwargs
#         context["item"] = get_object_or_404(ArtWork, pk=pk)
#         context["form"] = Selledartworkform()
#         return 
    
def get_or_refresh_access_token():
    load_dotenv()
    access_token = getenv("ACCESS_TOKEN")
    print("ACCESS:", access_token)
    
    headers = {'Authorization': f'Bearer {access_token}'}
    
    try:
        # Decode the access token to get its payload
        token_payload = jwt.decode(access_token, options={"verify_signature": False})
        expiration_timestamp = token_payload.get('exp')
        
        if expiration_timestamp and expiration_timestamp > datetime.utcnow().timestamp():
            print("Access token valid")
            return headers
    except jwt.ExpiredSignatureError:
        pass  # Token has expired
    
    refresh_token = getenv("REFRESH_TOKEN")
    response = requests.post('http://127.0.0.1:8001/art_api/token/refresh/', data={'refresh': refresh_token})
    
    if response.status_code == 200:
        new_access_token = response.json()['access']
        print("New access token obtained")
        headers = {'Authorization': f'Bearer {new_access_token}'}
        return headers
    else:
        print("Failed to refresh token:", response.content)
        return headers