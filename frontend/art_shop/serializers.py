# serializers.py
from rest_framework import serializers
from django.core.exceptions import ValidationError

def validate_size(value):
    if value is None:
        return
    
    allowed_keys = {'height', 'width'}
    for key in value.keys():
        if key not in allowed_keys:
            example = "{'width':22, 'height':33}"
            raise ValidationError(f"Invalid key '{key}' found. Only 'height' and 'width' are allowed.\nProvide in json format, like <{example}>.")

class ArtWorkSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    artist = serializers.CharField(max_length=100)
    image = serializers.ImageField()
    size = serializers.JSONField(allow_null=True, validators=[validate_size])
