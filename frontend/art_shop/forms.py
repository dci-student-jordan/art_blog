from django import forms
from .models import Selledartwork
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .serializers import ArtWorkSerializer, validate_size
import requests
from django.conf import settings

class Selledartworkform (forms.ModelForm):

    class Meta:
        model = Selledartwork
        fields = ["address" , "payment"]


class RegisterArtistForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']


class AddArtworkForm(forms.Form):
    name = forms.CharField(max_length=100)
    artist = forms.CharField(max_length=100)
    image = forms.ImageField()
    size = forms.JSONField(required=False, validators=([validate_size]))

    def save(self):
        serializer = ArtWorkSerializer(data=self.cleaned_data)
        if serializer.is_valid():
            # Send the data to the remote server using an API request
            # Example: Use requests library to send a POST request
            response = requests.post(settings.ART_API_URL+"artwork/add/", data=serializer.validated_data)
            if response.status_code == 201:
                return response.json()
            else:
                print("FORM SAVE response:", response.content, response.headers)
        else:
            print("FORM INVALID:", response.content, response.headers)
        return None
