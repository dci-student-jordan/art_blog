from django import forms
from .models import Selledartwork

class Selledartworkform (forms.Form):
    class Meta:
        model = Selledartwork
        fields = ["address" , "payment"]
        