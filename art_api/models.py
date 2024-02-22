from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

def user_directory_path(instance, filename):
    # images will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'images/artist_{0}/{1}'.format(instance.owner.username, filename)

def validate_size(value):
    if value is None:
        return
    
    allowed_keys = {'height', 'width'}
    for key in value.keys():
        if key not in allowed_keys:
            raise ValidationError(f"Invalid key '{key}' found. Only 'height' and 'width' are allowed.")

class ArtWork(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path)
    price = models.PositiveIntegerField()
    size = models.JSONField(null=True, blank=True, validators=([validate_size]))
    voters = models.ManyToManyField(User, related_name='voted_images', blank=True)
    uploade_time = models.DateTimeField(auto_now_add=True)
