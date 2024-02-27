from django.urls import path
from .views import ArtWorkListAPIView, ArtWorkDetailAPIView, ArtWorkCreateAPIView, ArtWorkRetrieveUpdateDestroyAPIView, get_artwork_image
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('artwork/', ArtWorkListAPIView.as_view(), name='artwork-list'),
    path('artwork/add/', ArtWorkCreateAPIView.as_view(), name='artwork-list-create'),
    path('artwork/alter/<int:pk>/', ArtWorkRetrieveUpdateDestroyAPIView.as_view(), name='artwork-detail'),
    path('artwork/<int:pk>/', ArtWorkDetailAPIView.as_view(), name='artwork-detail'),
    path('artwork/<int:artwork_id>/image/', get_artwork_image, name='get_artwork_image'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]