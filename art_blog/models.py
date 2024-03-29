from django.db import models
from django.contrib.auth.models import User
from art_api.models import ArtWork

# Create your models here.


class Comment(models.Model):
    user_fname = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now=True)
    item = models.ForeignKey(ArtWork, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_fname} - {self.message}"
