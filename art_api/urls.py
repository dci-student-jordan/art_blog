from django.urls import path
from .views import CreateArtistView, CreateUserView


app_name = "art_api"
urlpatterns = [
    path("register/artist/", CreateArtistView.as_view(), name="register_artist"),
    path("register/user/", CreateUserView.as_view(), name="register_user"),
]