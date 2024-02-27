from rest_framework import serializers
from .models import ArtWork

class ArtWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtWork
        fields =  ["name", "artist", "image", "pk"]


class ArtWorkDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtWork
        fields =  ["name", "artist", "image", "pk", "owner", "size"]


class AddArtWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtWork
        exclude = ["uploade_time"]