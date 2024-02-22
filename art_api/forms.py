from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ArtWork
from django.contrib.auth.models import User

class RegisterArtistForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class AddArtworkForm(forms.ModelForm):
    
    class Meta:
        model = ArtWork
        exclude = ["owner", "voters"]

