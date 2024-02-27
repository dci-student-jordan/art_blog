from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Comment(models.Model):
    user_fname = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now=True)
    item = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user_fname}: '{self.message}'"

class Vote(models.Model):
    item = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
