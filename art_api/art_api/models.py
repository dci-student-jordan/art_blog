from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

def user_directory_path(instance, filename):
    # images will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'images/artist_{0}/{1}'.format(instance.artist, filename)


def validate_size(value):
    if value is None:
        return
    
    allowed_keys = {'height', 'width'}
    for key in value.keys():
        if key not in allowed_keys:
            example = "{'width':22, 'height':33}"
            raise ValidationError(f"Invalid key '{key}' found. Only 'height' and 'width' are allowed.\nProvide in json format, like <{example}>.")


class ArtWork(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path)
    size = models.JSONField(null=True, blank=True, validators=([validate_size]))
    uploade_time = models.DateTimeField(auto_now_add=True)
