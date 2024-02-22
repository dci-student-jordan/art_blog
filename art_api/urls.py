from django.urls import path
from .views import CreateArtistView, CreateUserView, UploadArtWorkView
from django.views.generic import TemplateView


app_name = "art_api"
urlpatterns = [
    path("register/artist/", CreateArtistView.as_view(), name="register_artist"),
    path("register/user/", CreateUserView.as_view(), name="register_user"),
    path("upload/", UploadArtWorkView.as_view(), name="upload"),
    path("uploaded/", TemplateView.as_view(template_name="artwork_uploaded.html"), name="upload_success"),
]