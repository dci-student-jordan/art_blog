from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import ArtWork
from .serializers import ArtWorkSerializer, ArtWorkDetailSerializer, AddArtWorkSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.conf import settings
from django.http import HttpResponse

from .permissions import IsStaffUser

class ArtWorkListAPIView(generics.ListAPIView):
    queryset = ArtWork.objects.all()
    serializer_class = ArtWorkSerializer

class ArtWorkDetailAPIView(generics.RetrieveAPIView):
    queryset = ArtWork.objects.all()
    serializer_class = ArtWorkDetailSerializer
    authentication_classes = []

def get_artwork_image(request, artwork_id):
    artwork = ArtWork.objects.get(pk=artwork_id)
    image_data = artwork.image.read()  # Read the image binary data
    return HttpResponse(image_data, content_type='image/jpeg')  # Adjust content type if necessary


class ArtWorkCreateAPIView(generics.CreateAPIView):
    queryset = ArtWork.objects.all()
    serializer_class = AddArtWorkSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated, IsStaffUser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("ART_API add VIEW serializer invalid")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtWorkRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArtWork.objects.all()
    serializer_class = ArtWorkSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated, IsStaffUser]