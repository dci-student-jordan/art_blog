from django import forms
from .models import Selledartwork

class Selledartworkform (forms.ModelForm):

    class Meta:
        model = Selledartwork
        fields = ["address" , "payment"]
        