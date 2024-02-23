# Create your models here.    
from django.db import models
from art_api.models import ArtWork 
from django.contrib.auth.models import User

# Create your models here.

class Selledartwork(models.Model):
    item = models.ForeignKey(ArtWork,on_delete = models.CASCADE)
    buyer = models.ForeignKey(User,on_delete = models.CASCADE)
    address = models.CharField(max_length = 100)
    payment = models.CharField(max_length = 100, choices = [("Paypal","Paypal") , ("Credit Card","Credit Card") , ("Klarna","Klarna") , ("Bank Transfering","Bank Transfering")])
                               