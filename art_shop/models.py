# Create your models here.    
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Selledartwork(models.Model):
    item = models.PositiveIntegerField()
    buyer = models.ForeignKey(User,on_delete = models.CASCADE)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length = 100)
    payment = models.CharField(max_length = 100, choices = [("Paypal","Paypal") , ("Credit Card","Credit Card") , ("Klarna","Klarna") , ("Bank Transfering","Bank Transfering")])

class ArtworkToSell(models.Model):
    item = models.PositiveIntegerField()
    price = models.PositiveIntegerField()