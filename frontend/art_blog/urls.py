from django.urls import path
from .views import MainPageView, DataListView, DataDetailsView, CommentView


app_name = "art_blog"
urlpatterns = [
    path("", MainPageView.as_view(), name="main_page"),  # Main Page URL
    path("data/", DataListView.as_view(), name="data_list"),  # Data List Page URL
    path(
        "data/<int:pk>/", DataDetailsView.as_view(), name="data_details"
    ),  # Data Details Page URL
    path("comment/", CommentView.as_view(), name="comment_box"),  # Comment Box URL
]
