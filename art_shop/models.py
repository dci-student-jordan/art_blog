# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
    
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} bought {self.product.name}'